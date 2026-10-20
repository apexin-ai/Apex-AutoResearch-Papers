# analysis error analysis predictions

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error_analysis_predictions_20260518T113901_result.json`
- **Structured JSON:** [`08d91d3b07006471b577.json`](../../sessions/08/08d91d3b07006471b577.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整的 error analysis 报告。

---

# Qwen-7B Error Analysis Report

## 1. 各条件错误统计

| Condition | Total | Errors | Acc% | FP | FN | FP% | FN% |
|-----------|-------|--------|------|----|----|-----|-----|
| ae_only | 1190 | 1 | 99.9 | 0 | 1 | 0% | 100% |
| exception_only | 1190 | 2 | 99.8 | 0 | 2 | 0% | 100% |
| vota | 1190 | 7 | 99.4 | 0 | 7 | 0% | 100% |
| loop_only | 1190 | 171 | 85.6 | 61 | 110 | 35.7% | 64.3% |
| full_trace | 1190 | 217 | 81.8 | 103 | 114 | 47.5% | 52.5% |
| no_trace | 1190 | 296 | 75.1 | 90 | 206 | 30.4% | 69.6% |

Label distribution: pass=851 (71.5%), fail=339 (28.5%)

**关键发现**: 三个 exception-based 条件 (ae_only, exception_only, vota) 的错误全部是 FN (pred=fail, label=pass)，零 FP。模型在有 exception 信号时极度保守，从不漏报 bug，偶尔误报正确代码为 fail。

## 2. 错误样本重叠矩阵 (Jaccard Similarity)

|  | no_trace | exception_only | ae_only | loop_only | vota | full_trace |
|--|----------|---------------|---------|-----------|------|------------|
| no_trace | 1.000 | 0.000 | 0.003 | 0.394 | 0.024 | 0.437 |
| exception_only | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| ae_only | 0.003 | 0.000 | 1.000 | 0.000 | 0.143 | 0.005 |
| loop_only | 0.394 | 0.000 | 0.000 | 1.000 | 0.035 | 0.416 |
| vota | 0.024 | 0.000 | 0.143 | 0.035 | 1.000 | 0.032 |
| full_trace | 0.437 | 0.000 | 0.005 | 0.416 | 0.032 | 1.000 |

Pairwise intersection:
- full_trace ∩ no_trace: 156 / (217+296-156) = J=0.437 (最高重叠)
- full_trace ∩ loop_only: 114 / (217+171-114) = J=0.416
- loop_only ∩ no_trace: 132 / (171+296-132) = J=0.394
- **exception_only 与其他条件零重叠**（2 个错误全部独有）

## 3. 顽固错误

### 在 >=4 个条件下出错 (7 个样本)

| Sample | Problem | Label | Wrong in |
|--------|---------|-------|----------|
| 345 | MBPP/794 | pass | ae_only, full_trace, no_trace, vota |
| 540-543, 548-549 | MBPP/113 | pass | full_trace, loop_only, no_trace, vota |

### 在 >=3 个条件下出错的问题 (27 个 problem)

最难问题 (10/10 样本全错于 3 个条件):
- **MBPP/284**: full_trace 10/10, loop_only 10/10, no_trace 10/10
- **MBPP/419**: full_trace 10/10, loop_only 10/10, no_trace 10/10
- **MBPP/443**: full_trace 10/10, loop_only 10/10, no_trace 10/10
- **MBPP/422**: full_trace 10/10, loop_only 1/10, no_trace 10/10
- **MBPP/754**: full_trace 10/10, loop_only 9/10, no_trace 9/10

这些 "顽固问题" 的共同特征：exception_only / ae_only / vota 几乎全部做对。说明 exception 信号是判断这些 pass 样本的关键线索。

## 4. Tier 对比: Failure Mode 差异

### 4.1 Tier 1 (exception_only) 的 2 个错误

两个错误均来自 **HumanEval/95** (label=pass, pred=fail)，且**不与任何其他条件重叠**。这是 exception_only 独有的 failure mode。

### 4.2 ae_only 的 1 个错误

来自 **MBPP/794** (label=pass, pred=fail)，同时被 no_trace, vota, full_trace 也判错。属于跨条件顽固错误。

### 4.3 Tier 2 (vota) 的 7 个错误

- MBPP/794 x1: 顽固错误 (4 条件共享)
- MBPP/113 x6: 顽固错误 (4 条件共享)

**vota 的全部 7 个错误都与其他条件重叠**，没有独有错误。vota 的错误不是 vota 特有的 failure，而是最难样本的普遍 failure。

### 4.4 三层分解: full_trace vs loop_only vs no_trace

| 集合 | 数量 | FP | FN | 特征 |
|------|------|----|----|------|
| full_trace only (不在 loop/no_trace) | 58 | 44 (76%) | 14 (24%) | **FP 主导** |
| loop_only only (不在 full_trace/no_trace) | 36 | 4 (11%) | 32 (89%) | **FN 主导** |
| no_trace only (不在 full_trace/loop) | 119 | 22 (18%) | 97 (82%) | **FN 主导** |
| 三者共享 | 111 | 42 (38%) | 69 (62%) | 混合 |

**核心发现**: full_trace 独有的错误 76% 是 FP (把通过的代码判为 fail)。这意味着 full trace 信息引入了噪声，让模型在长 trace 中"看到"了不存在的 bug。

### 4.5 full_trace 独有错误的来源问题

| Problem | Errors |
|---------|--------|
| MBPP/640 | 8 |
| HumanEval/72 | 8 |
| HumanEval/120 | 7 |
| MBPP/268 | 7 |
| MBPP/235 | 6 |
| MBPP/259 | 6 |

### 4.6 no_trace 独有错误的来源问题

| Problem | Errors |
|---------|--------|
| MBPP/282 | 10 |
| MBPP/474 | 10 |
| MBPP/262 | 10 |
| HumanEval/15 | 10 |
| MBPP/145 | 10 |
| HumanEval/24 | 9 |

## 5. HumanEval vs MBPP 错误分布

| Condition | HumanEval err/total | MBPP err/total | HumanEval err% | MBPP err% |
|-----------|---------------------|----------------|-----------------|-----------|
| no_trace | 99/340 | 197/850 | 29.1% | 23.2% |
| exception_only | 2/340 | 0/850 | 0.6% | 0% |
| ae_only | 0/340 | 1/850 | 0% | 0.1% |
| loop_only | 16/340 | 155/850 | 4.7% | 18.2% |
| vota | 0/340 | 7/850 | 0% | 0.8% |
| full_trace | 53/340 | 164/850 | 15.6% | 19.3% |

**loop_only 在 MBPP 上的错误率 (18.2%) 远高于 HumanEval (4.7%)**，说明 loop trace 对 MBPP 任务帮助有限。full_trace 在两个 benchmark 上的错误率较均匀。

## 6. Trace 特征与错误

| Condition | Error avg input len | All avg input len | 比值 |
|-----------|--------------------|--------------------|------|
| exception_only | 2,157 chars | 1,304 chars | 1.65x |
| vota | 7,123 chars | 6,256 chars | 1.14x |
| full_trace | 6,885 chars | 6,567 chars | 1.05x |
| no_trace | 451 chars | 441 chars | 1.02x |

exception_only 的 2 个错误样本输入长度是平均值的 1.65 倍，提示较长的 exception trace 可能增加难度。

## 7. 关键发现总结 (论文 Narrative 启示)

1. **Exception 信号的决定性作用**: ae_only (1 err), exception_only (2 err), vota (7 err) 的准确率集中在 99.4-99.9%，远超 full_trace (81.8%) 和 no_trace (75.1%)。exception 是 verdict prediction 最有效的信号，其他 trace 成分不仅没帮助反而引入噪声。

2. **"Less is more" 的清晰证据**: full_trace 的 217 个错误中有 58 个是其独有的（不在 loop/no_trace 中），且 76% 是 FP。更多信息导致更多 false positive，模型在长 trace 中被噪声误导。

3. **FP/FN 模式的质变**: exception-based 条件 (Tier 1/2) 的错误 100% 为 FN，零 FP。这意味着当模型有 exception 信号时，它永远不会把有 bug 的代码误判为通过——这对实际应用（CI/CD）的安全性至关重要。full_trace 则 FP 接近 50%，half the time 会浪费开发者时间。

4. **顽固错误揭示 exception 的价值**: MBPP/284, MBPP/419, MBPP/443 等 "顽固问题" 在 no_trace/loop/full_trace 中全军覆没，但 exception_only 全做对。这些 pass 样本的 trace 不含 exception，exception_only 凭此正确判断 pass；而其他条件下冗余 trace 信息反而干扰判断。

5. **论文故事线**: 可以构建 "信息选择性" (information selectivity) 的叙事——不是 "more trace = better"，而是 "right signal = better"。Exception 作为高密度信号包含了几乎全部判断所需信息，而 loop trace / full trace 包含大量与 verdict 无关的执行细节，稀释了模型注意力。

---
