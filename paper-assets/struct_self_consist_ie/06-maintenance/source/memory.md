# Experiment Memory

## exp_e2_pretrained_fewnerd — Analysis (2026-05-21)

### Setup
- Model: Qwen2.5-7B-Instruct (pretrained, no fine-tuning)
- Dataset: FewNERD (37,648 instances)
- SC pipeline: N=8, T=1.0, seed=42

### Key Metrics

| Metric | FewNERD | CoNLL (ref) |
|--------|---------|-------------|
| Greedy F1 | 0.5121 | 0.5385 |
| Oracle F1 | 0.6175 | 0.6275 |
| Oracle headroom | +0.1054 | +0.0890 |
| Fleiss κ (mean) | 0.4501 | 0.5470 |
| Soft Jaccard (mean) | 0.6881 | 0.7764 |
| Sample F1 (mean±std) | 0.523±0.332 | 0.581±0.384 |
| Sample F1=0 (%) | 18.2% | 23.4% |
| Full ρ(κ,F1) | +0.383 | +0.377 |
| Full ρ(SJ,F1) | +0.433 | +0.392 |
| Cond ρ(κ,F1) | +0.371 | +0.435 |
| Cond ρ(SJ,F1) | +0.440 | +0.467 |
| Structural > Surface | YES (+0.050) | YES (+0.015) |
| LP full ρ | +0.189 | -0.020 (ns) |
| LP full AUROC | 0.596 | 0.538 |
| LP cond ρ | +0.176 | +0.210 |
| LP cond AUROC | 0.593 | 0.580 |
| Verdict | PASS | MARGINAL |

### Conclusion: SUCCESS

**Correlation-selection gap confirmed on pretrained model.**

1. **Gap exists**: Oracle F1 (0.618) exceeds Greedy F1 (0.512) by 10.5pp — substantial untapped selection potential in the 8 samples
2. **Agreement correlates with correctness**: ρ(SJ,F1) = +0.43 (p≈0), but this correlation does NOT close the gap via naive MV → classic correlation-selection gap
3. **Structural > Surface**: Soft Jaccard beats Fleiss κ as quality signal by +0.050 ρ — consistent across both datasets
4. **Logprob weak**: LP correlation exists (ρ=0.19) but much weaker than agreement-based signals — LP alone insufficient for selection
5. **Cross-dataset consistency**: Gap pattern replicates across FewNERD (37.6K instances) and CoNLL (3.5K instances), with FewNERD showing larger headroom and stronger structural advantage

**Implication**: The gap is model-intrinsic (not a fine-tuning artifact). Pretrained Qwen2.5-7B already exhibits the phenomenon where agreement signals predict quality but standard aggregation fails to exploit this — motivating learned selection/weighting approaches.

## Pretrained MV — 3/3 datasets positive (2026-05-21)

Pretrained Qwen2.5-7B-Instruct MV strict is **positive on all 3 datasets**:
- FewNERD: MV Δ = +3.90±0.22pp, degen=11.7%, α_crit=0.356±0.088 (3-seed)
- SciERC: MV Δ = +1.54±0.48pp, degen=0.8%, α_crit=0.151±0.004 (3-seed)
- CoNLL: MV positive (待汇总精确数字)

Finetuned MV is negative on all 3 datasets. This pretrained-vs-finetuned contrast is a core narrative element.

## 5-epoch Epoch Confound Analysis (2026-05-22, updated)

### 3-epoch vs 5-epoch FewNERD (finetuned)

| 指标 | 3-epoch | 5-epoch (3-seed Mean±Std) |
|------|---------|--------------------------|
| greedy_f1 | 0.7969 | 0.7978±0.0002 |
| mv_strict_f1 | 0.7695 | 0.7942±0.0008 |
| MV Δ | -2.74pp | -0.36±0.09pp |
| degeneracy | 8.8% | 26.2±0.7% |
| **LP Δ** | **+1.39pp** | **+0.12±0.04pp (2-seed)** |

**LP Selection 坍塌**: 5-epoch LP Δ 从 +1.39pp 降至 +0.12pp（**-91%**）。LP 只在 ~6.3% instances 选了与 greedy 不同的 sample——5-epoch 模型太 peaked，logprob 分布几乎没有区分力。Pilot (n=5000) 显示 +0.624pp 高估了效果；全量 (n=37648, 2 seeds) 更准确。

**叙事链**: pretrained(degen 11.7%, MV +3.9pp) → 3-epoch(degen 8.8%, MV -2.74pp) → 5-epoch(degen 26.2%, MV -0.36pp, LP Δ ≈0)

**注意**: 3-epoch degen(8.8%) < pretrained degen(11.7%) — 非单调！Fine-tuning 初期降低 degeneracy（因为模型变得更确信但输出仍有变化），5-epoch 才导致坍塌。叙事需处理这个非单调性。

## SciERC 3-Seed Finetuned N=8 方差分析 (2026-05-22)

MV Δ = -0.50 ± 0.74pp（per-seed greedy baseline, micro-F1）。方差大于均值绝对值（σ=0.74 > |μ|=0.50），方向不一致：s42=-1.01pp, s123=+0.34pp, s456=-0.84pp。

