# code d019 script dedup

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d019-script-dedup_20260515T170423_result.json`
- **Structured JSON:** [`e200dc88a386ab854235.json`](../../sessions/e2/e200dc88a386ab854235.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**已删除：**
- `scripts/train_instruction_probes.py`
- `scripts/train_goal_probe.py`
- `scripts/analyze_goal_results.py`

**保留：**
- `scripts/train_probes.py`（`--probe_type goal_classification` 正常工作）
- `scripts/analyze_goal_probes.py`

**`train_instruction_probes.py` 独特功能记录：**
- `--dino_visual_gate` flag（行 73）— 在 t=0 计算 DINO cosine similarity 作为 visual gate
- `compute_visual_gate()` 函数（行 320）— 实现 DINO 特征余弦相似度检查
- 相关逻辑在行 377-390（gate 执行 + 结果保存为 `visual_gate.json`）

该功能已由 `visual_similarity_gate.py` 独立实现，无需合并。

---
