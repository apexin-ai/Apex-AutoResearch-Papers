# analysis c3 extreme batch n

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c3_extreme_batch_n_20260522T082600_result.json`
- **Structured JSON:** [`2d7da572df1ff344659f.json`](../../sessions/2d/2d7da572df1ff344659f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**Figure 1b 确认为 N=1 vs N=1 单 batch 比较。** 所有三个 pool size（16/40/80-rel）均使用贪心构造的单个极端 batch。

核心发现：

1. **80-rel 的 CI [17.7, 42.7] 是实例级 bootstrap**（对 96 个 test instance 重采样），不是 batch 级复制。`bootstrap_ci.py` 源码确认了这一点。

2. **严重程度低于预期。** 论文已有充分的多 batch 证据作为主力支撑：
   - 100-batch 回归 R²=0.218, p<0.001（主证据）
   - 25v25 对比 Δ=25.5pp, r=-0.919（prompt sensitivity 部分）
   - 四分位对比 Δ=-5.3pp, N=25 per group
   - 论文已在正文中承认 "based on a single extreme batch per BCS level"

3. **真正的风险**：Figure 1b 的 bar chart 视觉权重超过其统计权重。读者会将每根柱子理解为有重复的均值，而非 N=1 单点。5v5 对比（同一数据）的 Δ=7.92pp 且 CI 跨零（不显著），暴露了 batch 级变异的问题。

4. **建议**：将 Figure 1b 降级为 illustrative example（论文已部分这样做），主证据地位交给 100-batch 回归分析。或用 scatter plot 替换 bar chart。

报告已保存并注册：`analysis_c3_extreme_batch_n.md`

---
