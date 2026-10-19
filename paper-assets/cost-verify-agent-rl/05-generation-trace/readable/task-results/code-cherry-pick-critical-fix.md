# code cherry pick critical fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cherry_pick_critical_fix_20260515T085324_result.json`
- **Structured JSON:** [`b53f2f8d4ab72802d6c5.json`](../../sessions/b5/b53f2f8d4ab72802d6c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成，3 个文件改动摘要：

**File 1: `RAGEN/ragen/llm_agent/ctx_manager.py` — `_build_step_independent_samples`**
- L1057-1058: 新增 `is_terminal_list = []`, `is_action_valid_list = []`
- L1077-1078: 每个 episode 预计算 `last_response_idx`（最后一个有 llm_response 的 turn）
- L1118-1119: 内循环中 append `is_terminal`（最后一步=1.0，其余=0.0）和 `is_action_valid`（从 turn dict 取，默认 1.0）
- L1142-1144: 写入 `non_tensor_batch["is_terminal"]`, `["is_action_valid"]`, `["reward"]`

**File 2: `RAGEN/ragen/trainer/agent_trainer.py`**
- 文件已有 `else` 分支 + `_step_ind_logger.warning()` 的 CRITICAL 警告（L271-277），无需额外修改。清理了误加的重复代码。

**File 3: `tests/test_step_independent.py`**
- 新增 Test 6：验证 `is_terminal`, `is_action_valid`, `reward` 字段存在、长度正确、is_terminal 在最后一步为 1.0、is_action_valid 默认 1.0、reward 同 episode 一致。

**测试结果**：`test_step_independent.py` 6/6 PASS，`test_step_rewards.py` 9/9 PASS，两个源文件编译通过。

---
