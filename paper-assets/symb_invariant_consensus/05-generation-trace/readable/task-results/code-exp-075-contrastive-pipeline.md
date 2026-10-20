# code exp 075 contrastive pipeline

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-075-contrastive-pipeline_20260519T164134_result.json`
- **Structured JSON:** [`061cb24ccb3fcd4c1d57.json`](../../sessions/06/061cb24ccb3fcd4c1d57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有任务完成。`run_contrastive.py` 已部署到 `westd-25068:/root/symb_invariant_consensus/run_contrastive.py`，5 题 vLLM dry-run 验证通过。

**实现摘要**：

- **596 行**，三阶段 pipeline：
  - **Phase 1**: 复用 `VLLMGenerator` 生成 K=12 traces + SC 投票确定候选集
  - **Phase 2**: 对每个候选答案，用新设计的 `CONTRASTIVE_PROMPT` 调用 LLM K_contrast=3 次，分别生成 pro/con FOL 约束，每条约束经 `parse_z3_formula` 验证兼容性
  - **Phase 3**: 对每个候选独立运行 MAX-SAT：`score = MAX-SAT(pro) - MAX-SAT(con)`，取最高分答案
- **复用模块**: `VLLMGenerator`, `VLLMBackend`, `ConstraintDeduplicator`, `MaxSATSolver`, `SelfConsistency`, `normalize_logic_answer`
- **特性**: resume 支持、checkpoint、save-intermediates、degenerate case 处理、ETA 估算
- **CLI 接口**与任务要求完全一致
- vLLM 未由本 Worker 启动（复用了已有的 port 8000），无需清理

---
