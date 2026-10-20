# code audit pipeline metrics

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_audit_pipeline_metrics_20260512T171433_result.json`
- **Structured JSON:** [`309ecc72ae14aef23b91.json`](../../sessions/30/309ecc72ae14aef23b91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v5 进程正常运行。

---

## 最终审计报告

| # | 指标 | 状态 | 代码位置 |
|---|------|------|----------|
| 1 | 谱有效秩 | ✅ 已覆盖 | `metrics.py:compute_spectral_effective_rank` — hidden states → SVD → exp(H(normalized σ)) |
| 2 | Token 级预测熵方差 | ✅ 已覆盖 | `metrics.py:compute_token_entropy_variance` — per-token entropy → mean/var/std |
| 3 | N-gram 熵 | ✅ 已覆盖 | `metrics.py:compute_ngram_entropy` — uni/bi/trigram Shannon 熵 |
| 4 | 词表覆盖率 | ✅ 已覆盖 | `metrics.py:compute_vocab_coverage` — unique_tokens / vocab_size |
| 5 | PPL | ✅ 已覆盖 | `metrics.py:compute_perplexity` — held-out 真实数据标准 PPL |
| 6a | 代际 KL（token 分布） | ✅ 已覆盖 | `metrics.py:compute_kl_divergence` — unigram/bigram KL + frequency-binned + bootstrap CI |
| 6b | 代际 KL（logit 分布） | ✅ **已补充** | `metrics.py:compute_logit_kl_divergence` — 同一输入上两代模型 softmax 分布的 per-token KL |

## 改动内容

**metrics.py**:
- 新增 `compute_logit_kl_divergence()` — 加载两代模型，同一 held-out 输入，计算 KL(P_prev || P_curr) 的 mean/var/std/median/max/p90/p99
- `compute_checkpoint_metrics()` 增加 `prev_model` 参数，有前代模型时自动调用 logit KL

**pilot_pipeline.py**:
- `evaluate_checkpoints()` 增加 `prev_model_dir` 参数，在 checkpoint 循环外一次性加载前代模型，循环结束后释放
- `run_pilot()` 调用时传入已有的 `prev_model_dir`

**dry-run**: `from metrics import *` 和 `from pilot_pipeline import evaluate_checkpoints, run_pilot` 均通过。v5 进程 (pid=32154) 未受影响。

---
