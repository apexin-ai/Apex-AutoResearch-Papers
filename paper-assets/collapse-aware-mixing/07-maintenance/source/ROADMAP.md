# collapse-aware-mixing — Research Dashboard

> 最后更新: 2026-05-13 23:49 UTC | 更新原因: D018: MVP FAIL, 三条路径全封，待用户决策

## 核心方向
Spectral effective rank 作为 model collapse 的 leading indicator → PI 控制器动态调节 real/synthetic mixing ratio。详见 paper_framing.md。

**❌ MVP FAIL (D018)**：三条路径全封，核心假设在 MVP 阶段未通过验证。

## 当前进展

**阶段**: MVP FAIL — 待决策（Q2 negative result 或 archive）

### 三条路径总结
1. **C1 holdout eff_rank** (D014): FALSIFIED — eff_rank 在 collapse 中反向上升 +0.96%，与 collapse 完全解耦
2. **Pivot B generated eff_rank** (D018): NO ADVANTAGE — 与 n-gram entropy 同时检测(G1 step 152)，噪声高 573 倍
3. **Direction C per-layer** (D016): DEAD — 所有层变化 <1%

### 核心发现（有价值的 negative result）
- Holdout spectral eff_rank 与 mode collapse 完全解耦：模型生成崩塌到 1 个 unique token 时，holdout eff_rank 反而上升
- Generated eff_rank 能检测 collapse 但不优于简单 n-gram entropy baseline
- 挑战了 SIGMA 等工作中"谱分析可监测 collapse"的隐含假设

## 待决选项

### Q2: Negative Result Paper
- **目标**: EMNLP 2026 Findings
- **核心贡献**: "holdout spectral effective rank rises during mode collapse" — 挑战谱监测假设
- **需补实验**: multi-seed (3 seeds) + multi-scale (Pythia-410M/2.8B)
- **成本**: ~3-4 天 GPU
- **风险**: Findings 接受率对 negative results 不确定

### Archive
- 释放 GPU 给更有前景的项目

## GPU 预算

| 资源 | 状态 |
|------|------|
| 1× RTX PRO 6000 (cqa1-38874) | 当前空闲，无 RUNNING 实验 |

## 近期任务

- [x] pivot_b_full_18ckpt 完成，确认 Pivot B 失败
- [ ] 等待用户决策：Q2 或 archive

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D019 | 2026-05-14 | 用户决策：归档项目，释放 GPU，从 Passed Ideas 重新立项 | mvp_seed0_replication_r2 |
| D018 | 2026-05-13 | MVP 最终判定 FAIL：三条路径全封（C1 falsified, Pivot B no adva | pivot_b_full_18ckpt, pivot_b_verification, mvp_pilot_v7 |
| D017 | 2026-05-13 | D013 存活条件 (a)(c) 未满足；启动 Option 1 细粒度 checkpoint 验证 | pivot_b_full_18ckpt |
| D016 | 2026-05-13 | Pivot B 核心信号确认 GO；Direction C KILLED；需全 checkpoint | pivot_b_verification |
| D015 | 2026-05-13 | Pivot B 失败预案：Q2 (negative result) 为首选保底，Q1 (multi- | — |
| D014 | 2026-05-13 | C1 原假设 definitively falsified by G2 data；立即启动 Pivo | mvp_pilot_v7 |
| D013 | 2026-05-13 | Pivot B 核心风险：generated eff_rank 必须证明比 n-gram entro | mvp_pilot_v7 |
| D012 | 2026-05-13 | Pivot 策略：B（生成文本 eff_rank）为首选，C（分层）并行验证，A（n-gram en | mvp_pilot_v7 |
| D011 | 2026-05-13 | v7 G1 数据：eff_rank 上升 +1.34 而非下降，核心假设 C1 面临挑战。等 G2  | mvp_pilot_v7 |
| D010 | 2026-05-13 | P0 补充：+3-seed 验证 + w=0.1 baseline + PI sweep 选择标准定 | mvp_pilot_v7 |

