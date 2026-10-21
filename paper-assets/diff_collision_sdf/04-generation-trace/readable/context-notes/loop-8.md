# director / loop_8.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`95d3c789ec8639e6cf14.json`](../../sessions/95/95d3c789ec8639e6cf14.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-28T05:44:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-35807:cuda:0/1/2/3 + westd-45947:cuda:0/1，严禁使用白名单外 GPU
- 论文修改后必须运行 `python paper_switch.py --verify`，否则 Scenario B/C 切换机制会 break（已发生 3 次，M064）
- eval 命令必须包含 `--pi05` flag，缺失会产生 frozen episodes 伪影（M056，已发生 2 次）
- 所有 eval 必须统一 eval seed=7，200 episodes
- Phase 2 训练 30K 未完成（磁盘满 step 19999），论文中 Phase 2 数据用 18K checkpoint (CAR=58.0%)，不可写成 30K

### 2. 🖥️ 基础设施快照
- **westd-35807**: /root/colliforce-vla, conda base (/root/miniconda3), WANDB_MODE=disabled
  - cuda:2 运行 Phase 2 s2_v4 (DDL 后完成，不影响提交)
  - cuda:0/1/3 空闲
- **westd-45947**: /root/colliforce-vla, conda base
  - eval_phase2_18k_s2 + eval_spatial_bowl_lora_ctrl_s0_v2 可能仍在运行（补充验证，不影响论文）
- **论文源码**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex`
- **编译 PDF**: 同目录 `main.pdf`（17 页，CoRL 2026 单栏）
- **paper_switch.py**: 远程 westd-35807 /root/colliforce-vla/ 或本地 docs/paper/ 目录

### 3. 📊 当前状态
**审稿报告 Round 1: 4/10 Weak Reject**。已制定全面修改方案 (D044) 并派 Agent 执行。

**Agent 当前任务**（正在处理）：
1. 主指令：全面论文修改（标题、统计重写、scope narrowing、SafeVLA 区分、Phase 2 修正、Limitations/BI 扩展）
2. Urgent 插队：claim3.tex L26 Phase 2 57.5%→58.0% + 全文绝对措辞→nuanced framing 对齐

**已完成的统计修复**（Worker worker_paper_p0-2-5-statistics-phase2 已 done，Reviewer 验证通过）：
- Section 6 双 null construction permutation test（Null A/B 均 non-significant）
- Power analysis（MDE≈5pp）
- Appendix J eval-seed 数据入主文
- Phase 2 appendix 更新为 18K/58.0%

**尚未完成的**（Agent 正在做或待做）：
- 标题修改（去 98%）
- Abstract/Intro/Discussion/Conclusion scope narrowing
- Related Work + Discussion SafeVLA 三路径区分
- claim3.tex L26 主文 Phase 2 数据同步
- 8 处绝对措辞→nuanced framing 对齐（urgent 消息中已列出精确位置）
- Limitations + Broader Impact 扩展
- P1: Oracle caveat, dfCAR displacement, 术语统一

**DDL: 2026-05-28 12:00 UTC**

### 4. 📋 待办
- Agent 完成全部修改 → 要求 Agent 汇报每条审稿意见的修前/修后段落 → post_to_reviewer 让 Reviewer 逐条验证修复充分性 → Reviewer 返回 PASS 后标 resolved
- paper_switch.py --verify 通过 → paper_compile_and_check(preview=True) → 视觉检查 → 如通过则 submit_paper_to_review 做最终审稿
- Reviewer 验证发现修复不充分 → 派 Agent 二次修改（时间允许的话）
- 修改全部完成 + 编译通过 → update_review_issues 把验证通过的 issue 标 resolved → update_roadmap 标记完成
- westd-45947 PDF 仍为旧版（01:39 UTC），如需从服务器提交需同步
- W11（缺失引用）/ W13（λ 粒度语言）/ W14（future work）/ 视觉修复 → 砍到 rebuttal，DDL 前不做除非有余时间

### 5. 🎯 战略上下文
- **核心结论**: action collapse 污染 CAR（Claim 1 强）；EE-only SDF oracle 无效（Claim 2 中）；SDF training 无显著收益但 λ=0.1 有一致正向趋势（Claim 3 需 nuanced framing）
- **决策链**: D041(统计策略双尾)→D042(全表reeval统一)→D043(λ=0.1 s2 Scenario B)→D044(审稿回应：claim降级+scope收窄)
- **最易判断错的事**: Claim 3 的措辞校准——"zero benefit" 过强（reviewer 会打回），"suggestive positive trend" 过度（Reviewer 建议用 "consistent positive direction"），正确区间是 "no significant benefit at tested scale, consistent positive direction below MDE"
- **易踩的坑**: (1) 修改 .tex 后忘跑 paper_switch.py --verify（已 3 次事故）；(2) review_issues.yaml 有 18 条 issue 全部 in_progress，Agent 完成后需逐条更新状态；(3) 审稿报告已提交 Review Director (submit_paper_to_review apr_20260528T045418)，修改完成后需要重新提交最终版
- **Reviewer 关键洞见已采纳**: 不用 Cohen's d 论证 null 等价性；不用 "case study"（自贬）；Phase 2 数据 10K→18K 修正


---
