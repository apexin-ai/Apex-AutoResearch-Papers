# cpu gemma probe training 102

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_gemma-probe-training-102_20260522T104418_result.json`
- **Structured JSON:** [`bbbd299f7252a7bddff2.json`](../../sessions/bb/bbbd299f7252a7bddff2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Probe training 已启动：

- **PID**: 476334
- **脚本**: `train_probe_fast.py`（joblib 32 workers 并行）
- **配置**: 4 方向 × 42 layers × 2000 bootstrap seeds
- **当前状态**: en_en 方向已开始处理
- **预计完成**: ~25-30 分钟（fast 版）

输出文件: `data/gemma2/probe_results_bootstrap_n2000.json`，日志: `logs/gemma_probe_training.log`。

---
