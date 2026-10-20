# analysis narrative review

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_narrative-review_20260515T153824_result.json`
- **Structured JSON:** [`924adccbc847e98563a7.json`](../../sessions/92/924adccbc847e98563a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/narrative_review_d026_d027.md`。核心结论：

**最重要的叙事调整**：Claim 3 需要重新表述。D027 证明"训练不稳定"是误称——训练 loss 跨 seed SD=0.0004，极其稳定。真正的问题是模型稳定地收敛到了不同的（且常常有害的）解，generalization 不可预测。建议新表述：**"stable convergence to harmful solutions"** 而非 "training instability"。

**三个发现的整合位置**：
- D027 training-eval paradox → §4.3 独立 subsection，用 loss 数据构建 memorization 证据
- D026 loop repetition → §5.1 Failure Mode Analysis，作为 fixation 机制解释
- Per-sample loss（待跑）→ 连接 §4.3 和 §5.1 的桥梁

**因果链**：overfit 注入模式（loss 证据）→ 行为 fixation（loop repetition）→ 开放动作空间中 fixation 致命（结构论证）。这条链比原来的"注入=噪声"叙事更深、更有说服力。

---
