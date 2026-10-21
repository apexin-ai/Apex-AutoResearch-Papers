# agent / loop_3.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`71d59626f9b9f08a587f.json`](../../sessions/71/71d59626f9b9f08a587f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-15T22:11:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 westd-34887 的 cuda:0 和 cuda:1，不得使用其他 GPU
- cuda:1 曾有系统性问题（kl_sparsity70_s42, kl_sparsity30_s42, ste_kl_s42 连续三次进程启动即死，零日志），后确认为缺 `--gradient_checkpointing` 导致 OOM。所有 LLaMA-3.1-8B sparsity 训练必须加 `--gradient_checkpointing`
- `submit_training_job` 的 command 必须自带环境激活：`source /root/miniconda3/bin/activate && python ...`（服务器用 conda，不是 venv）
- EMNLP 2026 ARR May DDL = **2026-05-25**，剩余 10 天
- Training-free baseline 数据已修复（原始全 buggy，per-layer normalization fix 后：Vanilla TEAL 23.31, WINA 27.93, TEAL Greedy 33.47），不要引用旧的 50K-80K 数字

### 2. 🖥️ 基础设施快照
- 服务器：**westd-34887**，工作目录 `/root/distill_sparse_swiglu/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`/root/autodl-tmp/models/llama-3.1-8b`（LLaMA-3.1-8B），Mistral 备用 `/root/autodl-tmp/models/mistral-7b/`
- 数据：wikitext-103（训练）/ wikitext-2（eval, seq_len=2048, 141 sequences），HF cached
- Checkpoints 目录：`/root/distill_sparse_swiglu/checkpoints/&lt;exp_id>/`
- Logs 目录：`~/runs/distill_sparse_swiglu/&lt;exp_id>.log`
- W&B：项目内配置（未见显式 wandb project name，需查服务器）
- 活跃进程：**无**。所有实验已完成或 killed，无 RUNNING 实验，reconcile_crons 返回 0 active

### 3. 📊 当前状态
**无任何实验在跑。** 两块 GPU 均空闲。

Registry 共 29 个实验：13 success / 6 negative / 5 failed / 5 killed。核心结论：
- **Claim 1 (KL > BCE+comp)**: ✅ 强确认。KL TEAL PPL 12.00±0.07 (4-seed) vs BCE 44.54 vs BCE+comp 25.44 vs training-free 23-33。BCE iso-compute (1000步, matched FLOPs) PPL=54.84，比 training-free 还差
- **Claim 2 (SPON composition)**: ❌ Negative → reframed to "KL subsumes SPON"。SPON recovery 仅 3.8%(seq128）/ 7.3%（seq2048），均 < 10% threshold。D013-D014 确认 SPON 正交且量级小
- **Claim 3 (sparsity scaling)**: 70% 数据点完成（sparsity=0.688），30% 卡住（sparsity=0.281, lambda_max=1000 不够），v3 准备 lambda_max=5000 重跑但未提交
- **STE baseline**: PPL 15.77，比 Gumbel(KL) 差 31.4%，Reviewer Concern #3 已有数据
- **s456 outlier**: 根因已知（TEAL Layer 31 over-pruning），不需重跑

PREPARING 状态的实验（均未提交）：kl_sparsity30_s42_v3, bce_isocompute_s42_v2(killed), eval_spon_supp_retry, spon_kl_s42, mvp_kl_norm_s456(killed/superseded), kl_norm_v3_quicktest(实际 success 未转 DONE), kl_lagrangian_v2(killed/superseded)

无等待中的 Worker 回调或 Cron。无待处理的 Director 决策。

### 4. 📋 待办（条件触发式）
- Director 指示恢复实验 → 优先提交 kl_sparsity30_s42_v3（lambda_max=5000），填 plan_008 sparsity sweep 最后一格
- kl_sparsity30_s42_v3 完成且 sparsity 收敛到 ~0.30 → 收集 30/50/70% 三点 PPL，画 sparsity-PPL 曲线（Claim 3 scaling）
- kl_sparsity30_s42_v3 sparsity 仍卡住 → lambda_max 继续提高或换策略（如 target 0.35 插值），汇报 Director
- Director 确认 Claim 2 reframe 最终版本 → 更新 paper_framing.md，全文 re-audit（读 framing-reaudit skill）
- DDL 倒计时进入 5 天 → 启动论文写作 Worker（需 Director 批准 writing_plan）
- bce_isocompute_s42_v2 如需重跑 → 注意原因是 tmux 被外部 kill，检查服务器是否有 cron/OOM killer 干扰

### 5. 🎯 战略上下文
**核心结论链**：KL distillation 是唯一有效的 contextual sparsity prediction 方法。BCE（independent per-neuron）根本无法学习 inter-neuron coordination，即使 iso-compute 也比 training-free 差。SPON（static bias）被 KL 的 per-token contextual mask 完全包含。Training-free（magnitude-based）在 50% sparsity 下 PPL 3.8-5.5x dense，可用但远不如 KL 的 2.0x。

**决策链要点**：D005(KL 归一化 seq_len-only) → D006(发现÷vocab_size bug 紧急停) → D007(MVP PASS) → D008(BCE+comp/SPON 双 negative) → D009-D014(Claim 2 多轮 reframe)

**易错点**：
1. 不要把 hard-mask PPL（~9.2, predictor 质量指标）和 TEAL sparse PPL（~12.0, 端到端指标）混用。论文需分开报告
2. s456 的 TEAL PPL 13.58 是 outlier（Layer 31 全局分配问题），不是 predictor 质量问题。报 4-seed mean 或标注
3. KL per-step FLOPs = 2.71x BCE，iso-compute 对比的步数比是 2700:1000 不是 1:1
4. Training-free baselines 数字已修复过一次（per-layer normalization bug），引用时用修复后的 23-33 范围
5. 两块 GPU 都空着 = 失职状态，接手后应立即向 Director 汇报并推进待提交实验


---
