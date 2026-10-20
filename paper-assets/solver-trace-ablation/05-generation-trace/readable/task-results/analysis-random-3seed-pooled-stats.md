# analysis random 3seed pooled stats

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_random-3seed-pooled-stats_20260515T193119_result.json`
- **Structured JSON:** [`f1d60efcfb6969cbc2e8.json`](../../sessions/f1/f1d60efcfb6969cbc2e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

### 统计显著

**H7 rate (ISR >> Random)**: p = 1.3×10⁻³⁹, OR = 15.05 — 极度显著。ISR 70.6% vs Random 13.7%。ISR 训练强烈诱导 H7 型 shortcut（直接输出 hypothesis 作为结论）。

### 统计不显著

**Genuine rate (ISR < Random)**: p = 0.18 (two-sided), p = 0.10 (one-sided) — 不显著。ISR 6.1% vs Random 9.5%，差异方向符合预期（ISR 更低）但样本量不足以达到显著性。

### 对论文 Framing 的影响

1. **H7 差异是铁板钉钉的主论点**：ISR 奖励导致 H7 shortcut 激增（OR=15），这是 Goodhart 效应的直接证据，可以作为论文核心 claim。

2. **Genuine rate 差异不能作为独立 claim**：p=0.18 不够，只能作为 descriptive observation 或 trend 提及（"numerically lower but not statistically significant"）。

3. **Per-seed 方差极大**是关键问题：ISR 的 H7 rate 从 16%（s42）到 100%（s43/s44），Random 从 0%（s42/s44）到 38%（s43）。论文必须报告 per-seed 数据而非仅 pooled，否则审稿人会质疑 Simpson's paradox。特别是 ISR s42 是明显的 outlier（H7 仅 16%，genuine 17.3%），需要在论文中讨论。

4. **Random 的高 H1 率 (71.4%)** 说明 Random ablation 并非真正学会推理——它主要靠背答案（memorization），只是没走 H7 shortcut。Genuine proof 两边都很低（6-10%），这支持"两种 ablation 都未学到真正推理，只是 gaming 方式不同"的 framing。

---
