# 引用审计报告（审计员 C）

**审计日期**: 2026-05-29
**审计范围**: `references.bib` 全部 45 条 entry + 正文/附录所有 `\cite` 引用位置
**方法**: 每条 entry 均通过 WebSearch 验证真实性、作者、年份、标题、Venue

---

## 总结

- **总引用数**: 45
- **真实存在**: 45/45（无 hallucinated citation）
- **有问题**: 3 条（均为未被正文引用的冗余 entry）
- **建议改进**: 2 条（年份/venue 可优化）
- **正文引用归因错误**: 0

---

## 逐条结果

### 1. @inproceedings{gu2023maniskill2}
- **标题**: ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills
- **真实性**: ✓ 论文存在，ICLR 2023
- **作者**: ✓ Gu, Jiayuan et al. 匹配
- **年份**: ✓ 2023
- **标题**: ✓ 逐词匹配
- **Venue**: ✓ International Conference on Learning Representations (ICLR 2023)
- **正文引用位置**: ✓ experiments_results.tex §F3-F5 提到 ManiSkill 任务，引用正确
- **状态**: **OK**

### 2. @inproceedings{micheli2023iris}
- **标题**: Transformers are Sample-Efficient World Models
- **真实性**: ✓ 论文存在，ICLR 2023 (notable top 5%)
- **作者**: ✓ Micheli, Vincent; Alonso, Eloi; Fleuret, François
- **年份**: ✓ 2023
- **标题**: ✓ 匹配
- **Venue**: ✓ ICLR 2023
- **正文引用位置**: ✓ conclusion.tex Limitations 部分提到 transformer-based world models
- **状态**: **OK**

### 3. @article{sutton1999options}
- **标题**: Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning
- **真实性**: ✓ 经典论文，Artificial Intelligence Vol 112, 1999
- **作者**: ✓ Sutton, R.S; Precup, D; Singh, S（缩写正确）
- **年份**: ✓ 1999
- **标题**: ✓ 匹配
- **Venue**: ✓ Artificial Intelligence 112（期刊名+卷号格式略非标准但正确）
- **正文引用位置**: ✓ related_work.tex "options framework" 引用正确
- **状态**: **OK**

### 4. @inproceedings{hafner2020dreamerv1}
- **标题**: Dream to Control: Learning Behaviors by Latent Imagination
- **真实性**: ✓ 论文存在，ICLR 2020
- **作者**: ✓ Hafner, D; Lillicrap, T; Ba, J; Norouzi, M
- **年份**: ✓ 2020
- **标题**: ✓ 匹配
- **Venue**: ✓ ICLR 2020
- **正文引用位置**: ✓ related_work.tex "Dreamer family" 引用正确
- **状态**: **OK**

### 5. @article{hafner2023dreamerv3}
- **标题**: Mastering Diverse Control Tasks through World Models
- **真实性**: ✓ 论文存在，Nature 2025; arXiv 2301.04104 (2023)
- **作者**: ✓ Hafner, Danijar; Pasukonis, Jurgis; Ba, Jimmy; Lillicrap, Timothy
- **年份**: ✓ 2025（Nature 发表年份，bib key "2023" 为 arXiv 年份，仅为助记符）
- **标题**: ✓ 匹配 Nature 版标题（arXiv 版为 "Mastering Diverse Domains..."，bib 正确使用 Nature 版）
- **Venue**: ✓ Nature
- **正文引用位置**: ✓ 多处引用 DreamerV3 均正确
- **状态**: **OK**

### 6. @inproceedings{sharma2017figar}
- **标题**: Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning
- **真实性**: ✓ 论文存在，ICLR 2017
- **作者**: ✓ Sharma, S; Lakshminarayanan, A.S; Ravindran, B
- **年份**: ✓ 2017
- **标题**: ✓ 匹配
- **Venue**: ✓ ICLR 2017
- **正文引用位置**: ✓ related_work.tex "FiGAR learns per-action repetition counts" 正确
- **状态**: **OK**

