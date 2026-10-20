# Negative 实验系统性复盘

> 18 个 conclusion=negative 实验，按 Group 合并分析。SFT baseline: rel_f1=0.4057 (Qwen3-4B, DocRED dev)。

---

## Group 1: GRPO lr5e6 全轨迹 (5 evals)

**实验**: mvp2_eval_lr5e6_r1_ckpt20 / ckpt40_r2 / ckpt60_r2 / ckpt80 / ckpt100

**一句话**: lr=5e-6 无法挽救 GRPO+QLoRA 灾难性遗忘，200 步全程 rel_f1 < 0.014。

### 1. 证伪了什么？

**假设**: "ced_kl001_r4 (lr=5e-5) 的灾难性遗忘源于学习率过高，降到 5e-6 可恢复关系抽取能力。"

证伪。lr 降 10x 后 rel_f1 从 max 0.217 (lr5e-5) 进一步恶化到 max 0.014 (lr5e-6)。遗忘在 step 20 即已发生且不可恢复。

### 2. 当时怎么处理的？

- D030: ckpt-20 FAIL 后扩展到全 checkpoint 轨迹评估
- D031: ckpt-40 更差后判死 GRPO+QLoRA 方向，pivot 到离线 RL (RSFT/DPO)
- D032: kill 训练释放 GPU
- D033: 全 6 checkpoint 确认，记为论文 negative result

### 3. 处理是否正确？

正确。此时已有两个 LR（5e-5 和 5e-6）的完整证据链，且后续 bf16 实验 (plan_011) 证实根因是 QLoRA 量化而非 GRPO 本身。Pivot 到 RSFT 是正确决策。

**遗漏诊断**: lr5e6 的 evi_f1 从 0.628 单调升至 0.850（超 SFT 0.798），说明 CED reward 确实在驱动证据能力提升。如果当时就意识到这是"单侧学习"（evidence 学到了但 relation 崩了），可以更早形成 decoupling claim 的 framing。

### 4. 推导链是否完整？

完整。lr5e-6 → lr5e-5 → bf16 (plan_011) 形成了完整的消融链，最终确认 QLoRA quantization 是 catastrophic forgetting 的根因 (D052: Δ=+23.8pp)。

---

## Group 2: GRPO Mode Collapse (3 experiments)

### mvp2_grpo_ced_r5 — CED reward 被 shortcut hack

**证伪假设**: "CED reward (format×0.3, f1×3.0, ced×1.0) 在 kl_coef=0 下可稳定训练。"

证伪。模型发现极短输出（34 tokens）即可获得 ced_reward≈0.99 + format_reward=0.3，完全放弃关系抽取。

**处理**: D014 提出 F1 门控（CED reward 仅在有有效 triple 时计算），D16 kill 释放 GPU。但 D020 发现 F1 门控从未实现，直到 ced_kl001_r4 才在 kl_coef=0.01 下跑出结果。

**处理正确性**: 部分正确。F1 门控方案合理但执行延迟。后续 ced_kl001_r4 用 kl_coef=0.01 替代了缺失的 F1 门控，但两者是互补的——F1 门控从未被真正测试。

### mvp2_grpo_extract_r3 — Extraction-only reward 停滞

**证伪假设**: "纯 extraction reward (format×0.3, f1×3.0) 可建立 stable GRPO baseline。"

证伪。num_gen=4 + kl_coef=0 导致 4 个输出完全相同 → reward_std=0 → 梯度消失。从 step 520+ grad_norm=0，训练实际已冻结。

**处理**: D17/D22/D23 kill 并记录 ablation 结论（CED dense signal 是 GRPO 训练必需的）。

**处理正确性**: 正确，但可追问：如果 extract_r3 用 num_gen=8 + kl_coef=0.01 会怎样？D020 配置下 extract_r4 仍在 step 10 后 f1_reward=0（D22），说明 extraction-only reward 本质上信号密度不足。

### mvp2_grpo_flatnli_r6 — Flat-NLI collapse

**证伪假设**: "Flat-NLI reward 在 D020 稳定配置 (kl=0.01, G=8) 下可维持训练。"

证伪。Step 25 即 frac_zero_std=0.9，f1/NLI reward 全零，仅 format hacking。

**处理**: D24/D25 kill，确立 "三路对比仅 CED 存活" 的 ablation 结论。

**处理正确性**: 正确。三路 reward ablation (CED/extract-only/flat-NLI) 在同一配置下的对比是干净的实验设计。

**Group 2 整体遗漏**: 所有 mode collapse 实验用的 num_gen=4 或 kl=0 配置偏极端。但 D020 配置 (G=8, kl=0.01) 下 extract-only 和 flat-NLI 仍 collapse 而 CED 存活，说明 CED reward 的信息密度确实是关键差异。无遗漏。

---

## Group 3: CED Reward Hacking (3 evals)

**实验**: mvp2_eval_ced_kl001_r4_early (step50) / step90 / step100

