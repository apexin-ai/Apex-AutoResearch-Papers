# director / loop_2.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`4f698103f20bb7ef0f2b.json`](../../sessions/4f/4f698103f20bb7ef0f2b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T11:17:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- rtx5090-4x 和 gpu-5090-4x-1 是**同一台机器**的两个 SSH endpoint，实际只有 4× RTX 5090 32GB，不是 8 张卡
- GPU 全部在 rtx5090-4x 上操作（cuda:0-3），gpu-5090-4x-1 不要单独派训练任务
- AutoDL 机器：pip/git 前必须 `source /etc/network_turbo`；HF 下载设 `HF_HUB_DISABLE_XET=1`
- BNB 4-bit 多 GPU 必须用 `device_map={"": local_rank}`，否则 OOM（r1 教训）

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (connect.bjb2.seetacloud.com)，root 用户
- 工作目录：/root/autodl-tmp/freige
- Python 环境：需 SSH 探查确认（conda 或 venv）
- NLI cache：已预计算 38180 samples，部署在服务器上
- 活跃进程：CED r2 全量训练，PID 39551，tmux session `mvp2_grpo_ced_r2`，cron 监控 120s 间隔
- W&B：未配置

### 3. 📊 当前状态
CED r2 全量训练 RUNNING（4/4 GPU，预估 189 步，~2-4h，约 73.7s/step）。参数：lr=2e-5, kl_coef=0.05, save_steps=20, format×0.3 / f1×**3.0** / ced×1.0, num_iterations=2。

Registry：
- mvp2_grpo_ced_r2: 应为 RUNNING（cron 监控中）
- mvp2_sft_eval: PREPARING（等 CED r2 完成）
- mvp2_grpo_extract: PREPARING（等 CED 完成后串行）
- mvp2_grpo_flatnli: PREPARING（等 extract 完成后串行）
- 其余 5 个实验 DONE（4 success, 1 failed）

注意事项：dry-run 发现 KL 异常高（1.73e8），可能是 BNB merge_and_unload 量化误差；completions clipped_ratio 40.6%（max_completion_length=1024）。需关注这两项是否在全量训练中恶化。

### 4. 📋 待办
- CED r2 cron 回调显示 DONE + success → 启动 mvp2_sft_eval（用 SFT checkpoint 跑 eval，与 GRPO CED 对比 Evi-F1）
- CED r2 出现 mode collapse（F1 归零）→ 立即 kill，分析 reward 曲线，考虑进一步调参（r1 就是 mode collapse 被 kill 的）
- mvp2_sft_eval 完成 → 启动 mvp2_grpo_flatnli（flat-NLI reward 替代 CED）
- mvp2_grpo_flatnli 完成 → 启动 mvp2_grpo_extract（extraction-only baseline）
- 三路 GRPO 全完成 → MVP-2 判定：CED GRPO Evi-F1 > SFT Evi-F1 ≥ 2pp 且 F1 > 45 → PASS → complete_mvp()

### 5. 🎯 战略上下文
- **核心假设**：CED（对比证据判别）奖励能引导 LLM 在文档级 RE 中生成可验证证据，优于 flat-NLI 和 extraction-only
- MVP-1 已 PASS（CED margin 0.48, accuracy 81.5%, r=0.34），证明 CED 信号有区分力
- MVP-2 是端到端训练验证：SFT warmup → GRPO+CED vs GRPO+flat-NLI vs GRPO+extraction-only
- **r1 失败教训**：f1_reward_weight=1.0 太低导致 F1 信号被 format reward 淹没 → mode collapse。r2 已调到 3.0，dry-run 确认三项 reward 同量级
- **易错点**：不要把 4 张卡当 8 张排期；串行执行计划不要改成并行（只有 4 张卡）；关注 KL 和 clipped_ratio 异常
- 决策链：D001(MVP 设计) → D002(MVP-1 PASS) → D003(Smoke PASS) → D004(发现只有 4 卡) → D005(r1 mode collapse) → D006(kill r1 准备 r2)


---
