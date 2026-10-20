# Related Work References — div_cal_verify

> 36 篇经过 WebSearch 验证的引用，覆盖 8 个子领域

## 1. Concept Drift / Embedding Drift

1. **Lu et al. (2019)** "Learning under Concept Drift: A Review" — *IEEE Transactions on Knowledge and Data Engineering*, Vol. 31, No. 12, pp. 2346–2363
   - 作者: Jie Lu, Anjin Liu, Fan Dong, Feng Gu, João Gama, Guangquan Zhang
   - 关联: 建立了 drift 检测与适应的分类体系，为理解自训练中嵌入空间几何漂移提供了概念框架

2. **Gama et al. (2014)** "A Survey on Concept Drift Adaptation" — *ACM Computing Surveys*, Vol. 46, No. 4, Article 44
   - 作者: João Gama, Indrė Žliobaitė, Albert Bifet, Mykola Pechenizkiy, Abdelhamid Bouchachia
   - 关联: 阐述分布漂移下决策边界退化的机制，为嵌入表征在自训练伪标签分布漂移时的失对齐提供理论基础

3. **Caccia et al. (2022)** "New Insights on Reducing Abrupt Representation Change in Online Continual Learning" — *ICLR 2022*
   - 作者: Lucas Caccia, Rahaf Aljundi, Nader Asadi, Tinne Tuytelaars, Joëlle Pineau, Eugene Belilovsky
   - 关联: 直接量化了序贯训练中内部表征的突变幅度，其度量框架与自训练循环中嵌入对齐间隙的观测高度类似

4. **Davari et al. (2022)** "Probing Representation Forgetting in Supervised and Unsupervised Continual Learning" — *CVPR 2022*, pp. 16712–16721
   - 作者: MohammadReza Davari, Nader Asadi, Sudhir Mudur, Rahaf Aljundi, Eugene Belilovsky
   - 关联: 表明表征层面的遗忘和漂移独立于任务性能衰退，与本文发现的嵌入几何多样性与语义内容多样性脱耦现象直接对应

## 2. Active Learning under Distribution Shift

5. **Ash et al. (2020)** "Deep Batch Active Learning by Diverse, Uncertain Gradient Lower Bounds" — *ICLR 2020*
   - 作者: Jordan T. Ash, Chicheng Zhang, Akshay Krishnamurthy, John Langford, Alekh Agarwal
   - 关联: BADGE 使用梯度嵌入上的 k-means++ 选择多样性批次——正是本文研究其在表征漂移下失效的嵌入多样性选择机制

6. **Kirsch et al. (2019)** "BatchBALD: Efficient and Diverse Batch Acquisition for Deep Bayesian Active Learning" — *NeurIPS 2019*
   - 作者: Andreas Kirsch, Joost van Amersfoort, Yarin Gal
   - 关联: 通过联合最大化互信息实现多样性批次选择，依赖稳定表征的假设与本文对嵌入漂移的发现形成对照

7. **Kothawade et al. (2021)** "SIMILAR: Submodular Information Measures Based Active Learning In Realistic Scenarios" — *NeurIPS 2021*
   - 作者: Suraj Kothawade, Nathan Beck, Krishnateja Killamsetty, Rishabh Iyer
   - 关联: 在分布偏移的现实场景下做主动学习，表明标准嵌入选择策略在非 i.i.d. 设置中退化——直接支持 BADGE 式选择在嵌入漂移时失效的论点（亦见 §8）

8. **Yehuda et al. (2022)** "Active Learning Through a Covering Lens" — *NeurIPS 2022*
   - 作者: Ofer Yehuda, Avihu Dekel, Guy Hacohen, Daphna Weinshall
   - 关联: 提出基于自监督嵌入空间的覆盖选择，证明表征质量决定多样性选择的成败

## 3. Dimensional Collapse

9. **Jing et al. (2022)** "Understanding Dimensional Collapse in Contrastive Self-supervised Learning" — *ICLR 2022*
   - 作者: Li Jing, Pascal Vincent, Yann LeCun, Yuandong Tian
   - 关联: 刻画对比训练如何将嵌入向量驱入低维子空间——嵌入对齐间隙核心的几何秩坍塌机制

10. **Hua et al. (2021)** "On Feature Decorrelation in Self-Supervised Learning" — *ICCV 2021*
    - 作者: Tianyu Hua, Wenxiao Wang, Zihui Xue, Sucheng Ren, Yue Wang, Hang Zhao
    - 关联: 识别自监督训练中特征轴间相关性导致的维度坍塌，与迭代自训练中嵌入多样性丧失直接对应

11. **Papyan et al. (2020)** "Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training" — *PNAS*, 117(40), pp. 24652–24663
    - 作者: Vardan Papyan, X. Y. Han, David L. Donoho
    - 关联: 高引经典，揭示训练末期最后一层激活坍塌为低维 simplex ETF 结构——建立优化压力坍塌嵌入几何的一般性原理

