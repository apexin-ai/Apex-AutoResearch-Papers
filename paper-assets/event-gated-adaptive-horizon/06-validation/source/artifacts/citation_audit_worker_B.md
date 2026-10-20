# 引用审计报告（审计员 B）

**审计日期**: 2026-05-29
**审计方法**: 逐条 WebSearch 验证（标题前5-8词 + 第一作者姓氏）
**bib 文件**: `docs/paper/references.bib`
**正文文件**: `sections/` 下 9 个 .tex 文件（introduction, related_work, experiments_results, methodology, results, analysis, appendix, conclusion, abstract_body）

**总引用数**: 45 条 bib entry
**正文中实际引用**: 42 条（3 条未被引用）
**幻觉引用**: 0 条（全部真实存在）
**归因错误**: 0 条（正文引用上下文均正确）

---

## 问题汇总

| 严重性 | 数量 | 说明 |
|--------|------|------|
| HIGH | 2 | 年份错误、作者缺失 |
| MEDIUM | 3 | 未引用的 bib entry |
| LOW | 4 | bib key 与 year 不一致、作者 initial 缺失、标题大小写 |

---

## 逐条结果

### 1. @inproceedings{gu2023maniskill2}
- **真实性**: ✓ 论文存在（arXiv:2302.04659）
- **作者**: ✓ Gu, Jiayuan 等 15 人，正确
- **年份**: ✓ 2023
- **标题**: ✓ "ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills"
- **Venue**: ✓ ICLR 2023
- **正文引用位置**: ✓ experiments_results.tex / results.tex 中引用 ManiSkill 任务，正确
- **状态**: **OK**

### 2. @inproceedings{micheli2023iris}
- **真实性**: ✓ 论文存在（arXiv:2209.00588）
- **作者**: ✓ Micheli, Vincent; Alonso, Eloi; Fleuret, François
- **年份**: ✓ 2023
- **标题**: ✓ "Transformers are Sample-Efficient World Models"
- **Venue**: ✓ ICLR 2023
- **正文引用位置**: ✓ conclusion.tex / limitations 中引用为 transformer-based world model 代表，正确
- **状态**: **OK**

### 3. @article{sutton1999options}
- **真实性**: ✓ 经典论文，存在
- **作者**: ✓ Sutton, R.S; Precup, D; Singh, S（缩写形式，实际为 Richard S. Sutton, Doina Precup, Satinder Singh）
- **年份**: ✓ 1999
- **标题**: ✓ "Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning"
- **Venue**: ✓ Artificial Intelligence, Volume 112（缺 issue/pages: Issues 1–2, pp 181–211，minor）
- **正文引用位置**: ✓ related_work.tex 中引用为 options framework，正确
- **状态**: **OK**（minor: journal 缺 issue/pages）

### 4. @inproceedings{hafner2020dreamerv1}
- **真实性**: ✓ 论文存在（arXiv:1912.01603）
- **作者**: ✓ Hafner, D; Lillicrap, T; Ba, J; Norouzi, M（缩写形式）
- **年份**: ✓ 2020
- **标题**: ✓ "Dream to Control: Learning Behaviors by Latent Imagination"
- **Venue**: ✓ ICLR 2020
- **正文引用位置**: ✓ related_work.tex Dreamer family 列表中，正确
- **状态**: **OK**

### 5. @article{hafner2023dreamerv3}
- **真实性**: ✓ 论文存在（Nature 640, 647–653, 2025; arXiv:2301.04104）
- **作者**: ✓ Hafner, Danijar; Pasukonis, Jurgis; Ba, Jimmy; Lillicrap, Timothy
- **年份**: ✓ year=2025 对应 Nature 发表年份，正确
- **标题**: ✓ "Mastering Diverse Control Tasks through World Models"（Nature 版标题，非 arXiv 版 "Domains"）
- **Venue**: ✓ Nature
- **正文引用位置**: ✓ 多处引用为 DreamerV3 基础架构，正确
- **状态**: **OK**（LOW: bib key `hafner2023dreamerv3` 中的 2023 对应 arXiv 日期，year 字段 2025 对应 Nature 日期，不一致但 year 字段本身正确。建议更新 key 为 `hafner2025dreamerv3`）

