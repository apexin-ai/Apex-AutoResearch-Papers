# research framing draft

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_framing_draft_20260515T184252_result.json`
- **Structured JSON:** [`7823fbb5533f1e4e0929.json`](../../sessions/78/7823fbb5533f1e4e0929.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。摘要：

**Core Insight**: 大多数 self-verification 是 confirmatory 而非 corrective——不改变 agent 行为。用 action change 作为 reward signal，RL 可以训练 agent 只在 verification 真正 informative 时触发验证，实现 cost-efficiency。

**三个 Claims**:
1. **Selective verification reduces cost while preserving performance** (moderate) — 最强 claim，需 always-on baseline ≥50% + B-IAVR verification ↓40%+ 且 success 持平。当前证据全部缺失，依赖 exp027 pass + Phase B。
2. **Action change 是有效的 verification informativeness reward** (moderate) — 需训练收敛 + ablation。尚未验证。
3. **Learned policy > heuristic baselines** (weak) — 需完整 ablation 矩阵（always-on / no-verify / random-p / confidence-threshold）。

**最大 Reviewer Concern**: **Baseline performance insufficient** — cost-efficiency story 的前提是 always-on baseline 本身要够强（≥50%）。如果 baseline 只有 20-30%，"省验证开销"在一个本就很弱的系统上没有实际意义。这是当前最大风险，因为 exp027 的 MVP 阈值仅 20%，距 50% 的论文门槛还有很大 gap。

---