### 7. @inproceedings{pertsch2020spirl}
- **标题**: Accelerating Reinforcement Learning with Learned Skill Priors
- **真实性**: ✓ 论文存在，CoRL 2020（PMLR v155, 2021 出版）
- **作者**: ✓ Pertsch, Karl; Lee, Youngwoon; Lim, Joseph J.
- **年份**: ✗ bib 写 year=2021（proceedings 出版年），但会议为 CoRL 2020。bib key 写 "pertsch2020" 暗示会议年。**建议统一为 2020 或在 booktitle 中注明 CoRL 2020**
- **标题**: ✓ 匹配
- **Venue**: ✓ Conference on Robot Learning
- **正文引用位置**: ✓ related_work.tex "SPiRL accelerates RL through learned skill priors" 正确
- **状态**: **有小问题**（年份 2021 vs 会议年 2020，不影响正确性但建议统一）

### 8. @inproceedings{janner2019mbpo}
- **标题**: When to Trust Your Model: Model-Based Policy Optimization
- **真实性**: ✓ 论文存在，NeurIPS 2019
- **作者**: ✓ Janner, M; Fu, J; Zhang, M; Levine, S
- **年份**: ✓ 2019
- **标题**: ✓ 匹配
- **Venue**: ✓ Advances in Neural Information Processing Systems (NeurIPS 2019)
- **正文引用位置**: ✓ related_work.tex "MBPO bounds rollout error" 正确
- **状态**: **OK**

### 9. @article{asadi2019combating}
- **标题**: Combating the Compounding-Error Problem with a Multi-step Model
- **真实性**: ✓ 论文存在，arXiv:1905.13320
- **作者**: ✓ Asadi, K; Misra, D; Kim, S; Littman, M.L
- **年份**: ✓ 2019
- **标题**: ✓ 匹配
- **Venue**: ✓ arXiv preprint（未找到正式发表版本）
- **正文引用位置**: ✓ related_work.tex "compounding error in multi-step rollouts" 引用正确
- **状态**: **OK**

### 10. @inproceedings{hansen2024tdmpc2}
- **标题**: TD-MPC2: Scalable, Robust World Models for Continuous Control
- **真实性**: ✓ 论文存在，ICLR 2024
- **作者**: ✗ bib 列出 "Hansen, N and Su, H and Wang, X"，实际为 Nicklas Hansen, Hao Su, Xiaolong Wang。缩写正确但不完整（可接受）
- **年份**: ✓ 2024
- **标题**: ✓ 匹配
- **Venue**: ✓ ICLR 2024
- **正文引用位置**: ✓ 多处引用 TD-MPC2 均正确
- **状态**: **OK**

### 11. @inproceedings{yu2020mopo}
- **标题**: MOPO: Model-based Offline Policy Optimization
- **真实性**: ✓ 论文存在，NeurIPS 2020
- **作者**: ✓ Yu, T; Thomas, G; Yu, L; Ermon, S; Zou, J; Levine, S; Finn, C; Ma, T
- **年份**: ✓ 2020
- **标题**: ✓ 匹配
- **Venue**: ✓ NeurIPS 2020
- **正文引用位置**: ✓ related_work.tex "MOPO" 引用正确
- **状态**: **OK**

### 12. @inproceedings{thrun1993issues}
- **标题**: Issues in Using Function Approximation for Reinforcement Learning
- **真实性**: ✓ 经典论文，1993
- **作者**: ✓ Thrun, S; Schwartz, A（Sebastian Thrun, Anton Schwartz）
- **年份**: ✓ 1993
- **标题**: ✓ 匹配
- **Venue**: ✓ Connectionist Models Summer School（Fourth Connectionist Models Summer School）
- **正文引用位置**: ✓ related_work.tex "Maximization bias" 引用正确
- **状态**: **OK**

### 13. @inproceedings{vanhasselt2016double}
- **标题**: Deep Reinforcement Learning with Double Q-Learning
- **真实性**: ✓ 论文存在，AAAI 2016
- **作者**: ✓ van Hasselt, Hado; Guez, Arthur; Silver, David
- **年份**: ✓ 2016
- **标题**: ✓ 匹配
- **Venue**: ✓ AAAI Conference on Artificial Intelligence
- **正文引用位置**: ✓ related_work.tex "Double Q-learning" 引用正确
- **状态**: **OK**

