# ops check all evals status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_evals_status_20260516T015420_result.json`
- **Structured JSON:** [`3ecb35eab9cf2034af2e.json`](../../sessions/3e/3ecb35eab9cf2034af2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 进程状态

| 实验 | PID | 状态 | 失败原因 |
|------|-----|------|---------|
| lm_eval_kl_30pct_s42 | 186674 | **DEAD** | HF httpx `Cannot send a request, client closed` |
| lm_eval_teal_50pct | 187335 | **DEAD** | 同上 |
| mistral dense | 181121 | **DEAD** | 已完成 |
| mistral kl | 174850 | **DEAD** | 未知（无单独输出） |
| sparse rerun | 179918 | **DEAD** | 未知 |

无活跃 tmux 会话。

### GPU 占用

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | **0 MiB** / 97887 MiB | 0% |
| cuda:1 | **0 MiB** / 97887 MiB | 0% |

两张卡完全空闲。

### 已完成实验结果

| Condition | arc_challenge | winogrande | mmlu | gsm8k | 耗时 |
|-----------|-------------|-----------|------|-------|------|
| **Llama dense** (lm_eval) | 0.5819 | 0.7814 | 0.6532 | 0.5004 | 45min |
| **Mistral dense** (plan_009) | 0.6024 | 0.7869 | 0.6244 | 0.3654 | 44min |
| **KL 50% s42** (plan_007) | 0.3771 | 0.6156 | 0.2591 | 0.0121 | 50min |
| **KL 50% s42** (lm_eval_kl_s42 详细) | 0.3259* | 0.6212 | 0.2359 | 0.0182 | — |

\* acc_norm

### 失败实验

- **lm_eval_kl_30pct_s42**: 无输出目录，需重新提交
- **lm_eval_teal_50pct**: 无输出目录，需重新提交

两个失败都是 HuggingFace httpx 客户端错误（可能是网络/代理问题导致模型下载失败）。建议重跑前先确认模型已缓存到本地或设置 `HF_HUB_OFFLINE=1`。

两张 GPU 均可用，可以并行提交 30% eval 和 TEAL 50% eval。需要我提交吗？

---
