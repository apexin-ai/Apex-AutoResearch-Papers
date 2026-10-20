# code plan015 curriculum

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan015-curriculum_20260515T005630_result.json`
- **Structured JSON:** [`8b07e89664e118e6be54.json`](../../sessions/8b/8b07e89664e118e6be54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 代码已有 schedule 支持，无需修改

`scripts/train_grpo.py` 已完整实现所有 plan_015 需要的功能：

- **CLI 参数**（L371-374）：`--beta_schedule {fixed,linear,sigmoid}` 和 `--beta_schedule_midpoint`（默认 250）
- **`compute_beta_t()`**（L154-163）：
  - `fixed`: `beta_t = beta`
  - `linear`: `beta_t = beta * min(step / max_steps, 1.0)` — 0 到 beta 线性增长
  - `sigmoid`: `beta_t = beta / (1 + exp(-(step - midpoint) / (T/10)))` — S 曲线
- **step 同步**（L319）：`LocalLogCallback.on_step_end` 将 `state.global_step` 写入 `schedule_state['current_step']`
- **beta_t 记录**（L284-285, L338, L349）：每步的 `beta_t` 写入 `reward_log.jsonl` 和日志

### 2. 训练命令（copy-paste ready）

**Run 1 — Linear ramp**:
```bash
export CUDA_VISIBLE_DEVICES=0
cd /root/solver-trace-ablation
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python3 scripts/train_grpo.py \
  --config configs/grpo_additive_bonus.yaml \
  --data_path data/train_500_seed42.jsonl \
  --num_steps 500 --seed 42 --beta 0.1 \
  --reward_mode additive_bonus \
  --beta_schedule linear \
  --output_dir /root/autodl-tmp/outputs/plan015_linear_s42
```

**Run 2 — Sigmoid**:
```bash
export CUDA_VISIBLE_DEVICES=0
cd /root/solver-trace-ablation
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python3 scripts/train_grpo.py \
  --config configs/grpo_additive_bonus.yaml \
  --data_path data/train_500_seed42.jsonl \
  --num_steps 500 --seed 42 --beta 0.1 \
  --reward_mode additive_bonus \
  --beta_schedule sigmoid --beta_schedule_midpoint 250 \
  --output_dir /root/autodl-tmp/outputs/plan015_sigmoid_s42
```

注意：按 C002 约束，`CUDA_VISIBLE_DEVICES` 使用 `export` 而非 inline 赋值。

### 3. 注意事项

- 两个 run 不能同时跑在同一张 GPU 上（按 C007，提交前需 `nvidia-smi` 确认 GPU 空闲）
- `--config configs/grpo_additive_bonus.yaml` 中的默认值可能覆盖 CLI 的 `--beta 0.1`，需确认 YAML 中 beta 字段的值（config merge 逻辑是 YAML 仅填充 CLI 未设置的值，CLI 显式设置的 `--beta 0.1` 会保留）
- 实际上 config merge 代码（L389-394）只在 `current is None` 时覆盖，`--beta` 默认值是 0.3 不是 None，所以 CLI 传的 `0.1` 会被保留——没问题

---
