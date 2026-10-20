# schema-conform-ie-training — Research Dashboard

> 最后更新: 2026-05-12 07:46 UTC | 更新原因: Reviewer 审查反馈：加 base model baseline (C)、ACE2005 RE in-domain 指标、灰区规则

## 核心方向
用 GRPO + 分解式 schema-conformance rewards 训练 Qwen3.5-9B，使模型学会 schema 验证程序（而非 schema 知识），实现零样本 IE 迁移。核心洞察：RL 训 verification 元技能可从少量 schema 泛化（~13 types），无需 KnowCoder 式 30K+ types SFT。详见 IDEA_BRIEF.md。

## 当前进展
- 阶段: **MVP 验证**
- 实验: 0 / 服务器未配置 / Agent 正在写代码
- DDL: EMNLP 2026 ARR May 25（剩余 13 天）

## MVP 验证方案（v2，含 Reviewer 修订）

**核心假设**: 分解式 schema-conformance rewards 能提升零样本 IE 迁移性能（vs gold-label-only GRPO）

**对比组**:
- (A) GRPO + F1 reward only（gold-label baseline）
- (B) GRPO + F1 + 4 schema-conformance rewards（GDPO normalization）
- (C) Qwen3.5-9B base model zero-shot（sanity check，防 catastrophic forgetting）

**评估指标**:
- In-domain: ACE2005 NER F1 + **RE F1**（确认 relational constraint reward 生效）
- Zero-shot: CrossNER（politics, science）NER F1

**Pass 标准**:
- CrossNER zero-shot: B ≥ A + 2 F1 points
- ACE2005 in-domain: B 的 NER/RE F1 降幅 ≤ 3pp vs A
- Sanity: A 和 B 的 zero-shot 不低于 C（base model）

**灰区规则**:
- 1 ≤ Δ < 2 F1 → 允许 1 天调参（lr / reward weights），最终须 ≥ 2 才 pass
- In-domain 降 2~3pp → 调查原因但不立即 kill
- Reward hacking（conformance ≈ 1.0 但 F1 << A）→ early stop，审查 reward 设计

**Kill 条件**:
- Zero-shot 无改善或下降 + 调参后仍无改善 → kill
- A 和 B 均显著低于 C（catastrophic forgetting）→ 方向需重审

**时间**: 2-3 天 | **GPU**: ~20h A100-80GB

## 近期任务
- [x] 配置 GPU 服务器 → seetacloud-westb-2xpro6000 (2x RTX PRO 6000 96GB)
- [x] 实现 5-component reward 函数
- [x] 准备 CrossNER 数据集 + schema 定义 → scierc/crossner_politics/crossner_science
- [x] 配置 GRPO 训练脚本（TRL + GDPO）
- [x] 实现 base model zero-shot 推理脚本 → src/inference_base.py
- [x] 运行 MVP 三组训练（A: F1-only, B: 5-comp+GDPO, C: base zero-shot）
- [ ] ~~准备 ACE2005 数据集~~ → D006: MVP 阶段跳过，后续用 CoNLL03 替代
- [ ] ~~评估脚本覆盖 ACE2005 RE in-domain 指标~~ → MVP 阶段跳过
- [x] 修复 eval thinking-mode bug（4 层防御）→ eval_A_v2/eval_B_v2 完成
- [ ] 修复 _match_relations metric（relation_f1 ≡ 0 bug）→ 代码已修复，待部署验证
- [ ] 调参实验 D1（F1=0.75, no GDPO）→ 训练中 cuda:1
- [ ] 调参实验 D2（curriculum: A checkpoint-200 → F1+conformance）→ 待 C eval 完成后启动
- [ ] 评估 + 判断 pass/fail → A/B 初步结果: B < A on F1, 调参进行中

## GPU 预算
- 分配: seetacloud-westb-2xpro6000 (2x RTX PRO 6000 96GB)
- MVP 已用: ~16h (A训练 10h + B训练 10h + eval ~6h, 双卡并行)
- 调参预估: ~20h (D1 10h + D2 5h + evals ~5h)

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D014 | 2026-05-14 | 用户决策 Kill 项目：释放 GPU、通知 Manager、归档 | — |
| D013 | 2026-05-13 | MVP FAIL 确认后暂停项目，向用户请示方向（kill+pivot vs reframe vs  | eval_A_continued_ckpt400, eval_D2_ckpt400, eval_B_v3 |
| D012 | 2026-05-13 | MVP 判定翻转为 FAIL：控制训练步数后 conformance reward 对 IE 质量无 | eval_A_continued_ckpt400, eval_D2_ckpt400, eval_B_v3 |
| D011 | 2026-05-13 | Relation_f1 基线修正：A=0.181（非0），MVP 判定标准不变，paper narr | eval_A_v3, eval_D2_ckpt400 |
| D010 | 2026-05-13 | 接受 Reviewer CONDITIONAL PASS，排期两个 blocking ablatio | eval_D2_ckpt400, eval_D1_v4 |
| D009 | 2026-05-13 | MVP 初步 PASS：D2 curriculum learning 在 CrossNER 零样本  | eval_D2_ckpt400, eval_D1_v4, eval_D2_final, eval_A_v2, eval_C_v2 |
| D008 | 2026-05-13 | Kill D1 v3 (step 21/500)，训练中禁用 thinking mode 后重跑 D | exp_004_d1_v3 |
| D007 | 2026-05-13 | Kill D1 v2 (59/500 steps)，修复 relation type 大小写 bug | exp_004_d1_v2 |
| D006 | 2026-05-13 | 批准 D1（F1 主导权重+去 GDPO）和 D2（两阶段课程学习）并行调参，D2 复用 A 的 c | eval_A_v2, eval_B_v2 |
| D005 | 2026-05-13 | MVP 首轮未达标（B<A），允许 1 轮 reward 权重调参，不直接 kill | eval_A_v2, eval_B_v2 |

