# ops d051 gpu check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d051-gpu-check_20260516T215744_result.json`
- **Structured JSON:** [`bdcf528926c6a30543ad.json`](../../sessions/bd/bdcf528926c6a30543ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D051 GPU 实验状态报告

### GPU 状态
- **GPU**: NVIDIA RTX PRO 6000 Black (98GB VRAM)
- **显存占用**: 89,357 / 97,887 MiB (91%)
- **GPU 利用率**: 16%（vLLM 推理中，正常偏低态）
- **进程**: `VLLM::EngineCore` (PID 412517)

### 当前正在运行
- **脚本**: `run_d051_count_curves_25.py --dataset fewnerd --n_batches 25 --seed 42`
- **当前进度**: `count_66` (Few-NERD 的最后一个 count level)，已完成 batch 6/25
- **启动时间**: 03:54 UTC (已运行约 2 小时)

### 已完成文件

**FewRel seed=42 (全部完成 ✓)**
| 文件 | 大小 | 完成时间 |
|------|------|----------|
| results_count_4.jsonl | 487KB | 03:14 |
| results_count_8.jsonl | 1.1MB | 03:35 |
| results_count_16.jsonl | 2.9MB | 03:07 |
| results_count_32.jsonl | 8.8MB | 03:13 |
| results_count_40.jsonl | 12.6MB | 03:20 |
| results_count_64.jsonl | 28.9MB | 03:34 |
| results_count_80.jsonl | 43.1MB | 03:54 |
| eval_results.json + count_curve_summary.json | ✓ | 03:54 |

**Few-NERD seed=42 (进行中)**
| 文件 | 大小 | 完成时间 |
|------|------|----------|
| results_count_2.jsonl | 7.3MB | 04:33 |
| results_count_6.jsonl | 9.6MB | 05:50 |
| results_count_12.jsonl | 13.1MB | 04:18 |
| results_count_22.jsonl | 18.6MB | 04:59 |
| results_count_44.jsonl | 30.6MB | 05:29 |
| results_count_66.jsonl | **进行中** | — |

### 预估剩余时间
- `count_66` 剩余 19 batches × ~70s/batch ≈ **22 分钟**完成当前 count level
- Few-NERD seed=42 完成后，FewRel 7/7 ✓ + Few-NERD 6/6 ✓ = **seed=42 全部完成**
- seed=123 和 seed=456 尚未开始

### 总结
FewRel seed=42 已全部完成。Few-NERD seed=42 还剩最后一个 count level (count_66)，预计约 22 分钟跑完。之后 seed=42 实验全部结束，需要手动启动 seed=123/456 的实验。

---