### 6. @inproceedings{sharma2017figar}
- **真实性**: ✓ 论文存在（arXiv:1702.06054）
- **作者**: ✓ Sharma, S; Lakshminarayanan, A.S; Ravindran, B（缩写形式）
- **年份**: ✓ 2017
- **标题**: ✓ "Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning"
- **Venue**: ✓ ICLR 2017
- **正文引用位置**: ✓ related_work.tex 中引用为 action-repetition 方法，正确
- **状态**: **OK**

### 7. @inproceedings{pertsch2020spirl}
- **真实性**: ✓ 论文存在（arXiv:2010.11944）
- **作者**: ✓ Pertsch, Karl; Lee, Youngwoon; Lim, Joseph J.
- **年份**: ✗ **year=2021，但会议是 CoRL 2020**（2020年11月16-18日举办）。PMLR Volume 155 于 2021 年出版。bib key 写 2020（会议年），year 字段写 2021（出版年），不一致。标准惯例应用会议年 2020。
- **标题**: ✓ "Accelerating Reinforcement Learning with Learned Skill Priors"
- **Venue**: ✓ Conference on Robot Learning（但配合 year=2021 会被理解为 CoRL 2021，实际是 CoRL 2020）
- **正文引用位置**: ✓ related_work.tex 中引用为 learned skill priors，正确
- **状态**: **有问题 (HIGH)** — year 应改为 2020

### 8. @inproceedings{janner2019mbpo}
- **真实性**: ✓ 论文存在（arXiv:1906.08253）
- **作者**: ✓ Janner, M; Fu, J; Zhang, M; Levine, S（缩写形式）
- **年份**: ✓ 2019
- **标题**: ✓ "When to Trust Your Model: Model-Based Policy Optimization"
- **Venue**: ✓ NeurIPS 2019
- **正文引用位置**: ✓ related_work.tex 中引用为 model-based 方法 bounding rollout error，正确
- **状态**: **OK**

### 9. @article{asadi2019combating}
- **真实性**: ✓ 论文存在（arXiv:1905.13320）
- **作者**: ✓ Asadi, K; Misra, D; Kim, S; Littman, M.L（缩写形式）
- **年份**: ✓ 2019
- **标题**: ✓ "Combating the Compounding-Error Problem with a Multi-step Model"
- **Venue**: ✓ arXiv preprint
- **正文引用位置**: ✓ related_work.tex 中引用为 compounding error，正确
- **状态**: **OK**

### 10. @inproceedings{hansen2024tdmpc2}
- **真实性**: ✓ 论文存在（arXiv:2310.16828）
- **作者**: ✓ Hansen, N; Su, H; Wang, X（Nicklas Hansen, Hao Su, Xiaolong Wang）
- **年份**: ✓ 2024
- **标题**: ✓ "TD-MPC2: Scalable, Robust World Models for Continuous Control"
- **Venue**: ✓ ICLR 2024
- **正文引用位置**: ✓ introduction.tex, related_work.tex, conclusion.tex 中引用为 TD-MPC2 / MPC 框架，正确
- **状态**: **OK**

### 11. @inproceedings{yu2020mopo}
- **真实性**: ✓ 论文存在（arXiv:2005.13239）
- **作者**: ✓ Yu, T; Thomas, G; Yu, L; Ermon, S; Zou, J; Levine, S; Finn, C; Ma, T
- **年份**: ✓ 2020
- **标题**: ✓ "MOPO: Model-based Offline Policy Optimization"
- **Venue**: ✓ NeurIPS 2020
- **正文引用位置**: ✓ related_work.tex 中引用为 bounding rollout error，正确
- **状态**: **OK**

