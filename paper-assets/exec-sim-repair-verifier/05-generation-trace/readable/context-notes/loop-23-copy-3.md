# reviewer / loop_23.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_23.md`
- **Structured JSON:** [`b143c6aa3a9f0318ef8b.json`](../../sessions/b1/b143c6aa3a9f0318ef8b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 23
reason: max_wall_time
updated: '2026-05-21T13:04:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `seetacloud-westd-4x5090`，GPU 0-3 全部属于本项目，当前 4/4 占用
- CWM 所有 repo-level 训练 eval_loss=NaN → 只能用 final epoch checkpoint，不能 val-select
- Qwen CWM 训练有 eval_steps=100 → tqdm ETA 不准（需 ×2 估真实 wall-clock），已多次确认
- Table 3 CLS Qwen std 应为 **0.67**（非 0.66），此修复至今未执行——提交前必改
- Appendix Threats 写 "No CWM overtraining, <2pp epoch difference" 但过拟合分析发现 -5.36pp → **在 multi-seed 数据确认前不要改论文中任何 CWM epoch claim**，两边矛盾未解决

### 2. 🖥️ 基础设施快照
- 服务器：`seetacloud-westd-4x5090`，远程代码根：`/home/sonny/exec-sim-repair-verifier`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/`
- 论文：`docs/paper/` 下的 .tex 文件；产出目录：`artifacts/`
- GPU 0: Qwen CWM s123 (PID 未记录, ~66%, ETA ~21:30 UTC May 21)
- GPU 1: DeepSeek CWM s456-v2 (PID 949112, 81%, ETA ~13:00 UTC May 21)，monitor PID 1769 + sidecar PID 1624 → 训练完成自动触发 eval
- GPU 2: DeepSeek CWM s123-v2 resume (PID 28200, ETA ~23:15 UTC May 21)
- GPU 3: Qwen CWM s456 (~66%, ETA ~21:30 UTC May 21)
- Qwen batch=2 测试脚本在远程 `/home/sonny/exec-sim-repair-verifier/test_qwen_eval_batch2.sh`，GPU 1 释放后可执行

### 3. 📊 当前状态
**刚完成**：
- M027 数据一致性修复验证 ✅（integrate/stats/plot 三文件值已正确）
- commit 44b6a29 数字审计修复验证 ✅（H1 13→19pp, H2 TOST 0.0087→0.007, H3 TRAJ 4B, M1 CLS保持, M2 DS 0-shot 48.54）
- Claim 强化策略分析、CWM 过拟合分析审查、Supplementary completeness 审计、Rebuttal framework 审查
- Appendix 5 处 overfull hbox 排版审查（3 处 >30pt 需 resizebox）
- CWM 数据到齐后三种 Scenario 叙事预演（A/B/C 方案已准备）

**等待中**：
- 4 个 CWM multi-seed 训练完成 → eval → 数据到齐预计 May 22 下午
- Paper Agent 叙事/去AI批量修复（queued）
- Agent 计算预算不一致核查（queued）

### 4. 📋 待办
- DS s456 训练完成（~13:00 UTC）→ 确认 sidecar→monitor→eval 自动触发成功 → 确认 GPU 1 释放 → 确认 Qwen batch=2 测试启动
- Qwen s123/s456 训练完成（~21:30 UTC）→ 确认 eval 启动 → 核实 eval 用的 seq_length/batch_size
- DS s123-v2 完成（~23:15 UTC）→ 比对 epoch 1 (75.45%) vs epoch 3 → 确认/否定 CWM 过拟合
- 全部 CWM eval 到齐（~May 22 下午）→ 判定 Scenario A/B/C → 执行对应叙事方案 → 填 Table 3 CWM 行 → 重跑 W5 → 更新 z 值
- Appendix overfull 修复后 → 验证 PDF 无溢出
- 提交前 → 全文 placeholder 扫描（grep `\tbd`）→ 8 页限制检查 → 最终数字一致性复核

### 5. 🎯 战略上下文
- 目标 EMNLP 2026 ARR，DDL May 25，当前 R6 评分 3.0（Findings），目标 3.5+
- 核心 story：function-level 三 formulation 等价 → repo-level CWM 崩溃（format collapse）→ complexity mediates formulation divergence
- 最大提分项：CWM multi-seed 消除 single-seed caveat（这是 R6 主要扣分项）
- **易判断错的事**：(1) Qwen 训练 ETA 不要信 tqdm，必须 ×2（eval_steps=100 开销）；DeepSeek tqdm 是准的（无 eval_steps）。(2) rebuttal framework Attack #1 第 4 点（过拟合防线）用了 cross-seed 数据但叙事读起来像 same-seed，已标 warning 待修正。(3) review_issues.yaml R6-N4 仍记录 z=-106.7，论文实际是 z=-64.4（stale record）。(4) Scenario A 最可能（~70%），但如果出现 Scenario B/C 需要更多时间做叙事重构——务必在 May 22 晚间判定 scenario，留足 May 23-24 调整空间


---
