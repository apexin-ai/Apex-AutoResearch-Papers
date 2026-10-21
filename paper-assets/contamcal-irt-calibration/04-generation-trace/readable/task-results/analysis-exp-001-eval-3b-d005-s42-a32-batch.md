# analysis exp 001 eval 3B d005 s42 a32 batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_eval_3B_d005_s42_a32_batch_20260516T062331_result.json`
- **Structured JSON:** [`37c5a633c60e1eff54b2.json`](../../sessions/37/37c5a633c60e1eff54b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。汇总结果如下：

## exp_001_eval_3B_d005_s42_a32_batch 结果

实验产出了两组结果：原始 eval 和 paraphrased eval。

### Original eval（全量 benchmark）
| Benchmark | Accuracy | Samples | d000 Baseline | Delta |
|-----------|----------|---------|---------------|-------|
| mmlu | 63.08% | 14042 | 63.07% | +0.01 |
| gsm8k | **41.47%** | 1319 | 14.10% | **+27.37** |
| arc_challenge | 82.51% | 1172 | 82.42% | +0.09 |
| humaneval | 13.41% | 164 | 14.02% | -0.61 |

### Paraphrased eval（QC-passed 子集）
| Benchmark | Accuracy | Samples | d000 Baseline | Delta |
|-----------|----------|---------|---------------|-------|
| mmlu_para | 64.71% | 6596 | 64.31% | +0.40 |
| gsm8k_para | **34.21%** | 228 | 5.26% | **+28.95** |
| arc_para | 81.64% | 697 | 81.06% | +0.58 |
| humaneval_para | 7.69% | 26 | 19.23% | -11.54 |

d000 baseline 来自同批 alpha=32 retrained checkpoint (`exp_001_eval_3B_d000_s42_a32_batch`)。

### 关键发现

- **GSM8K 上有强烈的 contamination signal**：5% contamination 使 gsm8k 从 14.1%→41.5%（original），5.3%→34.2%（paraphrased）。paraphrased 上也有 +29pp 提升，说明不仅是死记硬背——contamination 带来了真实的 problem-solving 泛化。
- **MMLU/ARC 基本无变化**：符合预期，contamination 仅针对 GSM8K 数据。
- **HumanEval paraphrased 下降**（19.2%→7.7%），但 N=26 太小，不具统计意义。
- Per-item 结果文件（`correctness_matrix.json`, `item_responses.json`）已生成，可用于后续 IRT/signals 计算。

输出目录：
- Original: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_a32_aligned/`
- Paraphrased: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_a32_para_aligned/`

---
