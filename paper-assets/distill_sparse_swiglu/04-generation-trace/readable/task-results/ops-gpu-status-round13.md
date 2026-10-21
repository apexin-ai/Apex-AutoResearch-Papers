# ops gpu status round13

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_round13_20260520T020757_result.json`
- **Structured JSON:** [`d20afca1c1002b5a814d.json`](../../sessions/d2/d20afca1c1002b5a814d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态 & 实验结果

### GPU 利用率

| 服务器 | GPU | 利用率 | 显存 |
|--------|-----|--------|------|
| westd-34887 | cuda:0 | 0% | 0/98GB | 
| westd-34887 | cuda:1 | 0% | 0/98GB |
| westd-41718 | cuda:0 | 0% | 0/98GB |
| westd-41718 | cuda:1 | **100%** | 69/98GB |

### 实验结果

| 实验 | 状态 | HellaSwag acc_norm | PIQA acc_norm | GSM8K exact_match |
|------|------|-------------------|---------------|-------------------|
| **qwen14b_teal30_uniform_hspiqa** | 完成 | 0.6772 | 0.7470 | — |
| **qwen14b_teal30_uniform_gsm8k** | 完成 | — | — | 0.5208 |
| **qwen14b_kl30_uniform_hspiqa** | 完成 | 0.7266 | 0.7514 | — |
| **qwen14b_kl30_global_hspiqa** | 运行中 (~42%, 25min/~60min ETA) | — | — | — |

KL uniform 在 HellaSwag 上比 TEAL uniform 高 **+4.94pp** (0.7266 vs 0.6772)，PIQA 上高 **+0.44pp** (0.7514 vs 0.7470)。

---
