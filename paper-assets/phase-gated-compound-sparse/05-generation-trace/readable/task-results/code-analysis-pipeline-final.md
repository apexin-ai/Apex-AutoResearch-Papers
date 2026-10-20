# code analysis pipeline final

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analysis_pipeline_final_20260514T214825_result.json`
- **Structured JSON:** [`3081eb824b0d11530e01.json`](../../sessions/30/3081eb824b0d11530e01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功。脚本路径：`/root/autodl-tmp/pacs/analyze_n500_unified.py`

## Dry-run 结果总结 (n=50 数据)

### Per-condition median II diff (low−high)

| Model | Masking | 15% | 20% | 25% | 30% |
|-------|---------|-----|-----|-----|-----|
| DeepSeek | Importance | +0.35*** | +1.14*** | +4.02*** | +9.95*** |
| DeepSeek | Random | +0.01 | +0.04 | +0.30 | +1.06 |
| Qwen | Importance | +0.06 | +0.29*** | +1.15*** | +2.59*** |
| Qwen | Random | −0.02 | +0.06 | +0.63 | +2.42 |

(`***` = Bonferroni p < 0.001)

### 关键发现

1. **Mid-phase null rate**: DeepSeek 20%, Qwen **58%** — 符合预期（Qwen ~45% 会更高些在 n=50）
2. **Within-imp d_z**: 单调递增，s015→s030 DeepSeek d_z=−0.80 (medium), Qwen d_z=−1.00 (large)
3. **Imp-vs-rand**: DeepSeek 所有 sparsity 显著 (Bonferroni p<0.001 at s020+)；Qwen 全部不显著（n=50 power 不足）
4. **Dose-response**: importance 和 random 均显示单调递增，但 permutation p=0.085（4 点排列只有 24 种，最小 p=1/25=0.04）
5. **Qwen s015**: CI=[0.01, 0.12] 刚好不含 0，但 Bonferroni 校正后 p=0.59 不显著 → n=500 数据关键

### 发现的问题
- Permutation monotonicity test 只有 4 个 sparsity level，排列数仅 24，p 值分辨率有限（最小 ~0.04）。这是设计限制，n=500 不会改变。
- Random masking 在 s030 也出现较大 II diff（DeepSeek +1.06, Qwen +2.42），Bonferroni 校正后不显著，但值得关注。

---
