# ssh seed7 eval westd

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_seed7_eval_westd_20260522T223403_result.json`
- **Structured JSON:** [`8cd8d073708c47fada3f.json`](../../sessions/8c/8cd8d073708c47fada3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

### 产出

**配置文件**: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_seed7_high_kl_step5_ood_eval_westd.yaml` — 已创建，D134 协议参数全部就位：
- `enable_think: True` (agent_proxy 下)
- `enable_response_mask: false` (YAML 顶级 + actor_rollout_ref.model 双重设置)
- `context_window_mode: full`
- `temperature: 0.4` (val_kwargs)
- 134 OOD tasks, `seed.val: 321`
- model_path → `/root/autodl-tmp/checkpoints/qwen_exp029_seed7_high_kl_step5_hf`

**Checkpoint 验证**: OK — 1720.6M params，加载正常。

**启动命令**:

```bash
bash -c "cd /root/cost-verify-agent-rl/RAGEN && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && WANDB_DIR=/root/autodl-tmp/wandb_tmp python3 -m verl.trainer.main_ppo --config-name _alfworld_seed7_high_kl_step5_ood_eval_westd enable_response_mask=false actor_rollout_ref.model.enable_response_mask=false"
```

---
