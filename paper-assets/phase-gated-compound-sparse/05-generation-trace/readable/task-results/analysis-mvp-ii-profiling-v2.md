# analysis mvp ii profiling v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_ii_profiling_v2_20260513T211541_result.json`
- **Structured JSON:** [`70d1aa198066ee3bf9dc.json`](../../sessions/70/70d1aa198066ee3bf9dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。核心结论：

**Verdict: SUCCESS (MVP PASS)**

| 指标 | 结果 |
|------|------|
| P0 修复 | 有效 — KV perplexity 从全 NaN 恢复为可计算值 |
| CI 非重叠 | **PASS** — execution vs reasoning 在 sparsity=0.3 时 CI 不重叠 (exec CI_high=0.67 < reas CI_low=4.09) |
| 符号反转 | **FAIL** — 所有可计算 II 均为正（super-additive），未观察到方向反转 |
| Phase segmentation | 三个 phase 均 ≥20 segments，但分布严重不均（transition 占 90.7%，execution 仅 1.2%） |

**关键发现：**
1. 方向反转假设**未被支持** — 所有 phase 都是 super-additive（compound 永远比 individual 之和更差）
2. **幅度差异显著**：reasoning II (17.8) 约为 transition II (3.1) 的 5.8 倍（sparsity=0.3）
3. MVP PASS 依赖 execution phase 的 ±Inf/NaN 数据（仅 25 segments），统计可靠性存疑

**主要风险：** PASS 的 CI 非重叠源自 execution phase 的 ∞ 值与 reasoning 有限值的对比，而非两个稳健分布的真实分离。需要评估"幅度差异"是否足以支撑 PACS 框架的后续工作。

---
