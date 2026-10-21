# research coverage audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_coverage-audit_20260516T022507_result.json`
- **Structured JSON:** [`ee96ea4377d08630f30a.json`](../../sessions/ee/ee96ea4377d08630f30a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/_project/report/coverage_audit_0516.md`。

核心结论：

**4 Claims 状态**: C1 🟡 C2 🟡 C3 🟢 C4 🟡

**6 个 Blocking 缺口**（按关键路径）：
1. 3B s42 eval 完成 → T-7
2. 3B signals 计算 → T-6
3. 跨 scale 信号对比表 → T-6
4. 1.5B+3B RRF 聚合 → T-6
5. Pooled IRT fitting (≥3 scales) → T-5
6. ≥1 baseline 对比 → T-5

**关键路径瓶颈**: 3B s42 的 4 个 cell（d000 需 eval，d005/d100 SFT 中，d025 eval 中）。全部完成后才能跑 signals → RRF → pooled IRT → baselines。最早 T-5 (May 20) 开始写 paper。

**兜底方案**: 若 3B s42 来不及，仅用 3B s123 (4 cells) + 1.5B (16 cells) 支撑，N=20 (excl 0.5B)。论点成立但 power 弱。

---
