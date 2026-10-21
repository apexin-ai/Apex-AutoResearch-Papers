# deploy smolvla precompute spatial goal

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_smolvla-precompute-spatial-goal_20260522T160632_result.json`
- **Structured JSON:** [`65c171648c22307ee99f.json`](../../sessions/65/65c171648c22307ee99f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前 GPU 实际占用与预期不同：

| GPU | 占用 | 进程 |
|-----|------|------|
| 0 | 1.8 GB | eval-lerobot-long-seed0（运行中）|
| 1 | 7.0 GB | eval-lerobot-long-seed1 + **precompute-object-fixed**（`CUDA_VISIBLE_DEVICES=1`）|
| 2 | 1.8 GB | eval-lerobot-long-seed2（运行中）|
| 3 | 9.8 GB | Pi05 goal precompute shard0（已跑 8h）|
| 4 | 9.8 GB | Pi05 goal precompute shard1（已跑 8h）|
| 5 | 9.8 GB | Pi05 goal precompute shard2（已跑 8h）|

**GPU 4/5 不空闲**，被 Pi05 goal precompute 占着。Object precompute 实际在 GPU 1 上（不是 3），占 ~5 GB。

之前创建的 `precompute-smolvla-{spatial,goal,object}-k10` sessions 都是空的，从未成功启动。

**方案**：GPU 0 和 2 各剩 ~22 GB，SmolVLA precompute 只需 ~5 GB。可以与 eval 共存，在 GPU 0 跑 Spatial，GPU 2 跑 Goal。要这样做吗？还是等 Pi05 结束腾出 GPU 3-5？

Object precompute 的实际参数：
```
CUDA_VISIBLE_DEVICES=1 python src/lerobot_native_precompute.py --benchmark object --K 10 --output_dir /root/autodl-tmp/crm_cache_lerobot_k10/
```

---
