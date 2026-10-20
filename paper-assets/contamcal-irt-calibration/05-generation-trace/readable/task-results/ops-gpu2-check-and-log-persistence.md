# ops gpu2 check and log persistence

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu2-check-and-log-persistence_20260515T111040_result.json`
- **Structured JSON:** [`539cc7bbd3f2c8f689ec.json`](../../sessions/53/539cc7bbd3f2c8f689ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

持久化完成，两个文件都已在 `/root/runs/contamcal-irt-calibration/` 中且持续追加。

---

## 报告

### 1. GPU 2 — exp_008 base pretrained eval (PID 530893)

| 项目 | 状态 |
|------|------|
| 进程状态 | `T (stopped)` — 被信号停止，非正常运行 |
| 子进程 | PID 548811 也是 `T (stopped)`，执行 `/tmp/tmp4kb0dwy6.py` |
| 运行时间 | 2h26m |
| GPU 利用率 | 0% |
| 显存占用 | 8225 MiB |
| 输出目录 | 空（无任何结果文件） |
| tmux 窗口 | 空白，无输出 |
| 日志 | 未找到任何日志文件 |

**结论：进程卡死，需要 kill 并重跑。** 进程处于 T (stopped) 状态，不是 CPU-bound，而是被信号暂停。2.5h 无任何产出。

### 2. SFT 日志持久化

| 日志 | 持久化路径 | tail PID |
|------|-----------|----------|
| d025 (GPU 0) | `/root/runs/contamcal-irt-calibration/exp_001_sft_15B_d025_s123_v2.log` | 551173 |
| d005 (GPU 1) | `/root/runs/contamcal-irt-calibration/exp_001_sft_15B_d005_s123_v2.log` | 551506 |

两个 SFT 训练正常运行中：d025 在 203/3384 (~6%), d005 在 185/3177 (~6%)，速度 ~2s/it。bitsandbytes 有 libnvJitLink.so 警告但不影响训练。

---
