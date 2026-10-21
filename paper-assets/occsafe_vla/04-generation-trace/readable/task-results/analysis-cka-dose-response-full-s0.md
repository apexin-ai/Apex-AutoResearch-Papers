# analysis cka dose response full s0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cka_dose_response_full_s0_20260525T064526_result.json`
- **Structured JSON:** [`024b5dca6f2ad6dbc6bf.json`](../../sessions/02/024b5dca6f2ad6dbc6bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**s0 cutoff checkpoints 不存在。** 两台服务器上都没有。

现有 cutoff checkpoints 的 seed 分布：

| 条件 | 可用 seed | s0 存在? |
|------|-----------|----------|
| cutoff_15k | s1, s2 | ❌ |
| cutoff_25k | s2 | ❌ |
| cutoff_35k | 无任何 seed | ❌ |
| cutoff_45k | s1 | ❌ |
| reverse_cutoff | s2 | ❌ |

**已有 s0 CKA 数据**（来自 `cka_same_seed/cka_results.json`）：
- Vanilla s0: DINOv2 mean ≈ 0.968, SigLIP mean ≈ 0.953
- Full OCC (BN) s0: DINOv2 mean ≈ 0.964, SigLIP mean ≈ 0.960
- Detach+BN s0: DINOv2 mean ≈ 0.965, SigLIP mean ≈ 0.955
- Full OCC (LN) s0: DINOv2 mean ≈ 0.660, SigLIP mean ≈ 0.955

**结论：** 5 个 cutoff s0 实验需要先训练才能构建完整 dose-response 曲线。这 5 个训练任务（cutoff_15k_s0, cutoff_25k_s0, cutoff_s0, cutoff_45k_s0, reverse_cutoff_s0）都尚未启动。

要继续推进，有两个选项：
1. **先训练 5 个 s0 cutoff 模型**（每个约 50K steps），然后再做 CKA 分析
2. **用现有不同 seed 的 cutoff checkpoints 先出一版 mixed-seed 曲线**，待 s0 训练完成后替换

你想怎么走？

---
