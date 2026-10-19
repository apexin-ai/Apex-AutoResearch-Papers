# agent / loop_3.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`6670100a002b574866a1.json`](../../sessions/66/6670100a002b574866a1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-13T21:48:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：bjb1-42106 的 cuda:0 和 cuda:1（之前在 cqa1 cuda:0 违规被 CRITICAL 两次）
- `/root/structfuse` 已重命名为 `/root/structfuse-context`，符号链接 `/root/structfuse → /root/structfuse-context` 存在。所有新脚本用新路径，旧路径通过 symlink 兼容运行中进程
- submit_training_job wrapper 的 `> log 2>&1` 会覆盖用户命令中的 tee。m2_full_qwen 脚本已修复（Worker kill_347730_fix_tee 结果待确认），后续 runs 不要再加 tee
- n=3 seeds，统计检验 df=2，t 临界值 4.303。不要对 pilot 级差异声称显著——D019/D020 已锁定 go/no-go 阈值，结果出来前不修改
- 措辞红线：不用 "StarCoder already knows" 等因果性表述，用 "pretrained representation separability varies across encoders"

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106，2× RTX PRO 6000 96GB
- 工作目录：`/root/structfuse-context`（symlink `/root/structfuse` → 此处）
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 数据：`/root/autodl-tmp/structfuse/`（M1 all.jsonl 6.6GB, M2 训练数据, checkpoints, wandb_logs）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 模型：Qwen/Qwen2.5-Coder-3B, bigcode/starcoder2-3b
- 活跃进程：
  - m2_full_qwen: PID 73544 (tmux), cuda:0, cron 已注册 600s
  - m2_full_starcoder: PID 74122 (tmux), cuda:1, cron 已注册 600s。**注意**：PID 76627 是实际 StarCoder 训练进程，PID 347730 重复进程已下令 kill（Worker 结果待确认）
  - m1_reextract_v2: PID 209827 + 4 CPU worker 子进程, cron 已注册 10min
- CodeQL：`/opt/codeql/codeql`，pack 已安装（之前 100% 查询失败的根因是缺 python-all pack）

### 3. 📊 当前状态
**刚做完：**
- 目录重命名 `/root/structfuse` → `/root/structfuse-context` + symlink（验证通过，进程/GPU 均正常）
- M2 训练 cron 补注册（session 重启时发现丢失）
- Session-start 初始化（registry + reconcile + ROADMAP 同步）

**正在等待 3 个 Worker 回调：**
1. `worker_ssh_kill_347730_fix_tee` — kill StarCoder 重复进程 + 修复 qwen tee 日志问题
2. `worker_ssh_neg_difficulty_2048_results` — 读取 MAX_LENGTH=2048 negative difficulty 分析结果（原 Worker 提前退出，派了读结果的 Worker）
3. `worker_research_plan_017_graph_methods` — inference-time graph method 文献对比（CodexGraph/LocAgent/RANGER 等）

**Registry RUNNING：**
- `m2_full_qwen`: 9 runs (random/embedding/dataflow × seeds 42,43,44)，random_s42 约在 step 500+
- `m2_full_starcoder`: 9 runs 同配置，可能还在 Phase 1 数据构建或刚开始训练
- `m1_reextract_v2`: 28,276 instances, 4 CPU workers, ~60h 预估，已运行 ~2h

**Registry PREPARING：**
- `neg_difficulty_analysis`: 等 2048 结果后更新

### 4. 📋 待办（条件触发式）
- `worker_ssh_kill_347730_fix_tee` 回调 → 确认 kill + tee 修复成功 → 更新 registry notes → 汇报 Director
- `worker_ssh_neg_difficulty_2048_results` 回调 → 对比 v1(128) vs v2(2048) margin 数据 → 更新 `neg_difficulty_analysis` registry（PREPARING→DONE） → 汇报 Director 结论是否成立
- `worker_research_plan_017_graph_methods` 回调 → 检查对比表质量 → 注册 artifact → 汇报 Director
- M2 cron 回调（进程退出）→ 按 on-experiment-done skill 处理：分析结果 → D019/D020 go/no-go 判定 → 汇报 Director
- m1_reextract_v2 cron 回调（完成）→ 统计恢复率 → 更新 m1_extraction metrics → 评估是否需要用扩增数据重训 M2
- M2 全部完成 → plan_014 temperature ablation（P1，~10h）+ plan_003 SWE-bench eval（P0，需 Qwen checkpoint）
- 训练全部结束 → 删除 symlink `/root/structfuse` + sed 批量替换 14 个文件中硬编码路径

### 5. 🎯 战略上下文
- **核心 story**：CodeQL inter-procedural data-flow → structure-grounded hard negatives → 对比式代码检索训练。3 个 Claims：(1) dataflow negatives improve retrieval, (2) embedding negatives 反而有害, (3) CodeQL extraction scales
- **决策链关键节点**：D018 = full M2 是 go/no-go 唯一依据；D019/D020 = 量化阈值已锁定；D022 = M1 28K 可恢复
- **Pilot 信号**：embedding > random 跨编码器一致（+2pp Qwen, +1.6pp StarCoder）；dataflow mixed（Qwen +0.8pp, StarCoder -0.5pp）→ Claim 1 可能落入 Conditional Go (B)
- **易错点**：
  - plan_006 scalability 已完成（全量 44K instances），不要重做
  - neg_difficulty v1 用 128 tokens 有 ceiling effect，必须用 v2 (2048) 数据。如果 v2 Worker 结果仍然缺失，需要直接 SSH 检查 `/root/autodl-tmp/structfuse/artifacts/` 下的产出文件
  - M2 wrapper 脚本循环跑 9 runs，中间某个 run 失败不代表整个实验失败——检查日志确认哪些 runs 完成了
  - StarCoder PID 74122 是 bash wrapper，实际训练 PID 可能已变（76627 或新进程）。kill_347730 是清理重复进程，不是 kill 训练本身


---
