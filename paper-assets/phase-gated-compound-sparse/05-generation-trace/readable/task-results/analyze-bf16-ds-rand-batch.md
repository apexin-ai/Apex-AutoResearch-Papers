# analyze bf16 ds rand batch

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_bf16_ds_rand_batch_20260514T070523_result.json`
- **Structured JSON:** [`b19a99b2279da94e71d0.json`](../../sessions/b1/b19a99b2279da94e71d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部 conclusion=success，registry 已更新。汇总：

| 实验 | Sparsity | Verdict | II[high] mean (95%CI) | II[mid] mean (95%CI) | II[low] mean (95%CI) | Sign Reversal |
|------|----------|---------|----------------------|---------------------|---------------------|---------------|
| bf16_ds_rand_s015 | 0.15 | PASS | +0.38 [-0.54, +1.31] | -172.66 [-427.01, -9.07] | -5.73 [-10.93, -1.44] | No |
| bf16_ds_rand_s020 | 0.20 | PASS | +2.53 [+1.25, +4.24] | -36.05 [-93.25, -2.20] | -2.48 [-5.63, +0.11] | Yes |
| bf16_ds_rand_s025 | 0.25 | PASS | +5.59 [+1.17, +9.47] | -514.24 [-1361.47, -24.94] | -9.11 [-25.80, +2.52] | Yes |

关键观察：
- 三个 sparsity 下 random masking 均 PASS（high vs mid CI 不重叠）
- high_sparsity II 始终为正，mid_sparsity II 始终为强负值，模式与 importance masking 一致
- s020/s025 出现 sign reversal（high>0, mid<0），s015 未达到（high CI 跨零）
- 随 sparsity 增大，high_sparsity II 效应增强（0.38→2.53→5.59），mid_sparsity 负效应也加剧

---
