# Top-k Ablation Negative Result: Literature Context

## 实验背景

CED RSFT top_k ablation 结果为 negative：
- top_k=3: rel_f1=0.4454, ign_f1=0.4364
- top_k=1: rel_f1≈0.46
- 增加 k 引入更多噪声训练样本，降低关系抽取精度

## 文献中的共识

### 1. RAFT 框架的关键设计：top-1 selection from K candidates

RAFT (Dong et al., TMLR 2024) 定义了 RSFT 的标准框架：每轮生成 K 个 response，用 reward model 排序，**始终只取 top-1** 做 SFT。论文的 ablation 显示 K∈{8,16,32} 时性能随 K 增加而提升（K=8→2.180, K=16→2.251, K=32→2.329），但这是因为更大的候选池提供了更好的 top-1 样本——而非保留更多样本训练。

这恰好与我们的实验形成对照：
- **RAFT 的 K**：候选池大小，增大→更好的 top-1→性能提升
- **我们的 top_k**：保留样本数，增大→引入次优样本→性能下降

RAFT 隐式地做出了 "只用最好的 1 个" 的设计选择，我们的 ablation 从实验角度验证了这个选择的合理性。

### 2. Best-of-N 文献：N 增大导致 reward hacking

literature_map.yaml 中 Category 13 收录了 4 篇直接相关论文：

- **Huang et al. (ICML 2025)** "Is Best-of-N the Best of Them?"：证明 BoN 在 N 增大时 provably suffers from reward hacking——proxy reward 持续改善但 true reward 先升后降。根本原因是 reward model 作为不完美代理，选择压力越大，over-optimization 越严重。
- **Chen et al. (NeurIPS 2025 Spotlight)** "Inference-Time Reward Hacking"：true reward 的先升后降是所有 inference-time 选择机制的固有属性，提出 BoP 和 HedgeTune 缓解。
- **Ichihara et al. (TMLR 2025)**：系统评估 BoN reward hacking，提出 SRBoN 正则化方法。
- **Jinnai et al. (NAACL 2025)**：MBR-BoN 用 proximity regularizer 约束选择偏离度。

虽然这些论文讨论的是 inference-time reranking，但核心机制完全适用于 training-time data selection：**当 reward model（此处为 CED score）不完美时，选择更多样本放大了 proxy-true reward 的 misalignment**。

### 3. 训练数据噪声的放大效应

- **DART-Math (NeurIPS 2024)**：在数学推理 rejection tuning 中发现，放宽选择阈值（保留更多样本）增加数据量但引入噪声，downstream 性能非单调——存在 sweet spot。
- **AdaSTaR (NeurIPS 2025)**：指出 RFT 的随机采样导致已解决样本被过度训练、困难样本训练不足，进一步论证了 naive top-k 扩大选择集的问题。
- **RLHF Book (Nathan Lambert)**：指出 rejection sampling 中 "more completions can improve the best available sample, but only if the reward model can separate good and bad answers"——隐含条件是 reward model 必须足够准确，否则扩大选择集只是放大噪声。

### 4. 对 CED top_k=3 negative result 的解释

综合文献，我们的 negative result 可归因于两个交互因素：

1. **CED score 作为不完美 proxy**：CED 用 NLI entailment 评估 evidence quality，但 evidence quality 与 relation extraction correctness 并非完全对齐。top_k=1 时只取 CED 最高分的样本，proxy 偏差影响小；top_k=3 时第 2、3 名样本的 CED score 更可能 reward-hack——evidence 看起来好但 RE triple 有误。

2. **噪声稀释训练信号**：即使第 2、3 名样本不是 reward hacking，它们客观上也是次优样本。将它们与最优样本混合训练，稀释了每个 prompt 的训练信号强度，等价于在 SFT loss 中引入 label noise。

## 建议

### 不需要加入 literature_map.yaml 的论文
上述关键论文（Huang et al., Chen et al., Ichihara et al., Jinnai et al., DART-Math, AdaSTaR）**已全部收录**在 literature_map.yaml 中。

### 可考虑补充的论文
- Nathan Lambert, *RLHF Book*, Chapter 9: Rejection Sampling (https://rlhfbook.com/c/09-rejection-sampling) — 作为 practitioner guide 补充，讨论了 completion 数量与 reward model 分辨力的交互，但无实验数据，优先级低。

### 写作建议
在论文 ablation section 中报告 top_k 结果时，可引用 Huang et al. (2025) 的 BoN reward hacking 理论和 RAFT 的 top-1 design choice 作为文献支撑，论证 "CED scoring 的最优 k=1 与 BoN 文献中 reward over-optimization 的发现一致"。
