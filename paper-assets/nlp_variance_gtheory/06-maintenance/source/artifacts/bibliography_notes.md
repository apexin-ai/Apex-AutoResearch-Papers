# Bibliography Notes

## 1. Bouthillier et al. (2021)
**Citation**: Bouthillier, X., Delaunay, P., Bronzi, M., Trofimov, A., Nichyporuk, B., Szeto, J., Mohammadi Sepahvand, N., Raff, E., Madan, K., Voleti, V., Ebrahimi Kahou, S., Michalski, V., Arbel, T., Pal, C., Varoquaux, G., & Vincent, P. (2021). Accounting for Variance in Machine Learning Benchmarks. *Proceedings of Machine Learning and Systems (MLSys)*, 3.
**关联**: 提出 ML benchmark 中方差的系统性量化框架，展示了随机种子、数据划分等因素对评估结果的显著影响，是将统计方法引入 ML 评估可靠性的先驱工作，与我们用 G-theory 分解评估方差的核心目标直接对应。

## 2. Polo et al. (2024)
**Citation**: Maia Polo, F., Weber, L., Choshen, L., Sun, Y., Xu, G., & Yurochkin, M. (2024). tinyBenchmarks: Evaluating LLMs with Fewer Examples. *Proceedings of the 41st International Conference on Machine Learning (ICML)*, PMLR 235.
**关联**: 用 IRT 建模 benchmark item 的区分力来选择代表性子集，实现高效评估。其 item-level 分析思路与我们用 G-theory 分解 item（题目）方差源的方法论互补——tinyBenchmarks 关注 item 选择效率，我们关注方差归因。

## 3. Perlitz et al. (2024)
**Citation**: Perlitz, Y., Bandel, E., Gera, A., Arviv, O., Ein-Dor, L., Shnarch, E., Slonim, N., Shmueli-Scheuer, M., & Choshen, L. (2024). Efficient Benchmarking (of Language Models). *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)*, pages 2519–2536.
**关联**: 系统研究了 benchmark 设计选择（任务数量、样本数量、指标选择）对评估可靠性的影响，以 HELM 为测试案例量化了计算成本-可靠性的权衡。为我们的 G-theory 框架提供了"哪些设计因素值得纳入方差分解"的实证依据。

## 4. Henderson et al. (2018)
**Citation**: Henderson, P., Islam, R., Bachman, P., Pineau, J., Precup, D., & Meger, D. (2018). Deep Reinforcement Learning That Matters. *Proceedings of the 32nd AAAI Conference on Artificial Intelligence (AAAI)*, pages 3207–3214.
**关联**: 深度 RL 领域的可复现性经典研究，揭示了超参数、随机种子、代码实现等因素导致的高方差问题。虽然领域不同，但其方差量化方法论和"评估结果不可靠"的核心发现，为我们在 NLP 评估中引入 G-theory 提供了跨领域动机。

## 5. Lalor et al. (2019)
**Citation**: Lalor, J. P., Wu, H., & Yu, H. (2019). Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds. *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)*, pages 4962–4973.
**关联**: 首次将 IRT 应用于 NLP 评估，用 DNN 生成的 artificial crowds 替代人类作答数据来估计 item 参数。为我们在 LLM 评估中使用心理测量学方法（G-theory 也源于心理测量学）提供了直接先例和方法论基础。

## 6. Rodriguez et al. (2021)
**Citation**: Rodriguez, P., Barrow, J., Hoyle, A., Lalor, J. P., Jia, R., & Boyd-Graber, J. (2021). Evaluation Examples Are Not Equally Informative: How Should That Change NLP Leaderboards? *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)*, pages 4486–4503.
**关联**: 用贝叶斯 IRT 模型分析 NLP leaderboard 的排名可靠性，发现不同 item 的信息量差异巨大。其"item 层面的评估质量分析"与我们 G-theory 中将 item 作为方差 facet 的设计理念高度一致。

## 7. Vania et al. (2021)
**Citation**: Vania, C., Htut, P. M., Huang, W., Mungra, D., Pang, R. Y., Phang, J., Liu, H., Cho, K., & Bowman, S. R. (2021). Comparing Test Sets with Item Response Theory. *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)*, pages 1141–1158.
**关联**: 用 IRT 分析 29 个 NLP 数据集的 item 属性（难度、区分度），发现部分 benchmark 对当前模型已经饱和。提供了 item 层面的定量分析方法，与我们的 G-theory 方差分解在 item facet 维度互补。

