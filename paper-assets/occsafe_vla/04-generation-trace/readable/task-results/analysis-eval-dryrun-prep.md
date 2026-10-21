# analysis eval dryrun prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_dryrun_prep_20260525T061953_result.json`
- **Structured JSON:** [`a470a71c9ecccefbe43a.json`](../../sessions/a4/a470a71c9ecccefbe43a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总：**

| 项目 | 状态 |
|------|------|
| eval 脚本创建（10894） | `eval_34685_batch.sh` + `eval_cmds/` 4个独立脚本 |
| dry-run（10894 cuda:2） | 通过 — 模型加载、MUJOCO EGL 初始化均正常 |
| 部署到 34685 | 5个脚本已部署到 34685 同路径 |

**Checkpoint 路径格式：**
```
/root/autodl-tmp/checkpoints/{exp_id}/openvla-7b+...--image_aug--{exp_id}--50000_chkpt
```

**训练完成后在 34685 上启动 eval：**
```bash
# 4个GPU并行，每个nohup独立跑
nohup bash eval_cmds/eval_cutoff_25k_s2_v3.sh > /tmp/eval_cutoff_25k_s2_v3.log 2>&1 &
nohup bash eval_cmds/eval_reverse_cutoff_s2_v3.sh > /tmp/eval_reverse_cutoff_s2_v3.log 2>&1 &
nohup bash eval_cmds/eval_cutoff_45k_s1_v3.sh > /tmp/eval_cutoff_45k_s1_v3.log 2>&1 &
nohup bash eval_cmds/eval_cutoff_15k_s2_v2.sh > /tmp/eval_cutoff_15k_s2_v2.log 2>&1 &
```

---
