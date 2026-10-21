# ops d100 mmlu rrf invalidate

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d100_mmlu_rrf_invalidate_20260517T002151_result.json`
- **Structured JSON:** [`e9642858b36b7dad7ac7.json`](../../sessions/e9/e9642858b36b7dad7ac7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**排除清单处理状态：**
| 文件 | 状态 |
|------|------|
| `rrf_d100/per_model/rrf_scores_Llama-3.2-3B_d100_s42_mmlu.json` | → `.invalid` |
| `rrf_d025/per_model/rrf_scores_Qwen2.5-3B_d025_s42_old_alpha16_mmlu.json` | → `.invalid` |
| `rrf_d100/exposure_scores.json` → Llama mmlu 条目 | 已删除（保留 gsm8k, arc_challenge） |
| `rrf_d025/exposure_scores.json` → alpha16 整条 | 已删除 |

**IRT 脚本 exclude 机制：**
- `run_pooled_rrf_irt.py` 从 `--exposure-file`（即 `exposure_scores.json`）加载，只处理文件中存在的 model+benchmark 组合。已从文件中移除无效条目，IRT 自然不会读到。
- `exposure_aggregated.json` 不被 IRT 脚本引用，无需处理。

**d100 RRF 是否需要重跑：**
- 不需要。Llama d100 的 `signals_merged_mmlu.json` 根本不存在，说明该 RRF 分数本身就是从不完整信号生成的无效数据。删除即可，无需重新生成。Llama d100 的 gsm8k 和 arc_challenge 仍保留且有效。

---
