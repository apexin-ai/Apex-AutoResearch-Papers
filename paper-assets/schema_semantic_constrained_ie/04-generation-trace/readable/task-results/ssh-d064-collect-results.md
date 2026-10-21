# ssh d064 collect results

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d064_collect_results_20260519T101822_result.json`
- **Structured JSON:** [`1a02466a9e82797db886.json`](../../sessions/1a/1a02466a9e82797db886.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验仍在运行中，远未完成。** 当前状态：

### GPU 0 — Llama 流水线
| 阶段 | 状态 | 进度 |
|------|------|------|
| Llama LoRA 训练 | **运行中** | step 445/573 (78%)，预计 ~18 min 完成 |
| 自动 merge 权重 | 等待训练完成 | — |
| Llama greedy unconstrained | 等待 merge | 排队中 |
| Llama greedy constrained | 等待 | 排队中 |
| Llama beam-4 unconstrained | 等待 | 排队中 |
| Llama beam-4 constrained | 等待 | 排队中 |

训练完成后 cascade 脚本 (`d064_gpu0_llama_all_with_greedy.sh`) 会自动运行 4 个推理任务（998 docs × 4 = 3992 次推理）。

### GPU 1 — Qwen 流水线
| 阶段 | 状态 | 进度 |
|------|------|------|
| Qwen beam-4 unconstrained | **运行中** | doc 167/998 (17%)，已写 211 行 |
| Qwen beam-4 constrained | 等待 unc 完成 | 排队中 |

### 输出文件状态
| 文件 | 行数 | 状态 |
|------|------|------|
| `d064_qwen_docred_beam4_unconstrained.jsonl` | 211/998 | 运行中 |
| `d064_qwen_docred_beam4_constrained.jsonl` | — | 未开始 |
| `d064_llama_docred_greedy_unconstrained.jsonl` | — | 未开始 |
| `d064_llama_docred_greedy_constrained.jsonl` | — | 未开始 |
| `d064_llama_docred_beam4_unconstrained.jsonl` | — | 未开始 |
| `d064_llama_docred_beam4_constrained.jsonl` | — | 未开始 |

### 时间估算
- **Llama 训练**: ~18 min + ~10 min merge
- **Llama 4×推理**: 每次 ~4-6 小时 (greedy 快些，beam-4 慢些)，串行总计 ~16-20 小时
- **Qwen unc 完成**: ~4-5 小时，之后 Qwen con 再 ~5-6 小时
- **总计**: GPU 0 瓶颈，预计 **~20-24 小时**后全部完成

Cascade 脚本已正确配置，会在前序任务完成后自动启动后续任务。无需人工干预，但现在还不能收集结果。建议明天再来检查。

---
