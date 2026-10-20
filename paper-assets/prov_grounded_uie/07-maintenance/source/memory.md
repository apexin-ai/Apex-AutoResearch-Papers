# prov_grounded_uie Memory

## 服务器环境约束 (westd-37397)

- **DeBERTa NLI 本地路径**: `/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large`。HF cache 路径不完整（下载被中断），必须传 `--nli_model_name` 指定本地路径，不能用 HF ID（AutoDL 无外网会失败）。
- **Qwen3-8B 本地路径**: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
- **tmux**: 已安装 v3.2a，`/usr/bin/tmux`
- **vLLM**: **不可用**。0.17.1 和 0.18.1 都与 torch 2.10.0 不兼容（`AssertionError: duplicate template name` in torch._inductor）。Blackwell SM120 + torch 2.10 + vLLM = 死路。GRPO 用 HF native generation。
- **GPU**: 8× NVIDIA RTX PRO 6000 Blackwell (SM 120), 每卡 ~98GB
- **SDPA 自动生效**: transformers 4.57.6 默认使用 SDPA，不需要安装 flash-attn。
- **CUDA_VISIBLE_DEVICES 映射规则**: submit_training_job 自动注入 CUDA_VISIBLE_DEVICES，脚本内部必须用 `--device cuda:0`（不管物理 GPU 编号是多少）。用 `cuda:1` 在 `CUDA_VISIBLE_DEVICES=1` 下会报 "CUDA error: invalid device ordinal"。

## TRL 1.1.0 关键兼容性

- `SFTConfig.max_seq_length` → 已改为 `max_length`
- **GRPOConfig 无 max_prompt_length**: TRL 1.1.0 已移除，prompt 不截断
- **GRPOTrainer model 参数**: 传路径字符串（非模型对象），model_init_kwargs 传 dtype/attn
- **parse_json_output**: TRL 传 `list[dict]` chat message 格式给 reward 函数，已修复

## GRPO 采样参数（关键教训 2026-05-12）

**TRL GRPOConfig 默认 top_k=0 与 Qwen3 不兼容**。top_k=0 禁用 top-k 过滤 → 全词表采样 → 模型不生成 EOS → completions 全截断 → reward=0。

**必须设置**：`top_k=20, top_p=0.95`（匹配 Qwen3 模型默认值）。修复后验证：
- completions mean_length=743.8（自然终止）
- reward=0.4804
- clipped_ratio=0.333
- train_loss=-0.1361（有学习信号）

## GRPO max_completion_length 教训（2026-05-12）

**max_completion_length 必须 >= eval 的 max_new_tokens**。grpo_pilot_v1 用 1024 导致 100% clipped_ratio + 0 terminated + reward 全 0（steps 1-3），训练完全无效。

**长度链条约束**：SFT max_seq_length=4096 → eval max_new_tokens=2048 → GRPO max_completion_length >= 2048。
- 1024 太短：DocRED 多关系 JSON 输出在 1024 token 内无法完成
- GRPO v2 应设 max_completion_length=2048
- 单卡 2048 会 OOM（峰值 ~85GB），正式训练需用 2 卡

## GRPO 失败教训总结（2026-05-13）

**GRPO v1b 训练完全失败的根因**：KL=0.001 太低（有效 GRPO 训练需要 0.01-0.1），credit assignment 在长序列（1000-2000 tokens）上失败，reward 100 步内无显著增长。综合 LR=5e-6 太低 + batch=4 太小 + group=4 太小 → 梯度信号不足以移动策略。

## Reward 分布诊断（2026-05-13）

**Composite reward std=0.136 >> 0.05 阈值，Route A（超参调优）可行。**

关键发现：
- **Format reward 已饱和**：SFT 模型 format=1.0 (std=0)，在 GRPO 阶段贡献零梯度。占 20% weight = 死权重。v2 降至 0.05，provenance/structural 各 0.475。
- **Structural F1 方差最大 (std=0.223)**：GRPO 的主要学习信号来源。
- **Provenance std=0.172**：有区分度但偏右分布，9 个零值样本可能是 anchor cases。
- **v1b 默认 LR=5e-6**：远低于 Director 猜测的 1e-5/2e-5。v1b 策略未更新的主因之一。
- **Reward 分量不可用**：rewards.py 的 composite_reward() 只返回加权和，TRL 只 log composite。需离线 eval 才能拿到分量 breakdown。

## GRPO v1b eval 最终定论（2026-05-13）

**v1b eval 确认模型 ≈ SFT baseline**：RE-F1 0.4264 vs 0.4337 (-1.7%)，Evi-F1 0.3593 vs 0.3652 (-1.6%)，AP 0.9540 vs 0.9529 (+0.1%)。差异在噪声范围内，完全符合 KL=8.3e-5（策略未更新）预期。

**根因**：LR=5e-6 太低 + batch=4 太小 + group=4 太小 → 梯度信号不足以移动策略。v2 修正：LR 10x (5e-5)，batch 4x (16)，group 2x (8)。

## NLI Oracle 失败（2026-05-13，D006/D007）

