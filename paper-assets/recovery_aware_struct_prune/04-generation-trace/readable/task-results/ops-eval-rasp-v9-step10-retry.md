# ops eval rasp v9 step10 retry

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-rasp-v9-step10-retry_20260516T044338_result.json`
- **Structured JSON:** [`b683653ecbe65a2636d4.json`](../../sessions/b6/b683653ecbe65a2636d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正在运行：
- 模型已加载到 GPU 0（12937 MiB）
- GSM8K 本地 parquet 加载成功（1319 samples）
- 推理进行中（3/1319，~4s/it）
- `HF_HUB_OFFLINE=1` 生效，无网络请求
- PID: 585618

**汇报：**
- 之前的 eval 已退出（网络不可达导致 GSM8K 数据集加载失败）
- `HF_HUB_OFFLINE=1` 会同时阻止 datasets 库访问 Hub，所以改为从本地 parquet 缓存加载数据集（修改了 eval_gsm8k.py 第 346 行）
- 重启成功，当前正在推理中，预估 ~1.5 小时完成（1319 samples × ~4s/it）
- 服务器: westb-23072, GPU: cuda:0, tmux session: `eval_grpo_rasp_v9_step10`

---
