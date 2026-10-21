# research phase b prep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_phase-b-prep_20260514T064739_result.json`
- **Structured JSON:** [`893c7c01544756b51226.json`](../../sessions/89/893c7c01544756b51226.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase B 启动准备完成。Checklist 已写入 `artifacts/phase_b_prep_checklist.md`。

核心发现：

1. **FSDP→HF 转换**: veRL 内置 `python -m verl.model_merger merge --backend fsdp` 直接可用，已确认 checkpoint 格式匹配（world_size=2, FSDP v1）

2. **Phase B 配置**: `_alfworld_phase_b.yaml` 存在，需改 3 个字段（model_path, experiment_name, local_log_dir），建议补 `max_prompt_length: 4096`

3. **biavr_changed bug**: 已修复。`_compute_and_update_a_pre()` 正确计算 greedy counterfactual action 并通过 `compare_actions()` 更新 changed 标志

4. **阻塞项**: 仅 Phase A exp012b 完成 + 验收通过。代码侧零阻塞。

---
