# submit eval xvla l2norm k05 long seed42 v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval_xvla_l2norm_k05_long_seed42_v4_20260524T044822_result.json`
- **Structured JSON:** [`202cd8500b44913bba59.json`](../../sessions/20/202cd8500b44913bba59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 2 上已有一个**完全相同的命令**在跑（pid 447356，已运行 34 分 38 秒）：

```
python -u eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_10 --keep_ratio 0.5 --mode l2_norm --num_episodes 50 --seed 42 --domain_id 3 --gpu 0
```

这看起来就是同一个实验。是否需要：
1. **跳过提交** — 让现有进程继续跑
2. **kill 现有进程再重新提交** — 如果你认为它可能 hang 了
3. **改用 cuda:3**（完全空闲）提交新实验

怎么处理？

---
