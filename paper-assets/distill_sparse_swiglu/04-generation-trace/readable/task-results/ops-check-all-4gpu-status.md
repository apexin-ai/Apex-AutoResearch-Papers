# ops check all 4gpu status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_4gpu_status_20260520T003803_result.json`
- **Structured JSON:** [`0a63dfa9fd139ca3dcb1.json`](../../sessions/0a/0a63dfa9fd139ca3dcb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### westd-41718

| GPU | 实验 | PID | 状态 | GPU 利用率 | 显存 | 进度 |
|-----|------|-----|------|-----------|------|------|
| cuda:0 | bench_teal50_uniform_6task | 182919 | **运行中** | 100% | 45551/97887 MiB | MMLU loglikelihood 63% (25465/40168) |
| cuda:1 | kl30_uniform_hspiqa_s123 | 183059 | **已完成** ✓ | 0% | 0 MiB | EXIT_CODE=0 |

**kl30_uniform_hspiqa_s123 结果：**
| Task | acc | acc_norm |
|------|-----|----------|
| hellaswag | 0.5100 | 0.7067 |
| piqa | 0.7410 | 0.7481 |

bench_teal50_uniform_6task 已完成 wikitext2 PPL + ARC/WinoGrande/HellaSwag/PIQA，当前在跑 MMLU（最大的 task），预计还需 ~15-20 分钟。

---

### westd-34887

| GPU | 实验 | PID | 状态 | GPU 利用率 | 显存 | 进度 |
|-----|------|-----|------|-----------|------|------|
| cuda:0 | kl30_uniform_hspiqa_s456 | 142999 | **运行中** | 100% | 47681/97887 MiB | MMLU loglikelihood 99% (39961/40168)，即将完成 |
| cuda:1 | qwen14b_teal30_uniform_gsm8k | 133911 | **运行中** | 73% | 37277/97887 MiB | GSM8K generate_until 73% (961/1319) |

- **kl30_uniform_hspiqa_s456**：MMLU 99%，几分钟内完成，之后还有 hellaswag + piqa 两个 task（~35 min）。
- **qwen14b_teal30_uniform_gsm8k**：GSM8K 生成式评估，73%，已跑 ~4h，剩余 ~358 items × ~13.5s/it ≈ **~80 min**。

---
