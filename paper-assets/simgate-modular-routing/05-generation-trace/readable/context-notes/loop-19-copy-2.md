# reviewer / loop_19.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_19.md`
- **Structured JSON:** [`3903c8b88978a21ff460.json`](../../sessions/39/3903c8b88978a21ff460.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_wall_time
updated: '2026-05-22T18:40:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- D131/D132: DDL 前不跑新 GPU 实验，D129 已释放 GPU 分配。任何"补一个实验"的提议都应拒绝（已评估过 72B 复现 / task-type 扩展 / grounding 深化 / death predictor，全部 ROI 不足）
- 论文主文恰好 8 页（EMNLP 2026 上限），任何内容新增必须等量压缩
- Anonymous code repo 有 max_steps=50 vs 论文 T_max=30 不一致（我已 report warning，用户尚未处理）
- references.bib 中 switch-transformer-2022 用了 @inproceedings 但实际是 JMLR journal paper（info 级，未修）

### 2. 🖥️ 基础设施快照
- 服务器：westd-18266 (root), 4× RTX PRO 6000 (96GB)，**GPU 已全部释放，无活跃进程**
- 远程代码：/root/autodl-tmp/simgate-modular-routing
- 本地论文：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/
- 编译产物：main.pdf (24 页, 0 errors)
- 无活跃 PID / tmux / cron / W&B run

### 3. 📊 当前状态
刚完成：
1. R28 Writing Fixes 验收 10/10 PASS（W-Critical-1/2 + W1-W7 + M4/M5 + 数字一致性 + 页数）
2. ROADMAP 审查 — 无异常
3. 写作提分评估 — 给出 2 处低风险建议（Intro bridge sentence + Conclusion specificity），判断写作已近天花板
4. 紧急实验评估 — 确认 D131/D132 冻结正确，无高 ROI 实验
5. 叙事完整性审计 — 53/53 成功实验已引用，29/30 阴性实验已纳入叙事，无遗漏

Registry: 119 DONE + 2 ANALYZING（alfworld-llama-cross-model, gemma-scienceworld-cross-model — 这两个 ANALYZING 状态可能是残留，数据已被 gemma-v5 和 alfworld-llama-v3 覆盖）
无等待中的 Worker 回调或 Director 决策。用户说"论文提交你不用管，我们手动做"。

### 4. 📋 待办
- 用户确认提交 → 无需 Reviewer 动作
- Director 要求执行写作微调（Intro bridge / Conclusion specificity）→ 验收修改
- Director 转发真实 ARR 审稿意见 → 用 rebuttal_prep.md（6 Attacks）+ 论文数据独立核实，进入 rebuttal 模式
- 发现 anonymous code max_steps 不一致被修正 → 验证修正内容

### 5. 🎯 战略上下文
- **核心结论**：ScienceWorld 中 78.9% non-tie routing labels 源于 death asymmetry（penalty-independent），DAF=90.4% at P=100，跨 3 个 7-9B 模型家族复现（spread 2.2pp）
- **决策链**：D126/D127 framework-centric pivot → D129 GPU 释放 → D130 接受 Findings ≥3.0 → D131/D132 实验冻结 → R28 修复 → 验收 PASS
- **易错点 1**：DAF 是 P-dependent 的（P=10 时只有 50.4%）。论文已在 §2.4 明确标注。审稿人如果攻击"90% 是 P=100 制造的"，正确回应是"label fraction 78.9% 是 penalty-independent 的主指标，DAF 是补充"
- **易错点 2**：router negative result 不是 limitation 而是 framework prediction（oracle degeneracy → routing unnecessary → router should fail）。D126 pivot 后这是 feature not bug
- **易错点 3**：cross-env 只有 preliminary evidence（MATH 无 signal，ALFWorld 信息不对称），论文已明确区分 methodological generality vs empirical generality。不要替论文 claim empirical generality
- **Rebuttal 就绪**：artifacts/rebuttal_prep.md，6 Attacks（P-dependence / oracle confound / single env / novelty / router failure / step-level），精简版 ~670 词 + 详细版 ~1200 词


---
