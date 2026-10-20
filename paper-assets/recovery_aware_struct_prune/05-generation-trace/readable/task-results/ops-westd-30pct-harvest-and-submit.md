# ops westd 30pct harvest and submit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_30pct_harvest_and_submit_20260520T113653_result.json`
- **Structured JSON:** [`482eef8fb7c5fb7a9e8c.json`](../../sessions/48/482eef8fb7c5fb7a9e8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### westd-29022 全部 4 GPU 都在跑 eval

| GPU | 任务 | 进度 | 当前 acc | 速度 | 预计完成 |
|-----|------|------|---------|------|---------|
| cuda:0 | CKA-only 30% post-prune eval (N=1319) | 512/1319 (38.8%) | 1.60% | ~48s/sample | ~10.5h 后 |
| cuda:1 | Standard 30% post-prune eval (N=1319) | 503/1319 (38.1%) | 2.80% | ~48s/sample | ~10.5h 后 |
| cuda:2 | seed123 GRPO full eval (N=1319) | 420/1319 (31.8%) | 61.5% | ~3s/sample | ~45min 后 |
| cuda:3 | seed456 GRPO full eval (N=1319) | 427/1319 (32.4%) | 63.25% | ~3s/sample | ~45min 后 |

### 30% eval 中间结果

30% 剪枝后模型几乎完全丧失推理能力（>95% 样本生成 4096 token 都无法完成）：
- **CKA-only 30%**: 1.60% (8/500)
- **Standard 30%**: 2.80% (14/500)

已有 N=200 版本的结果：CKA-only=0%, Standard=4%, RASP=0%。

### 阻塞

- **CKA-only seed456 GRPO (P0)** 和 **15% GRPO restart (P1)** 都需要 cuda:0/1，被 30% eval 阻塞
- 30% eval 只完成 38%，远低于 50% 阈值，不等待
- 预计 **~10.5 小时后**（约 UTC 05:30-06:00）cuda:0/1 空闲

### 建议下一步

30% 的全量 eval 在这种几乎 0 准确率的模型上跑 N=1319 价值不高（N=200 已经足够确认 post-prune 性能崩塌）。如果想快速释放 GPU，可以考虑 kill 这两个进程，用已有的 N=200 结果即可。否则等 ~10.5h 自然完成后再提交两个新实验。

---
