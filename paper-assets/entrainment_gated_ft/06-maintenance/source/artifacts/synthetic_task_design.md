# L-Sequential Function Composition Task: Design Document

## 1. Ye et al. (arXiv 2602.01763) Formal Construction 调研

### 1.1 论文概述

**Title**: A Provable Expressiveness Hierarchy in Hybrid Linear-Full Attention  
**Authors**: Xiaowei Ye, Xiaoyu He, Chao Liao, Chen Wu, Pinyan Lu  
**Date**: 2026-02-02  

论文建立了 hybrid linear-full attention 的表达能力层级：(L+1)-layer full attention 可解 L-sequential function composition，但 (L-1, 2^{3L^2}, ..., 2^{3L^2})-hybrid Transformer（即用 L-1 层 full attention + 指数多层 linear attention）无法解决。这是 hybrid attention 与 full attention 之间的首个可证明分离。

### 1.2 L-FuncComp 的精确定义

**Definition 2.5** (L-sequential function composition):

给定正整数 L >= 2，L-FuncComp(w, z_0, z_1, ..., z_L) 由以下参数定义：

- 正整数 m, n_1, ..., n_{L-1}
- 初始输入 z_0 in [m]
- 函数序列 z_1, ..., z_L，其中 z_l in A_l := {[N_{l-1}] -> [N_{l-1}]}
- 查询 w = (w_1, ..., w_{L-1}) in [n_1] x ... x [n_{L-1}]

**Domain size 递归定义**：

- N_0 = m
- N_l = m * prod_{l'=1}^{l} n_{l'}, for l in [0:L-1]

**计算过程**：

1. i_0 = z_0 in [m]
2. i_1 = z_1(i_0) in [N_0]
3. 对 l = 1, ..., L-1: i_{l+1} = z_{l+1}(w_l, i_l) in [N_l]
4. 最终输出 = i_L

**输入表示**：函数 z_l 的每个 entry 编码为一个 token（z_l 需要 N_{l-1} 个 token），查询 w 编码为一个 token。

### 1.3 关键理论结果

**Theorem 1.1**：当 Hdp <= n^{2^{-4L-2}} 时，(L-1, 2^{3L^2}, ..., 2^{3L^2})-hybrid Transformer 无法解决 L-FuncComp。其中 H = attention heads 数, d = head dimension, p = MLP hidden dimension。

**含义**：增加指数级多的 linear attention 层也无法弥补少一层 full attention 的损失。

### 1.4 理论构造 vs 实际评估的差异

| 维度 | 理论构造 | 实际评估（本设计） |
|------|---------|------------------|
| Domain size | N_l 指数增长 | 固定 \|Sigma\| = 10 |
| 函数类型 | z_l: [N_{l-1}] -> [N_{l-1}] | f_l: Sigma -> Sigma |
| 查询 w | 多维查询 (w_1,...,w_{L-1}) | 无（简化为纯 composition） |
| 评估方式 | 渐近下界证明 | 经验 accuracy 测量 |
| 目的 | 证明表达力分离 | 测量实际性能差距 |

理论构造中 domain size 指数增长是为了 communication complexity 下界证明所需，实际评估中不必如此。核心机制相同：模型必须在 forward pass 中完成 L 步顺序查找，前一步输出决定后一步输入。

---

## 2. 实际评估任务设计

### 2.1 Task Parameters

- **Alphabet**: Sigma = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, |Sigma| = 10
  - 选择数字而非字母：在 LLaMA-style tokenizer 中，单个数字可靠地为单 token
- **Functions**: f_l: Sigma -> Sigma, 随机满射映射（每个 task instance 独立采样）
- **Depths**: L in {1, 2, 3, 4, 5}
- **Format**: 8-shot in-context learning（每个 demonstration 使用不同随机函数）
- **Evaluation**: exact match on final answer token

### 2.2 为什么用随机映射而非随机置换

随机映射（允许多对一）比随机置换（双射）更难：
- 置换保证每个输出值恰好出现一次，模型可能利用排除法
- 随机映射无此性质，模型必须逐条查找

### 2.3 Prompt Format

两种变体，通过参数控制：

#### Variant A: Direct（主实验，对齐 Ye et al. 理论）

模型必须在 forward pass 中完成全部 composition，不生成中间步骤。

**Depth 1 示例**：
```
Apply the function to the input.

f: 0->3 1->7 2->1 3->5 4->9 5->0 6->8 7->2 8->6 9->4
Input: 4
Answer: 9

f: 0->1 1->5 2->8 3->2 4->0 5->6 6->4 7->3 8->9 9->7
Input: 6
Answer: 4

[... 6 more shots ...]

f: 0->6 1->3 2->9 3->0 4->7 5->2 6->1 7->8 8->4 9->5
Input: 7
Answer:
```

**Depth 3 示例**：
```
Compose the functions and give the final answer.

f1: 0->3 1->7 2->1 3->5 4->9 5->0 6->8 7->2 8->6 9->4
f2: 0->5 1->2 2->8 3->0 4->6 5->1 6->3 7->9 8->7 9->4
f3: 0->2 1->6 2->4 3->8 4->1 5->9 6->0 7->3 8->5 9->7
Input: 4
Answer: 1

[... 7 more shots ...]

f1: 0->6 1->3 2->9 3->0 4->7 5->2 6->1 7->8 8->4 9->5
f2: 0->1 1->5 2->4 3->8 4->0 5->9 6->3 7->6 8->2 9->7
f3: 0->7 1->0 2->3 3->6 4->9 5->1 6->5 7->4 8->8 9->2
Input: 7
Answer:
```

