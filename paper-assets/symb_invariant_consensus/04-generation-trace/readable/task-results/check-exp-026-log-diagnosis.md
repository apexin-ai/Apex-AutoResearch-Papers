# check exp 026 log diagnosis

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp-026-log-diagnosis_20260518T144334_result.json`
- **Structured JSON:** [`13cc956988d1afd751d8.json`](../../sessions/13/13cc956988d1afd751d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

| 项目 | 结果 |
|------|------|
| **完成数** | **204/204** (100%) |
| **判定** | **success** |
| **退出原因** | 正常完成后自然退出（非 crash） |
| **SICA accuracy** | 74.51% (152/204) |
| **SC accuracy** | 75.00% (153/204) |
| **Extraction rate** | 98.53% |
| **运行时间** | 20:11 → 22:39，约 2.5h |
| **结果路径** | `/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json` |
| **cuda:0** | vLLM (PID 23449) 仍在跑，0% 利用率（idle），exp-029 正在通过 port 8003/cuda:3 复用其 intermediates |

日志仅 42 行（stdout 被重定向到别处，log 文件只捕获了初始化输出）。无 error/traceback。

Registry 已更新为 DONE/success，cron 已删除。

---
