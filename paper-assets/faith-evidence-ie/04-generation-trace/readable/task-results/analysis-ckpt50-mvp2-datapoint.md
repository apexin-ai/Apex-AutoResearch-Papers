# analysis ckpt50 mvp2 datapoint

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ckpt50-mvp2-datapoint_20260514T182948_result.json`
- **Structured JSON:** [`be815567ab99ece834fe.json`](../../sessions/be/be815567ab99ece834fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在，无需清除。

## Checkpoint-50 Eval Results (MVP-2 Data Point #1)

| Metric | SFT Baseline | CED ckpt-50 | Δ | Pass? |
|--------|-------------|-------------|---|-------|
| rel_f1 | 0.4057 | 0.1563 | **-24.9pp** | ❌ (≥ -5pp) |
| evi_f1 | 0.7979 | 0.5643 | **-23.4pp** | ❌ (≥ +2pp) |
| edcr   | 0.7118 | 0.8858 | +17.4pp | (参考) |

Additional metrics:

| | precision | recall | evi_precision | evi_recall | format_ok | n_parseable | n_truncated | predictions |
|--|-----------|--------|---------------|------------|-----------|-------------|-------------|-------------|
| | 0.2356 | 0.1169 | 0.4864 | 0.6721 | 99.9% | 984/985 | 11 | 9250 |

**MVP-2 Overall: FAIL**

**诊断**: Training reward 上升 (1.101) 但 eval F1 崩塌，典型的 reward hacking。模型学会了高 EDCR（减少 distractor 引用，+17pp）但代价是 recall 崩塌——pred_count=6032 vs gold=12151，模型只预测了一半的关系。GRPO 优化了 reward proxy 而非实际任务质量。

关键悬念：step-90 (reward=1.37) 和 step-100 的 eval 仍在跑。如果更高 reward 的 checkpoint 同样崩塌，说明 CED reward 设计存在根本问题（EDCR 项鼓励模型少预测来规避 distractor penalty）。

---
