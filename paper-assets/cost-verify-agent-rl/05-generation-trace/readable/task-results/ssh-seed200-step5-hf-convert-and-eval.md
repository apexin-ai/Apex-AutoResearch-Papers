# ssh seed200 step5 hf convert and eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_seed200_step5_hf_convert_and_eval_20260523T011103_result.json`
- **Structured JSON:** [`5295f06fff6ad3f2d6d3.json`](../../sessions/52/5295f06fff6ad3f2d6d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。验证清单：

- [x] 训练进程 PID 467039 已退出
- [x] FSDP checkpoint 存在（2 rank × model + optim + extra_state）
- [x] HF checkpoint 转换成功：`/root/autodl-tmp/checkpoints/qwen_exp029_seed200_step5_hf`，1,720,574,976 参数，可正常加载
- [x] eval config 已创建：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_seed200_step5_ood_eval.yaml`
- [x] 启动命令如下

**LAUNCH_COMMAND:**
```
bash -c "cd /root/cost-verify-agent-rl/RAGEN && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && WANDB_DIR=/root/autodl-tmp/wandb_tmp python train.py --config-name _alfworld_seed200_step5_ood_eval enable_response_mask=false actor_rollout_ref.model.enable_response_mask=false"
```

---