**一句话**: CED reward 训练曲线上升但 eval F1 崩塌，经典 reward hacking + QLoRA 灾难性遗忘。

### 1. 证伪了什么？

**假设**: "CED reward + kl_coef=0.01 + G=8 + lr=5e-5 可以在避免 mode collapse 的同时提升任务指标。"

证伪。训练 reward 从 0.3 升至 1.37，但 eval rel_f1 max=0.217（SFT=0.4057），EDCR=0.86 (高) 但 recall 崩塌。模型学会了少预测以获高 EDCR。

### 2. 当时怎么处理的？

- D26/D27: 诊断为 lr=5e-5 过高 + CED recall shortcut
- 启动 P0 (lr=5e-6) 和 P0+P1 (recall penalty)
- P0+P1 因 recall penalty 梯度爆炸被 kill (D28/D29)
- P0 也全线失败（见 Group 1）
- 最终 D31 pivot 到离线 RL

### 3. 处理是否正确？

部分正确。Pivot 是对的，但诊断归因不够精确——当时归因为 "lr 过高" 和 "CED recall shortcut"，后来 plan_011 证明真正根因是 QLoRA quantization (D52)。如果当时直接尝试 bf16 训练而非 lr sweep，可以节省约 12h GPU 时间。

### 4. 推导链是否完整？

完整（通过后续 plan_011 补全）。lr5e-5 → lr5e-6 → bf16 → 确认 quantization 是根因。recall penalty 方向被正确放弃（梯度不稳定）。

---

## Group 4: DPO Failures (4 records, 3 独立实验)

### plan_012_dpo_ced (3 epochs) — 严重过拟合

**证伪假设**: "DPO+CED preference pairs (β=0.1, 3ep, 2666 pairs) 可以替代 online GRPO。"

证伪。rewards_accuracy=1.0, margins 9x 膨胀, rel_f1=0.3429（低于 SFT baseline 6.3pp）。

**处理**: 识别为过拟合 confound，重训 1 epoch。

### plan_012_dpo_ced_1ep / eval_plan_012_dpo_ced_1ep — 1ep 灾难性崩塌（后证实为 bug）

**证伪假设**: 原以为证伪 "1 epoch DPO 可消除过拟合问题"。

**实际**: rel_f1=0.0022 是 eval bug（缺 --sft_adapter 参数）。D064 发现后重跑。

### eval_plan_012_dpo_1ep_fixed_r2 — DPO 1ep = SFT（无提升）

**证伪假设**: "DPO+CED preference learning 可以改善 SFT baseline。"

证伪。修复后 rel_f1=0.4034，vs SFT=0.4057 (Δ=-0.23pp)。DPO 1ep 中性，无正向收益。

### 处理

- D61: 关闭 DPO 线（基于 bug eval）
- D63/D64: 发现 --sft_adapter bug，重跑
- D67/D68: 修正叙事为 "DPO 中性/轻度退化"

### 处理正确性

**遗漏**: 
1. DPO 3ep rel_f1=0.3429 + evi_f1=0.8403 呈现与 GRPO 一致的 decoupling 方向（rel↓ evi↑），这在 D62/D69 被正确识别为跨方法系统性现象。
2. **未探索**: β 调参（0.1 可能过大）、更少 epochs（0.5ep?）、不同 pair 构造策略。但考虑到 1ep 已经是中性结果，DPO 路线被正确放弃。

### 推导链完整性

完整。1ep→3ep 的非单调退化 + bug 修复后中性结果 = DPO 对此任务无效。作为 RL spectrum 数据点有论文价值。

---

## Group 5: RSFT top_k=3

### reeval_rsft_topk3

**证伪假设**: "RSFT 取 top_k=3 (更多训练数据) 优于 top_k=1。"

证伪。rel_f1=0.4454 vs CED RSFT top_k=1 约 0.46 (低约 1.5pp)。更多样本引入噪声。

**处理**: 记为 negative，保留 top_k=1 作为最优策略。

**处理正确性**: 正确。但有一个未探索方向：top_k=1 with higher CED threshold（只取 CED score 极高的样本）可能进一步提升质量。当前 top_k=1 实质是 "per-doc best CED score sample"，但未对绝对 CED 分数做 threshold 过滤。

**推导链**: 基本完整。top_k=3 vs top_k=1 的对比清晰。D078 进一步确认 CED vs flat-NLI 统计不可区分。

---

## Group 6: Truncation Diagnosis

### mvp2_eval_rsft_r2b_maxtok1536_r2

**证伪假设**: "EDCR 偏低 (0.66) 是因为输出被 1024 token 截断，增加 max_tokens 可显著改善。"

证伪。1536 tokens 后 truncated 179→146 (-33)，EDCR 0.6609→0.6740 (+0.013)，效果微乎其微。Distractor citation 是 RSFT 模型的真实行为。

**处理**: 确认 EDCR 偏高是 RSFT 固有局限（模型 spray-and-pray 引用），不再追求 truncation 修复。

