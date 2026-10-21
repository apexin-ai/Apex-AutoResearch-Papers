# 论文图表方案

> 项目：gen-depth-contamination
> 目标投稿：EMNLP ARR May 25, 2026
> 最后更新：2026-05-12

---

## Fig 1: Method Overview / Pipeline 图

**类型**：示意图 / flow diagram

**数据来源**：无数据依赖，纯概念图

**核心信息**：一图看懂整个方法——从人类文本出发，经过递归 LLM 生成形成不同 depth 的文本，提取统计特征后送入 ordinal depth classifier，最终输出 depth 估计用于 graduated filtering。读者看完应理解 (1) depth chain 的构造方式 (2) 特征提取到分类的 pipeline (3) graduated filtering 的思路。

**设计要点**：

- **布局**：左到右水平流程，分三个区域——Corpus Construction / Feature Extraction / Depth-Aware Curation
- **Corpus Construction 区域**：
  - 左起一个 Human Text 方块（X₀），颜色最深（深蓝 #1a5276）
  - 依次经过 LLM 信道符号（▷）连接到 X₁, X₂, ..., X₅
  - 每个 Xₖ 用渐变色编码 depth：depth 0 深蓝 → depth 5 浅蓝/白色，隐喻信息衰减
  - X₀ 到 X₅ 之间画一条从粗到细的灰色箭头，底部标注 "I(X₀; Xₖ) ↓ (DPI)"
