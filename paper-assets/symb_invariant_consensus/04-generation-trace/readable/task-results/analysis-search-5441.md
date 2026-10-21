# analysis search 5441

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_search-5441_20260520T141452_result.json`
- **Structured JSON:** [`72926efd7702f41c03aa.json`](../../sessions/72/72926efd7702f41c03aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件权限均为 644（可写），无只读文件。

以下是完整的搜索结果，按文件分类：

---

## "54.41" 出现在 .tex 文件中的位置

### `docs/paper/experiments.tex`
| 行号 | 内容 |
|------|------|
| 37 | `Mistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\` |
| 40 | `Mistral-7B & FOLIO (s789) & 204 & 54.41 & 53.92 & $-$0.49 & 1.000 \\` |

### `docs/paper/analysis.tex`
| 行号 | 内容 |
|------|------|
| 30 | `Mistral-7B (s123) & FOLIO & 0.49 & 1.88 & 54.41 & $+$2.94 \\` |
| 31 | `Mistral-7B (s789) & FOLIO & 0.41 & 2.17 & 54.41 & $-$0.49 \\` |
| 98 | `& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\` |

### `docs/paper/diagnosis.tex`
| 行号 | 内容 |
|------|------|
| 20 | `Mistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\` |
| 23 | `Mistral-7B & FOLIO (s789) & 204 & 54.41 & 53.92 & $-$0.49 & 1.000 \\` |
| 76 | `Mistral-7B (s123) & FOLIO & 0.49 & 1.88 & 54.41 & $+$2.94 \\` |
| 77 | `Mistral-7B (s789) & FOLIO & 0.41 & 2.17 & 54.41 & $-$0.49 \\` |
| 151 | `& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\` |

### `docs/paper/solutions.tex`
| 行号 | 内容 |
|------|------|
| 11 | `...below SC's 54.41\% baseline. Combo mode at $w{=}1$...` |

### `docs/paper/figures/gen_f6_kappa_accuracy_scatter.py`
| 行号 | 内容 |
|------|------|
| 26 | `m_acc = [38.24, 54.41, 56.86, 51.96]` |

**共 12 处**（.tex 11 处 + .py 1 处）

---

## "55.88" 已存在于 .tex 文件中的位置（新值）

### `docs/paper/experiments.tex`
| 行号 | 内容 |
|------|------|
| 38 | `Mistral-7B & FOLIO & 204 & 55.88 & \textbf{59.31} & $+$3.43 & 0.092 \\` |
| 39 | `Mistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\` |
| 58 | `Mistral-7B & FOLIO & 204 & 55.88 & \textbf{85.78} & $\mathbf{+29.90}$...` |
| 65 | (oracle 相关行) |

### `docs/paper/analysis.tex`
| 行号 | 内容 |
|------|------|
| 28 | `Mistral-7B (s456) & FOLIO & 0.51 & 1.82 & 55.88 & 0.00 \\` |
| 29 | `Mistral-7B & FOLIO & 0.50 & 1.84 & 55.88 & $+$3.43 \\` |

### `docs/paper/diagnosis.tex`
| 行号 | 内容 |
|------|------|
| 21 | `Mistral-7B & FOLIO & 204 & 55.88 & \textbf{59.31} & $+$3.43 & 0.092 \\` |
| 22 | `Mistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\` |
| 74-75 | kappa 表中 s456 和 primary seed 行 |
| 112 | T sensitivity 分析段落 |

### `docs/paper/appendix.tex`
| 行号 | 内容 |
|------|------|
| 464, 469, 475, 477 | K-sensitivity 图表说明中引用 SC=55.88% |

---

## "54.41" 出现在 .md/.yaml/.py 文件中的位置（非论文，供参考）

| 文件 | 行号 | 说明 |
|------|------|------|
| `paper_framing.md` | 69, 93, 187, 201, 273, 289 | 实验记录/分析 |
| `decisions.yaml` | 999, 1040, 1413, 1421, 1717, 1816-1817 | 决策日志 |
| `registry.yaml` | 2756, 3576, 3656, 3670, 5562, 5670, 5701, 5707, 5709 | 实验注册表 |
| `paper_provenance.yaml` | 939, 1061, 2491, 2584 | 论文溯源 |
| `memory.md` | 110, 124 | 项目记忆 |
| `task_context/agent.md` | 41 | 任务上下文 |
| `direction_f_blind_fol.py` | 5, 390, 423, 424 | 实验脚本（硬编码 baseline） |
| `artifacts/summarize_k_sensitivity.py` | 36 | 分析脚本 |
| `artifacts/analyze_seed_replication.py` | 39 | 分析脚本 |
| `artifacts/exp-013-constraint-ablation/data/constraint_ablation_summary.txt` | 13 | 实验报告 |
| `artifacts/fleiss_kappa_unified_merged.json` | 122, 140, 238 | 数据文件 |
| `artifacts/exp-046/report/exp046_analysis.md` | 51 | 实验报告 |
| `artifacts/manifest.yaml` | 1795, 1846 | 产出清单 |

**所有文件权限均为 644，无只读文件。**

---
