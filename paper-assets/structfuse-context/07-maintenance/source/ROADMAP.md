# StructFuse — Research Dashboard

> 最后更新: 2026-05-16 06:33 UTC | 更新原因: Reviewer 修正：pool=8→pool=50 数据、标注 D061 superseded、补充遗漏风险

## 核心方向
Hard negative mining strategy comparison for contrastive code retrieval: random vs embedding_distance vs dataflow_aware vs BM25, across 3 encoder architectures. Dual-track narrative (D059): A=stratified heterogeneity reveals when mining helps, B=explain why aggregate deltas are small. 详见 paper_framing.md。

## 当前进展
- **阶段**: Research（post-MVP）+ 审稿进行中
- **Qwen (cuda:0)**: 主链完成中，watcher PID 966920 就绪 → 自动触发 s42 supplement (embed+dataflow+bm25)
- **StarCoder (cuda:1)**: embedding_s42 之后还有 embed_s43/s44 + dataflow×3。ETA ~May 19-20
- **UniXcoder**: 3-strat s42 训练中（PID 149872, step 400+, R@1@200=0.5245）。Registry 待修复为 RUNNING
- **BM25 Phase 1**: ✅ 已完成（索引+挖掘）。Phase 2 watcher 就绪
- **D062 query split**: Workers 失败两次（rate/context limit），待重派。**阻塞 Claim 2 全部进展**
- **写作**: Intro/Method/Related/Conclusion v1 ✅ | Abstract v2 + Experiments v1 修复中

## ⚠️ Claim 1 Delta 状况 — Pool=50 数据（D060 确认 pool=8 不可靠）
| seed | checkpoint | random R@1 | embed R@1 | Δ |
|------|-----------|-----------|-----------|---|
| s43 | by_val_loss | 0.3138 | 0.3331 | **+1.93pp** ✓ |
| s44 | by_val_loss | 0.3181 | 0.3694 | **+5.13pp** ��� |
| s43 | by_R@1 | 0.3829 | 0.3897 | +0.68pp |
| s44 | by_R@1 | 0.3181 | 0.3171 | -0.10pp |
| s42 | — | — | **缺失** | — |

- **by_val_loss 下两 seed 均 embed > random**，信号正面
- **Checkpoint 选择标准是核心方法论问题**：D061 (统一 val_loss) 已被 D062 (query split) supersede
- **翻盘路径**: D062 实现 → 统一 checkpoint selection → embed_s42 补完 → bootstrap CI

## 实验缺口补充计划 (D063, May 16)
| Priority | 实验 | 耗时 | 状态 | 触发条件 |
|----------|------|------|------|----------|
| **P0** | D062 pool=50 re-eval (query split) | 2h | **Worker 失败×2，重派中** | 立即 |
| **P0** | RepoBench-R eval (plan_004) | 5h | 就绪 | 立即启动 |
| **P0** | Pool sensitivity (plan_019) | 5h | 就绪 | 立即启动 |
| **P0** | BM25 Phase 2 训练 (plan_018) | 15h | Watcher 就绪 | Qwen/SC 完成后自动 |
| **P0** | 分层分析 (plan_005) | 分析 | 就绪 | D062 pool=50 后 |
| **P1** | UniXcoder multi-seed (s43, s44) | 20h | 新增 plan_020 | s42 完成后 |
| **P1** | 温度 ablation 缩减 (τ=0.05,0.2 × Qwen) | 15h | 新增 plan_021 | GPU 空闲时 |
| **P1** | random_s42 retrain (统一 regime) | 10h | 已派 Agent | — |

## 时间预算
- **bjb1-42106**: 2× RTX PRO 6000 96GB
- **可用**: 9天 × 24h × 2GPU = 432 GPU·h
- **已占用**: ~100h (运行中训练)
- **新增 must-do**: ~42h | should-do: ~35h
- **总计 ~177h，余量充足**

