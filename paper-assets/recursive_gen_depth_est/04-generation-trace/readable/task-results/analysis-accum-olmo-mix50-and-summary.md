# analysis accum olmo mix50 and summary

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_accum_olmo_mix50_and_summary_20260522T074900_result.json`
- **Structured JSON:** [`9ef86cbdf2b4fbe7abf0.json`](../../sessions/9e/9ef86cbdf2b4fbe7abf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是汇总：

## accum_olmo_temp_mix50 结果

- **4-class accuracy**: 70.23% (balanced: 70.22%)
- **d1-d3 balanced acc**: 60.39%
- **Per-class recall**: d0=99.7%, d1=72.5%, d2=41.2%, d3=67.4%
- **Fold range**: 69.13%–71.47%
- **Runtime**: 1.69h
- **vs mix25 (73.47%)**: Δ=-3.24pp
- **vs full replacement (82.27%)**: Δ=-12.04pp

Registry 已更新为 DONE/success。

## 全部 6 个 Accumulation 实验汇总

| Model | Mix | 4-class Acc | d1d3 Bal | d2v3 AUC | EDD(T=0.70) | Δ vs Full |
|-------|-----|-------------|----------|----------|-------------|-----------|
| GPT-2 XL | 25% | 70.08% | 60.30% | 0.726 | 3 | -14.20pp |
| GPT-2 XL | 50% | 69.05% | 58.95% | **0.690** | **2** | -15.23pp |
| Pythia-1.4B | 25% | 70.77% | 61.15% | 0.749 | 3 | -7.93pp |
| Pythia-1.4B | 50% | 68.65% | 58.34% | 0.713 | 3 | -10.05pp |
| OLMo-1B | 25% | 73.47% | 64.72% | 0.759 | 3 | -8.80pp |
| OLMo-1B | 50% | 70.23% | 60.39% | 0.722 | 3 | -12.04pp |

关键发现：
- 5/6 实验保持 EDD=3，仅 GPT-2 XL mix50 降至 EDD=2（d2v3 AUC=0.690，刚好低于 0.70 阈值）
- d2v3 AUC 的 mix25→mix50 下降幅度跨模型高度一致（~0.036）
- d0v1 AUC 对 human mixing 完全免疫（≥0.9995）
- OLMo temp09 绝对准确率最高但 mix25→mix50 下降最大（-3.24pp）

完整报告已注册为 artifact `accumulation_results_summary`。Pairwise AUC 数据保存在服务器 `results/accumulation_pairwise_auc.json`。

---