### 12. @inproceedings{thrun1993issues}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Thrun, S; Schwartz, A（Sebastian Thrun, Anton Schwartz）
- **年份**: ✓ 1993
- **标题**: ✓ "Issues in Using Function Approximation for Reinforcement Learning"
- **Venue**: ✓ Connectionist Models Summer School（完整应为 "Proceedings of the 1993 Connectionist Models Summer School"，minor）
- **正文引用位置**: ✓ related_work.tex 中引用为 maximization bias 来源，正确
- **状态**: **OK**

### 13. @inproceedings{vanhasselt2016double}
- **真实性**: ✓ 论文存在
- **作者**: ✓ van Hasselt, Hado; Guez, Arthur; Silver, David
- **年份**: ✓ 2016
- **标题**: ✓ "Deep Reinforcement Learning with Double Q-Learning"
- **Venue**: ✓ AAAI 2016
- **正文引用位置**: ✓ related_work.tex 中引用为 Double Q-learning 解决 maximization bias，正确
- **状态**: **OK**

### 14. @inproceedings{fujimoto2018td3}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Fujimoto, Scott; van Hoof, Herke; Meger, David
- **年份**: ✓ 2018
- **标题**: ✓ "Addressing Function Approximation Error in Actor-Critic Methods"
- **Venue**: ✓ ICML 2018
- **正文引用位置**: ✓ related_work.tex (TD3), experiments_results.tex / methodology.tex (dual-critic 引用 TD3)，正确
- **状态**: **OK**

### 15. @inproceedings{lu2018nondelusional}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Lu, T; Schuurmans, D; Boutilier, C（Tyler Lu, Dale Schuurmans, Craig Boutilier）
- **年份**: ✓ 2018
- **标题**: ✓ "Non-delusional Q-learning and Value-Iteration"（LOW: 官方标题为小写 "value-iteration"，BibTeX style 通常自动处理大小写）
- **Venue**: ✓ NeurIPS 2018
- **正文引用位置**: ✓ introduction.tex / related_work.tex / analysis.tex / appendix.tex 中引用为 delusional bias，正确
- **状态**: **OK**（LOW: 标题大小写 "Value-Iteration" → "value-iteration"）

### 16. @inproceedings{biedenkapp2021temporl}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Biedenkapp, A; Rajan, R; Hutter, F; Lindauer, M
- **年份**: ✓ 2021
- **标题**: ✓ "TempoRL: Learning When to Act"
- **Venue**: ✓ ICML 2021
- **正文引用位置**: ✓ related_work.tex 中引用为 action-repetition 方法，正确
- **状态**: **OK**

### 17. @inproceedings{hafner2021dreamerv2}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Hafner, D; Lillicrap, T; Norouzi, M; Ba, J
- **年份**: ✓ 2021
- **标题**: ✓ "Mastering Atari with Discrete World Models"
- **Venue**: ✓ ICLR 2021
- **正文引用位置**: ✓ related_work.tex Dreamer family 列表中，正确
- **状态**: **OK**

### 18. @inproceedings{gumbsch2024thick}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Gumbsch, C; Sajid, N; Martius, G; Butz, M.V
- **年份**: ✓ 2024
- **标题**: ✓ "Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics"
- **Venue**: ✓ ICLR 2024
- **正文引用位置**: ✓ related_work.tex / appendix.tex 中引用为 hierarchical world model (THICK)，正确
- **状态**: **OK**

### 19. @inproceedings{mattes2024hieros}
- **真实性**: ✓ 论文存在（PMLR v235）
- **作者**: ✓ Mattes, P; Schlosser, R; Herbrich, R
- **年份**: ✓ 2024
- **标题**: ✓ "Hieros: Hierarchical Imagination on Structured State Space Sequence World Models"
- **Venue**: ✓ ICML 2024
- **正文引用位置**: ✓ related_work.tex / appendix.tex 中引用为 hierarchical world model，正确
- **状态**: **OK**

