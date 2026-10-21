# Evidence Summary — Capability Trap & Operating Regime

> 供 Methods Paper (D030) 使用。数据来源：project registry，2026-05-17 snapshot。

---

## Table 1: Operating Regime Evidence

按 SC baseline accuracy 排序，展示 SICA 增益随模型能力变化的模式。

| Model | Dataset | N | K | SC Acc | SICA Acc | Δ (pp) | p-value | C0 / Notes | exp_id |
|-------|---------|---|---|--------|----------|--------|---------|------------|--------|
| Mistral-7B-v0.3 | D012 (PW+FOLIO) | 60 | 12 | 48.3% | 48.3% | 0 | 1.0 | multi_candidate=6.7%; 太弱，无多样性 | exp-010-mistral-v3 |
| Qwen-14B | StrategyQA | 60 | 12 | 53.3% | 56.7% | +3.33 | n.s. | multi_candidate=10%; 方向正但N小 | exp-017-strategyqa-v3 |
| LLaMA-3.1-8B | D012 (PW+FOLIO) | 60 | 12 | 60.0% | 66.7% | +6.67 | 0.219 | multi_candidate=61.7%; sweet spot | exp-011-llama8b-v3 |
| LLaMA-3.1-8B | StrategyQA | 200 | 12 | 72.0% | 74.0% | +2.0 | 0.424 | discordant_rate=7%; 信号弱化 | exp-019-llama8b-strategyqa-200 |
| Qwen-14B | PW+FOLIO | 804 | 12 | 76.2% | 76.5% | +0.3 | n.s. | extraction=89%; 约束无增益 | sica_expanded_14b |
| Qwen-14B | ARC-Challenge | 60 | 12 | 96.7% | 95.0% | -1.67 | — | multi_candidate=8.3%; 天花板效应 | exp-018-arc-v2 |
| QwQ-32B | AIME | 22 | — | — | — | 0 | — | C0=10.3%(名义)/2.6%(有效); 推理模型自洽 | exp-005 |
| QwQ-32B | ProofWriter | 17 | — | — | — | -5.9 | — | 推理模型几乎不产生多样性 | exp-005 |
| LLaMA-3.1-8B | FOLIO | 204 | 12 | — | — | PENDING | — | RUNNING | exp-020-llama8b-folio-204 |

**Takeaway**: SICA 增益集中在 SC baseline 55-65% 区间（模型能力中等、输出多样性高）。低于 50% 模型太弱无法产生有质量的约束；高于 75% 模型已足够确定，多样性消失。推理模型（QwQ-32B）C0 极低，SICA 退化为 SC。整体呈现"倒 U 型"模式，但 sweet spot 极窄且增益在 powered test (N=200) 中不显著。

---

## Table 2: Mechanism Vacuousness Evidence

验证 SICA 的核心机制（MAX-SAT 优化、约束质量、K 敏感性）是否真正贡献增益。

### 2a. Constraint Aggregation Ablation (exp_id: sica_constraint_ablation_013)

| 聚合方式 | Accuracy | vs SC Δ | 意义 |
|----------|----------|---------|------|
| MAX-SAT (full SICA) | 76.49% | +0.25pp | 标准 SICA |
| Count-only (无权重) | 76.62% | +0.38pp | 去掉满足度权重 |
| Random-weight | 76.37% | +0.13pp | 随机权重 |
| SC baseline | 76.24% | — | majority vote |

- N=804, Qwen-14B, PW+FOLIO
- 802/804 题三种方式选择相同答案 (agreement 99.8%)
- McNemar p > 0.7 all pairs

**Takeaway**: MAX-SAT 优化相对简单计数和随机权重无统计差异。约束满足度信号被噪声淹没，优化组件事实上无效。

### 2b. Weighted SC Comparison (exp_id: exp-016-weighted-sc)

| 加权方式 | Accuracy | vs SC p-value |
|----------|----------|---------------|
| SICA (MAX-SAT) | 76.49% | — |
| Inv-length weighted | 76.74% | 0.453 |
| Length weighted | 75.25% | 0.153 |
| Constraint-count weighted | 75.25% | 0.066 |
| SC (uniform) | 76.24% | — |

