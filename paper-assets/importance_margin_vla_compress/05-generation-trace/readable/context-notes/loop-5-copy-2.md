# agent / loop_5.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`ac15069e931463b87f7e.json`](../../sessions/ac/ac15069e931463b87f7e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-16T11:09:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-27271 的 cuda:0 和 cuda:1，不可用其他设备
- 服务器环境激活必须用 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不存在 .venv
- 网络操作前必须 `source /etc/network_turbo`，否则 HF/pypi 全部超时
- HF 下载必须设 `HF_HOME=/root/autodl-tmp/.hf_cache` + `HF_HUB_DISABLE_XET=1` + SSL 证书变量
- WANDB_MODE=offline（当前无在线 wandb）
- submit_training_job 命令必须自带完整环境激活链（conda + network_turbo + 环境变量）

### 2. 🖥️ 基础设施快照
- 服务器：westd-27271，2× RTX PRO 6000 96GB
- 工作目录：`/root/autodl-tmp/importance_margin_vla_compress`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`lerobot/smolvla_base`（HF cache at `/root/autodl-tmp/.hf_cache`）
- 数据集：`lerobot/aloha_sim_insertion_scripted_image`（20K samples）
- Checkpoints：`/root/autodl-tmp/importance_margin_vla_compress/checkpoints/`
  - baseline_v5: `checkpoints/baseline_v5/` (成功 baseline)
  - imm_anchor_v8: `checkpoints/imm_anchor_v8/` (G3=1.344x, negative)
  - imm_two_stage: `checkpoints/imm_two_stage/` (v8b_twostage 的输出，状态未知)
- wandb offline run: `/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260516_122925-2t4p795u/`
- 活跃进程：无（两张 GPU 均空闲）
- Worker 在跑：`worker_diagnose_mvp_imm_v8b_twostage_20260516T070648`（SSH 查日志诊断中）

### 3. 📊 当前状态
刚收到 cron 回调：`mvp_imm_v8b_twostage` 进程异常退出（"process dead 5× with no sentinel/W&B"）。已派诊断 Worker 查日志，尚未返回。已向 Director 汇报失败现象 + GPU 空闲状态。

Registry 状态：
- 全部 17 个实验均 DONE（无 RUNNING/PREPARING）
- `imm_two_stage_v9` 标记 killed（被 v8b_twostage 替代）
- 最后一个成功实验：`mvp_baseline_v5`
- 三个 negative：v7.2 (G3=3.19x), v8 (G3=1.344x), v8.1 (G3=2.53x)

等待中：
- 诊断 Worker 回调 → 确认失败根因
- Director 对下一步方向的决策

### 4. 📋 待办
- 诊断 Worker 返回 → 判断失败类型：
  - 如果是代码 bug / OOM / Stage transition 错误 → 修复后在 cuda:1 重跑 two-stage
  - 如果训练完成但无 sentinel → 检查是否有可用 checkpoint，直接跑 eval
  - 如果方法论失败（训练 diverge / loss 爆炸）→ 向 Director 提交 fallback 方向决策
- two-stage 确认失败（方法论）→ 启动 fallback 梯队第一项：mask ratio annealing (keep=0.9→0.5，基于 v8 checkpoint)
- 任何实验重跑/新跑 → 两张 GPU 必须都安排任务（cuda:0 跑 fallback 准备，cuda:1 跑修复后的 two-stage 或另一个 fallback）

### 5. 🎯 战略上下文
**核心问题**：IMM 训练导致 backbone co-adaptation，G3 (deploy loss ratio) 始终 >1.10。

**决策链**：
- D029: v8 bypass 7.12x 确认 co-adaptation 是 backbone 内化 sparse token 偏好（非梯度泄漏）
- D033: 降低 λ 不解决 G3（反而恶化，因为 ACIS 质量差）
- D032: two-stage 是解耦 co-adaptation 的最后尝试（冻结 backbone 训 ACIS → 冻结 ACIS 训 LoRA）
- v8 (G3=1.344x) 是目前最接近目标的结果，gradient isolation 有效但不够

**易错点**：
- v8b_twostage 可能实际跑完了（~10K seconds = 足够 30K steps at 4.3 steps/sec），但因为 WANDB_MODE=offline 没有 sentinel → 检查 checkpoint 目录是否有最终权重
- 不要混淆 "进程退出 = 训练失败"，可能是正常完成但缺少 done marker
- Fallback 方向决策权在 Director，Agent 不能自行 pivot
- 两张 GPU 空闲 = 失职，诊断完后必须立即安排任务


---
