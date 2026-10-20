# analysis phase2 semantic and full s1

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_semantic_and_full_s1_20260514T003508_result.json`
- **Structured JSON:** [`165b2d73d230766195c2.json`](../../sessions/16/165b2d73d230766195c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

我会停止频繁轮询。当前状况和已有分析结果的总结：

---

## 当前进度
- **semantic_only**: 127/551 (23%), ~2-3/min → 预计还需 ~140-200 min
- **full_s1**: 192/551 (35%), ~3-4/min → 预计还需 ~90-120 min

速率比初始阶段慢（数据集后半部分文本更长）。

## 已有的部分分析结果（108 样本，信号已稳定）

**核心结论已经明确，全量数据只会微调数字：**

### semantic_only = 负面结果
- DR violation 16.4%，比 unconstrained (15.4%) 更高
- TypeConstraintProcessor 单独使用反而增加违规率
- 可能原因：语义约束独立修改 entity type logits，但未配合 grammar 约束 relation name，导致类型组合更不协调

### full_s1 (grammar+semantic) = 强正面结果
- DR violation 0.56%（从 15.4% 降至 0.56%，降幅 96%）
- 仅 Evaluate-for 有残余 DR violations
- RV=0%, ET=0% 
- 代价：CF violation 从 0.08% 升至 12.3%（跨关系类型不一致）

### F1 无显著损失
- Entity F1: ±1.5pp 波动范围
- Relation F1: 略有提升

---

两个实验还在 tmux 中运行，`monitor_analysis` 脚本会在完成后自动执行 `analyze_phase2.py`。完成后我会运行完整分析、更新 registry、写分析总结。

如果你想让我现在就基于部分结果更新 registry 并先写分析总结，告诉我。否则我会等全量数据。

---