### 14. @inproceedings{fujimoto2018td3}
- **标题**: Addressing Function Approximation Error in Actor-Critic Methods
- **真实性**: ✓ 论文存在，ICML 2018
- **作者**: ✓ Fujimoto, Scott; van Hoof, Herke; Meger, David
- **年份**: ✓ 2018
- **标题**: ✓ 匹配
- **Venue**: ✓ International Conference on Machine Learning (ICML 2018)
- **正文引用位置**: ✓ related_work.tex "TD3" + experiments dual-critic method 引用正确
- **状态**: **OK**

### 15. @inproceedings{lu2018nondelusional}
- **标题**: Non-delusional Q-learning and Value-Iteration
- **真实性**: ✓ 论文存在，NeurIPS 2018 (Oral)
- **作者**: ✓ Lu, T; Schuurmans, D; Boutilier, C（Tyler Lu, Dale Schuurmans, Craig Boutilier）
- **年份**: ✓ 2018
- **标题**: ✓ 匹配
- **Venue**: ✓ Advances in Neural Information Processing Systems (NeurIPS 2018)
- **正文引用位置**: ✓ introduction.tex + related_work.tex + appendix.tex "delusional bias" 引用正确
- **状态**: **OK**

### 16. @inproceedings{biedenkapp2021temporl}
- **标题**: TempoRL: Learning When to Act
- **真实性**: ✓ 论文存在，ICML 2021
- **作者**: ✓ Biedenkapp, A; Rajan, R; Hutter, F; Lindauer, M
- **年份**: ✓ 2021
- **标题**: ✓ 匹配
- **Venue**: ✓ International Conference on Machine Learning (ICML 2021)
- **正文引用位置**: ✓ related_work.tex "TempoRL" 引用正确
- **状态**: **OK**

### 17. @inproceedings{hafner2021dreamerv2}
- **标题**: Mastering Atari with Discrete World Models
- **真实性**: ✓ 论文存在，ICLR 2021
- **作者**: ✓ Hafner, D; Lillicrap, T; Norouzi, M; Ba, J
- **年份**: ✓ 2021
- **标题**: ✓ 匹配
- **Venue**: ✓ ICLR 2021
- **正文引用位置**: ✓ related_work.tex "Dreamer family" 引用正确
- **状态**: **OK**

### 18. @inproceedings{gumbsch2024thick}
- **标题**: Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics
- **真实性**: ✓ 论文存在，ICLR 2024
- **作者**: ✓ Gumbsch, C; Sajid, N; Martius, G; Butz, M.V（Christian Gumbsch, Noor Sajid, Georg Martius, Martin V. Butz）
- **年份**: ✓ 2024
- **标题**: ✓ 匹配
- **Venue**: ✓ ICLR 2024
- **正文引用位置**: ✓ related_work.tex + appendix.tex "THICK" hierarchical variant 引用正确
- **状态**: **OK**

### 19. @inproceedings{mattes2024hieros}
- **标题**: Hieros: Hierarchical Imagination on Structured State Space Sequence World Models
- **真实性**: ✓ 论文存在，ICML 2024
- **作者**: ✓ Mattes, P; Schlosser, R; Herbrich, R（Paul Mattes, Rainer Schlosser, Ralf Herbrich）
- **年份**: ✓ 2024
- **标题**: ✓ 匹配
- **Venue**: ✓ International Conference on Machine Learning (ICML 2024)
- **正文引用位置**: ✓ related_work.tex + appendix.tex "Hieros" hierarchical variant 引用正确
- **状态**: **OK**

### 20. @inproceedings{henderson2018deep}
- **标题**: Deep Reinforcement Learning that Matters
- **真实性**: ✓ 论文存在，AAAI 2018
- **作者**: ✓ Henderson, P; Islam, R; Bachman, P; Pineau, J; Precup, D; Meger, D
- **年份**: ✓ 2018
- **标题**: ✓ 匹配
- **Venue**: ✓ AAAI Conference on Artificial Intelligence
- **正文引用位置**: ✓ related_work.tex "factorial diagnostic methodology follows Henderson et al." 引用正确
- **状态**: **OK**

