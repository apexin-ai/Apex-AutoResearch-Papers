# agent / loop_7.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`376605e10c72be501f46.json`](../../sessions/37/376605e10c72be501f46.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-16T19:18:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-27271 cuda:0/1 + cqa1-33015 cuda:0/1/2/3（config 已更新）
- westd 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不存在 .venv
- cqa1 环境同为 conda base（Python 3.12, CUDA 12.4）
- 网络操作前必须 `source /etc/network_turbo`，HF 下载设 `HF_HOME=/root/autodl-tmp/.hf_cache` + `HF_HUB_DISABLE_XET=1` + SSL 证书变量
- WANDB_MODE=offline（两台服务器均无在线 wandb）
- submit_training_job 命令必须自带完整环境激活链

### 2. 🖥️ 基础设施快照
- **westd-27271** (2× RTX PRO 6000 96GB)
  - 工作目录：`/root/autodl-tmp/importance_margin_vla_compress`
  - Python：`/root/miniconda3/bin/python`
  - 模型：`lerobot/smolvla_base`（HF cache `/root/autodl-tmp/.hf_cache`）
  - 数据：`lerobot/aloha_sim_insertion_scripted_image`（20K samples）
  - LIBERO sim 环境已装（libero 0.1.1, robosuite 1.4.0, mujoco 3.8.1）
  - Checkpoints: baseline_v5 `checkpoints/baseline_v5/step_029999/checkpoint.pt`, imm_two_stage `checkpoints/imm_two_stage/final/checkpoint.pt`
  - 活跃进程：无训练，Workers 做短期 eval 推理
- **cqa1-33015** (4× RTX 4090 24GB, connect.cqa1.seetacloud.com:33015, root)
  - 工作目录：`/root/autodl-tmp/importance_margin_vla_compress`
  - LIBERO 数据：`HuggingFaceVLA/libero` (~37GB)
  - 活跃 cron：`libero_full_ft_baseline` (cuda:0), `libero_lora_baseline` (cuda:1)

### 3. 📊 当前状态
Loop #7 刚完成 session-start 初始化，已向 Director 汇报全局状态。

**RUNNING（GPU 训练）**：
- `libero_full_ft_baseline` — cqa1 cuda:0, full expert FT (99.9M params), 验证 pipeline 正确性，目标 >50% SR
- `libero_lora_baseline` — cqa1 cuda:1, LoRA r=32 alpha=16, 验证 LoRA+flow matching 是否系统性 collapse

**PREPARING**：
- `plan_005_formal_bound` — 脚本崩溃（AttributeError），Worker 正在修复
- `eval_sim_success_rate` — 旧 aloha eval，已被 LIBERO 取代，可忽略

**活跃 Worker（3 个）**：
1. `worker_fix_plan_005_formal_bound_20260516T150723` (turn 27) — 调试 formal bound 脚本
2. `worker_eval_libero_10k_checkpoint_v2_20260516T151045` (turn 14) — cqa1 跑 LIBERO 10K checkpoint eval（关键：决定 cuda:2/3 分配）
3. `worker_fix_plan_008_pruning_sweep_v2_20260516T151209` (turn 19) — 修复 pruning sweep

**等待中**：Director 对 westd GPU 分配 + CoRL 可行性的回复

### 4. 📋 待办
- Worker `eval_libero_10k_checkpoint_v2` 返回 → 如果 full FT action diversity 正常 + LoRA collapse → 确认 LoRA 系统性问题，向 Director 建议 cuda:2/3 全跑 full FT + IMM two-stage
- Worker `eval_libero_10k_checkpoint_v2` 返回 → 如果两者都正常 → LoRA 可行，cuda:2/3 启动 IMM two-stage (LoRA) + ablation
- LIBERO 训练 cron 回调（完成/失败）→ 按 on-experiment-done skill 处理
- Director 回复 CoRL 可行性 → 如果放弃 CoRL 切 AAAI → 可做更多 ablation + full FT 路线
- plan_005/008 Workers 完成 → 更新 registry，这些是 westd 上的 aloha ablation 补充数据

### 5. 🎯 战略上下文
**核心矛盾**：v8b_twostage MVP 全 gate PASS（G3=0.87x），但 LoRA mode collapse 导致 sim SR=0%。Offline metrics 证明 IMM 有效，但需要 closed-loop 验证。

**决策链关键节点**：
- D034: two-stage 解决 co-adaptation
- D035: LoRA mode collapse 确认
- D039: aloha SR 已死（社区已知问题），LIBERO 升 P0
- D040: LIBERO 双轨验证（full FT vs LoRA）

**易错点**：
- aloha 0% SR 是社区已知问题（非 IMM 特有），不要再花时间修 aloha SR
- baseline_v5 本身也 0% SR，所以 mode collapse 讨论只在 LIBERO 上有意义
- westd 的 plan_005/008 是 aloha offline ablation 补充实验（支撑 paper 某些 claim），不是 critical path
- cqa1 cuda:2/3 分配权在 Director，不能自行决定——等 10K eval 结果出来后提建议
- CoRL deadline May 29 (13天)，时间极紧，需要 4 卡 + LIBERO 全流程顺利才有可能


---
