# director / loop_15.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_15.md`
- **Structured JSON:** [`b39c990cb2120d53e4f1.json`](../../sessions/b3/b39c990cb2120d53e4f1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_messages
updated: '2026-05-15T18:16:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（4 张卡，服务器 autodl-l40s-4）
- CWM 8B 最终结果必须基于 checkpoint-400（step 400 best，后续严重过拟合），不是训练结束时的 checkpoint
- 修改 seq_length / batch_size / precision / lr 等训练超参需要 Director 审批（D103 决策）
- checkpoint-400 路径已确认存在且完整（adapter_model.safetensors 61MB），save_total_limit=5 因 best_model 保留

### 2. 🖥️ 基础设施快照
- 服务器：autodl-l40s-4，工作目录需从 `load_project_config("exec-sim-repair-verifier", section="execution")` 获取
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/`
- 现存 checkpoint：400, 4900, 5000, 5100, 5200
- 活跃实验（截至 handoff 时刻）：
  - cuda:0: val-sweep-seq8192-v2（ckpt-1800 1/21, ETA ~May 16 10:50 UTC）
  - cuda:1: cls-8b-s42-resume 训练（94.4%, ETA ~May 16 02:10 UTC）
  - cuda:2: cwm-8b-v5 resume（模型加载中, ETA ~May 16 06:00 UTC）
  - cuda:3: cwm8b-ckpt400-test-eval（17.4%, ETA ~May 16 17:10 UTC）

### 3. 📊 当前状态
刚处理完 Reviewer 对 method.tex 的审查报告（3 个 WARNING 全部修复），Paper Agent 已完成两轮 patch：超页压缩（10页→9页，正文~7.7页满足 ACL 8页限制）+ method.tex WARNING 修复。check_paper_consistency 0 critical 0 warning。

关键发现：CWM 8B 严重过拟合（step 400 eval_loss 0.286 → step 5200 eval_loss 0.507）。ckpt-400 确认存在，基于 ckpt-400 的 test eval 在 cuda:3 跑。

等待中：
- 4 个实验的完成回调
- Paper Agent 待办：CWM 8B repo-level 结果出来后填 Table 4 + 8B-8B 对比 + 更新 abstract/intro/conclusion + Step 5e 三件套

### 4. 📋 待办
- cwm8b-ckpt400-test-eval 完成 → 汇报 Director，这是论文 CWM 8B 的最终数据
- cls-8b-s42-resume 完成 → 汇报结果，与之前的 CLS 8B 结果对比
- cwm-8b-v5 resume 完成 → 提取完整 training curve（用于论文展示过拟合趋势），确认 v5 用的脚本参数是否与 8B 一致（Agent 已标注 ⚠️ 用了 train_repo_cwm.py 而非 train_repo_cwm_8b.py）
- val-sweep-seq8192-v2 完成 → 21 个 checkpoint 的 val 结果用于 scaling analysis
- 所有 8B 结果就绪 → 派 Paper Agent 做 CWM 8B Patch（Table 4 + 对比 + abstract/intro/conclusion 更新）+ Step 5e 三件套

### 5. 🎯 战略上下文
- 项目核心：对比 CLS vs CWM 两种 execution-simulation verification formulation，CLS 显著优于 CWM（尤其 repo-level）
- CWM 8B 过拟合是重要发现——论文需要展示 training curve 说明即使增大模型，CWM 的 format compliance collapse 仍是根本瓶颈
- 论文目标：ACL 投稿，8 页限制（references 不计入）
- 项目处于审稿阶段（review_chat_id 已配置），Review Director + 2 Reviewers 并行审稿
- Paper Agent 延迟项（experiments/limitations 中处理）：exact match fairness、ICC exchangeability assumption、TRAJ context window disadvantage
- 易错点：v5 resume 用了 train_repo_cwm.py 而非 train_repo_cwm_8b.py，需确认参数一致性


---
