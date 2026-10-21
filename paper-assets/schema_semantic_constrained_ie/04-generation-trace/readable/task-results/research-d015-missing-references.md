# research d015 missing references

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d015_missing_references_20260514T223133_result.json`
- **Structured JSON:** [`34c80590b3ab68a0f9fe.json`](../../sessions/34/34c80590b3ab68a0f9fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有编辑完成。汇总：

### 已有（无需操作）
| 引用 | Cite key | 状态 |
|------|----------|------|
| NeuroLogic (Lu et al., NAACL 2021) | `lu2021neurologic` | bib 已有，但 §6 未引用 → **已补入** P3 vocabulary constraint 列表 |

### 新增 bib entries（5 条）
| 引用 | Cite key | Venue |
|------|----------|-------|
| Guidance | `guidance2023` | GitHub / Microsoft Research, 2023 |
| TANL | `paolini2021tanl` | ICLR 2021 |
| REBEL | `cabot2021rebel` | Findings of EMNLP 2021 |
| TKRL | `xie2016tkrl` | IJCAI 2016 |
| SGD | `rastogi2020sgd` | AAAI 2020 |

### §6 正文引用插入（4 处）
| 位置 | 插入内容 |
|------|----------|
| P1 Grammar-Constrained Decoding | `Guidance~\cite{guidance2023}` 加入工具列表 |
| P3 Vocabulary and Type-Constrained | `NeuroLogic~\cite{lu2021neurologic}` 加入 vocabulary constraint 列表 |
| P3 Vocabulary and Type-Constrained | `; see also~\cite{xie2016tkrl}` 附在 Roth & Yih ILP 句后 |
| P4 Structural Constraints via Training | `TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}` 加入 seq2seq IE 列表 |

### 未加入 §6 正文
- **SGD** (`rastogi2020sgd`): bib 已添加，但 SGD 是对话系统工作，与 IE 段落无自然契合点，未强行插入。如需引用可放在 P4 或 closing paragraph。

---
