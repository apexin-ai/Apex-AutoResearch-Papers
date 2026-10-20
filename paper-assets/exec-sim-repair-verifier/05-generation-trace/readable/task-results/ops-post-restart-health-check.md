# ops post restart health check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart-health-check_20260519T143335_result.json`
- **Structured JSON:** [`9e7710424ca544bb579d.json`](../../sessions/9e/9e7710424ca544bb579d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

| GPU | 实验 | PID | 状态 | GPU 利用率 | 显存 | 进度 |
|-----|------|-----|------|-----------|------|------|
| 0 | qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval | 778328 | **运行中** (14h22m) | 90% | 27.7/32.6 GB | **7192/9784 (73.5%)**, acc=63.9% |
| 1 | cls8b-repo-s456-train-v2 | 840928 | **运行中** (25m) | 68% | 28.1/32.6 GB | **148/6633 (2.2%)**, loss=16.29 @ step 100, ~8s/it, ETA ~14h |
| 2 | deepseek-cwm-repo-s42-seq4096-eval | 833667 | **运行中** (1h54m) | 84% | 28.2/32.6 GB | **1472/9784 (15.0%)**, acc=60.3% |
| 3 | deepseek-cls-repo-s456-train-v3 | 842751 | **⚠️ 异常** (2m41s) | **0%** | **0 MiB** | 数据已加载(70748条)，但无训练步输出 |

### ⚠️ GPU 3 异常详情

PID 842751 进程存活，但 GPU 3 显存占用为 0、利用率 0%。日志停在：
```
Loaded train=70748, val=9335
Token indices sequence length is longer than the specified maximum sequence length for this model (21629 > 16384)
```

没有任何训练 step 输出。可能原因：
1. 仍在 tokenize/预处理阶段（但已过 2m41s 且无 GPU 占用，不太正常）
2. 模型尚未加载到 GPU（序列长度警告可能导致后续处理卡住）

建议过几分钟再查一次日志，若仍无进展则需要介入排查。

---
