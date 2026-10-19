# agent / loop_4.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`f1db6dc3dfccf2e23d65.json`](../../sessions/f1/f1db6dc3dfccf2e23d65.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-16T01:56:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 westd-34887 的 cuda:0 和 cuda:1**（C001 约束，RTX PRO 6000 Blackwell × 2）
- KL PPL 引用：论文统一用 **4-seed mean 12.00±0.07**，禁止用单 seed 最佳值 11.91（memory.md 约定）
- BCE framing：禁止用 "anti-learning"，必须用 **"objective mismatch"**（BCE per-neuron binary accuracy vs TEAL global top-k 结构性不兼容）
- SPON framing：禁止 "KL subsumes SPON"，正确措辞为 **"marginal complement"**（cos_sim=0.196, magnitude 16%）
- s456 outlier：报 "5-seed mean 12.32±0.71" + "Excluding s456: 12.00±0.07"，不跑第 6 个 seed
- DDL：**2026-05-25 ARR May submission**，仅剩 9 天

### 2. 🖥️ 基础设施快照
- 服务器：**westd-34887**，工作目录 `/root/distill_sparse_swiglu/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 环境激活：`source /root/distill_sparse_swiglu/setup_env.sh`（项目代码用这个）
- LLaMA-3.1-8B：`/root/autodl-tmp/models/llama-3.1-8b`
- Mistral-7B：`/root/autodl-tmp/models/mistral-7b/`（已下载，7.25B params）
- HF cache：`/root/autodl-tmp/.hf_cache`（推测，需确认）
- Checkpoints：`/root/distill_sparse_swiglu/checkpoints/` 下多个子目录（见 memory.md Checkpoints 节）
- 关键 checkpoint：KL-only s42 = `checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt`
- 活跃进程（截至 handoff 前）：
  - `lm_eval_teal_50pct`：PID 187335，cuda:0，tmux session，TEAL 50% downstream eval
  - `lm_eval_kl_s42`：PID 179913，cuda:1，tmux session，KL 50% downstream eval（notes 已有结果但状态仍 RUNNING）
- W&B：`WANDB_MODE=disabled`（所有实验禁用 W&B，指标通过 log 文件收集）
- 累计 GPU·h：~90h / 预算 ~196h

### 3. 📊 当前状态
**刚完成**：
- D026 确认 downstream 崩溃根因 = 稀疏化摧毁深层表征（非 eval format artifact）。退化梯度与任务推理深度正相关：WinoGrande -21% < ARC-c -35% < MMLU -60% < GSM8K -98%。
- `training_free_baselines` 重跑完成（TEAL 50%=23.31, 70%=100.11 确认）
- `kl_sparsity70_s42_v2` 完成（success）
- `gsm8k_gen_compare` 完成（negative）——sparse 50% 模型 1-3 句后进入无限重复循环，0/10 正确，推理能力根本性丧失

**RUNNING**：
- `lm_eval_teal_50pct`（cuda:0）：TEAL 50% training-free downstream eval，验证 downstream 崩溃是否为 50% sparsity 固有限制
- `lm_eval_kl_s42`（cuda:1）：状态 RUNNING 但 notes 已有完整结果（ARC-c 0.3771, WinoGrande 0.6156, MMLU 0.2591, GSM8K 0.0121），可能需要手动转 DONE

**PREPARING（排队等 GPU）**：
- `lm_eval_kl_30pct_s42`：30% sparsity downstream eval，决定论文能否 claim "30% 为推荐配置"
- `bce_isocompute_s42_v2`：BCE iso-compute retry（v1 在 step 500 crash）
- `lm_eval_mistral_downstream` / `lm_eval_mistral_dense`：Mistral 泛化验证（plan_009）
- `diag_30pct_downstream` / `diag_teal_downstream` / `diag_gsm8k_gencomp`：诊断类实验
- `lm_eval_dense_test`：dense baseline 补充

**等待中**：
- `lm_eval_teal_50pct` cron 回调 → 对比 TEAL vs KL downstream，判断 50% 固有限制
- `lm_eval_kl_s42` 状态需确认（已有结果但仍 RUNNING）

### 4. 📋 待办（条件触发式）
- `lm_eval_teal_50pct` 完成 → 对比 KL vs TEAL downstream 退化。若 TEAL 也崩 → 50% 是固有限制，论文用 30% 展示 sparsity-task tradeoff；若 TEAL 不崩 → KL predictor 特有问题，需深查
- `lm_eval_kl_s42` 结果确认后 → 转 DONE，释放 cuda:1 → 立即提交 `lm_eval_kl_30pct_s42`（30% downstream，决定论文 recommended config claim）
- 30% downstream 结果 → 若保持合理退化（<10% drop）→ 论文 claim "30% 为推荐配置"；若也崩 → 需更低 sparsity 或放弃 downstream claim
- `bce_isocompute_s42_v2` 待 GPU 空闲 → 提交（Reviewer Concern #2 defense，证明 KL 优势非计算量差异）
- Mistral 实验（plan_009）待 GPU → 提交 KL 训练 + dense/sparse eval（Reviewer Concern #4 defense）
- 论文写作：BCE objective mismatch 分析需写入 analysis section

### 5. 🎯 战略上下文
**核心结论链**：
- D001-D006：KL 训练从 sparsity 坍塌到修复（seq_len-only 归一化 + Lagrangian），中间经历 ÷vocab_size bug（D006 作废 D005）
- D009-D010：SPON framing 从 "subsumption" 转为 "marginal complement"
- D021-D023：TEAL baseline 因 normalization bug 重跑，确认 Claim 1 gap
- D024-D026：**downstream 崩溃是当前最大风险**。50% sparsity PPL 12.00 但 GSM8K 仅 1.2%。D026 确认是表征破坏非 eval artifact

**最容易判断错的事**：
1. **lm_eval_kl_s42 状态矛盾**：notes 已有完整结果但状态仍 RUNNING。可能需要手动更新状态。先 SSH 查进程是否还活着再决定
2. **Downstream 崩溃的论文策略尚未定论**：D026 确认了根因但 Director 还没给最终 framing 指导。不要自行决定论文如何处理 50% downstream 数据——等 Director 或 `lm_eval_teal_50pct` 结果后再提方案
3. **30% 是 Plan B 的核心**：如果 30% sparsity 能保持合理 downstream，论文可以 reframe 为 "30% 推荐 + 50% 展示极限"。30% 训练 checkpoint 已就绪（`kl_sparsity30_s42_v3`，145MB），但 downstream eval 还没跑
4. **Mistral 零改动兼容已确认**（memory.md），但训练和 eval 都还没跑。plan_009 是 Reviewer Concern #4 的 defense
5. **BCE iso-compute v1 在 step 500 crash**，v2 是 retry，也还没跑。这是 Reviewer Concern #2 的关键 defense


---