**DeBERTa-v3-large NLI 在 DocRED evidence 上完全失效**。posthoc_nli_v3 结果：
- Gold evidence 平均 NLI 得分 = **0.4949**（≈随机，理论应接近 1.0）
- NLI > 0.5 比例 = 49.99%，NLI > 0.7 比例 = 46.84%
- 所有 NLI filter 阈值均降低 Evi-F1（0.3652 → 0.15-0.19）
- NLI rerank-top3 仅 0.3641 ≈ baseline 0.3652

**根因**：DocRED 的 evidence 是 sentence-level span，NLI 模型评估的是 premise-hypothesis 蕴含关系。两个语义空间不匹配——evidence span 不是 hypothesis 的 textual entailment。

**处置**：
- Provenance reward 中 nli_weight 0.3→0.0，iou_weight 0.5→0.8（D007）
- rewards.py 加 `nli_w > 0` guard 跳过 NLI 模型加载
- Narrative 采用 C+A：NLI 失败作为 motivation + 简化 kill criteria 为 GRPO vs SFT 直接对比（D006）

## AP 指标澄清（2026-05-13，Reviewer 发现）

**AP (Attribution Precision) 不是 evidence 质量指标，是格式完整率。** evaluate.py L106-110：`compute_attribution_precision` 只接收 pred_rels，不接收 gold_rels。逻辑 = 有 evidence 且非空的预测关系数 / 总预测关系数。不比对 gold evidence。

**Evi-F1 才是 evidence 质量指标**（L56-103）：比对 pred/gold evidence 的 sentence index 集合，计算 P/R/F1。

**后续**：AP 在论文中重定义为 "evidence coverage rate"，不作为 evidence 质量指标。Kill criteria 基于 Evi-F1 不受影响。

## SFT Baseline 锚点（2026-05-13，已修正）

**sft_eval_v5 是正确 baseline（修复 chat_template 后），v4 作废。**

sft_eval_v5（DocRED dev, 985 samples）：
- RE F1: **0.4337**
- Evidence F1: **0.3652**
- Evidence Coverage (AP): 0.9529（格式完整率，非质量指标）

vs sft_eval_v4（旧模板，thinking mode 污染输出）：RE-F1=0.2726, Evi-F1=0.238, AP=0.5139。模板修复带来 RE-F1 +59%, Evi-F1 +53%, AP +85%。

**教训**：Qwen3 thinking mode 对输出格式影响极大。AP 从 0.51→0.95 说明 thinking mode 导致大量输出格式不匹配。所有 eval 必须确认 chat_template 是修复后版本。

## Random Evidence Baseline（2026-05-13）

随机打乱 evidence indices 的 lower bound：RE-F1=0.4337（不变），Evi-F1=**0.0903**，AP=0.9529（不变）。SFT evidence 质量是 random 的 4.0x。

## DPO Candidate 生成（2026-05-13）

- **generate_dpo_candidates.py slicing bug**: 脚本先执行 `data[:max_samples]` 再执行 `data[resume_from:]`。如果 max_samples=1514 且 resume_from=1514，结果是空集。解决方案：后半部分不传 `--max_samples`，只传 `--resume_from`。
- **生成速度**: Qwen3-8B 在 RTX PRO 6000 上每 sample 生成 8 candidates 需要 ~32-35s。1514 samples ≈ 14h。双卡并行可以将总时间减半。

## Qwen3 Thinking Mode

- Qwen3 有 `<think>...</think>` thinking mode，采样时触发
- **禁用方式**：修改 `chat_template.jinja`，去掉 `enable_thinking` 条件判断，无条件输出 `<think>\n\n</think>\n\n`
- train_grpo.py 中也通过 `chat_template_kwargs={"enable_thinking": False}` 传递
- rewards.py 中加了 `<think>` 标签剥离作为 fallback
- **影响量化**：thinking mode ON vs OFF，RE-F1 差 59%，AP 差 85%（sft_eval_v4 vs v5）

## GRPO 显存约束

- max_completion_length=2048 单卡 OOM（峰值 ~85GB，差 2.3GB）
- max_completion_length=1024 单卡 OK（峰值 ~34GB）
- **正式训练用 2 卡**：2048 completion + bf16 + gradient_checkpointing 应稳过
- per_device_train_batch_size 需是 num_generations 的倍数

## Eval 脚本教训（2026-05-12）

- **旧代码在 Blackwell 上卡死**：逐条 generate + max_length=2048 + 无 PYTHONUNBUFFERED → 6h+ 零产出。修复后（batch=8, 4096, PYTHONUNBUFFERED）正常。
- **max_length 必须与训练一致**：SFT 用 4096，eval 也必须 4096。
- **rerank_nli.py --predictions_file**：复用 evaluate.py 输出，串行执行。

## OOM 教训

- Qwen3-8B bf16 + LoRA rank 32 + max_seq_length=4096 + batch_size=4 → OOM
- 瓶颈：logit shift 操作 vocab_size(151936) × seq_length × batch
- 修复: 降 seq_length + 降 batch_size + 升 grad_accum

## 术语

- 用 "evidence provenance reward" / "grounding reward"，不用 "faithfulness reward"（避免与 MR-UIE 撞词）
