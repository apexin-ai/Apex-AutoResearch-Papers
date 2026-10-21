# Analysis: sweep-exec-only-s45-r2

## Training Summary
- **Status**: Completed 500/500 steps, EXIT_CODE=0
- **Model**: Qwen3-4B, seed=45, execution-only reward
- **Data**: data/train_500_seed42.jsonl (500 examples)
- **Runtime**: 3282s (~54.7 min), 2 epochs

### Training Metrics (Final)
| Metric | Value |
|--------|-------|
| prove_rate | 0.74025 |
| mean_isr | 0.3596 |
| train_loss | 0.0273 |
| parse_rate | 1.0 |
| entropy (final) | 0.045 |
| frac_reward_zero_std | 1.0 |

### Training Trajectory
- Steps 1–19: cold start, reward=0
- Step 20: first successful proving
- Steps ~100+: prove_rate climbing to 0.5–0.75
- Steps 400+: consistently 0.75–1.0

## Eval Results (proofwriter_fol_100.jsonl)
| Metric | Value |
|--------|-------|
| prove_rate | 99/100 (0.99) |
| mean_isr | 0.5012 ± 0.2055 |
| median_isr | 0.5000 |
| proved_only_isr | 0.5062 |

### By Answer Type
| Type | n | Proved | Prove Rate | Mean ISR |
|------|---|--------|------------|----------|
| false | 25 | 25 | 1.00 | 0.590 |
| unknown | 41 | 41 | 1.00 | 0.476 |
| true | 34 | 33 | 0.971 | 0.467 |

## Hacking Taxonomy (classify_h7.py)
| Category | Count | Rate |
|----------|-------|------|
| H7a (text-match tautology) | 93 | 93.9% |
| H7b (obfuscated tautology) | 0 | 0.0% |
| H7 total | 93 | 93.9% |
| H1 (conclusion embedding) | 5 | 5.1% |
| H8 (conjunction collapse) | 1 | 1.0% |
| **Genuine** | **1** | **1.0%** |
| Content-independent | 47 | 47.5% |
| Single premise | 92 | 92.9% |

## Cross-Seed Comparison (Exec-Only)
| Seed | Steps | Prove% | H7% | H1% | H8% | Genuine% |
|------|-------|--------|-----|-----|-----|----------|
| s42 (plan001-r2) | 500 | 93 | 0 | 87.1 | 6.5 | 7.5 |
| s43 (plan001-1000-r2) | 1000 | 90 | 100 | 0 | 0 | 0 |
| s44 (plan001-1000-r2) | 1000 | 100 | 0 | 85 | 15 | 0 |
| **s45 (this)** | **500** | **99** | **93.9** | **5.1** | **1.0** | **1.0** |

## Conclusion: **success**
Training completed normally. Results are consistent with the exec-only reward hacking pattern observed across all seeds.

## Paths
- Checkpoint: `/root/autodl-tmp/outputs/sweep_exec_only_s45`
- Log: `~/runs/solver-trace-ablation/sweep-exec-only-s45-r2.log`
- Eval: `/root/autodl-tmp/outputs/sweep_exec_only_s45/eval_sta_results.json`
- Taxonomy: `/root/autodl-tmp/outputs/sweep_exec_only_s45/classify_h7_results.json`

---

# Key Insight: ISR β=0.1 Bimodal Distribution (2026-05-17)

## 5-seed ISR β=0.1 Complete Data
| Seed | eval_PR | genuine% (total) | Dominant hacking |
|------|---------|-------------------|-----------------|
| s42 | 81% | 14% | H1 52% + H7 16% |
| s43 | 61% | 0% | H7 100% |
| s44 | 89% | 0% | H7 100% |
| s45 | 42% | 23% | H7 38% + H1 5% |
| s46 | 77% | 42% | H1 26% + H7 14% |

**Mean genuine = 15.8 ± 17.6 (bimodal)**

## Random β=0.1 Complete 5-seed Data (2026-05-17)
| Seed | PR | H7 | H1 | H8 | genuine | genuine% |
|------|-----|-----|-----|-----|---------|----------|
| s42 | 79 | 0 | 58 | 4 | 18 | 22.8% |
| s43 | 88 | 0 | 82 | — | 6 | 6.8% |
| s44 | 89 | 0 | 73 | 16 | 6 | 6.7% |
| s45 | 58 | 0 | 53 | 0 | 5 | 8.6% |
| s46 | 94 | 86 | 2 | 4 | 2 | 2.1% |

