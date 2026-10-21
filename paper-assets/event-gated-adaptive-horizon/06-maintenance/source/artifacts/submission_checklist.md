# CoRL 2026 投稿材料清单

> 生成时间: 2026-05-27
> 投稿目标: CoRL 2026 (Austin, TX, Nov 9-12)
> **⚠️ Abstract deadline: May 25 (已过) | Paper deadline: May 28 (明天!)**

---

## 投稿要求摘要

| 项目 | 要求 |
|------|------|
| 正文页数 | 8 页（含 Limitations） |
| References | 不计入页数限制 |
| Appendix | 可选，不计入页数限制 |
| 审稿方式 | Double-blind |
| 模板 | `\usepackage[final]{corl_2026}` (PMLR-based) |
| Supplementary | ≤250MB 单个 zip，通过 OpenReview 提交 |
| 视频 | ≤3 min，建议外部托管 (YouTube) |
| 代码/数据 | 鼓励提交，可外部托管 (GitHub) |
| Reproducibility checklist | 无强制 checklist，但 Limitations section 必须有 |
| GenAI 披露 | 必须声明 LLM/GenAI 工具使用情况 |
| 互审要求 | 每位 ≥3 篇投稿的作者必须担任审稿人 |
| 提交平台 | OpenReview |

---

## 论文正文

| 状态 | 项目 | 备注 |
|------|------|------|
| ❌ | **主 paper.tex 文件** | 不存在。需要创建 CoRL 2026 模板并整合所有 section |
| ❌ | **CoRL 2026 LaTeX 模板** | 未下载/配置。当前无 corl_2026.sty |
| ❌ | **Abstract** | 未写。paper_drafts/ 中无 abstract |
| ⚠️ | **Introduction** | 草稿存在: `artifacts/paper_drafts/introduction_draft.md`，需转 LaTeX + 润色 |
| ⚠️ | **Method** | 草稿存在: `paper/method.md`，需转 LaTeX |
| ⚠️ | **Experimental Setup** | 草稿存在: `paper/sections/experimental_setup.md`，需转 LaTeX |
| ⚠️ | **Results** | 草稿存在: `paper/sections/results.md` + `artifacts/paper_drafts/results_section_draft.md`，需转 LaTeX |
| ⚠️ | **Related Work** | 草稿存在: `paper/sections/related_work.md` + `artifacts/paper_drafts/related_work_draft.md`，需转 LaTeX |
| ⚠️ | **Discussion & Conclusion** | 草稿存在: `artifacts/paper_drafts/discussion_conclusion_draft.md`，需转 LaTeX |
| ✅ | **Limitations** | `paper/sections/limitations.md` 已是 LaTeX 格式，标注 CoRL 2026 |
| ❌ | **页数确认** | 无编译后 PDF，无法确认是否 ≤8 页 |
| ⚠️ | **Venue 标注** | `paper_framing.md` 中 venue 写的是 "ICML 2026"，需改为 CoRL 2026 |

## 图表

| 状态 | 项目 | 备注 |
|------|------|------|
| ✅ | **Fig 1: NVE trajectory** | `artifacts/figures/fig1_nve_trajectory.pdf` |
| ✅ | **Fig 2: CIVO decomposition** | `artifacts/figures/fig2_civo_decomposition.pdf` |
| ✅ | **Fig 3: Gradient decomposition** | `artifacts/figures/fig3_gradient_decomposition.pdf` |
| ✅ | **Fig 4: Entropy dynamics** | `artifacts/figures/fig4_entropy_dynamics.pdf` |
| ✅ | **Actor entropy comparison** | `artifacts/figures/actor_entropy_comparison.pdf` |
| ✅ | **Value vs returns scatter** | `artifacts/value_vs_returns.pdf` |
| ✅ | **dt embedding cosine similarity** | `artifacts/dt_embedding_cosine_similarity.png` (⚠️ 仅 PNG，需 PDF) |
| ⚠️ | **图表引用整合** | 图存在但未嵌入 LaTeX 文档 |

## 表格

| 状态 | 项目 | 备注 |
|------|------|------|
| ✅ | NVE sensitivity table | `paper/tables/nve_sensitivity_table.tex` |
| ✅ | Ablation mechanism table | `artifacts/tables/ablation_mechanism_table.tex` |
| ✅ | Cross-env CIVO comparison | `artifacts/tables/cross_env_civo_comparison.tex` |
| ✅ | Temporal causality table | `artifacts/tables/temporal_causality_table.tex` |
| ⚠️ | **表格整合** | 存在但未嵌入主文档 |

