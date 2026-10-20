# c2_n500_deepseek 诊断报告

**日期**: 2026-05-15
**结论**: SUCCESS — 全部 8 conditions 完成，n=500，Verdict 均为 PASS

## 各 Condition 完成状态

| Condition | Method | Sparsity | Problems | Verdict | 完成时间 |
|-----------|--------|----------|----------|---------|----------|
| ds_imp_s015 | importance | 0.15 | 500/500 | PASS | May 15 02:31 |
| ds_imp_s020 | importance | 0.20 | 500/500 | PASS | May 15 06:55 |
| ds_imp_s025 | importance | 0.25 | 500/500 | PASS | May 15 11:19 |
| ds_imp_s030 | importance | 0.30 | 500/500 | PASS | May 15 15:44 |
| ds_rand_s015 | random | 0.15 | 500/500 | PASS | May 15 02:05 |
| ds_rand_s020 | random | 0.20 | 500/500 | PASS | May 15 06:30 |
| ds_rand_s025 | random | 0.25 | 500/500 | PASS | May 15 10:54 |
| ds_rand_s030 | random | 0.30 | 500/500 | PASS | May 15 15:19 |

## 结果文件

所有 8 个 profiling_results.json 文件均为 22MB：
- /root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_{imp,rand}_s{015,020,025,030}/profiling_results.json

## 关键日志

GPU0 full log 最后一行：`===== C2 n=500 GPU0: ALL DONE ===== Fri May 15 15:44:10 CST 2026`
GPU1 full log 最后一行：`===== C2 n=500 GPU1: ALL DONE ===== Fri May 15 15:19:35 CST 2026`

所有 conditions 的 CI overlap test 均通过（low_sparsity vs mid_sparsity CI non-overlapping）。

## II 指标摘要

### Importance masking (median II)
| Sparsity | low_sparsity | mid_sparsity | high_sparsity |
|----------|-------------|--------------|---------------|
| 0.25 | +5.1191 | +0.8019 | +0.0332 |
| 0.30 | +10.6274 | +1.7367 | +0.0511 |

### Random masking (median II)
| Sparsity | low_sparsity | mid_sparsity | high_sparsity |
|----------|-------------|--------------|---------------|
| 0.25 | +1.6449 | +1.4109 | +1.3289 |
| 0.30 | +4.1493 | +3.3652 | +3.4756 |

Importance masking 呈现明显的 phase-dependent 效应（low >> mid >> high），random masking 各 phase 差异小，符合预期。