# code exp012 reward fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp012-reward-fix_20260514T055810_result.json`
- **Structured JSON:** [`a487f76860e91d01692f.json`](../../sessions/a4/a487f76860e91d01692f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过，所有关键字段正确。

### 产出汇总

| 项目 | 结果 |
|------|------|
| **Config 文件** | `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp012_reward_fix.yaml` |
| **format_penalty** | `0`（原 `-0.1`），定义在 `es_manager.py:236`，从 config 读取 |
| **group_size** | `16`（原 `8`） |
| **Step 5 checkpoint** | 存在：`/root/autodl-tmp/checkpoints/exp008_grpo/global_step_5/`（FSDP 2-rank） |
| **Resume 机制** | `resume_mode: "resume_path"` + `resume_from_path` |
| **Dry-run** | 通过 |

### exp012 启动命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p $TMPDIR && \
export ALFWORLD_DATA=/root/autodl-tmp/alfworld && \
cd /root/cost-verify-agent-rl/RAGEN && \
nohup python -m ragen.llm_agent.agent_proxy --config-name _alfworld_exp012_reward_fix \
  > /root/autodl-tmp/exp012_grpo.log 2>&1 &
```

### exp008 → exp012 diff

- `format_penalty`: `-0.1` → `0`
- `es_manager.train.group_size`: `8` → `16`
- `trainer.resume_mode`: (unset/disable) → `"resume_path"`
- `trainer.resume_from_path`: (unset) → `"/root/autodl-tmp/checkpoints/exp008_grpo/global_step_5"`
- `trainer.default_local_dir` / `local_log_dir`: `exp008_grpo/` → `exp012_grpo/`
- `trainer.experiment_name`: `exp008-alfworld-sft-grpo` → `exp012-alfworld-reward-fix`

---
