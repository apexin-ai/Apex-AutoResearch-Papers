# ops sync figures to local

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync-figures-to-local_20260518T185303_result.json`
- **Structured JSON:** [`2ec60bd7523de82d7e90.json`](../../sessions/2e/2ec60bd7523de82d7e90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 本地 figures/ 文件

| 文件 | 大小 |
|------|------|
| `mask_divergence_heatmap.pdf` | 18,285 B |
| `mask_divergence_heatmap.png` | 45,409 B |
| `neuron_scatter_layer16.pdf` | 61,204 B |
| `neuron_scatter_layer16.png` | 141,172 B |
| `mask_comparison.pdf` | 16,394 B |
| `mask_comparison.png` | 31,216 B |

路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/figures/`

### Eval 进度

**kl_sparsity45_s42_eval_teal_uniform** — **已完成** (EXIT_CODE=0, 耗时 2366.6s)
- arc_challenge: acc=0.3387, acc_norm=0.3763
- winogrande: acc=0.6361
- mmlu: acc=0.3063
- gsm8k: exact_match=0.0273
- 结果已保存至 `results/benchmark/kl_sparsity45_s42_eval_teal_uniform/results.json`

**kl_sparsity35_s42_eval_teal_uniform** — **运行中** (pid 47633)
- 已完成 tokenizing（wikitext2/arc_challenge/winogrande/mmlu）
- 当前正在 MMLU loglikelihood 阶段，进度约 1%（737/58702），速度 ~30 it/s
- 预计 MMLU 部分还需约 30 分钟，之后还有 gsm8k generate_until

---
