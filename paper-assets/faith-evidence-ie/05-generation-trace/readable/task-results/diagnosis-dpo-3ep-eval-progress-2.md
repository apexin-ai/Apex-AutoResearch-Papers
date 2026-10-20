# diagnosis dpo 3ep eval progress 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_dpo-3ep-eval-progress-2_20260523T132708_result.json`
- **Structured JSON:** [`b43ac73bc62555a52a6c.json`](../../sessions/b4/b43ac73bc62555a52a6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前进度：**237/247 batches (95.9%)**，已运行 3h44m。

| 指标 | 值 |
|------|-----|
| 进度 | 237/247 (95.9%) |
| 剩余 | 10 batches |
| 平均速度 | ~60s/batch |
| 预计完成 | ~10 分钟后 |
| GPU (cuda:2) | 12309 MiB / 97887 MiB, 73% util |

GPU 状态：
- cuda:0, cuda:1: 空闲
- cuda:2: 12.3GB (DPO 3ep eval)
- cuda:3: 12.7GB (另一任务)

推理接近完成，约 10 分钟后会写出 predictions.jsonl。完成后需运行 batch_eval 计算 metrics。

---
