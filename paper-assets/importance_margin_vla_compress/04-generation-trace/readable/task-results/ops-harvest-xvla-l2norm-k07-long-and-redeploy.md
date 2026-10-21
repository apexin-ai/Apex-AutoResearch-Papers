# ops harvest xvla l2norm k07 long and redeploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_xvla_l2norm_k07_long_and_redeploy_20260523T075350_result.json`
- **Structured JSON:** [`02fbc1fc2ab6a082d05d.json`](../../sessions/02/02fbc1fc2ab6a082d05d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有检查完成，汇报结果：

---

### 1. eval_xvla_l2norm_k07_long_seed42 — 已完成

**Overall SR: 49.4%** (247/500), 95% CI: [45.0%, 53.8%]

| Task | SR | Detail |
|------|----|--------|
| T0 | 12% | put both alphabet soup & tomato sauce in basket |
| T1 | 4% | put cream cheese box & butter in basket |
| T2 | 56% | turn on stove & put moka pot |
| T3 | 98% | put black bowl in drawer & close |
| T4 | 68% | put white mug on left, yellow mug on right |
| T5 | 94% | pick up book & place in caddy |
| T6 | 78% | put white mug on plate & chocolate pudding right |
| T7 | 76% | put alphabet soup & cream cheese in basket |
| T8 | 0% | put both moka pots on stove |
| T9 | 8% | put yellow mug in microwave & close |

Registry 已更新（conclusion=success, metrics 已写入）。无 cron 需要删除。

### 2. eval_xvla_l2norm_k05_long_seed42 — 仍在跑

进程 459651 运行中（1h33m），当前 Task 9 ep 42/50，预计几分钟内完成。

### 3. GPU 状态

| GPU | 显存占用 | 状态 |
|-----|----------|------|
| 0 | 1 MiB / 97887 MiB | 空闲 |
| 1 | 1 MiB / 97887 MiB | 空闲 |
| 2 | 4830 MiB / 97887 MiB | k05 eval 占用 |
| 3 | 1 MiB / 97887 MiB | 空闲 |

### 4. 新实验部署 — 无法部署

- **E3 cosine similarity**: 脚本 `analyze_token_cosine_similarity.py` 不存在
- **E4 inference latency**: `measure_inference_latency.py` 存在但**只支持 SmolVLA**（SmartCompress M=32/M=64 vs baseline 128 tokens），不支持 X-VLA，且没有 `--models` 参数

需要你决定：
1. 是否在空闲 GPU 上跑 SmolVLA 版本的 E4 latency（需确认 SmolVLA checkpoints 在这台服务器上）
2. 是否需要为 X-VLA 编写新的 E3/E4 脚本

---
