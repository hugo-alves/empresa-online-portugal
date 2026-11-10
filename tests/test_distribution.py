"""Distribution tests, not agent-behavior or real-incorporation tests."""
import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest
import zipfile

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('package', REPO / 'scripts/package.py')
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)


class DistributionTests(unittest.TestCase):
    def copied_skill(self, temp):
        return Path(shutil.copytree(REPO / 'skills/pt/empresa-online-portugal',
                                    Path(temp) / 'empresa-online-portugal'))

    def test_both_languages_are_portable_and_share_sources(self):
        sources = []
        with tempfile.TemporaryDirectory() as temp:
            for lang in ('pt', 'en'):
                root = REPO / 'skills' / lang / 'empresa-online-portugal'
                files = package.skill_files(root)
                sources.append(set(re.findall(r'https://[^)\s`]+',
                                               '\n'.join(p.read_text() for p in files))))
                out = package.package_skill(root, Path(temp) / f'{lang}.zip')
                with zipfile.ZipFile(out) as archive:
                    self.assertIsNone(archive.testzip())
                    expected = {'empresa-online-portugal/' + p.relative_to(root).as_posix():
                                p.read_bytes() for p in files}
                    self.assertEqual(set(archive.namelist()), set(expected))
                    for name, data in expected.items():
                        self.assertEqual(archive.read(name), data)
            self.assertEqual(sources[0], sources[1])

    def test_case_record_contamination_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.copied_skill(temp)
            private = root / '.empresa-online/synthetic-case'
            private.mkdir(parents=True)
            (private / 'registo.md').write_text('SYNTHETIC PRIVATE SENTINEL')
            out = Path(temp) / 'distribution.zip'
            with self.assertRaises(ValueError):
                package.package_skill(root, out)
            self.assertFalse(out.exists())

    def test_external_reference_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.copied_skill(temp)
            (Path(temp) / 'outside.md').write_text('synthetic outside material')
            with (root / 'SKILL.md').open('a') as file:
                file.write('\n[outside](../outside.md)\n')
            with self.assertRaises(ValueError):
                package.skill_files(root)

    def test_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.copied_skill(temp)
            (root / 'references/linked.md').symlink_to(root / 'SKILL.md')
            with self.assertRaises(ValueError):
                package.skill_files(root)

    def test_repeated_build_is_identical(self):
        with tempfile.TemporaryDirectory() as temp:
            root = REPO / 'skills/en/empresa-online-portugal'
            a = package.package_skill(root, Path(temp) / 'a.zip')
            b = package.package_skill(root, Path(temp) / 'b.zip')
            self.assertEqual(a.read_bytes(), b.read_bytes())


if __name__ == '__main__':
    unittest.main()