上例中 depth 3 的计算：f1(4)=9, f2(9)=4, f3(4)=1, 答案为 1。

#### Variant B: Chain-of-Thought（对比实验）

Demonstrations 显示中间步骤，模型也可以逐步生成。

**Depth 3 示例**：
```
Compose the functions step by step.

f1: 0->3 1->7 2->1 3->5 4->9 5->0 6->8 7->2 8->6 9->4
f2: 0->5 1->2 2->8 3->0 4->6 5->1 6->3 7->9 8->7 9->4
f3: 0->2 1->6 2->4 3->8 4->1 5->9 6->0 7->3 8->5 9->7
Input: 4
f1(4)=9 f2(9)=4 f3(4)=1
Answer: 1

[...]
```

### 2.4 Token Budget 估算

假设 LLaMA-style tokenizer (vocab_size=32000)：

| 组件 | 每条估算 tokens |
|------|----------------|
| 函数行 "f1: 0->3 1->7 ... 9->4\n" | ~35 |
| "Input: X\n" | ~4 |
| "Answer: Y\n\n" | ~4 |
| CoT 行 (depth L) | ~6L |

**Direct format** 每条 demo = 35L + 8，9 条 (8-shot + test) + instruction:

| Depth | 估算 tokens | 是否 fit 2048 |
|-------|------------|--------------|
| 1 | 9 * 43 + 15 = 402 | Yes |
| 2 | 9 * 78 + 15 = 717 | Yes |
| 3 | 9 * 113 + 15 = 1032 | Yes |
| 4 | 9 * 148 + 15 = 1347 | Yes |
| 5 | 9 * 183 + 15 = 1662 | Yes |

**CoT format** 每条 demo = 35L + 6L + 8 = 41L + 8:

| Depth | 估算 tokens | 是否 fit 2048 |
|-------|------------|--------------|
| 1 | 9 * 49 + 15 = 456 | Yes |
| 2 | 9 * 90 + 15 = 825 | Yes |
| 3 | 9 * 131 + 15 = 1194 | Yes |
| 4 | 9 * 172 + 15 = 1563 | Yes |
| 5 | 9 * 213 + 15 = 1932 | Yes (tight) |

所有配置均在 2048 token 限制内。depth 5 + CoT 最紧，实际运行时需用 tokenizer 验证。

### 2.5 随机种子与可复现性

- 每个 (depth, sample_index) 使用确定性种子：`seed = depth * 100000 + sample_index`
- 8-shot demonstrations 使用同一种子序列，保证所有模型看到相同 prompt
- 函数采样：`numpy.random.RandomState(seed)` 生成 f_l(i) for each i in [0,9]

---

## 3. 评估 Pipeline 选择

### 3.1 lm-eval-harness custom task

**Pros**:
- 标准化框架，结果可比
- 内置 batch inference、logging
- 支持多种模型后端

**Cons**:
- Custom task 需要写 YAML config + Python filter
- Prompt format 灵活性受限（特别是动态生成 few-shot examples）
- 对 randomly-generated lookup tables 的支持不自然（lm-eval 期望静态 dataset）
- Debug 困难：prompt 拼接逻辑不透明

### 3.2 独立脚本

**Pros**:
- 完全控制 prompt 构造、batch size、生成参数
- 动态生成 task instances（随机函数 + 固定种子）
- 易于添加 CoT vs Direct 变体
- 调试和验证方便（可以 print prompt 检查）
- 结果输出格式灵活

**Cons**:
- 需要自己处理 model loading、tokenization、batched generation
- 没有 lm-eval 的标准化对比基线

### 3.3 推荐：独立脚本

理由：
1. **动态 task generation** 是核心需求。每个 prompt 包含随机生成的 lookup tables，不适合 lm-eval 的静态 dataset 模式
2. **80 个评估点**（16 模型 x 5 depths）需要灵活的 batch size 控制。340M 模型推理快，可以用大 batch (64-128)
3. **Prompt format 精确控制**关键。Direct vs CoT、不同 depth 的 instruction 差异，在独立脚本中更直接
4. **可以先生成固定 dataset（JSON），再跑 inference**。这样既保证可复现性，又保持灵活性

如果后续需要与社区 benchmark 对比，可以额外包一层 lm-eval adapter，但主实验用独立脚本。

---

## 4. 实验参数建议

| 参数 | 值 | 理由 |
|------|---|------|
| num_samples per (model, depth) | 500 | 10 类答案，500 样本给出 ±2% 置信区间 |
| num_shots | 8 | 足够示范 pattern，不超 token limit |
| alphabet_size | 10 | 单 token 编码，足够的 composition 难度 |
| depths | [1, 2, 3, 4, 5] | 覆盖 Ye et al. 的层级预测 |
| batch_size | 64 | 340M 模型，单 A6000 可承受 |
| variants | [direct, cot] | Direct 对齐理论，CoT 作为对比 |
| max_new_tokens | 1 (direct) / 4L (cot) | Direct 只生成答案，CoT 生成中间步骤 |
| temperature | 0.0 (greedy) | 确定性评估 |
