# analysis conditional granger fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_conditional_granger_fix_20260521T023044_result.json`
- **Structured JSON:** [`08cffb1d0a5cfde3e134.json`](../../sessions/08/08cffb1d0a5cfde3e134.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已完成的修改：**

1. **14b 路径问题**：确认脚本原路径 `scale/14b_a050_s42_fp32/` 不存在。用户指定的 `scale_check/pythia14b_a050_s42_bf16/` 只有 2 个 generation（实验未完成），无法用于 Granger 分析。已从脚本中移除 14b 条目。

2. **JSON 保存**：修复 statsmodels API 兼容问题（`df_num/df_denom` → `test.df`），在 westd-19828 上重跑分析，`conditional_granger_v2.json` 已保存到 `results/analysis/`。

3. **本地 artifact 更新**：
   - 修正为 11 实验 / 44 pairs（原误报 12/48）
   - 所有数字更新到新结果（uncond 79.5%/79.5%, cond 36.4%/52.3%, joint 88.6%）
   - 添加 df_resid caveat 和 citation evidence hierarchy
   - 添加 14b 未完成的 caveat

4. **关键结论不变**：ECE 仍然是 dominant channel（75% pR² wins, pR²=0.472 vs 0.351），collinearity r=−0.84 to −0.98。

---
