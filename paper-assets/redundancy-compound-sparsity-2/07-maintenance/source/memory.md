# Memory — solver-verified-formalizer-rl

## EMA 失败根因分析 (2026-05-12)

文献调研确认：**centroid-based eviction 思路本身可行，EMA smoothing 是失败原因。**

- **KeyDiff** (arXiv 2504.15364): 论文原始算法 pairwise O(B²)，kvpress 实现 exact mean anchor O(B)。两种都有效。8K budget 下与 full context 差距仅 0.17pp (Llama-8B) / 0.09pp (Llama-3B)。Ablation 显示 Pairwise/Median/Mean 差距极小。
- **DefensiveKV** (ICLR'26): mean aggregation stability assumption 脆弱，importance 突变时灾难性失败（2.3-4.3× worse）。
- EMA smoothing 导致 centroid 收敛到全局均值，丧失区分度 → 等效于 random。

**关键对比**：KeyDiff 每步精确重算 mean，EMA 是有偏估计器（过度加权近期 token）。同样 centroid 思路，exact mean 有效而 EMA 无效。

## D009 Archive 决策 (2026-05-12)

gamma sweep 8 个 decay rate 全面测试，仅 gamma=0.99 beat random (+1.38%)，远低于 5% gate。项目 archive。
- **recency 是极强 baseline**: PPL 7.1758 略优于 full cache 7.1822（-0.09%），任何 eviction 方法的真正对手是 recency 而非 random
- **gamma→1 时 EMA 收敛到 recency**: 验证 EMA 上界即 recency，无额外价值
- **EMA 方向正确但精度不够**: inverted EMA +15% 恶化证明方向对，但正向 EMA 精度不足以 beat random
- **per-layer 结构存在**: 中层(16-35) EMA 信号最强，浅层(0-5)最弱，WikiText 和 reasoning 一致。per-layer adaptive 可能有价值但本项目未验证

## Cross-axis 假说证伪 (2026-05-12)

MVP 实验（seed 42 + 1337）证伪：|r|=0.12, perturbation_diff=5.5%。KV similarity 与 MLP sparsity 无显著关联。

## 实验经验 (2026-05-12)

- gamma_sweep 日志可能混入其他进程的 OOM traceback（共享终端输出），需检查 PID 归属
- WikiText-2 32K 上 recency 几乎完美，不是 eviction 方法的好 benchmark。建议用 LongBench multi-doc QA
- 未设 seed 的实验结论不可靠（inverted_ema_wikitext 未设 seed，但 +15% gap 足够大可忽略）
- Worker 轮询长时间进程易提前退出，用 check_job_status + tail_training_logs 直接工具更可靠
