# Registo de trabalho local

## Guardar e retomar

Use por defeito `.empresa-online/<caso>/registo.md` na pasta de trabalho local privada. Use um identificador neutro, por exemplo `caso-2026-11-10-01`, sem NIF ou nome pessoal no caminho. Não escreva dentro da skill instalada. Se houver repositório Git, crie `.empresa-online/.gitignore` com `*` para excluir os registos; nunca os inclua em commits ou pacotes partilhados. Isto evita controlo de versões, mas não torna uma pasta partilhada privada: numa pasta pública, sincronizada com terceiros ou com acesso inadequado, use uma localização privada autorizada. Se não conseguir guardar, explique o impedimento concreto sem afirmar que existe persistência.

No arranque procure o registo nesta pasta antes de voltar a perguntar. Havendo vários casos, peça apenas qual retomar. Leia decisões, evidência, documentos e próxima ação. Confirme o estado atual do pedido no portal; não repita o questionário nem confunda estado histórico com estado atual. Reuse aprovações registadas no seu âmbito, respeitando as regras da plataforma; alterações materiais exigem revisão.

Atualize no mesmo ficheiro quando houver decisão, alteração de documento, intervenção da pessoa, resultado do portal ou interrupção. Evite um diário de cliques. Registe os dados mínimos para retomar e caminhos locais dos documentos, sem PIN, códigos temporários, URLs de sessão ou cópias de identificação. Identificadores completos só quando indispensáveis, em armazenamento privado; de preferência mantenha referências locais aos documentos.

## Modelo

```markdown
# Caso <identificador>
Atualizado: <data, hora e fuso>
Fase: <estado verificado>
Pedido: <referência privada se existir; caso contrário, não iniciado>
Última evidência: <portal/documento/declaração da pessoa, com data>

## Ficha
| Campo | Valor | Confirmado / proposta / falta | Origem/data |
| --- | --- | --- | --- |

## Decisões e autorizações
| Decisão/ação | Conteúdo aprovado e âmbito | Quem/quando | Precisa de revisão? |
| --- | --- | --- | --- |

## Documentos e tarefas
| Documento/tarefa | Versão/caminho privado | Interveniente | Estado/evidência |
| --- | --- | --- | --- |

## Pendências
| Tarefa | Bloqueia o quê? | Responsável | Próxima ação/prazo e origem |
| --- | --- | --- | --- |

## Retomar daqui
<Próxima ação concreta; o que pode continuar independentemente.>

## Plano pós-registo
| Obrigação | Data de origem | Prazo / por confirmar | Responsável | Comprovativo/estado |
| --- | --- | --- | --- | --- |
Continuação pós-registo autorizada: <não solicitada / decisão da pessoa e âmbito>
```

Não preencha valores inexistentes para completar o modelo. Depois da aprovação, guarde o plano e pergunte se deve continuar; sem essa decisão, as ações seguintes ficam planeadas, não executadas.
