# deploy westd38929 gpu1 l2norm long seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-westd38929-gpu1-l2norm-long-seed43_20260523T233254_result.json`
- **Structured JSON:** [`e7188781b883a8751e32.json`](../../sessions/e7/e7188781b883a8751e32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已部署完成。

- **实验**: `eval_xvla_l2norm_k05_long_seed43`
- **服务器**: westd-38929, GPU 1 (4141 MiB)
- **命令**: `CUDA_VISIBLE_DEVICES=1 python eval_xvla_pruning_libero.py --mode l2_norm --keep_ratio 0.5 --suite libero_10 --domain_id 3 --seed 43 --model_path /root/autodl-tmp/X-VLA-Libero`
- **tmux session**: `eval_xvla_l2norm_k05_long_seed43`
- **日志**: `/tmp/eval_xvla_l2norm_k05_long_seed43.log`
- **状态**: Task 0 已开始运行，预计 ~95 分钟完成

---
