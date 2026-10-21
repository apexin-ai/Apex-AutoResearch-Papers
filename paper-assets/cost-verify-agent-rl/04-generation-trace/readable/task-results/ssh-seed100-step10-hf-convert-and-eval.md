# ssh seed100 step10 hf convert and eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_seed100_step10_hf_convert_and_eval_20260523T003121_result.json`
- **Structured JSON:** [`f4f1d376f85088f102c4.json`](../../sessions/f4/f4f1d376f85088f102c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 产出

**1. HF checkpoint**
- 路径：`/root/autodl-tmp/checkpoints/qwen_exp029_seed100_step10_hf`
- 参数量：1,720,574,976 (~1.7B，实际是 Qwen2.5-1.5B，不是 3B)

**2. Eval config**
- 路径：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_seed100_step10_ood_eval.yaml`

**3. Eval 启动命令**（未执行）：
```bash
bash -c "cd /root/cost-verify-agent-rl/RAGEN && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && WANDB_DIR=/root/autodl-tmp/wandb_tmp python train.py --config-name _alfworld_seed100_step10_ood_eval enable_response_mask=false actor_rollout_ref.model.enable_response_mask=false"
```

---
