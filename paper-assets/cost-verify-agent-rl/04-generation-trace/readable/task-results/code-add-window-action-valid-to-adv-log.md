# code add window action valid to adv log

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add-window-action-valid-to-adv-log_20260517T162230_result.json`
- **Structured JSON:** [`0e6a61d2840275bfe756.json`](../../sessions/0e/0e6a61d2840275bfe756.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出总结

### 1. 修改文件
`ragen/trainer/agent_trainer.py` (两台服务器: bjb1-17606, westd-47453)

**新增行**（line 354-364, 375-376 — 修改后行号）：
- 在 logging block 内增加 per-episode cumulative valid ratio 计算逻辑
- 在 `_record` dict 中增加两个字段：
  - `window_action_valid`: 当前 window 的 action validity（0.0 或 1.0，不可用时为 null）
  - `window_action_valid_ratio`: 当前 episode 截至该 window 的 cumulative valid action ratio

**数据来源**: `is_valid` 变量（line 279），从 `data.non_tensor_batch["is_action_valid"]` 获取，在 logging 代码执行时已在作用域内。

### 2. Hot-patch 不可行
PID 945877 (hsweep_h2_seed2) 是 Python 训练进程，`agent_trainer.py` 模块在启动时已加载到内存。磁盘修改不影响运行中进程。修改会在 seed2 完成后的下一次实验中自动生效。

### 3. 启用方式
无需额外配置。只要实验启动时设置 `LOG_PER_SAMPLE_ADV=1`（已有机制），新字段就会自动写入 `advantage_log.jsonl`。向后兼容：如果 `is_action_valid` 数据不可用，两个新字段输出 `null`。

---
