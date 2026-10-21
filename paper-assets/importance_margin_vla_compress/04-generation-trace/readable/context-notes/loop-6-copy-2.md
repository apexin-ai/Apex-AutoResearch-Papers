# agent / loop_6.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`bcf600c0fe60f87bb167.json`](../../sessions/bc/bcf600c0fe60f87bb167.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-16T15:14:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-27271 的 cuda:0 和 cuda:1，不可用其他设备
- 环境激活必须用 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不存在 .venv
- 网络操作前必须 `source /etc/network_turbo`，否则 HF/pypi 全部超时
- HF 下载必须设 `HF_HOME=/root/autodl-tmp/.hf_cache` + `HF_HUB_DISABLE_XET=1` + SSL 证书变量
- WANDB_MODE=offline（无在线 wandb）
- submit_training_job 命令必须自带完整环境激活链（conda + network_turbo + 环境变量）

### 2. 🖥️ 基础设施快照
- 服务器：westd-27271，2× RTX PRO 6000 96GB
- 工作目录：`/root/autodl-tmp/importance_margin_vla_compress`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`lerobot/smolvla_base`（HF cache at `/root/autodl-tmp/.hf_cache`）
- 数据集：`lerobot/aloha_sim_insertion_scripted_image`（20K samples）
- Checkpoints：
  - baseline_v5: `checkpoints/baseline_v5/step_029999/checkpoint.pt`（唯一成功 baseline）
  - imm_two_stage (MVP PASS): `checkpoints/imm_two_stage/final/checkpoint.pt`
  - v8c annealing: `checkpoints/imm_anchor_v8c_annealing/`
- wandb offline run: `/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260516_122925-2t4p795u/`
- 活跃进程：无（两张 GPU 均空闲，无 tmux session，无 cron）

### 3. 📊 当前状态
刚完成 Loop #6 session-start 初始化。已向 Director 汇报全局状态 + mode collapse 修复方案候选列表，等待方向决策。

Registry：全部 20 个实验 DONE，无 RUNNING/PREPARING。

等待中：
- Worker `worker_research_lora-mode-collapse-fix_20260516T111218`（文献调研：LoRA + flow matching mode collapse 修复方案）
- Worker `worker_analysis_checkpoint-diversity-test_20260516T111238`（SSH 检查 baseline_v5 中间 checkpoint 的 action diversity，判断 early stopping 可行性）
- Director 决策：mode collapse 修复优先级 + CoRL DDL 是否仍为目标

### 4. 📋 待办
- 文献调研 Worker 返回 → 整合报告到 memory.md，提取最可行方案补充给 Director
- Checkpoint diversity Worker 返回 → 若早期 checkpoint (5K/10K) 无 collapse → 立即提议 Director 用 early stopping baseline 做 success rate eval
- 若早期 checkpoint 也 collapse → early stopping 路线关闭，聚焦 merge+full FT 或 generation loss
- Director 决策返回 → 立即在 cuda:0 + cuda:1 并行启动对应修复实验（两卡必须同时跑）
- 若 Director 确认 CoRL DDL 不可行 → 切换到 AAAI 节奏，可做更彻底的 full FT 实验

### 5. 🎯 战略上下文
**核心矛盾**：v8b_twostage MVP 全 gate PASS（G3=0.87x），但 LoRA mode collapse 导致 sim success rate = 0%。Offline metrics 有效但模型不能 closed-loop 执行。

**决策链**：
- D034: two-stage 解决 co-adaptation（G3 从 1.344x → 0.87x）
- D035: LoRA mode collapse 确认（alpha=64, scale=2.0 破坏 flow matching velocity field）
- D037: v8c annealing NEGATIVE（G3=2.04x），确认 single-stage 无法解决
- D038: alpha=16 未修复 mode collapse（std 0.006→0.007，需 >0.05）

**易错点**：
- 不要混淆"进程退出 = 训练失败"——v8b_twostage 进程退出是正常完成，已确认 success
- baseline_v5 本身也 0% success rate（mode collapse 是 LoRA 训练通病，不是 IMM 特有）
- baseline_mean_reward=0.16（非零）暗示模型有部分能力，可能是 max_episode_steps=300 vs 训练数据 400 步的 bug
- mode collapse 修复方向决策权在 Director，Agent 不能自行 pivot
- 两张 GPU 空闲 = L1 违规，Director 决策到手后必须秒级派活


---
