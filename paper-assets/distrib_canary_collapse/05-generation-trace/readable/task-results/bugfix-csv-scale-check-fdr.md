# bugfix csv scale check fdr

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_csv_scale_check_fdr_20260520T171938_result.json`
- **Structured JSON:** [`2c862185c2b90b1f658c.json`](../../sessions/2c/2c862185c2b90b1f658c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结论

**CSV `dose_response_d120_compiled.csv` 的 PermG 字段已正确使用 FDR-corrected 值，无需修正。**

### 详细证据

**scale_check/pythia14b_a050_s42（Reviewer 质疑的行）：**

逐 pair 验证 forward perm_granger：

| Pair | p_value | significant (pre-FDR) | fdr_p | significant_fdr |
|------|---------|----------------------|-------|----------------|
| te→d1 | 0.0470 | true | 0.0921 | **false** |
| te→d2 | 0.0768 | false | 0.1024 | false |
| te→d3 | 0.0576 | false | 0.0921 | false |
| te→mauve | 0.1156 | false | 0.1321 | false |
| ece→d1 | 0.0142 | true | 0.0437 | **true** |
| ece→d2 | 0.0164 | true | 0.0437 | **true** |
| ece→d3 | 0.0124 | true | 0.0437 | **true** |
| ece→mauve | 0.2158 | false | 0.2158 | false |

- Pre-FDR count = 4/8, post-FDR count = **3/8**
- CSV permg_count = **3** — 使用的是 FDR 校正后的值
- JSON summary `perm_granger_fdr_forward_sig: 3` 一致

**全面交叉验证（9 个实验，JSON summary vs CSV）：**

| 实验 | JSON | CSV | 匹配 |
|------|------|-----|------|
| scale_check/pythia14b_a050_s42 | 3 | 3 | ✓ |
| scale_check/pythia69b_a100_s42 | 7 | 7 | ✓ |
| scale_check/pythia69b_a100_s43 | 6 | 6 | ✓ |
| generalize/pythia14b_a100_s42 | 2 | 2 | ✓ |
| generalize/pythia14b_a100_s43 | 6 | 6 | ✓ |
| generalize/smollm3_3b_a100_s42 | 3 | 3 | ✓ |
| generalize/gpt2m_a100_s43_bf16 | 0 | 0 | ✓ |
| intervention/reactive_d1_s42 | 8 | 8 | ✓ |
| scale/14b_c4_s42_fp32 | 8 | 8 | ✓ |

**数据流确认：** `t20_post_analysis.py:74` 明确使用 `results["summary"]["perm_granger_fdr_forward_sig"]`，即 FDR 校正后的计数。

**Reviewer 的 "0/8" 判断有误。** pythia14b_a050_s42 的 FDR-corrected PermG 确实是 3/8（ece 相关的 3 对 pair 在 FDR 校正后仍显著，fdr_p ≈ 0.044 < 0.05）。CSV 无需修改。

---
