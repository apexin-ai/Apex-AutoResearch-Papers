# director / loop_9.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`f13a2b9688cd484bc8e1.json`](../../sessions/f1/f13a2b9688cd484bc8e1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-21T01:30:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文 w=3 是 primary analysis parameter，w=5 仅 supplementary。Table 3 全部使用 w=3 值，不要混入 w=5
- DeBERTa-large-MNLI standalone accuracy = 55.00%（不是 36%），论文多处引用此数字
- FOLIO SC baseline 必须用 alphabetical tiebreaking 后的 corrected 值：55.88%（非 54.41%）
- Abstract/Intro 报告 peak results（Mistral +10.67pp w=5, LLaMA +4.17pp w=3）不指定 w，这是 L1 LOCKED 不可改
- Process-κ 方向：gap 最大的是弱模型（Mistral +0.230），随 capability 收窄（Qwen-14B +0.022）——不是"随 capability 增大"
- Paper Agent 产出的数值必须 cross-validate：M054 事故教训——Agent 曾将 w=5 值错标为 w=3 传播到 5+ 处

### 2. 🖥️ 基础设施快照
- 无远程服务器活跃进程，所有实验已完成
- westd-16639: 4× GPU 空闲，westd-25068: 4× GPU 空闲（Reviewer 正式确认 No-Go，hold for R9）
- 论文源码：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/`
- 编译：docs/paper/ 下 latexmk，最近一次编译 22 页（8 主文），0 errors，0 undefined refs
- Sub-population 数据：`artifacts/sub_population_results.json`
- 无活跃 Worker / cron / tmux session

### 3. 📊 当前状态
刚完成的工作（本轮全部 V11+ polish）：
- related_work.tex: 加 PAL/PoT/Faithful CoT 引用 + Positioning 段 sigmoid framing 修复
- limitations_content.tex: DeBERTa 55%（非36%）+ LLaMA counter-example
- appendix.tex: Sub-population analysis 整合（answer-type + constraint-count，corrected baseline，multiple comparison caveat）
- appendix.tex: Table 20 full 12-condition BH table（之前完成）
- solutions.tex: 5 处 w-value 修正 + resizebox + BH m=12 parenthetical

Registry: 无 RUNNING/PREPARING 实验。全部 DONE。
等待中：**R9 审稿报告**（Review Director 在 review_chat_id `oc_c338e034cbffa10b9cc723e731d288d8` 执行）。

### 4. 📋 待办
- R9 审稿报告回来 → Read `skills/global/review-report-action.skill.md` → Holistic Pass → Per-Comment Action Matrix → 派 Agent/Paper Agent 修复
- R9 如果暴露 evidence gap 需要新实验 → 评估 GPU 需求，westd-16639/25068 可立即使用
- R9 如果 clean → 进入 final polish → submit_paper_to_review 提交 R10 确认稿 → 最终提交
- May 25 DDL 前 1 天（May 24）：必须完成所有修改，进入 freeze

### 5. 🎯 战略上下文
- 论文是 negative result paper：SICA（symbolic self-verification）全面失败，root cause 是 Symbolic Mirage（self-extracted constraints = bias projection）。Cross-arch DeBERTa NLI escape 是唯一正面结果。
- Capability Gap Hypothesis 是 sigmoid decay（不是 threshold/monotonic）：gains persist into moderate negative gaps（LLaMA gap=-15pp still significant），vanish only when gap widens further
- 8-point Spearman ρ=0.970 (p<0.001) 跨 3 NLI architectures × 4 generators from 3 families——这是 §6 的统计骨架
- 易错判断：(1) 不要把 sub-population mid-constraint +9.4pp 包装为 main finding（exploratory only，multiple comparison caveat 已加）；(2) 不要建议加第 4 个 model family（Reviewer 已 No-Go，ρ=0.970 sufficient）；(3) GPU 空闲是合理的——Reviewer 正式确认 hold for R9
- 决策链：D110(Symbolic Mirage universal) → D112(paper pivot) → D117(sigmoid reframe) → D118(LLaMA approval) → D119(w-value fix)


---
