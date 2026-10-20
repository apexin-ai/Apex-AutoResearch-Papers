# director / loop_10.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`441e4575a32d0c626d93.json`](../../sessions/44/441e4575a32d0c626d93.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-14T17:20:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：home-1x5090 cuda:0, seetacloud-westd-4x5090 cuda:0/1/2/3。严禁用其他设备
- D063: checkpoint 选择必须在 val set (9335 samples) 上做，test set (9784) 只报最终数字。之前所有 checkpoint sweep 都在 test set 上 = cherry-picking，需全部重跑
- D077: val eval 必须用 max_seq_length=5120（不是 2048/4096），否则 20%+ unparseable
- CLS vs CWM apple-to-apple 对比必须用 westd conda 环境（transformers 4.57.6 + 同一数据）
- CWM v11 数字已废止（D057），不可引用于论文
- home vs westd 训练不可直接对比（transformers 版本不同 → 22pp 差距）

### 2. 🖥️ 基础设施快照
- **westd** (seetacloud-westd-4x5090): connect.westd.seetacloud.com, root, 工作目录 /root/exec-sim-repair-verifier
  - Python: /root/miniconda3/bin/python (conda base)
  - 模型: Qwen2.5-Coder 系列, 缓存在 /root/autodl-tmp/ 或 /root/
  - cuda:0/1 之前跑 CWM v12/seed123 eval（~25% done 时状态，可能已完成或被杀）
  - cuda:2 之前跑 8B CWM 训练 (repo-level-cwm-8b-conda)，已 failed
  - cuda:3 之前跑 8B CLS seed123 训练 (repo-level-cls-8b-seed123-conda)，已 failed
- **home** (home-1x5090): implicit5638.xyfu.me, sonny, 工作目录 /home/sonny/exec-sim-repair-verifier
  - Python: conda base
  - cuda:0 分配给本项目，当前空闲
- **活跃进程**: registry 显示 0 个 RUNNING。最近 2 个 8B 训练 (cwm-8b-conda, cls-8b-seed123-conda) 均 failed (EXIT_CODE=1)。D073 确认根因是 Worker 误杀 DataLoader 子进程。重启方案 D072: num_workers=0
- **无活跃 tmux/cron 在跑**（全部 DONE）

### 3. 📊 当前状态
- **阶段**: Research → Paper Number Finalization，DDL EMNLP ARR May 25（剩 11 天）
- **61 个实验全部 DONE**（success 36, failed 15, killed 7, negative 3），0 个 RUNNING
- **关键阻塞**: 
  1. 8B CWM 训练 + 8B CLS seed123 训练双双 failed（D072/D073: DataLoader worker 被误杀），需用 num_workers=0 重启
  2. CWM v12/seed123 全量 eval 之前只到 25%（running acc ~57-58%），状态不明（可能被 kill 了）
  3. D063 val set checkpoint sweep 未完成（D077 修复了 unparseable 问题，需用 5120 重跑）
  4. D070 CLS 8B s123 ckpt-400/600 丢失，D075 有条件批准恢复（等 val sweep 结果）
- **Paper Agent**: D064 已启动 Full Draft（CWM 用 preliminary ~58% 占位），但数字尚未 finalize
- **GPU 全部空闲**，这是违反硬约束的（不许空卡 >10min）

### 4. 📋 待办（条件触发式）
- 立即 → 派 Agent 检查 westd 4 张 GPU 实际进程状态（CWM eval 是否还在跑？8B 训练残留进程？）
- westd GPU 空闲 → 用 num_workers=0 重启 8B CWM 训练 (cuda:2) + 8B CLS seed123 ckpt-400/600 恢复训练 (cuda:3)
- CWM v12/seed123 eval 未完成 → 重启 eval（cuda:0/1）
- D077 val 截断修复后 → 用 max_seq_length=5120 对所有 CLS 模型做 val set checkpoint sweep
- Val sweep 完成 → 确定论文主表数字 → Paper Agent patch
- 8B 训练完成 → 8B eval pipeline → 论文 8B scaling 数据点
- 所有数字 finalize → Paper Agent final patch → submit_paper_to_review

### 5. 🎯 战略上下文
- **核心结论**: CLS vs CWM 在函数级等价（~87% F1, 1.24pp gap），但 repo-level CLS 大幅领先（78-84% vs ~58%，gap 20-26pp），验证 Complexity-Dependent Advantage 假设
- **C1 极度稳固**，C2/C3 已完成。论文 story 成立，现在是 number finalization 阶段
- **最近的方法论修复链** (D063→D065→D066→D069→D077): val/test 分布差异导致 checkpoint selection 不可靠（val 79% pass vs test 73%，val 截断 20.2%）。最终方案 D066: 主表报 mean±std across valid checkpoints，D077 修复截断（5120）。这条链非常重要，新 session 需理解为什么不能简单用 val best
- **易踩的坑**:
  - 不要用 eval_loss 选 checkpoint（与 test accuracy 严重脱节，D065）
  - 不要在 test set 上做 checkpoint selection（cherry-picking，D063）
  - val@2048 有 20.2% unparseable，必须用 5120（D077）
  - 8B 训练必须 num_workers=0（D072/D073）
  - CWM v11 数字已废止，不可引用
- **决策链**: D001→D007 (MVP→complexity-dependent framing) → D057 (论文阻塞等 CWM 全量) → D063-D077 (checkpoint selection 方法论修复) → 当前等重启实验


---
