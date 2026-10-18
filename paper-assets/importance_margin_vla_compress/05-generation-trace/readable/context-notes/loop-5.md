# director / loop_5.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`590c71ad2df8fcab8caf.json`](../../sessions/59/590c71ad2df8fcab8caf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-16T10:29:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-27271 的 cuda:0 和 cuda:1（2× RTX PRO 6000 96GB）
- AutoDL submit 命令必须含完整环境前缀：`source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export WANDB_MODE=offline`
- v8c_annealing 和 baseline_v6 都曾因缺 WANDB_MODE=offline 或 network_turbo 崩溃，已反复踩坑
- 用户明确要求 **success rate 作为核心指标**，action loss 只是辅助，不可用 action loss 代替 success rate 做 headline

### 2. 🖥️ 基础设施快照
- 服务器：westd-27271 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/autodl-tmp/importance_margin_vla_compress
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型 checkpoints：/root/autodl-tmp/importance_margin_vla_compress/checkpoints/（v8b MVP PASS: checkpoints/imm_two_stage/final/checkpoint.pt）
- Eval results：/root/autodl-tmp/importance_margin_vla_compress/eval_results/
- HF cache：/root/autodl-tmp/.hf_cache
- 活跃进程：
  - cuda:0: mvp_imm_v8c_annealing（tmux session，PID 需确认）
  - cuda:1: baseline_v6_alpha16（tmux session，刚启动 30K steps）
- W&B：offline mode（服务器无法连 wandb API）

### 3. 📊 当前状态
**阶段**：刚从 MVP 转入 Research。Post-MVP kickoff 已完成（paper_framing.md + experiment_plan.yaml + dream_simulate 已启动）。

**RUNNING 实验**：
- `mvp_imm_v8c_annealing` (cuda:0)：mask ratio annealing ablation，P1 实验
- `baseline_v6_alpha16` (cuda:1)：降低 LoRA alpha 64→16 重训 baseline，用于修复 flow matching mode collapse 以支持 success rate 评估

**等待中**：
- Dream dream_20260516T075046（full review mode，CoRL 2026），完成后会注入 session
- baseline_v6 训练完成 cron 回调
- v8c_annealing 训练完成 cron 回调

**关键背景**：MVP 已 PASS（v8b_twostage G3=0.87x），Reviewer 独立审计确认。但 success rate 评估发现所有模型（包括 baseline）0% success rate——根因是 LoRA alpha=64 导致 flow matching ODE mode collapse（action chunk std 从 0.104 collapse 到 0.006）。这不是 ACIS/IMM 的问题，是 LoRA 训练超参问题。正在用 alpha=16 重训修复。

### 4. 📋 待办
- baseline_v6_alpha16 训练完成 → sample_actions() 验证 action diversity (std 应 ≈0.1 而非 0.006) → 50 episode success rate → baseline 能完成任务则用 alpha=16 重训 IMM two-stage → 对比 success rate
- v8c_annealing 完成 → 500-batch eval → 与 v8b 对比（plan_010 ablation）
- Dream 回调 → Read dream-report-action skill → 按行动列表处理 → 如需调整 framing/plan 则改完 re-dream → 达标后批准 P0 实验
- success rate baseline 验证通过 → 向 Manager 申请加卡（CoRL DDL May 29，P0 总量 ~242 GPU-hrs，2 卡不够）
- 如果 alpha=16 仍然 mode collapse → 尝试 alpha=8 或减少训练步数 30K→15K

### 5. 🎯 战略上下文
- **MVP 通过**：v8b_twostage two-stage 训练（Stage1 冻结 backbone 训 ACIS 10K → Stage2 冻结 ACIS 训 LoRA 20K）是解决 ACIS-backbone co-adaptation 的正确方案。G3 演进：v7(3.28x) → v8(1.344x) → v8.1(2.53x，降 λ 反而恶化) → v8b(0.87x ✅)
- **核心决策链**：D029(co-adaptation 确认) → D032(two-stage 简化) → D033(低 λ 恶化) → D034(MVP PASS) → D035(mode collapse 确认+修复方案)
- **最易判断错的事**：不要认为 success rate = 0 意味着方法失败——这是 LoRA 训练超参问题，所有模型（含 baseline）都 collapse。G1-G4 offline metrics 仍然有效
- **用户偏好**：用户要求 success rate 为核心结果，回复要简洁直接，禁止客套。用户会追问细节，需要能用通俗类比解释技术概念
- **Claim 措辞**：Reviewer 指出 "certified" 应改为 "provable"（已改）；"lossless" 应改为 "lossless-to-gainful"（已改，待跨 benchmark 验证）；所有 P0 实验需 ≥3 seeds（已更新 plan）
- **CoRL 2026 DDL May 29**（13 天）：极紧但 AI 团队可行，前提是 success rate 修复成功 + 加卡。如果 mode collapse 修复耗时超预期，AAAI 2027 (~Aug) 是 secondary target


---
