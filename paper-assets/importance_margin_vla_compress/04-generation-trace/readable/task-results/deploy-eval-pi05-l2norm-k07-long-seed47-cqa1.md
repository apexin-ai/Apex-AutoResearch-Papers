# deploy eval pi05 l2norm k07 long seed47 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_eval_pi05_l2norm_k07_long_seed47_cqa1_20260528T222235_result.json`
- **Structured JSON:** [`66537f5bdbfc796d2372.json`](../../sessions/66/66537f5bdbfc796d2372.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动，正在加载 π0.5 模型（从磁盘加载到 CPU，尚未传到 GPU）。

**部署完成：**
- **exp_id**: `eval_pi05_l2norm_k07_long_seed47_w41`
- **服务器**: cqa1-33015, cuda:0
- **tmux session**: `eval_pi05_l2norm_k07_long_seed47_w41`
- **日志**: `~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k07_long_seed47_w41.log`
- **Registry**: RUNNING，spec 已补充完整
- **参数**: `--prune_mode l2norm --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 47 --gpu 0`
- **环境变量**: HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache MUJOCO_GL=egl (符合 C004)

---