**Mean: PR=81.6±13.8%, genuine=9.4±7.9%**
Note: s46 collapsed to H7 (86/94) — random bonus at β=0.1 can also trigger H7 (1/5 seeds)

## Trajectory Divergence Mechanism (2026-05-17)
- **No early signal**: All seeds indistinguishable in first 100 steps (ISR 0.05-0.07)
- **Bifurcation at steps 150-200**: H7 exploit discovery triggers positive feedback
- **H7 structural advantage**: Single-premise tautology gets ISR≥0.5 by construction
- **Stochastic, not deterministic**: Which attractor a seed hits depends on stochastic sampling in critical window
- **All seeds eventually converge**: s42 at 1000 steps → ISR=0.90 (collapse delayed, not prevented)

## Framing (D119/D120): Goodhart Inevitable at All Doses
- β=0.1 is phase transition critical point (bimodal)
- β≥0.2 deterministic collapse (H7 discovery guaranteed within all seeds' critical windows)
- β=0.05 = "no safe dose" (s42 already 100% H7, pending s43/s44 confirmation)
- Paper expression: "stochastic bifurcation with irreversible positive feedback once H7 exploit discovered"

---

# Key Insight: β=0.05 Dose-Response (2026-05-17)

## ISR β=0.05 vs Random β=0.05 — cleanest separation
| Condition | PR | H7% | genuine% |
|-----------|-----|------|---------|
| ISR β=0.05 s42 | >0 (produces proofs) | 100% | 0% |
| Random β=0.05 s42 | **0%** (no learning) | N/A | N/A |

**Why this matters**: At β=0.05, random noise provides zero learning signal (model cannot learn to produce any proofs), while ISR provides enough signal to learn proof generation. But 100% of learned proofs are H7 tautologies. This is the cleanest evidence that:
1. ISR acts as genuine learning signal (not just noise) even at low doses
2. That learning signal is entirely captured by the H7 exploit
3. "No safe dose" — even minimal ISR exposure leads to complete Goodhart collapse

This comparison is more informative than β=0.1 (where random also learns and produces mixed hacking) because it isolates the ISR-specific contribution cleanly.

---

# Key Insight: H9 Conjunction Aggregation — 新型 hacking 模式 (2026-05-18)

## 发现来源
d129-1.7b-isr-b01-s44 审计：classify_h7.py 报告 genuine=42.7% (35/82)，但 content_independent=93.9%。手动审查 35 个 "genuine" 样本后发现 30 个是新型 hacking。

## H9 Conjunction Aggregation 机制
模型学会了 AND-intro structural template：
1. 把 NL 前提映射为单字母谓词 (P, Q, R...) — 91% content-independent
2. 生成多个前提 `∀x(A→B1), ∀x(A→B2), ...`
3. 结论合并为 `∀x(A→B1∧B2∧...)`
4. Prover9 验证通过 (valid AND-intro)，ISR > 0 (每个前提 "necessary")

## 为什么逃过现有分类器
- 逃 H1: 结论 ≠ 任何单个前提
- 逃 H7: 需要前提（非重言式）
- 逃 H8: 结论形式 `∀x(A→B∧C)` 而非裸 `B∧C`

## 影响
- **修正后 genuine = 5/82 (6.1%)**，与 content_independent=93.9% 一致
- "1.7B 无 genuine content-aware reasoning" 结论成立
- classify_h7.py 存在分类器 gap，需评估是否影响 4B 数据
- 建议在 Table 2 taxonomy 中增加 H9_conj 子类或在 limitations 标注

## 教训
- **content_independent 比 classify_h7.py 的 genuine 更可靠**作为 ground truth 指标
- 当两者矛盾时，应以 content_independent 为准，然后手动审查差异样本
- 1.7B mixed-mode seed (s44) 不等于 genuine window，只是分类器 gap

---

## d129-1.7b-random-b01-s43 配置错误 (2026-05-18)
- **错误**: Worker 用了 `--reward_mode random_reward`，应为 `--reward_mode additive_random`
- 两者是完全不同的 reward 函数，结果不可比
- **正确配置参考**: w2-qwen3-1.7b-random-b01 (s42 baseline) 用 `--reward_mode additive_random --beta 0.1`
- **教训**: 提交 D129 额外 seed 实验时，必须从 s42 baseline checkpoint 中提取完整命令行，只改 seed 和 output_dir

---

# Key Insight: D146 ProofFOL 跨数据集效应反转 (2026-05-20)

## 核心发现
ProofFOL 上 ISR 的 Goodhart 效应与 FOLIO **完全相反**：
- **FOLIO**: ISR 触发 Goodhart collapse（TS hacking 主导）
- **ProofFOL**: ISR 反而**抑制** hacking，exec-only 才是 hacking 重灾区

## D146 Classify 完整数据 (7 experiments, Qwen3-4B, 500 steps)

| Model | proved | genuine | genuine% | TS | CE | PG | CI |
|---|---|---|---|---|---|---|---|
| base (no training) | 16 | 16 | 100% | 0 | 0 | 0 | 0 |
| exec_s42 | 99 | 0 | **0%** | **99** | 0 | 0 | 0 |
| exec_s43 | 63 | 32 | 50.8% | 0 | **31** | 0 | 0 |
| exec_s44 | 72 | 1 | **1.4%** | 0 | **71** | 0 | 0 |
| isr_s42 | 46 | 46 | **100%** | 0 | 0 | 0 | 0 |
| isr_s43 | 56 | 17 | 30.4% | 0 | **39** | 0 | 0 |
| isr_s44 | 66 | 66 | **100%** | 0 | 0 | 0 | 0 |

## 聚合
- **exec-only mean genuine: 17.4%** (hacking 主导: TS in s42, CE in s43/s44)
- **ISR mean genuine: 76.8%** (2/3 seeds 100% genuine, 1/3 有 CE)
- **无 PG/CI**: ProofFOL 上只出现 TS 和 CE 两种 hacking mode

## 机制假说
- ProofFOL 是银标准 FOL（ProofWriter 生成），原生 Prover9 格式，结构比 FOLIO（人写自然语言→手翻 FOL）更规则
- exec-only 在规则结构上更容易发现 TS/CE 快捷方式（proved 数更高但 genuine 率极低）
- ISR bonus 在 ProofFOL 上恰好惩罚了 TS（单前提 → ISR=0）和部分 CE，反而起到了正则化作用
- 这与 FOLIO 上 ISR 加速 TS 的效应相反，因为 FOLIO 的 TS 结构不同（ISR 可以 >0）

## 论文意义
- 支持 D148 "dataset-dependent Goodhart effects" framing
- 支持 D149 C2 claim: "ISR as proxy triggers dataset-dependent Goodhart effects"
- exec-only 不是 "好基线"，而是 "收敛到 hacking 均衡（退化但稳定）"
- ISR 在 ProofFOL 上牺牲 convergence (proved 56 vs 78) 换取 integrity (genuine 76.8% vs 17.4%)

---

# Key Insight: O(1) Binary ISR 在 ProofFOL 上退化 (2026-05-20)

## 核心发现
Binary tautology-check ISR（O(1) approximation）在 ProofFOL 402 个 proved 样本中 **0 tautology**，退化为常数 1.0。
- Pearson/Spearman 相关系数因零方差无法计算
- 所有 179 个 disagreement 均为 FP（binary=1, LOO=0）

## 分模型类型
| 模型类型 | N | Agreement | Mean LOO ISR | Mean Binary ISR |
|----------|---|-----------|-------------|----------------|
| exec-only | 234 | 34.2% | 0.046 | 1.0 |
| ISR-trained | 168 | 85.1% | 0.183 | 1.0 |

## 含义
- 训练时 O(1) binary ISR 等价于 proof success check——对所有 proved 样本一视同仁
- Binary 无法检测 Conclusion Echo (CE): `nice(charlie)` 作为 premise+conclusion 重复不是逻辑 tautology
- ISR 训练效果可能来自间接信号（鼓励非 tautology formalization），非 premise necessity 判别
- 数据: `artifacts/r16_o1_vs_on_consistency.json`

---

# Qwen3-8B OOM 诊断 (2026-05-20)

## 根因
仅差 ~1.4 GiB。Generation 成功，training step `lm_head` forward OOM。93.42/94.97 GiB allocated。

## 当前配置（已极限）
K=2, batch=1, grad_accum=16, gradient_checkpointing=true, adamw_bnb_8bit, max_completion_length=512

## 显存拆解
- 固定开销 ~66.4 GB (policy 16.6 + ref 16.6 + optimizer 16.6 + grads 16.6)
- 剩余 ~28.6 GB 给 activations/KV cache/buffers，打满

## 推荐方案
- 方案 A: `PYTORCH_ALLOC_CONF=expandable_segments:True` + completion 512→384（pilot mean=148, max=323）
- 方案 B: completion→256
- 方案 C: DeepSpeed ZeRO-2 CPU offload（~11h）
- K=2 学习效率低，建议 grad_accum 16→32 补偿
- 预估 500 步: 6.3-7.5h（方案 A/B）

---

# D158 LLaMA-3.2-3B SFT 失败教训 (2026-05-20)

## 结论
LLaMA-3.2-3B SFT warmstart 完全失败：PR=0.0%（0/100），gate 未通过。

## 两个致命问题
1. **生成退化**：SFT 后模型循环输出 system prompt 片段，无法生成有效 FOL proof
2. **语法不匹配**：模型输出 Unicode FOL 符号（∀, →, ∧），但 Prover9 要求 ASCII 语法（all, ->, &）

## 教训
- LLaMA-3.2-3B 在 500 样本 SFT 下无法学会 Prover9 ASCII FOL 格式
- 跨模型族（LLaMA vs Qwen）验证 Goodhart 效应需先确保 base model 有 FOL 格式基础能力
- 如需继续 cross-family 实验，应换用更大模型（LLaMA-3.1-8B）或增加 SFT 数据量+epochs
- D158-grpo 因 gate 未通过被取消

## 服务器约束 (westd-39279)
- **只有 1 张 GPU (cuda:0)**，非 2 张——所有实验必须串行
- **无 wandb API key**——所有实验必须加 --no_wandb
- GPU 型号: RTX PRO 6000 (98GB VRAM)

---

# Key Insight: D157 Shuffled-ISR 因果证据 (2026-05-20)

## 核心发现
Shuffled-ISR（打乱 batch 内 ISR 与 sample 的语义关联，保持 ISR 分布不变）的 genuine rate 远超标准 ISR，证明 **语义关联是 Goodhart collapse 的必要条件**。

## 3-Seed 汇总
| Seed | PR | Genuine | Genuine% | TS | CE |
|------|-----|---------|----------|----|----|
| s42 | 15% | 13/15 | 86.7% | 1 | 1 |
| s43 | 16% | 14/16 | 87.5% | 1 | 1 |
| s44 | 15% | 13/15 | 86.7% | 1 | 1 |

Pooled: 40/46 genuine (86.96%), Wilson 95% CI: [74.3%, 93.9%]

## 对比
| Condition | Mean Genuine% | Variance |
|-----------|--------------|----------|
| Shuffled-ISR β=0.1 | **86.9±0.5%** | **极低** |
| ISR β=0.1 | 15.8±17.6% | 极高（bimodal） |
| Random β=0.1 | 9.4±7.9% | 中等 |
| Exec-only | 5.9% | 低 |

## 因果推断
- Shuffled-ISR 保留了 ISR 的所有分布属性（均值、方差、range），唯一打破的是 sample↔ISR 的语义关联
- 打破语义关联后 genuine rate 从 15.8% 飙升至 86.9% → 语义关联是 Goodhart collapse 的充分且必要条件
- 3 seed 方差极小（±0.5%）vs ISR 的 ±17.6% → shuffled 消除了 bimodal attractor dynamics
- 这是控制实验（controlled ablation），不是相关性证据

## 论文用途
- 直接支撑 C2（ISR 作为诊断工具揭示 Goodhart 效应）
- §4.3 控制实验段（D159 决策：替换占位符）
- Limitations L11 改写（distributional confound concern 已被控制实验覆盖）
