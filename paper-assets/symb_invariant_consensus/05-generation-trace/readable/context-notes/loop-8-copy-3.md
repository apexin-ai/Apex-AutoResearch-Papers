# reviewer / loop_8.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`4b595b259a83cc2aef2b.json`](../../sessions/4b/4b595b259a83cc2aef2b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-17T21:16:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-32608 上的 cuda:0（RTX PRO 6000），其他卡不属于本项目
- 所有实验已完成，GPU 空闲，当前阶段纯写作/审查，不应有新的 GPU 进程
- 11.5% discriminative constraints 统计量无服务器端数据文件溯源（已多次 WARNING，未解决）——引用此数字时必须注明来源为 manual analysis of 43 pilot problems，不可声称有自动化分析支撑
- 论文 bib 中 diverseaware2025、satbench2025、llmmeets_cp2025 刚修复过 author 字段（Round 1 CRITICAL），核实任何 bib 修改不要回退到 "Various"

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608(root)，远程代码根目录 /root/symb_invariant_consensus
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/
- 论文 tex 文件：上述 workspace 下 docs/paper/（main.tex 为主文件）
- 远程分析数据：/root/symb_invariant_consensus/analysis/（exp013_agreement_matrix.json, power_analysis.json, bootstrap_cis.json, paper_table_data.json）
- 无活跃进程、无 tmux session、无 cron 任务、无 wandb 运行中实验
- registry: 42 个实验，13 个 success，全部 DONE

### 3. 📊 当前状态
刚完成 Pre-Round 2 独立质量评估并提交 Director。论文已通过 Round 1 全部 16 issues 修复（含 2 CRITICAL bib + answer_assertion 说明 + Qwen-7B 新增 + Limitations 扩展至 7 项）。

发现 1 处残留不一致已报告：Appendix power analysis L181 "remaining six conditions" 应为 "seven" 或 "eight"（Qwen-7B 加入后条件总数从 10→11）。

当前等待：Director 审批 Round 2 审稿卡（apr_20260517T193104_lw9x），之后可能收到 Round 2 审稿反馈需要再次审查。

### 4. 📋 待办
- Director 转发 Round 2 审稿报告 → 按 5.3 模板评分，重点看 Overall 是否 ≥4（EMNLP Conference 线）
- Paper Agent 提交 Step 5 Round 2 修复 → 验证 appendix "remaining six" 是否已修正 + 任何新增修改的数据一致性
- Director 转发最终提交确认 → 做最终 10 项检查（CLAUDE.md §七.3）
- 如收到 Framing 调整提案 → Read negative-framing-review.skill.md，按四维度审查

### 5. 🎯 战略上下文
**核心结论**：SICA（自提取 FOL + MAX-SAT）= SC（多数投票），全 11 条件 Δ n.s.。Oracle +8.82pp 证明聚合机制有效，瓶颈在自提取质量（capability trap）。这是一篇 diagnostic negative result 论文，不是方法论文。

**决策链关键节点**：D038（oracle 确认提取瓶颈）→ D037（dream 审稿 3/6 Weak Reject，结构性问题已修复）→ D039（re-dream 4/6 Borderline Reject，批准 Phase 2）

**易错点**：
- 论文说"five model families"——QwQ 和 Qwen2.5 算不同 family（QwQ 是 reasoning-specialized，独立训练管线）。DeepSeek-R1-Distill-Qwen-7B 算 DeepSeek family（虽然 Qwen 架构）。这个分类审稿人可能质疑，不要自己改动
- Qwen-7B 条件 n=56（不是 60），论文未解释原因——如果审稿人问，需要查 registry 确认是否有 4 个 parsing failure
- "803/804" 是 MAX-SAT vs Count-only 的 agreement，不是 MAX-SAT vs SC（那个是 773/804）。之前出过 802 的错，已彻底修复，但要防止回退
- 论文 DDL: EMNLP 2026 ARR May 25（~8 天）


---
