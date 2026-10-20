# experiment mismatch inference

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_mismatch-inference_20260524T231829_result.json`
- **Structured JSON:** [`33c30aae136bd612d3f8.json`](../../sessions/33/33c30aae136bd612d3f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都完成。结果如下：

## 错配实验结果

| 训练条件 | 推理条件 | Accuracy | 95% CI | 对比 baseline |
|----------|----------|----------|--------|--------------|
| exception_only | exception_only | **99.83%** | [99.6%, 100%] | baseline |
| exception_only | **full_trace** | **53.6%** | [50.8%, 56.7%] | Exp A: **-46.2pp** |
| full_trace (head2048) | full_trace_head | **81.0%** | [78.7%, 83.3%] | baseline |
| full_trace (head2048) | **exception_only** | **30.9%** | [28.4%, 33.5%] | Exp B: **-50.1pp** |

### Per-class 分析

| 实验 | Pass P/R/F1 | Fail P/R/F1 |
|------|------------|------------|
| Exp A (exc→full) | 0.84/0.43/0.57 | 0.36/0.80/0.49 |
| Exp B (full→exc) | 0.63/0.08/0.14 | 0.28/0.88/0.42 |

### 关键发现

1. **两个方向都大幅崩溃**，确认 reviewer 指出的 forward-pass confound 存在
2. **两个模型在错配时都严重偏向预测 "fail"**（Exp A fail recall=80%, Exp B fail recall=88%），说明模型看到不熟悉的输入格式就倾向判 fail
3. **full_trace→exception_only (30.9%) 比 exception_only→full_trace (53.6%) 崩得更狠**，full_trace 模型对输入格式的依赖更强
4. 截断验证：full_trace 样本全部 ≤ 2016 tokens，均未超过 2048 上限，左截断设置未实际生效（无需截断）
5. exception_only 样本中位数 150 tokens，同样无需截断

### 对 Reviewer 回复的意义

这个结果**证实了 confound 的存在**，但也可以从另一个角度解读：模型确实学到了特定于输入格式的特征，而非通用的 bug 检测能力。这本身就是论文的核心发现之一——trace 的信息密度差异不仅影响准确率，还影响模型的泛化模式。

---
