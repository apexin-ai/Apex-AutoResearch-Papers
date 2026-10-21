# ssh westd phase2 progress check v4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-phase2-progress-check-v4_20260519T120507_result.json`
- **Structured JSON:** [`87e8da8eb0139b763d39.json`](../../sessions/87/87e8da8eb0139b763d39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态更新：

**GPU 使用：**
| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 99% | 31.7/97.9 GiB | phi4_d100 eval（19:49 启动） |
| 1 | 96% | 32.7/97.9 GiB | qwen14b_d100 eval（19:56 启动） |
| 2 | 94% | 16.7/97.9 GiB | olmo2_d100 eval（19:55 启动） |
| 3 | 空闲 | — | — |

**注意：** olmo2_d100 实际跑在 GPU 2（不是之前预期的 GPU 2 给 olmo2_d100，吻合）。但 qwen14b 在 GPU 1 而非预期的 GPU 1，也吻合。

**Eval 完成情况：**
- phi4_d100: 运行中
- qwen14b_d100: 运行中
- olmo2_d100: 运行中
- olmo2_d000/d005/d025/d050: 尚未开始（MISSING）

**OLMo monitor：** 正常运行，已完成 4 轮检查（每 120s 一轮），持续检测到 GPU 0/1 繁忙，尚未触发任何新 eval 启动。等 GPU 0 或 1 的任务完成后会自动启动 olmo2 d000-d050 eval。

三个 eval 均已跑约 10-18 分钟，都还在进行中，无新完成项。

---
