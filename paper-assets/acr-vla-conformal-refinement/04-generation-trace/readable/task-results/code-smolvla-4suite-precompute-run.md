# code smolvla 4suite precompute run

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_smolvla-4suite-precompute-run_20260522T143700_result.json`
- **Structured JSON:** [`257c5766a281a77367de.json`](../../sessions/25/257c5766a281a77367de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现状汇总：

**bjb2-28827** — 6 张 GPU 全部占用：
| GPU | 任务 | 状态 |
|-----|------|------|
| cuda:0-2 | SmolVLA Long eval (seed 0/1/2) | 运行中，6.3GB/卡 |
| cuda:3-5 | π0.5 Goal precompute (3 shard) | 运行中 6.5h，各到 10000 samples |

**bjb2-40593** — 1×4090D：
- PID 23742: OpenVLA-OFT object eval，跑了 15h，**0% GPU 利用率**（16.4GB 显存），大概率已完成或卡住
- 代码目录缺 `lerobot_precompute.py`
- 模型和数据已就位

**已有缓存**：`/root/autodl-tmp/crm_cache_smolvla/object/` 已完成但 K=5，需要重新跑 K=10

**SmolVLA precompute 速度估算**：Object (3020 samples, K=5) ~7min → K=10 约 14min。4 suites 串行约 2h。

---

**需要你确认：**

1. bjb2-40593 上那个 15h 0% 利用率的 OpenVLA-OFT eval（PID 23742），可以 kill 吗？
2. cache_dir 用 `/root/autodl-tmp/crm_cache_smolvla_v1/` 还是默认的 `/root/autodl-tmp/crm_cache_smolvla/`（会覆盖已有 K=5 的 object）？
3. 是等 bjb2-28827 的 cuda:3-5 空出来（π0.5 Goal precompute 剩余时间未知），还是先在 bjb2-40593 单卡串行跑起来？

---
