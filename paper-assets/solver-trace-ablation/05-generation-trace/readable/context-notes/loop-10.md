# director / loop_10.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`d53642975aa2b64af99a.json`](../../sessions/d5/d53642975aa2b64af99a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-21T01:42:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 1 张 GPU：westd-39279:cuda:0（RTX PRO 6000 96GB）。之前因误以为有多卡被纠正过。
- 所有跨 run 的 ISR/PR 比较必须使用 eval_sta.py 统一评估（Constraint C004），禁止直接比较训练 log 中的 ISR。
- ISR 命名决策待定：当前用 "Intensional Structural Reward"，用户可能改为 "Irreducible Solver Rate"。已给用户设 5/22 24:00 默认截止。
- 论文真源在本地 `docs/paper/`，不在远程。改论文永远改本地再 sync。

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279，工作目录 /root/solver-trace-ablation
- Python：/root/miniconda3/bin/python（conda base）
- 模型：Qwen3-4B（HF cache 在远程服务器）
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/`
- paper/ 目录是 docs/paper/ 的同步副本（编译在 paper/ 下进行）
- 无活跃进程/tmux/cron。GPU 完全空闲。所有实验已完成。

### 3. 📊 当前状态
论文提交就绪。刚完成：
- ARR 格式合规检查 PASS（8 页主文、匿名化、0 undefined refs）
- Reviewer 最终 presentation polish 审查完成（2 条 bib 格式问题已修复，其余 false positive）
- references.bib 修复：ng1999policy 删 ordinal、uesato2022solving 加 case braces，已同步 paper/
- D157 shuffled-ISR 3-seed 实验全部完成并写入论文（§4.3、Table 1、Limitations、Abstract、Intro、Conclusion、Appendix Table 5）
- Figure 3 gen_fig3.py 已更新匹配 Table 1 数据

Registry：0 RUNNING / 0 PREPARING。73 个成功实验，44 个 negative。全部完成。

### 4. 📋 待办
- 用户回复 ISR 命名 → 如选 "Irreducible Solver Rate"：全文替换 "Intensional Structural Reward" → "Irreducible Solver Rate"，重新编译，sync paper/。如 5/22 24:00 前无回复 → 保持现名。
- 命名确定后 → 最终编译 + `submit_paper_to_review` 提交给 Review Director 做投稿前审查。
- Review Director 返回审稿报告 → 按 review-report-action skill 处理。
- DDL: EMNLP 2026 ARR May 25。

### 5. 🎯 战略上下文
- 核心发现：ISR 的 observer/optimizer 不对称性——作为诊断可靠（99.5% collapse invisible to PR），作为 reward 被 Goodhart（TS gaming）。Shuffled-ISR 控制实验证实语义对应而非分布形状驱动 gaming。
- 决策链关键：D159 决定不升级 C2 为 "mechanistic"（PR=15% 解释模糊），用 "rules out distributional confound"。
- 易错点：Reviewer 可能读到旧版本文件报 false positive（本轮发生过两次——Figure 3 和 D157 per-seed rows）。收到 Reviewer 报告时先核实当前文件状态再行动。
- GPU 空闲是正常状态——实验阶段已结束，所有核心 claim 有数据支撑。System keepalive 会反复催 GPU 利用，合理回应即可。


---
