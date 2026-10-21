# verify d102 eval metrics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_d102_eval_metrics_20260518T122108_result.json`
- **Structured JSON:** [`60bc3f4a86bd5077a830.json`](../../sessions/60/60bc3f4a86bd5077a830.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D102 k=1 Eval 结果汇总

| 模型 | rel_f1 | ign_f1 | evi_f1 | edcr | 路径 | 修改时间 |
|---|---|---|---|---|---|---|
| **1.7B k=1 s42** | 52.90 | 51.22 | 82.43 | 62.24 | `/root/autodl-tmp/eval_results/d102_1_7b_k1_s42/metrics.json` | 2026-05-18 18:14 |
| **8B k=1 s42** | 55.49 | 53.76 | 81.36 | 62.31 | `/root/autodl-tmp/eval_results/d102_8b_k1_s42/metrics.json` | 2026-05-18 19:43 |
| **8B k=1 s43** | 56.51 | 54.71 | 81.80 | 60.94 | `/root/autodl-tmp/eval_results/d102_8b_k1_s43/metrics.json` | 2026-05-18 19:45 |
| **LLaMA k=1 s42** | 58.39 | 57.14 | 82.38 | 57.99 | `/root/autodl-tmp/eval_results/d102_llama_k1_s42/metrics.json` | 2026-05-18 18:52 |

补充指标（format/field compliance）：

| 模型 | format_ok_rate | field_compliance_rate | n_truncated |
|---|---|---|---|
| 1.7B k=1 s42 | 99.90% | 74.42% | 249 |
| 8B k=1 s42 | 100% | 74.92% | 242 |
| 8B k=1 s43 | 100% | 75.33% | 231 |
| LLaMA k=1 s42 | 99.90% | 83.96% | 158 |

---

## LLaMA s43 训练进度

- **PID 537136 存活**，在 cuda:3 运行，GPU 利用率 98%，显存 30593MiB/32607MiB
- 进度：**761/1107 steps (68.7%)**，~3.15s/it
- 最新 checkpoint：`checkpoint-750`（`/root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s43/`）
- 训练 loss 已降至 ~0.45，token accuracy ~0.89
- 预估剩余：~346 steps × 3.15s ≈ **18 分钟**

---

## Qwen3-14B 下载状态

已完成。8 个 shard 全部下载完毕，总计 ~27.5GB，路径 `/root/autodl-tmp/models/Qwen/Qwen3-14B/`。

---

## Wave1 脚本内容

**sft_seed43.sh** — SFT Qwen3-4B seed43，CUDA_VISIBLE_DEVICES=0，output → `/root/autodl-tmp/sft_output_seed43`，batch=1, grad_accum=64, epochs=3, lr=2e-4, lora_rank=64

**sft_seed44.sh** — SFT Qwen3-4B seed44，CUDA_VISIBLE_DEVICES=1，output → `/root/autodl-tmp/sft_output_seed44`，同上参数 seed=44

**grpo_bf16_g4.sh** — GRPO bf16 Qwen3-4B stage3，CUDA_VISIBLE_DEVICES=2，no_quantize，num_generations=4，grad_accum=16，max_steps=200，kl_coef=0.0，reward weights: format=0.3 / f1=3.0 / ced=1.0，output → `/root/autodl-tmp/grpo_bf16_g4`

---
