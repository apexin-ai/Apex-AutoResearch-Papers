# eval check ckpt1000 results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check-ckpt1000-results_20260520T002535_result.json`
- **Structured JSON:** [`4e1f5bc257391e3bf36f.json`](../../sessions/4e/4e1f5bc257391e3bf36f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程仍在运行，刚启动约 6 分钟。**

| 项目 | 状态 |
|------|------|
| PID | 171048（子进程 171049） |
| 已运行时间 | ~6 分钟（08:20:05 启动） |
| GPU 1 | RTX 5090，16.7GB / 32.6GB 占用，19% 利用率 |
| 进度 | 已加载模型 + LoRA，正在对 362 个 eval pair 做推理 |
| 结果目录 | `/root/contrastive_entrain_calib/results/exp008v3_ckpt1000_eval/` — 当前为空 |

日志显示模型和 LoRA adapter 加载正常，NLI 模型也已就绪，当前处于推理阶段。按 362 对的量级和单 GPU 推理速度，预计还需要一段时间。

看起来这个 eval 是刚被（重新）启动的，不是之前预期的 ~100 分钟前的那个。需要等推理完成后才能查看结果。要我稍后再检查吗？

---
