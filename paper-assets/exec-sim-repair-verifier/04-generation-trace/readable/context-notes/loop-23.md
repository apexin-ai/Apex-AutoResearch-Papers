# director / loop_23.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_23.md`
- **Structured JSON:** [`a01d3b3629a449e28a5f.json`](../../sessions/a0/a01d3b3629a449e28a5f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 23
reason: max_messages
updated: '2026-05-23T20:00:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：seetacloud-westd-4x5090 的 cuda:0-3，无其他服务器
- TRAJ function-level 训练集是 **8,052** variant-level 样本（不是 447——447 是 test set 的 matched variant 数）。之前 34× 比例是错误的，已修正为 2.24× more unique variants
- 论文 EMNLP 2026 DDL 5/25，abstract ≤200 words（当前 172），正文 ≤8 pages
- 匿名仓库 push 只用 HTTPS+token URL（/tmp/anon_repo），token 不提交到代码里
- CLS@400 downsample 结果解读：不是 matched comparison（TRAJ 有 20× 更多数据），只是 data efficiency ablation，放 Appendix 不放正文

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-westd-4x5090 (connect.westd.seetacloud.com, user=root)
- GPU：RTX 5090 ×4，cuda:0/1/3 跑 CWM eval，cuda:2 刚完成 CLS@400
- 远程工作目录：/home/sonny/exec-sim-repair-verifier
- 本地项目：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier
- 匿名仓库：/tmp/anon_repo → https://github.com/anonymous-nlp-2026-2/exec-sim-repair-verifier (latest commit: 99d9154)
- 论文源码：docs/paper/*.tex，编译 23 页
- 活跃进程：cuda:0/1/3 上 CWM eval（batch_size=1，s123/s456 跑得慢）

### 3. 📊 当前状态
**R17 全部修复完成**，等待用户决定是否提交 R18。

已完成：
- R17 写作修复 10 项：N2 inconclusive、N3 14B downgrade、W1 scope、W3 format collapse qualifier、W4 merge contributions (2 bullets now)、W6 predictability、M1 TRAJ config (corrected data counts)、M3 CWM footnote、M4 DreamPRM/CodePRM
- 数据审计修复 2 项：§3.2 CLS-TRAJ gap 层级混淆 (<1pp→2.13pp)、DeepSeek 0-shot (63.00→63.02)
- CLS@400 实验 3-seed 完成：78.57 ± 0.78%，已写入 Appendix O
- 匿名仓库已同步
- review_issues.yaml 已更新至 R17

Registry: CLS@400 3 seeds DONE。CWM eval (s123/s456) 仍 RUNNING on cuda:0/1/3（batch_size=1，DDL 前可能跑不完）。

### 4. 📋 待办
- 用户回复"提交 R18" → submit_paper_to_review(recommended_review_mode="continue", mode_reason="R17 fixes verification")
- CWM eval 完成回调 → 如果数字与论文不一致则更新 Table 2 DeepSeek CWM 行
- 运维要求再推匿名仓库 → cd /tmp/anon_repo, cp latest .tex + main.pdf, git push
- R18 审稿报告回来 → 按 8 步协议处理（Read skills/global/review-report-action.skill.md）
- DDL 5/25 后如无 rebuttal 需求 → seetacloud 服务器可归类 C 释放

### 5. 🎯 战略上下文
- **审稿轨迹**：R14/R15 3.0 → R16 3.5 → R17 3.0（fresh review 回归）。Excitement 2.5-3.0/5 是 binding constraint，empirical comparison 贡献类型无法通过修改提升
- **核心叙事**：三层结构（fine-tuning necessary → function-level equivalence → repo-level divergence under ≤8B LoRA）。GenRM cross-domain hypothesis 在 Intro 作为 question 而非 claim
- **最易判断错的事**：TRAJ 数据量。function-level TRAJ 有 8,052 variants（比 CLS 的 3,596 还多），confound 是 label granularity 不是 data volume。Repo-level 反过来：TRAJ 只有 386 variants vs CLS ~70K。两个 level 的数据结构完全不同
- **14B 证据权重**：3 seeds × 1 family × df=2，几乎无统计区分力。Abstract 已降级为 "Preliminary 14B results suggest gap may narrow"。不要重新升级
- **Contribution 结构**：现在只有 2 个 bullets（Complexity-moderated formulation choice + Failure mode taxonomy），error complementarity 已合并入 #1 作为子句


---
