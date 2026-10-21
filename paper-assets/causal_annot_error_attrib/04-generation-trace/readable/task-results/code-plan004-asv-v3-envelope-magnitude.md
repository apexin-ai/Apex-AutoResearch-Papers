# code plan004 asv v3 envelope magnitude

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan004-asv-v3-envelope-magnitude_20260520T132338_result.json`
- **Structured JSON:** [`57e172e67b1d5dac69ff.json`](../../sessions/57/57e172e67b1d5dac69ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Part 1 — Envelope 单调性**：Raw |bias| 非单调违反 440-1033/1500 点，envelope 违反 = **0**（构造性保证成立）

**Part 2 — 三种 ASV (τ=0.5)**：
- Sign-flip ASV：全部 None（confounding/mediation 结构性安全）
- Magnitude ASV (10%)：0.076–0.487（C0 准确度越高 → ASV 越大 → 越鲁棒）
- Protection ASV (collider)：0.338–2.028

**Part 3 — 小 τ ASV**：
- τ=0.05 magnitude ASV 仅 0.008–0.047（小效应在极小 δ 就不安全）
- τ=0.1 magnitude ASV 0.014–0.093
- MagAbs.05 与效应量无关，值同 τ=0.5

**Part 4 — Coverage**：全部 **100%**（τ=0.05 和 0.1，所有拓扑）

**Part 5 — Type I/II (小 τ)**：
- Confounding/mediation：naive 100% 误拒（偏差远大于效应）；magnitude-ASV-informed 在 H1 下 0% 拒绝（正确标记为不安全，ASV << 1）
- Collider H0：naive 4.6%–37.8%（取决于 C0 准确度）；H1 naive=100%, mag_rej=0%

关键发现：小 τ 下 magnitude ASV 全部远小于 1，说明当前标注误差水平对小效应的因果推断是**不安全的**——这正是 ASV 框架应该报告的结论。

---
