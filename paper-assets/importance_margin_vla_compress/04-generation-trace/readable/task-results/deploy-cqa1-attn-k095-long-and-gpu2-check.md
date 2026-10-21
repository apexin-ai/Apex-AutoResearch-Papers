# deploy cqa1 attn k095 long and gpu2 check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_attn_k095_long_and_gpu2_check_20260526T165103_result.json`
- **Structured JSON:** [`d1151c88f9ea3da4aeb2.json`](../../sessions/d1/d1151c88f9ea3da4aeb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 任务 1 结果

```
GPU2_STATUS: alive
GPU2_PID: 467731
GPU2_PROCESS: eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 (不是 Attn k=0.5)
GPU3_STATUS: idle
GPU3_PID: none
```

**注意：** GPU 2 上运行的是 `random k=0.7`，不是 `attention k=0.5`。

## 任务 2 结果

已部署 `eval_pi05_attn_k095_long_seed42` 到 GPU 3：

- tmux session: `eval_pi05_attn_k095_long_seed42` ✓
- PID: 546282
- log: `~/runs/importance_margin_vla_compress/eval_pi05_attn_k095_long_seed42.log`
- 日志显示模型正在加载 (`Loading pi0.5 from /root/autodl-tmp/pi05_libero_finetuned`)
- GPU 3 显存尚未上涨（CPU 加载阶段，π0.5 模型较大，属正常现象）

命令：
```
CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u eval_pi05_pruning_libero.py \
  --prune_mode attention --keep_ratio 0.95 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0
```

---