**关键洞察**: Greedy F1 跨 seed 极稳定（0.6640±0.0024），不稳定性完全来自 MV 聚合过程。SciERC 的 degeneracy 低（12.6%），样本多样性足够，但 MV 的 selection 效果是 seed-dependent 的——这说明 MV 对 SciERC finetuned model 既不稳定地 help 也不稳定地 hurt，属于 noise regime。

**与 N-scaling 表的关系**: N-scaling table 用 unified greedy baseline 报告 -1.24pp（单 seed=42），per-seed baseline 为 -1.01pp。差异源于 baseline 计算方式不同。3-seed mean (-0.50pp) 比单 seed (-1.01pp) 更温和。

## Per-type FewNERD Analysis (2026-05-21)

**θ 依赖性是关键 — 之前报告的 +0.90 仅在 strict MV 下成立：**

| 配置 | θ | Pearson r | p-value |
|------|---|-----------|---------|
| exp_021 (3-epoch) | 0.5 (strict) | **+0.87** | **0.005** |
| mf4v2 (3-epoch) | 0.5 (strict) | +0.77 | 0.024 |
| exp_021 | 0.25 (liberal) | -0.52 | 0.19 (ns) |

**机制**: strict MV (θ=0.5) 是强过滤器，easy types 样本一致性高→MV 保留大部分实体；hard types 样本分散→MV 丢弃过多→F1 下降大。Liberal MV (θ=0.25) 反而让 hard types 受益（聚合多样正确实体）。

**含义**: 排除了 "baseline quality confound"——strict MV 下，高 greedy_f1 实体类型 MV loss 更大（非更小），符合直觉。

Artifact: `art_20260521_81fcee` (fewnerd_per_type_mv_analysis)
Server JSON: `/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_per_type_mv_analysis.json`

## N-scaling 关键方法论发现 (2026-05-22)

### 统一 Instance 集 (P0)
不同 N 的独立运行各自解码 greedy，导致 greedy baseline 微漂移（SciERC 52/529 instances, CoNLL 24/2756 instances 不一致）。这使 MV Δ 呈现非单调（SciERC N=64 的 MV Δ 反而低于 N=32）。

**解决方案**: 固定 N=8 的 greedy 解码作为所有 N 的统一 baseline，只在 greedy 一致的实例子集上计算。结果：SciERC 和 CoNLL 的 MV Δ 均完美单调递增。**论文 Figure 必须用统一基线数据。**

### SciERC N=32 Multi-seed 高方差
s42 +0.78pp, s123 +0.12pp, s456 −0.17pp → mean +0.24±0.49pp。MV 增益在 N=32 尚不稳定，需 N=64 统一基线下的 +0.53pp 作为更可靠的证据点。CoNLL N=32 稳定（+0.46, +0.55, mean +0.51±0.05pp）。

### LP-best Δ 饱和行为
- SciERC: LP Δ 稳定在 ~+3pp (N=8→64 变化不大)——LP 区分力不随 N 提升
- CoNLL: LP Δ 随 N 递减 (+1.18→+0.26)——高 degeneracy 下 LP 区分力尤其弱

**含义**: LP-best 是一种"挑最自信的样本"策略，N 越大也不会更好（不像 MV 可以从更多投票中受益）。这区分了 LP 和 MV 两种 selection 策略的 N-scaling 行为。

### Pretrained N-scaling 确认
方向翻转在 N=32 仍成立：SciERC PT +1.97pp, CoNLL PT +3.21pp。Pretrained MV 增益随 N 略增（SciERC +1.43→+1.97），与 finetuned 的从负到正趋势形成对比。

## Freeform Decoding Ablation (2026-05-22)

**核心发现**: 移除 XGrammar 约束后，FewNERD 几乎无变化，CoNLL 有小幅变化。

| 指标 | CoNLL Δ (free-constrained) | FewNERD Δ |
|------|---------------------------|-----------|
| greedy_f1 | -0.42pp | +0.00pp |
| degeneracy | +3.0pp (56.7%→59.3%) | 0.0pp (9.1%→9.1%) |
| mv_delta_pp | +0.43pp (less hurt) | +0.01pp |
| lp_delta_pp | — | +0.02pp |

**机制解释**: FewNERD 有 8 大类 66 细粒度实体类型，输出空间天然受约束——移除 grammar 约束不改变模型行为。CoNLL 仅 4 类粗粒度实体，grammar 约束对输出格式有边际贡献（degeneracy 升 3pp）。

**论文意义**: 确认 degeneracy 是 model-intrinsic 而非 constrained decoding artifact。两个数据集的对比进一步说明 schema 复杂度与 grammar 约束必要性的关系。

## vLLM Unicode Surrogate Bug (2026-05-22)

**问题**: vLLM 偶尔在生成文本中产生 lone Unicode surrogates (`\ud800`-`\udfff`)，`json.dumps(ensure_ascii=False)` 传递到 `open(path, "w", encoding="utf-8")` 时 UTF-8 编码拒绝，导致 UnicodeEncodeError crash。

**修复**: `sampling.py:673` 添加 `errors='replace'`，用 `�` 替代不可编码的 surrogates。已应用到 autodl-5090-c。**autodl-5090 尚未修复**，下次在该服务器跑实验前需同步修复。