### 21. @inproceedings{lambert2020objective}
- **标题**: Objective Mismatch in Model-based Reinforcement Learning
- **真实性**: ✓ 论文存在，L4DC 2020
- **作者**: ✓ Lambert, N; Amos, B; Yadan, O; Calandra, R
- **年份**: ✓ 2020
- **标题**: ✓ 匹配
- **Venue**: ✓ L4DC（Proceedings of 2nd Conference on Learning for Dynamics and Control）
- **正文引用位置**: ✓ related_work.tex 与 asadi2019combating 一起引用于 "Compounding error in multi-step rollouts"。Lambert 2020 主题为 objective mismatch 而非 compounding error，但上下文将两者作为 "related but distinct" 现象讨论，引用可接受
- **状态**: **OK**

### 22. @inproceedings{agarwal2021precipice}
- **标题**: Deep Reinforcement Learning at the Edge of the Statistical Precipice
- **真实性**: ✓ 论文存在，NeurIPS 2021 Outstanding Paper
- **作者**: ✓ Agarwal, R; Schwarzer, M; Castro, P.S; Courville, A.C; Bellemare, M
- **年份**: ✓ 2021
- **标题**: ✓ 匹配
- **Venue**: ✓ Advances in Neural Information Processing Systems (NeurIPS 2021)
- **正文引用位置**: ✓ experiments 多处引用 per-seed trajectories / IQM 方法，正确
- **状态**: **OK**

### 23. @article{tassa2018dmcontrol}
- **标题**: DeepMind Control Suite
- **真实性**: ✓ 论文存在，arXiv:1801.00690
- **作者**: ✓ Tassa, Yuval et al. 完整作者列表匹配
- **年份**: ✓ 2018
- **标题**: ✓ 匹配
- **Venue**: ✓ arXiv preprint（该论文广泛以 arXiv 形式被引用，无正式期刊版本）
- **正文引用位置**: ✓ experiments 多处引用 DMC Walker Walk / Cheetah Run，正确
- **状态**: **OK**

### 24. @article{hafner2025dreamerv4}
- **标题**: Training Agents Inside of Scalable World Models
- **真实性**: ✓ 论文存在，arXiv:2509.24527 (Sep 2025)
- **作者**: ✓ Hafner, Danijar; Yan, Wilson; Lillicrap, Timothy
- **年份**: ✓ 2025
- **标题**: ✓ 匹配
- **Venue**: ✓ arXiv preprint
- **正文引用位置**: ✓ related_work.tex "Dreamer family" + appendix.tex "DreamerV4 transformer-based" 正确
- **状态**: **OK**

### 25. @inproceedings{lyle2022capacity}
- **标题**: Understanding and Preventing Capacity Loss in Reinforcement Learning
- **真实性**: ✓ 论文存在，ICLR 2022 Spotlight
- **作者**: ✓ Lyle, C; Rowland, M; Dabney, W（Clare Lyle, Mark Rowland, Will Dabney）
- **年份**: ✓ 2022
- **标题**: ✓ 匹配
- **Venue**: ✓ ICLR 2022
- **正文引用位置**: ✓ appendix.tex 讨论 capacity loss 与 CIVO seed divergence 的关系，正确
- **状态**: **OK**

### 26. @inproceedings{nhu2025tawm}
- **标题**: Time-Aware World Model for Adaptive Prediction and Control
- **真实性**: ✓ 论文存在，ICML 2025
- **作者**: ✓ Nhu, Anh N.; Son, Sanghyun; Lin, Ming C.
- **年份**: ✓ 2025
- **标题**: ✓ 匹配
- **Venue**: ✓ International Conference on Machine Learning (ICML 2025)
- **正文引用位置**: ✓ introduction.tex + related_work.tex + appendix.tex "TAWM conditions a world model on Δt" 正确
- **状态**: **OK**

