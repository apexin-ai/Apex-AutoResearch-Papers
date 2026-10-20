# code ds dense baseline and c2 artifacts

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ds_dense_baseline_and_c2_artifacts_20260515T204039_result.json`
- **Structured JSON:** [`41e345f0bc86bd01561c.json`](../../sessions/41/41e345f0bc86bd01561c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 注册成功。下面是完整的汇总分析结果，可直接转发给 Director：

---

## C2 Accuracy Evaluation — MATH-500 (n=50)

### Summary Table

| Condition | n | Dense Acc | Sparse Acc | Delta | null_rate | trunc_rate | wrong_rate |
|-----------|---|-----------|------------|-------|-----------|------------|------------|
| **DS dense** | 50 | **52%** (26/50) | — | — | 46% | 56% | 2% |
| **DS s015** | 50 | 52% | **34%** (17/50) | **-18pp** | 50% | 52% | 16% |
| **DS s030** | 50 | 52% | **10%** (5/50) | **-42pp** | 64% | 66% | 26% |
| **QW dense** | 50 | **32%** (16/50) | — | — | 10% | 10% | 58% |
| **QW s015** | 50 | 32% | **32%** (16/50) | **0pp** | 10% | 8% | 58% |
| **QW s030** | 50 | 32% | **14%** (7/50) | **-18pp** | 20% | 6% | 66% |

DS spike s025 (n=10): dense=40%, sparse=10%, delta=-30pp（小样本，方向一致）

### 失败模式分析

**(a) Wrong answer** (pred≠null 但 ≠ ref):
- DS: 2% → 16% → 26%（sparsity 增加，错答率上升）
- QW: 58% → 58% → 66%（QW 本身就以错答为主要失败模式）

**(b) Truncation** (gen_length=2048 且 null):
- DS: 23/50 → 24/50 → 30/50（DS 是 thinking model，CoT 长，2048 token 预算严重不足——dense 就已经截断 56%）
- QW: 5/50 → 4/50 → 3/50（QW 生成短，截断不是问题）

**(c) Extraction failure** (gen<2048 但 null):
- 所有条件均极低（0-7），其中 QW s030 有 7 个——可能是 sparsity 导致格式退化，`\boxed{}` 缺失

### DS s030 中文推理
- **20/50 (40%)** 的 DS s030 sparse 生成包含中文
- DS s015 sparse: 2/50 (4%)
- DS dense: 0/50 (0%)
- 结论：30% sparsity 触发 DeepSeek 语言切换（中←→英），这是 DS 特有的病理现象

### 关键结论
1. **DS 对 sparsity 比 QW 敏感得多**：s030 下 DS 丢 42pp vs QW 丢 18pp
2. **失败模式不同**：DS 主要因截断失败（CoT 太长），QW 主要因答案错误
3. **QW s015 完全无损**：0pp degradation，15% compound sparsity 对 Qwen 免费
4. **DS dense 的 2048 token 预算本身就不够**：56% 截断率意味着 dense baseline 受限，真实 DS dense accuracy 可能远高于 52%
5. **语言切换**是 DS 在高 sparsity 下的独特退化信号，40% 问题受影响

---
