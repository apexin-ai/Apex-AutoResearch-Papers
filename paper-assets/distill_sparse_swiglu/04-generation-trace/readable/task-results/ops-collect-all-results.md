# ops collect all results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-all-results_20260519T010513_result.json`
- **Structured JSON:** [`baac3896ea968c243c56.json`](../../sessions/ba/baac3896ea968c243c56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

C1 eval is at 91% on gsm8k (1201/1319), the last task. Should finish in ~2 minutes. Here are all results:

---

## 实验结果汇报

| # | 实验 | 服务器 | 状态 | 结果 |
|---|------|--------|------|------|
| 1 | **c1_ablation_30pct_s42_eval_v2** | westd-34887 GPU1 | **运行中** (gsm8k 91%, ~2min剩余) | PPL = **9.4463**; arc_challenge/winogrande/mmlu/gsm8k 待完成 |
| 2 | **dense_baseline_hellaswag_piqa** | westd-34887 GPU0 | **完成** ✓ | hellaswag acc_norm = **0.8235**, piqa acc_norm = **0.8090** |
| 3 | **kl50_uniform_hellaswag_piqa** | westd-41718 GPU0 | **完成** ✓ | hellaswag acc_norm = **0.5666**, piqa acc_norm = **0.6910** |
| 4 | **bce_isocompute_hellaswag_piqa** | westd-41718 GPU1 | **失败** ✗ | `FileNotFoundError: /root/distill_sparse_swiglu/checkpoints/bce_isocompute_v3_s42/predictor_bce.pt` |

## GPU 状态

| 服务器 | GPU | 利用率 | 显存占用 |
|--------|-----|--------|----------|
| westd-34887 | cuda:0 | 0% | 0 / 97887 MiB |
| westd-34887 | cuda:1 | 62% | 66997 / 97887 MiB |
| westd-41718 | cuda:0 | 0% | 0 / 97887 MiB |
| westd-41718 | cuda:1 | 0% | 0 / 97887 MiB |

**备注**：
- 实验1 的 downstream metrics (arc_challenge, winogrande, mmlu, gsm8k) 会在脚本结束后一并输出，目前仅有 PPL 结果
- 实验4 失败原因：checkpoint 路径 `bce_isocompute_v3_s42/predictor_bce.pt` 不存在

---
