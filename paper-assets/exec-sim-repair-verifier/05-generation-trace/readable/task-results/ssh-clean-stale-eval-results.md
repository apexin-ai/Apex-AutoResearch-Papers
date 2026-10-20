# ssh clean stale eval results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_clean-stale-eval-results_20260521T140455_result.json`
- **Structured JSON:** [`5c354f73471d7f812305.json`](../../sessions/5c/5c354f73471d7f812305.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

DS s123 清理完成。s456 的 incremental 正在被写（224 行），不动。Qwen 目录有旧结果，需确认是否 backup。

**清理结果汇总：**

| 目录 | 操作 | 详情 |
|------|------|------|
| **DS s123** (`deepseek_cwm_repo_s123_v2_eval/`) | ✅ 已清理 | 3 个文件 mv 为 `*_epoch1_backup.*`（共 ~34MB） |
| **DS s456** (`deepseek_cwm_repo_s456_v2_eval/`) | ⚠️ 未动 | `results_incremental.jsonl` 224 行，正在被写入；另有 `results_contaminated_e2e3_mix.jsonl`（870KB）已标记为 contaminated |
| **Qwen CWM** (`qwen3_8b_cwm_repo_s42_ckpt400_seq4096/`) | ⚠️ 有旧结果 | May 20 的 `eval_repo_cwm.json` + `results_incremental.jsonl` + `predictions.jsonl`（共 ~63MB），需要你确认是否 backup |

DS s456 的 `results_contaminated_e2e3_mix.jsonl` 看文件名已经标记了污染，是否也需要处理？Qwen 那个目录要不要一起 backup？

---
