# ops full gpu health 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-gpu-health-17855_20260523T034635_result.json`
- **Structured JSON:** [`2c2cf376befc8eaf7a4b.json`](../../sessions/2c/2c2cf376befc8eaf7a4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full report:

---

## westd-17855 (6/6 GPUs active)

| GPU | exp_id | PID | 状态 | gen进度 | 剩余 |
|-----|--------|-----|------|---------|------|
| 0 | t15_a060_s43_fp32_14b | 749427 | 训练中 97% | 1✓ + gen_1训练中 / 15 | ~14 gen |
| 1 | t15_a050_s43_fp32_14b | 750075 | 训练中 100% | 1✓ + gen_1训练中 / 15 | ~14 gen |
| 2 | 14b_t10_a075_s43_fp32 | 719178 | 训练中 100% | 7✓ + gen_7训练中 / 10 | ~3 gen |
| 3 | 14b_t10_a060_s43_fp32 | 719252 | 训练中 99% | 7✓ + gen_7训练中 / 10 | ~3 gen |
| 4 | t10_a045_s43_fp32_14b | 738796 | 训练中 100% | 3✓ + gen_3训练中 / 10 | ~7 gen |
| 5 | t15_a045_s42_fp32_14b | 680608 | 训练中 89% | 15✓ + gen_15训练中 / 15 | **最后1gen** |

磁盘: 350G, 325G used, **26G free (93%)** ⚠️

### 已完成 14b 实验 (有 all_metrics.json):
- t15_a060_s42_fp32_14b ✓ (PermG=6/8)
- t15_a050_s42_fp32_14b ✓ (PermG=3/8)
- t10_a060_s42_fp32_14b ✓
- t10_a075_s42_fp32_14b ✓
- t10_a045_s42_fp32_14b ✓

---

## westd-19828 (2/2 GPUs active)

| GPU | exp_id | PID | 状态 | gen进度 | 剩余 |
|-----|--------|-----|------|---------|------|
| 0 | scale_14b_t15_a075_s42_fp32 | 793171 | 训练中 88% | 14✓ + gen_14训练中 / 15 | **最后1gen** |
| 1 | 14b_t10_a050_s43_fp32 | 822048 | 训练中 99% | 7✓ + gen_7训练中 / 10 | ~3 gen |

磁盘: 250G, 146G used, 105G free (59%) ✓

---

### 异常/注意:
- **17855 磁盘 93%** — 仅 26G 剩余，6 个实验同时写入，需关注。新实验勿提交到此服务器（C007）。
- GPU:5 t15_a045_s42 使用 `--start_gen 2` 恢复，gen_15 为最后一代，即将完成。
- 19828 的 t15_a075_s42 output_dir 在 `outputs/` 而非 `results/`（路径不一致），完成后可能需要移动。

---
