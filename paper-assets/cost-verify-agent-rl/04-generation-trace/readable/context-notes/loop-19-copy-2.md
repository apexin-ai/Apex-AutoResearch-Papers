# reviewer / loop_19.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_19.md`
- **Structured JSON:** [`6e0d9330764090b8a928.json`](../../sessions/6e/6e0d9330764090b8a928.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_wall_time
updated: '2026-05-23T20:04:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-17606 当前只有 **1 张 GPU (cuda:0)**，nvidia-smi 只显示 1 张。所有旧 h-sweep 配置写的 `n_gpus_per_node: 2` 和 `CUDA_VISIBLE_DEVICES: "0,1"` 会报错，必须用 1GPU 配置
- Registry 中 model_name 字段有已知误记问题（多个实验被记为 Qwen2.5-3B，实际全是 Qwen3-1.7B SFT）。断言模型不一致前必须 SSH 查 config 文件验证
- h=5 数据来自 `gsweep_g095_h5_seed1`（gamma sweep γ=0.95），不是独立 h-sweep 实验。功能等价但名字不同，不要当作"缺失实验"
- 论文 DDL: **2026-05-25**（EMNLP 2026 ARR）。Abstract ≤200 words，main text ≤8 pages

### 2. 🖥️ 基础设施快照
- **服务器**: bjb1-17606 (root)，1× NVIDIA RTX PRO 6000 96GB
- **远程工作目录**: `/root/cost-verify-agent-rl/RAGEN`
- **本地论文目录**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/`
- **模型**: `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` (Qwen3-1.7B SFT)
- **W&B**: entity/project 见 `ref_wandb_config.md` memory file
- **磁盘**: /root/autodl-tmp 97GB 可用
- **活跃进程**: `run_eval_variance.sh` (PID 46190) — eval variance 实验，预计还需 ~2h 完成（seed300 ×3 done, seed7hk 进行中，还有 ~5 轮 ×23min）

### 3. 📊 当前状态
**刚完成：** Round 3 全部 16 项修复验证通过 + 数据自查审计（修复了 p=5% 计算错误 5.1%→14.9%，Table 1 caption 17.2% 归属歧义）+ h=10 数据源确认（W&B 证实 6.25% 正确）+ γ=1.0 模型不一致确认是 registry 误记

**正在运行：**
- `eval variance` — 3 checkpoints × 3 seeds 评估方差量化，进度 4/9
- h=10 seed2 **被 SIGTERM kill**（eval variance 脚本占 GPU），未产生有效数据

**等待中：**
- eval variance 完成后 → 结果可加入 appendix 回应 cherry-picking 攻击面
- Director 决策：是否在 eval variance 后重启 h=10 seed2（剩余时间约 24h，单 run 需 8-12h）

### 4. 📋 待办
- eval variance 9/9 完成 → 审查方差数据，确认是否支持论文 Limitations 中的 "20pp range for seed5" 描述
- 如 Director 决定重启 h=10 seed2 → 验证用 1GPU 配置 `_alfworld_hsweep_h10_1gpu.yaml`，确认 step 5 val 是否 collapse（预期 0% 或 ~6%）
- Round 4 审稿请求到达 → 执行审查模式 B（章节写作对抗审查），用 reviewer-audit-checklist §7 + paper-quality-lessons skill
- 如收到 h=10 seed2/seed3 结果 → 与 seed1 (6.25%) 对比，确认 threshold 稳健性

### 5. 🎯 战略上下文
- **核心论点**: step-independent windowing 通过 M1(信息损失) + M2(符号误归因) 双机制导致 agent RL 崩溃。Episode-level GRPO（非新方法，是回退原始设计）修复两者
- **预估评分**: 3.0-3.25 (Findings)，上行至 3.5 需 Soundness 提升
- **最大审稿人攻击面**: (1) "修复"不是新方法 (2) Cell C 缺失 (3) h-sweep 单 seed (4) 只有 36% seeds 泛化
- **易错点**: 
  - 训练时间远超直觉——h=2 单 run 就要 10-12h（2 GPU），不要低估 GPU 时间
  - Figure 3(b) 各 bar 的 eval set 不同（h≤20 用 32-task ID，Full 用 134-task OOD），caption 已标注但容易忽略
  - 论文中 17.2% 是 Cell D 2-seed 均值，不是 11-seed 均值（17.71%）。已修复 caption 但 abstract 仍用 17.2%（正确，因为 abstract 说的是 Cell D）
  - p=5% 上界刚从 5.1% 修复为 14.9%——如果看到旧值残留立即标 critical


---