## 关键路径
```
Qwen主链完成 → s42 supplement (18h) → BM25 P2 自动触发
              ↘ pool=50 re-eval → stratified analysis + bootstrap CI
D062 修复 → pool=50 query split 实现 ↗
RepoBench-R + Pool sensitivity → 立即并行启动（用已有 checkpoint）
UniXcoder s42 完成 → s43/s44 → 跨架构统计
StarCoder chain → May 19-20 全部完成
```

## 近期任务
- [ ] **D062 重派 Worker**（已失败两次，阻塞 Claim 2）
- [ ] RepoBench-R 立即启动（已有 Qwen s42/s43/s44 checkpoints）
- [ ] Pool sensitivity 立即启动
- [ ] UniXcoder registry 修复为 RUNNING
- [ ] Qwen 主链完成 → 验证 watcher 触发 supplement
- [ ] random_s42 retrain（已在 Agent 队列）
- [ ] Qwen 全量完成后 → D062 pool=50 + stratified + bootstrap CI
- [ ] 温度 ablation 缩减版排期

## 覆盖率
- Claim 1: pool=50 eval 已跑部分（Qwen 12 ckpt + StarCoder 8 ckpt），但 D062 query split 未实现前数据不能作为最终结论
- Claim 2: **0/3 done** — plan_005 blocked on D062。⚠️ 这是 dual-track B 的核心，完全无定量数据
- Claim 3: 1/1 done ✅

## 关键风险
1. **D062 连续失败**: 阻塞 checkpoint selection + Claim 2 stratified analysis + bootstrap CI——整条 post-M2 分析链
2. **StarCoder embedding < random (pool=50 确认, -1.9pp)**: Claim 1 跨架构泛化受挑战。Paper 需 qualify 为 encoder-dependent 或靠 UniXcoder 扳回
3. **Checkpoint 选择标准矛盾**: val_loss vs pool=8 R@1 给出相反结论，D062 (query split) 是唯一可靠解法
4. **Claim 2 覆盖率 0%**: Dual-track narrative B 支柱完全无实验数据，plan_005 + neg_difficulty 分析全部依赖 D062
5. **UniXcoder 只有 1 seed**: 无法做统计检验，需补 s43/s44（plan_020）
6. **ARR May 25**: 9 天完成所有补充实验 + 论文定稿

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D066 | 2026-05-16 | D066: D062 eval 8/14 失败（adapter format bug），16.3pp | d062_qwen_query_split_eval |
| D065 | 2026-05-16 | D065: Checkpoint selection criterion effect (+16.3 | d062_qwen_query_split_eval |
| D064 | 2026-05-16 | D064: UniXcoder s42 null result (Δ<0.4pp) 支撑 Track | unixcoder_3strat_s42, plan_020 |
| D063 | 2026-05-16 | D063: 实验缺口补充——新增 plan_020 (UniXcoder multi-seed) + | plan_020, plan_021, plan_004, plan_019 |
| D062 | 2026-05-16 | D062: Checkpoint 选择采用方案 2——从 2980 val queries 分出 5 | m2_full_qwen_continued, plan_005_stratified |
| D061 | 2026-05-16 | D061: pool=50 eval 首批结果——统一用 best_by_val_loss 选 ch | m2_full_qwen_continued, m2_full_starcoder_resumed |
| D060 | 2026-05-16 | D060: in-training eval R@1 不可靠（val negative 非确定性 ± | m2_full_qwen_continued, plan_005_stratified |
| D059 | 2026-05-15 | 确认 A/B 双轨叙事策略：A=stratified 揭示异质性，B=B1+Claim2 hybri | m2_full_qwen_continued, m2_full_starcoder_resumed, plan_005_stratified |
| D058 | 2026-05-15 | D057 trajectory 发现重新定位：从 Claim 2 evidence 降级为 §4.3 | m2_full_qwen_continued |
| D057 | 2026-05-15 | embed_s44 展示 R@1/val_loss 指标分歧：R@1 峰值 step 500 而 v | m2_full_qwen_continued |

