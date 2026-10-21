# Memory — causal_style_decomp_judge

## Rebuttal 备弹: Llama-70B Cross-Benchmark (2026-05-24)

AEval formality BT=95.7% (n=47), AEval verbosity BT=97.0% (n=66), MTB formality BT=91.7% (n=36)。
三组 Likert 全部显著 (d=0.21-0.30)，Blindspot 消失。MTB verbosity 数据缺失。
**解读**: Blindspot 是 effect-size dependent——LLMBar 小效应 (BT~70%) 时 Likert 失灵，AEval/MTB 大效应 (BT>90%) 时 Likert 可检测。
GEE 因 near-perfect separation 全部 degenerate/不可靠。

## Rebuttal 备弹: Rewriter Independence (2026-05-24)

Llama-70B 重写器 + Qwen3 judge: BT=71.1% [64.3, 77.5], Likert NS (d=0.013).
与 Qwen3 重写器 baseline (BT=66.5%) 差 +4.6pp，CI 重叠。
**结论**: Formality bias 在 judge 端，与重写器独立。Blindspot 复现。

## Rebuttal 备弹: Llama-70B Scaled n=355 (2026-05-24)

BT=72.5% (非 Worker 误报的 88.1%——那是 consistent-pair win rate)。
LLMBar 子集 (n=89) BT=74.4%, Likert NS → Blindspot YES。
Full n=355 Likert 终于显著 (d=0.048, p=.026) → Blindspot NO。
**教训**: Likert 可以检测 formality bias，但需要 ~355 对才勉强显著，BT 在 88 对就极显著。效率差距 4x+。

## Verbosity n=355 Scaling Insights (2026-05-23)

GEE Style OR 大幅缩水证实 n=86 小样本上偏：Qwen 13.1→3.83 (-71%), Llama 8.21→4.01 (-51%)。
但 Likert blindspot 在 n=355 下对开源 judge 被打破（Qwen d=.149 p=.0006, Llama d=.160 p=.0001），
而 API judges 仍维持 blindspot（GPT-5.4 d=-.026 NS, Claude d=.032 NS）。

**Judge-family 异质性**：开源 judges 为 style-dominated (GEE Style OR 3.8-4.0, Orig OR<1)，
API judges 为 originality-dominated (Style OR ~1, Orig OR 1.7-2.0)。这是新发现，n=86 时不明显。

GPT-5.4 的 verbosity style effect 接近零（OR=1.06），但 originality effect 很强（OR=1.96），
说明 GPT-5.4 不真正偏好 verbose，而是偏好"原文"。

## R16 Construct Divergence Adjudication (2026-05-23)

Non-tie concordance 分析结论：**attenuation 为主**。
- Pooled concordance 76.6% (154/201), p<0.0001, CI [70.3%, 81.9%]
- Likert 平局率 60-75% 是 blindspot 主因，非构念分歧
- Item-level correlation: 8/9 conditions 显著 (r_pb=0.20-0.45)
- Bias-corrected OR (Nemes/Hedges) 校正 <2%，原始值稳健
- Llama-70B concordance 最高 (83-88%)，Qwen32b formality 最低 (67%)

论文建议：从"两种解释无法区分"改为"证据支持 attenuation，Likert 粗粒度评分导致信号衰减"

## R16 FK GEE Covariate (2026-05-23)

FK grade 作为 GEE covariate 显著改变 Style OR（avg |change| 30.4%）：
- GPT-4o: OR 2.70→2.15 (-20.2%, p变NS .132)
- Qwen3-32B: OR 4.20→3.38 (-19.6%, still sig .014)
- Llama-70B: OR 5.52→2.69 (-51.3%, still sig .037)
- FK 本身均 NS (p>.11)，说明 readability confounding 通过 style 间接作用

## R16 Direction-aware Gating (2026-05-23)

DA gating 不引入系统偏差：
- Bidirectional (n=65) BT%=78.5% vs DA-only (n=21) BT%=73.8%
- Permutation p=0.663, Likert d diff=0.009

## R16 Claude Likert Fix (2026-05-23)

Claude Likert 方法统一为 pole-aligned + Wilcoxon：
- LLMBar: form d=−0.021 p=.721, verb d=−0.039 p=.743
- AEval verb 符号翻转修正: d=−0.243 → d=+0.298 (语义正确)

## R16 Bayesian Equivalence (2026-05-23)

Claude LLMBar pooled BF₀₁：
- σ=0.3→0.57, σ=0.5→0.80, σ=1.0→1.48 (inconclusive)
- Verbosity only BF₀₁ 达 moderate evidence for null (σ=1.0→3.78)

## R15 补充分析 (2026-05-23)

- TOST pooled (LLMBar n=174): 84% power at Δ=10pp, equivalence at Δ=12pp (p=0.035)
- 100pt Likert: 降低 tie rate (GPT-4o 66%, Qwen 51%, Llama 40%) 但 ATE 仍 NS
- FK mediation: Sobel z=3.60, p=0.0003, 60.3% mediated by sentence length

## MF1 Human Annotation (2026-05-23)

- Gate precision: 98.6% [92.3, 99.8] (69/70 per annotator)
- Inter-annotator: AC1=0.958, raw agreement 96%, κ=−0.015 (prevalence paradox)
- Sensitivity: 排除 flagged pairs 后所有效应变化 <5%
- 4 disagreements (S073, S098, S063, S136), 2 sensitivity-flagged (S073, S063)

## Claude Negative Control 定位 (2026-05-22)

Director 决策：Claude 作为 negative control 限定 LLMBar only。
AEval/MTB 上 Claude 有强偏差 (BT 75-85%)，转为 "benchmark-dependent finding"。

## GPT-5.4 No-Go (2026-05-23)

GPT-5.4 在原始 LLMBar 三轴数据上 bias 方向全部反转（formality: P(formal)=.39, verbosity: P(verbose)=.44, register: P(academic)=.44）。不能替代 GPT-4o 作 drop-in replacement。等 Director 决策。

## API Key

OpenRouter key active: sk-or-v1-10197... (via TUM secret_req)
