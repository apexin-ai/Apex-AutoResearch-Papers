# ssh autodl small model inference

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_small_model_inference_20260522T181927_result.json`
- **Structured JSON:** [`f3843885186240b21f5b.json`](../../sessions/f3/f3843885186240b21f5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Mistral-7B 完成，500 条 response 已写入。

Qwen 下载速度 ~300-350 kB/s/shard，4 个 shard 并行但总量 ~14GB，预计 2.5-3 小时完成。下载完后会自动启动生成（`os.execvp` 接力）。

## 汇总

| 模型 | GPU | 状态 | PID | 输出 |
|------|-----|------|-----|------|
| **Mistral-7B-v0.3** | cuda:2 | **完成 500/500** (0 err, ~1min) | 163155 (已退出) | `responses/mistral-7b-v0.3.jsonl` |
| **Qwen2.5-7B** | cuda:1 | 下载中 (~1% of 14GB, ~3h ETA) → 下载完自动生成 | 163745 | 待生成 → `responses/qwen2.5-7b.jsonl` |
| cuda:0 | exp-003b MCMC | 未碰 | — | — |

Qwen 下载进程 PID=163745，日志 `/tmp/gen_qwen7b.log`。下载完成后会自动 `execvp` 到 `generate_vllm_batch.py --model qwen2.5-7b` 在 cuda:1 上生成。

---