12. **Laurent et al. (2024)** "Feature Collapse" — *ICLR 2024*
    - 作者: Thomas Laurent, James H. von Brecht, Xavier Bresson
    - 关联: Laurent et al. 证明 feature collapse 在正确条件下是良性的（共享角色实体获得相似表征），但我们的工作表明在迭代自训练中同一机制成为病理性的——内部嵌入坍缩导致 diversity selection 反向选择

## 4. Broader Model Collapse

13. **Shumailov et al. (2024)** "AI Models Collapse When Trained on Recursively Generated Data" — *Nature*, Vol. 631
    - 作者: Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal
    - 关联: Nature 标志性论文，证明递归训练 AI 生成数据导致不可逆的尾分布坍塌，奠定模型坍塌文献基础

14. **Seddik et al. (2024)** "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse" — *COLM 2024*
    - 作者: Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Mérouane Debbah
    - 关联: 理论刻画纯合成/混合训练下的坍塌行为，推导出坍塌不可避免的最大合成数据比例

15. **Briesch et al. (2023)** "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop" — *arXiv preprint, arXiv: 2311.16822*
    - 作者: Martin Briesch, Dominik Sobania, Franz Rothlauf
    - 关联: 实证表明 LLM 迭代自消费中输出多样性随合成数据比例退化，与嵌入空间多样性坍塌互补

16. **Guo et al. (2024)** "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text" — *Findings of NAACL 2024*
    - 作者: Yanzhu Guo, Guokan Shang, Michalis Vazirgiannis, Chloé Clavel
    - 关联: 追踪自训练轮次中词汇、句法、语义多样性的衰退，在高熵创作任务中多样性坍塌最强——直接对应嵌入空间多样性坍塌

17. **Alemohammad et al. (2024)** "Self-Consuming Generative Models Go MAD" — *ICLR 2024*
    - 作者: Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk
    - 关联: 提出"模型自噬障碍"(MAD)，理论证明无新鲜真实数据时自消费循环必然退化质量或多样性

18. **Dohmatob et al. (2025)** "Strong Model Collapse" — *ICLR 2025*
    - 作者: Elvis Dohmatob, Yunzhen Feng, et al.
    - 关联: 建立"强模型坍塌"概念——迭代合成再训练超过临界阈值时的急剧退化相变，为经验坍塌文献提供严格补充

19. **Gerstgrasser et al. (2024)** "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" — *ICML 2024*
    - 作者: Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, Sanmi Koyejo
    - 关联: 证明累积数据可避免坍塌，仅替换式训练不可避免——我们的实验设置正是替换式（每代替换前一代），为坍塌的必然性提供理论基础

## 5. Broader Data Selection

20. **Xia et al. (2024)** "LESS: Selecting Influential Data for Targeted Instruction Tuning" — *ICML 2024*
    - 作者: Mengzhou Xia, Sadhika Malladi, Suchin Gururangan, Sanjeev Arora, Danqi Chen
    - 关联: 基于梯度相似性的指令微调数据选择，在迭代 SFT 场景中与多样性方法直接对比

21. **Liu et al. (2024)** "SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection" — *NeurIPS 2024*
    - 作者: Liangxin Liu, Xuebo Liu, Derek F. Wong, Dongfang Li, Ziyi Wang, Baotian Hu, Min Zhang
    - 关联: 使用 LLM 内部不确定性（token/句子/模型级别）选择指令数据——与多样性正交的质量信号替代方案

22. **Wettig et al. (2024)** "QuRating: Selecting High-Quality Data for Training Language Models" — *ICML 2024*
    - 作者: Alexander Wettig, Aatmik Gupta, Saumya Malik, Danqi Chen
    - 关联: 基于 LLM 判断的四维质量评分进行预训练数据选择，表明质量选择优于启发式过滤

23. **Engstrom et al. (2024)** "DsDm: Model-Aware Dataset Selection with Datamodels" — *ICML 2024*
    - 作者: Logan Engstrom, Axel Feldmann, Aleksander Madry
    - 关联: 将数据选择框架化为基于 datamodel 的任务性能优化，发现朴素质量代理相似性可能损害性能——与代理信号和真实训练效用之间的间隙相关

24. **Sorscher et al. (2022)** "Beyond Neural Scaling Laws: Beating Power Law Scaling via Data Pruning" — *NeurIPS 2022* (Outstanding Paper Award)
    - 作者: Ben Sorscher, Robert Geirhos, Shashank Shekhar, Surya Ganguli, Ari S. Morcos
    - 关联: 证明基于质量指标的数据修剪可打破幂律缩放——激发整个数据选择文献的基础性结果

