# agent / loop_6.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`010aec4ad0f28c27c663.json`](../../sessions/01/010aec4ad0f28c27c663.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-15T02:44:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 **仅 cuda:0, cuda:1**（C001 约束，westb-23072 上）。绝不使用其他 GPU。
- 服务器仅 **westb-23072**，account=root。
- 模型基础是 **DeepSeek-R1-Distill-Qwen-7B**，distilled 模型对剪枝极度敏感——35% sparsity 已证实摧毁模型，仅 20% 可行。
- SFT warmup 是 GRPO 前的**必要步骤**——剪枝后模型 sampling 模式退化（无 EOS），直接上 GRPO 零梯度。不要跳过 SFT 直接跑 GRPO。
- conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，**没有 .venv**。
- EMNLP 2026 ARR May 25 提交，距今 **10 天**。

### 2. 🖥️ 基础设施快照
- **服务器**: westb-23072, 2× RTX PRO 6000 Blackwell 94GB
- **工作目录**: `/root/recovery_aware_struct_prune`（代码）
- **Python**: `/root/miniconda3/bin/python`（conda base）
- **模型路径**:
  - 原始: `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`
  - Pruned RASP 20%: `/root/autodl-tmp/pruned_rasp_20`（post-prune 29% GSM8K）
  - Pruned Standard 20%: `/root/autodl-tmp/pruned_standard_20`（post-prune 1% GSM8K）
  - SFT RASP: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20`
  - SFT Standard: `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20`
  - GRPO Stage 2 output: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20` 和 `grpo_stage2_standard_20`
- **活跃进程**:
  - `grpo_stage2_rasp_20`: PID 263888, tmux session, cuda:0, cron 监控中
  - `grpo_stage2_standard_20`: PID 263966, tmux session, cuda:1, cron 监控中
- **W&B**: 项目内，历史 run IDs: ou02s4k4 (standard), sz9264sx (rasp), ccx0jr0z (rasp 4096)
- **日志**: `~/runs/recovery_aware_struct_prune/` 下各实验 log

### 3. 📊 当前状态
**两个 GRPO Stage 2 实验正在双卡并行运行**——这是项目的**决定性实验**：
- `grpo_stage2_rasp_20` (cuda:0): SFT-warmed RASP 模型 GRPO 恢复，起点 57% sampling accuracy
- `grpo_stage2_standard_20` (cuda:1): SFT-warmed Standard 模型 GRPO 恢复（负对照），起点 64% sampling accuracy

Cron 监控两个实验均 active（reconcile 确认 PID 存活）。无 running Worker。

**已完成实验链**:
1. mvp_rasp_pipeline → v2 → v3 → v4: 迭代修复 GQA 约束、per-layer floor、sparsity 调优
2. D009 (1024 truncation) → D010 (4096 确认 sampling 退化) → D013 (SFT warmup) → D015 (GRPO Stage 2)
3. SFT 结果: RASP 57% vs Standard 64%（Standard 反超，但 SFT 是 pattern matching 非真正推理恢复）

**Dream 分析 (D016) 已完成**: Best=Weak Accept (4/6)，三档一致结构性问题: α ablation 缺失(Critical)、single model、no inference speedup、multi-seed。新增 plan_015/016/017。

### 4. 📋 待办（条件触发式）
- **GRPO Stage 2 完成回调到达** → 按 ROADMAP contingency 表判断:
  - RASP >> Standard (>10pp): 全面推进 plan_001-017，优先 plan_015 (α ablation, P0)
  - RASP > Standard (5-10pp): 优先 plan_001 (full eval) + plan_006 (multi-seed) + plan_015 (α ablation)
  - RASP ≈ Standard (<5pp): 转 training dynamics 分析 + 试 25% sparsity
  - Standard > RASP: **核心假设失败**，走 red-section Framing 调整提案
- **GRPO 完成后立即** → 派 Worker 跑 GRASPrune baseline (plan_005，代码调研已完成见 memory.md)
- **α ablation (plan_015)** → GRPO 完成后 P0 优先级，α∈{0.5, 1.0, 2.0} 三组，可双卡并行 2+1
- **Inference speedup (plan_016)** → 简单测量，1h GPU 时间
- **Unstructured baseline (plan_017)** → ~15h GPU

### 5. 🎯 战略上下文
**核心假设**: CKA functional overlap F(h) 预测 RLVR recoverability。RASP scoring S(h)=I(h)×(1-F(h))^α 让 GRPO 恢复效果显著优于 importance-only pruning。

**决策链**: D007(kill 270h runs) → D008(改 MVP 标准) → D009(1024 truncation 伪阴性) → D010(4096 确认 sampling 退化) → D013(SFT warmup 方案) → D014(MVP PASS: 29% vs 1%) → D015(SFT Standard>RASP 不改方向，GRPO 是决定性实验) → D016(Dream 分析)

**最容易判断错的事**:
1. SFT 阶段 Standard 64% > RASP 57% **不代表 Standard 更好**。SFT 是 teacher forcing pattern matching，GRPO 才测试真正的推理恢复能力。不要因为 SFT 数字被 Standard 领先而动摇 story。
2. Post-prune accuracy (RASP 29% vs Standard 1%) 是在 N=100 greedy 上测的，full GSM8K eval 还没做（plan_001）。
3. GRASPrune 调研报告在 memory.md 里，集成方案已就绪，但**还没在服务器上 clone/跑**——等 GRPO 完成释放 GPU 再执行。
4. 两模型 20% sparsity 下 MLP 总参数量完全相同（395,232），差异纯粹来自分布策略（Scenario B）。这是排除"RASP 只是剪得少"替代解释的关键证据，汇报时务必提及。


---
