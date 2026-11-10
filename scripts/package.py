"""Build portable Markdown-only skill ZIPs using the Python standard library."""
from pathlib import Path
import re
import zipfile

REPO = Path(__file__).resolve().parents[1]


def skill_files(root):
    root = Path(root)
    if root.is_symlink():
        raise ValueError('Symlink root is not allowed')
    files = []
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise ValueError('Symlinks are not allowed')
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if rel != Path('SKILL.md') and not (
            len(rel.parts) == 2 and rel.parts[0] == 'references' and path.suffix == '.md'
        ):
            raise ValueError(f'Unexpected skill file: {rel}')
        files.append(path)
    entry = root / 'SKILL.md'
    if entry not in files:
        raise ValueError('Missing SKILL.md')
    text = entry.read_text(encoding='utf-8')
    if not text.startswith('---\n') or len(text.split('---', 2)) != 3:
        raise ValueError('Missing frontmatter')
    if not re.search(r'^name: empresa-online-portugal$', text.split('---', 2)[1], re.M):
        raise ValueError('Unexpected skill identity')
    for path in files:
        for href in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if href.startswith('https://'):
                continue
            target = (path.parent / href).resolve()
            if not target.is_relative_to(root.resolve()) or not target.is_file():
                raise ValueError(f'Invalid local reference: {href}')
    return files


def package_skill(root, destination):
    root, destination = Path(root), Path(destination)
    files = skill_files(root)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            name = 'empresa-online-portugal/' + path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(name)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    return destination


if __name__ == '__main__':
    for language in ('pt', 'en'):
        out = package_skill(REPO / 'skills' / language / 'empresa-online-portugal',
                            REPO / 'dist' / f'empresa-online-portugal-{language}.zip')
        print(out.relative_to(REPO))
