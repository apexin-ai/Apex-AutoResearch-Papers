# check n32 progress

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_n32_progress_20260523T034532_result.json`
- **Structured JSON:** [`7652060cdf8358c04327.json`](../../sessions/76/7652060cdf8358c04327.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_fewnerd_pretrained_n32_s42_v2 状态：Running**

| | 进度 | 已处理/总量 | 耗时 |
|---|---|---|---|
| shard0 (GPU 0) | **41%** | 122,560 / 301,184 | ~42 min |
| shard1 (GPU 1) | **40%** | 120,352 / 301,184 | ~41 min |
| shard2 (GPU 2) | **39%** | 116,736 / 301,184 | ~41 min |
| shard3 (GPU 3) | **39%** | 117,024 / 301,184 | ~40 min |

- **父进程**: PID 157197, 运行 11h 31m, 命令: `run_mvp_pilot.py --model_path Qwen2.5-7B-Instruct --n_samples 32 --seed 42 --collect_logprobs`
- **GPU 3**: 68% 利用率, 29.8 GB 显存占用
- **推理速度**: ~8k input toks/s, ~4k output toks/s (每 shard ~60-80 it/s)
- **预估剩余**: 各 shard 还剩 ~60% (~180k prompts)，按当前速度约需 **60-65 分钟**完成

4 个 shard 并行跑 4 张 GPU，进度接近同步。整体预计约 1 小时后完成。

---
