# analysis docred unconstrained recheck

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_docred_unconstrained_recheck_20260514T131743_result.json`
- **Structured JSON:** [`138fed986522de8ac4f6.json`](../../sessions/13/138fed986522de8ac4f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。汇报如下：

---

## 1. GPU 状态
| GPU | 型号 | 利用率 | 显存 | 状态 |
|-----|------|--------|------|------|
| 0 | RTX PRO 6000 Blackwell | 0% | 0/97887 MiB | **空闲** |
| 1 | RTX PRO 6000 Blackwell | 85% | 17535/97887 MiB | **占用** (semantic_only) |

## 2. 实验完成状态
| 实验 | 状态 | 行数 |
|------|------|------|
| `docred_unconstrained.jsonl` | **已完成** | 998 |
| `docred_semantic_only.jsonl` | **运行中** (820/998) | 837 (已输出) |
| `docred_full_s1.jsonl` | **已完成** (EXIT_CODE=0) | 998 |

## 3. 去重结果
- `docred_unconstrained.jsonl`: 998 lines, 998 unique doc_ids, **无重复**
- `docred_semantic_only.jsonl`: 837 lines, 837 unique doc_ids, **无重复**

## 4. Unconstrained Violation Metrics — Phase 2 重新分析

| Metric | OLD (错误文件) | **NEW (正确)** | 差异 |
|--------|---------------|----------------|------|
| Documents checked | 962 | **986** | +24 |
| Parse failures | 36 | **12** | -24 |
| Entities | 19099 | **20171** | +1072 |
| Triples | 16540 | **17497** | +957 |
| **DR%** | 18.7% | **18.5%** | -0.2pp |
| **RV%** | 28.9% | **29.7%** | +0.8pp |
| **ET%** | 7.5% | **8.2%** | +0.7pp |
| **CF%** | n/a | **0.10%** | — |

确认：OLD 报告数字与新数字不同，说明之前确实用了错误文件（parse failures 差异尤为明显：36 vs 12）。

## 5. F1 Metrics

| Metric | Unconstrained | Full_S1 |
|--------|--------------|---------|
| Entity P | 0.5726 | 0.5845 |
| Entity R | 0.5831 | 0.5963 |
| **Entity F1** | **0.5778** | **0.5904** |
| Relation P | 0.0931 | 0.0699 |
| Relation R | 0.0935 | 0.0991 |
| **Relation F1** | **0.0933** | **0.0820** |

## 6. Semantic Only — 未完成
进度 820/998，预计还需 ~1.5h 完成。完成后需同样运行 violation checker + F1 评估。

## 7. 全模式对比表

| Mode | DR% | RV% | ET% | CF% | Triples | Ent F1 | Rel F1 |
|------|-----|-----|-----|-----|---------|--------|--------|
| **Unconstrained** (Phase 2 新) | 18.5 | 29.7 | 8.2 | 0.10 | 17497 | 0.5778 | 0.0933 |
| Grammar Only | 26.2 | 0.0 | 0.0 | — | 17341 | — | — |
| Full S1 | 10.2 | 0.0 | 0.0 | 2.57 | 17372 | 0.5904 | 0.0820 |
| Semantic Only | *(运行中)* | | | | | | |

报告已保存至服务器：
- `outputs/violation_report_docred_unconstrained_phase2.json`
- `outputs/f1_report_docred_unconstrained_phase2.json`

---