### 27. @inproceedings{li2025lsimagine}
- **标题**: Open-World Reinforcement Learning over Long Short-Term Imagination
- **真实性**: ✓ 论文存在，ICLR 2025 Oral
- **作者**: ✓ Li, J; Wang, Q; Wang, Y; Jin, X; Li, Y; Zeng, W; Yang, X
- **年份**: ✓ 2025
- **标题**: ✓ 匹配
- **Venue**: ✓ ICLR 2025
- **正文引用位置**: ✓ related_work.tex + appendix.tex "LS-Imagine" hierarchical variant 引用正确
- **状态**: **OK**

### 28. @inproceedings{chen2021redq}
- **标题**: Randomized Ensembled Double Q-Learning: Learning Fast Without a Model
- **真实性**: ✓ 论文存在，ICLR 2021
- **作者**: ✓ Chen, Xinyue; Wang, Che; Zhou, Zijian; Ross, Keith
- **年份**: ✓ 2021
- **标题**: ✓ 匹配
- **Venue**: ✓ ICLR 2021
- **正文引用位置**: ✓ related_work.tex "ensemble methods" 引用正确
- **状态**: **OK**

### 29. @inproceedings{bacon2017optioncritc}
- **标题**: The Option-Critic Architecture
- **真实性**: ✓ 论文存在，AAAI 2017
- **作者**: ✓ Bacon, Pierre-Luc; Harb, Jean; Precup, Doina
- **年份**: ✓ 2017
- **标题**: ✓ 匹配
- **Venue**: ✓ AAAI Conference on Artificial Intelligence
- **正文引用位置**: ✓ related_work.tex "option-critic" 引用正确
- **备注**: bib key 拼写为 "optioncritc"（缺少 'i'），仅影响 key 名称，不影响输出
- **状态**: **OK**

### 30. @inproceedings{buckman2018steve}
- **标题**: Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion
- **真实性**: ✓ 论文存在，NeurIPS 2018 Oral
- **作者**: ✓ Buckman, Jacob; Hafner, Danijar; Tucker, George; Brevdo, Eugene; Lee, Honglak
- **年份**: ✓ 2018
- **标题**: ✓ 匹配
- **Venue**: ✓ NeurIPS 2018
- **正文引用位置**: ✗ **未在任何 tex 文件中被引用（冗余 entry）**
- **状态**: **有问题** — 未被引用，应从 bib 中移除

### 31. @inproceedings{chua2018pets}
- **标题**: Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models
- **真实性**: ✓ 论文存在，NeurIPS 2018
- **作者**: ✓ Chua, Kurtland; Calandra, Roberto; McAllister, Rowan; Levine, Sergey
- **年份**: ✓ 2018
- **标题**: ✓ 匹配
- **Venue**: ✓ NeurIPS 2018
- **正文引用位置**: ✗ **未在任何 tex 文件中被引用（冗余 entry）**
- **状态**: **有问题** — 未被引用，应从 bib 中移除

### 32. @article{bishop1995noise}
- **标题**: Training with Noise is Equivalent to Tikhonov Regularization
- **真实性**: ✓ 论文存在，Neural Computation 1995
- **作者**: ✓ Bishop, Chris M.
- **年份**: ✓ 1995
- **标题**: ✓ 匹配
- **Venue**: ✓ Neural Computation, Vol 7, No 1, pp 108-116
- **正文引用位置**: ✓ related_work.tex "training-with-noise" 与 TCN 方法类比，引用正确
- **状态**: **OK**

### 33. @inproceedings{fortunato2018noisynet}
- **标题**: Noisy Networks for Exploration
- **真实性**: ✓ 论文存在，ICLR 2018
- **作者**: ✓ Fortunato, Meire et al. 完整作者列表匹配
- **年份**: ✓ 2018
- **标题**: ✓ 匹配
- **Venue**: ✓ ICLR 2018
- **正文引用位置**: ✗ **未在任何 tex 文件中被引用（冗余 entry）**
- **状态**: **有问题** — 未被引用，应从 bib 中移除

