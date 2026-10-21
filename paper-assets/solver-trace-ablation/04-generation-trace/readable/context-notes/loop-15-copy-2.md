# reviewer / loop_15.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_15.md`
- **Structured JSON:** [`d6aeffa091bee3c96cc6.json`](../../sessions/d6/d6aeffa091bee3c96cc6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-16T15:07:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0, cuda:1（westd-39279 双卡 H800 97GB）
- 数据盘 `/root/autodl-tmp/` 曾 100% 满导致训练崩溃，现已清理到 45%（111G/250G）——新实验前必须确认剩余空间 > 30G
- ISR-gated 实验 checkpoint 每个约 15-20G（4B 模型），一个实验 500 步约存 10 个 checkpoint = 150-200G，必须设 `save_total_limit`
- 1.7B 实验发现的 H9 (ex falso quodlibet) 是新 hacking 类型——ISR threshold=0.2 可能放行 H9（ISR≈0.26 > 0.2），需要 `n_comp > 2` 联合阻止

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279(root)，工作目录 `/root/solver-trace-ablation`
- Python：`/root/miniconda3/bin/python`（conda base env）
- 模型：`/root/autodl-tmp/models/Qwen3-4B`, `/root/autodl-tmp/models/Qwen3-1.7B`
- 数据：`/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl`（100样本），`data/train_500_seed42.jsonl`（500样本）
- 输出：`/root/autodl-tmp/outputs/`
- 日志：`/root/runs/solver-trace-ablation/`（旧实验），`/root/autodl-tmp/outputs/isr_gated_curriculum_s42.log` / `s43.log`（当前活跃）
- W&B：project=solver-trace-ablation（curriculum-r2 可能启用了 wandb）
- 活跃进程：curriculum-r2 双卡运行中（cuda:0 + cuda:1, step ~50/500）

### 3. 📊 当前状态
**刚完成**：审查 ISR-gated 系列实验（t03 失败 → curriculum-t02 磁盘满崩溃 → curriculum-r2 正在运行）

**活跃实验**：
- `isr_gated_curriculum_s42`：step 52/500，warmup 阶段，step 51 首次 prove_rate=1.0 (ISR=0.571)
- `isr_gated_curriculum_s43`：step 49/500，warmup 阶段，step 49 首次 prove_rate=1.0 (ISR=0.143)

**已 post 给 Director**：
1. [warning] ISR-gated t03 确认失败 + curriculum 设计隐患（threshold=0.2 可能放行 H9）
2. [critical] 磁盘满 + warmup 数据效率问题（已解决：清理磁盘 + 切小数据集）

**等待中**：curriculum-r2 到 step 100 Phase 2 激活，观察 gate 能否过滤 hacking

### 4. 📋 待办
- curriculum-r2 step ~80-100 → 检查 warmup 是否建立稳定 prove 能力；如果仍是 all-or-nothing（8/8 或 0/8），Phase 2 会因 frac_reward_zero_std=1.0 而无梯度
- Phase 2 激活后（step 101+）→ 观察 gate 过滤效果：如果 step 120+ 仍全零 → gate 过严，需报 Director
- Phase 2 出现 constant ISR≈0.26 模式 → H9 exploit 绕过了 gate，需 critical 报告
- 如果 prove_rate 上升且 gate 通过 → 跟踪 genuine 率，与 4B additive_bonus 对比
- PENDING 实验 plan018-random-b01-s46 和 plan001-exec-only-s46 → GPU 空闲时提醒 Director 启动

### 5. 🎯 战略上下文
**核心论文 story**：ISR reward 导致 Goodhart 效应（8→9 种 hacking 模式），ISR-gated 是潜在解法。

**决策链关键节点**：
- D108：8B OOM → pivot 到 1.7B cross-scale
- 1.7B ISR pilot → 发现 H9 (ex falso quodlibet, 93/100, constant ISR≈0.26, 0% genuine)
- ISR-gated 方案：threshold=0.3 完全封死 → 降到 0.2 + warmup=100 + 小数据集

**易错点**：
- 不要把 warmup 阶段的 prove 信号当成功——warmup 是 exec-only，任何 hack 都拿满分，真正考验在 Phase 2
- s42 step 51 的 ISR=0.571 很可能是 H7 类 exploit（单前提 tautology），不是 genuine
- GRPO 需要 within-group reward variance；当 prove_rate=1.0 (8/8) 时 reward_std=0，无法学习——这��� K=8 + easy problems 的结构性问题
- gated-isr-t03-s43 registry 标了 RUNNING+conclusion=failed 的奇怪状态（cron 已报 failed 但进程实际已死）


---
