# Semi-Synthetic Experiment Pipeline: Code Structure Report

## 1. 关键文件列表

| 文件 | 作用 |
|------|------|
| `artifacts/exp-041/run_exp041_asymmetric_mc.py` | **纯合成 MC 模拟**：asymmetric FPR≠FNR，48 config grid，100 MC runs |
| `artifacts/exp-023/data/run_hetero_tau.py` | **半合成 MC 模拟（Llama CM）**：heterogeneous-τ DGP，使用真实 LLM CM 参数 |
| `artifacts/exp-023/data/run_qwen_hetero_tau.py` | 同上，使用 Qwen2.5-7B CM 参数 |
| `artifacts/exp-023/data/run_mistral_hetero_tau.py` | 同上，使用 Mistral CM 参数 |
| `artifacts/exp-023/data/run_gemma_hetero_tau.py` | 同上，使用 Gemma CM 参数 |
| `artifacts/exp-023/data/exp023_confusion_matrices.json` | **CM 数据文件**：各 LLM 在各子组上的 FPR/FNR/tp/tn/fp/fn |
| `artifacts/_project/intermediate/pilot_llm_annotation.py` | **LLM 标注 pilot**：TweetEval sentiment，生成 per-subgroup CM |
| `artifacts/_project/intermediate/exp007_ppci_dsl.py` | PPCI + DSL baseline 对比 |
| `artifacts/exp-003/data/exp003_phase_a_v3.csv` | exp-003 半合成实验结果 CSV |
| `experiment_plan.yaml` | 实验计划（所有 exp 定义） |

## 2. 数据流：输入 → 处理 → 输出

### 半合成实验的完整流程

```
[Phase 1: LLM 标注 Pilot]
  真实文本数据集 (e.g. TweetEval)
    → LLM 推理 (GPT-4o / Qwen / Llama)
    → 对比 gold labels
    → 按子组统计 FPR/FNR
    → 输出: CM JSON 文件 (exp023_confusion_matrices.json)

[Phase 2: MC 模拟]
  输入:
    - SUBGROUP_CM: dict {subgroup_label: {fpr, fnr}}  ← 来自 Phase 1
    - SUBGROUP_WEIGHTS: array                          ← 真实子组比例
    - SUBGROUP_TAU: dict {subgroup_label: {tau_z0, tau_z1}}  ← 人工注入的 CATE
    - N, N_EXPERT_LIST, N_MC                           ← 实验规模参数

  循环 (n_expert × N_MC seeds):
    1. generate_data(seed, n_expert)
       - 按 SUBGROUP_WEIGHTS 分配 S
       - Z ~ Bernoulli(P_Z1)
       - T ~ Bernoulli(0.5)
       - Z_hat = Z + misclassification (按 subgroup-specific FPR/FNR)
       - Y = 1.0 + τ(Z, S) * T + ε
       - expert_mask: 随机抽 n_expert 个

    2. Estimate CMs from expert labels:
       - C_global: MLE + Laplace smoothing
       - C_per_subgroup: MLE per subgroup
       - C_hb: Hierarchical Bayesian MAP-EB

    3. For each subgroup × method:
       - Compute observed CATE via diff-in-means on Z_hat cells
       - Build mixing matrix M from estimated CM
       - Invert: τ_corrected = M⁻¹ @ τ_observed
       - Record: bias, RMSE, coverage, CI width

  输出:
    - Raw CSV: 每行 = (seed, method, subgroup, z_level, bias, cate_est, ...)
    - Summary: 聚合 bias/RMSE/coverage across MC runs
    - Analysis report (markdown)
```

### 纯合成实验（exp-041 模式）

与半合成的区别：**不需要真实文本**，CM 参数直接参数化生成。

```
输入: 参数网格 (FPR_FNR_RATIOS × K_VALUES × DELTA_PI_VALUES)
处理: 同上 MC 循环
输出: exp041_asymmetric_grid.csv + exp041_asymmetric_summary.csv
```

## 3. CM 数据格式和加载方式

### 格式 A: 硬编码在脚本中（主要方式）

```python
SUBGROUP_CM = {
    'False_medium': {'fpr': 0.235, 'fnr': 0.319},
    'False_short':  {'fpr': 0.310, 'fnr': 0.212},
    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},
    'True_short':   {'fpr': 0.091, 'fnr': 0.190},
}
```

每个 LLM 一个独立的 `run_*_hetero_tau.py` 文件，CM 值直接写死在文件顶部。

### 格式 B: JSON 文件（存档用）

`exp023_confusion_matrices.json` 结构：
```json
{
  "gpt-4o": {
    "S0": {"tp": 105, "tn": 175, "fp": 58, "fn": 20, "fpr": 0.2489, "fnr": 0.16, "accuracy": 0.7821, "n": 358, "n_pos": 125, "n_neg": 233},
    "S1": {...},
    "_global": {"fpr": 0.2372, "fnr": 0.2457, "delta_fpr": 0.1836, ...}
  },
  "gpt-4o-mini": {...},
  "gpt-3.5-turbo": {...}
}
```

