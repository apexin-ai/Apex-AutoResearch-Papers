文献调研完成，覆盖 25+ 篇论文，4 个方向核心发现：

**方向 1 (Self-Verification)**: 纯 intrinsic self-correction 不可靠（Huang et al. survey），>90% self-verification 是冗余确认（Self-Verification Dilemma, 2026）。支持 B-IAVR 的 selective verification 设计。

**方向 2 (Agent RL)**: GiGPO (NeurIPS 2025)、SPEAR (ICLR 2026)、WebAgent-R1 (EMNLP 2025) 是主要 agent RL 训练方法。Self-Guide (2604.03098) 是 B-IAVR 的直接前驱。所有方法只优化任务成功率，不考虑 verification cost。

**方向 3 (Selective Verification)**: 最近的竞争者是 Derailer-Rerailer (ACL 2025, 但限于 reasoning chains)、ARES (2026, SFT-trained effort router)、Sherlock (Microsoft, workflow-level offline analysis)。没有工作在 interactive agent 设定下用 RL 训练 verification trigger。

**方向 4 (ALFWorld)**: 当前 SOTA 是 ReflAct 93.3% (prompting) 和 ReAct-Finetune 96% (finetuned)。ALFWorld 成功率接近饱和，B-IAVR 的价值在 cost-efficiency 而非 peak accuracy。

**Novelty claim 成立**：selective verification + RL-trained trigger + interactive agent + action-change signal 的交叉点是全新的。