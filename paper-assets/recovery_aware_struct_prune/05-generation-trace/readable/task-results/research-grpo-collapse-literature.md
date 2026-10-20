# research grpo collapse literature

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_grpo-collapse-literature_20260515T183839_result.json`
- **Structured JSON:** [`b8e4cfa1f5d0d28c0ee7.json`](../../sessions/b8/b8e4cfa1f5d0d28c0ee7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have enough data to compile the results. Here's the synthesis.

---

## 搜索结论

### 方向 1: Structured Pruning + RLVR/RL Fine-tuning Failure Modes

**该方向暂无直接先例。** 没有找到任何论文报告剪枝模型在 GRPO/RLVR 训练中出现 collapse。这是你们发现的核心新颖性。最近几篇相关论文从不同角度接近这个问题：

### 方向 2: Pruning 与 Training Plasticity

有较强的理论支撑文献，尤其是 Dohare et al. (Nature 2024) 和 Lyle et al. (2024) 的 plasticity loss 框架可直接解释 CKA-pruned 模型在 RLVR 中的 collapse。

### 方向 3: Functional Redundancy 在 RL Training 中的作用

Ma et al. (ICML 2025) 发现 random sparsity 反而帮助 RL scaling——但这是 **random** pruning from scratch，与你们的 **targeted structural redundancy removal** 截然不同。这个对比恰好支持你们的论点：有目的地移除冗余结构比随机稀疏化更危险。

---

## YAML 产出

```yaml
literature_entries:

  # === Direction 1: Structured Pruning + RLVR Failure Modes ===

  - id: wang2025think_prune
    title: "Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models"
    authors: "Ziyan Wang et al."
    year: 2025
    venue: "arXiv"
    category: method-component
    role: "Shows pruning severely damages reasoning LLMs — even 20% sparsity can collapse accuracy; introduces RESP framework with reasoning-aligned calibration"
    relevance: 8
    key_finding: "Existing pruning methods cause catastrophic accuracy collapse on reasoning LLMs at moderate sparsity (20%+) due to mismatch between calibration data and reasoning dynamics"
    our_relation: "Directly supports our observation: CKA-pruned model's reasoning capacity is fragile. Their finding that generic calibration destroys reasoning parallels our RLVR collapse — pruning decisions misaligned with downstream task demands"
    citation_priority: high
    arxiv_id: "2512.02185"

  - id: ding2026llms_to_lrms
    title: "From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models"
    authors: "Longwei Ding et al."
    year: 2026
    venue: "arXiv"
    category: background
    role: "Controlled study showing pruning strategies don't transfer from instruction-following LLMs to reasoning-augmented LLMs"
    relevance: 7
    key_finding: "Width pruning is more robust for reasoning tasks than depth pruning; static pruning better preserves reasoning performance than dynamic pruning"
    our_relation: "Our CKA-guided pruning is a form of width pruning (removing attention heads/FFN channels). Their finding that even 'better' width pruning still degrades reasoning supports the hypothesis that structural redundancy removal harms reasoning capacity"
    citation_priority: high
    arxiv_id: "2601.18091"

  - id: huang2025reasoning_compression
    title: "When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models"
    authors: "Huang et al."
    year: 2025
    venue: "arXiv"
    category: background
    role: "Mechanistic analysis of how compression affects reasoning via attribution patching on DeepSeek-R1"
    relevance: 7
    key_finding: "Weight count impacts knowledge memorization more than reasoning; MLP up projection in final layers is critical; protecting 2% of excessively compressed weights raises accuracy by 6.57%"
    our_relation: "Provides mechanistic explanation for why CKA-pruned models may fail in RLVR — CKA identifies representational redundancy but may miss functionally critical weights for downstream RL training dynamics"
    citation_priority: medium
    arxiv_id: "2504.02010"

  - id: exploring_limits_pruning_2026
    title: "Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific LLMs"
    authors: "Anonymous"
    year: 2026
    venue: "arXiv"
    category: background
    role: "Shows task-specific neurons exist; removing ~10% causes complete performance collapse with sharp threshold at 15-20%"
    relevance: 8
    key_finding: "Robustness threshold at 15-20% pruning; removing a small subset of highly task-specific neurons (~10%) causes complete collapse; fine-tuning can recover performance"
    our_relation: "Directly relevant: our CKA-guided pruning may be inadvertently removing task-specific neurons for RL training. The 'collapse threshold' concept maps to our RLVR collapse observation"
    citation_priority: high
    arxiv_id: "2604.27115"

  - id: sun2025gtpo
    title: "GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control"
    authors: "Sun et al."
    year: 2025
    venue: "arXiv"
    category: background
    role: "Identifies gradient conflicts and policy collapse as fundamental GRPO failure modes"
    relevance: 6
    key_finding: "Token-level penalization creates conflicting gradient updates on valuable tokens; negatively rewarded completions can penalize confident responses and flatten likelihood distribution, causing policy collapse"
    our_relation: "Explains the GRPO-side mechanism of our collapse. A pruned model with reduced capacity likely amplifies these gradient conflicts — fewer parameters means less ability to resolve conflicting token-level signals"
    citation_priority: medium
    arxiv_id: "2508.03772"

  # === Direction 2: Pruning + Training Plasticity ===

  - id: dohare2024plasticity
    title: "Loss of Plasticity in Deep Continual Learning"
    authors: "Shibhansh Dohare, J. Fernando Hernandez-Garcia, Parash Rahman, Richard S. Sutton, A. Rupam Mahmood"
    year: 2024
    venue: "Nature"
    category: background
    role: "Foundational work showing deep networks lose plasticity over training; only algorithms injecting diversity (random reinitialization) maintain it"
    relevance: 9
    key_finding: "Standard deep learning methods gradually lose plasticity until they learn no better than a shallow network. Sustained learning requires a random, non-gradient component to maintain variability"
    our_relation: "Core theoretical frame for our finding. CKA-guided pruning removes 'redundant' structures — but these may be the diversity reservoir needed for plasticity during RLVR. Standard pruning preserves more random diversity, explaining its survival"
    citation_priority: critical
    arxiv_id: null  # Nature paper, not arXiv

  - id: lyle2024disentangling
    title: "Disentangling the Causes of Plasticity Loss in Neural Networks"
    authors: "Clare Lyle et al."
    year: 2024
    venue: "arXiv (TMLR 2025)"
    category: background
    role: "Decomposes plasticity loss into independent mechanisms; shows layer norm + weight decay maintain plasticity in RL"
    relevance: 8
    key_finding: "Plasticity loss has multiple independent causes; no single intervention suffices; combination of LayerNorm + weight decay is effective; particularly relevant in RL where data distributions are non-stationary"
    our_relation: "CKA-pruned model likely has compounded plasticity loss mechanisms — removing representationally similar units reduces the network's ability to reroute gradients, exactly the multi-mechanism failure described here"
    citation_priority: high
    arxiv_id: "2402.18762"

  - id: liu2024neuroplastic
    title: "Neuroplastic Expansion in Deep Reinforcement Learning"
    authors: "Jiashun Liu, Johan Obando-Ceron, Aaron Courville, Ling Pan"
    year: 2024
    venue: "arXiv"
    category: method-component
    role: "Proposes growing networks from small to large during RL training to maintain plasticity; includes dormant neuron pruning"
    relevance: 7
    key_finding: "Dynamically growing the network maintains learnability; dormant neuron pruning + experience review balances plasticity-stability tradeoff"
    our_relation: "Inverse of our approach: they grow to maintain plasticity, we prune and lose it. Their success with expansion supports the hypothesis that our CKA-pruned model lacks sufficient capacity for RLVR adaptation"
    citation_priority: medium
    arxiv_id: "2410.07994"

  # === Direction 3: Functional Redundancy in RL Training ===

  - id: ma2025sparsity_scaling
    title: "Network Sparsity Unlocks the Scaling Potential of Deep Reinforcement Learning"
    authors: "Guozheng Ma, Lu Li, Zilin Wang, Li Shen, Pierre-Luc Bacon, Dacheng Tao"
    year: 2025
    venue: "ICML 2025"
    category: background
    role: "Shows random static sparsity HELPS RL scaling — sparse networks resist plasticity loss and gradient interference better than dense ones"
    relevance: 9
    key_finding: "One-shot random pruning before training improves RL performance; sparse networks achieve higher parameter efficiency and stronger resistance to plasticity loss and gradient interference"
    our_relation: "CRITICAL CONTRAST: Random sparsity helps RL, but targeted redundancy removal (our CKA pruning) hurts it. This distinction is the crux of our contribution — it's not sparsity per se that causes collapse, but the selective removal of representationally similar (but functionally important for RL) structures"
    citation_priority: critical
    arxiv_id: "2506.17204"

  - id: ma2025rethinking_dst
    title: "Rethinking the Role of Dynamic Sparse Training for Scalable Deep Reinforcement Learning"
    authors: "Guozheng Ma, Lu Li, Zilin Wang, Haoyu Wang, Shengchao Hu, Leszek Rutkowski, Dacheng Tao"
    year: 2025
    venue: "arXiv"
    category: background
    role: "Shows fixed pruning masks lock models into obsolete structure; architectural improvements matter more than dynamic sparsity regimes"
    relevance: 7
    key_finding: "Fixed pruning masks fail because they optimize for early-stage data distributions, missing connections needed for later tasks; representational collapse occurs without LayerNorm"
    our_relation: "Our CKA-guided pruning creates a fixed structural change before RLVR. The mask is optimized for pre-RLVR representations but may be catastrophically wrong for the non-stationary RLVR training distribution"
    citation_priority: high
    arxiv_id: "2510.12096"
