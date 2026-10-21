# code analysis unify integrate

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analysis-unify-integrate_20260514T214855_result.json`
- **Structured JSON:** [`4e594961373a9e687f89.json`](../../sessions/4e/4e594961373a9e687f89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Header now includes PermGr column. All changes are complete and verified.

---

## Summary

### P0: FDR / Effect Size 统一

**发现的不一致：**
1. **FDR 实现**：`analyze_mvp.py` 和 `method_ablation.py` 使用 `scipy.stats.false_discovery_control`，`analyze_alpha_sweep.py` 使用 `statsmodels.stats.multitest.multipletests`
2. **TY Effect Size**：`analyze_alpha_sweep.py` 使用 Cohen's f²（`F*p/df_resid`），`method_ablation.py` 使用 partial η²（`F/(F+df_resid)`）
3. **字段名**：`method_ablation.py` 的 TY 用 `effect_size`，`analyze_alpha_sweep.py` 用 `effect_size_f2`

**修改：**
- `analyze_mvp.py`、`method_ablation.py`：FDR 统一为 `multipletests(method='fdr_bh')`
- `analyze_alpha_sweep.py`：TY effect size 改为 partial η²（`F*p/(F*p+df_resid)`）
- 三个脚本 TY 字段名统一为 `effect_size_eta2`，分类阈值用 0.14/0.06/0.01

### P1: Permutation Granger 集成

- 在 `analyze_alpha_sweep.py` 中新增 `perm_granger()` 包装函数，调用 `permutation_granger_test`
- 将 f² 转换为 η²（`η² = f²/(1+f²)`）
- METHODS 字典扩展为 4 方法
- FDR 校正自动覆盖 permutation_granger
- Consensus 更新：≥3 methods = strong_consensus，≥2 = consensus
- 输出表格和 summary.txt 均包含 PermGr 列

**Dry-run 结果：**
- `analyze_mvp.py` (seed_42)：STRONG PASS，BH FDR 11/20 sig，输出格式正确
- `analyze_alpha_sweep.py` (a000_s42, 7 gen)：4 方法均产出结果，FDR 校正正常，JSON/summary.txt 格式正确
- `method_ablation.py` (seed_42)：5 方法均运行，TY details 显示 `eta2=` 值

### P2: 代码去重

未执行。三个脚本逻辑差异较大（analyze_mvp 有 verdict 系统、method_ablation 有 spurious 检测、alpha_sweep 有多 α 聚合），重构风险高，建议单独任务处理。

---
