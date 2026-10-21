# debug kl downstream disconnect

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_kl_downstream_disconnect_20260516T000033_result.json`
- **Structured JSON:** [`6fc9009e3c9e0c4e7d2a.json`](../../sessions/6f/6fc9009e3c9e0c4e7d2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已经有足够证据了。以下是完整诊断报告。

---

## 诊断结果

### 根因：不是 mask 应用 bug，是 **token-level bias 放大** + **MMLU 评估格式敏感**

### 证据链

**1. Mask 应用正确**
- 诊断脚本验证：mask 在所有 32 层生效，平均 sparsity 51.5%，范围 [30%, 68%]
- Dense/sparse logits 差异 1.34（mask 确实在工作）
- `patch_predictor` 和 `unpatch_model` 逻辑均无 bug

**2. Sparse 模型保留了 significant 语言理解能力**
- 手动 QA（完整答案文本 "Paris"/"London" 等）：**90%** (18/20)
- PPL 9.2（vs dense 6.1）：合理的 50% sparsity 退化

**3. 关键发现：HFLM loglikelihood 直接测试**

Dense:
```
Q0: logprobs=[A:-6.06, B:-2.42, C:-6.47, D:-7.50] → B (Au) ✓
```
Sparse（始终选 "A"）:
```
Q0: logprobs=[A:-2.80, B:-4.75, C:-4.19, D:-3.61] → A ✗
Q1: logprobs=[A:-2.81, B:-5.38, C:-3.31, D:-2.81] → A ✗
Q2: logprobs=[A:-2.47, B:-4.91, C:-4.09, D:-3.72] → A ✗
Q3: logprobs=[A:-2.92, B:-5.16, C:-4.84, D:-4.28] → A ✗
Q4: logprobs=[A:-2.56, B:-4.50, C:-4.44, D:-3.88] → A ✗
```

**Sparse 模型在 "Answer:" 后的单字母 token 上有系统性偏差：** "A" logprob ~-2.7 始终最高，与问题内容无关。Dense 模型没有此问题。

**4. 评估指标差异导致表象差异**

| Task | Metric | 为何受影响 |
|------|--------|-----------|
| MMLU 25.9% | `acc` (raw) | 单字母 A/B/C/D 选择，"A" bias 主导 → 随机 |
| ARC-c 37.7% | `acc_norm` | 归一化消除 unconditional bias → 反映真实退化 |
| WinoGrande 61.6% | `acc` | 完整句子续写，非字母选择 → bias 不适用 |
| GSM8K 1.2% | `exact_match` | 生成任务，sparsity 严重降低推理能力 |

### PPL-Downstream Disconnect 解释

- PPL 衡量所有 token 的平均预测质量，分散在数十万个 token 上，单字母 bias 影响极小
- MMLU 的评估完全依赖 A/B/C/D 这 4 个 token 的 logprob 排序，bias 效应被放大到 100%
- 这是 **真实的 PPL-downstream disconnect**，但大部分由评估格式造成，不是模型完全失能

### 根因判断

**(A) + (C) 混合**：
- 不是 eval_benchmark.py 的 code bug（mask 正确应用）
- 50% dynamic sparsity 削弱了模型在"Answer:"上下文中对单字母 token 的区分能力
- MMLU 的 `acc` 指标 + 字母选择格式将此缺陷放大为 ~random

### 修复方案

**快速修复（评估侧）**：

`eval_benchmark.py` 第 325 行，MMLU 改用 `acc_norm`：

```python
def _primary_metric(task_name):
    return {
        "arc_challenge": "acc_norm,none",
        "winogrande": "acc,none",
        "mmlu": "acc_norm,none",   # ← 修改此行
        "gsm8k": "exact_match,strict-match",
    }.get(task_name, "acc,none")
```

但 MMLU task config 只有 `acc`，没有 `acc_norm`。需要自定义 task config 或改用 `mmlu_pro`/`mmlu_generative` 变体。

**更好的修复方案**：

1. **重跑 MMLU 同时报告 `acc` 和 `acc_norm`** — 需要修改 MMLU task yaml 添加 `acc_norm` metric
2. **对比 TEAL 静态 mask vs 动态 predictor mask** — PID 179918 正在运行 TEAL 版本，结果即将出来。静态 mask 可能因为全局 sparsity 约束不会有同样严重的 token bias
3. **长期方案**：如果 dynamic predictor 在评估中持续展现此 bias，考虑训练时加入 token-discrimination 正则化

### PID 179918 状态

正在运行（已 29 分钟），`lm_eval_sparse.py` 用 TEAL 静态 mask + lm-eval，结果目录尚未创建。建议等待完成后对比。

---
