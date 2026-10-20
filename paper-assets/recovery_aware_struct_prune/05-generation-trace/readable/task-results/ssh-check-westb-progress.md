# ssh check westb progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westb_progress_20260522T141821_result.json`
- **Structured JSON:** [`93c5bdc36ba9e78fc8ce.json`](../../sessions/93/93c5bdc36ba9e78fc8ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 1. grpo_random_20_seed456 (PID 209508, GPU:0)
- **状态**: 运行中，已运行 1h12m
- **进度**: ~30/100 steps（completions 目录有 step 10/20/30 的 parquet）
- **速度**: ~2.4 min/step
- **预计剩余**: ~2.8h（70 steps × 2.4 min）
- **GPU 占用**: 55.7GB / 97.9GB, 利用率 100%
- **注意**: 未找到 nohup 日志文件，可能 stdout 直接丢弃了

### 2. eval_gsm8k_grpo_qwen_math_cka_only_20_n500 (PID 202364, GPU:1)
- **状态**: 运行中，已运行 2h11m
- **进度**: **25/500** 样本 (5%)
- **速度**: ~337s/sample（远慢于预估的 78s/sample，慢了 4.3x）
- **预计剩余**: ~44h（475 × 337s）
- **GPU 占用**: 29.6GB / 97.9GB, 利用率 98%
- **警告**: 日志显示 `text generation call has exceeded the model's predefined maximum length (4096)`，模型生成超长导致速度极慢

### 磁盘
- 数据盘 `/root/autodl-tmp/`: 233GB/250GB used (**94%**)，仅剩 18GB，需关注

### 关键问题
eval N=500 按当前速度需要 ~44h 而非预估的 11h。超长生成是主因——可能需要在 generation config 中加 `max_new_tokens` 限制，否则单个样本可能生成到 4096 tokens 才停。

---