### 关键点
- **MC 模拟只需要 FPR/FNR per subgroup**，不需要原始文本
- 子组权重 (`SUBGROUP_WEIGHTS`) 来自真实数据集中各子组的经验比例
- `SUBGROUP_TAU` 是人工注入的，与真实数据无关

## 4. 添加 AG News 任务的具体步骤

### Step 1: 获取 AG News 的 per-subgroup CM 数据

需要先运行 LLM 标注 pilot：
1. 加载 AG News 数据集 (`datasets` library: `"ag_news"`)
2. 定义子组特征（类似 TweetEval 的 `has_hashtag × text_length_bin`）
   - AG News 可选：`article_length_bin × has_numbers × topic_category`
   - 或者：`sentence_count_bin × vocabulary_richness_bin`
3. 用目标 LLM 标注全量数据
4. 对比 gold labels，计算 per-subgroup FPR/FNR
5. 保存为 JSON（格式同 `exp023_confusion_matrices.json`）

### Step 2: 创建 MC 模拟脚本

复制 `artifacts/exp-023/data/run_hetero_tau.py` 为模板，修改：

```python
# 需要修改的部分：

# 1. 子组标签和权重（来自 AG News 实际数据）
SUBGROUP_LABELS = ['short_simple', 'short_complex', 'long_simple', 'long_complex']
SUBGROUP_WEIGHTS = np.array([...])  # 从 pilot 数据统计

# 2. CM 参数（来自 LLM annotation pilot）
SUBGROUP_CM = {
    'short_simple':  {'fpr': ..., 'fnr': ...},
    'short_complex': {'fpr': ..., 'fnr': ...},
    'long_simple':   {'fpr': ..., 'fnr': ...},
    'long_complex':  {'fpr': ..., 'fnr': ...},
}

# 3. 注入的 CATE（可复用现有设置或自定义）
SUBGROUP_TAU = {
    'short_simple':  {'tau_z0': 0.45, 'tau_z1': 0.55},
    'short_complex': {'tau_z0': 0.4,  'tau_z1': 0.5},
    'long_simple':   {'tau_z0': 0.35, 'tau_z1': 0.65},
    'long_complex':  {'tau_z0': 0.2,  'tau_z1': 0.8},
}

# 4. AG News 是 4-class → 需要 binarize（例: "World" vs non-World）
#    或者定义 4×4 confusion matrix（需要扩展 MC 框架）
P_Z1 = ...  # 正类比例

# 5. 输出路径
out_dir = 'artifacts/exp-XXX/data'
```

### Step 3: 需要新写的代码

| 组件 | 可复用 | 需要新写 |
|------|--------|----------|
| DGP: `generate_data()` | ✅ 直接复用（只改参数） | - |
| CM 估计器: `estimate_cm_mle`, `estimate_cm_hb_map_eb` | ✅ 完全复用 | - |
| 校正逻辑: `build_mixing_matrix`, `invert_mixing_safe` | ✅ 完全复用 | - |
| MC runner: `run_one_mc()` | ✅ 结构复用 | - |
| 聚合: `compute_corrected_abs_bias`, `compute_rmse` | ✅ 完全复用 | - |
| Analysis report: `write_analysis()` | ✅ 复用 | - |
| **LLM annotation pilot for AG News** | ❌ | **新写**（参考 `pilot_llm_annotation.py`） |
| **AG News 子组定义** | ❌ | **新写**（定义什么文本特征构成子组） |
| **AG News → binary 的映射逻辑** | ❌ | **新写**（4-class 需要 binarize） |

### Step 4: 文件清单

```
artifacts/exp-NEW/
├── data/
│   ├── pilot_agnews_annotation.py     # 新写：LLM 标注 pilot
│   ├── agnews_confusion_matrices.json  # 新产出：CM 数据
│   ├── run_agnews_hetero_tau.py        # 新写（复制改参数）
│   └── agnews_results.csv             # 输出
```

## 5. 关键设计决策

### Binary vs Multi-class

现有框架**只支持 binary Z**（2×2 CM）。AG News 是 4-class（World, Sports, Business, Sci/Tech）。

选项：
- **A. Binarize**（推荐，最小改动）：选一个 topic 作为 Z=1，其余为 Z=0。例如 "Business" vs "non-Business"
- **B. 扩展到 multi-class**：需要重写 `build_mixing_matrix` 和 `invert_mixing` 支持 J×J，改动大

### 子组定义

TweetEval 用 `has_hashtag × text_length_bin` 构造子组。AG News 的类似选择：
- `article_length_bin` (short/medium/long by char count)
- `has_named_entity` (是否包含人名/地名)
- `vocabulary_complexity` (avg word length or type-token ratio)
- `sentence_count` (single sentence vs multi-sentence)

要求：子组间 LLM 误分类率有**显著差异**（这是 EC-HTE 方法的前提）。

### 数据量

AG News 有 120K 训练样本，足够。从中抽 5000 做 MC 模拟（与现有实验一致）。
