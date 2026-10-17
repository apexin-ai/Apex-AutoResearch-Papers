# R3 Text Fixes Log — 2026-05-15

## 修改清单
| Issue ID | 文件 | 修改摘要 | 状态 |
|----------|------|---------|------|
| R3-N1 | method.tex L89-93 | Eq.1 已有 ∀ 量词（此前已修改）；无需改动 | already done |
| R3-N1 | conclusion.tex L26 | Limitations EDD 段落加 cross-strategy AUC 反例（GPT-2 XL 0.129, OLMo 0.253） | done |
| R3-N4 | abstract.tex L5 | 'universal depth markers' → 加 'within the studied 3×3 model--strategy grid' | done |
| R3-N4 | introduction.tex L14 | 'universal stability across model families and decoding strategies' → 'across the three model families and three decoding strategies studied' | done |
| R3-N5/W3 | discussion.tex L4-8 | 重写部署段落：加 d1/d2 反转数字，降低期望，strategy identification 作为前提 | done |
| R3-N5/W3 | discussion.tex | 'geometry-level shift' 全文未找到，无需修改 | N/A |
| R3-N5/W3 | discussion.tex L7 | 加入 'a residual gap that simple feature normalization cannot resolve; whether more sophisticated domain adaptation methods could recover the boundary remains open' | done |
| R3-W1 | abstract.tex L5 | 70-85% 后并列 d0-excluded 3-class accuracy placeholder (XX.X--XX.X%) | done |
| R3-W1 | atlas.tex Table 2 caption | 加 d0 recall >98% 说明 + d1-d3 3-class accuracy placeholder | done |
| R3-W1 | generalization.tex (cross-model) | 文中加 d1-d3 balanced accuracy: Pythia 49.9%, OLMo 59.2%, GPT-2 XL 57.3%, 均值 55.5% | done |
| R3-W1 | generalization.tex Table 5 caption | 加 d0 inflation 说明 + d1-d3 均值 55.5% | done |
| R3-W1 | generalization.tex (cross-strategy) | 文中加 d1-d3 accuracy placeholder (XX.X%) | done |
| R3-W1 | generalization.tex Table 6 caption | 加 d0 recall ≥89.5% inflation 说明 | done |
| R3-W2/W6 | discussion.tex | 从 ~80 词 1 段扩展至 ~350 词 5 段：(a) 部署约束+策略识别 (b) 混合深度语料库 (c) 对抗鲁棒性 (d) 数据溯源 (e) 规模扩展 | done |
| R3-W4 | 全部 .tex | 无 experiment ID，无内部路径泄露 | clean |
| R3-M1.1 | method.tex | §3 标题 "Task Formulation"，非 "Methodology"/"Experimental Setup"，不改 | N/A |
| R3-M1.2 | references.bib | holtzman2020=ICLR 2020（正确），basu2021=ICLR 2021（正确），均为会议年份，不改 | kept |
| R3-M1.3 | abstract.tex L5 | ρ=0.868 → 'high cross-cell consistency with Spearman ρ > 0.85' | done |
| R3-M1.4 | conclusion.tex (末尾) | 添加 \section*{Ethics Statement}，3 句 | done |
| R3-M1.5 | method.tex L35 | 已是 'commonly used LoRA hyperparameters'，无需修改 | already done |
| R3-M1.6 | related_work.tex L19-20 | 加入 Ghostbuster、M4-SemEval、DNA-GPT 3 篇引用 | done |
| R3-M1.6 | references.bib | 加入 verma2024_ghostbuster, wang2024_m4_semeval, yang2024_dnagpt 三条 bib entry | done |

## 需要后续处理
- **d0-excluded 3-class accuracy 数字 (abstract, atlas Table 2, cross-strategy)**：论文中无法直接推导，需要从实验数据（confusion matrix）计算。当前留 XX.X% placeholder
- **3 篇新引用的 bib 信息需验证**：Ghostbuster (Verma et al., 2024)、M4-SemEval (Wang et al., 2024)、DNA-GPT (Yang et al., 2024) 的作者、年份、venue 需确认。bib entry 中已标注 "Citation needs verification"
- **holtzman2020 / basu2021 年份**：审稿人建议改为 arXiv 年份 (2019/2020)，但当前 bib 使用会议年份 (ICLR 2020/2021)，属标准做法。保持不动，如审稿人坚持可在 camera-ready 调整
- **§5.4 attention-importance 分析**：遵照硬约束未触碰，等 SHAP 数据
- **contribution 表述**：遵照硬约束未触碰，等 ablation 结果

## 硬约束遵守确认
- [x] 未修改 Wikipedia subset 种子数据描述
- [x] EDD 叙事保持分级：Pythia 显著 (p=0.001)，OLMo 边际 (p=0.091)，GPT-2 XL 不显著 (p=0.505)
- [x] 未动 §5.4 attention-importance 分析
- [x] 未调整 contribution 表述
- [x] 未编造数字（cross-model d1-d3 55.5% 从表中 recall 推导，其余留 placeholder）
- [x] 未删除已有正确内容
