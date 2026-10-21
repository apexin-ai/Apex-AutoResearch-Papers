# ssh urgent check 3 experiments

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_check_3_experiments_20260517T040955_result.json`
- **Structured JSON:** [`4745e464b69deecdfbdd.json`](../../sessions/47/4745e464b69deecdfbdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态

| 实验 | 服务器 | 训练状态 | Eval PPL | GPU 状态 |
|------|--------|---------|---------|---------|
| random_reweight_v2 | 47453 | 进行中 (7305/8477, 86%) ETA ~6min | 待跑 | GPU0 占用 77% |
| rho02_adaptive_tau09 | 47453 | 进行中 (4272/8477, 50%) ETA ~22min | 待跑 | GPU1 占用 93% |
| batchsize16_nmin8 | 41312 | 进行中 (1499/6103, 25%) ETA ~9.5h | 待跑 | GPU2 占用 100% |

## GPU 空闲情况
- **westd-47453**: 4×RTX PRO 6000 Black 全部占用（GPU0: 77%, GPU1: 93%, GPU2: 99%, GPU3: 100%）
- **westd-41312**: 4×RTX PRO 6000 Black 全部占用（GPU0: 83%, GPU1: 78%, GPU2: 100%, GPU3: 100%）

**无空闲 GPU。**

## 关键信息

- **random_reweight_v2** 约 6 分钟后完成（3.25 it/s），输出在 `/root/autodl-tmp/output/models/random_reweight_v2_seed42/`
- **rho02_adaptive_tau09** 约 22 分钟后完成
- **batchsize16_nmin8** 还需约 9.5 小时（batch_size=16 导致 steps 更少但每 step 更慢）

是否需要我等 random_reweight_v2 完成后自动跑 eval？它最快 6 分钟就能结束。

---
