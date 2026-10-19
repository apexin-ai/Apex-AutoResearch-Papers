# code exp028a director corrections

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp028a_director_corrections_20260515T204310_result.json`
- **Structured JSON:** [`3305ad2c1fc96efe872e.json`](../../sessions/33/3305ad2c1fc96efe872e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修正完成。产出总结：

## 修正执行报告

### 修正 1: 删除 exp028_gigpo 配置 ✅
- `_alfworld_exp028_gigpo.yaml` → `_alfworld_exp028_gigpo.yaml.blocked`

### 修正 2: 使用 Qwen3-1.7B ✅
- model_path 改为 `/root/cost-verify-agent-rl/models/Qwen3-1.7B`（本地已验证存在）
- 涉及文件：exp028a、exp028b、prereq_zeroshot 三个 config + 三个启动脚本

### 修正 3: invalid_action_penalty ✅
- **代码已存在完整链路**：`env.py` 检查 `action in admissible_commands` → `ctx_manager.py` 传递 `is_action_valid` → `step_rewards.py` 应用 penalty → `agent_trainer.py` 汇入 GRPO advantage
- 在 `algorithm` 配置段显式添加 `invalid_action_penalty_coef: 0.1`
- `format_penalty` 改回 0（与 exp027 一致，避免 gradient hijacking）
- 单元测试 5/5 通过，验证了：
  - 基本 penalty 逻辑
  - 全失败 group 中不同 invalid 数量产生不同 return（方差 > 0 → 有梯度信号）
  - coef=0 时禁用
  - 成功 + penalty 的叠加正确

### 修正 4: mini_batch_size 保持 32 ✅
- exp028a: 32（已一致）
- exp028b: 256 → 32

### 修正 5: 严格最小变更 ✅
exp028a vs exp027 diff 仅有：
- `model_path`: SFT checkpoint → Qwen3-1.7B
- `algorithm.invalid_action_penalty_coef: 0.1`（显式声明）
- 实验名/路径（预期差异）

LR(5e-7)、env_groups(8)、steps(50)、mini_batch(32)、save_freq(5) 均保持不变。

---
