# code exp013 config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp013-config_20260514T075731_result.json`
- **Structured JSON:** [`d582e11fbb31664f36eb.json`](../../sessions/d5/d582e11fbb31664f36eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 已清理完毕。GPU 已释放。

---

## 产出汇总

### 1. 配置 Diff（exp012 vs exp013）

```diff
< experiment_name: exp012-alfworld-reward-fix
> experiment_name: exp013-alfworld-lr-kl-fix

< local_log_dir: "/root/autodl-tmp/checkpoints/exp012_grpo/"
< default_local_dir: "/root/autodl-tmp/checkpoints/exp012_grpo/"
> local_log_dir: "/root/autodl-tmp/checkpoints/exp013_grpo/"
> default_local_dir: "/root/autodl-tmp/checkpoints/exp013_grpo/"

< kl_loss_coef: 0.01
> kl_loss_coef: 0.05
```

注意：`lr` 在 exp012 配置中**已是 1e-6**（非用户预期的 5e-6），保持不变。

### 2. Pre-flight Checklist

| 项目 | 状态 |
|------|------|
| 入口点 `train.py` | ✓ |
| Checkpoint `exp008_grpo/global_step_5` | ✓ |
| 磁盘 23GB 可用 | ✓ |
| GPU 2× RTX PRO 6000 96GB 空闲 | ✓ |

### 3. Dry-run 结果

✓ 无 Traceback/Error
✓ Qwen3 1.72B 加载成功
✓ Checkpoint (model + optimizer + rng + lr_scheduler) 从 step_5 恢复
✓ AlfWorld 3553 games / 494 envs 初始化完成
✓ vLLM 引擎启动，进入 val_before_train rollout

### 4. 启动命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p $TMPDIR && \
export ALFWORLD_DATA=/root/autodl-tmp/alfworld && \
export CUDA_VISIBLE_DEVICES=0,1 && \
cd /root/cost-verify-agent-rl/RAGEN && \
nohup python train.py --config-name _alfworld_exp013_lr_kl_fix > /root/autodl-tmp/checkpoints/exp013_grpo/train.log 2>&1 &
```

---
