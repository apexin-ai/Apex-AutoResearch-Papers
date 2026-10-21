# healthcheck all gpus 20260522

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_healthcheck_all_gpus_20260522_20260522T080910_result.json`
- **Structured JSON:** [`9f53caa25d04dd6bdb5f.json`](../../sessions/9f/9f53caa25d04dd6bdb5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个已完成实验的 registry 已全部更新为 DONE。

## 最终汇总

### 进程状态
| GPU | 实验 | 状态 |
|-----|------|------|
| cuda:0 | bs16_uniform_seed456 | **完成** → eval 完成 → registry DONE |
| cuda:1 | bs16_adaptive_tau07_seed456 | **完成** → eval 完成 → registry DONE |
| cuda:2 | detect_remove_q05_v2_seed123_r2 | **运行中** (GPU 100%, 57GB) |
| cuda:3 | random_reweight_v2_seed456 | **运行中** (GPU 99%, 57GB) |

### Eval 结果
| Metric | bs16_uniform_seed456 | bs16_adaptive_tau07_seed456 | Δ(adaptive−uniform) |
|--------|---------------------|---------------------------|---------------------|
| holdout_ppl | 17.717 | 17.645 | **−0.072** |
| owt_ppl | 17.885 | 17.807 | **−0.078** |
| wiki_ppl | 14.781 | 14.713 | **−0.068** |

Adaptive 在 bs=16 下全面优于 uniform，Δ ≈ −0.07，比 bs=4 的 Δ=−0.020 更大，支持 batch size 放大 adaptive 优势的假设。

### 磁盘
`/root/autodl-tmp`: 192G/250G used (77%)

---
