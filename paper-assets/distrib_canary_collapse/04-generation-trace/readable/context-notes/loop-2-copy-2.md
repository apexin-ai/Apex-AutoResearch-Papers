# agent / loop_2.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`bb226ff7e1c7fc374ac0.json`](../../sessions/bb/bb226ff7e1c7fc374ac0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T21:05:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 westd-19828 的 cuda:0 和 cuda:1，不可用其他设备
- **kill_job 不杀子进程**：kill 后必须 `ps aux | grep python` 确认子进程死亡，否则会出现幽灵进程写同一输出目录（a025_s42 事故已发生两次）
- submit_training_job command 必须 `bash -c "..."` 包裹（tmux 用 sh 不是 bash）
- α-sweep 所有 run 必须用修复后的代码（双向 subsample + shuffle(seed=seed) + EXIT_CODE 哨兵），旧版 257 行代码已备份为 .bak.mvp 和 .bak.v2
- a000_s42 (α=0.0) 不受 subsample bug 影响可继续；任何 α>0 的实验必须确认远程 iterative_train.py 含 shuffle

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828，用户 root
- 工作目录：`/root/autodl-tmp/distrib_canary_collapse`
- Python：`/root/miniconda3/bin/python`，conda base，PyTorch 2.10.0+cu128
- 激活命令：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 2× RTX PRO 6000 Blackwell 96GB
- HF cache：`/root/autodl-tmp/.hf_cache`，HF_ENDPOINT=https://hf-mirror.com
- 模型：EleutherAI/pythia-410m（已缓存）
- 数据：`data/wikitext103_5k/`（5000 prompts from train split）
- MVP 结果：`results/mvp/rep_42/` ~ `rep_45/`（4 seed 全部 DONE success）
- α-sweep 结果：`results/alpha_sweep/`（a000_s42 运行中，a025_s42 可能被 fix worker 清理重启）
- 分析脚本：`analyze_mvp.py`, `method_ablation.py`, 可能新增 `dmax_sensitivity.py`
- 活跃进程：a000_s42 (PID 46716, tmux=alpha_sweep_a000_s42, cuda:0, Gen 4/10)
- a025 状态不确定——fix-a025-corruption worker 可能已 kill 并重启为 v3

### 3. 📊 当前状态
**刚完成**：
- MVP 4-seed 正式分析：STRONG PASS，token_entropy 和 ECE lead diversity 1-2 gen
- max_lag=7 重分析：无截断伪影，lag=-5 是真实信号但 p borderline
- 方法论 ablation (plan_002 Phase 1)：**75% 伪回归率**，token_entropy 是唯一 gold-standard canary（Granger 因果），ECE 仅对 distinct_1 有效
- mix_datasets bug 修复（双向 subsample + shuffle）+ EXIT_CODE 哨兵 + 部署到远程
- rep44 registry 修正（conclusion: success, wall_clock: 15134s/4.20h）

**等待回调的 Worker**：
- `worker_ops_fix-a025-corruption_20260514T210319`：kill 旧进程 + 清理损坏数据 + 重启 a025_s42_v3
- `worker_analysis_dmax-sensitivity_20260514T210356`：d_max 敏感度分析（d_max=0/adaptive/1 三组 TY）

**Registry RUNNING/PREPARING**：
- alpha_sweep_a000_s42: RUNNING (cuda:0, Gen 4/10, ~2h 剩余)
- alpha_sweep_a025_s42_v2: 状态待 fix worker 确认（可能被 kill 并替换为 v3）

**等待 Director 决策**：
- narrative 是否据方法论 ablation 结果调整 paper_framing.md

### 4. 📋 待办（条件触发式）
- fix-a025-corruption worker 完成 → 确认 a025_s42_v3 RUNNING，更新 registry
- dmax-sensitivity worker 完成 → 汇报 Director，重点看 ECE 是否在 d_max=1 下恢复 canary 地位
- a000_s42 完成（cron 回调）→ 收集 metrics → update_registry(DONE, success) → **立即** submit a000_s43 (cuda:0, seed=43, α=0.0, plan_001)
- a025_s42_v3 完成 → 收集 metrics → **立即** submit a025_s43 (cuda:1, seed=43, α=0.25, plan_001)
- cuda:0 序列：a000_s42 → a000_s43 → a000_s44 → a050_s42 → a050_s43 → a050_s44 → plan_006_s42 (20-gen)
- cuda:1 序列：a025_s42_v3 → a025_s43 → a025_s44 → a075_s42 → a075_s43 → a075_s44 → plan_006_s43 (20-gen)
- 每个 run 完成后立即提交下一个，不等批量。每个实验 plan_id=plan_001（α-sweep）或 plan_006（extended）
- plan_006 完成 → 执行 memory.md 中的分析 checklist（full series CCF + rolling-window gen 5-20 + TY 主检验）
- Director 批准 narrative 调整 → 读 framing-reaudit skill → 全文 re-audit

### 5. 🎯 战略上下文
**核心结论链**：
- D001: MVP 设计 Pythia-410M × WikiText-103 × 100% SC × 10 gen × 4 seeds
- D005: MAUVE demote 为 supplementary（floor effect）
- MVP STRONG PASS: token_entropy 和 ECE lead diversity 1-2 gen，但不 lead perplexity
- **方法论 ablation 改变了 story**：75% naive 显著关联是伪回归。token_entropy 是唯一真 canary。ECE 大幅缩水。论文 Claim 3（方法论贡献）从 nice-to-have 变为 essential

**易错点**：
- **不要信 cross-correlation 结果**——必须用 Toda-Yamamoto 做主检验。ECE→distinct_2 的 "完美" lag=-1 (std=0, 4/4 seed) 是伪回归
- **α-sweep 代码版本**：远程已是修复版（293行 + shuffle），但 kill 进程时必须确认子进程死亡（不能只杀 tmux）
- **token_entropy→perplexity lag=-5**：真实信号但 p borderline，瓶颈是统计功效（10 gen 太少），plan_006 (20-gen) 是解决方案
- **α=0.0 是 null control**（纯 real，不涉及 mix_datasets），任何 canary signal = fine-tuning artifact 而非合成污染


---
