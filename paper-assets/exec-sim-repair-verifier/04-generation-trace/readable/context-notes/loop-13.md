# director / loop_13.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_13.md`
- **Structured JSON:** [`a3b4a92da2cd51bea372.json`](../../sessions/a3/a3b4a92da2cd51bea372.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_messages
updated: '2026-05-15T13:52:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd cuda:0-3 + home cuda:0。禁止在白名单外启动实验
- home-1x5090 当前离线（SSH timeout），不可派任务，已通知用户检查
- references.bib 刚修复 8 条 AI 幻觉作者——任何新增引用必须 WebSearch 核实 first author，禁止凭训练数据猜
- CWM 8B ckpt-400 eval (cuda:3) 预计 27-54h，**无 cron 监控**（Agent 上次说要注册但未确认），接手后第一件事确认 cron 是否在位
- LoRA rank 消融 alpha/rank 策略已定（D095 修正）：rank=32/alpha=32 已跑完或接近完成；rank=64 必须用 alpha=128（scaling=2）。不要用 alpha=32

### 2. 🖥️ 基础设施快照
- **westd**: seetacloud-westd-4x5090, connect.westd.seetacloud.com, root, 工作目录 /root/exec-sim-repair-verifier
- **home**: home-1x5090, implicit5638.xyfu.me, sonny, 工作目录 /home/sonny/exec-sim-repair-verifier（当前离线）
- Python/conda：westd 用 conda base（/root/miniconda3/bin/python）
- 论文目录：本地 `projects/exec-sim-repair-verifier/docs/paper/`（.tex/.bib 真源在本地，不在远程）
- 活跃进程（截至 handoff 前）：
  - cuda:0: cwm-rank32-ablation-v2 (PID 368823) — 函数级 rank=32 训练，应接近完成或已完成
  - cuda:1: repo-level-cls-8b-s42-resume (PID 295794) — CLS 8B s42 扩展训练，ETA ~May 16 02:00 UTC
  - cuda:2: repo-level-cwm-8b-conda-v4 (PID 266816) — CWM 8B 训练，ETA ~May 16 05:00 UTC
  - cuda:3: cwm8b-ckpt400-test-eval (PID 367292) — CWM 8B ckpt-400 全量 test eval，ETA ~May 17 18:00 UTC

### 3. 📊 当前状态
**刚做完**：审稿报告 Round 1 (Weak Reject 2.5/5) 的完整 Action Matrix 处理——Holistic Pass + 17 条逐条方案 + Reviewer 独立审查 + 综合定稿。所有零成本分析已完成（relaxed matching / TOST multi-margin / mutation type / seed variance / 引用修正）。

**关键发现**：
- CLS 8B seed 方差仅 2.08pp（s42=83.52%, s123=85.60%），C1 攻击在 8B 层面已解决（D096）
- 4B 的 8.3pp 方差是 checkpoint 选择 artifact（s123 val-best=ckpt-800 过早）
- 论文主表改用 8B-8B 对比（D096），4B 降为 supplementary
- bib 8 条幻觉作者已修复 + 5 条新引用已添加，Reviewer 确认 PASS
- CWM relaxed matching：即使最宽松匹配 overall 62.34%，仍低于 majority baseline 72.96%

**等待中**：
- rank32 ablation 训练完成 cron 回调 → eval → 决策 rank64
- CLS 8B s42 resume 完成 → eval
- CWM 8B 训练完成 → eval（关键：锁定 8B-8B gap）
- 用户确认 venue 是否从 EMNLP Main 转 Findings（已发消息询问，未收到回复）

### 4. 📋 待办（条件触发式）
- **rank32 cron 回调** → 立即 eval（脚本已就绪 `artifacts/cwm_rank32_eval_command.sh`）→ 检查 unparseable rate：≥50% 直接跑 rank64/alpha128，<40% 先补 rank32/alpha64 消歧
- **rank32 eval 完成** → 汇报 {rank, alpha, scaling, unparseable_rate, accuracy, train_loss} 表格 → cuda:0 接 rank64
- **CLS 8B s42 resume 完成** → 全量 test eval → 更新 multi-seed 主表
- **CWM 8B 训练完成** → 不急提交 final ckpt eval（等 ckpt-400 eval 先出结果再定）
- **cwm8b-ckpt400-test-eval 完成** → 如果 format collapse 仍严重（unparseable >40%）→ 不跑 final ckpt eval，直接用 ckpt-400 数据写论文；如果合理 → 补 final ckpt eval 做对比
- **用户确认 Findings** → 通知 Paper Agent 调整 venue 定位；如果用户坚持 Main → 需补更多实验强化 empirical contribution
- **Paper Agent 需要新数据** → 图表数据 CSV/JSON 已在 artifacts/，Paper Agent 可直接用；rank ablation + CWM 8B 结果出来后补增量数据

### 5. 🎯 战略上下文
- **核心 story**：classification formulation 在 repo-level 复杂度下显著优于 generation（CWM format compliance collapse），函数级两者等价。8B 是主比较（seed 方差小），4B 是 supplementary
- **审稿 4 个 critical 的处置**：C1 已解（8B seed variance 2.08pp）；C2 在跑（CWM 8B）；C3 在跑（rank ablation）；C4 建议转 Findings（等用户确认）
- **CWM 8B eval_loss 持续上升**（step 400: 0.286 → step 4400: 0.482），最优 checkpoint 极可能在 step 400。这本身支持 formulation bottleneck 叙事——generation 即使 scale 到 8B 也极早过拟合
- **易错点**：(1) 不要混淆 4B 和 8B 的 seed variance 数据——4B s123=75.33% 是 artifact，8B s123=85.60% 才是真实表现；(2) rank ablation 的 alpha 必须与 rank 配套，不要默认 alpha=32；(3) main.bbl 需重新编译才能反映 bib 修正，提交前必须确认；(4) cwm8b-ckpt400-test-eval 无 cron，需手动检查或补注册
- **DDL**：ARR May 25（10 天），所有计划实验可在 May 17 前完成，写作并行推进中


---
