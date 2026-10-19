# ops full 4gpu status check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_4gpu_status_check_20260520T004148_result.json`
- **Structured JSON:** [`754e7a6d88f0654365cf.json`](../../sessions/75/754e7a6d88f0654365cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4 GPU 实验状态汇总

### westd-41718

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| cuda:0 | 98% | 45551/97887 MiB | PID 182924 运行中 (43min) |
| cuda:1 | 0% | 0 MiB | 空闲 |

**bench_teal50_uniform_6task** — 运行中
- 进度: 78% (31137/40168 loglikelihood requests)
- 已耗时 ~24min，预估剩余 ~6min
- results.json 尚未生成

**kl30_uniform_hspiqa_s123** — ✅ 已完成

| Task | acc | acc_norm |
|------|-----|----------|
| HellaSwag | 0.5100 | 0.7067 |
| PIQA | 0.7410 | 0.7481 |

---

### westd-34887

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| cuda:0 | 0% | 0 MiB | 空闲 (PID 142999 已结束) |
| cuda:1 | 73% | 37277/97887 MiB | PID 133911 运行中 (4h03m) |

**kl30_uniform_hspiqa_s456** — ✅ 已完成

| Task | acc | acc_norm |
|------|-----|----------|
| HellaSwag | 0.5112 | 0.7168 |
| PIQA | 0.7410 | 0.7524 |

**qwen14b_teal30_uniform_gsm8k** — 运行中
- 进度: 74% (977/1319 generate_until requests)
- 已耗时 ~4h，预估剩余 ~1h20m
- 速率 ~14.6s/it (generate_until 比 loglikelihood 慢很多)

---
