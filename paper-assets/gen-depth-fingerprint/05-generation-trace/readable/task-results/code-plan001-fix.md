# code plan001 fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-fix_20260514T184702_result.json`
- **Structured JSON:** [`da48dbb2c486b933299f.json`](../../sessions/da/da48dbb2c486b933299f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 处修复已完成，dry-run 验证通过。

### 修复详情

**修复 1: Part B — H1/H2 判定逻辑**
- Pearson linregress → **Spearman rank correlation** 作为主判定依据（linregress 仅保留画趋势线）
- 新增 **相邻深度间 Cohen's d** 计算（4 个 effect sizes）
- 新增 **effect-size 趋势检验**（Spearman of effect sizes vs position）
- 判定逻辑：es_trend_rho < 0 且 p < 0.05 → H1；|rho| > 0.5 且 p < 0.05 且 effect sizes 不递减 → H2；否则 inconclusive
- 删除了 R² < 0.3 → H1 的硬判定

**修复 2: Part A — 统计功效**
- 5-fold → **10-fold** stratified CV
- paired t-test → **bootstrap CI**（1000 resample, seed=42）
- 报告格式：`diff=+0.2582 [0.1493, 0.3642], p=0.0000`

**修复 3: Part A — 多重比较校正**
- 3 对比较加 **Bonferroni 校正**，α = 0.05/3 ≈ 0.0167
- 输出标注 `significant (Bonferroni corrected)` 或 `ns`

### Dry-run 结果
- Part A: 10-fold CV, bootstrap CI + Bonferroni 标注正常；full vs ref 显著 (p=0.0000), ref vs surf 显著 (p=0.0020), full vs surf 不显著
- Part B: Spearman ρ + 4 个 effect sizes + H1/H2/inconclusive 判定正常；hapax_ratio 判为 H1（effect sizes 严格递减 ρ=-1.0, p=0.0）
- Part C: 正常运行

---
