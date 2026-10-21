# diagnose westd38929 gpu3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd38929_gpu3_20260526T081210_result.json`
- **Structured JSON:** [`fc8a76c08394757f6806.json`](../../sessions/fc/fc8a76c08394757f6806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**状态：正常，eval 已完成。**

| 项目 | 当前值 |
|------|--------|
| PID 288325 | 存活，状态 `Rl`（运行中），已运行 2h47m |
| GPU util | **84%**（已从 0% 恢复） |
| 显存 | 15980 MiB |

**日志显示 eval 已跑完：**
- Overall SR: **0.5500** (275/500)
- 耗时 259.3 min
- 结果已保存: `eval_results/openvla_attn_prune_k085_object_seed42.json`

**结论：** audit 时捕捉到的 0% GPU 利用率是 episode 间的正常间歇。当前进程仍在运行（可能在做后处理或已完成但未退出），eval 结果已落盘。无需 kill，不影响后续实验部署。4 张 GPU 全部在正常工作（67%-84% util）。

---
