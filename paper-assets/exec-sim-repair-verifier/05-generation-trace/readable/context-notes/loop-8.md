# director / loop_8.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`9bfb351295013638ca16.json`](../../sessions/9b/9bfb351295013638ca16.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-14T11:02:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: westd cuda:0-3, home cuda:0。不可动用其他卡
- **D024**: 禁止杀死正在正常训练的进程，必须 Director 审批后才能 kill
- **环境一致性**: apple-to-apple 对比必须同 server + 同 transformers 版本。home=4.57.6, westd conda=4.57.6, westd 系统=5.8.0。跨版本对比无效（D053 证实 22pp 差距）
- **D066**: 主表用 mean±std across valid checkpoints，不再做 val-based checkpoint selection（D065 已放弃，val/test 分布差异太大）
- **seetacloud cgroup 360GB**: 不能并行跑两个训练，单进程安全
- **CWM v11 数字已废止（D055/D057）**: 混合 transformers 版本 checkpoint，论文禁止引用

### 2. 🖥️ 基础设施快照
- **westd**: seetacloud-westd-4x5090 (connect.westd.seetacloud.com:22, user=root)
  - 项目目录: `/root/exec-sim-repair-verifier/`
  - Python (conda): `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` → transformers 4.57.6
  - Python (系统): `/usr/bin/python3` → transformers 5.8.0（**不要用于正式实验**）
  - 模型 checkpoints: `/root/exec-sim-repair-verifier/outputs/repo_*/`
  - 数据: `/root/exec-sim-repair-verifier/data/swebench_{train,val,test}.jsonl`
- **home**: home-1x5090 (implicit5638.xyfu.me, user=sonny)
  - 项目目录: `/home/sonny/exec-sim-repair-verifier/`
  - Python: venv 或系统 python，transformers 4.57.6
  - CLS v5 (home) 和 seed123 (home) 的 checkpoint 在此
- **活跃进程**:
  - westd cuda:0: CWM seed123 eval (ckpt-500, ~25% done, running acc ~57.2%)
  - westd cuda:1: CWM v12 eval (ckpt-500, ~25% done, running acc ~58.5%)
  - westd cuda:2: 8B CWM 训练 (PID 210568, tmux: repo-level-cwm-8b-conda)
  - westd cuda:3: 8B CLS seed123 训练 (PID 210652, tmux: repo-level-cls-8b-seed123-conda)
  - home cuda:0: 状态需确认（D063 val sweep 或空闲）

### 3. 📊 当前状态
- **阶段**: Research → Paper Number Finalization, DDL=EMNLP ARR May 25（剩 11 天）
- **Paper Agent 已激活**（D064）: Full Draft 进行中，CWM 用 ~58% 占位
- **registry RUNNING**: repo-level-cls-8b-seed123-conda, repo-level-cwm-8b-conda
- **等待中**: CWM v12 + CWM seed123 全量 eval 完成（ETA 约 May 14 18:30 UTC）→ 解除 D057 阻塞 → Paper Agent patch 最终数字
- **D063 val sweep**: 已决定放弃 val inference-based selection（D065），改用 Trainer eval_loss 选 checkpoint + mean±std across valid checkpoints 报告（D066）
- **Reviewer session 刚被 RESET**（即本次 handoff 原因）

### 4. 📋 待办（条件触发式）
- CWM v12 eval 完成 → 确认最终 accuracy/F1 → 更新 memory.md 数字 → Paper Agent patch CWM 占位数字
- CWM seed123 eval 完成 → paired bootstrap CLS vs CWM (2 seeds) → 更新 C1 统计显著性
- 8B CWM 训练完成 → checkpoint sweep → eval → 填充 2×2 scaling table (4B/8B × CLS/CWM)
- 8B CLS seed123 训练完成 → eval → 8B multi-seed robustness
- Paper Agent 报告写作进展 → 审批 writing_plan / 处理 Reviewer critical / 补数据请求
- 所有 eval 完成 → Paper Agent 最终 patch → 提交审稿

### 5. 🎯 战略上下文
- **C1 (Complexity-Dependent Advantage)**: 极度稳固。函数级 CLS-CWM gap 1.24pp (p=0.051), 8B 2.43pp (p=0.008)。Repo-level gap 预估 20-27pp（CLS 78-84% vs CWM 57-58%），放大 16-22x。CWM 跌破 majority baseline（72.96%）且 75% 输出不可解析
- **C2 (Diagnostic Granularity)**: ✅ 已完成，TOST p=0.007
- **C3 (Accuracy-Utility Frontier)**: ✅ 已完成
- **最大风险**: checkpoint selection 方法论（D062/D063/D065/D066 链条长且复杂），Reviewer 可能质疑。D066 方案已被 Reviewer 确认 review-proof，但下一个 Reviewer session 需重新建立这个上下文
- **易错点**: 不要混淆 home 和 westd 的实验数字——跨 server 对比无效。CLS v5 (home, 81.51%) 和 CLS v5-conda (westd, 78.43%) 是同超参不同环境，论文主表只用 westd conda 数据做 CLS-CWM 对比
- **决策链**: D001→D006 MVP → D007 reframe complexity-dependent → D008 go/no-go criteria → D052 GO → D054 环境一致性修复 → D056 early stop → D064 启动写作 → D066 reporting strategy


---
