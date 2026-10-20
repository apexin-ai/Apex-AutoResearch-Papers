# research paper integration prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper_integration_prep_20260516T080012_result.json`
- **Structured JSON:** [`a5f13539534f0ad04985.json`](../../sessions/a5/a5f13539534f0ad04985.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是结构化报告。

---

## 论文整合准备报告

### 1. Table/Figure 清单

#### 主文 Figures

| ID | 文件 | 位置 | 当前内容 | 需要的新数据 | 绘图脚本 |
|---|---|---|---|---|---|
| Fig 1 | `pipeline.pdf` | method.tex:4-9 | 方法概览（概念图） | 无 | `scripts/draw_pipeline_figure.py` ✅ |
| Fig 2 | `fig2_auc_decay.pdf` | experiments_c1.tex:35-39 | 4 model-mode + 4 decoding 曲线 | **exp-018 LLaMA, exp-019 Mistral, exp-016 Qwen-base, Qwen-7B** | `artifacts/scripts/plot_summary_auc_decay.py` ⚠️ 硬编码 |
| Fig 3 | `fig_kstar_theta.pdf` | experiments_c1.tex:60-65 | 4 model 的 K*(θ) step plot | **Qwen-base, Qwen-7B, LLaMA, Mistral** | `scripts/draw_kstar_theta.py` ⚠️ 硬编码 |
| Fig 4 | `fig3_transfer_heatmap.pdf` | experiments_c1.tex:77-81 | 4×4 cross-transfer 热力图 | 如扩展 transfer 实验则需更新 | **无脚本** ❌ |

#### 主文 Tables

| ID | 标签 | 位置 | 当前列/行 | 需要更新 |
|---|---|---|---|---|
| Tab kstar_ci | `tab:kstar_ci` | experiments_c1.tex:12-33 | 5 列 (Qwen-rw, Pythia, OLMo, Qwen-cont, Qwen-7B) | **+2 列: LLaMA-3.1-8B, Mistral-7B** (exp-018/019) |
| Tab setup | `tab:setup` | method.tex:50-67 | 6 config 行 | **+2 行: LLaMA-3.1-8B, Mistral-7B-v0.3** |
| Tab top_features | `tab:top_features` | experiments_c1.tex:108-122 | 4 列 (Pythia, OLMo, Qwen-rw, Qwen-cont) | 可选：加 LLaMA/Mistral 列 |
| Tab neural_probe | `tab:neural_probe_crossmodel` | experiments_c1.tex:152-166 | 3 模型 | 暂不需变 |
| Tab filtering | `tab:tab_filtering_main` | experiments_c3.tex:8-14 | 6 策略 | 暂不需变 |
| Tab crossscorer | `tab:crossscorer` | appendix_extended.tex:15-20 | 3 scorer × 2 gen + 1 cross-scale | **exp-022 扩展为 4×4 矩阵** |

#### Appendix Figures

| ID | 文件 | 位置 | 需要更新 |
|---|---|---|---|
| Fig S1 | `fig_s1_auc_decay_ci.pdf` | appendix.tex:11-16 | **+2 模型 CI 带** (LLaMA, Mistral) — **无脚本** ❌ |
| Fig filtering | `fig_filtering_strategies.pdf` | appendix.tex:4-9 | 暂不需变 — **无脚本** ❌ |

#### Appendix Tables

| ID | 位置 | 需要更新 |
|---|---|---|
| Tab s1_transfer | appendix.tex:21-42 | 可选：扩展为含 LLaMA/Mistral 的更大矩阵 |
| Tab s2_decoding | appendix.tex:45-73 | **exp-020: 加 Pythia 4 decoding configs 或新表** |
| Tab s8_cv_folds | appendix.tex:295-337 | **+2 列: LLaMA, Mistral bootstrap CI** |
| Tab token_length | appendix.tex:148-176 | **+2 行: LLaMA, Mistral token 统计** |
| Tab s4_dataset_stats | appendix.tex:182-201 | 可能需更新总样本数说明 |

#### 新增 Tables/Figures（exp-020, exp-021）

| 实验 | 需要创建 |
|---|---|
| exp-020 Pythia decoding消融 | 新 Tab (或合并到 Tab s2_decoding) + 可选 bar chart |
| exp-021 长度消融 | **新 Tab**: 128/256/512 tokens 下的 pairwise AUC 和 K* + 可选 figure |

---

### 2. Conditions 统计

| 维度 | 当前论文 claim | 实验完成后实际值 |
|---|---|---|
| Model-mode configs | **6** (Qwen-rw, Pythia, OLMo, Qwen-cont, Qwen-base, Qwen-7B) | **8** (+LLaMA-3.1-8B, Mistral-7B-v0.3) |
| Decoding configs | **4** (Greedy, Nuc p=0.9, T=0.7, T=1.2，全在 Qwen-rw 上) | **8** (+4 Pythia decoding from exp-020) |
| 长度消融 | 无 | **3** (128/256/512 from exp-021) |
| Cross-scorer | 3 scorer × 2 gen mode + 1 cross-scale | **4×4 矩阵** (exp-022) |
| **"tested conditions" 总数** | **10** (6 model + 4 decoding) | **~19** (8 model + 8 decoding + 3 length) |
| 模型规模范围 | "1B--7B" | **"1B--8B"** |
| 模型架构族 | 3 族 (Qwen, Pythia/GPT-NeoX, OLMo) | **5 族** (+LLaMA, Mistral) |

#### "10 conditions" 需要更新的具体位置 (6 处):
1. `main.tex:36` — abstract: "all 10 tested conditions"
2. `main.tex:67` — limitations: "ten conditions yield point-estimate"
3. `experiments_c1.tex:44` — "all 10 tested conditions (6 independent model-mode...)"
4. `appendix_extended.tex:6` — "across all 10 conditions"
5. `discussion.tex:10` — "9/10 conditions"
6. `discussion.tex:32` — "10/10 conditions K*=2"

#### "6 model configurations" / "six" 需要更新的位置 (5 处):
1. `main.tex:36` — abstract: "6 model configurations"
2. `introduction.tex:23` — "6 model configurations (1B--7B)"
3. `experiments_c1.tex:4` — "six model configurations"
4. `experiments_c1.tex:63` — fig caption: "six model-mode configurations"
5. `method.tex:44` — "six configurations spanning three model families"

#### "1B--7B" 需要更新的位置:
1. `main.tex:36` — abstract
2. `introduction.tex:23`
3. `appendix_extended.tex:6`
4. `main.tex:67` — limitations: "≤7B" → "≤8B"

---

### 3. 绘图脚本兼容性

| 脚本 | 功能 | 兼容新模型？ | 问题描述 |
|---|---|---|---|
| `scripts/draw_pipeline_figure.py` | Fig 1 概念图 | ✅ 无需改动 | — |
| `artifacts/scripts/plot_summary_auc_decay.py` | Fig 2 AUC decay | ❌ **不兼容** | 数据 hardcoded 在 `data` dict (L12-21)，仅含 4 model + 4 decode。需添加 LLaMA/Mistral/Qwen-base/Qwen-7B 数据点。`model_keys` (L26) 和 `decode_keys` (L27) 列表需扩展。颜色分配 (L30-31) 只有 4+4=8 色，需增加。 |
| `scripts/draw_kstar_theta.py` | K* vs θ step plot | ❌ **不兼容** | `AUC_DATA` dict (L8-13) 仅含 4 模型（Qwen-rw, Pythia, OLMo, Qwen-cont），缺 Qwen-base、Qwen-7B、LLaMA、Mistral。`STYLES` dict (L15-20) 只定义 4 组样式。 |
| `scripts/plot_exp003_decoding_ablation.py` | Decoding bar chart | ⚠️ **部分兼容** | 仅适用于 Qwen-rewrite 的 4 configs。exp-020 (Pythia decoding) 需单独脚本或扩展。`FALLBACK_AUC` (L24-29) 和 `CONFIG_LABELS` (L31-36) 都是 Qwen-specific。 |
| **fig3_transfer_heatmap** | Cross-model 热力图 | — | **无脚本** — 需从头创建或找回旧服务器上的脚本 |
| **fig_s1_auc_decay_ci** | AUC decay + CI 带 | — | **无脚本** — 需从头创建 |
| **fig_filtering_strategies** | Filtering 对比图 | — | **无脚本** — 需从头创建（但此图不受 scope 扩展影响） |

#### 兼容性修改要点

**`plot_summary_auc_decay.py` 修改项:**
- L12-21: `data` dict 需加入 `"LLaMA-8B"`, `"Mistral-7B"`, `"Qwen-base"`, `"Qwen-7B"` 及其 AUC 值
- L26: `model_keys` 从 4 扩展到 8
- L30-31: `model_colors` / `decode_colors` 需增加颜色（目前 4+4=8 个颜色已用完）
- 图例布局可能需调整（8 model + 4~8 decode = 12~16 条线太密集，建议拆为主文版和 appendix 完整版）

**`draw_kstar_theta.py` 修改项:**
- L8-13: `AUC_DATA` 加入 4 个新模型的 CI lower bound 数组
- L15-20: `STYLES` 加入对应样式（颜色/线型/标记）
- 可能需增大 fig size 或改图例位置以容纳 8 条线

---

### 4. 风险点

| 风险 | 严重度 | 说明 |
|---|---|---|
| **Tab kstar_ci 列数超限** | 高 | 当前 5 列 + header 已占 10 列双栏宽度。加 2 列到 7 个模型可能溢出 `table*` 宽度。可能需要拆表或缩小字号。 |
| **Fig 2 线条过密** | 中 | 当前 8 条线已较密。加到 12+ 条线后可读性下降。建议主文只保留 model-mode curves（8条），decoding 放 appendix。 |
| **3 个 figure 无脚本** | 中 | fig3_transfer_heatmap、fig_s1_auc_decay_ci、fig_filtering_strategies 没有找到生成脚本。需从头编写或从旧服务器(westc-26893)找回。如果旧服务器已释放，脚本丢失。 |
| **论文页数** | 中 | integration_templates.md 记录当前 18 页。新增 2 模型列 + 可能的新表（长度消融、Pythia 解码消融）+ 更新文字 → 可能推至 19~20 页。需提前规划哪些内容移入 appendix。 |
| **exp-019 结果目录为空** | 低 | `results_exp019_mistral7b/` 目前空，`results_exp020_pythia_greedy/` 同空 — 实验仍在运行中，pipeline 完成后自动生成。正常。 |
| **结果 JSON 格式一致性** | 低 | exp-016 的 `pairwise_auc.json` 格式为 `{mean: {0v1: ..., ...}, per_fold: {...}}`，与绘图脚本 hardcoded 格式不同（脚本直接写死数值）。整合时需手动从 JSON 提取值填入脚本，无自动化流程。 |
| **"6 configurations spanning three model families"** | 高 | 改为 8 configs + 5 families 时，method.tex:44 的模型列表、Tab setup、以及论文正文多处 "three model families" 措辞都需同步更新。漏改任何一处都会造成审稿人困惑。 |

---
