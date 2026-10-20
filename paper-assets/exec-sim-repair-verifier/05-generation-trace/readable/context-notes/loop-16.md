# director / loop_16.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_16.md`
- **Structured JSON:** [`544997fc430242d4ee82.json`](../../sessions/54/544997fc430242d4ee82.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-16T13:48:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 seetacloud-westd-4x5090 的 cuda:0/1/2/3，home-1x5090 已从项目移除（长期离线）
- D112: re-repair 实验不写入论文（含 Discussion），纯 future work
- D114: DeepSeek TRAJ v1 数据（82.27±1.23%）已作废——train/eval 格式不匹配（train pass/fail, eval resolved/unresolved）。**绝不能用 v1 数字**，必须用 v2 重训结果
- D109: repo-level 不 claim "gap widens with scale"，只 claim absolute magnitude + generation degradation
- cwm-repo 的 total steps 是 13266（grad_accum=8, effective_batch=16），不是 6633
- 论文 func-level 锁定数字: CLS 86.85±0.11%, CWM 86.83±1.49%, gap 0.02pp（不要用 Agent 偶尔汇报的错误数字 87.88%）

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-westd-4x5090 (connect.westd.seetacloud.com)
- 工作目录：/home/sonny/exec-sim-repair-verifier
- Python/conda：aml-train 镜像，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：DeepSeek-Coder-6.7B-Instruct（已下载到服务器）
- 训练脚本：train_unified.py (CLS/CWM), train_traj_verifier.py (TRAJ)
- Eval 脚本：eval_repo_verifier.py (CLS), eval_repo_cwm.py (CWM), eval_traj_verifier.py (TRAJ), run_deepseek_repo_eval.sh
- 活跃进程：
  - cuda:0: deepseek-cls-repo PID 470263 (~30%, ETA May 17 04:00 UTC)
  - cuda:1: deepseek-cwm-repo PID 479953 (~14%, ETA May 17 14:00 UTC)
  - cuda:2: deepseek-traj-func-v2 s42 PID 511676 (~53%, ETA ~14:10 UTC today)
  - cuda:3: deepseek-traj-func-v2-s123 PID 513110 (~2%, ETA ~14:30 UTC today)
- 所有 4 个实验都有 cron 监控

### 3. 📊 当前状态
刚完成 DeepSeek TRAJ v1 → Reviewer CRITICAL → D114 作废 → v2 重训已启动（cuda:2/3）。

**RUNNING**:
- deepseek-cls-repo: cuda:0, 30%, repo-level CLS 训练
- deepseek-cwm-repo: cuda:1, 14%, repo-level CWM 训练（13266 steps）
- deepseek-traj-func-v2: cuda:2, 53%, func-level TRAJ 正确重训 (train_traj_verifier.py)
- deepseek-traj-func-v2-s123: cuda:3, 2%, func-level TRAJ s123 正确重训

**等待中**:
- TRAJ v2 s42 完成回调 (~14:10 UTC) → eval → 汇报
- TRAJ v2 s123 完成回调 (~14:30 UTC) → eval → 汇报
- cls-repo 完成 (~May 17 04:00) → repo eval on cuda:3
- cwm-repo 完成 (~May 17 14:00) → repo eval on cuda:2

论文 v41, consistency 0 critical / 0 warning。Paper Agent 已完成 DeepSeek CLS 2-seed mean patch。

### 4. 📋 待办
- TRAJ v2 s42 eval 完成 → 收集 accuracy，与 CLS/CWM 对比。Reviewer 需验证 v2 方法论一致性
- TRAJ v2 s123 eval 完成 → 计算 2-seed mean ± std，确认 CLS≥TRAJ 跨模型是否成立
- TRAJ v2 两个 seed 都出来 → 如果方法论 OK，与 repo-level 结果合并做一次 Paper Agent 最终更新
- cls-repo 训练完成 → cuda:3 跑 `eval_repo_verifier.py --split test --max_seq_length 8192` (n=9784, val-best ckpt)
- cwm-repo 训练完成 → cuda:2 跑 `eval_repo_cwm.py --split test --max_seq_length 8192` (n=9784, val-best ckpt)
- 两个 repo eval 齐全 → 如果 gap >15pp + unparseable >50%，升级 generalizability claim 到 "consistent across model families"
- 全部结果齐全 (预计 May 17 18:00 UTC) → Paper Agent 最终 patch（DeepSeek TRAJ + repo-level + claim 升级）→ submit_paper_to_review

### 5. 🎯 战略上下文
- 核心论文：CLS vs CWM vs TRAJ for code repair verification。CLS 优势随复杂度增长（func 1-2pp → repo 19-26pp）
- DeepSeek 跨模型验证是 D108 scope 扩展，封堵 "single model family" 攻击面
- func-level: CLS≈CWM 跨模型确认 (gap 0.02pp)。TRAJ 待 v2 结果
- repo-level: Qwen3 数据全部锁定，DeepSeek 是最后一块拼图
- 关键决策链: D108(scope扩展) → D109(CWM8B叙事) → D110(func跨模型) → D112(re-repair不写) → D113(TRAJ纳入)→D114(TRAJ v1作废重训)
- 易错点：Agent 有时汇报错误数字（CLS s123=87.88% 实际是 CWM s123 的数字），论文数字以 Paper Agent 锁定版本为准
- 易错点：TRAJ 训练必须用 train_traj_verifier.py 不是 train_unified.py --task cls（D114 教训）
- DDL: EMNLP 2026 ARR May 25, 剩 9 天，时间充裕
- 审稿阶段已启动 (review_chat_id: oc_0ae20ec1ce60f9c0589d629648584eff)，Research Director 不参与审稿流程


---
