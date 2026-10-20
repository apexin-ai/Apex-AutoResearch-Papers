# ops gpu status check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260516T062852_result.json`
- **Structured JSON:** [`4193980c13e394893033.json`](../../sessions/41/4193980c13e394893033.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

### GPU 状态

| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| cuda:0 | **0 MiB** / 32G | 0% | **空闲**（eval-rp-s42 已完成） |
| cuda:1 | 25 GiB / 32G | 99% | llama31-taxei-s42 训练中 |
| cuda:2 | 29 GiB / 32G | 99% | llama31-random-s42 训练中 |
| cuda:3 | 28 GiB / 32G | 99% | v4-taxei-rp-s7 训练中 |

### 任务状态

| 任务 | 状态 | 进度 | 关键指标 |
|------|------|------|----------|
| **eval-rp-s42** | **Done** | 47/47 | recovery_rate=**38.3%**, detection=0% |
| **eval-rp-s0** | **Done**（额外发现） | 47/47 | recovery_rate=**46.8%**, detection=0% |
| **llama31-taxei-s42** | Running | 160/3387 (4.7%) | loss=0.606, ETA ~2h |
| **llama31-random-s42** | Running | 170/3387 (5.0%) | loss=0.685, ETA ~2h |
| **v4-taxei-rp-s7** | Running | 140/5415 (2.6%) | loss=0.657, ETA ~3h41m |
| **scale-up collection** | Running | 805/1000 processed, 70 success (8.2%) | success_rate=8.7% |

### eval-rp-s42 per-operator breakdown
- C1_context_truncation: 50.0% (6/12)
- C4_observation_masking: 27.3% (3/11)
- P1_step_order_swap: 50.0% (6/12)
- P2_sub_goal_deletion: 25.0% (3/12)

### 要点
- 3 个训练均刚启动约7分钟，loss 正常下降，无异常
- eval-rp-s42 结果偏低（38.3% vs s0 的 46.8%），seed 间方差较大
- scale-up 收集还剩约 200 条，按当前速度预计还需 ~15-20 分钟
- GPU 0 空闲可用

---
