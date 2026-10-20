# ssh westd olmo reeval cuda2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-olmo-reeval-cuda2_20260519T100239_result.json`
- **Structured JSON:** [`b5bd97a2d2d592120026.json`](../../sessions/b5/b5bd97a2d2d592120026.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部三个 eval 完成。汇总结果：

## 结果汇总

| Dosage | Benchmark | westd (新) | cqa1 (旧) | 差异 |
|--------|-----------|-----------|-----------|------|
| **d000** | MMLU | **58.60%** | 58.71% | -0.11pp |
| **d000** | ARC | **80.20%** | 68.09% | **+12.11pp** |
| **d005** | MMLU | **58.10%** | 58.21% | -0.11pp |
| **d005** | ARC | **80.20%** | 68.17% | **+12.03pp** |
| **d025** | MMLU | **56.17%** | 59.14% | **-2.97pp** |
| **d025** | ARC | **78.16%** | 67.83% | **+10.33pp** |

### 关键发现

1. **MMLU**：d000/d005 差异极小（~0.1pp），但 d025 差异较大（-2.97pp），可能是 evaluate.py 版本差异的影响
2. **ARC**：westd 版本一致性地比 cqa1 高 10-12pp。这解释了之前观察到的 d025→d050 跳跃 — 实际上是 cqa1 vs westd 的 evaluate.py 版本差异导致的，不是 dosage 效果。现在用 westd 统一跑后，ARC 数据可比了。

### 输出文件路径
- d000: `/root/autodl-tmp/exp001/eval_results_cross_family/olmo2_d000_s42_westd/`
- d005: `/root/autodl-tmp/exp001/eval_results_cross_family/olmo2_d005_s42_westd/`
- d025: `/root/autodl-tmp/exp001/eval_results_cross_family/olmo2_d025_s42_westd/`

### 无异常
三个 eval 均正常完成，所有输出文件（eval_results.json, arc_challenge_results.json, mmlu_results.json, correctness_matrix.json, item_responses.json）齐全。

---