- **Feature Extraction 区域**：
  - 三组特征用图标 + 颜色区分：Surprisal (蓝 #2980b9) / Diversity (绿 #27ae60) / Tail-thinning (橙 #e67e22)
  - 简洁的 15-dim feature vector 示意
- **Depth-Aware Curation 区域**：
  - Ordinal Classifier 输出 depth 估计 k̂
  - 底部分支：graduated weight = quality(k̂)/quality(0) → 加权训练数据
  - 与 binary filtering（remove all synthetic）对比的小示意
- **底部信息条**：DPI 理论支撑——"Data Processing Inequality: information about X₀ can only decrease with depth"
- **字体**：标题用 sans-serif bold，标注用 9pt，数学符号用 LaTeX 渲染
- **配色**：以蓝色系为主色调，三组特征颜色贯穿后续所有图表

**制作工具**：TikZ（LaTeX 原生，与论文排版一致，方便调整尺寸）。如时间不够，matplotlib + 手动布局。

---

## Fig 2: Pairwise AUC 随 depth 衰减曲线（核心结果图）

**类型**：折线图

**数据来源**：
- P0-9 (全配置特征提取) + P0-10 (LightGBM 5-fold CV)
- 文件：`artifacts/analysis/pairwise_auc_matrix.csv`
- 每个 (model, decoding_strategy) 配置的 pairwise AUC 值

**核心信息**：depth signal 存在且随深度单调衰减，K* 可精确测量。不同模型/解码策略的衰减速度不同但趋势一致。读者看完应得出：(1) depth 0v1 区分度最高 (2) 衰减是单调的 (3) K* 位置清晰可读。

**设计要点**：

- **X 轴**：depth pair (0v1, 1v2, 2v3, 3v4, 4v5)，等间距
- **Y 轴**：AUC，范围 [0.45, 1.0]，0.5 处标注 "random baseline"
- **线条**：
  - 主实验线（Qwen2.5-1.5B × 5 种解码策略）：实线，不同明度的蓝色系
    - D-greedy: 深蓝实线 ●
    - D-p90: 蓝色实线 ■
    - D-p95: 中蓝实线 ▲（MVP 配置，加粗）
    - D-lowT: 浅蓝实线 ◆
    - D-highT: 天蓝实线 ★
  - 跨模型线：虚线
    - Pythia-1.4B (D-p95): 红色虚线 ●
    - OLMo-1B (D-p95): 绿色虚线 ■
    - Qwen2.5-7B (D-p95): 紫色虚线 ▲
- **水平参考线**：AUC=0.60 灰色虚线，右侧标注 "K* threshold"
- **K* 标注**：每条曲线与 0.60 线交叉处用竖向箭头标注 K* 值（如 K*=3）
- **误差带**：5-fold CV 的 ±1 std 用半透明色带
- **图例**：右侧或图下方，按模型分组

**制作工具**：matplotlib (seaborn style)。代码模板在 `draw-paper-figure` skill 中。

---

## Fig 3: JSD 衰减曲线 + 理论预测叠加

**类型**：折线图（双 panel 或叠加）

**数据来源**：
- P0-9 特征提取中的 JSD 计算：`artifacts/analysis/jsd_decay.csv`
- 每个配置下 JSD(P_{X_0}, P_{X_k}) 对 k 的值
- 理论预测：Proposition 2 的 ρ^k · d(P_{X_0}, P*) 指数衰减 bound

**核心信息**：实验观测的 JSD 衰减与信道级联理论（DPI bound）定性一致。指数衰减拟合 vs 多项式衰减拟合的 AIC/BIC 对比验证 Proposition 3 的经验假设。读者看完应得出：(1) MI 确实单调衰减 (2) 衰减速率与解码策略相关 (3) 理论框架有实验支撑。

**设计要点**：

- **Panel A — JSD 衰减观测**：
  - X 轴：depth k (0, 1, 2, 3, 4, 5)
  - Y 轴：JSD(P_{X_0}, P_{X_k})，对数刻度可选
  - 多条实线：不同 decoding strategies（复用 Fig 2 配色）
  - 叠加虚线：指数拟合 ρ̂^k · C（用 least squares fit）
  - 标注拟合的 ρ̂ 值和 R² 或 AIC
- **Panel B — 衰减模型对比**：
  - 分组柱状图或表格嵌入
  - X 轴：decoding strategy
  - Y 轴：AIC（越低越好）
  - 两组柱：exponential fit / polynomial fit
  - 颜色：exponential 蓝色 / polynomial 橙色
  - 核心观察：greedy 更符合指数衰减，high-T 可能更接近多项式
- **辅助元素**：
  - Panel A 中用灰色水平带标注 "noise floor"（JSD 值低于此不可靠）
  - 箭头标注 convergence to P*
- **配色**：与 Fig 2 一致

**制作工具**：matplotlib，subplot(1,2) 布局

---

## Fig 4: Feature Importance Ranking

**类型**：水平柱状图

**数据来源**：
- P0-10 LightGBM classifier 的 feature importance (gain-based)
- 文件：`artifacts/analysis/feature_importance.csv`
- 15 维特征的 importance 排序

**核心信息**：哪类特征最 depth-discriminative。读者看完应得出：(1) 三组特征的相对重要性排序 (2) 单个最重要特征是什么 (3) 不同特征组的贡献是互补的还是冗余的。

**设计要点**：

- **布局**：水平柱状图，特征名在 Y 轴，importance 在 X 轴
- **排序**：按 importance 降序（最重要的在最上方）
- **颜色编码（贯穿全文）**：
  - Surprisal 组 (9 维): 蓝色系 #2980b9
  - Diversity 组 (3 维): 绿色系 #27ae60
  - Tail-thinning 组 (3 维): 橙色系 #e67e22
- **特征名标注**：
  - 简写 + 全称 tooltip（如 "surp_mean" / "mean token surprisal"）
  - 同组特征用括号分组标注
- **分组分隔线**：在不同颜色组之间用细灰线分隔（如果特征交错排列则不需要）
- **误差条**：5-fold CV 的 importance std
- **右侧标注**：每组特征的累计 importance 百分比
- **图例**：右上角，三色块 + 组名

**制作工具**：matplotlib (barh)

---

## Fig 5: Graduated vs Binary Filtering 下游对比

**类型**：分组柱状图

**数据来源**：
- P0-12 下游过滤评估结果
- 文件：`artifacts/downstream/filtering_comparison.csv`
- 4 种过滤策略 × 下游 benchmark 分数

**核心信息**：graduated filtering 优于 binary filtering 和 no filtering。读者看完应得出：(1) 过滤好于不过滤 (2) graduated > binary (3) 差异具有统计显著性。

**设计要点**：

- **X 轴**：filtering 策略，4 组
  - No filter (灰色)
  - Binary (DivEye) (红色)
  - Graduated (本文方法) (蓝色，加粗边框突出)
  - Surplexity (紫色)
- **Y 轴**：Accuracy (%)
- **Panel 布局**：subplot(1,2) 或 subplot(1,3)
  - Panel A: MMLU (5-shot)
  - Panel B: HellaSwag (10-shot)
  - Panel C: XSum ROUGE-L（如果 P1-7 完成）
- **误差条**：bootstrap 95% CI
- **显著性标注**：
  - graduated vs binary: 横线 + * 或 ** 标注 p-value
  - graduated vs no-filter: 同上
- **数值标注**：每个柱顶标注精确值（如 "43.2"）
- **baseline 参考线**：no-filter 的值用灰色水平虚线贯穿
- **如果有多个污染比例**（P1-2 完成时）：
  - 改为 subplot(2,2) 或 subplot(1,3)，每个 panel 一个污染比例
  - 或改为折线图：X 轴=污染比例 (10%/30%/50%), 多条线=不同策略

**制作工具**：matplotlib (bar + errorbar)

---

## Fig 6: Feature Group × Depth 判别力热力图（降解序分析）

**类型**：热力图

**数据来源**：
- P0-11 K* + 饱和边界分析
- 文件：`artifacts/analysis/feature_group_saturation.csv`
- 每个 feature group 在每个 depth pair 上的 AUC

**核心信息**：揭示 "linguistic degradation ordering"——不同语言维度在哪个 depth 率先丧失判别力。读者看完应得出：(1) 哪组特征最先饱和 (2) 哪组特征最晚饱和（最 robust）(3) 饱和顺序是否跨模型一致。

**设计要点**：

- **行**：Feature group（Surprisal / Diversity / Tail-thinning），每组可进一步拆分单特征
- **列**：Depth pair (0v1, 1v2, 2v3, 3v4, 4v5)
- **色标**：连续色标 viridis 或 RdYlGn
  - AUC > 0.70: 深绿
  - AUC 0.60-0.70: 黄色
  - AUC < 0.60: 红色（已饱和）
- **cell 标注**：每个 cell 内写 AUC 数值（2 位小数）
- **K* 标注线**：在每行特征组的 K* 位置画竖线或加粗边框
- **面板**：如果做跨模型对比（P0-2, P0-3 数据），可做 subplot(1,3)，每个 panel 一个模型
- **行内排序**：按每组的 K*（或平均 AUC）降序，最 robust 的组在最上方

**制作工具**：matplotlib (imshow/pcolormesh) 或 seaborn (heatmap)

---

## Table 1: 完整 Pairwise AUC 矩阵

**类型**：表格

**数据来源**：
- P0-10 所有配置的 pairwise AUC
- 文件：`artifacts/analysis/pairwise_auc_matrix.csv`

**核心信息**：跨模型 × 跨解码策略的 K* 一致性或差异。读者看完应得出：(1) 每个配置的 K* 是多少 (2) K* 在哪些条件下变化 (3) 整体结论的可靠性。

**设计要点**：

- **行**：depth pair (0v1, 1v2, 2v3, 3v4, 4v5)
- **列**：按配置分组
  - Group 1 - Qwen2.5-1.5B 解码消融：Greedy / p=0.9 / p=0.95 / T=0.7 / T=1.2
  - Group 2 - 跨模型 (D-p95)：Qwen-1.5B / Pythia-1.4B / OLMo-1B / Qwen-7B
- **每个 cell**：AUC ± std（5-fold CV）
- **粗体**：AUC > 0.60 的 cell（K* 以内）
- **底行**：K* 值汇总
- **灰色底纹**：AUC < 0.55 的 cell（完全不可分）
- **列头**：简写 + 脚注对应完整配置
- **表格宽度**：如列太多，拆为 Table 1a (解码消融) 和 Table 1b (跨模型)
- **格式**：LaTeX booktabs 风格（三线表）

**制作工具**：LaTeX tabular (booktabs)，数据由 Python 脚本生成 .tex 片段

---

## Fig 7: t-SNE / UMAP 特征空间可视化（篇幅允许时）

**类型**：散点图

**数据来源**：
- P0-9 的 15 维特征矩阵
- 文件：`artifacts/analysis/features_all.csv`
- 随机采样每个 depth 500 个样本

**核心信息**：特征空间中不同 depth 的文本形成可分辨的 cluster，且随 depth 增加 cluster 逐渐重叠。直观展示 depth signal 的强度和饱和。

**设计要点**：

- **降维方法**：UMAP（保持全局结构优于 t-SNE）
- **颜色编码**：depth 0-5 使用渐变色标（深蓝→浅蓝→白色，与 Fig 1 一致）
- **点大小**：小（alpha=0.3-0.5），避免遮挡
- **标注**：每个 cluster 中心标注 depth 编号
- **Panel 对比**（可选）：
  - Panel A: 全部 depth 0-5
  - Panel B: 仅 depth 0, 1, 2（清晰可分的部分）
  - Panel C: 仅 depth 3, 4, 5（重叠的部分）
- **轮廓线**：每个 depth 的 KDE 等高线（50% density contour）
- **辅助信息**：标注 cluster 间距与 AUC 的对应关系

**制作工具**：matplotlib (scatter) + umap-learn

---

## Fig 8: Surprisal 分布随 depth 偏移（篇幅允许时）

**类型**：Ridge plot（岭线图）或 violin plot

**数据来源**：
- P0-9 特征提取中的 per-document mean surprisal 分布
- 文件：`artifacts/features/surprisal_by_depth.csv`

**核心信息**：递归生成文本的 surprisal 分布逐代向低 surprisal 偏移，尾部逐渐消失。直观展示 Shumailov et al. 描述的 tail disappearance 现象。

**设计要点**：

- **布局**：Ridge plot（垂直堆叠，从上到下 depth 0→5）
- **X 轴**：mean token surprisal（或 mean log-prob 取负）
- **Y 轴**：密度（每个 depth 一条分布曲线）
- **颜色**：与全文 depth 色标一致（深蓝→浅蓝）
- **标注**：
  - 每个分布的 mean 和 std
  - 用箭头标注 tail 消失方向
  - 标注 depth 0 的 heavy tail 区域
- **Panel B（可选）**：叠加 vocabulary entropy 或 type-token ratio 的类似 ridge plot，展示 diversity 维度的同步变化
- **参考线**：depth 0 的 mean 值用竖虚线贯穿所有分布

**制作工具**：matplotlib (joypy 库) 或 seaborn (kdeplot + offset)

---

## Fig 9: Confusion Matrix — Ordinal Classifier（篇幅允许时）

**类型**：热力图（6×6 混淆矩阵）

**数据来源**：
- P0-10 ordinal classifier 的 test set predictions
- 文件：`artifacts/analysis/confusion_matrix.csv`

**核心信息**：分类器的误差集中在相邻 depth（ordinal 特性），远距离混淆极少。K* 以外的 depth 互相混淆严重。

**设计要点**：

- **行**：True depth (0-5)
- **列**：Predicted depth (0-5)
- **色标**：单色渐变（白→深蓝），数值越大越深
- **对角线高亮**：正确分类 cell 加粗边框
- **标注**：每个 cell 写百分比值
- **右侧/底部**：per-class precision/recall
- **观察重点**：off-diagonal 的误差是否集中在 ±1 位置（ordinal 结构的证据）
- **K* 分隔线**：在 K* 位置画粗线，标注 "discrimination boundary"

**制作工具**：matplotlib (imshow) 或 seaborn (heatmap)

---

## Table 2: 消融实验汇总（篇幅允许时）

**类型**：表格

**数据来源**：
- P0-10 (分类器对比) + P1-3 (ordinal vs multinomial vs regression)
- 文件：`artifacts/analysis/ablation_results.csv`

**核心信息**：(1) ordinal regression 优于 multinomial classification，证明 depth 有序结构有用 (2) 手工特征 vs. learned representation 的对比 (3) 特征组消融

**设计要点**：

- **行**：不同配置
  - Classifier: LightGBM / CORAL / CORN / MLP / LM-embed+MLP
  - Feature set: All 15 / Surprisal only / Diversity only / Tail only / Surprisal+Diversity / ...
  - Classification paradigm: Ordinal / Multinomial / Regression (MAE)
- **列**：
  - Exact accuracy
  - ±1 accuracy（ordinal 评价指标）
  - MAE
  - K* AUC (平均 K* 以内的 pairwise AUC)
- **最佳值粗体**
- **格式**：booktabs 三线表

**制作工具**：LaTeX tabular

---

## Fig 10: Cross-Model / Cross-Scale Transfer（篇幅允许时）

**类型**：热力图或分组柱状图

**数据来源**：
- P0-10 的 cross-model evaluation
- 文件：`artifacts/analysis/cross_model_transfer.csv`
- 训练在 model A，测试在 model B 的 accuracy

**核心信息**：depth classifier 具有跨模型泛化能力（或展示其局限性）。

**设计要点**：

- **热力图方案**：
  - 行：训练模型 (Qwen-1.5B / Pythia / OLMo)
  - 列：测试模型 (Qwen-1.5B / Pythia / OLMo / Qwen-7B)
  - Cell：AUC 或 accuracy
  - 对角线（same-model）应最高
- **辅助柱状图**：Qwen-1.5B 训练 → Qwen-7B 测试 的 per-depth-pair AUC，展示 scale transfer

**制作工具**：matplotlib (imshow + bar)

---

## 全局设计规范

### 配色方案

| 元素 | 颜色 | Hex |
|------|------|-----|
| Depth 色标 | 深蓝 → 浅蓝 → 白色 | #1a5276 → #5dade2 → #ebf5fb |
| Surprisal 特征组 | 蓝色系 | #2980b9 |
| Diversity 特征组 | 绿色系 | #27ae60 |
| Tail-thinning 特征组 | 橙色系 | #e67e22 |
| K* threshold 线 | 灰色虚线 | #7f8c8d |
| Graduated filtering | 蓝色（本文方法高亮） | #2c3e50 |
| Binary filtering | 红色 | #c0392b |
| No filter | 灰色 | #95a5a6 |
| Surplexity | 紫色 | #8e44ad |

### 字体和排版

- 图标题：10pt bold sans-serif
- 轴标签：9pt sans-serif
- 刻度标签：8pt
- 图例：8pt
- 所有数学符号用 LaTeX 渲染（matplotlib 的 `usetex=True` 或 `mathtext`）
- 图片格式：PDF（矢量图，适配 LaTeX）+ PNG（300 dpi，用于 review）

### 尺寸

- 单栏图：宽 3.25 in
- 双栏图：宽 6.875 in
- 高度根据内容调整，通常 2-4 in
- 遵循 ACL/EMNLP 模板的图表尺寸限制

### 制作顺序（按依赖排序）

| 优先级 | 图表 | 依赖实验 | 何时可开始 |
|--------|------|----------|-----------|
| P0 | Fig 1 (Pipeline) | 无 | 立即 |
| P0 | Fig 2 (AUC 衰减) | P0-10 | Day 5-6 |
| P0 | Table 1 (AUC 矩阵) | P0-10 | Day 5-6 |
| P0 | Fig 4 (Feature Importance) | P0-10 | Day 5-6 |
| P0 | Fig 5 (Filtering 对比) | P0-12 | Day 6-8 |
| P0 | Fig 6 (降解序热力图) | P0-11 | Day 5-6 |
| P1 | Fig 3 (JSD + 理论) | P0-9 | Day 5-6 |
| P1 | Table 2 (消融) | P0-10 + P1-3 | Day 8-9 |
| P2 | Fig 7 (UMAP) | P0-9 | Day 5-6 |
| P2 | Fig 8 (Surprisal ridge) | P0-9 | Day 5-6 |
| P2 | Fig 9 (Confusion matrix) | P0-10 | Day 5-6 |
| P2 | Fig 10 (Cross-model) | P0-10 | Day 5-6 |

### 路线适配

- **路线 A (K*≥3)**：所有图表按上述方案执行，Fig 2 展示丰富的衰减曲线，Fig 5 展示 graduated filtering 的显著优势
- **路线 B (K*=2)**：Fig 2 的 K* 标注在 depth 2 处，但配合 Fig 6 的降解序热力图讲故事——saturation boundary 本身是贡献；Fig 5 改为 3-class (human/gen-1/gen-2+) vs binary 对比；Fig 3 的理论拟合用 K*=2 参数化
