## Paper Data Gap Analysis (2026-05-19)

### Claim 1: Direction discriminability + stability — 🟢 LOW risk
- exp-001 (DONE, success): AUROC 0.827, per-strength breakdown
- exp-002v2 step 500 stability: cosine≈0.96
- 缺口：完整训练曲线 stability 只有 1 个数据点，需 exp002v2-recalib 补充

### Claim 2: DC-GRPO effectiveness — 🔴 CRITICAL
- 0 个已完成实验有有效 R1 信号
- exp-002v3 (scaled cosine, PREPARING) 是唯一能验证的实验，需 ~52h
- baselines 在跑：exp-003 (May 21), exp-004 (今晚), exp-008v3 (May 22)
- 无 seed 复现，无 eval 结果

### Claim 3: R1-R3 disagreement — 🟡 depends on Claim 2
- 完全依赖 DC-GRPO 训练日志

### Baselines gap: 缺 SMART/BCT, 缺第二个 model family

### Timeline: exp-002v3 必须今晚启动，May 22 完成训练，May 23 eval，剩 2 天写论文