### 20. @inproceedings{henderson2018deep}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Henderson, P; Islam, R; Bachman, P; Pineau, J; Precup, D; Meger, D
- **年份**: ✓ 2018
- **标题**: ✓ "Deep Reinforcement Learning that Matters"（LOW: 官方标题 "That" 大写，BibTeX style 自动处理）
- **Venue**: ✓ AAAI 2018
- **正文引用位置**: ✓ related_work.tex 中引用为实验方法论参考（"factorial diagnostic methodology follows Henderson et al."），合理——该论文讨论 RL 实验方法学
- **状态**: **OK**

### 21. @inproceedings{lambert2020objective}
- **真实性**: ✓ 论文存在（arXiv:2002.04523, PMLR v120）
- **作者**: ✓ Lambert, N; Amos, B; Yadan, O; Calandra, R
- **年份**: ✓ 2020
- **标题**: ✓ "Objective Mismatch in Model-based Reinforcement Learning"
- **Venue**: ✓ L4DC (Learning for Dynamics & Control)
- **正文引用位置**: ✓ related_work.tex 中引用为 compounding error / objective mismatch，正确
- **状态**: **OK**

### 22. @inproceedings{agarwal2021precipice}
- **真实性**: ✓ 论文存在（NeurIPS 2021 Outstanding Paper Award）
- **作者**: ✓/~ Agarwal, R; Schwarzer, M; Castro, P.S; Courville, A.C; Bellemare, M（LOW: Bellemare 的 initial 应为 "M.G."，Marc G. Bellemare）
- **年份**: ✓ 2021
- **标题**: ✓ "Deep Reinforcement Learning at the Edge of the Statistical Precipice"
- **Venue**: ✓ NeurIPS 2021
- **正文引用位置**: ✓ experiments_results.tex / results.tex 中引用为 per-seed trajectories / IQM 报告方法，正确
- **状态**: **OK**（LOW: Bellemare, M → Bellemare, M.G.）

### 23. @article{tassa2018dmcontrol}
- **真实性**: ✓ 论文存在（arXiv:1801.00690）
- **作者**: ✓ Tassa, Yuval 等 12 人，正确
- **年份**: ✓ 2018
- **标题**: ✓ "DeepMind Control Suite"
- **Venue**: ✓ arXiv preprint
- **正文引用位置**: ✓ 多处引用为 DMC 环境来源，正确
- **状态**: **OK**

### 24. @article{hafner2025dreamerv4}
- **真实性**: ✓ 论文存在（arXiv:2509.24527，2025年9月提交）
- **作者**: ✓ Hafner, Danijar; Yan, Wilson; Lillicrap, Timothy
- **年份**: ✓ 2025
- **标题**: ✓ "Training Agents Inside of Scalable World Models"
- **Venue**: ✓ arXiv preprint
- **正文引用位置**: ✓ related_work.tex Dreamer family 列表中，正确
- **状态**: **OK**

### 25. @inproceedings{lyle2022capacity}
- **真实性**: ✓ 论文存在（arXiv:2204.09560, ICLR 2022 Spotlight）
- **作者**: ✓ Lyle, C; Rowland, M; Dabney, W
- **年份**: ✓ 2022
- **标题**: ✓ "Understanding and Preventing Capacity Loss in Reinforcement Learning"
- **Venue**: ✓ ICLR 2022
- **正文引用位置**: ✓ appendix.tex 中引用为 capacity loss 参考，正确
- **状态**: **OK**

### 26. @inproceedings{nhu2025tawm}
- **真实性**: ✓ 论文存在（arXiv:2506.08441, ICML 2025）
- **作者**: ✓ Nhu, Anh N.; Son, Sanghyun; Lin, Ming C.
- **年份**: ✓ 2025
- **标题**: ✓ "Time-Aware World Model for Adaptive Prediction and Control"
- **Venue**: ✓ ICML 2025
- **正文引用位置**: ✓ introduction.tex / related_work.tex / appendix.tex 中引用为 TAWM（Δt-conditioning in TD-MPC2），正确
- **状态**: **OK**

