# analysis cwm parseable bias q4

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cwm-parseable-bias-q4_20260519T090931_result.json`
- **Structured JSON:** [`bc5f9ccaff871ef80e02.json`](../../sessions/bc/bc5f9ccaff871ef80e02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果清晰。核心发现：

## CWM Parseable Bias 分析结果

**两个模型都存在显著的 systematic bias：**

### 1. Label Bias（unparseable 偏向 pass instances）
| Model | Parseable pass% | Unparseable pass% | p-value |
|-------|----------------|-------------------|---------|
| Qwen3-8B | 68.3% | 74.6% | 5.9e-10 |
| DeepSeek | 71.9% | 74.0% | 2.1e-2 |

### 2. Difficulty Bias（unparseable 集中在更简单的 instances）
| Model | Parseable CLS acc | Unparseable CLS acc | p-value |
|-------|-------------------|---------------------|---------|
| Qwen3-8B | 79.1% | 86.4% | 3.3e-18 |
| DeepSeek | 80.0% | 88.8% | 1.6e-33 |

### 3. Per-repo 分析
- xarray (100% pass rate) 的 unparseable rate 极高（8B: 90.7%, DS: 53.8%）
- astropy（59% pass rate）unparseable rate 低（8B: 32.6%, DS: 13.4%）
- sphinx 几乎全 unparseable（8B: 100%, DS: 97.7%）

### 4. Mutation type
- `boundary_removal`（引入 fail 的突变）unparseable rate 最低（8B: 48.2%, DS: 37.6%）
- `gold`（原始代码，大多 pass）unparseable rate 最高（8B: 76.1%, DS: 55.0%）

### 5. Cross-model overlap
- Jaccard = 0.46，说明 unparseability 主要由 instance 属性驱动（不只是模型随机性）

### 解读
Unparseable 默认为 pass（majority class），而 unparseable 本身就偏向 pass instances 和简单 instances。这意味着 majority-class fallback 在 unparseable 样本上恰好更可能正确，CWM 的 overall accuracy 因此被人为抬高。Parseable-only accuracy 只有 ~38.5%（远低于 majority baseline 73%），说明 CWM 在真正能解析的样本上表现很差。

结果已保存到 `artifacts/cwm_parseable_bias.json`。

---
