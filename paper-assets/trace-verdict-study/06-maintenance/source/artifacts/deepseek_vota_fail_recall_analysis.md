# DeepSeek VOTA fail_recall 异常低原因分析

## 核心数据对比

| 指标 | DeepSeek VOTA | Qwen VOTA |
|------|--------------|-----------|
| accuracy | 84.45% | 99.16% |
| pass_recall | 1.000 | 0.988 |
| fail_recall | **0.454** | **1.000** |
| pass_precision | 0.821 | 1.000 |
| fail_precision | 1.000 | 0.971 |
| train_loss (avg) | 0.0594 | 0.0500 |
| eval_loss @epoch2 | 0.0950 | 0.0795 |
| eval_loss @epoch3 | 0.1121 (+18%) | 0.0867 (+9%) |
| eval_token_acc @epoch3 | 0.9791 | 0.9828 |

数据分布: test 集 71.5% pass / 28.5% fail, majority baseline = 71.5%。

## 预测模式

fail_precision=1.0 + fail_recall=0.454 + pass_recall=1.0 构成一个清晰的模式：**模型默认预测 "pass"，只在极度确信时才预测 "fail"**。54.6% 的实际 fail 样本被保守地归为 pass。这不是随机错误，而是系统性的 pass 偏向。

## 原因分析

### 1. 不是 tokenizer 问题

| 文本 | DeepSeek tokens | Qwen tokens |
|------|----------------|-------------|
| "pass" | [4805] (1 token) | [6385] (1 token) |
| "fail" | [16156] (1 token) | [18403] (1 token) |
| "Verdict: pass" | [8618, 13057, 25, 1445] | [10141, 8477, 25, 1494] |
| "Verdict: fail" | [8618, 13057, 25, 4564] | [10141, 8477, 25, 3690] |

两者结构一致，verdict 仅最后一个 token 不同。**tokenizer 不是原因。**

### 2. 不是 label 分布问题

train 集 pass:fail ≈ 66:34，不算极端不平衡。Qwen 在同样分布上学到了 fail_recall=1.0。**数据分布不是根因。**

### 3. 存在 overfitting 迹象

DeepSeek 的 eval_loss 从 epoch 2 到 epoch 3 上升了 18%（0.095→0.112），同时 train loss 仅 ~0.02。train-eval gap 远大于 Qwen（Qwen eval_loss 仅上升 9%）。这表明 DeepSeek 在 epoch 3 已经 overfit，但 overfit 方向是"记住 trace 格式"而非"学会区分 verdict"。

注意两者都用了 `label_only=False`（全序列 loss），verdict token 在整个序列中占比极低。训练 token accuracy 0.993 主要由 trace 复现能力贡献，不代表 verdict 判别能力。

### 4. 根本原因：DeepSeek 模型能力差异

最可能的解释是 **DeepSeek-Coder-6.7B-Instruct 的指令跟随和推理能力弱于 Qwen2.5-Coder-7B-Instruct**：

- DeepSeek-Coder-6.7B 是较老的模型（2023），Qwen2.5-Coder-7B 是 2024 年底的模型，架构和训练数据更新
- DeepSeek 的 pretrained weights 可能对代码执行 trace 的理解不如 Qwen，导致无法从 VOTA trace 中提取 fail 信号
- 在 LoRA 微调的有限容量下，DeepSeek 把参数花在了拟合 trace 格式上，没有足够余力学习 verdict 判别
- 模型的 prior 偏向 "pass"（代码通常是正确的），微调未能充分纠正这个 prior

## 结论

这是 **DeepSeek 模型能力不足** 导致的，不是数据或训练配置问题。模型在给定 VOTA trace 的情况下，无法有效学习 fail 的判别特征。

## 如何解读即将到来的 deepseek_no_trace 结果

| deepseek_no_trace 结果 | 解读 |
|------------------------|------|
| fail_recall 同样很低（~0.45） | 确认是 DeepSeek 模型能力问题，不管有无 trace 都偏向 pass |
| fail_recall 比 vota 更高（>0.6） | VOTA trace 对 DeepSeek 是**负干扰**——trace 信息过多淹没了 verdict 信号，反而不如简单判别 |
| fail_recall 比 vota 更低（<0.3） | trace 至少提供了部分帮助，但不够；无 trace 时 DeepSeek 几乎完全猜 pass |

**最关键的对比是 deepseek_no_trace vs deepseek_vota**——它能区分 "DeepSeek 能力差" 和 "VOTA trace 干扰 DeepSeek"。
