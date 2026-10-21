# eval cls v5 conda ckpt sweep westd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls-v5-conda-ckpt-sweep-westd_20260514T023919_result.json`
- **Structured JSON:** [`783a2356a339b1914fef.json`](../../sessions/78/783a2356a339b1914fef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

## 任务 A: 已完成 eval 结果

### CLS v5-conda (Qwen3-4B) checkpoint-200
| 指标 | 值 |
|------|-----|
| Accuracy | 52.96% (majority baseline 72.96%, gap -20.0pp) |
| F1 macro | 52.89% |
| F1 fail | 51.02% (P=35.5%, R=90.6%) |
| F1 pass | 54.76% (P=91.8%, R=39.0%) |
| Unparseable | 132/9784 |

模型严重偏向预测 fail（recall_fail=90.6%），但 precision_fail 很低（35.5%），导致大量 pass 被误判为 fail（FN=4353）。

### CLS 8B-conda (Qwen3-8B) checkpoint-200
| 指标 | 值 |
|------|-----|
| Accuracy | 70.22% (majority baseline 72.96%, gap -2.74pp) |
| F1 macro | 68.21% |
| F1 fail | 60.23% (P=47.1%, R=83.4%) |
| F1 pass | 76.19% (P=91.4%, R=65.3%) |
| Unparseable | 136/9784 |

8B 比 4B 好很多：accuracy +17pp, F1 macro +15pp。仍偏向 fail 但程度大幅缓解。

## 任务 B: ckpt-400/600 eval 启动确认

- GPU 2: `eval_cls_v5_ckpt400` — checkpoint-400，模型已加载，推理进行中（GPU 2 utilization 100%, 17167 MiB）
- GPU 3: `eval_cls_v5_ckpt600` — checkpoint-600，模型已加载，推理进行中（GPU 3 utilization 100%, 17167 MiB）

预计约 30 分钟完成（参考 ckpt-200 eval 用时约 27 分钟）。

---
