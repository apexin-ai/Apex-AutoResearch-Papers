# code fix paper skeleton params

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_paper_skeleton_params_20260516T012354_result.json`
- **Structured JSON:** [`ae86a6b247e1b7f2ce3f.json`](../../sessions/ae/ae86a6b247e1b7f2ce3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修正完毕。修正记录：

```
1.  top_p:      0.95 → 0.9        （来源: generate_synthetic.py:32）
2.  top_k:      50 → 删除（未使用）  （来源: generate_synthetic.py 无 top_k 参数）
3.  生成方式:    prefix-seeded (32-token FineWeb prefixes) → BOS unconditional
                                    （来源: generate_synthetic.py:57-58）
4.  learning_rate: 1e-4 → 1e-5     （来源: train.py:71）
5.  β₂:         0.95 → 0.999       （来源: train.py:94, PyTorch AdamW 默认值）
6.  weight_decay: 0.1 → 0.01       （来源: train.py:94）
7.  warmup:      1% → 2%           （来源: train.py:72）
8.  Corpus spectral rank: 
     旧: concatenate all hidden states → [N×256, d] → SVD
     新: mean-pool per example → [5000, d] → Gram matrix [d, d] → SVD
                                    （来源: compute_signals.py:127-131）
9.  distinct-n:  
     旧: 1,000 sequences, 256 tokens
     新: all probe-set sequences (~5000), 64-token prefixes, 128 new tokens
                                    （来源: compute_signals.py:138,181-182）
10. bootstrap/permutation: 已在 analyze_correlation.py 实现
     bootstrap: 1000 iterations（analyze_correlation.py:175-206）
     permutation test: 10000 permutations（analyze_correlation.py:235-256）
     §3.3 描述与代码一致，无需修改
```

---