### 27. @inproceedings{li2025lsimagine}
- **真实性**: ✓ 论文存在（arXiv:2410.03618, ICLR 2025 Oral）
- **作者**: ✓ Li, J; Wang, Q; Wang, Y; Jin, X; Li, Y; Zeng, W; Yang, X
- **年份**: ✓ 2025
- **标题**: ✓ "Open-World Reinforcement Learning over Long Short-Term Imagination"
- **Venue**: ✓ ICLR 2025
- **正文引用位置**: ✓ related_work.tex / appendix.tex 中引用为 hierarchical imagination variant (LS-Imagine)，正确
- **状态**: **OK**

### 28. @inproceedings{chen2021redq}
- **真实性**: ✓ 论文存在（arXiv:2101.05982）
- **作者**: ✓ Chen, Xinyue; Wang, Che; Zhou, Zijian; Ross, Keith
- **年份**: ✓ 2021
- **标题**: ✓ "Randomized Ensembled Double Q-Learning: Learning Fast Without a Model"
- **Venue**: ✓ ICLR 2021
- **正文引用位置**: ✓ related_work.tex 中引用为 ensemble methods 解决 overestimation，正确
- **状态**: **OK**

### 29. @inproceedings{bacon2017optioncritc}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Bacon, Pierre-Luc; Harb, Jean; Precup, Doina
- **年份**: ✓ 2017
- **标题**: ✓ "The Option-Critic Architecture"
- **Venue**: ✓ AAAI 2017
- **正文引用位置**: ✓ related_work.tex 中引用为 option-critic，正确
- **状态**: **OK**

### 30. @inproceedings{buckman2018steve}
- **真实性**: ✓ 论文存在（arXiv:1807.01675）
- **作者**: ✓ Buckman, Jacob; Hafner, Danijar; Tucker, George; Brevdo, Eugene; Lee, Honglak
- **年份**: ✓ 2018
- **标题**: ✓ "Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion"
- **Venue**: ✓ NeurIPS 2018
- **正文引用位置**: ✗ **未在任何 .tex 文件中引用**
- **状态**: **有问题 (MEDIUM)** — bib entry 存在但从未被 \cite 引用，属于多余条目

### 31. @inproceedings{chua2018pets}
- **真实性**: ✓ 论文存在（arXiv:1805.12114）
- **作者**: ✓ Chua, Kurtland; Calandra, Roberto; McAllister, Rowan; Levine, Sergey
- **年份**: ✓ 2018
- **标题**: ✓ "Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models"
- **Venue**: ✓ NeurIPS 2018
- **正文引用位置**: ✗ **未在任何 .tex 文件中引用**
- **状态**: **有问题 (MEDIUM)** — bib entry 存在但从未被 \cite 引用，属于多余条目

### 32. @article{bishop1995noise}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Bishop, Chris M.
- **年份**: ✓ 1995
- **标题**: ✓ "Training with Noise is Equivalent to Tikhonov Regularization"
- **Venue**: ✓ Neural Computation, vol 7, no 1, pp 108–116
- **正文引用位置**: ✓ related_work.tex 中引用为 training-with-noise 理论基础（TCN intervention），正确
- **状态**: **OK**

### 33. @inproceedings{fortunato2018noisynet}
- **真实性**: ✓ 论文存在（arXiv:1706.10295）
- **作者**: ✗ **缺少作者 Matteo Hessel**（实际 13 人，bib 中仅 12 人）。此外 "Vlad" Mnih 应为 "Volodymyr" Mnih。
- **年份**: ✓ 2018
- **标题**: ✓ "Noisy Networks for Exploration"
- **Venue**: ✓ ICLR 2018
- **正文引用位置**: ✗ **未在任何 .tex 文件中引用**
- **状态**: **有问题 (HIGH/MEDIUM)** — 作者列表缺人且从未被引用。建议直接删除此条目。

