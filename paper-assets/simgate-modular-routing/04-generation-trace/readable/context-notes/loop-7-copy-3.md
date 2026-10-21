# reviewer / loop_7.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`e618f66ef40e1f85b145.json`](../../sessions/e6/e618f66ef40e1f85b145.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-15T00:24:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- westb-13313 只有 cuda:0 和 cuda:1（热备），当前项目 GPU 白名单需从 registry/config 确认，审查时必查 `nvidia-smi` 核对进程设备号
- 论文正文硬限 4 页，当前已接近满页（~248 行），任何新增内容必须同步压缩等量行数
- 本地 workspace 论文文件路径：`projects/simgate-modular-routing/` 下；远程代码/数据在 `/root/autodl-tmp/simgate-modular-routing/`。两边都有 paper/ 目录，审查前必须确认哪边是最新源（L1 #5 双边核对）
- DAF 数字有 penalty-dependent 和 penalty-independent 两套：90.41% (P=100) vs 78.9% (penalty-independent)。审查 claim 时必须核对用的是哪套，不能混用

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (root)，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- 论文源文件：`/root/autodl-tmp/simgate-modular-routing/paper/` （main.tex + 各章节 .tex）
- 实验数据：`/root/autodl-tmp/simgate-modular-routing/results/`（plan_c/ 11 task types, alfworld_counterfactual/, decomposition 等）
- trajectory 数据格式：`results/plan_c/{task}/episodes.jsonl`，每 step 含 `is_dead` 字段 + `score_after`
- GPU 状态：cuda:0 空闲, cuda:1 空闲（report.md 2026-05-14）
- Worker 池：0（后端无可用账号）
- 活跃进程：无（全部实验已完成）

### 3. 📊 当前状态
刚完成 R6 fresh review (3.25/5 Borderline Accept) 修复方案的审查，已通过 `reviewer_post_to_director` 提交。审查内容：
- C1 DAF dual reporting：可行，Abstract 精简措辞后 ~140 words 仍在限内
- C2 三篇 counterfactual-in-RL 文献：**全部验证为真实**（AAAI'24 Amitai, AAMAS'23 Gajcin, AIJ'21 Olson）
- W1 structural coupling caveat：建议微调措辞，避免过度自我削弱，引导读者关注 78.9% penalty-independent finding
- W3 death temporal data：trajectory 数据中 `is_dead` 字段可直接提取，无需新实验
- 页面预算：极紧但可行，§4.3 keyword baseline 细节必须 Appendix 化

Registry: 全部 55 实验 DONE（成功 22 / 负向 13 / 失败 10）。无 RUNNING/PREPARING。

### 4. 📋 待办
- Director 批准修复方案 → 审查修改后的 LaTeX diff，重点核对 Abstract 词数 ≤150、C1 数字与 registry 一致（DAF_P100=89.6 还是 90.41%——registry 中 plan-012-penalty-sensitivity 记 89.6，plan-012-full 记 0.9041，需确认是否四舍五入差异）
- Worker 提交修改后论文 → 做全文数字一致性交叉验证（Abstract/Introduction/Conclusion 中的 DAF 数字必须统一）
- 如果 Director 决定做 W3 death temporal 提取 → 审查提取脚本逻辑和结果（关注 `is_dead` 字段在 death episode 中是否正确标记——chemistry-mix ep0 final=-100 但可见 steps 全为 `is_dead: false`，可能 death 发生在最后一步需要确认）
- 论文 5/17 初稿交付 → 需最终 PDF 视觉检查 + 编译验证

### 5. 🎯 战略上下文
- 项目核心发现：modular LLM agent 的 routing signal 主要来自 death avoidance（78.9% penalty-independent），deterministic computation 的价值集中在灾难性失败预防
- 论文状态 READY，当前是 review response 阶段（R6 fresh review 3.25/5 Borderline Accept）
- **最易判断错的事**：DAF 数字有两个来源——plan-012-penalty-sensitivity (DAF_P100=89.6%) 和 plan-012-full (death_avoidance_fraction=0.9041 即 90.41%)。差异可能来自样本范围（11 tasks vs 全部）或计算方式。修改论文时必须确认引用的是哪个实验的数字，不能混用
- **易踩的坑**：(1) 远程 `paper/` 和 `docs/paper/` 是两套文件，`paper/` 是当前版本；(2) `latex_build/` 下还有一份，是编译产物不是源文件；(3) R6 reviewer 是 fresh review 没看过 R4/R5 修改历史，C1 是 R4-W1 的升级版但要当新问题处理


---
