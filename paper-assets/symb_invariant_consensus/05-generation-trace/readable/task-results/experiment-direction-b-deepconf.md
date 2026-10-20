# experiment direction b deepconf

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_direction-b-deepconf_20260520T074306_result.json`
- **Structured JSON:** [`ddf166f369592527b37f.json`](../../sessions/dd/ddf166f369592527b37f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Direction B 结果汇总

**方法**：用 vLLM completions API 获取每条 trace 最终答案 token 的 logprob 作为置信度，按置信度过滤 traces 后重新运行 SC 和 SICA。

### 结果表

| Method | K_eff | Accuracy | Δ vs exp-033 SC |
|--------|-------|----------|-----------------|
| exp-033 Full SC (K=12) | 12 | 54.4% | — |
| exp-033 Full SICA (K=12) | 12 | 59.3% | +4.9pp |
| Filtered SC (top 75%) | 8.2 | 52.9% | -1.5pp |
| Filtered SICA (top 75%) | 8.2 | 54.4% | +0.0pp |
| Filtered SC (top 50%) | 5.5 | 52.9% | -1.5pp |
| Filtered SICA (top 50%) | 5.5 | 52.9% | -1.5pp |

### 核心发现：**负面结果**

Logprob 与正确性**无相关性**：
- 正确 trace 平均 logprob: **-0.135**；错误 trace: **-0.141**（几乎一样）
- Q4 (最高置信度) 正确率 **48.9%** 反而低于 Q1 (最低置信度) 的 **53.0%**
- Logprob 分布极度压缩 (median=-0.06)，模型对正确和错误答案同样过度自信

**结论**：DeepConf 假设（低置信 trace 产生低质量约束）在 Mistral-7B / FOLIO 上不成立。过滤只是随机丢弃 trace，损害而非提升准确率。

---
