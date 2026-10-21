# research cogrouter deep read

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cogrouter-deep-read_20260513T090830_result.json`
- **Structured JSON:** [`d06e2faf5a9b59647f0f.json`](../../sessions/d0/d06e2faf5a9b59647f0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结提取结果：

**ScienceWorld 结果**: CoPO (Qwen2.5-7B) Score=84.6, SR=72.0%, 1543 tokens。超过 GPT-4o (+40.3pp SR)、o3 (+18pp)、GRPO (+19pp)。无 seen/unseen 分拆，无 per-task breakdown，测试集仅 200 simulations。

**方法**: 4 层认知深度（ℒ₁ 直觉→ℒ₄ 战略规划），LLM 自回归生成 level tag 路由（无外部 classifier/模拟器）。CoSFT 用 GPT-4o 轨迹+随机层级分配做冷启动，CoPO 用 confidence-aware advantage reweighting 训练层级选择偏好。

**消融**: 训练后 ℒ₁ 占 55%（GRPO 坍缩到 76% ℒ₄）；去掉 balanced CoSFT → SR -7.5pp；复杂任务自动增加 ℒ₄ 使用率。

**与 SimGate 正交**: CogRouter 路由 thinking depth，SimGate 路由 computation modality。CogRouter 的 ℒ₄ "心理模拟"仍受 LLM 幻觉限制，而 SimGate 用真实模拟器做精确计算——这是关键差异化论点。两者理论上可组合。

已写入 `memory.md` (CogRouter 竞品分析 section) 和服务器 `notes/baselines.md`。

---
