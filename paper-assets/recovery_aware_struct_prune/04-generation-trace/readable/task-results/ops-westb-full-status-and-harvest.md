# ops westb full status and harvest

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_full_status_and_harvest_20260519T030812_result.json`
- **Structured JSON:** [`885532985dfec5d70a1f.json`](../../sessions/88/885532985dfec5d70a1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 状态审计结果

### 1. GPU 状态

| GPU | Utilization | Memory Used | Memory Total |
|-----|------------|-------------|--------------|
| cuda:0 | 0% | 0 MiB | 97887 MiB |
| cuda:1 | 96% | 6537 MiB | 97887 MiB |

### 2. eval_gsm8k_sft_rasp_20_1p5b (cuda:0) — 已完成

| 指标 | 值 |
|------|-----|
| **accuracy** | **26.91%** |
| n_correct | 355 |
| n_total | 1319 |
| eos_rate | 94.16% |
| avg_response_length | 378.6 |

进程已退出，结果已写入 JSON。

### 3. eval_gsm8k_sft_standard_20_1p5b (cuda:1) — 运行中

- 进度: **1282/1319 (97.2%)**，即将完成
- 最近一次中间报告 (1250/1319): acc=0.2296, eos_rate=90.56%, avg_len=512
- 预计几分钟内完成

### 4. 空闲 GPU

- **cuda:0 完全空闲**（0% utilization, 0 MiB）
- cuda:1 被 standard 评估占用，预计很快释放

---
