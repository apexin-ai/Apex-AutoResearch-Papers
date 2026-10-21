# Related Work Survey — Provenance Weight Training

## 1. Data Quality / Data Selection for LLM Pretraining

| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |
|---|------|------|------|-------------------|------------|
| 1 | **DSIR: Data Selection for Language Models via Importance Resampling** (Xie, Santurkar, Ma, Liang) | 2023 | NeurIPS | 用 hashed n-gram 特征估计 importance weight，对大规模语料做 importance resampling 来匹配目标分布 | DSIR 按目标分布做 selection，我们按 provenance 做 weighting——都用 lightweight feature 做数据筛选，但动机不同：DSIR 优化 domain match，我们降低 synthetic contamination |
| 2 | **QuRating: Selecting High-Quality Data for Training Language Models** (Wettig, Gupta, Malik, Chen) | 2024 | ICML | 用 LLM pairwise judgment 对数据做 4 维质量评分（writing style / expertise / facts / educational value），训练 QuRater 模型标注 260B 语料 | QuRating 用 LLM 判断 "质量"，我们用检测器判断 "来源"——都是 model-based annotation + downstream reweighting，但 quality 和 provenance 是正交维度 |
| 3 | **The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale** (Penedo et al., HuggingFace) | 2024 | arXiv | 用 Llama-3-70B 合成标注训练 educational quality classifier，过滤出 1.3T token 的 FineWeb-Edu，在 MMLU/ARC 上大幅领先 | FineWeb-Edu 用 LLM-based classifier 做 hard filtering（保留/丢弃），我们用 detector 做 soft weighting（降权不丢弃），保留更多数据多样性 |
| 4 | **D4: Improving LLM Pretraining via Document De-Duplication and Diversification** (Tirumala, Simig et al.) | 2023 | NeurIPS D&B | 用 pretrained embedding + K-Means 做去重和多样性平衡，6.7B 模型上提升 2% 下游准确率和 20% 训练效率 | D4 关注重复和多样性，我们关注 synthetic contamination——互补方法，可以先 D4 去重再用我们的 provenance weighting |
| 5 | **DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining** (Xie, Pham et al.) | 2023 | NeurIPS | 用 Group DRO 在 proxy model 上优化 domain mixture weights，无需下游任务信息，8B 模型提升 6.5% few-shot 准确率 | DoReMi 做 domain-level reweighting（按 domain 调权），我们做 instance-level reweighting（按 q-score 调权）——粒度不同，理论上可以组合使用 |
| 6 | **DataComp-LM (DCLM): In Search of the Next Generation of Training Sets for Language Models** (Li et al.) | 2024 | NeurIPS D&B | 提供 240T token 标准化语料 + 评估套件，系统性对比 data curation 策略，证明 model-based filtering 是关键 | DCLM 是 benchmark 框架，我们的 provenance-based weighting 可以作为一种新的 curation strategy 在 DCLM 上评估 |
| 7 | **Scaling Data-Constrained Language Models** (Muennighoff, Rush et al.) | 2023 | NeurIPS | 系统研究数据受限时的 scaling law，发现 ≤4 epochs 重复数据对 loss 影响可忽略，提出考虑重复衰减的 compute-optimal law | 当 unique data 不足时更可能混入 synthetic data 来补量——我们的方法提供了一种替代方案：不用丢弃 synthetic data，而是降权使用 |

## 2. Synthetic Data Contamination Detection

| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |
|---|------|------|------|-------------------|------------|
| 1 | **DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature** (Mitchell et al.) | 2023 | ICML | 零样本检测：用 log probability curvature（在 perturbation 前后的 log-prob 变化）区分 human vs machine text，无需训练分类器 | DetectGPT 做 binary detection（是否机器生成），我们需要 calibrated probability（q-score）——我们选择 TF-IDF + LogReg 正是因为需要 well-calibrated 的连续 score 而非仅 binary 判断 |
| 2 | **Fast-DetectGPT: Efficient Zero-Shot Detection via Conditional Probability Curvature** (Bao et al.) | 2024 | ICLR | 将 DetectGPT 的 perturbation 步骤替换为 sampling，加速 340 倍且 AUROC 提升约 75% | 同上——更高效但仍是 binary detection，calibration 质量（ECE）未被重点评估，而这正是我们工作的核心关注点 |
| 3 | **Binoculars: Zero-Shot Detection of LLM-Generated Text** (Hans et al.) | 2024 | ICML | 用两个 LLM 的 perplexity / cross-perplexity 比值做检测，ChatGPT 文本在 0.01% FPR 下召回 >90% | Binoculars 需要两个 LLM 推理，计算成本高；我们的 TF-IDF + LogReg 检测器极轻量，适合标注数十亿 token 级别的 pretraining corpus |
| 4 | **GLTR: Statistical Detection and Visualization of Generated Text** (Gehrmann, Strobelt, Rush) | 2019 | ACL | 用 LM 的 top-k token 排名做统计检测和可视化，帮助人类识别机器文本（人类检测率从 54% 提升到 72%） | 早期 statistical detection 工作，启发了后续基于 model statistics 的方法；我们的方法同样基于统计特征但目标不同（scoring for weighting 而非 human-in-the-loop detection） |
| 5 | **A Watermark for Large Language Models** (Kirchenbauer et al.) | 2023 | ICML | 在生成时嵌入 statistical watermark（green/red token list），可用 p-value 统计检验来检测 | Watermarking 需要控制生成过程，无法检测已有的、未 watermarked 的 synthetic data——我们的场景是 post-hoc detection on existing corpus |
| 6 | **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions** (Wu et al.) | 2024 | Computational Linguistics (MIT Press) | 系统综述 statistical / neural / watermarking 三类检测方法，讨论 robustness 和 generalization | 综述文献，帮助定位我们的检测器在整个 detection 方法谱系中的位置——我们是 training-based statistical classifier，但用于 weighting 而非 filtering |

## 3. Sample Reweighting in Training

| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |
|---|------|------|------|-------------------|------------|
| 1 | **Improving the Accuracy of Likelihood-based Inference under Covariate Shift** (Shimodaira) | 2000 | JASA | 奠基性工作：提出 importance weighted ERM（IWERM），通过 density ratio 修正 covariate shift 下的 loss | 理论基础直接相关——我们的 weight = 1 - q^b 可以看作一种 bounded importance weight，Shimodaira 的 IWERM 理论为我们的方法提供了正当性 |
| 2 | **Learning to Reweight Examples for Robust Deep Learning** (Ren, Zeng, Yang, Urtasun) | 2018 | ICML | 用 meta-learning 在训练中动态学习 sample weights（基于 gradient direction 在 clean validation set 上的表现） | L2RW 需要 clean validation set 做 meta-optimization，我们的方法不需要——weight 由 provenance detector 预先确定，无需在训练中迭代调整 |
| 3 | **Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting** (Shu et al.) | 2019 | NeurIPS | 用 MLP 学习 loss → weight 的显式映射函数，在 noisy label 和 class imbalance 场景下优于手工设计的 weighting | 与 L2RW 类似用 meta-learning；我们的 weight function 是 analytic form（1 - q^b），不需要 meta-learning，更透明可解释 |
| 4 | **Curriculum Learning** (Bengio, Louradour, Collobert, Weston) | 2009 | ICML | 奠基性工作：证明按从易到难的顺序训练（curriculum）可以加速收敛并改善 non-convex optimization 的局部极小值 | Curriculum learning 按难度排序，我们按 provenance 加权——虽然形式不同（排序 vs 加权），但都是 non-uniform training 的思想 |
| 5 | **Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining** (Wang et al.) | 2025 | ICLR | 在 LLM pretraining 中做 instance-level dynamic reweighting（基于 loss 值在线调整权重），提出 LinUpper / Quadratic 等策略 | 最直接的对比工作之一——他们基于 loss 做 weighting，我们基于 provenance 做 weighting。两者可组合：先用 provenance weight 再用 loss-based dynamic adjustment |
| 6 | **DoReMi** (Xie et al., 2023, 见第 1 节) | 2023 | NeurIPS | Domain-level reweighting via Group DRO | 我们做 instance-level provenance weighting，DoReMi 做 domain-level mixture optimization——粒度和信号来源不同 |

## 4. Theoretical Analysis of Data Mixing / Contamination

