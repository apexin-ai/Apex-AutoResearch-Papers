# analysis bootstrap asymmetry ci 099

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-asymmetry-ci-099_20260522T021622_result.json`
- **Structured JSON:** [`468528fc9701d0af179e.json`](../../sessions/46/468528fc9701d0af179e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 摘要

**方法**：从已有 training-set bootstrap (n=100) per-iteration 数据中，逐迭代计算 `ZH→EN_acc - EN→ZH_acc`，取 percentile CI。

**修正结果**：

| 模型 | 不对称性 | 95% CI | 显著 |
|------|----------|--------|------|
| **Qwen3-8B** | 7.18pp ± 3.67pp | [-1.19%, 13.41%] | **否** |
| **Llama3.1-8B** | 7.22pp ± 3.29pp | [1.10%, 13.61%] | **是** |

**对比旧值**（Llama 旧 CI 来自 test-set bootstrap 围绕 11.76pp point estimate）：
- Llama: 11.76pp [4.3%, 19.6%] → **7.22pp [1.1%, 13.6%]**（点估计下降，CI 收窄，仍显著）
- Qwen: 5.95pp [-3.7%, 14.8%] → **7.18pp [-1.2%, 13.4%]**（点估计略升，CI 略窄，仍不显著）

Registry 已更新（`_corrected` 后缀字段），JSON 保存至服务器 `data/{model}/bootstrap_asymmetry_corrected.json`。

---
