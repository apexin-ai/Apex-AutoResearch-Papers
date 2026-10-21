# ops phase a launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_phase-a-launch_20260518T114058_result.json`
- **Structured JSON:** [`935e6cdce9dddbdd0906.json`](../../sessions/93/935e6cdce9dddbdd0906.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正常。

## Phase A 启动结果汇总

| GPU | 任务 | PID | VRAM | 状态 |
|-----|------|-----|------|------|
| cuda:0 | 7B d005 s42 训练 | 23304 | 69,429 MiB | 运行中，96% util |
| cuda:1 | 7B d000 s42 GSM8K eval | 24377 | 17,711 MiB | 运行中，正在评估 |
| cuda:2 | (空闲) | - | 0 MiB | 14B 未就绪 (incomplete=1, safetensors=7) |
| cuda:3 | (未知进程) | - | 0 MiB | 100% util 但 0 VRAM，异常 |

**问题记录：**
- GSM8K eval 首次启动因 httpx client closed 崩溃，二次因 `HF_HUB_OFFLINE=1` 阻断数据集下载崩溃，第三次成功
- 14B 模型仍有 1 个 incomplete 文件，未启动 14B 训练
- cuda:3 显示 100% utilization 但 0 VRAM，可能是残留进程或驱动异常，需关注

---
