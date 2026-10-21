# ops kill deploy westd41074 v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_deploy_westd41074_v4_20260522T080610_result.json`
- **Structured JSON:** [`8e7df647528e858f3b11.json`](../../sessions/8e/8e7df647528e858f3b11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程都在加载模型中，状态正常。

## 汇总

### Kill 确认
| PID | 实验 | 状态 |
|-----|------|------|
| 273012 | eval_pi05_random_k05_spatial_seed43 | ✓ 已 kill |
| 273085 | eval_pi05_l2norm_k05_spatial_seed43 | ✓ 已 kill |

### 新实验部署
| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| 0 | eval_pi05_random_k085_object_seed43 | 304126 | Running, 加载模型中 |
| 1 | eval_pi05_l2norm_k0925_object_seed43 | 304198 | Running, 加载模型中 |

### 二次确认
- 两个 PID 均存活（状态 `Rl`，运行约 43 秒）
- 显存暂 3 MiB（正在从磁盘加载 π0.5 模型，尚未搬到 GPU）
- 日志正常输出 config 和 loading 信息，无报错

---
