# prov_grounded_uie — Research Dashboard

> 最后更新: 2026-05-13 15:14 UTC | 更新原因: 修正实验统计（25个非18个）；Part 1 崩溃 + Part 2 预防性停止；采纳 Reviewer 建议加 Best-of-N 并行 track

## 核心方向
ProvUIE: 训练 LLM 在做 UIE 时同步输出高质量证据跨度。
核心发现：GRPO sequence-level reward 对长序列（1000-2000 tokens）存在 credit assignment 困难，无法有效学习 evidence provenance 信号。转用 DPO preference learning 绕过此问题。

## 当前进展
- 阶段: MVP 验证 → DPO 路线执行中
- SFT baseline: ✅ RE-F1=0.4337, Evi-F1=0.3652, AP=0.9529（sft_eval_v5）
- NLI reranking: ❌ negative（NLI 在 DocRED 上≈随机，D006）→ 用作 negative finding 强化 end-to-end motivation
- GRPO v1b: ❌ KL≈0，模型未训够（超参过保守）
- GRPO v2: ❌ KILL（Evi-F1=0.3705 < kill 线 0.3852，D010）
- Reward 诊断: ✅ composite_std=0.138，信号充足但 GRPO 无法利用
- DPO candidates: ⚠️ Part 1 崩溃（rewards.py:216 TypeError，380/1514），Part 2 预防性停止。修复 + 冒烟测试中
- 完成 21 / 运行 2 / 待处理 2（成功 6 / 负向 4 / 失败 5 / killed 6）

## MVP 执行进度
- [x] Step 0: 环境搭建（westd-37397，2×RTX PRO 6000 96GB）
- [x] Step 1: DocRED 数据准备
- [x] Step 2: SFT baseline → RE-F1=0.4337, Evi-F1=0.3652
- [x] Step 3: Post-hoc NLI reranking → negative（NLI oracle≈随机）
- [x] Step 4: GRPO pilot → KILL（v1b KL≈0, v2 Evi-F1 +0.53pp 噪声范围）
- [ ] Step 4b: DPO preference learning（替代 GRPO）
  - [ ] 4b.1: 修复 rewards.py + 冒烟测试
  - [ ] 4b.2: 候选生成完成（双卡并行，从断点 resume）
  - [ ] 4b.3: Best-of-N 评估（零成本，复用候选 + reward 排序）← 与 DPO 训练并行
  - [ ] 4b.4: DPO 训练 + eval
- [ ] Step 5: 三组对比 + degeneration sanity checks

## Kill Criteria（SFT-only baseline，D006 更新）
- Kill: Evi-F1(DPO) < 0.3852（SFT + 2pp）
- Inconclusive: 0.3852-0.4152
- Pass: Evi-F1(DPO) >= 0.4152（SFT + 5pp），且 RE-F1 >= 0.4037

## DPO Backup Plan（若 DPO 未通过 kill criteria）
1. **Reward 重设计**: 当前 composite reward 基于 IoU-based provenance_fidelity，若 DPO 也失败，说明 reward 对 evidence 质量区分度不足 → 改用 span-level Evi-F1 直接作为 reward signal。⚠️ 需重新生成候选（~28 GPU-hours 额外成本）
2. **Rejection Sampling / Best-of-N**: 不再训练 policy，转为 inference-time 方法——SFT 模型生成 N 个候选，用 reward 排序取 best。**候选生成完成后立即评估 Best-of-N（零额外成本），作为 DPO 的并行 track 而非仅 fallback**
3. **判定逻辑**: DPO fail + reward margin 充足 → 路径 1；DPO fail + reward margin 退化 → 路径 2 作为 salvage + 重新审视 reward 设计；Best-of-N 本身效果好 → 可能不需要 DPO 训练

## 近期任务
- [ ] 修复 rewards.py:216 + 冒烟测试 50 样本（⚡ 紧急）
- [ ] 从断点 resume 双卡候选生成
- [ ] 服务器路径重命名 trace-verdict-study → prov_grounded_uie（Worker 执行中）
- [ ] 候选生成完成后立即跑 Best-of-N 评估
- [ ] 提交 dpo_pilot_v1 审批
- [ ] DPO 训练 + eval
- [ ] Kill criteria 判定

## GPU 预算
- 已分配: 2×RTX PRO 6000 (96GB) @ westd-37397
- MVP 已用: ~35 GPU-hours（SFT 训练 + eval + GRPO v1b/v2 + NLI）
- DPO 预估: ~30-50 GPU-hours（candidates 28h×2卡 + 训练 + eval）
- 全项目: ≤200 GPU-hours

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D012 | 2026-05-13 | 论文 framing 定向：analysis paper（系统性比较 SFT/GRPO/DPO/NL | grpo_pilot_v1b, grpo_pilot_v2, posthoc_nli_v3, sft_eval_v5, random_evidence_baseline |
| D011 | 2026-05-13 | 采纳 Best-of-N 作为 DPO 并行评估 track：候选生成完成后零成本评估，不仅是 fa | dpo_candgen_v2_gpu0, dpo_candgen_v2_gpu1_r3 |
| D010 | 2026-05-13 | grpo_pilot_v2 KILL：Evi-F1=0.3705 < kill 线 0.3852。G | grpo_v2_step50_eval, grpo_pilot_v2, grpo_pilot_v1b |
| D009 | 2026-05-13 | v2 step 50 mid-eval 为 kill/continue 判定点；同时提前准备 DPO | grpo_pilot_v2, grpo_v1b_eval |
| D008 | 2026-05-13 | grpo_v1b_eval 结果：RE-F1=0.4264, Evi-F1=0.3593, AP=0 | grpo_v1b_eval, grpo_pilot_v2 |
| D007 | 2026-05-13 | GRPO provenance reward 砍掉 NLI 分量（nli_weight 0.3→0. | posthoc_nli_v3, grpo_pilot_v2 |
| D006 | 2026-05-13 | NLI reranking 失效，采用 C+A narrative：NLI 失败作为 negativ | posthoc_nli_v3, sft_eval_v5 |
| D005 | 2026-05-12 | GRPO pilot 自恢复确认：evidence provenance reward 设计可行，冷 | grpo_pilot_v1 |
| D004 | 2026-05-12 | D003 阻塞解除：MR-UIE faithfulness ≠ ProvUIE evidence p | — |
| D003 | 2026-05-12 | MR-UIE faithfulness reward 精读升级为阻塞性前置，与 ProUIE 同级 | — |

