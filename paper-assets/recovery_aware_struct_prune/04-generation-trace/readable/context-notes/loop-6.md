# director / loop_6.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`92f546673783935837f1.json`](../../sessions/92/92f546673783935837f1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-15T09:28:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- westb-23072 只能用 cuda:0, cuda:1（约束 C001）
- westd-11672 只能用 cuda:0, cuda:1（约束 C003）
- 用户即将加 2 张卡（80GB+），等用户发 SSH 信息后才能使用，未到手前不要假设可用
- α ablation 必须用 n_samples=512 calibration（与 westb 原始实验一致），之前 westd 用了 256 导致 29pp 数据矛盾
- GRPO 训练必须保留 KL penalty (beta>0)，不允许 beta=0 绕过 ref_model 问题
- pruned model 必须用 load_pruned_model() 加载，不能用 from_pretrained()（会导致非均匀 MLP 权重 reinit）

### 2. 🖥️ 基础设施快照
- **westb-23072** (connect.westb.seetacloud.com, root): 2× RTX PRO 6000 94GB
  - 工作目录: /root/recovery_aware_struct_prune
  - 模型: /root/autodl-tmp/pruned_rasp_20, /root/autodl-tmp/pruned_standard_20
  - SFT checkpoint: /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20（retrain 会覆盖原 ckpt）
  - GRPO v4: PID 339111, cuda:0, wandb run 75d1o9wa, 29min/step, 250 steps
  - SFT retrain: PID 239076, cuda:1, step ~828/1870, ETA ~1.3h from last check
- **westd-11672** (connect.westd.seetacloud.com, root): 2× RTX PRO 6000 94GB
  - α ablation pipeline: nohup PID 7186, α=2.0/4.0 eval 接近完成
  - α ablation 结果目录: 需要 Agent 确认具体路径
- W&B: 未全局配置，GRPO v4 有 wandb run
- D023 re-eval: westb CPU eval + westd GPU eval Workers 应该还在运行

### 3. 📊 当前状态
**刚做完**：D022 代码对比确认 1% 不是 artifact（calibration 差异导致 30% vs 1%）。D025 决策：GRPO v4 需优化速度 + α=4.0 需紧急验证。

**Registry RUNNING/PREPARING**：
- grpo_stage2_rasp_20_v4: RUNNING (cuda:0 westb), 29min/step, 需 kill 并优化重启为 v5
- sft_standard_20_retrain: RUNNING (cuda:1 westb), ~44% done
- 5 个 α ablation 实验: 无 registry 条目（需补注册）

**等待中**：
- D025 线 1: Agent vLLM 兼容性调研结果（~10-15 min，可能已出）
- D025 线 2: α=0.0 vs α=4.0 N=500 验证准备
- D023: re-eval pruned_standard_20/pruned_rasp_20 结果（CPU + GPU 两条线）
- 用户加卡 SSH 信息

### 4. 📋 待办
- vLLM 调研出结论 → 兼容则 kill v4 + vLLM 重启为 v5; 不兼容则 max_completion_length=2048→512 重启为 v5
- D023 re-eval 结果出来 → 如果 Standard ~30% 则确认 calibration 是根因（已高度确信）; 如果仍 1% 则有其他未知差异需深挖
- α=4.0 N=500 验证结果 → ≥35% 且显著高于 α=0.0 → CKA claim 成立（α=4.0 为最优）; 差异不显著 → CKA claim 需重大调整或放弃
- SFT retrain 完成 → cuda:1 空出，可跑其他 eval 或 GRPO Standard
- 用户发新服务器 SSH 信息 → register_server + 部署环境 + 分配实验（GRPO Standard 并行 + baseline 实验）
- GRPO v5 首步 reward>0 且 grad_norm>0 → 训练正常; reward=0 / grad_norm=0 → 第五次 GRPO 失败，需根本性反思

### 5. 🎯 战略上下文
- **目标**: EMNLP 2026 ARR May 25（还剩 10 天）
- **核心 claim**: RASP (CKA-aware pruning) 在 matched sparsity 下比 Standard 更好地保留/恢复推理能力
- **决策链**: D014 MVP pass (29% vs 1%) → D015 SFT Standard>RASP 不改方向 → D017-D020 GRPO v1-v3 全失败（sampling collapse / ref_model crash）→ D021 v4 修复启动 → D023 数据可信度危机（α=0.0=30% vs Standard=1%）→ D022 确认是 calibration 差异不是 eval bug → D025 GRPO 速度优化 + α=4.0 验证
- **最关键判断点**: α=4.0 (40%) 是否在 N=500 + 512 calibration 下仍显著高于 α=0.0。这决定 CKA 贡献是否真实
- **易踩的坑**:
  - 不要混淆 calibration=256 和 calibration=512 的 α 结果，只有 512 才与原始实验可比
  - GRPO 已失败 4 个版本(v1 killed, v2 collapse, v3 crash, v4 太慢)，v5 需要成功否则 GRPO recovery claim 无实验支撑
  - SFT 结果 Standard 64% > RASP 57%，post-SFT RASP 没优势，必须靠 GRPO 翻盘
  - α ablation 曲线非单调（30→25→27→29→40），α=4.0 可能是噪声，不要在 N=100 下过度解读
  - Registry 卫生问题严重（多个状态未更新，α ablation 无条目），Reviewer 已三次提醒


---
