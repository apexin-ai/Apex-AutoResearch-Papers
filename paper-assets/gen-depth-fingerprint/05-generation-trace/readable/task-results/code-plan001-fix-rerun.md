# code plan001 fix rerun

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-fix-rerun_20260514T184556_result.json`
- **Structured JSON:** [`40266eedb4b24c55ffc9.json`](../../sessions/40/40266eedb4b24c55ffc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。修改摘要：

**Part A — Bootstrap CI（新增）**
- 对每组 feature set 的 5-fold macro-F1 scores 做 1000 次 bootstrap，报告 95% CI
- 保留 paired t-test 作为对照

**Part B — H1/H2 Trend Analysis（重写）**
- `linregress` → `spearmanr`，用 Spearman ρ 和 p-value 判定趋势
- 新增 `cohens_d()` 计算每对相邻深度的 effect size（d_01 ~ d_34）
- 检查 effect size 序列是否递减（attractor/convergence 证据）
- 删除 R²<0.3→H1 硬判定，新逻辑：|ρ|>0.5 且 p<0.05 → H2 (drift)，否则 H1 (near-stationary)
- 图表改用 std error bars，标注 ρ 和 p-value（不再标 R²）
- JSON 输出格式按要求更新

**Part C — Perplexity 补充分析（增强）**
- 新增 per-depth median PPL
- 新增 PPL>100 样本占比 (high_ppl_ratio)
- 新增退化文本检测（重复 token >50% 或长度 <20 tokens）
- 新增 clean PPL 统计（过滤退化样本后的 mean/median/n）
- 新增 Kruskal-Wallis clean 版本
- 打印前 5 个退化样本预览
- JSON 输出格式按要求更新

**运行状态**
- PID 101585，日志 `/tmp/plan-001-fix.log`
- Cron 每 3 分钟自动检查进度

---
