# check sft 3B eta

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_sft-3B-eta_20260515T144410_result.json`
- **Structured JSON:** [`a71cd3b8a1dac6e7f2af.json`](../../sessions/a7/a71cd3b8a1dac6e7f2af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

### exp_001_sft_3B_d025_s123 — 已完成 ✓

| 指标 | 值 |
|------|-----|
| 状态 | 完成（exit code 0） |
| 完成时间 | 2026-05-15 14:42:08 UTC |
| 总 steps | 3384/3384 |
| 最终 loss | 1.1401 (step 3380) |
| 最终 token accuracy | 0.734 |
| GPU 4 | 空闲（0%, 0 MiB） |

Final adapter 已保存在 `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter/`。

---

### exp_001_sft_3B_d005_s123 — 训练中

| 指标 | 值 |
|------|-----|
| 进度 | **2829/3177** (89%) |
| 速度 | ~2.91 s/it |
| 已运行 | 2h 46m |
| 剩余 | ~348 steps ≈ **17 分钟** |
| 预计完成 | **~23:02 UTC** (约 17 分钟后) |
| 当前 loss | ~1.05–1.14 (epoch 0.87-0.88) |
| GPU 2 | 61% 利用率, 19325/24564 MiB |

---

**结论：** d025 已就绪可以开始 eval。d005 预计 ~23:02 UTC 完成，两个实验的 eval 和 exp-002 信号计算可以在 ~23:10 UTC 之后安排。

---
