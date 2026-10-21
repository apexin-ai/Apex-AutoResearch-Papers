# director / loop_3.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`2e5d17f5ee314b79b441.json`](../../sessions/2e/2e5d17f5ee314b79b441.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-12T17:00:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- **seetacloud-westd-4x5090 GPU 分配**: cuda:0-3 全部属于本项目（config `execution.gpu_ids`）。root 账号。
- **westd-48478**: sonny 账号，只有 cuda:2/cuda:3 可用。
- **home-1x5090**: sonny 账号，只有 cuda:0。远程路径 `/home/sonny/exec-sim-repair-verifier`。
- **D024 硬性纪律**: 禁止 Worker 杀死正在正常训练的进程来应用代码修改。已经因此丢失 ~5.1 GPU-hours（repo-level-cls PID 34681 被杀 + repo-level-cwm 被杀）。只有训练出错或 Director 明确批准才能 kill。
- **repo-level 脚本有已知 bug**: `sample_weight KeyError`——`compute_loss` 尝试 `inputs.pop("sample_weight")` 但 Dataset/Collator 未提供该字段。v2 版本正在修复中，**确认修复后再提交训练**。
- **统计检验**: 论文只用 clustered bootstrap (variant-level aligned)，禁用 Welch's t-test（D019）。

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090** (connect.westd.seetacloud.com): root, 4× RTX 5090, 代码路径 `/home/sonny/exec-sim-repair-verifier`（注意 sonny 也有登录）
- **home-1x5090** (implicit5638.xyfu.me): sonny, 1× RTX 5090, 同路径
- **westd-48478** (connect.westd.seetacloud.com): sonny, cuda:2/3
- 模型: Qwen3-4B LoRA (函数级 + repo-level), Qwen3-8B LoRA (scaling 实验), 均在 seetacloud 上
- W&B/Git: 未配置。HF cache 路径未确认。
- **活跃进程**: 上一轮 ROADMAP 记录 repo-level-cls-v2 PID 63878 (cuda:2), repo-level-cwm-v2 PID 63096 (cuda:3)——但这两个可能已因 sample_weight bug 崩溃，需 Agent 确认是否仍在跑。8B eval JSON 生成在 cuda:0/1, matched-seed predictions 在 home cuda:0。

### 3. 📊 当前状态
- **Agent 队列 depth=6**, 正在处理 repo-level v3 确认 + 空闲 GPU 分配指令。队列中有多个 worker done 回调待处理（infra verify, datacollator fix, seed123 predictions, 8B scaling bootstrap）。还有一条我发的纠错指令：8B scaling bootstrap 分析中 4B 行数据用错了 5-paired CLS-vs-TRAJ 的 CI 而非 CLS-vs-CWM。
- **repo-level-cls-v2 / repo-level-cwm-v2**: PREPARING 状态，修复 sample_weight KeyError 后重提交。这是第 3+ 次尝试，之前失败原因：v1 sample_weight bug + 进程被误杀。
- **已完成的关键实验**: 4B 5-seed CLS/CWM/TRAJ 全部完成，8B 3-seed CLS/CWM 完成，TOST 等价检验通过，5-paired bootstrap 完成。
- **37 个实验**: 27 success / 3 negative / 3 failed / 4 pending（含 2 个 repo-level v2）。

### 4. 📋 待办（条件触发式）
- **repo-level-cls-v2 / cwm-v2 修复确认** → 确认 sample_weight 问题已解决 → 批准训练启动（seetacloud cuda:2/3, ~10-15h）
- **repo-level 训练完成** → 按 D008 Go/No-Go: ≥3pp 全力推 EMNLP Main, 1-3pp 加 seeds/数据, <1pp kill C1 pivot Plan B
- **8B eval JSON 补生成完成** → 合并到 8B scaling 分析，修正 bootstrap 表中 4B 行数据（Reviewer 发现 4B CI=[-1.71, +0.84] 是 CLS-vs-TRAJ 不是 CLS-vs-CWM）
- **Worker done 回调全部处理完** → 检查 GPU 空闲状态，确保无卡空转（>10min 空卡违规）
- **repo-level 结果出来后** → 启动论文写作（`director_post_to_paper_agent`），DDL ARR May 25（13 天）
- **Plan B（repo-level null）** → scope 收缩: C3 Oracle frontier + 两个 empirical null results + P2P ~1% finding + efficiency comparison → 目标 EMNLP Findings 或 workshop

### 5. 🎯 战略上下文
- **核心叙事**: execution simulation 从 generation → classification 的 task reformulation。函数级两者等价（F1 diff <0.5pp, TOST p=0.007），核心假说是 **complexity-dependent advantage**——repo-level 是决胜战场。
- **4 个 Pillars**: P1 Complexity-Dependent ⏳（等 repo-level）, P2 Equivalence ✅, P3 Oracle Frontier ✅, P4 8B Scaling ✅ (gap 从 4B 1.25pp → 8B 2.26pp)
- **Dream #5 (D021) 结构性缺陷**: related work 不足（需 15+ refs）, 只有 Qwen 单 model family, re-repair 未 fully specify, error overlap 分析缺失。写作阶段优先修复。
- **最容易判断错的事**: (1) 不要把 8B bootstrap 表中 4B 行的 CLS-vs-TRAJ CI 当成 CLS-vs-CWM CI——已发纠错指令但可能还没处理。(2) repo-level 脚本反复失败，不要急于催 Agent，确认 bug 真正修复再提交。(3) per-test vs traj 的 ~2pp gap 是粒度假象（D018），variant-level 对齐后无差异——论文 Claim 2 是 equivalence 不是 superiority。(4) 时间线紧张（13 天），但关键路径只有 repo-level 训练 15h + eval 2h + 写作 3-5d，AI 24/7 可行，不要 panic。


---
