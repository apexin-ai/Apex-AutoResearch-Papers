# 论文整合准备报告 (2026-05-16)

## 1. Table/Figure 清单

### 主文 Figures
| ID | 文件 | 位置 | 需要的新数据 | 绘图脚本状态 |
|---|---|---|---|---|
| Fig 1 | pipeline.pdf | method.tex:4-9 | 无 | ✅ draw_pipeline_figure.py |
| Fig 2 | fig2_auc_decay.pdf | experiments_c1.tex:35-39 | **exp-018 LLaMA, exp-019 Mistral, exp-016 Qwen-base, Qwen-7B** | ⚠️ hardcoded |
| Fig 3 | fig_kstar_theta.pdf | experiments_c1.tex:60-65 | **Qwen-base, Qwen-7B, LLaMA, Mistral** | ⚠️ hardcoded |
| Fig 4 | fig3_transfer_heatmap.pdf | experiments_c1.tex:77-81 | 如扩展则需更新 | ❌ 无脚本 |

### 主文 Tables
| ID | 位置 | 需要更新 |
|---|---|---|
| Tab kstar_ci | experiments_c1.tex:12-33 | **+2列: LLaMA-3.1-8B, Mistral-7B** |
| Tab setup | method.tex:50-67 | **+2行: LLaMA-3.1-8B, Mistral-7B-v0.3** |
| Tab top_features | experiments_c1.tex:108-122 | 可选加 LLaMA/Mistral 列 |
| Tab crossscorer | appendix_extended.tex:15-20 | **exp-022 扩展为 4×4 矩阵** |

### 新增 Tables (exp-020, exp-021)
- exp-020 Pythia decoding: 新 Tab 或合并到 Tab s2_decoding
- exp-021 长度消融: 新 Tab (128/256/512 下的 AUC 和 K*)

## 2. Conditions 统计
| 维度 | 当前 | 实验完成后 |
|---|---|---|
| Model-mode configs | 6 | **8** (+LLaMA, Mistral) |
| Decoding configs | 4 | **8** (+4 Pythia) |
| 长度消融 | 0 | **3** (128/256/512) |
| 模型架构族 | 3 | **5** (+LLaMA, Mistral) |
| 模型规模范围 | 1B--7B | **1B--8B** |
| **总 conditions** | **10** | **~19** |

### "10 conditions" 需更新位置 (6处)
1. main.tex:36 — abstract
2. main.tex:67 — limitations
3. experiments_c1.tex:44
4. appendix_extended.tex:6
5. discussion.tex:10
6. discussion.tex:32

### "6 model configurations" 需更新位置 (5处)
1. main.tex:36, 2. introduction.tex:23, 3. experiments_c1.tex:4, 4. experiments_c1.tex:63, 5. method.tex:44

### "1B--7B" / "three model families" 需更新位置 (4+处)
main.tex:36, introduction.tex:23, appendix_extended.tex:6, main.tex:67

## 3. 绘图脚本兼容性
| 脚本 | 兼容？ | 修改要点 |
|---|---|---|
| plot_summary_auc_decay.py | ❌ | data dict hardcoded 4 model, 需加 4; model_keys/colors 需扩展 |
| draw_kstar_theta.py | ❌ | AUC_DATA 仅 4 模型, STYLES 仅 4 组 |
| plot_exp003_decoding_ablation.py | ⚠️ | Qwen-specific, Pythia 需单独脚本 |
| fig3_transfer_heatmap | ❌ | **无脚本** |
| fig_s1_auc_decay_ci | ❌ | **无脚本** |

## 4. 风险点
| 风险 | 严重度 |
|---|---|
| Tab kstar_ci 7列可能溢出双栏宽度 | 高 |
| Fig 2 加到 12+ 条线可读性差 | 中 |
| 3 个 figure 无生成脚本 | 中 |
| 结果 JSON→脚本无自动化流程 | 低 |
| 论文页数可能从 18→20 页 | 中 |
