# research libero goal assessment

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_libero-goal-assessment_20260515T141212_result.json`
- **Structured JSON:** [`090c2bcc39d6aadcefec.json`](../../sessions/09/090c2bcc39d6aadcefec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/libero_goal_feasibility.md`。核心结论：

**Conditional GO** — LIBERO-Goal 数据完全可用且兼容，instruction-conditioned probe 可行，但有条件：

1. **数据**: 10 tasks × 50 demos，HDF5 格式与现有 pipeline 完全兼容，HuggingFace 直接下载 (6.37 GB)
2. **Probe 设计**: 10-way instruction identity classification，核心实验是 **early-timestep probe** (前 5-20 步，视觉场景几乎相同)，对比 trained VLA vs untrained vs DINO/SigLIP
3. **工时**: 端到端 ~10h（精简层版本 ~6h），不需要修改 `extract_features.py`
4. **与 Grant et al.**: 互补而非重复。他们做 behavioral intervention (success rate 100%→10%)，我们做 representational probing (trained vs untrained + layer-wise)。**Trained vs untrained 对比是 Grant 没有的**
5. **Story 强度**: 单独撑 paper 偏弱（Grant 已覆盖核心 insight），但与 action prediction probe 组合叙事很强——共同回答 "when does VLA training matter?"
6. **最大风险**: 审稿人攻击 "instruction tokens 本身就在 input 里，hidden states 当然有这个信息"。防御靠 untrained baseline（有 tokens 但无 grounding）
7. **前置条件**: 先验证 t=0 视觉相似性（DINO cosine similarity），如果初始帧就有大差异则 abort

---
