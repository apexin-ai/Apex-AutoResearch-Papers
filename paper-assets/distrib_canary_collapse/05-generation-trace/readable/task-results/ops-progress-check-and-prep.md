# ops progress check and prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-check-and-prep_20260522T225023_result.json`
- **Structured JSON:** [`19cb2e70fd228e9ed344.json`](../../sessions/19/19cb2e70fd228e9ed344.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**410M s44 已经完成了。** `results/alpha_sweep/a050_s44_fp32` 有完整的 gen_0 到 gen_10（s43 也已完成）。

当前时间 22:54 UTC。以下是全局状态：

## 全局进度

### 已完成
| 实验 | Server | 状态 |
|------|--------|------|
| 14b_c4_s42_fp32 | 17855 | ✅ gen 10/10 |
| t10_a060_s42_fp32_14b | 17855 | ✅ gen 10/10 |
| t10_a075_s42_fp32_14b | 17855 | ✅ gen 10/10 |
| t10_a050_s42_fp32_14b | 19828 | ✅ gen 10/10 |
| 14b_a050_s42_fp32 | 19828 | ✅ gen 10/10 |
| 410M a050_s42_fp32 | 17855 | ✅ gen 10/10 |
| 410M a050_s43_fp32 | 17855 | ✅ gen 10/10 |
| 410M a050_s44_fp32 | 17855 | ✅ gen 10/10 |

### 运行中
| 实验 | Server:GPU | 当前 gen | 目标 | 预估完成 (UTC) |
|------|-----------|---------|------|---------------|
| t10_a045_s42_fp32_14b | 17855:GPU4 | gen 9 synth data | 10 | ~00:40 |
| t15_a045_s42_fp32_14b | 17855:GPU5 | gen 10/15 | 14 | ~02:50 |
| t15_a050_s42_fp32_14b | 17855:GPU1 | gen 12/15 | 14 | ~01:20 |
| t15_a060_s42_fp32_14b | 17855:GPU0 | gen 12/15 | 14 | ~01:20 |
| 14b_t10_a060_s43_fp32 | 17855:GPU3 | gen 2 (65%) | 10 | ~05:20 |
| 14b_t10_a075_s43_fp32 | 17855:GPU2 | gen 2 (28%) | 10 | ~05:50 |
| t15_a075_s42_fp32 | 19828:GPU0 | gen 9 synth | 14 | ~03:50 |
| 14b_t10_a050_s43_fp32 | 19828:GPU1 | gen 2 (65%) | 10 | ~05:20 |

GPU 利用率：17855 全部 6 卡满载（88-100%），19828 全部 2 卡满载。

## t10_a045 进度
- 当前：gen 9/10，正在生成合成数据
- 预估完成：~00:40 UTC（约 1h 45min）
- GPU 4 将最先释放

## 410M s44 部署参数
**无需部署——实验已完成。** `results/alpha_sweep/a050_s44_fp32` 包含完整 gen_0-10 metrics。

注意事项：
- s42/s43/s44 均使用脚本默认 `EleutherAI/pythia-410m`（**non-deduped**），非 Director 提到的 `pythia-410m-deduped`
- 如需 deduped 版本的 s44，HF cache 中有 `pythia-410m-deduped`，但需确认是否要与 s42/s43 保持一致（它们都是 non-deduped）

---
