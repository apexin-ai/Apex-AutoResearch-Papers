# Memory — ec_hte_llm_annotation

## 研究发现

### 非对称诊断等价性 (2026-05-23, Worker A)
对 K_Z=2（二值标签），非对称诊断公式 |B_s[1,1] - B_s[1,0]| / (FPR_s + FNR_s) 恒等于对称公式 |δ_s| / ((1-2π̄)·π_s)。FPR/FNR 不对称性在行差中完全抵消。AUC=0.63 的真正原因是 τ_s=0 子组的 MC 噪声，排除后 AUC=1.0。

### Centered EB 优于 Dir(α/2, α/2) (2026-05-23, Worker C)
原始 HB 用 Dir(α/2, α/2) 向 (0.5, 0.5) 收缩是错误目标。Centered EB 向 global CM 收缩，在 moderate heterogeneity 下 RMSE ≈ Global（消除弱点），在 extreme 下 RMSE < Global < original HB。K4 extreme 下 original HB RMSE > Global 的问题也被修复。

### Bootstrap SE 在小 n_expert 下的表现 (2026-05-23, Task G)
DIM + Centered EB, K=2 extreme (π=[0.05,0.25]), 20 MC × B=100。Bootstrap coverage 在所有 n_expert ≥25 下均达 nominal (≥95%): n=25→100%, n=50→98.8%, n=75→97.5%, n=100→96.3%, n=200→95.0%。Plug-in SE 在 n≥50 时 ≥92.5%，最弱点 n=75 (91.2%)。高误差子群 s1 (π=0.25) 是 bootstrap 的主要受益者。数据: results/exp_bootstrap_small_n_summary.csv

### UCB Annotator Demographics Δπ 不足 (2026-05-24)
UCB Hate Speech 135K行数据，7个 annotator demographic features + 交互特征。最大 Δπ = 0.117（race × ideology），单一特征最大 0.084（education）。根因：GPT-4.1 的主要错误模式是 FNR ≈ 0.55（漏检 hate speech），这在所有 demographic 组中高度一致。Δπ 来自次要效应（如保守派 π≈0.39 vs 自由派 π≈0.35），幅度不够。即使用虚高 Δπ=0.23 跑 semi-synthetic，correction 因 1-FPR-FNR ≈ 0.28 放大噪声，全面劣于 naive。**结论：annotator demographics 维度的异质性不足以支撑 EC-HTE real-data 成功案例，且高 FNR 使 CM inversion 本身不稳定。这是 task-level 的结构性限制，非 subgroup 选择问题。**

## 决策记录

### API 模型版本 (已验证)
- GPT-4.1: `gpt-4.1-2025-04-14`
- GPT-5.4: `gpt-5.4` (reasoning model, 慢, ~1min/call)
- GPT-5.5 不可用（reasoning tokens 消耗 max_tokens budget）

### 论文写作
- EMNLP 2026 DDL: 2026-05-25 (ARR)
- 8 页主文限制，Limitations/References 不计入
- R15 审稿修复已全部完成（8 项，2026-05-23）
- Messing (2026) 已加入 Related Work
- 数据完整性审计完成：AUC=0.86 确认正确（Δπ-only diagnostic），AUC=0.82→0.66 已修复（3处），74-82% coverage 确认正确
- 匿名代码仓库已推送: https://github.com/anonymous-nlp-2026-2/ec_hte_llm_annotation (74 files, commit 5b722d5)

### 实验边界条件
- K=8 是 scalability boundary：coverage 95.6% 但 RMSE > Global
- 分类器质量阈值：任一子群 FNR≈0.5 时 CM 反转放大噪声（exp-015, exp-004 确认）
- 预算阈值：n_expert/K ≥ 25 per subgroup，K=4 时 n_expert ≥ 100
- Class imbalance: P(Z=1)=0.18 + K=4 → per-subgroup Z=1 labels 不足，EC-HTE 失效（exp-015, exp-016）