### 34. @inproceedings{parr1998ham}
- **标题**: Reinforcement Learning with Hierarchies of Machines
- **真实性**: ✓ 论文存在，NIPS 1997 / NeurIPS 10
- **作者**: ✓ Parr, Ronald; Russell, Stuart
- **年份**: ✓/△ bib 写 1998（proceedings 出版年），会议实际为 NIPS 1997。两种写法均有先例，可接受
- **标题**: ✓ 匹配
- **Venue**: ✓ Advances in Neural Information Processing Systems
- **正文引用位置**: ✓ related_work.tex "HAM" 引用正确
- **状态**: **OK**（年份 1998 = proceedings year，可接受）

### 35. @article{dietterich2000maxq}
- **标题**: Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition
- **真实性**: ✓ 论文存在，JAIR 2000
- **作者**: ✓ Dietterich, Thomas G.
- **年份**: ✓ 2000
- **标题**: ✓ 匹配
- **Venue**: ✓ Journal of Artificial Intelligence Research, Vol 13, pp 227-303
- **正文引用位置**: ✓ related_work.tex "MAXQ" 引用正确
- **状态**: **OK**

### 36. @inproceedings{bradtke1995smdp}
- **标题**: Reinforcement Learning Methods for Continuous-Time Markov Decision Problems
- **真实性**: ✓ 论文存在，NIPS 1994 / NeurIPS 7
- **作者**: ✓ Bradtke, Steven J.; Duff, Michael O.
- **年份**: ✓/△ bib 写 1995（proceedings 出版年），会议实际为 NIPS 1994。可接受
- **标题**: ✓ 匹配
- **Venue**: ✓ Advances in Neural Information Processing Systems
- **正文引用位置**: ✓ related_work.tex "Semi-MDP theory" 引用正确
- **状态**: **OK**（年份 1995 = proceedings year，可接受）

### 37. @inproceedings{kidambi2020morel}
- **标题**: MOReL: Model-Based Offline Reinforcement Learning
- **真实性**: ✓ 论文存在，NeurIPS 2020
- **作者**: ✓ Kidambi, Rahul; Rajeswaran, Aravind; Netrapalli, Praneeth; Joachims, Thorsten
- **年份**: ✓ 2020
- **标题**: ✓ 匹配
- **Venue**: ✓ NeurIPS 2020
- **正文引用位置**: ✓ related_work.tex "MOReL penalizes model uncertainty" 引用正确
- **状态**: **OK**

### 38. @inproceedings{yu2021combo}
- **标题**: COMBO: Conservative Offline Model-Based Policy Optimization
- **真实性**: ✓ 论文存在，NeurIPS 2021
- **作者**: ✓ Yu, Tianhe; Kumar, Aviral; Rafailov, Rafael; Rajeswaran, Aravind; Levine, Sergey; Finn, Chelsea
- **年份**: ✓ 2021
- **标题**: ✓ 匹配
- **Venue**: ✓ NeurIPS 2021
- **正文引用位置**: ✓ related_work.tex "COMBO" 引用正确
- **状态**: **OK**

### 39. @inproceedings{hamrick2021planning}
- **标题**: On the Role of Planning in Model-Based Deep Reinforcement Learning
- **真实性**: ✓ 论文存在，ICLR 2021
- **作者**: ✓ Hamrick, Jessica B. et al. 完整作者列表匹配
- **年份**: ✓ 2021
- **标题**: ✓ 匹配
- **Venue**: ✓ ICLR 2021
- **正文引用位置**: ✓ related_work.tex "Decision-aware model learning" — Hamrick et al. 研究 MuZero planning，MuZero 的 end-to-end 训练可视为 decision-aware。引用语境可接受
- **状态**: **OK**

### 40. @inproceedings{wu2023daydreamer}
- **标题**: DayDreamer: World Models for Physical Robot Learning
- **真实性**: ✓ 论文存在，CoRL 2022 (PMLR v205, 2023 出版)
- **作者**: ✓ Wu, Philipp; Escontrela, Alejandro; Hafner, Danijar; Abbeel, Pieter; Goldberg, Ken
- **年份**: ✓ 2023（PMLR proceedings 出版年）
- **标题**: ✓ 匹配
- **Venue**: ✓ Conference on Robot Learning
- **正文引用位置**: ✓ introduction.tex "World-model RL enables sample-efficient learning" 引用正确
- **状态**: **OK**

