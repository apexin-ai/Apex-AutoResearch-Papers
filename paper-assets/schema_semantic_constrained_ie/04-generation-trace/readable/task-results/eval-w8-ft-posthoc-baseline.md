# eval w8 ft posthoc baseline

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_w8_ft_posthoc_baseline_20260516T063514_result.json`
- **Structured JSON:** [`9d9c7606a996ea08ad2e.json`](../../sessions/9d/9d9c7606a996ea08ad2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总结果：

| Model | Dataset | R_F1_before | R_F1_posthoc | R_F1_constrained | Reject% | TP_lost | Δ_post_vs_const |
|-------|---------|-------------|-------------|------------------|---------|---------|-----------------|
| Qwen  | SciERC  | 43.86%      | 43.94%      | 43.77%           | 1.95%   | 4/461   | +0.17%          |
| Llama | SciERC  | 45.45%      | 45.23%      | 45.47%           | 1.11%   | 5/467   | -0.24%          |
| Qwen  | DocRED  | 40.91%      | 41.11%      | TBD              | 1.03%   | 1/5666  | TBD             |
| Llama | DocRED  | 43.77%      | 43.92%      | 44.23%           | 0.64%   | 1/6136  | -0.31%          |

**核心发现**：FT 后违约率仅 0.6%–2.0%（零样本是 11%–17%），post-hoc filtering 几乎不损失 recall（最多丢 5 个 TP）。Post-hoc 和 constrained decoding 在 FT regime 下 R_F1 差距 <0.3pp，远小于零样本下的差距。

**结论**：constrained decoding 的核心价值在 zero-shot/low-resource 场景——模型未内化约束时 post-hoc 会大量误删正确 triple。FT 后模型已隐式学会约束，两种方法效果趋同，但 constrained decoding 仍提供 0% 违约的硬保证。

报告已注册：`w8_ft_posthoc_baseline`。修复的 `posthoc_filter_v2.py` 已保存在服务器上（处理 `parsed_output=None` 和缺失 `tail` key 的情况）。

---
