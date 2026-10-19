# ops urgent check all experiments

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-check-all-experiments_20260518T195547_result.json`
- **Structured JSON:** [`ae0f173ed33fc1125d75.json`](../../sessions/ae/ae0f173ed33fc1125d75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个实验已完成 (`EXIT_CODE=0`)，两台服务器 GPU 空闲。

---

## 实验结果汇总

### 1. kl_sparsity25_s42_eval_teal (TEAL global_topk, sparsity=23%)
| Metric | Value |
|--------|-------|
| wikitext2_ppl | **8.169** |
| arc_challenge (acc_norm) | **0.4539** |
| winogrande (acc) | **0.7056** |
| mmlu (acc) | **0.4660** |
| gsm8k (exact_match) | **0.1145** |

### 2. kl_sparsity25_s42_eval_teal_uniform (TEAL uniform, sparsity=25%)
| Metric | Value |
|--------|-------|
| wikitext2_ppl | **8.2344** |
| arc_challenge (acc_norm) | **0.4650** |
| winogrande (acc) | **0.7182** |
| mmlu (acc) | **0.4395** |
| gsm8k (exact_match) | **0.1099** |

### 3. kl_sparsity35_s42_eval_teal_uniform (TEAL uniform, sparsity=35%)
| Metric | Value |
|--------|-------|
| wikitext2_ppl | **9.4416** |
| arc_challenge (acc_norm) | **0.3874** |
| winogrande (acc) | **0.6654** |
| mmlu (acc) | **0.3783** |
| gsm8k (exact_match) | **0.0432** |

### 4. Latency Benchmark (mask-and-multiply, no sparse kernel)

**batch_size=1, seq_len=2048:**
| Condition | tok/s | ms/tok | vs Dense |
|-----------|-------|--------|----------|
| Dense | 17308.5 ± 118.0 | 0.0578 | 1.00x |
| KL Sparse 30% | 16089.2 ± 38.3 | 0.0622 | 0.93x |
| KL Sparse 50% | 16056.8 ± 16.5 | 0.0623 | 0.93x |

**batch_size=8, seq_len=2048:**
| Condition | tok/s | ms/tok | vs Dense |
|-----------|-------|--------|----------|
| Dense | 15636.6 ± 15.2 | 0.0640 | 1.00x |
| KL Sparse 30% | 14697.4 ± 4.6 | 0.0680 | 0.94x |
| KL Sparse 50% | 14756.8 ± 2.5 | 0.0678 | 0.94x |

Predictor overhead (32 layers): ~3.2ms (bs=1), ~14.4ms (bs=8). Memory identical across conditions.

### GPU 状态
- **westd-41718**: 2x RTX PRO 6000 Blackwell, 0% util, 0MB used
- **westd-34887**: 2x RTX PRO 6000 Blackwell, 0% util, 0MB used

---
