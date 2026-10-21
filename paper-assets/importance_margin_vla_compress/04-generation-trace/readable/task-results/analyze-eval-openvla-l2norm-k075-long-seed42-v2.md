# analyze eval openvla l2norm k075 long seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_l2norm_k075_long_seed42_v2_20260527T131537_result.json`
- **Structured JSON:** [`58acc765b28ab349535f.json`](../../sessions/58/58acc765b28ab349535f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**汇总**：

| 指标 | 值 |
|------|-----|
| overall_success_rate | **34.0%** |
| total_success / total_episodes | 170 / 500 |
| all_tasks_completed | yes (10/10) |
| any_errors | no (EXIT_CODE=0) |
| 运行时间 | 690.5 min (~11.5h) |

**L2norm cliff curve (Long suite) 更新**：

| k | 保留 tokens | Success Rate |
|---|------------|-------------|
| 0.85 | 218/256 | 38.8% |
| **0.75** | **192/256** | **34.0%** |
| 0.70 | 179/256 | 31.2% |

k=0.75 的 34.0% 落在 31.2%–38.8% 区间内，符合单调递减预期，cliff curve 中间点填充成功。

---
