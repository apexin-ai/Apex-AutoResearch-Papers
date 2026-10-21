# analysis d145 4b sft s44 no evi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d145_4b_sft_s44_no_evi_2048_20260521T193710_result.json`
- **Structured JSON:** [`57d05769059805e26fe4.json`](../../sessions/57/57d05769059805e26fe4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总结果：

## s44 no_evi 完整 metrics

| 指标 | 值 |
|---|---|
| ign_f1 | 0.4680 |
| f1 | 0.4784 |
| ign_precision | 0.4492 |
| ign_recall | 0.4884 |
| precision | 0.4710 |
| recall | 0.4860 |
| evi_f1 | 0.0000 (expected) |
| format_ok | 983/985 (99.8%) |
| truncated | 158/985 |
| predictions | 24,103 |
| inference_time | 7,248s |

## s44 fair_tax

| 指标 | 值 |
|---|---|
| fair_subset_size | 982 docs |
| fair_with_evi_ign_f1 | 0.4667 |
| fair_no_evi_ign_f1 | 0.4688 |
| **fair_tax** | **+0.21pp** |

## 4B SFT 3-seed evidence tax 汇总

| Seed | fair_tax (pp) | fair_subset | with_evi ign_f1 | no_evi ign_f1 |
|------|-------------|-------------|----------------|--------------|
| s42 | +0.73 | 981 | 0.3951 | 0.4024 |
| s43 | -0.20 | 982 | 0.4367 | 0.4355 |
| s44 | +0.21 | 982 | 0.4667 | 0.4688 |
| **Mean±Std** | **+0.25 ± 0.47pp** | | | |

## 异常检查
- `no_evidence: true` 参数正确传递 ✓
- format_ok 率 99.8%，与 with_evi 完全一致（均 983/985），fair_subset 982 docs — 正常
- s44 的 with_evi (0.4665) 和 no_evi (0.4680) 绝对性能是三个 seed 中最高的，但 s42 明显低于 s43/s44（可能 s42 adapter 质量较差）
- **3-seed 结论：4B SFT 的 evidence tax 均值 +0.25pp，方向为正（no_evi 略优），但 std=0.47pp 远大于均值，且 s43 为负值，说明 4B 模型上 evidence 的影响不显著且方向不稳定**

---