## 8. Lu et al. (2022)
**Citation**: Lu, Y., Bartolo, M., Moore, A., Riedel, S., & Stenetorp, P. (2022). Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity. *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)*, pages 8086–8098.
**关联**: 实证表明 few-shot prompt 中示例的排列顺序可导致性能从 SOTA 级别降至随机猜测水平。这种 prompt ordering 效应是我们 G-theory 框架中 infrastructure facet（评估执行方式带来的方差）的关键组成部分。

## 9. Pezeshkpour & Hruschka (2024)
**Citation**: Pezeshkpour, P. & Hruschka, E. (2024). Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions. *Findings of the Association for Computational Linguistics: NAACL 2024*, pages 2006–2017.
**关联**: 量化了 LLM 在多选题中对选项顺序的敏感性（性能差异 13%–75%），直接证明了评估基础设施层面的方差来源。这是我们 G-theory 方差分解中 item presentation format 这一 facet 的核心实证支撑。

## 10. Dodge et al. (2020)
**Citation**: Dodge, J., Ilharco, G., Schwartz, R., Farhadi, A., Hajishirzi, H., & Smith, N. A. (2020). Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping. *arXiv preprint arXiv:2002.06305*.
**关联**: 系统量化了微调过程中随机种子（权重初始化和数据顺序）对性能的影响，发现 BERT 在 GLUE 任务上的表现因种子不同差异显著。直接为我们 G-theory 框架中"模型训练方差"这一 facet 提供了实证依据。

## 11. Sellam et al. (2022)
**Citation**: Sellam, T., Yadlowsky, S., Tenney, I., Wei, J., Saphra, N., D'Amour, A., Linzen, T., Bastings, J., Turc, I., Eisenstein, J., Das, D., & Pavlick, E. (2022). The MultiBERTs: BERT Reproductions for Robustness Analysis. *Proceedings of the 10th International Conference on Learning Representations (ICLR)*.
**关联**: 训练了 25 个独立 BERT 模型来量化预训练随机性对下游任务的影响，提供了严格的多次复现分析框架。MultiBERTs 的方法论（多次独立训练 + 统计分析）与 G-theory 的 D-study（决策研究，估计需要多少复现才能达到可靠评估）思想天然契合。

## 12. Dehghani et al. (2021)
**Citation**: Dehghani, M., Tay, Y., Gritsenko, A. A., Zhao, Z., Houlsby, N., Diaz, F., Metzler, D., & Vinyals, O. (2021). The Benchmark Lottery. *arXiv preprint arXiv:2107.07002*.
**关联**: 提出"benchmark lottery"概念，证明算法的相对优劣可能仅因选择不同 benchmark 任务而逆转。这种 benchmark 选择带来的系统性方差正是我们 G-theory 框架中 methodology facet（任务/benchmark 选择作为方差源）要量化的核心问题。

## 13. Biderman et al. (2024)
**Citation**: Biderman, S., Schoelkopf, H., Sutawika, L., Gao, L., Tow, J., Abbasi, B., Aji, A. F., Ammanamanchi, P. S., Black, S., Clive, J., DiPofi, A., Etxaniz, J., Fattori, B., Forde, J. Z., Foster, C., Hsu, J., Jaiswal, M., Lee, W. Y., Li, H., Lovering, C., Muennighoff, N., Pavlick, E., Phang, J., Skowron, A., Tan, S., Tang, X., Wang, K. A., Winata, G. I., Yvon, F., & Zou, A. (2024). Lessons from the Trenches on Reproducible Evaluation of Language Models. *arXiv preprint arXiv:2405.14782*.
**关联**: 基于 lm-evaluation-harness 的大规模实践，系统总结了 LLM 评估中影响可复现性的实际因素（prompt 格式、tokenization、采样策略等）。为我们 G-theory 框架中 infrastructure facet 的具体操作化提供了丰富的第一手经验。

## 14. Shavelson & Webb (1991)
**Citation**: Shavelson, R. J. & Webb, N. M. (1991). *Generalizability Theory: A Primer*. Sage Publications. ISBN: 978-0-8039-3745-1.
**关联**: G-theory 的入门教材，系统介绍了 G-study/D-study 框架、方差分量估计和概化系数计算。是我们将 G-theory 从教育测量领域迁移到 LLM 评估的核心理论基础。

## 15. Brennan (2001)
**Citation**: Brennan, R. L. (2001). *Generalizability Theory* (2nd ed.). Springer. ISBN: 978-0-387-95282-6.
**关联**: G-theory 的权威教科书，涵盖了多 facet 交叉设计、随机/固定 facet 处理、方差分量的负估计等高级主题。为我们设计复杂的 LLM 评估 G-study（多 facet：模型 × benchmark × prompt × 种子）提供了完整的统计理论基础。
