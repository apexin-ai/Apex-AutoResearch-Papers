# code intervention c hard cap

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_intervention_c_hard_cap_20260521T210801_result.json`
- **Structured JSON:** [`2e816c96dc804ebb1591.json`](../../sessions/2e/2e816c96dc804ebb1591.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已提交。汇报产出：

### 1. agent_trainer.py Revert
- 已删除 lines 1545-1558 的 `_lp_coef`/`_lp_threshold` 响应长度惩罚代码块（14行）
- grep 确认 `_lp_coef`、`response_length_penalty` 在文件中无残留
- 其他功能代码（GiGPO、step_rewards、B-IAVR 等）保持不动

### 2. Hard Cap 机制调研
- **`max_turn`**：在 `agent_proxy.py:259` 通过 `for i in range(max_turn)` 控制最大交互轮数，机制完善，直接可用
- **`response_length`**：在 `VllmWrapperWg` 中作为 `max_tokens` 传入 vLLM SamplingParams，控制 per-turn 生成上限
- **`max_response_length`**（data 级）：仅在 verl 单轮 setup 中使用，不影响 agent proxy 多轮流程，无需设置
- **方案**：`response_length: 512` + `max_turn: 20`，最坏情况总 trajectory ≤ 10,240 tokens（原 1024×50 = 51,200）

### 3. Config 参数

| 参数 | 值 | 对比 Seed 7 |
|------|-----|------------|
| seed.train | 999 | 相同 |
| total_training_steps | 7 | 7 vs 15 |
| response_length | 512 | 512 vs 1024 |
| max_turn | 20 | 20 vs 50 |
| kl_loss_coef | 0.01 | 相同 |
| response_length_penalty_coef | 0 | 安全措施 |
| val env_groups | 32 | ≥16（满足 C003） |

### 4. 训练提交确认
- **PID**: 788147
- **Server**: westd-47453
- **GPU**: cuda:0, cuda:1
- **tmux session**: `intervention-c-hard-cap`
- **Log**: `~/runs/cost-verify-agent-rl/intervention-c-hard-cap.log`
- **W&B experiment**: `intervention-c-hard-cap`

---
