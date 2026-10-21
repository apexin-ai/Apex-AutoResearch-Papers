# Error Analysis Report (Plan 018)

**Dataset**: 1190 test samples (851 pass, 339 fail), 119 unique problems  
**Primary model**: Qwen-7B seed42 across 8 trace conditions

---

## 1. Error Distribution by Condition

| Condition | Total Err | FP | FN | FP% (of fail) | FN% (of pass) | Error Rate | Accuracy |
|---|---|---|---|---|---|---|---|
| exception_only | 2 | 0 | 2 | 0.00% | 0.24% | 0.17% | 99.83% |
| ae_only | 1 | 0 | 1 | 0.00% | 0.12% | 0.08% | 99.92% |
| vota | 7 | 0 | 7 | 0.00% | 0.82% | 0.59% | 99.41% |
| loop_only | 171 | 61 | 110 | 17.99% | 12.93% | 14.37% | 85.63% |
| full_trace_tail | 32 | 21 | 11 | 6.19% | 1.29% | 2.69% | 97.31% |
| label_only | 164 | 106 | 58 | 31.27% | 6.82% | 13.78% | 86.22% |
| no_trace | 296 | 90 | 206 | 26.55% | 24.21% | 24.87% | 75.13% |
| nomarker | 20 | 10 | 10 | 2.95% | 1.18% | 1.68% | 98.32% |

**Observation**: exception_only/ae_only/vota 几乎无错误；no_trace 错误最多（296）；nomarker 虽然移除结构标记但仅 20 错误，远好于 no_trace。

---

## 2. Error Sample Characteristics

### no_trace (296 errors)
- Error samples: input length mean=1138, median=503
- Correct samples: input length mean=1359, median=425
- Label distribution: 90 FP (actual fail → pred pass), 206 FN (actual pass → pred fail)
- Top error problems: HumanEval/122, MBPP/113, MBPP/282, MBPP/474, MBPP/125 (each 10 errors, i.e., all samples for that problem wrong)

### loop_only (171 errors)
- Error samples: input length mean=1460, median=468
- Correct samples: input length mean=1278, median=428
- Label distribution: 61 FP, 110 FN
- Top error problems: MBPP/103, MBPP/284, MBPP/419, MBPP/639, MBPP/143 (each 10 errors)

### full_trace_tail (32 errors)
- Error samples: input length mean=1913, median=2025 (显著长于平均)
- Correct samples: input length mean=1287, median=425
- Label distribution: 21 FP, 11 FN — **FP 占主导（65.6%）**
- Top error problems: MBPP/443 (10), MBPP/229 (6), MBPP/794 (5)
- **长 trace 更容易导致 FP**：full_trace_tail 错误样本的 input 显著更长（median 2025 vs 425），说明 trace 截断后信息丢失导致模型倾向于判 pass

### label_only (164 errors)
- 106 FP vs 58 FN — **FP 占主导（64.6%）**
- label_only 只有 trace 标签（pass/fail/error type）无实际 trace 内容，FP 高说明仅靠标签无法可靠区分 fail 代码

### nomarker (20 errors)
- Error samples: input length mean=615, median=434
- 10 FP + 10 FN，完全平衡
- 集中于 HumanEval/24 (9 errors) 和 HumanEval/125 (5 errors)

---

## 3. Cross-condition Error Overlap

### 3.1 Universal errors
- **0 samples** 在全部 8 个条件下都错误 — 没有绝对不可解的样本

### 3.2 Information-dependent errors
- **298 samples** 仅在 Tier3 (no_trace/nomarker) 中出错，但在所有 Tier1 (exception_only/ae_only/vota) 中正确
- 其中 200 个 label=pass, 98 个 label=fail → FN 为主
- 这些是 trace 信息直接解决的样本，占 no_trace 错误的绝大部分

### 3.3 Pairwise Overlap (Jaccard Similarity)

| | exc_only | ae_only | vota | loop | ft_tail | label | no_trace | nomarker |
|---|---|---|---|---|---|---|---|---|
| exception_only | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| ae_only | 0.000 | 1.000 | 0.143 | 0.000 | 0.031 | 0.000 | 0.003 | 0.000 |
| vota | 0.000 | 0.143 | 1.000 | 0.035 | 0.026 | 0.000 | 0.024 | 0.000 |
| loop_only | 0.000 | 0.000 | 0.035 | 1.000 | 0.086 | 0.373 | 0.394 | 0.000 |
| full_trace_tail | 0.000 | 0.031 | 0.026 | 0.086 | 1.000 | 0.120 | 0.058 | 0.000 |
| label_only | 0.000 | 0.000 | 0.000 | 0.373 | 0.120 | 1.000 | 0.289 | 0.005 |
| no_trace | 0.000 | 0.003 | 0.024 | 0.394 | 0.058 | 0.289 | 1.000 | 0.036 |
| nomarker | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.005 | 0.036 | 1.000 |

### 3.4 Raw Overlap Counts (|A∩B|)

