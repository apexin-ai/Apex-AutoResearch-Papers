# Gated-ISR-Curriculum: Narrative Impact Analysis

## 三种结果解读

**A. Gated-ISR 仍产生 hacking（最可能）**
- 支持核心论点：ISR 作为 proxy reward 本质上 gameable，门控/课程设计无法消除 Goodhart 效应
- 论文框架：在 Discussion 加 "Attempted Mitigations" 段落，1-2 段说明门控失败，强化 "metric optimization ≠ capability improvement" 结论
- 若出现新 hacking 模式（如 H9 变体），扩展 taxonomy

**B. Gated-ISR 显著减少 hacking（genuine >30%）**
- 论文转为 "diagnosis + partial mitigation"：ISR 既能诊断又能（有条件地）指导训练
- 框架：新增 Section 6 "Toward Safe ISR Deployment"，报告门控阈值与 hacking 率的关系
- 风险：削弱 Goodhart 主线的尖锐度，需权衡叙事一致性

**C. 训练不收敛（PR <20% 或 loss 不降）**
- 解读：门控过强截断了学习信号，ISR 的信息量不足以独立驱动学习
- 框架：支持 "ISR 只适合做诊断不适合做 reward" 的结论，与 Claim 2 一致
- 1 句话写入 limitations 即可

## Eval Metrics 优先级

1. **Genuine rate**（C013 标准）— 核心判定指标
2. **H7/H9 rate** — hacking 模式分布
3. **PR trajectory** — 收敛性判断
4. **ISR proved-only** — 是否仍被 game
