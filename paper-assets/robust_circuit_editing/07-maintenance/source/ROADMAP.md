# robust_circuit_editing — Research Dashboard

> 最后更新: 2026-05-16 07:31 UTC | 更新原因: Reviewer WARNING: 补 post-MVP pass/fail 分支骨架 + 同步 mvp_001 PREPARING 状态

## 核心方向
跨方法二值共识（MNC/CSS）用于鲁棒电路编辑：二值稳定性评分在分布偏移下优于得分平均。核心 insight：binary presence/absence 是所有电路发现算法族唯一可比的信号，无需校准对齐。详见 paper_framing.md（待创建）。

## 当前进展
- **阶段**: MVP 验证
- **目标会议**: EMNLP 2026 Main（ARR 截止 2026-05-25，剩 9 天）
- **实验**: mvp_001_cross_method_consensus (PREPARING) — 环境搭建中，2 Workers 并行（SSH 环境 + 文献调研）
- **关键待验证假设**: CIRCUS-core (s=1) 中 CSS < 0.75 的边 ≥10% AND ≥10 条

## 近期任务
- [ ] Agent 补全 mvp_001 registry spec（命令、服务器、数据路径、模型 ID、种子、IOI 构造方式）
- [ ] 环境搭建完成：rtx6000-diagprobe 上 TransformerLens + ACDC + AtP* 验证通过
- [ ] 优先验证 ACDC 和 AtP* 在 GPT-2 Small / IOI 上可跑通
- [ ] MVP 实验：K=4 方法 pilot → CSS + CIRCUS config-bagging
- [ ] 交叉表 CIRCUS-stability × CSS → 判断 off-diagonal ≥10% AND ≥10 条
- [ ] MVP 判定

## Post-MVP 分支骨架

### Pass 路线（off-diagonal ≥10% AND ≥10 条）
1. **扩模型**: GPT-2 Medium → GPT-2 Large → Pythia-1.4B（同 decoder-only 家族，验证 scale 效应）
2. **扩任务**: IOI → Greater-Than → Docstring（验证 task 泛化性）
3. **OOD 变体**: template perturbation / name distribution shift / position shuffle
4. **Ablation**: K 值敏感性（K=3,4,5,6）、bagging B 值（B=5,10,20）、threshold 敏感性
5. **Baseline 对比**: 得分平均 vs 二值共识 vs 单方法最优，三者在 OOD 下的稳定性对比
6. 写 paper_framing.md → experiment_plan.yaml → dream_simulate → 进入 research 阶段

### Fail 路线（off-diagonal < 10% 或 < 10 条）
1. **Reframe**: 从 "二值共识更鲁棒" 转向 "跨方法一致性 taxonomy"
2. **分析实验**: 方法间 agreement heatmap、per-edge method signature clustering
3. **Story**: "电路发现方法在哪些边上达成共识、在哪些边上分歧" → empirical taxonomy paper
4. **扩展**: 多模型/多任务下 taxonomy 是否稳定
5. 写 paper_framing.md（taxonomy 版）→ 重新评估投稿目标

## GPU 预算
- 本地：rtx6000-diagprobe 2×RTX 6000（cuda:0, cuda:1）
- 总预算上限：200 H100-hours（~290h A100）
- MVP 预计：~2-4h RTX 6000

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D002 | 2026-05-16 | MVP gate 补充绝对下限：off-diagonal ≥10% AND ≥10 条边 | — |
| D001 | 2026-05-16 | MVP 方案：GPT-2 Small / IOI 上 K=4 方法 pilot，pass/fail  | — |


