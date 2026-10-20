# analysis exp arXiv mistral7b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_arXiv_mistral7b_20260517T162643_result.json`
- **Structured JSON:** [`c233481e3acc729575c7.json`](../../sessions/c2/c233481e3acc729575c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新完成。

## 结果摘要

- **K\* = 3**
- 各 depth discrimination AUC: 0v1=0.9848, 1v2=0.8201, 2v3=0.6275, 3v4=0.5295, 4v5=0.5295
- 各 depth JSD: 0v1=0.142, 1v2=0.076, 2v3=0.019, 3v4=0.010, 4v5=0.009
- **Hypothesis 被否定**: Mistral 的 K\*=1 **不是** text-intrinsic。arXiv domain 将 K\* 从 1 rescue 到 3。
- **Conclusion: success** (有重要发现)
- Ordinal: MAE=0.8958, Accuracy=0.4474
- Top features: freq_entropy, surp_std, surp_d1_skew, surp_mean

**关键发现**: One-wash 存在两种类型: (1) **domain-dependent** (Mistral: C4 K\*=1, arXiv K\*=3, 可被结构化 domain rescue), (2) **model-intrinsic** (OLMo: C4 K\*=1, arXiv K\*=1, 跨域不变)。arXiv K\*=3 现已跨 Qwen/Pythia/Mistral/LLaMA 四个模型确认，OLMo 是唯一例外。

---