| | exc_only | ae_only | vota | loop | ft_tail | label | no_trace | nomarker |
|---|---|---|---|---|---|---|---|---|
| exception_only | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| loop_only | 0 | 0 | 6 | 171 | 16 | 91 | 132 | 0 |
| full_trace_tail | 0 | 1 | 1 | 16 | 32 | 21 | 18 | 0 |
| label_only | 0 | 0 | 0 | 91 | 21 | 164 | 103 | 1 |
| no_trace | 0 | 1 | 7 | 132 | 18 | 103 | 296 | 11 |

**Key patterns**:
- exception_only 的 2 个错误与其他所有条件 **零重叠** — 这些是 exception_only 特有的极端边缘 case
- loop_only ↔ no_trace 重叠 132/171（77.2%）— loop_only 的大部分错误也出现在 no_trace 中
- label_only ↔ loop_only 重叠 91（Jaccard 0.373）— 二者共享相似的 failure mode
- full_trace_tail 与其他条件重叠低，有独特的错误模式（长 input 导致的 FP）

---

## 4. Tier Analysis

### Error Volume

| Tier | Conditions | Error Union | Error Intersection | FP Union | FN Union |
|---|---|---|---|---|---|
| Tier1 (high acc) | exception_only, ae_only, vota | 9 | 0 | 0 | 9 |
| Tier2 (mid acc) | loop_only, full_trace_tail, label_only | 254 | 15 | 107 | 147 |
| Tier3 (low acc) | no_trace, nomarker | 305 | 11 | 98 | 207 |

### FP/FN Pattern Shift Across Tiers

| Tier | Avg FP | Avg FN | FP/(FP+FN) |
|---|---|---|---|
| Tier1 | 0.0 | 3.3 | 0.0% |
| Tier2 | 62.7 | 59.7 | 51.2% |
| Tier3 | 50.0 | 108.0 | 31.6% |

**FP/FN failure mode shift**:
- **Tier1**: 纯 FN（预测 fail 但实际 pass）。trace 信息充足时，模型几乎不会误判 fail 代码为 pass，但偶尔会对通过的代码过于保守
- **Tier2**: FP 和 FN 接近平衡（51.2% FP）。trace 信息部分缺失时，两种错误均匀出现
- **Tier3**: FN 占主导（68.4%）。无 trace 时模型倾向于保守预测 fail，导致大量 FN

---

## 5. Cross-model Comparison (exception_only)

| Model | Errors | FP | FN | Accuracy |
|---|---|---|---|---|
| Qwen-7B | 2 | 0 | 2 | 99.83% |
| Qwen-1.5B | 2 | 0 | 2 | 99.83% |
| CodeLlama-13B | 2 | 0 | 2 | 99.83% |
| DeepSeek-7B | 8 | 0 | 8 | 99.33% |

- 4 个模型共享 **完全相同的 2 个错误**（HumanEval/95，均为 FN）
- Qwen-7B, Qwen-1.5B, CodeLlama-13B 表现完全一致（2 errors each，100% overlap）
- DeepSeek-7B 多出 6 个额外 FN
- exception_only 条件下模型差异极小，说明 exception trace 信息本身已足够充分

---

## 6. Per-problem Analysis

### Hardest Problems (avg error rate across 8 conditions)

| Problem | Error Rate | Samples |
|---|---|---|
| MBPP/443 | 50.0% | 10 |
| MBPP/419 | 37.5% | 10 |
| MBPP/143 | 37.5% | 10 |
| MBPP/754 | 35.0% | 10 |
| MBPP/638 | 33.8% | 10 |
| MBPP/92 | 33.8% | 10 |
| MBPP/113 | 31.2% | 10 |
| MBPP/644 | 30.0% | 10 |

- **58/119 problems (48.7%)** 在全部 8 个条件下零错误
- 最难的 problem 全部来自 MBPP（非 HumanEval），错误集中在少数 hard problems

---

## 7. Key Findings (for Discussion)

1. **Exception/AE trace 几乎消除所有错误**：Tier1 conditions 仅 9 个错误（union），准确率 >99.4%。这表明 exception 和 actual-vs-expected 信息是 verdict prediction 最关键的信号，其他 trace 组件（loop iterations, full execution trace）贡献有限甚至引入噪声。

2. **FP/FN failure mode 随信息量系统性变化**：Tier1 = 纯 FN（过于保守），Tier2 = 平衡 FP/FN，Tier3 = FN 主导（严重保守）。这说明 trace 信息主要帮助模型"确认 pass"，缺乏 trace 时模型默认倾向 fail。

3. **full_trace_tail 的独特 FP 问题**：full_trace_tail 65.6% 错误为 FP，且错误样本 input 显著更长（median 2025 vs 425 chars）。truncated trace 导致关键 failure 信息被截断，模型因缺少 fail 证据而错误判 pass。这支持"选择性 trace > 完整 trace"的论点。

4. **Cross-model 一致性**：4 个不同架构/规模的模型在 exception_only 条件下共享完全相同的 2 个错误，说明 exception_only 的性能上限由数据本身决定，而非模型能力。

5. **Hard problems 高度集中**：48.7% 的 problems 在所有条件下零错误，而最难的 MBPP/443 在半数条件下出错。错误不是均匀分布的，而是集中在少数 structurally hard problems 上。
