# diagnose stale running 41718

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_stale_running_41718_20260522T023215_result.json`
- **Structured JSON:** [`873e4de28efbe134d8d9.json`](../../sessions/87/873e4de28efbe134d8d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在死亡前成功完成，结果已落盘。

---

## 实验 1: reverse_kl_30_s42_uniform_eval ✅ 已完成

- **日志**: `/root/distill_sparse_swiglu/logs/reverse_kl_30_s42_uniform_eval.log` (1.1MB, 完整)
- **结果**: `/root/distill_sparse_swiglu/results/benchmark/reverse_kl_30_s42_uniform_eval/results.json`
- **时间戳**: 2026-05-21 03:47:55
- **配置**: llama-3.1-8b, teal_global mode, sparsity=0.3, allocation=uniform, checkpoint=`reverse_kl_30_s42/predictor_reverse_kl.pt`

**Metrics (7 tasks)**:
| Task | Metric | Value |
|------|--------|-------|
| wikitext2 | PPL | **9.3081** |
| arc_challenge | acc / acc_norm | 0.3968 / **0.4283** |
| winogrande | acc | **0.7009** |
| mmlu | acc | **0.3749** |
| gsm8k | exact_match (flex) | **0.0697** |
| hellaswag | acc / acc_norm | 0.5057 / **0.6969** |
| piqa | acc / acc_norm | 0.7427 / **0.7459** |

---

## 实验 2: qwen14b_teal30_uniform_hspiqa_v2 ✅ 已完成

- **日志**: 没有 `*_v2.log` 文件，只有早期版本 `qwen14b_teal30_uniform_hspiqa.log` (May 19)
- **结果**: `/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa_v2/results.json`
- **时间戳**: 2026-05-19 22:26:26
- **配置**: qwen2.5-14b, baseline_teal_vanilla (per_token mode), sparsity=0.3, allocation=uniform

**Metrics (2 tasks)**:
| Task | Metric | Value |
|------|--------|-------|
| hellaswag | acc / acc_norm | 0.4936 / **0.6756** |
| piqa | acc / acc_norm | **0.7443** / 0.7427 |

---

**结论**：两个 PID 虽已死，但都是在写完 results.json 之后才死的，无需重跑。可直接用这两个 JSON 填充论文。

---
