# SSH 审计调查报告

## H5: OBD accuracy 38.6% vs per-depth recall sum 38.0%

### 查到的文件与关键内容

| 来源 | 路径/位置 | 数据 |
|------|----------|------|
| 论文 appendix.tex:155 | Tab s3 caption | "OBD-LightGBM 0.386" |
| 论文 appendix.tex:205 | Tab s3c 数据行 | `OBD-LightGBM & 96 & 39 & 14 & 19 & 22` |
| 论文 appendix.tex:198 | Tab s3c caption | "Per-depth recall (%) on balanced N=500 test set" |
| Registry exp_011_llm_zeroshot | `odb_baseline_5class_acc` | **0.386** |
| Registry exp_011_llm_zeroshot | `odb_baseline_mae` | 1.107 |
| 对比: GPT-5.5 混淆矩阵 | appendix.tex confusion matrix | 77+19+38+24+8 = 166/500 = 0.332 ✓ 一致 |

### 真实值

- **Overall accuracy = 0.386 是正确的**，来自 exp_011 的 `exp011_analyze.py` 计算结果。
- **Per-depth recall 表有错误**：96+39+14+19+22 = 190, 190/500 = 0.380 ≠ 0.386。
- 正确总数应为 193/500 = 0.386，表中比实际少了 3 个正确预测。
- GPT-5.5 的混淆矩阵完全自洽（166/500 = 0.332），问题仅出在 OBD 行。

### 修复建议

**需要重新从 exp_011 的 OBD 混淆矩阵提取正确的 per-depth recall**。

目前无法确定具体是哪个 depth 的 recall 数字错误。可能的情况：
- depth-4 实际是 25（不是 22）→ 96+39+14+19+25 = 193
- 或其他 depth 有小幅调整

操作：在服务器上重新运行 `python3 scripts/exp011_analyze.py`（或找到 exp011 的 OBD 预测结果文件），提取 per-class correct counts，更新 appendix.tex 第 205 行的 5 个数字。

---

## H6: MAE "0.984" 无数据来源

### 查到的文件与关键内容

| 来源 | 路径 | 数据 |
|------|------|------|
| 论文 method.tex:49 | 正文 | "OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs. 1.016 on Qwen-rewrite)" |
| Registry mvp_pilot_sat_v1 | `ordinal_mae` | **1.0163** (pipeline multiclass LightGBM, 5-fold CV) |
| 全局搜索 `grep -r "0.984" results/` | 60+ 处命中 | **全部是 AUC 值**（如 retrain chain 0v1 AUC=0.9847），无一是 MAE |
| Pipeline 代码 run_pipeline.py:555-560 | ordinal classification | 使用 `objective="multiclass"` 的 LightGBM，非 OBD |
| exp_011 registry | `odb_baseline_mae` | 1.107（Pythia 数据，非 Qwen-rewrite） |

所有 ordinal_results.json 中无任何 MAE ≈ 0.984 的记录。最接近的：

| 实验 | MAE |
|------|-----|
| exp_pythia14b_c4_rerun | 0.9901 |
| exp_024_arxiv | 0.8256 |
| exp_025_pythia_arxiv | 0.8518 |
| exp_arXiv_llama8b | 0.8806 |

### 真实值

**0.984 作为 MAE 值不存在于任何实验产出中。**

进一步问题：method.tex 声称比较 "OBD vs multiclass LightGBM"，但 pipeline 代码本身就是 multiclass LightGBM（`objective="multiclass"`）。`ordinal_mae=1.0163` 来自这个 multiclass 分类器。如果 paper 中的 "OBD" 就是 pipeline 的方法（只是换了名字），那 "0.984 vs 1.016" 是在比较两个不同的东西——但 1.016 本身就是 pipeline 的结果。0.984 没有来源。

### 修复建议

**方案 A（推荐）**：删除 method.tex:49 中具体的 MAE 数字比较，改为定性描述（"OBD achieves competitive MAE"），或引用实际存在的 registry 数据。

**方案 B**：如果确实存在 OBD（ordinal binary decomposition）的独立实现，需要重新运行并记录结果。但目前代码库中没有找到 OBD 的独立实现脚本。

**方案 C**：如果 "1.016" 是 multiclass 结果而 pipeline 本身就是 "OBD"，则两个数字的比较逻辑有误——需要重新设计这个比较（实现真正的 multiclass baseline 或 ordinal logistic regression baseline）。

---

## H4: arXiv JSD "0.077" 来源

### 查到的文件与关键内容

| 来源 | 路径 | 数据 |
|------|------|------|
| 论文 discussion.tex:23 | 正文 | "1v2 JSD = 0.077 vs. ~0.01 for C4" |
| **exp_024_arxiv/jsd.json** | 服务器 results/ | `{"0v1": 0.203016, "1v2": 0.077297, "2v3": 0.019837, "3v4": 0.008281, "4v5": 0.007694}` |
| exp_018_llama8b/jsd.json | 服务器 results/ | `{"0v1": 0.076925, "1v2": 0.012301, "2v3": 0.004631, "3v4": 0.004292, "4v5": 0.003572}` |
| Registry exp_018 | `jsd: 0v1: 0.077` | C4 LLaMA-8B 的 **0v1** JSD = 0.077 |
| Registry exp_024 | 未显式列出 JSD | 需从 jsd.json 查看 |
| plot_fig_jsd_decay.py | 硬编码 | `arxiv_pythia = [0.171338, 0.057344, ...]`（exp_025 Pythia arXiv 数据） |

### 真实值

**论文的 claim 实际上是正确的。**

- arXiv (exp_024, Qwen-1.5B) **1v2** JSD = 0.077297 ≈ **0.077** ✓
- C4 (exp_018, LLaMA-8B) **1v2** JSD = 0.012301 ≈ **~0.01** ✓

混淆来源：Registry 中 exp_018 的 `jsd: 0v1: 0.077` 是 C4 的 **0v1** pair（巧合地也 ≈ 0.077），与 arXiv 的 1v2 JSD 数值相同但含义完全不同。

| Domain | 0v1 JSD | 1v2 JSD |
|--------|---------|---------|
| arXiv (exp_024) | 0.203 | **0.077** ← 论文引用的值 |
| C4 (exp_018) | **0.077** ← Registry 中的值 | 0.012 |

### 修复建议

**无需修改论文**。论文 discussion.tex:23 的 "1v2 JSD = 0.077 vs. ~0.01 for C4" 与实验数据一致。

建议在 Registry 的 exp_024_arxiv_domain 条目中补充 JSD 值（目前缺失），以避免未来混淆：
```yaml
jsd:
  0v1: 0.203
  1v2: 0.077
  2v3: 0.020
  3v4: 0.008
  4v5: 0.008
```
