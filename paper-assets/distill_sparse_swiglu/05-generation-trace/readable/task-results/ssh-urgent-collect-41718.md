# ssh urgent collect 41718

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_collect_41718_20260520T181356_result.json`
- **Structured JSON:** [`5fa050bbd5589c5d6093.json`](../../sessions/5f/5fa050bbd5589c5d6093.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

KL50 的 lm_eval 结果要等所有 task 跑完才一起输出。当前进度：wikitext2 PPL 已出 (12.0109)，arc/wg/mmlu/gsm8k 已跑完，正在跑 hellaswag，piqa 待跑。

---

## 汇总

### westd-41718 GPU 状态
| GPU | 型号 | 显存 | 利用率 | 状态 |
|-----|------|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 0/98GB | 0% | **空闲** |
| 1 | RTX PRO 6000 Blackwell | 66/98GB | 100% | PID 272689 (kl50_global_s456_eval) |

---

### STE 30% s42 eval — 已完成 (EXIT_CODE=0)

| Metric | Value |
|--------|-------|
| WikiText-2 PPL | **8.4138** |
| ARC-c (acc_norm) | **0.4846** |
| WinoGrande (acc) | **0.7277** |
| MMLU (acc) | **0.4395** |
| GSM8K (exact_match) | **0.1676** |
| HellaSwag (acc_norm) | **0.7511** |
| PIQA (acc_norm) | **0.7726** |

配置：`sparsity_mode=teal_global, sparsity_target=0.3, allocation=uniform, relaxation=ste, loss=kl_normalized, seed=42`

---

### KL 50% global s456 eval — 仍在运行

- WikiText-2 PPL: **12.0109**
- 已完成：arc_challenge, winogrande, mmlu, gsm8k
- **正在跑**：hellaswag（刚启动）
- **待跑**：piqa
- 配置：`sparsity_mode=teal_global, sparsity_target=0.5, allocation=global_topk, checkpoint=mvp_kl_norm_v2_s456`

预计还需 ~20-30 分钟完成全部评测。完成后结果会写入 `/root/distill_sparse_swiglu/results/benchmark/kl50_global_s456_eval/results.json`。

---
