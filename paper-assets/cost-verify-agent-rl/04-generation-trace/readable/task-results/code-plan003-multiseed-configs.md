# code plan003 multiseed configs

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan003_multiseed_configs_20260517T031806_result.json`
- **Structured JSON:** [`a0ec1357dd8cc455c66b.json`](../../sessions/a0/a0ec1357dd8cc455c66b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本语法验证通过。总结：

## 完成情况

**脚本已创建**: `/root/cost-verify-agent-rl/scripts/launch_multiseed.sh`

**关键发现**:

| 项目 | 结果 |
|------|------|
| exp029 原始 seed | `seed.train=10000`, `seed.val=123`（继承自 base.yaml，未覆盖） |
| seed 设置方式 | Hydra CLI override: `seed.train=X seed.val=X` |
| 配置路径 | `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_episode_level.yaml` |
| Trajectory tracker | `VERL_ENABLE_TRACKER=1` + `VERL_TRACKER_HDFS_DIR=&lt;path>` 可启用，但这是 tensor-level HDFS dump，不是 per-step 文本 trajectory 记录 |

**脚本用法**:
```bash
bash /root/cost-verify-agent-rl/scripts/launch_multiseed.sh &lt;seed> [gpu_ids]
# 例: bash launch_multiseed.sh 2 "0,1"
```

**plan_003 需要跑的 4 个 seed**:
- `bash launch_multiseed.sh 2 "0,1"`
- `bash launch_multiseed.sh 3 "0,1"`
- `bash launch_multiseed.sh 4 "0,1"`
- `bash launch_multiseed.sh 5 "0,1"`

原始 exp029 的 seed=10000（将作为第 5 个数据点），multi-seed 实验用 seed 2-5，W&B run name 为 `exp029_multiseed_s{2,3,4,5}`，checkpoint 存入 `/root/autodl-tmp/checkpoints/exp029_multiseed/seed{N}/`。

由于只有 2 张 GPU 且 exp029 正在运行，这 4 个 seed 需等 exp029 结束后串行跑。

---
