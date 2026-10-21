# director / loop_12.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_12.md`
- **Structured JSON:** [`70d5c4f837e30a7e38bb.json`](../../sessions/70/70d5c4f837e30a7e38bb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-15T09:35:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd cuda:0/1/2/3 + home cuda:0，不得使用其他设备
- D088 铁律：论文主指标必须用 val-selected checkpoint，test 数字只报在 supplementary sweep curve 中
- Val baseline = 75.88%, Test baseline = 72.96%，不要混用（之前 val_sweep_compilation.md 用错过，已修正）
- 同一 GPU 不得并行两个 8B eval（之前两次 OOM 事故：ckpt-1200 和 ckpt-3000 test v2）
- Registry 标 FAILED 前必须 `ps -p PID` 确认进程已退出（幽灵进程导致 GPU 冲突教训）
- home 上的 eval_repo_cls.py 版本与 westd 不同，不支持 --max_new_tokens 参数

### 2. 🖥️ 基础设施快照
- **westd**: seetacloud-westd-4x5090 (connect.westd.seetacloud.com), root, 工作目录 /root/autodl-tmp/
  - Checkpoints: /root/autodl-tmp/checkpoints_repo_cls_8b_conda/ (s42), /root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000 (seed123 val-best)
  - CWM 8B: /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/ (训练中)
  - Eval 脚本: eval_repo_cls.py (支持 --max_new_tokens)
  - conda: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **home**: home-1x5090 (implicit5638.xyfu.me), user=sonny, 工作目录 /home/sonny/exec-sim-repair-verifier
  - 4B checkpoints: /home/sonny/ 下的 repo-level-cls 相关目录
  - eval_repo_cls.py 旧版（不支持 --max_new_tokens）
- **活跃进程**（RESET 前）:
  - westd cuda:1: s42 resume 训练 (~55%)
  - westd cuda:2: CWM 8B v4 训练 PID 266816 (~57%, step ~3800/6633)
  - westd cuda:0/3, home cuda:0: 空闲

### 3. 📊 当前状态
**刚完成**：所有 CLS eval sweep（8B s42 val 8点 + test 7点，seed123 val 5点 + val-best test，4B val 5点 + test 2点）。Multi-seed CLS-CWM gap=25.99pp 锁定 (D093)。Paper Agent 已启动 Full Draft，完成 Step 1-3 (writing_plan + literature)，Step 4 Section Writing 审批通过正在执行。

**Registry RUNNING**: 
- repo-level-cls-8b-s42-resume (westd cuda:1, s42 resume 训练)
- repo-level-cwm-8b-conda-v4 (westd cuda:2, CWM 8B 训练 ~57%)
- cls4b-seed123-ckpt800-test5120-eval (home, 实际已 FAILED，需标记——启动参数错误 EXIT_CODE=2)

**等待中**：
- CWM 8B 训练完成 → 立即提交 test@8192 eval on cuda:3 → 锁 8B-8B direct gap
- s42 resume 训练完成 → extended val sweep on cuda:0
- Paper Agent Step 4 写作产出 → 审批
- 4B seed123 test eval 待修复（去掉 --max_new_tokens 或 sync_code）

### 4. 📋 待办（条件触发式）
- CWM 8B 训练完成 (ETA ~May 16 05:30 UTC) → cuda:3 提交 CWM 8B test@8192 eval → 结果出来后 patch Paper Agent 的 Table 4（8B-8B gap）
- s42 resume 训练完成 (ETA ~May 15 23:00 UTC) → cuda:0 做 extended val sweep（检查 resume 后是否有比 ckpt-1000 更好的 val checkpoint）
- Paper Agent 提交 writing_plan 变更或 Reviewer critical → 审批/方向决策
- 4B seed123 test eval 修复后结果到手 → patch 进 Paper Agent 的 4B-4B multi-seed 数据
- CWM 8B test 结果出炉 → 如果 CWM 8B ~58-60%（与 4B 持平）→ "CWM 瓶颈是 generative complexity 非 model capacity" narrative；如果 CWM 8B 显著好于 4B → 调整跨尺寸 gap 叙述

### 5. 🎯 战略上下文
- **核心结论**：Classification >> Generation at repo-level (25.99pp mean gap, 2 seeds)。Function-level near-null (1.24pp) 是 story 关键部分——证明 advantage 不是因为 task trivially easier。
- **决策链**：D007(complexity-dependent framing) → D063(val sweep) → D087(val-test分布偏移根因) → D088(val-selected策略) → D093(multi-seed锁定)
- **易错点**：
  1. 论文 headline gap 必须用 same-size 比较（4B-4B: 25.59pp），不是跨尺寸（8B CLS vs 4B CWM）——Reviewer 已指出
  2. seed123 ckpt-3000 在备份路径 `/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000/`，不在主训练目录
  3. save_total_limit 问题：seed123 中段 checkpoint 已丢失（默认 limit=5），但 s42 resume 设了 limit=35 安全
  4. DDL = EMNLP ARR May 25（还剩 10 天），Paper Agent 已在写，不要重新规划实验方向
  5. home eval 脚本版本不同——之前多次 4B eval 在 home 成功是因为没传 --max_new_tokens


---