- N=804, all non-significant
- Inv-length vs SICA: p=0.864

**Takeaway**: 所有加权方案（含 SICA）与 uniform SC 无显著差异。简单的启发式加权与复杂的 MAX-SAT 优化效果相同。

### 2c. K-Sensitivity (exp_id: sica_k_sensitivity_14b)

| K | SICA Acc | SC Acc | Δ (pp) |
|---|----------|--------|--------|
| 6 | 73.3% | 73.3% | 0 |
| 8 | 73.3% | 75.0% | -1.7 |
| 11 | 73.3% | 73.3% | 0 |
| 12 | 70.0% | 75.0% | -5.0 |
| 16 | 71.7% | 75.0% | -3.3 |
| 20 | 70.0% | 73.3% | -3.3 |

- N=60, Qwen-14B, D012 dataset
- 所有 K: SICA ≤ SC
- 更大 K → SICA 退化更严重

**Takeaway**: 增加采样次数不改善 SICA，反而因约束噪声累积导致退化。这与"更多证据应更好"的直觉相反，证实约束质量是瓶颈。

### 2d. Constraint Filtering Ceiling (exp_id: pilot-constraint-filtering)

| 指标 | 值 |
|------|-----|
| Discriminative ratio (by weight) | 37.2% |
| Discriminative ratio (by count) | 11.5% |
| Effective flip rate | 17.4% |
| Best gap (T=1) | +2.33pp |
| Gap at T≥5 | 0pp |

- N=43 (multi-answer problems from expanded set)
- 即使用最宽松阈值(T=1)，约束能区分答案的比例也很低

**Takeaway**: 约束过滤天花板极低。大部分约束对所有候选答案一视同仁（non-discriminative），无法提供超越投票的信息增量。

---

## Table 3: Cross-Domain Evidence

| Domain | Model | N | SC Acc | SICA Δ (pp) | Significant? | exp_id |
|--------|-------|---|--------|-------------|--------------|--------|
| ProofWriter | Qwen-14B | 600 | 75.2% | +0.3 | No | sica_expanded_14b |
| FOLIO | Qwen-14B | 204 | 79.4% | 0 | No | sica_expanded_14b |
| ProofWriter | LLaMA-8B | 30* | 60.0% | +3.33 | No | exp-011-llama8b-v3 |
| FOLIO | LLaMA-8B | 30* | 60.0% | +10.0 | bootstrap p≈0.04 | exp-011-llama8b-v3 |
| FOLIO | LLaMA-8B | 204 | — | PENDING | — | exp-020-llama8b-folio-204 |
| StrategyQA | Qwen-14B | 60 | 53.3% | +3.33 | No | exp-017-strategyqa-v3 |
| StrategyQA | LLaMA-8B | 200 | 72.0% | +2.0 | No (p=0.424) | exp-019-llama8b-strategyqa-200 |
| ARC-Challenge | Qwen-14B | 60 | 96.7% | -1.67 | No | exp-018-arc-v2 |
| AIME | QwQ-32B | 22 | — | 0 | — | exp-005 |

*exp-011 中 PW 和 FOLIO 各 30 题

**Takeaway**: 跨 4 个推理域（形式逻辑、常识推理、科学推理、数学），SICA 仅在 LLaMA-8B × FOLIO (N=30) 上达到边缘显著。该组合的 powered test (exp-020, N=204) 正在运行。即使该结果显著，也仅说明 sweet spot 局限于特定模型-域组合，不具备通用性。

---

## Claims 对应关系

| Paper Claim | 支撑证据 |
|-------------|----------|
| Claim 1 (Capability Trap) | Table 1 倒 U 型 + Table 2d 约束过滤天花板 + Table 2c K退化 |
| Claim 2 (Operating Regime is Empty) | Table 1 所有 powered test 不显著 + Table 2a/2b 机制无效 + Table 3 跨域一致 |
| Claim 3 (C0 as Diagnostic) | Table 1 中 C0/multi_candidate 与 delta 的对应: C0<7%→Δ=0, C0>60%→Δ>0 但约束质量不足 |

---

*Last updated: 2026-05-17. exp-020-llama8b-folio-204 标记为 RUNNING/pending.*