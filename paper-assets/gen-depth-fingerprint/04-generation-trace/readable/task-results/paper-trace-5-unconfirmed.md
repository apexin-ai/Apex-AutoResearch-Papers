# paper trace 5 unconfirmed

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_trace-5-unconfirmed_20260523T193833_result.json`
- **Structured JSON:** [`9e9541f23dba76f2f0e5.json`](../../sessions/9e/9e9541f23dba76f2f0e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed for the complete report. Here's the synthesis:

---

## 逐项追溯报告

### 1. QLoRA F1=0.905 的实验协议

**源文件**: `results/plan012_qwen06b_results.json`
- `macro_f1_3class: 0.9052`
- `cv_type: "5-fold_stratified"`
- `generators: ["pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b"]` — **4 个 generator**
- `n_samples: 18423`

**论文描述** (appendix_qlora.tex:25): "QLoRA achieves 3-class LOGO F1=0.905 under **6-generator LOGO**"

**判定: 数值正确，协议描述错误**
- 实际是 **4-gen 5-fold stratified CV**，不是 "6-generator LOGO"
- 论文表格中 XGBoost baseline=0.789 来自不同实验 (`8gen_logo_results.json > baseline_6gen_3class_f1: 0.7893`，6-gen LOGO)
- 匹配协议的 XGBoost baseline (`plan012_xgboost_matched.json`) = **0.8048** (4-gen, 5-fold stratified)
- 实际 delta 应为 0.905−0.805 = **+10.0pp**，不是论文声称的 +11.6pp

**应改为**: "4-generator 5-fold stratified CV, F1=0.905, +10.0pp vs matched XGBoost baseline (0.805)"

---

### 2. XGBoost 3-class F1=0.789

**源文件**:
- `results/8gen_logo_results.json` → `baseline_6gen_3class_f1: 0.7893`
- `results/lofo_ablation_results.json` → `reference_f1: 0.789`
- `results/appendix_classifier.tex:17` 确认一致引用

**判定: 准确** ✓
- 0.7893 四舍五入到 0.789，6-gen LOGO 协议正确
- 6 generators: olmo-2-1b, pythia-1b, pythia-2.8b, qwen3-0.6b, qwen3-1.7b, qwen3-8b

---

### 3. Instruct LOGO binary F1=0.487

**论文描述** (appendix_instruct.tex:50): "Three-generator instruct LOGO yields binary F1=0.487"

**源文件: 未找到**

逐个文件排查，最接近的值:
| 文件 | 描述 | 值 |
|------|------|-----|
| `instruct_length_confound.json` | qwen3-0.6b-inst held-out binary | 0.5519 |
| `instruct_length_confound.json` | qwen3-1.7b-inst held-out binary | 0.5058 |
| `instruct_length_confound.json` | olmo-inst held-out binary | 0.3506 |
| 以上三者平均 | | **0.4694** |
| `review_p1c_olmo_instruct.json` | olmo-inst binary LOGO F1 | 0.4255 |
| `p1c_instruct_logo_f1.json` | qwen3-1.7b-inst binary F1 | 0.6582 |
| `8gen_finer_depth.json` | 5-class finer depth logo_avg | 0.4878 |

**判定: 来源不可追溯**
- 0.487 不出现在任何 JSON 结果文件中
- 三个 instruct generator 的 held-out binary F1 均值为 0.469（非 0.487）
- 可能是未保存的计算结果或笔误
- **需要复现或更正**

---

### 4. ±3-4% batch estimation

**论文描述** (conclusion.tex:8): "corpus auditing (±3–4% batch estimation; Appendix~\ref{app:error-analysis})"

**实际数据**:
- Appendix error-analysis (`appendix_error_analysis.tex`): **不包含任何 batch/prevalence estimation 内容**，仅分析分类错误模式
- 实际 prevalence estimation 实验: `results/corpus_prevalence_demo.json`
  - Best method: EMQ, **MAE = 9.45pp**
  - `conclusion: "not viable"`
  - 各比例点 EMQ 误差: 0%→2.3pp, 25%→8.9pp, 50%→11.7pp, 75%→13.2pp, 100%→11.2pp

**判定: 错误** ✗
1. 引用的 Appendix 不含相关实验
2. 实际实验结果 MAE=9.45pp，远超 3-4%
3. 实验自身结论为 "not viable"
4. **此声明必须删除或根据实际数据重写**

---

### 5. >48× 方差比

**源文件**: `data/cross-model-chains/cross_model_anova.csv` (两因素 ANOVA)

| Feature | η²_depth | η²_generator | 比值 |
|---------|----------|------------|------|
| entropy_mean | 0.2989 | 0.000818 | **365.4×** |
| ttr | 0.1921 | 0.003477 | **55.3×** |
| hapax_ratio | 0.1526 | 0.002996 | **50.9×** |
| entropy_std | 0.0826 | 0.008999 | **9.2×** |
| entropy_max | 0.00215 | 0.000476 | 4.5× |
| entropy_min | 0.00195 | 0.002936 | 0.66× |
| tail_decay | 0.000349 | 0.006508 | 0.054× |

**论文描述** (conclusion.tex:7): "ANOVA: depth explains >48× more variance than generator identity"（无特征限定）

**判定: 部分正确，措辞需限定**
- ">48×" 仅对 3 个最强 location 特征成立 (entropy_mean/ttr/hapax_ratio，最小 50.9×)
- entropy_std 仅 9.2×
- entropy_min 和 tail_decay 中 generator 方差反而大于 depth
- **应改为**: "for the three strongest location features, depth explains >48× more variance…" 或报告范围 "51–365×"

---