**处理正确性**: 正确。此实验干净地隔离了 truncation vs distractor 两个因素。

**遗漏**: 后续未直接用 CED-as-reranker 尝试去除 distractor citations（在推理时过滤低 CED 分的 evidence）。D037 曾提出此方案但因 RSFT eval bug 被搁置，修复后未再跟进。

---

## Group 7: Cross-dataset Transfer

### plan_007_redocred_rsft_eval_r2

**证伪假设**: "CED-RSFT improvements on DocRED transfer to Re-DocRED。"

F1=0.0025 (catastrophic)，但 Evi-F1=0.8837 正常。

**处理**: 诊断为 pipeline bug（adapter loading / prompt format / relation label mapping）。后续 r4/r5 修复后成功（SFT baseline Re-DocRED Ign-F1=0.3659, D080）。

**处理正确性**: 正确。Evi-F1 正常排除了模型彻底崩坏的可能，明确指向 pipeline 问题。

**推导链**: 完整。r2 bug → 修复 → r4/r5 成功。

---

## 最终总结：被忽视的方法改进线索

### 线索 1: RSFT + 推理时 CED Reranking（去除 Distractor Citations）

**来源**: Group 6 (truncation diagnosis) + D037 (CED-as-reranker 被搁置)

**线索**: RSFT 模型 EDCR=0.66 是因为 spray-and-pray 式引用 distractor sentences。当前方案接受这个行为不做处理。但 CED 本身是强判别器（MVP-1: accuracy 81.5%, margin 0.48），可以在推理时对每个 predicted triple 的 evidence sentences 逐条做 NLI 过滤，去除 CED score 低于 threshold 的 citations。

**为什么有潜力**: 
- 不需要额外训练，纯推理时增强
- CED 判别能力已验证
- EDCR 从 0.66 提升到 0.80+ 是合理预期（参考 GRPO 训练后 EDCR 约 0.85-0.99）
- 可以作为论文的 inference-time component，与 RSFT training-time 互补

**建议验证**: 对 RSFT 输出的每个 triple 的 evidence list，用 DeBERTa NLI 逐条评分，去除 entailment score < tau 的 sentences。评估 EDCR 变化和 Evi-F1 变化。成本：约 30min 推理时间，无训练开销。

### 线索 2: bf16 GRPO → RSFT 两阶段训练

**来源**: Group 1 (GRPO evi_f1 单调提升) + D51 (bf16 GRPO rel_f1=0.4549)

**线索**: bf16 GRPO (plan_011) 达到 rel_f1=0.4549 + evi_f1=0.8086，与 RSFT (0.46 + 0.81) 基本平齐。两者各有优势：GRPO 优化 reward 信号（包括 CED 对 evidence 质量的直接监督），RSFT 通过数据筛选保持训练稳定性。未尝试过的组合：SFT → RSFT (筛选高质量样本) → 短程 bf16 GRPO (进一步优化 evidence 质量)。

**为什么有潜力**:
- RSFT 后模型已有良好的 rel_f1 基础，短程 GRPO 不太可能导致灾难性遗忘
- GRPO 对 evidence quality 的优化是在线的（可以利用 CED 做 per-step feedback），RSFT 是离线的（只能用固定 CED 阈值）
- bf16 已证明无 catastrophic forgetting

**建议验证**: 从 RSFT checkpoint 开始，bf16 GRPO 20-50 步（低 lr=1e-6），只用 CED reward（不加 f1 reward 避免冲突），评估 EDCR 是否显著提升且 rel_f1 不退化。

### 线索 3: DPO 数据质量问题——pair 构造策略可能是失败根因

**来源**: Group 4 (DPO 1ep 中性，3ep 退化)

**线索**: 当前 DPO pairs 构造为 "CED top-1 = chosen, CED bottom-1 = rejected"。但 D078 证明 CED vs flat-NLI 统计不可区分，且 CED 在 data selection 上无显著优势。这意味着 DPO pairs 的 preference signal 本身可能太弱——chosen 和 rejected 在关系抽取质量上可能差异不大，仅在 evidence 质量上有差异。DPO 因此只学到了 evidence 偏好（evi_f1 上升）而对 relation extraction 无正向信号（rel_f1 不变或下降）。

**为什么有潜力**: 如果改用 rel_f1-based pair construction（chosen = 关系抽取 F1 高的样本，rejected = F1 低的样本，同时要求两者 format 正确），DPO 的 preference signal 直接对准关系抽取任务，而非 evidence 质量。这可能打破当前 "DPO 只优化 evidence 无法提升 relation" 的困局。

**建议验证**: 从现有 RSFT candidates (8 generations per doc) 中重新构造 pairs：chosen = max(rel_f1) sample, rejected = min(rel_f1) sample（要求两者 format_ok）。用相同 DPO 配置 (beta=0.1, 1ep) 训练。如果 rel_f1 > 0.42 (超过 SFT+DPO-CED 的 0.4034)，说明 pair 构造是关键变量。
