# Paper Framing — FREIGE

> **状态**: POST-MVP (MVP-1 + MVP-2 均 PASS，进入 Research 阶段)
> **最后更新**: 2026-05-15

## Target Venue

- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)
- Stretch: ARR May 25 (10 days, 极紧，仅在实验全部顺利时考虑)
- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)

## Core Insight

LLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。朴素 NLI faithfulness reward 可被 entity-mentioning distractor 句子游戏——共享实体但不支持具体关系的句子仍获正面蕴含分数。

**CED (Contrastive Evidence Discrimination)** 通过文档内 hard negative 对比，将 evidence 质量评估从"是否蕴含"升级为"是否比最佳干扰句更蕴含"——本质上是 evidence grounding 场景下的 **anti-reward-overoptimization mechanism**（连接 Gao et al. 2023 reward overoptimization 理论）。

**MVP 关键发现**: CED 作为在线 RL (GRPO) reward 导致 catastrophic forgetting（3 种 reward type × 多个 lr 全线失败），但作为离线 RL (RSFT) 的候选筛选信号极其有效——4 组超参配置均稳定超过 SFT baseline。**方法论结论**: 对结构化 IE 任务，CED 应作为离线质量信号而非在线训练奖励。

## Story Arc

1. **Problem**: LLM DocRE 无证据 → 部署障碍（human-in-the-loop KB population、生物医学审计、RAG 溯源）
2. **Why naive reward fails**: flat-NLI 被 entity-sharing distractors 欺骗（SFT EDCR=71.2%，大量引用干扰句）
3. **Why online RL fails**: GRPO+CED/flat-NLI/extract-only 全部 catastrophic forgetting（reward ↑ + rel_f1 ↓ 至 <0.02）
4. **Solution**: CED 作为离线质量信号 + RSFT（rejection sampling fine-tuning）：SFT 模型生成 N 候选 → CED 打分筛选 → 微调，规避在线 RL 的遗忘风险
5. **Theoretical grounding**: 连接 LongRLVR (ICLR 2026) evidence grounding 梯度消失分析 + "RSFT=PPO" (ICML 2025) 等价性理论
6. **Result**: 首个 LLM-based DocRE 方法同时生成抽取和可验证证据

## Core Claims

### Claim 1 (Main): CED-scored RSFT 使 LLM 同时生成抽取和忠实证据
- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法
- RSFT+CED: rel_f1 +3.9~6.0pp over SFT, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp
- **MVP-2 已验证**: 4/4 configs PASS
- **Research 需要**: test set 评估，DREEAM/SAIS Evi-F1 直接对比

### Claim 2 (Ablation): CED scoring 优于 flat-NLI scoring 用于 RSFT
- CED-filtered RSFT vs flat-NLI-filtered RSFT 的 evi_f1 和 EDCR 差异
- CED 的对比性 margin 过滤掉 distractor-heavy 候选
- **Research 需要**: flat-NLI scored RSFT ablation（核心实验）

### Claim 3 (Analysis): 在线 RL 在结构化 IE 上 catastrophically forget
- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败
- 关键对比: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——CED 驱动了 evidence 学习但在线 RL 摧毁了抽取能力
- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据
- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功

### Claim 4 (Evaluation): EDCR 作为独立评估指标
- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|
- Evi-F1 盲区：不惩罚 plausible-looking distractor citations
- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）
- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比

## MVP Evidence Summary

| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |
|--------|--------|----------|--------|------|------|
| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |
| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |
| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |
| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |
| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |
| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |
| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |

## Anticipated Reviewer Concerns

### RC1: NLI reward 信号质量（高概率攻击）
- **攻击**: "DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声"
- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径
- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比

### RC2: Gold evidence 标注不完整导致 false distractor
- **攻击**: "被标为 distractor 的句子可能是 annotator 遗漏的有效证据"
- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱
- **Research 补充**: false-distractor 鲁棒性量化分析

### RC3: 评测可比性
- **攻击**: "生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？"
- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation

### RC4: 单数据集 + 单模型泛化性
- **攻击**: "只在 DocRED + Qwen3-4B 上验证"
- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation

### RC5: RSFT vs GRPO 是否公平对比
- **攻击**: "GRPO 失败可能是超参问题而非方法论问题"
- **应对**: 完整 GRPO 轨迹——3 种 reward × 多个 lr × 全 checkpoint eval；D020 控制变量下 CED 是唯一存活的 reward type

### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限
- **攻击**: "RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著"
- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确
- **Research**: CED reranker PoC（运行中），top_k ablation

### RC7: 方法过于简单
- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度

## Key Baselines (8+)

1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL
2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）
3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法
4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中
5. **GRPO+CED**: 在线 RL with CED reward — negative baseline
6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)
7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)
8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)
9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)

## Publishability Threshold

- **必要条件**: RSFT+CED 在 test set 上 Evi-F1 > DREEAM 57.34 AND rel_f1 显著 > SFT baseline
- **充分条件**: 上述 + CED vs flat-NLI RSFT Evi-F1/EDCR 差异显著 + GRPO 分析完整
- **Failure pivot**: Evi-F1 < 57.34 on test set → 转为 analysis contribution（在线 vs 离线 RL for structured IE）

## Research Phase Priorities

| Priority | 实验 | Claim | 预估 GPU-hours |
|----------|------|-------|---------------|
| P0 | CED vs flat-NLI RSFT ablation | C2 | ~20h |
| P0 | Test set evaluation (RSFT best config) | C1 | ~4h |
| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h |
| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h |
| P1 | CED-as-reranker (running) | C1 bonus | ~6h |
| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h |
| P1 | Re-DocRED extension | RC4 | ~12h |
| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h |
| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h |
| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h |
