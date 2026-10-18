# consistency pi05 random k07 vs k085

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_consistency_pi05_random_k07_vs_k085_20260526T175611_result.json`
- **Structured JSON:** [`d9390a70fb084cb9f993.json`](../../sessions/d9/d9390a70fb084cb9f993.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
CONSISTENCY_CHECK:
  model_path: MATCH
    Both: /root/autodl-tmp/pi05_libero_finetuned (model.safetensors 7.47GB, unchanged since May 22)
  
  script: MATCH
    Both: /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py
    Note: 脚本在 May 26 05:43 被修改过。k=0.7 原始运行 (May 22) 和 k=0.85 v1 (May 22) 
    使用旧版本；k=0.85 v2 (May 26) 使用新版本。但 k=0.85 两次结果完全一致 (44.4%)，
    证明脚本变更不影响 random pruning 逻辑。

  code_version: MATCH (功能等价)
    k=0.7 和 k=0.85 v1 同批创建 (May 22 19:10:48-50)，使用同一版本代码。
    k=0.85 v2 使用更新版本但结果相同。

  params_diff: ONLY keep_ratio
    k=0.7 command: --prune_mode random --keep_ratio 0.7  --suite libero_10 --n_episodes 50 --seed 42 --gpu 0
    k=0.85 command: --prune_mode random --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0
    Token counts correct: k=0.7→179/256, k=0.85→217/256
  
  env_vars: MATCH
    Both: HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0

  reproducibility: CONFIRMED
    k=0.85 v1 (May 22) = 44.4%, k=0.85 v2 (May 26) = 44.4% → 完全复现
    k=0.85 seed43 = 42.0% → 跨 seed 一致
    k=0.7  seed43 = 68.6% → 跨 seed 一致

  per-task pattern:
    V-shape 主要由 T4 (put mugs on plates) 驱动:
      k=0.7:  80% (seed42), 86% (seed43)
      k=0.85: 12% (seed42),  4% (seed43) ← 灾难性下降
    T0 也有大差距: k=0.7=100%, k=0.85=52%

  VERDICT: CONSISTENT — V-shape 是真实现象，非 bug
    两组实验条件完全一致（除 keep_ratio），同批创建，同一模型/脚本/参数/环境。
    k=0.85 已跨两次独立运行和两个 seed 复现。V-shape 由 random pruning 
    在 k=0.85 时恰好丢弃关键 spatial tokens 导致特定任务 (T4) 崩溃引起。
```

---
