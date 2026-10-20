# monitor exec only r2 progress

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exec-only-r2-progress_20260515T155615_result.json`
- **Structured JSON:** [`70e182d98b103c52f468.json`](../../sessions/70/70e182d98b103c52f468.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总

| 指标 | s43-1000-r2 (cuda:0) | s44-1000-r2 (cuda:1) |
|------|----------------------|----------------------|
| **当前 step** | 947 / 1000 | 856 / 1000 |
| **进度** | 94.7% | 85.6% |
| **已运行** | 2h04m57s | 2h04m52s |
| **reward** | 1.0 (稳定) | 1.0 (稳定) |
| **loss** | 0.0 | 0.0 |
| **entropy** | ~0.01–0.10 | ~0.04–0.10 |
| **ISR** | 0.667–0.708 | 0.000–0.124 (多数为 0) |
| **最新 checkpoint** | checkpoint-900 | checkpoint-850 |
| **GPU 利用率** | 100%, 81GB/96GB | 90%, 83GB/96GB |

**ETA 估算：**
- **s43**: 947步用了~2h05m → ~7.9s/step 平均，剩 53 步 → **~7 分钟后完成**
- **s44**: 856步用了~2h05m → ~8.7s/step 平均，剩 144 步 → **~21 分钟后完成**

s44 比 s43 慢的原因：同样运行时间但 step 数少 ~90 步，可能是 s44 在早期 step_time 较长。

**磁盘**：/root/autodl-tmp 47G/250G (19%)，空间充裕。

**注意**：s44 的 ISR 几乎全为 0，与 s43 的 0.67–0.71 差异很大。这符合 exec-only 的预期行为（C006：低 ISR = 冗余编码，非无推理），但 seed 间差异值得后续 eval 时关注。

---
