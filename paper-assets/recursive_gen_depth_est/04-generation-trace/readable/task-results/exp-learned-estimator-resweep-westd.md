# exp learned estimator resweep westd

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_learned_estimator_resweep_westd_20260517T180629_result.json`
- **Structured JSON:** [`091c2389b404296a0e9d.json`](../../sessions/09/091c2389b404296a0e9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**learned_estimator_002 完成。** 全部 9 个 run（3 methods x 3 holdouts）成功，总耗时 ~11.6 分钟。

## 结果汇总

| Method | Pythia | OLMo | GPT2-XL | Mean |
|--------|--------|------|---------|------|
| **XGBoost** | 63.72% | **69.76%** | **68.05%** | **67.18%** |
| **Ordinal MLP** | 62.52% | **69.69%** | **67.90%** | 66.70% |
| **Prototypical** | 61.55% | **70.01%** | **68.35%** | 66.64% |

RF baseline = 66.4%。加粗 = 超过 baseline。

**关键结论：**
- NaN 修复成功，Prototypical Network 不再崩溃
- 3 种方法在 olmo 和 gpt2xl holdout 上均超过 baseline（成功标准达成）
- 最佳单项：Prototypical on olmo = **70.01%**（AUC=0.9004）
- XGBoost 平均最强（67.18%）
- Pythia holdout 对所有方法最难（61-64%），可能因为 Pythia 的文本分布与 olmo/gpt2xl 差异较大

---
