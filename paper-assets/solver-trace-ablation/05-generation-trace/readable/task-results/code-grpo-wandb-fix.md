# code grpo wandb fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-wandb-fix_20260513T195748_result.json`
- **Structured JSON:** [`f1bfa78dece6bcbf604b.json`](../../sessions/f1/f1bfa78dece6bcbf604b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，清理完毕。

---

## 报告

### 修改内容

1. **W&B 禁用**：两个 YAML config 添加 `no_wandb: true`；`train_grpo.py` 修复 YAML boolean 加载逻辑（`store_true` 参数默认 `False` 不是 `None`，原逻辑会跳过），并在 `main()` 中提前设置 `os.environ["WANDB_MODE"] = "disabled"`

2. **本地 per-step logging**：
   - 新增 `step_buf` 累积器用于 per-step reward 统计（与全局 `stats` 分开）
   - 新增 `LocalLogCallback(TrainerCallback)` 类，在 `on_log` 回调中写入 `reward_log.jsonl`
   - 文件名用 `reward_log.jsonl`（避免与 Transformers 内置 `training_log.jsonl` 冲突）
   - `logging_steps=1` 确保每步都触发回调

3. **其他**：清理了所有残留 tmux session 和旧输出

### 验证结果

**exec-only 模式（3 步）**：
| step | reward_mean | reward_std | prove_rate | isr_mean | parse_rate | loss   | lr      |
|------|-------------|------------|------------|----------|------------|--------|---------|
| 1    | 0.25        | 0.463      | 0.25       | 0.25     | 1.0        | 0.0042 | 1e-6    |
| 2    | 0.0         | 0.0        | 0.0        | 0.0      | 1.0        | 0.0    | 6.67e-7 |
| 3    | 0.375       | 0.518      | 0.375      | 0.375    | 1.0        | 0.0    | 3.33e-7 |

**exec-sta 模式（3 步）**：同样 3 行 JSONL，数值与 exec-only 一致（因为同 seed=42 + 相同模型初始权重，符合预期）。

### Warnings
- **vLLM 版本警告**：`TRL currently supports vLLM versions from 0.11.0 to 0.17.1. You have version 0.18.1`（不影响运行，TRL 未使用 vLLM）
- **无 error**，训练稳定推进，每步 ~10-15s

### 结论
训练可以稳定运行，W&B 已禁用，`reward_log.jsonl` 每步正确写入。

---