### 41. @inproceedings{park2021timediscretization}
- **标题**: Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods
- **真实性**: ✓ 论文存在，NeurIPS 2021
- **作者**: ✓ Park, Seohong; Kim, Jaekyeom; Kim, Gunhee
- **年份**: ✓ 2021
- **标题**: ✓ 匹配
- **Venue**: ✓ Advances in Neural Information Processing Systems (NeurIPS 2021)
- **正文引用位置**: ✓ related_work.tex "complementary formulations" for action repetition 引用正确
- **状态**: **OK**

### 42. @article{wang2024elastic}
- **标题**: Reinforcement Learning with Elastic Time Steps
- **真实性**: ✓ 论文存在，arXiv:2402.14961
- **作者**: ✓ Wang, Dong; Beltrame, Giovanni
- **年份**: ✓ 2024
- **标题**: ✓ 匹配
- **Venue**: ✓ arXiv preprint
- **正文引用位置**: ✓ related_work.tex "learn elastic time steps that adapt step size to state dynamics" 引用正确
- **状态**: **OK**

### 43. @article{colas2018seeds}
- **标题**: How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments
- **真实性**: ✓ 论文存在，arXiv:1806.08295
- **作者**: ✓ Colas, Cédric; Sigaud, Olivier; Oudeyer, Pierre-Yves
- **年份**: ✓ 2018
- **标题**: ✓ 匹配
- **Venue**: ✓ arXiv preprint
- **正文引用位置**: ✓ conclusion.tex/limitations "Seed counts (4-5)" 引用正确
- **状态**: **OK**

### 44. @article{benechehab2023multitimestep}
- **标题**: Multi-timestep models for Model-based Reinforcement Learning
- **真实性**: ✓ 论文存在，arXiv:2310.05672
- **作者**: ✓ Benechehab, Abdelhakim; Paolo, Giuseppe; Thomas, Albert; Filippone, Maurizio; Kégl, Balázs
- **年份**: ✓ 2023
- **标题**: ✓ 匹配
- **Venue**: ✓ arXiv preprint
- **正文引用位置**: ✓ related_work.tex "Multi-timestep world models learn predictions at variable horizons" 引用正确
- **状态**: **OK**

### 45. @inproceedings{hafner2022director}
- **标题**: Deep Hierarchical Planning from Pixels
- **真实性**: ✓ 论文存在，NeurIPS 2022
- **作者**: ✓ Hafner, Danijar; Lee, Kuang-Huei; Fischer, Ian; Abbeel, Pieter
- **年份**: ✓ 2022
- **标题**: ✓ 匹配
- **Venue**: ✓ Advances in Neural Information Processing Systems (NeurIPS 2022)
- **正文引用位置**: ✓ related_work.tex "hierarchical variants" (Director) 引用正确
- **状态**: **OK**

---

## 问题汇总

| # | Cite Key | 问题类型 | 严重程度 | 说明 |
|---|----------|----------|----------|------|
| 1 | `buckman2018steve` | 冗余 entry | 低 | bib 中存在但未被任何 tex 文件引用，应移除 |
| 2 | `chua2018pets` | 冗余 entry | 低 | bib 中存在但未被任何 tex 文件引用，应移除 |
| 3 | `fortunato2018noisynet` | 冗余 entry | 低 | bib 中存在但未被任何 tex 文件引用，应移除 |
| 4 | `pertsch2020spirl` | 年份不一致 | 极低 | year=2021（proceedings年）vs 会议年 CoRL 2020；建议统一 |

## 未发现的问题

- **无 hallucinated citation**: 全部 45 篇论文均经 WebSearch 验证真实存在
- **无作者拼写错误**: 所有作者名（含中文作者拼音）均正确
- **无标题错误**: 所有标题逐词核对匹配
- **无 venue 错误**: 所有会议/期刊名称正确
- **无错误归因**: 所有正文 `\cite` 位置的引用上下文均与被引论文内容一致
- **无 arXiv→会议版遗漏**: hafner2023dreamerv3 已更新为 Nature 2025 版；其余 arXiv-only 论文（asadi2019, tassa2018, wang2024, colas2018, benechehab2023）经查证确无正式发表版本
