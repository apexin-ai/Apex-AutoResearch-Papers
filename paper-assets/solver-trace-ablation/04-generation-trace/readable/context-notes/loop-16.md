# agent / loop_16.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_16.md`
- **Structured JSON:** [`90792b9d0e057f0c8f43.json`](../../sessions/90/90792b9d0e057f0c8f43.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: idle_timeout
updated: '2026-05-16T03:48:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 westd-39279:cuda:0 和 cuda:1**，无其他 GPU 可用，Director 指令也不能覆盖
- 训练脚本路径：`python3 scripts/train_grpo.py --config configs/...`（不是 `train_grpo.py`），首次提交曾因缺 `scripts/` 前缀导致 GPU 空转
- ISR β=0.1 实验必须用 `configs/grpo_additive_bonus_b01.yaml`（Reviewer 要求追溯一致性）
- K=4 已全量确认（D099/D100）：`per_device_batch_size=2, num_generations=4, B×K=8`。所有新实验必须 `--num_generations 4`，不要用 8
- D095 Narrative A 已批准生效——H7a GRPO-general + H7b ISR-specific，任何 paper 修改不得偏离此 framing
- genuine rate ISR 6.06% vs Random 9.54% p=0.182 **不显著**，禁止 claim genuine rate 有显著差异

### 2. 🖥️ 基础设施快照
- **服务器**：westd-39279，account=root
- **工作目录**：`/root/solver-trace-ablation`
- **Python**：`/root/miniconda3/bin/python`（conda base 环境，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **输出目录**：`/root/autodl-tmp/outputs/` (训练输出)
- **Qwen3-8B 下载**：已有 Worker 下载过，但未确认完成——需 SSH 检查 `/root/autodl-tmp/` 下是否有 8B 模型
- **W&B**：项目使用 W&B 记录训练指标，config merge bug（D097）曾导致 `no_wandb` 被强制 true，**已修复**（train_grpo.py line 393 移除 boolean 分支 + YAML 移除 no_wandb 字段）
- **活跃进程**：sweep-isr-b01-s45（cuda:0）和 sweep-isr-b005-s42（cuda:1）的 tmux 被 cron 误杀，但 **Python 孤儿进程可能仍在运行**——b005 ~241/500 步时被杀（约 11min 剩余），b01 ~92/500 步（约 68min 剩余）。monitor Worker `worker_monitor_cuda1-b005-completion_20260516T034110` 仍在运行中监控 b005
- **Cron**：reconcile_crons 返回 0 条活跃 cron（均已清理）

### 3. 📊 当前状态
**刚做完的事**：
1. 修复了 config merge bug（D097/D098）：argparse 默认值覆盖 YAML config 的 boolean 字段问题
2. K=4 全量 SSH 验证 + 论文修正（D100）
3. Round 2 排期（D101）：β=0.2 ISR 为 P1，5-seed 扩展为 P3
4. paper Round 2 fixes：H8 样本数、σ 符号、SFT 92.3%、RW softening（最新 commit 8fd6215）

**Registry 状态**：
- DONE: 88（success 26 / negative 28 / killed+failed 34）
- PREPARING: 17（Round 2 sweep 实验全部就绪待提交）
- RUNNING: 0（两个 sweep 已转 DONE/killed，但孤儿进程可能还在跑）

**等待中**：
- Worker `worker_monitor_cuda1-b005-completion_20260516T034110`（running）正在监控 cuda:1 上 sweep-isr-b005-s42 的孤儿进程
- sweep-isr-b01-s45 的孤儿进程（cuda:0）无人监控，需要检查

### 4. 📋 待办（条件触发式）
- **monitor Worker 回调到达** → 检查 b005-s42 孤儿进程是否完成训练；如果完成，从 `reward_log.jsonl` 提取 metrics → 更新 registry → 分析结果
- **确认 cuda:0 b01-s45 孤儿进程状态** → spawn Worker SSH 检查 `ps aux | grep train_grpo`；如果还在跑等完成，如果已结束从 reward_log.jsonl 提取 metrics
- **两个 sweep 都完成且数据可用** → 分析 β=0.05 和 β=0.1 s45 结果 → 更新 registry（conclusion 应改为 success/negative 而非 killed）→ 汇报 Director
- **GPU 空闲后** → 按 D101 排期提交 P1：sweep-isr-b02-s42 + sweep-isr-b02-s43（cuda:0 和 cuda:1 并行）
- **β=0.2 三 seed 完成** → 填 0.1↔0.3 剂量间隙 → 更新 paper dose-response narrative
- **w2-qwen3-7b-pilot** → DEFER 到投稿后/rebuttal（D101 决策）

### 5. 🎯 战略上下文
**项目核心**：STA/ISR 作为 GRPO neurosymbolic formalizer 的诊断工具 + Goodhart's Law 案例研究。三个 Core Claims 全部闭环，论文处于 Writing + Review 阶段。**DDL 2026-05-25（9 天）**。

**决策链关键节点**：
- D095: Narrative A 生效（H7a GRPO-general seed-dependent + H7b ISR-specific）
- D097/D098: config merge bug 修复 + sweep 重跑
- D100: K=4 confirmed（非 K=8）
- D101: Round 2 排期确定

**最容易判断错的事**：
1. sweep-isr-b01-s45 和 sweep-isr-b005-s42 在 registry 中是 DONE/killed，但**实际训练可能已在孤儿进程中完成**——不要当作失败实验重新提交，先 SSH 检查 reward_log.jsonl 是否有完整 500 步数据
2. 17 个 PREPARING 实验中有重复——`plan001-exec-only-s45` 和 `sweep-exec-only-s45` 是同一个意图的不同 ID，提交时只跑一个
3. Random H7 pooled 13.7% 由 s43-r3 单 seed 贡献（38.3%），写论文时极易滑向 "ISR amplifies H7 5x" 的简单对比——必须同时报 per-seed
4. 不要用 `--num_generations 8`，所有实验统一 K=4


---
