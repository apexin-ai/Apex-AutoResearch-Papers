# research model collapse literature

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_model-collapse-literature_20260519T031633_result.json`
- **Structured JSON:** [`2d425bd03ccc77e3e70f.json`](../../sessions/2d/2d425bd03ccc77e3e70f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。结果写入 `artifacts/model_collapse_literature_notes.md`。

**核心发现**：

references.bib 已包含 12 篇 model collapse 相关文献，覆盖非常充分。**唯一需要添加的是 Bertrand et al. (ICLR 2024 Spotlight)**，提供迭代再训练的稳定性理论框架，直接解释 retrain-chain 行为。

**Positioning 核心论点**（已附可直接用于 Discussion 的段落）：

Model collapse 文献关注质量退化（分布尾部消失、多样性下降），我们的发现揭示同一现象的另一面：每代分布漂移同时产生可检测的代际签名。Retrain-chain 因每代修改模型权重（LoRA），分布漂移远大于 prompt-chain（权重冻结），解释了 K*≥7 vs. K*=2 的差异。纯合成循环的理论不稳定性（Bertrand et al., Gerstgrasser et al.）正是代际可区分性的来源。

---