### 34. @inproceedings{parr1998ham}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Parr, Ronald; Russell, Stuart
- **年份**: ✗ **year=1998，但会议是 NIPS 1997**（1997年12月举办）。NIPS 10 proceedings 由 MIT Press 1998 年出版。DBLP 和多数数据库记录为 1997。建议改为 1997。
- **标题**: ✓ "Reinforcement Learning with Hierarchies of Machines"
- **Venue**: ✓ Advances in Neural Information Processing Systems (NIPS)
- **正文引用位置**: ✓ related_work.tex 中引用为 HAM，正确
- **状态**: **有问题 (HIGH)** — year 应改为 1997

### 35. @article{dietterich2000maxq}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Dietterich, Thomas G.
- **年份**: ✓ 2000
- **标题**: ✓ "Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition"
- **Venue**: ✓ Journal of Artificial Intelligence Research, vol 13, pp 227–303
- **正文引用位置**: ✓ related_work.tex 中引用为 MAXQ，正确
- **状态**: **OK**

### 36. @inproceedings{bradtke1995smdp}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Bradtke, Steven J.; Duff, Michael O.
- **年份**: ✓ 1995（NIPS 1994 会议，proceedings 1995 出版；1995 可接受）
- **标题**: ✓ "Reinforcement Learning Methods for Continuous-Time Markov Decision Problems"
- **Venue**: ✓ Advances in Neural Information Processing Systems
- **正文引用位置**: ✓ related_work.tex 中引用为 semi-MDP theory 数学基础，正确
- **状态**: **OK**

### 37. @inproceedings{kidambi2020morel}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Kidambi, Rahul; Rajeswaran, Aravind; Netrapalli, Praneeth; Joachims, Thorsten
- **年份**: ✓ 2020
- **标题**: ✓ "MOReL: Model-Based Offline Reinforcement Learning"
- **Venue**: ✓ NeurIPS 2020
- **正文引用位置**: ✓ related_work.tex 中引用为 model uncertainty penalization，正确
- **状态**: **OK**

### 38. @inproceedings{yu2021combo}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Yu, Tianhe; Kumar, Aviral; Rafailov, Rafael; Rajeswaran, Aravind; Levine, Sergey; Finn, Chelsea
- **年份**: ✓ 2021
- **标题**: ✓ "COMBO: Conservative Offline Model-Based Policy Optimization"
- **Venue**: ✓ NeurIPS 2021
- **正文引用位置**: ✓ related_work.tex 中引用为 model uncertainty penalization，正确
- **状态**: **OK**

### 39. @inproceedings{hamrick2021planning}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Hamrick, Jessica B. 等 10 人，正确
- **年份**: ✓ 2021
- **标题**: ✓ "On the Role of Planning in Model-Based Deep Reinforcement Learning"
- **Venue**: ✓ ICLR 2021
- **正文引用位置**: ✓ related_work.tex 中引用为 decision-aware model learning，合理
- **状态**: **OK**

### 40. @inproceedings{wu2023daydreamer}
- **真实性**: ✓ 论文存在（arXiv:2206.14176）
- **作者**: ✓ Wu, Philipp; Escontrela, Alejandro; Hafner, Danijar; Abbeel, Pieter; Goldberg, Ken
- **年份**: ✓ 2023（CoRL 2022 会议，PMLR v205 于 2023 年出版；2023 可接受）
- **标题**: ✓ "DayDreamer: World Models for Physical Robot Learning"
- **Venue**: ✓ Conference on Robot Learning
- **正文引用位置**: ✓ introduction.tex 中引用为 world-model RL sample-efficient 代表，正确
- **状态**: **OK**

### 41. @inproceedings{park2021timediscretization}
- **真实性**: ✓ 论文存在（arXiv:2111.03941）
- **作者**: ✓ Park, Seohong; Kim, Jaekyeom; Kim, Gunhee
- **年份**: ✓ 2021
- **标题**: ✓ "Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods"
- **Venue**: ✓ NeurIPS 2021
- **正文引用位置**: ✓ related_work.tex 中引用为 action-repetition 补充方法，正确
- **状态**: **OK**

