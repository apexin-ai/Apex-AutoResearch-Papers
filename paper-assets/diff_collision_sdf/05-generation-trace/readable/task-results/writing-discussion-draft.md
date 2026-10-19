# writing discussion draft

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_discussion_draft_20260527T082809_result.json`
- **Structured JSON:** [`cd8904f1315082f868c5.json`](../../sessions/cd/cd8904f1315082f868c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已同步更新。主要改动：

**结构重组**：将原来分散在三个 paragraph（"Two-level failure" + "Why EE-only SDF adds no value" + "Implications"）的机理分析合并为一个核心 paragraph "Why EE-only SDF is redundant: a two-level account"，逻辑更紧凑。

**机理分析强化**：
- **(i) Demo data subsumption**：明确阐述 collision-free demo → distributional shift → implicit avoidance encoding 的因果链，用 per-task CAR fingerprint 不变性和 Phase 2 ablation 作为双重证据
- **(ii) EE-body mismatch**：新增 action space 维度的论证（VLA output delta EE pose, SDF gradient 操作在同一低维空间，无法约束 full joint configuration），补充了 oracle 实验的机理解释（push EE away → rotate unmonitored links through obstacle）
- 两个 level 的**独立性**明确阐述，说明需要同时解决两个问题

**新增内容**：
- Implications 段新增 planning-layer vs action-prediction-layer 的讨论
- Future work 新增 joint-space planning constraints 方向
- Limitations 段加入 `\placeholder` 标记 λ=0.1 30K pending

**写作规范**：无 em-dash，无 `-ing` 结尾句，无 AI 味用词，数值范围用 `\textendash`。

---
