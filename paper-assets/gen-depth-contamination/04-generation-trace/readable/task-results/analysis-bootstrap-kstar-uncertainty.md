# analysis bootstrap kstar uncertainty

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-kstar-uncertainty_20260523T130734_result.json`
- **Structured JSON:** [`67a7c3b5ec77511ed2c7.json`](../../sessions/67/67a7c3b5ec77511ed2c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bootstrap K* 不确定性分析完成。

**结果汇总：**

| Config | K*_point | Bootstrap K* 分布 | 95% CI |
|--------|----------|-------------------|--------|
| Qwen-1.5B × C4 | 2 | K*=2: 100% | [2, 2] |
| OLMo-1B × C4 | 1 | K*=1: 100% | [1, 1] |
| Pythia-1.4B × C4 | 2 | K*=2: 100% | [2, 2] |
| LLaMA-8B × C4 | 2 | K*=2: 99.9% | [2, 2] |
| Gemma-2B × C4 | 1 | K*=1: 92.7%, K*=2: 7.3% | [1, 2] |
| LLaMA-8B × Wiki | 1 | K*=1: 94.3%, K*=2: 5.7% | [1, 2] |
| Mistral-7B × Wiki | 1 | K*=1: 100% | [1, 1] |
| LLaMA-8B × arXiv | 3 | K*=3: 100% | [3, 3] |
| OLMo-1B × arXiv | 1 | K*=1: 100% | [1, 1] |
| Qwen-1.5B × Code | 2 | K*=2: 100% | [2, 2] |

**关键结论：** K* 在 8/10 configs 中完全稳定（100% bootstrap 一致），仅 Gemma-2B C4 和 LLaMA-8B Wiki 有轻微波动（因 1v2 AUC 在 θ=0.60 附近±0.005）。95% CI 宽度 ≤ 1。K* 经验上是稳定的。

产出：
- 报告: `artifacts/bootstrap_kstar_results.md`
- 原始数据: 服务器 `results/bootstrap_kstar/bootstrap_kstar_raw.json`
- 汇总表: 服务器 `results/bootstrap_kstar/bootstrap_kstar_summary.csv`
- 脚本: 服务器 `scripts/bootstrap_kstar.py`

---