| # | 论文 | 年份 | 场所 | 一句话 Contribution | 与我们的关系 |
|---|------|------|------|-------------------|------------|
| 1 | **AI Models Collapse When Trained on Recursively Generated Data** (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal) | 2024 | Nature | 提出 model collapse 概念：在 synthetic data 上迭代训练导致分布尾部丢失和性能退化，在 VAE / GMM / LLM 上验证 | 我们工作的核心 motivation——Shumailov 证明了 synthetic contamination 的危害，我们提出用 provenance weighting 来缓解而非完全过滤 |
| 2 | **Strong Model Collapse** (Dohmatob, Feng, Subramonian, Kempe) | 2025 | ICLR | 证明即使极小比例的 synthetic data（1/1000）也会导致 model collapse；用 operator-valued free probability theory 给出 bias-variance 分解 | 强化了 motivation——即使少量 synthetic data 也有害，说明我们的 provenance weighting 方法的必要性：不能靠 "少量就没事" 来忽视 |
| 3 | **Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data** (Gerstgrasser, Schaeffer et al.) | 2024 | COLM | 证明如果 accumulate（而非 replace）数据，model collapse 可以避免；在 linear model 下证明 test error 有有限上界 | 与我们的方法互补——他们说 "保留 real data 可以救"，我们说 "对 synthetic data 降权也可以救"，都是 mitigate 而非 discard 的思路 |
| 4 | **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** (Seddik, Chen, Hayou, Youssef, Debbah) | 2024 | COLM | 给出 recursive training 的统计模型，证明纯 synthetic 训练不可避免 collapse，但 real + synthetic 混合训练在 synthetic 比例低于阈值时可避免 | 直接相关——他们给出了 synthetic data 比例的阈值分析，我们的 α_eff 理论可以看作这类阈值分析的推广（从 hard threshold 到 soft weighting） |
| 5 | **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance** (Ye, Liu, Sun, Zhan, Zhou, Qiu) | 2025 | ICLR | 发现 domain mixture proportion 和 model performance 之间存在可预测的函数关系（data mixing laws），可以用小规模实验预测大模型表现 | Data mixing laws 可用于预测不同 provenance weight 设置下的 model performance——我们的 Grid-b 搜索可以理论上用 mixing laws 来加速 |
| 6 | **Scaling Data-Constrained Language Models** (Muennighoff et al., 2023, 见第 1 节) | 2023 | NeurIPS | 数据受限下的 scaling law，重复 ≤4 epochs 影响可忽略 | 提供了数据受限场景的理论框架，我们的 α_eff 分析在此基础上进一步考虑了 contamination 的影响 |

## Key Observations

### 与现有工作的主要区别

1. **Data selection vs. data weighting**: 多数现有方法（DSIR, FineWeb-Edu, D4）做 hard selection（保留或丢弃），我们做 soft weighting（降权但不丢弃），保留了更多数据多样性和信息。
2. **Quality-based vs. provenance-based**: QuRating / FineWeb-Edu 基于 "质量" 评分，我们基于 "来源"（是否 synthetic）评分——这是正交的信号维度，可以组合使用。
3. **Detection for filtering vs. detection for weighting**: 现有 synthetic text detection 工作（DetectGPT, Binoculars）几乎全部用于 binary filtering 或人工审核，我们首次将 calibrated detection score 用于 continuous training weight，对检测器的 calibration（ECE）提出了新要求。
4. **Analytic weight function vs. learned weights**: 与 meta-learning reweighting（L2RW, Meta-Weight-Net）相比，我们的 weight = 1 - q^b 是 closed-form，无需 clean validation set 或 meta-optimization，更高效透明。

### 最直接的竞争对手 / 对比工作

- **Dynamic Loss-Based Sample Reweighting (Wang et al., ICLR 2025)**: 同为 instance-level reweighting for LLM pretraining，但信号来源不同（loss vs. provenance）。
- **DoReMi (Xie et al., NeurIPS 2023)**: Domain-level reweighting，粒度不同但目标相似。
- **FineWeb-Edu filtering**: 最接近的 "data quality" 竞品，但是 hard filtering 不是 soft weighting。

### 潜在的引用遗漏风险

- **Ghostbuster** (Verma et al., 2024): 另一个 feature-based synthetic text detector，可能需要作为 detection baseline 引用 [需确认场所]
- **GPTZero**: 商业工具，学术论文 (2025 arXiv) 可作为检测方法的 context 引用 [需确认]
- **Self-play fine-tuning / synthetic data augmentation 文献**: 我们的工作假设 synthetic data 有害，但有大量文献证明 synthetic data 在 fine-tuning 中有益——需要在 related work 中 acknowledge 并区分 pretraining contamination vs. fine-tuning augmentation 的不同场景
- **Distributionally robust optimization (DRO) 基础文献**: Sagawa et al. (2020) Group DRO 等，作为 DoReMi 的理论基础可能需要提及
- **Data influence / data attribution 文献**: TracIn, influence functions 等，虽然不是直接竞品但在 "understanding data's effect on training" 的大框架下相关
