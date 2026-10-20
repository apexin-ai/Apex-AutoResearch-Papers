# Paper Framing — Phase-Gated Compound Sparsity

> 最后更新: 2026-05-14 | 维护者: Director

## Core Insight

Compound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 在 low-sparsity reasoning phase 产生 12-75× severity amplification，而 random eviction 保持 ~1× 平坦。这一发现挑战了 compound degradation 均匀分布的隐含假设。

## Narrative Arc

Compound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 在 distributed-attention phase 剧烈放大 compound degradation（gradient 12-75×），而 random eviction 在所有 phase 保持平坦（~1×）。我们通过 entropy-discrimination collapse 机制解释这一现象：head pruning → attention 重分布 → importance score 的判别力崩塌 → importance eviction 退化为有偏伪随机。这一发现为 phase-aware sparsity allocation 提供了动机。

**Framing 硬约束（D015）**：
- MUST: "emergent phase-strategy interaction"
- MUST NOT: "importance metric limitation / importance is broken"

## Core Claims

| ID | Claim | Status | Key Evidence |
|----|-------|--------|-------------|
| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance gradient 12-75× vs random ~1× |
| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | low phase >> high phase at all 4 sparsity levels; monotonic increase 12.8→28.7→52.9→74.9 |
| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.584 < random=3.002, importance low_phase=30.903 > random=2.915 |
| C4 | Entropy-discrimination collapse explains the mechanism | partially_confirmed | Conceptual argument solid; empirical attention entropy data not yet collected |
| C5 | Finding generalizes across model families | pending | Qwen2.5-7B-Instruct experiments in progress |
| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: 2.24×→1.84×→1.42× |

## Anticipated Reviewer Concerns

### RC1: Generalizability — 7B models only, single benchmark
- **预期质疑**: "Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?"
- **应对**: Cross-model replication (DeepSeek + Qwen, 不同架构血统) 是第一层防御。MATH-500 是 standard benchmark。Limitations 明确声明 scale 限制。机制解释 (entropy-discrimination collapse) 是 architecture-agnostic 的，原则上适用于任何 attention-based model。
- **实验支撑**: C5 (Qwen cross-model), 若需加强可扩展到更多模型

### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量
- **预期质疑**: "The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?"
- **应对**: 如果有 GPU 预算，可以直接测量 pruned vs unpruned 的 attention entropy 和 importance score 分布。目前 C4 status = partially_confirmed，需要决定是否投入 GPU 时间做 direct measurement。
- **实验支撑**: 可选 ablation：测量 attention entropy pre/post pruning × phase

### RC3: Practical impact — 没有 throughput 数据
- **预期质疑**: "No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?"
- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。
- **实验支撑**: 不需要额外实验

### RC4: Statistical rigor — bootstrap 是否足够
- **预期质疑**: "Per-problem bootstrap with 50 problems — sufficient sample size?"
- **应对**: B=10000 iterations, all p=0.0000, CI 不跨零。50 problems 的 paired bootstrap 统计效力已充分。可在 appendix 补充 per-problem 分布图。
- **实验支撑**: 已完成，fig4_bootstrap

### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity
- **预期质疑**: "ThinKV and phase-aware methods already consider phase. What's new?"
- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。
- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析

## Paper Positioning

**类型**: Empirical finding paper（非 method paper）
**核心贡献**:
1. 发现 compound sparsity severity 的 strategy × phase 交互
2. 量化 severity gradient（12-75×）和 crossover 现象
3. 提出 entropy-discrimination collapse 机制解释
4. Cross-model replication 验证泛化性

**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25
