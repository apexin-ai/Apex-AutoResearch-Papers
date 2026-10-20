# paper flyingsquid check

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_flyingsquid-check_20260515T062347_result.json`
- **Structured JSON:** [`df3ba39af03d6c396f0d.json`](../../sessions/df/df3ba39af03d6c396f0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/flyingsquid-check/report.md`。

核心发现：

**数据不一致（1处）**：Table 5 FlyingSquid Conf≥2 F1 论文写 0.7820，registry 为 0.7816（差 0.0004）。建议统一为 0.7816。

**未报告但 registry 有数据（3处）**：
- FlyingSquid 下游 probe F1 = 0.7343（表中标 "---"）
- Conf≥2 子集与 MV 100% 一致（conf2_vs_mv_agreement=1.0）未在论文提及
- Divergent 窗口数 n=9,841 未在正文给出

**叙述完整性**：Snorkel 对比、divergent pattern 方向、i.i.d. 假设违反、root cause 分析均已完整覆盖。

---
