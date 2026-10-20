# ssh auto pipeline setup

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_auto-pipeline-setup_20260520T125535_result.json`
- **Structured JSON:** [`aaa21401a61f00530a4e.json`](../../sessions/aa/aaa21401a61f00530a4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**产出汇总：**

| 项目 | 状态 |
|------|------|
| `extract_eval_results.py` | 已部署，s42 验证通过（accuracy=56.7%, unparseable_rate=51.02%, pred_file=`eval_deepseek_cwm_repo_s42_predictions.jsonl`） |
| `watch_eval_completion.sh` | 已后台运行，PID=**966158** |
| 监控目标 | s123-v2 monitor PID=957333 → eval dir: `deepseek_cwm_repo_s123_v2_eval` |
| | s456-v2 monitor PID=957406 → eval dir: `deepseek_cwm_repo_s456_v2_eval` |
| 输出位置 | `artifacts/eval_summaries/deepseek_cwm_s{123,456}_v2.json` |
| 完成标志 | `artifacts/eval_summaries/deepseek_cwm_status.flag` → `BOTH_COMPLETE` |

---
