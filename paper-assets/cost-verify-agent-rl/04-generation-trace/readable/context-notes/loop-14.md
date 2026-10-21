# director / loop_14.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_14.md`
- **Structured JSON:** [`04e5ac5a07d4c19a9b5d.json`](../../sessions/04/04e5ac5a07d4c19a9b5d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-21T02:36:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-17606 cuda:0,1 + westd-47453 cuda:0,1,2,3（共 6 张），home-1x5090 不在白名单
- FSDP checkpoint 跨服务器加载有 device mismatch 问题，必须设 `optimizer_offload: false` 或在训练原机 eval
- Seed 2 checkpoint 在 5/20 磁盘清理中永久丢失，不要尝试恢复
- Cell C v3 止损阈值已定：step 5 success=0% + action_is_valid<20% → 终止释放 westd cuda:2,3
- 论文 h-sweep 数据全部是 seed 1（controlled comparison），不要改成 mean

### 2. 🖥️ 基础设施快照
- westd-47453: `/root/cost-verify-agent-rl`，conda base (`/root/miniconda3/bin/python`)
- bjb1-17606: `/root/cost-verify-agent-rl`，同上
- 模型 SFT base: westd `/root/autodl-tmp/checkpoints/` 下，bjb1 需从 westd scp
- Seed 3 checkpoint: westd `/root/autodl-tmp/checkpoints/exp029-seed3/global_step_15/`
- W&B: seed3 OOD eval run `gqr6ux4z`; Cell C v3 run `ghswaew5`
- 论文本地路径: `projects/cost-verify-agent-rl/docs/paper/`
- 活跃进程: Cell C v3 PID 94753 westd cuda:2,3 (tmux session)
- 刚派 Agent 在 bjb1 启动第三个 seed 训练（exp029_seed4，seed=123）

### 3. 📊 当前状态
**刚完成**：Seed 3 OOD = 10.45%（vs Seed 1 23.88%），论文全部数字已更新为 17.2% mean [10.4-23.9%]。Table 1、Abstract、Intro、Conclusion、Limitations 全改完。Reviewer D108 一致性审查通过（0 critical）。Figure caption 补注 seed 信息。bib 清理完成（17 orphan entries 删除）。

**Running**：
- Cell C v3 (ScienceWorld episode-level GRPO): westd cuda:2,3, ~3/15 步, ⚠️ step 2 出现坍塌信号(action_valid=0.6%), 每步 2-3h, ETA ~28h
- **刚派但未确认启动**：bjb1 Seed 4 训练（第三个 episode-level seed），等 Agent 回调确认

**等待**：Agent 回调（bjb1 seed 4 启动确认 + Cell C v3 进度）

### 4. 📋 待办
- Agent 回调确认 bjb1 seed 4 启动 → 审批实验 + allocate GPU
- Cell C v3 到 step 5 → 检查 val 结果：success=0% + valid<20% → 终止；否则继续
- bjb1 seed 4 训练完成（~5.5h）→ 立即在 bjb1 本地跑 134-task OOD eval（optimizer_offload=false）
- Seed 4 OOD 出来 → 3-seed mean 更新论文 Table 1 + 所有引用数字
- Cell C v3 最终结论出来 → 若坍塌确认，Limitations "Fix generality" 段加具体 ScienceWorld 数据
- 所有数据整合完 → submit_paper_to_review 提交正式审稿

### 5. 🎯 战略上下文
- **诊断 claim VERY STRONG**（ALFWorld factorial + γ-sweep + 8B + ScienceWorld 全验证）；**修复 claim STRONG**（ALFWorld-specific, seed-variant）
- 核心决策链：D104(claim升级) → D106(跨环境确认) → D107(Cell C 最后重试) → D108(seed 3 OOD 整合+claim 细化)
- **最容易判断错的事**：看到 bjb1 FSDP eval 失败不要再花时间修——用 `optimizer_offload: false` 从头训练+本地 eval 是正确路径
- **GPU 空闲是高压线**：用户刚明确要求利用好空闲卡，Manager 也反复催。M037 教训：训练完成后 eval 必须自动衔接，不能等手动触发
- 论文 Reviewer R5 8/10，写作已收敛。数字下调（23.9%→17.2%）后 story 仍成立，因为对比是 17.2% vs 0%（step-independent collapse），且 8B 90.3% 提供 scale-up 叙事
- ScienceWorld Cell C v3 大概率坍塌——但论文措辞安全（只 claim collapse generalizes，不 claim fix generalizes），不影响核心 story


---
