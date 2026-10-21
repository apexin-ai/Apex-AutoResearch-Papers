# reviewer / loop_3.md

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`2f5a6b2acb2f4a510775.json`](../../sessions/2f/2f5a6b2acb2f4a510775.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-22T18:50:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-29046 只能用 cuda:0, cuda:1；westd-28034 只能用 cuda:0-3
- 28034 是 RTX 5090 32GB 卡，**无法运行 Qwen3-8B GRPO**（即使 num_generations=2 也 OOM）。只能跑 ACT(SFT) 和 eval
- exp-004-s2 训练有过重复进程事故（PID 494017 + 502516 写同一目录），checkpoint-3000 被污染（被后进程覆盖）。已 SCP 到 28034 并 eval 的 ckpt-3000 结果(SYCONScore=0.2543)的可信度未定论——SCP 时间 vs 污染时间需要仔细核对时区
- exp-003-gs8 也出过 duplicate 进程（PID 519538），已 kill。launch 流程可能有系统性 bug，每次启动后必须验证只有 1 个训练进程
- 不要在训练 GPU 上同时跑 eval——之前 eval 在 GPU0 上导致 gs8 从 24.5s 减速到 65s/step

### 2. 🖥️ 基础设施快照
**westd-29046** (2× H100 96GB)
- 工作目录: `/root/contrastive_entrain_calib`
- Python: `/root/miniconda3/bin/python`（conda base）
- 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
- 数据: `/root/contrastive_entrain_calib/data/calibration_v2_1_expanded.jsonl`（362 samples, 181 pairs）
- W&B: 未启用（report_to=none）
- 活跃进程:
  - exp-003-gs8 (PID 516696, tmux=exp-003-gs8, cuda:0, ~step 150/8000, 24.5s/step)
  - exp-004-s2-v2 ACT resume (PID 494017, tmux=?, cuda:1, ~step 4800/8000, 9.1s/step)

**westd-28034** (4× RTX 5090 32GB)
- 工作目录: `/root/contrastive_entrain_calib`
- 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
- Checkpoints: `/root/autodl-tmp/checkpoints/`
- 活跃进程:
  - exp-004-reduced-lora (PID 30011, tmux=exp-004-reduced-lora, cuda:1, ~step 10+, 72s/step)
  - eval_r3s2_ckpt8000 可能已结束

**westb-13953**: SSH 认证失败，未配置

### 3. 📊 当前状态
刚完成 Round 5 Action Matrix 独立评估（已 post to Director），核心判断：
- **纯 framing 天花板已到**，3.0→3.5 需要 data-level 突破（gs=8 结果或跨模型复现）
- §3/§5 矛盾修复方案正确但需"likely"→"possibly"
- 标题不建议加"A Case Study"
- C2 primary / C1 conditional 策略正确

**R3-only seed 2 全 trajectory 已完成**：17 个 checkpoint 全部 eval 完毕，全部低于 vanilla（peak 0.1429 at ckpt-4000）。确认 R3-only gs=2 跨 seed 失败。

**ACT s2 eval 进度**（已完成 8/16）：
ckpt-500:0.223, 1000:0.256, 1500:0.214, 2000:0.214, 2500:未eval(污染?), 3000:0.254, 3500:0.231, 4000:0.206, 4500:0.223。全部 > vanilla。训练约 step 4800，ckpt-5000 即将产生。

**等待中**：
- exp-003-gs8 ckpt-500 (~2h 后) → 早期 gs=8 信号判断
- exp-004-s2-v2 完成 (~10h) → ACT s2 后半段 eval
- exp-004-reduced-lora ckpt-500 (~10h on 28034) → LoRA ablation 数据

### 4. 📋 待办（条件触发式）
- exp-003-gs8 ckpt-500 出来 → eval 并与 gs=2 baseline 对比（gs=2 ckpt-500: s1=0.116, s2=0.105）。如果 gs=8 > 0.13 (vanilla) 且趋势明显优于 gs=2 → 立即通知 Director 这是 C1 突破性数据
- exp-004-s2-v2 每 500 步 checkpoint → SCP 到 28034 eval，更新 ACT s2 trajectory
- exp-004-reduced-lora ckpt-500 → eval 并与原始 ACT (lora_alpha=128, 7 modules) 对比，判断 LoRA 参数是否是 ACT 成功的关键因素
- Director 发来论文章节审查 → 切换到 Mode B，必须先读 paper-quality-lessons.skill.md
- 任何新实验启动 → 验证无 duplicate 进程、GPU 在白名单内

### 5. 🎯 战略上下文
**核心叙事**：论文只有 C2（probe reward trap in SFT）一个干净贡献。C1（GRPO failures）被 group_size=2 + truncation 双重 confound 侵蚀，已降为 conditional observation。

**关键决策链**：
- C2 primary / C1 conditional pivot（Round 4-5）
- exp-008 是 SFT 不是 GRPO → C2 免疫于 group_size 批评（我在 Round 3 时的关键发现）
- exp-009 (continuous probe) 才是 GRPO（在 28034 上）
- 截断 confound 已量化：full response AUROC 0.76 → truncated@256 降至 0.60

**最容易判断错的事**：
1. 不要把 28034 的 32GB 卡当能跑 GRPO 的——只能跑 SFT/eval
2. exp-004-s2 的 checkpoint-3000 可能被污染（duplicate 进程覆盖），引用其 eval 结果时需标注
3. 不要在训练 GPU 上启动 eval，速度惩罚 2.6x
4. step time 初始几步偏快（warmup），steady-state 才是真实速度——gs8 真实 24.5s/step，reduced-lora 72s/step
5. 论文 Table 4 中 Binary Probe 归类为 SFT（不是 GRPO），Continuous Probe 才是 GRPO——搞混会导致 MF1 策略错误
6. 监控系统误报 eval "failed"——eval 脚本不写 sentinel 文件，进程正常退出但被判失败。看日志确认 EXIT_CODE=0 + 结果文件存在即可


---