### 42. @article{wang2024elastic}
- **真实性**: ✓ 论文存在（arXiv:2402.14961）
- **作者**: ✓ Wang, Dong; Beltrame, Giovanni
- **年份**: ✓ 2024
- **标题**: ✓ "Reinforcement Learning with Elastic Time Steps"
- **Venue**: ✓ arXiv preprint
- **正文引用位置**: ✓ related_work.tex 中引用为 elastic time steps 方法，正确
- **状态**: **OK**

### 43. @article{colas2018seeds}
- **真实性**: ✓ 论文存在（arXiv:1806.08295）
- **作者**: ✓ Colas, Cédric; Sigaud, Olivier; Oudeyer, Pierre-Yves
- **年份**: ✓ 2018
- **标题**: ✓ "How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments"
- **Venue**: ✓ arXiv preprint
- **正文引用位置**: ✓ conclusion.tex (limitations) 中引用为 seed count 参考，正确
- **状态**: **OK**

### 44. @article{benechehab2023multitimestep}
- **真实性**: ✓ 论文存在（arXiv:2310.05672）
- **作者**: ✓ Benechehab, Abdelhakim; Paolo, Giuseppe; Thomas, Albert; Filippone, Maurizio; Kégl, Balázs
- **年份**: ✓ 2023
- **标题**: ✓ "Multi-timestep models for Model-based Reinforcement Learning"
- **Venue**: ✓ arXiv preprint
- **正文引用位置**: ✓ related_work.tex 中引用为 multi-timestep world models，正确
- **状态**: **OK**

### 45. @inproceedings{hafner2022director}
- **真实性**: ✓ 论文存在
- **作者**: ✓ Hafner, Danijar; Lee, Kuang-Huei; Fischer, Ian; Abbeel, Pieter
- **年份**: ✓ 2022
- **标题**: ✓ "Deep Hierarchical Planning from Pixels"
- **Venue**: ✓ NeurIPS 2022
- **正文引用位置**: ✓ related_work.tex 中引用为 Dreamer hierarchical variant (Director)，正确
- **状态**: **OK**

---

## 需要修复的问题

### HIGH — 必须修复

| # | Entry | 问题 | 修复方案 |
|---|-------|------|----------|
| 7 | `pertsch2020spirl` | year=2021，实际为 CoRL 2020 | 改 `year = {2020}` |
| 34 | `parr1998ham` | year=1998，实际为 NIPS 1997 | 改 `year = {1997}` |

### MEDIUM — 建议修复

| # | Entry | 问题 | 修复方案 |
|---|-------|------|----------|
| 30 | `buckman2018steve` | 从未被 \cite 引用 | 删除此 bib entry 或在正文中补充引用 |
| 31 | `chua2018pets` | 从未被 \cite 引用 | 删除此 bib entry 或在正文中补充引用 |
| 33 | `fortunato2018noisynet` | 从未被 \cite 引用 + 作者缺 Matteo Hessel + "Vlad"→"Volodymyr" | 删除此 bib entry（如需保留则修复作者） |

### LOW — 可选修复

| # | Entry | 问题 | 修复方案 |
|---|-------|------|----------|
| 5 | `hafner2023dreamerv3` | bib key "2023" 与 year=2025 不一致 | 可更新 key 为 `hafner2025dreamerv3`（需同步所有 \cite） |
| 15 | `lu2018nondelusional` | 标题 "Value-Iteration" 应为 "value-iteration" | 用 BibTeX 大括号保护或修正大小写 |
| 22 | `agarwal2021precipice` | Bellemare 的 initial "M" 应为 "M.G." | 改为 `Bellemare, M.G.` 或 `Bellemare, Marc G.` |

---

## 审计结论

- **全部 45 条引用均为真实论文**，无幻觉引用
- **正文中所有 citation 归因正确**，无张冠李戴
- **2 条年份错误**需要修复（pertsch2020spirl, parr1998ham）
- **3 条 bib entry 未被引用**（buckman2018steve, chua2018pets, fortunato2018noisynet），建议清理
- 其余均为 minor 格式问题（初始名缩写、大小写等），不影响学术正确性
