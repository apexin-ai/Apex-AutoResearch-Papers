# research d098 correlational analysis

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d098_correlational_analysis_20260522T063947_result.json`
- **Structured JSON:** [`515d4db0657f20a44374.json`](../../sessions/51/515d4db0657f20a44374.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果写入 `artifacts/d098_correlational_analysis.md`。

核心发现：

- **Spearman ρ = 0.583, p = 0.099, n = 9** — 正向趋势但未达显著性阈值
- 所有 within-suite 比较方向一致：R² Δ 更大的架构在同一 suite 上 SR 也更高（Goal suite n=3 完美单调）
- Within OpenVLA (n=3) 完美 rank 相关；within TracVLA (n=4) 弱相关（ρ=0.4），Long suite 打破单调性
- 主要 confound：架构容量差异和 suite 难度效应，有效自由度接近 3（架构数）而非 9

**结论**：方向性证据支持 exit collapse 与 task performance 的关联，但不足以宣称显著的 functional connection。需要更多架构才能脱离 confound。

---
