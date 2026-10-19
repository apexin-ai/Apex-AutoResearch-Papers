# code exp014c success gated bonus

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp014c-success-gated-bonus_20260514T124628_result.json`
- **Structured JSON:** [`341fd457e7079a66fd55.json`](../../sessions/34/341fd457e7079a66fd55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出总结

### 1. 修改的文件

**`ragen/env/alfworld/config.py`** — 添加 `success_gated_bonus: bool = False` 字段

**`ragen/env/alfworld/env.py`** — 3 处修改:
- `__init__`: 添加 `self.valid_action_count = 0`
- `reset()`: 添加 `self.valid_action_count = 0`（每 episode 重置）
- `step()`: 重写 reward 逻辑：
  - 每步追踪 `valid_action_count`（不论 gating 模式，metrics 不受影响）
  - `success_gated_bonus=True` 时：仅在 `done and won` 时发放 `valid_action_count * valid_action_bonus`
  - `success_gated_bonus=False` 时：保持原逻辑（每步 unconditional bonus）

**`config/envs.yaml`** — 新增 `AlfworldSG_SuccessGated` 环境定义（`valid_action_bonus: 0.15`, `success_gated_bonus: true`）

### 2. 新 config 文件
`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp014c_success_gated.yaml`

### 3. 注意事项
**resume 路径不存在**: `/root/autodl-tmp/checkpoints/exp008_grpo/global_step_5/` 在磁盘上找不到，仅有 `qwen3_sft_final` 和 `exp008_sft/final`。已将 config 设为 `resume_mode: "disable"` 从 SFT 模型开始。如需从 GRPO checkpoint 恢复，需提供正确路径。

### 4. Dry-run 验证
- Import OK
- Hydra config 解析 OK，所有关键参数正确

### 5. 提交命令（不执行）
```bash
export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p $TMPDIR
export ALFWORLD_DATA=/root/autodl-tmp/alfworld
export RAY_memory_monitor_refresh_ms=0
export RAY_SYSTEM_MEMORY=210000000000
export HYDRA_FULL_ERROR=1
export CUDA_VISIBLE_DEVICES=0,1
cd /root/cost-verify-agent-rl/RAGEN/
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python train.py --config-name=_alfworld_exp014c_success_gated
```

---