25. **Xie et al. (2023)** "Data Selection for Language Models via Importance Resampling" (DSIR) — *NeurIPS 2023*
    - 作者: Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang
    - 关联: 基于重要性重采样的特征分布匹配框架，提供非多样性导向的可扩展选择基线

## 6. Goodhart's Law / Reward Hacking

26. **Gao et al. (2023)** "Scaling Laws for Reward Model Overoptimization" — *ICML 2023*
    - 作者: Leo Gao, John Schulman, Jacob Hilton
    - 关联: 定量展示对代理奖励模型的过度优化导致真实目标性能下降——与使用内部嵌入作为优化代理并随模型漂移脱耦的现象直接类比

27. **Skalse et al. (2022)** "Defining and Characterizing Reward Hacking" — *NeurIPS 2022*
    - 作者: Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger
    - 关联: 从形式化角度证明非平凡代理奖励本质上可被利用——解释了为何任何嵌入多样性指标在优化器发现代理与真实目标失对齐后都会被攻破

28. **Pan et al. (2022)** "The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models" — *ICLR 2022*
    - 作者: Alexander Pan, Kush Bhatia, Jacob Steinhardt
    - 关联: 实证映射代理奖励误差在优化压力增加下的复合效应，直接对应嵌入多样性指标随训练推进逐步失效

29. **Karwowski et al. (2024)** "Goodhart's Law in Reinforcement Learning" — *ICLR 2024*
    - 作者: Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kissel, Adrià Garriga-Alonso, Ulrich Paquet
    - 关联: 提供代理优化偏离真实目标的几何刻画并证明早停界——几何直觉直接映射到嵌入漂移中代理指标有效性坍塌的现象

## 7. Diversity Metrics

30. **Li et al. (2016)** "A Diversity-Promoting Objective Function for Neural Conversation Models" — *NAACL-HLT 2016*
    - 作者: Jiwei Li, Michel Galley, Chris Brockett, Jianfeng Gao, Bill Dolan
    - 关联: 提出 Distinct-1/Distinct-2（唯一 n-gram 比例），成为与嵌入多样性指标对比的标准表面多样性度量

31. **Zhu et al. (2018)** "Texygen: A Benchmarking Platform for Text Generation Models" — *SIGIR 2018*
    - 作者: Yaoming Zhu, Sidi Lu, Lei Zheng, Jiaxian Guo, Weinan Zhang, Jun Wang, Yong Yu
    - 关联: 提出 Self-BLEU 作为标准化多样性指标并整合文本生成评估方法论，建立了后续几何/嵌入指标试图扩展的评估框架

32. **Tevet & Berant (2021)** "Evaluating the Evaluation of Diversity in Natural Language Generation" — *EACL 2021*
    - 作者: Guy Tevet, Jonathan Berant
    - 关联: 系统审计 n-gram 和神经多样性指标（包括 Distinct-N 和 Self-BLEU）的失效模式，直接激发了对更好的内容感知多样性度量的需求

33. **Pillutla et al. (2021)** "MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers" — *NeurIPS 2021* (Outstanding Paper Award)
    - 作者: Krishna Pillutla, Swabha Swayamdipta, Rowan Zellers, John Thickstun, Sean Welleck, Yejin Choi, Zaid Harchaoui
    - 关联: 在量化 LLM 嵌入空间中使用 KL 散度衡量生成文本与人类文本的分布差异——嵌入空间多样性度量的直接先例，为"嵌入对齐间隙"提供关键前置工作

## 8. Submodular Maximization for Data Selection

34. **Iyer & Bilmes (2013)** "Submodular Optimization with Submodular Cover and Submodular Knapsack Constraints" — *NeurIPS 2013* (Outstanding Paper Award)
    - 作者: Rishabh Iyer, Jeff Bilmes
    - 关联: 建立带预算约束的次模最大化框架，为嵌入空间上的多样性数据选择方法奠基

35. **Wei et al. (2015)** "Submodularity in Data Subset Selection and Active Learning" — *ICML 2015*
    - 作者: Kai Wei, Rishabh Iyer, Jeff Bilmes
    - 关联: 将数据子集选择形式化为次模最大化（facility location、graph cut），在特征/嵌入空间中度量覆盖和多样性——嵌入对齐间隙问题直接攻击的经典框架

36. **Mirzasoleiman et al. (2020)** "Coresets for Data-efficient Training of Machine Learning Models" — *ICML 2020*
    - 作者: Baharan Mirzasoleiman, Jeff Bilmes, Jure Leskovec
    - 关联: CRAIG 使用梯度嵌入上的 facility location 次模函数选择核心集，在迭代应用时直接受嵌入空间退化影响

## 统计
- 总引用数: 36
- 子领域覆盖: 8/8
- 每子领域篇数: 3–7
- 验证状态: 全部 VERIFIED（WebSearch 确认标题、作者、年份、venue）
- 年份分布: 2013–2025，其中 2020 年后 26 篇