```

---

## 关键发现总结

1. **方向 1（Pruning + RLVR collapse）无直接先例** — 没有人报告过剪枝模型在 GRPO/RLVR 中 collapse。这是强新颖性信号。最近论文只讨论了剪枝对 reasoning accuracy 的静态影响，未涉及 RL post-training dynamics。

2. **方向 2（Plasticity）有强理论支撑** — Dohare (Nature 2024) 的核心论点是：sustained learning 需要 diversity reservoir（随机非梯度组件）。CKA pruning 恰好移除了 representationally similar 的结构，减少了这个 reservoir。

3. **方向 3 有一个完美的反例** — Ma et al. (ICML 2025) 证明 random sparsity 帮助 RL，但你们的 targeted redundancy removal 导致 collapse。这个对比构成论文的核心 argument：**不是 sparsity 本身有害，而是移除功能冗余（functional redundancy）破坏了 RL training 所需的 plasticity buffer**。

Sources:
- [Think Before You Prune (2512.02185)](https://arxiv.org/abs/2512.02185)
- [From LLMs to LRMs (2601.18091)](https://arxiv.org/abs/2601.18091)
- [When Reasoning Meets Compression (2504.02010)](https://arxiv.org/abs/2504.02010)
- [Exploring the Limits of Pruning (2604.27115)](https://arxiv.org/abs/2604.27115)
- [GTPO (2508.03772)](https://arxiv.org/abs/2508.03772)
- [Loss of Plasticity in Deep Continual Learning](https://www.nature.com/articles/s41586-024-07711-7)
- [Disentangling the Causes of Plasticity Loss (2402.18762)](https://arxiv.org/abs/2402.18762)
- [Neuroplastic Expansion in Deep RL (2410.07994)](https://arxiv.org/abs/2410.07994)
- [Network Sparsity Unlocks RL Scaling (2506.17204)](https://arxiv.org/abs/2506.17204)
- [Rethinking Dynamic Sparse Training (2510.12096)](https://arxiv.org/abs/2510.12096)
- [DAPO (2503.14476)](https://arxiv.org/abs/2503.14476)

---
