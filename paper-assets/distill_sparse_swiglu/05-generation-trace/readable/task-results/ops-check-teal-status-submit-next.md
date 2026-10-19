# ops check teal status submit next

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-teal-status-submit-next_20260516T121625_result.json`
- **Structured JSON:** [`d525cdcb77d4b2d90df9.json`](../../sessions/d5/d525cdcb77d4b2d90df9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. bench_teal30/50 结果

| Metric | bench_teal30 (TEAL 30%) | bench_teal50 (TEAL 50%) |
|--------|------------------------|------------------------|
| wikitext2_ppl | **10.97** | **23.31** |
| arc_challenge_acc_norm | 0.4232 | 0.2841 |
| winogrande_acc | 0.6606 | 0.5304 |
| mmlu_acc | 0.3861 | 0.2832 |
| gsm8k_exact_match | 0.0788 | 0.0197 |

两个均成功完成，耗时 ~38 分钟。

### 2. Registry 更新

- bench_teal30: QUEUED → RUNNING → **DONE** (success, metrics 已录入)
- bench_teal50: QUEUED → RUNNING → **DONE** (success, metrics 已录入)
- bench_kl40_global: 新建 QUEUED → RUNNING

### 3. 新提交实验

| exp_id | GPU | PID | 内容 |
|--------|-----|-----|------|
| bench_kl50_uniform | cuda:0 | 229957 | KL 50% predictor + uniform allocation |
| bench_kl40_global | cuda:1 | 230101 | KL 40% predictor + global top-k |

预计 ~40 分钟完成。

---
