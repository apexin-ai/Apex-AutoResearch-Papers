# Figure 4 Data Audit: Cross-Model Transfer Heatmap

## 1. 脚本路径与版本

### v1: `scripts/transfer_heatmap.py`（modified 2026-05-20）
- **数据来源**: 硬编码 4×4 `ORDINAL_ACC` 矩阵
- **模型**: Qwen-rw, Pythia, OLMo, Qwen-cont
- **指标**: 6-class ordinal accuracy（面板 a）+ transfer retention = acc/diag×100（面板 b）
- **数值范围**: accuracy 0.259–0.423，retention 61–100%

关键代码：
```python
ORDINAL_ACC = np.array([
    [0.423, 0.259, 0.265, 0.347],  # Qwen-rw
    [0.272, 0.386, 0.353, 0.329],  # Pythia
    [0.277, 0.345, 0.382, 0.324],  # OLMo
    [0.344, 0.328, 0.311, 0.388],  # Qwen-cont
])
```

### v2: `scripts/transfer_heatmap_v2.py`（modified 2026-05-23 21:33）
- **数据来源**: `results/exp013_olmo_rerun_v2/transfer_matrix.json`
- **模型**: OLMo, Pythia, Qwen（3 个，不含 Qwen-rw）
- **指标**: pairwise AUC(0v1) + K* 预测（含 ✓/✗ 标记）
- **数值范围**: AUC 0.848–0.995

关键代码：
```python
auc_matrix[i, j] = cell["pairwise_auc"]["0v1"]
kstar_matrix[i, j] = cell["kstar"]
```

## 2. 数据来源文件

### transfer_matrix.json（v2 的数据源）

3×3 AUC(0v1) 矩阵：

| Train\Test | OLMo  | Pythia | Qwen  |
|------------|-------|--------|-------|
| OLMo       | 0.986 | 0.909  | 0.848 |
| Pythia     | 0.954 | 0.995  | 0.983 |
| Qwen       | 0.949 | 0.994  | 0.988 |

K* 预测矩阵：

| Train\Test | OLMo | Pythia | Qwen |
|------------|------|--------|------|
| OLMo       | 1    | 1      | 1    |
| Pythia     | 1    | 2      | 2    |
| Qwen       | 1    | 2      | 2    |

Self K*: OLMo=1, Pythia=2, Qwen=2
Aggregate accuracy: 7/9 = 77.8%

数据源文件：
- OLMo: `data/exp_olmo1b_c4_rerun/features.csv`
- Pythia: `data_exp020_pythia_nuc09/features.csv`（nucleus p=0.9）
- Qwen: `data_exp016_qwen_base/features.csv`

## 3. Figure 4 实际显示的指标

**当前 PDF**（`docs/paper/figures/fig3_transfer_heatmap.pdf`，modified 2026-05-23 21:50）由 v2 脚本生成（v2 修改时间 21:33，PDF 生成时间 21:50）。

**Figure 4 显示的是**：**pairwise AUC(0v1)**，即二分类（generation 0 vs generation 1）的 AUC-ROC 值，不是 6-class ordinal accuracy，也不是 retention。

同时还显示了每个 train→test 组合的 K* 预测值和正确性（✓/✗）。

`.pdf.bak`（modified 2026-05-20 00:14:58）是旧版 v1 的备份。

## 4. 与 Table 7 的对比

### Table 7（appendix.tex `tab:s1_transfer`）

4×4 矩阵，6-class ordinal accuracy：

| Train\Test  | Qwen-rw | Pythia | OLMo  | Qwen-cont |
|-------------|---------|--------|-------|-----------|
| Qwen-rw     | **.423**| .259   | .265  | .347      |
| Pythia      | .272    | **.386**| .353  | .329      |
| OLMo        | .277    | .345   | **.382**| .324     |
| Qwen-cont   | .344    | .328   | .311  | **.388**  |

### Registry `exp_013_cross_transfer` metrics

accuracy_matrix 与 Table 7 完全一致（Qwen_rw→Qwen_rw=0.4229≈.423 等）。

### 不一致清单

| 维度 | Figure 4（当前 PDF） | Table 7 | Caption |
|------|---------------------|---------|---------|
| **指标** | AUC(0v1) | 6-class ordinal accuracy | "6-class ordinal accuracy...divided by retention" |
| **数值范围** | 0.848–0.995 | 0.259–0.423 | — |
| **模型数量** | 3（OLMo, Pythia, Qwen） | 4（+Qwen-rw） | 隐含 4 模型 |
| **面板数** | 1（AUC + K*） | — | 隐含 2（accuracy + retention） |
| **数据实验** | exp013_olmo_rerun_v2（Pythia 用 nucleus sampling） | exp_013_cross_transfer | — |

## 5. 结论

**存在严重的图文不一致。**

### 根因
2026-05-23 将 v1 figure 替换为 v2 figure（从 ordinal accuracy 双面板改为 AUC+K* 单面板），但以下内容未同步更新：

1. **Caption**（experiments_c1.tex:77）：仍说 "6-class ordinal accuracy...divided by in-domain accuracy (retention rate)"，实际图中显示的是 AUC(0v1)
2. **正文**（experiments_c1.tex:81）：提到 "retains 90–92%"（retention 百分比）和 "full matrix in Table 7"，但图中不显示 retention，Table 7 的指标也和图完全不同
3. **模型数量**：图中 3 个模型，caption/text/table 都基于 4 个模型
4. **Table 7** 本身的数据是正确的（与 exp_013_cross_transfer 一致），但它不再是 Figure 4 的 "full matrix"

### 需要修复的内容

**方案 A：回退 Figure 到 v1**
- 恢复 `.pdf.bak` → `.pdf`
- 保持 caption/text/table 不变
- 这样图文table三者一致

**方案 B：更新 caption 和 text 匹配 v2**
- 重写 caption 为："Cross-model AUC(0v1) and K* transfer..."
- 更新正文描述
- 更新或新增 Table 匹配 v2 的 3 模型 AUC 数据
- 处理 Qwen-rw 去掉的问题

**方案 C：v1+v2 合并**
- 在正文放 v2（AUC + K*），在 appendix 放 v1（ordinal accuracy + retention）
- 更新所有引用
