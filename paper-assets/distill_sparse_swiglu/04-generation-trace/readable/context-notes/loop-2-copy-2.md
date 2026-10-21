# agent / loop_2.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`21bbcfce1724a38c6f65.json`](../../sessions/21/21bbcfce1724a38c6f65.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-15T18:51:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westd-34887 **cuda:0 + cuda:1** 仅此两张，不可用其他 GPU
- 环境激活: `source /root/distill_sparse_swiglu/setup_env.sh`（conda 环境，不是 venv）
- 模型路径: `/root/autodl-tmp/models/llama-3.1-8b`（不要改）
- submit_training_job 命令必须自带 `bash -c "source /root/distill_sparse_swiglu/setup_env.sh && ..."`
- EMNLP ARR May DDL = **2026-05-25**（剩 10 天）
- s456 outlier（TEAL sparse PPL 13.58 vs 4-seed mean 12.00）原因未查明，论文报告需谨慎处理

### 2. 🖥️ 基础设施快照
- 服务器: **westd-34887**, 工作目录 `/root/distill_sparse_swiglu/`
- Python: `/root/miniconda3/bin/python`（conda base 环境）
- 模型: `/root/autodl-tmp/models/llama-3.1-8b`
- 数据: wikitext-103 (HF cached), eval 用 wikitext-2
- W&B: 大部分实验 `WANDB_MODE=disabled`
- Checkpoints: `/root/distill_sparse_swiglu/checkpoints/` 下各子目录
- 活跃进程: ste_kl_s42 (PID 112025, tmux, cuda:1) + spon_2048_s42 (PID 109601, tmux, cuda:0)——但 registry 状态卡在 PREPARING，需要确认进程是否还活着
- 活跃 Worker: `worker_code_plan_002_ste_20260515T183953`（running，在写 STE baseline 代码）
- Cron: reconcile 返回 0 条——可能 ste_kl_s42 和 spon_2048_s42 的 cron 没注册上，需要检查

### 3. 📊 当前状态
**刚完成**: SPON seq_len=128 训练 (negative, 3.8% recovery)、BCE+Comp staged 训练 (negative, 25.44 PPL)、5-seed KL 汇总 (4/5 seed 收敛 12.00±0.07)、training-free baselines 评估 (全崩)、ste_baseline_s42 训练 (negative——但这个是旧的 STE 实验，不是 plan_002 的)

**正在进行**:
- `ste_kl_s42` (PREPARING, PID 112025, cuda:1): STE+KL loss 训练，替代 Gumbel-sigmoid 的 plan_002 实验
- `spon_2048_s42` (PREPARING, PID 109601, cuda:0): SPON seq_len=2048 重训，消除 train/eval seq_len mismatch
- Worker `worker_code_plan_002_ste` 仍在 running（可能在等 ste_kl_s42 提交确认）

**等待中**:
- spon_2048_s42 完成 → 决定 Claim 2 最终 framing（≥2pp recovery 保留 composition claim, <2pp 确认 "KL subsumes SPON"）
- ste_kl_s42 完成 → 回答 Reviewer Concern #3（是 KL 还是 Gumbel-sigmoid 解释 gains）
- plan_003 iso-compute BCE 未启动（等 cuda:0 空出）
- Reviewer 提出的数据修复清单（ROADMAP 中 4 项）未完成

### 4. 📋 待办（条件触发式）
- spon_2048_s42 cron 回调 → 分析结果: recovery ≥2pp 则 Claim 2 保留 composition; <2pp 则确认 "KL subsumes SPON" reframe → 更新 paper_framing.md → 汇报 Director
- ste_kl_s42 cron 回调 → 对比 STE+KL vs Gumbel+KL (mvp_kl_norm_v2_s42): 如果 STE 接近则 gains 来自 KL loss 而非 relaxation → 强化 Claim 1 → 汇报 Director
- cuda:0 空出后 → 启动 plan_003 iso-compute BCE（给 BCE 等量 FLOPs 预算，回应 Reviewer Concern #2）
- Worker `worker_code_plan_002_ste` 完成 → 检查产出，确认 STE 代码是否正确提交
- 数据修复: training_free_baselines metrics 需正式注册 registry（目前在 notes 里不在 metrics 里的部分）; SPON teal_with_spon=11.93 补录; bce_comp sparsity mismatch (0.558 vs 0.498) 标注

### 5. 🎯 战略上下文
**核心结论链**: D001(MVP设计) → D003(KL坍塌) → D004(方案C: 归一化+Lagrangian) → D006(÷vocab_size bug紧急停止) → D007(MVP PASS, KL>>BCE 确认) → D008(BCE+Comp 和 SPON 均 negative) → D009(Claim 2 tentative reframe "KL subsumes SPON")

**Claim 1 极强**: KL PPL 9.21 vs BCE 27.96 vs BCE+Comp 25.44 vs training-free 50K+。论文核心卖点。

**Claim 2 摇摇欲坠**: SPON 仅 3.8% recovery，spon_2048_s42 是最后一次机会。如果仍 negative，reframe 为 "KL makes compensation unnecessary" 而非 "composition adds value"。

**Claim 3 完全未开始**: sparsity scaling sweep (plan_008) 需 7 级 sparsity × 2 loss = 14 runs，至少 2 天 GPU 时间。DDL 前可能来不及做完整 sweep，考虑简化为 3 级 (30%/50%/70%)。

**易错点**:
- ste_kl_s42 和 spon_2048_s42 状态卡在 PREPARING，cron 可能没注册——优先检查进程是否存活 + 手动注册 cron
- `vanilla_teal_sparse_ppl_INVALID` 标记的 66036 是 INVALID 值（vanilla TEAL 实现有 bug），论文中不能引用
- hard-mask PPL (9.21) 和 TEAL sparse PPL (12.08) 是两个不同指标，不要混淆: hard-mask = predictor 质量，TEAL sparse = 端到端效果
- 论文中 KL vs BCE+Comp 对比时必须标注 sparsity 不完全一致 (KL 0.498 vs BCE+Comp 0.558)


---
