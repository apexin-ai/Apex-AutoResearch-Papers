# code plan013 random reward

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan013-random-reward_20260513T232958_result.json`
- **Structured JSON:** [`a776a798401bb4d78c5d.json`](../../sessions/a7/a776a798401bb4d78c5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

**完成。** 产出总结：

### 新增/修改文件

1. **`configs/grpo_random_reward.yaml`** — plan_013 配置，reward_mode=random_reward，α=0.9, β=0.1，500 steps, K=8, seed=42
2. **`scripts/train_grpo.py`** — 新增 `random_reward` 模式：
   - `import random as _random`（L25）
   - `elif reward_mode == "random_reward"` 分支（L173-186）：proved 样本 reward = 0.9 + 0.1×rand，未 proved = 0；random seed = 样本全局计数器（可复现）
   - argparse choices 加入 `"random_reward"`（L293）

### 提交训练命令

```bash
bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && CUDA_VISIBLE_DEVICES=0 nohup python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml > /root/autodl-tmp/outputs/plan013_random_reward_s42/train.log 2>&1 &'
```

---