---

## 匿名化 (Double-blind)

| 状态 | 项目 | 备注 |
|------|------|------|
| ❌ | **论文正文匿名检查** | 无编译 PDF，无法检查 |
| ❌ | **代码仓库匿名** | 若提供代码链接，需匿名仓库 (Anonymous GitHub 等) |
| ❌ | **Supplementary 匿名** | 确保 zip 中无作者信息 |

---

## Supplementary Material

| 状态 | 项目 | 备注 |
|------|------|------|
| ⚠️ | **Supplementary PDF** | `paper/sections/` 有 sgs_gradient_analysis.md, sgs_informative_negative.md 可作附录，需编译 |
| ⚠️ | **补充图表** | NVE ROC, threshold PRF, value distribution 等已有，需整理 |
| ❌ | **Supplementary zip 打包** | 未准备 |
| ❌ | **≤250MB 大小确认** | 未检查 |

---

## 代码仓库整洁度

| 状态 | 项目 | 备注 |
|------|------|------|
| ✅ | **核心代码无硬编码路径** | dreamer.py, models.py, networks.py, tools.py, configs.yaml 均无 `/root/` |
| ⚠️ | **scripts/ 硬编码路径** | 大量 shell/python 脚本含 `/root/autodl-tmp/...` 硬编码路径 (约 40+ 处)。若提交代码需清理 |
| ✅ | **无 pdb/breakpoint 调试代码** | 核心文件均无 |
| ⚠️ | **print() 语句** | dreamer.py:10, models.py:4, networks.py:4, tools.py:4 处 print()。多数可能是功能性输出，需审查 |
| ✅ | **.gitignore 存在** | 覆盖 logdir*, __pycache__/, *.py[cod], .env 等 |
| ⚠️ | **.gitignore 缺 *.pt/*.pth** | 未显式排除模型文件（logdir* 间接覆盖，但根目录 .pt 不受保护） |
| ⚠️ | **残留文件** | `models.py.bak_sgs_fix` (36KB) 应删除；根目录有多个分析脚本应移入 scripts/ |
| ✅ | **logdir 不可提交** | 7.7GB，已被 .gitignore 覆盖 |
| ⚠️ | **pickcube_ve_comparison.png** | 127KB PNG 在根目录，应移走或加入 gitignore |

---

## Reproducibility

| 状态 | 项目 | 备注 |
|------|------|------|
| ✅ | **Limitations section** | 已写好，7 段，覆盖环境/种子/阈值/算法限制 |
| ⚠️ | **requirements.txt** | 存在 (233B)，需确认是否完整 |
| ⚠️ | **实验配置** | configs.yaml 存在，但需确认是否包含所有实验配置 |
| ❌ | **README 运行说明** | 当前 README.md 未检查，可能需要更新复现步骤 |
| ❌ | **随机种子记录** | 需在论文/附录中列出所有实验的种子 |

---

## OpenReview 提交

| 状态 | 项目 | 备注 |
|------|------|------|
| ❌ | **OpenReview 账号** | 需确认已注册 |
| ❌ | **Abstract 提交** | Deadline May 25 已过！需确认是否已提交 |
| ❌ | **GenAI 使用声明** | 提交时需填写 |
| ❌ | **PDF 上传** | 无编译后 PDF |

---

## 紧急优先级排序

**⏰ 距 deadline 不到 24 小时 (May 28 EOD)**

### P0 — 必须完成 (无此则无法提交)
1. ❌ 确认 abstract 是否已在 May 25 提交（若未提交，可能已无法投稿）
2. ❌ 下载 CoRL 2026 LaTeX 模板
3. ❌ 创建主 paper.tex，整合全部 section
4. ❌ 写 Abstract
5. ❌ 编译 PDF 并确认 ≤8 页
6. ❌ 匿名化检查
7. ❌ OpenReview 提交

### P1 — 强烈建议
8. ⚠️ 润色 Introduction、Results、Discussion
9. ⚠️ 确认所有图表嵌入正确
10. ⚠️ paper_framing.md venue 从 ICML → CoRL

### P2 — 提交后可补
11. ⚠️ 清理代码 scripts/ 硬编码路径
12. ⚠️ 准备 supplementary zip
13. ⚠️ 匿名代码仓库
14. ⚠️ 更新 README 和 requirements.txt
