# deploy westd38929 gpu2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_gpu2_20260524T193528_result.json`
- **Structured JSON:** [`5755bbec053d7caee5fe.json`](../../sessions/57/5755bbec053d7caee5fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**已完成实验结果**（结果文件已存在，registry zombie 已修复为 DONE）：
| 实验 | SR |
|------|-----|
| L2norm k=0.5 Long seed42 | **50.2%** |
| L2norm k=0.3 Long seed42 | **40.6%** |
| L2norm k=0.85 Long seed43 | **79.0%**（fallback，也已完成） |

**GPU2 部署**：
- 实验：`eval_pi05_l2norm_k03_long_seed43_postfix_v2` — L2norm k=0.3 Long seed43
- PID：756339，GPU2
- Cron 监控：每 17 分钟检查（job 9adb4eaf）
- 选择理由：k=0.5 seed43 正在 GPU3 上跑，k=0.3 seed43 是其 extreme-pruning 配对，从未运行过

---
