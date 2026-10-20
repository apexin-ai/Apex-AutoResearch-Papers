# eval cuda0 sanity and deepseek reeval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cuda0_sanity_and_deepseek_reeval_20260515T180312_result.json`
- **Structured JSON:** [`cbb583af0a12e81f6b01.json`](../../sessions/cb/cbb583af0a12e81f6b01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果已收集。汇总如下：

---

## Sanity Check — 两项均通过 (偏差 = 0)

| Condition | 期望 | 实际 | 状态 |
|-----------|------|------|------|
| VOTA (Qwen) | 99.41% | 99.41% | **PASS** |
| full_trace (Qwen) | 81.76% | 81.76% | **PASS** |

evaluate.py 的 truncation 修复已验证正确。

---

## DeepSeek full_trace 重评结果（修复后）

| Metric | 值 |
|--------|-----|
| **Accuracy** | **10.59%** (95% CI: [8.9%, 12.3%]) |
| Majority baseline | 71.5% (always "pass") |
| **Lift vs majority** | **-60.9pp** |
| pass P / R / F1 | 0.00 / 0.00 / 0.00 |
| fail P / R / F1 | 0.37 / 0.37 / 0.37 |

### 与旧评估对比

| 版本 | Accuracy | Lift | fail R |
|------|----------|------|--------|
| 旧 (无截断) | 28.49% | -43.0pp | 1.00 |
| **新 (截断修复)** | **10.59%** | **-60.9pp** | **0.37** |

修复截断后结果**更差了**：旧评估中模型至少一致地预测 "fail"（fail recall=1.0），现在模型输出大量垃圾 token：

| raw_pred | 数量 |
|----------|------|
| `fail` | 338 |
| `{` | 276 |
| `execution` | 125 |
| `{}` | 121 |
| `assert` | 120 |
| `import` | 73 |
| `this` | 37 |

模型**从未输出 "pass"**。

### vs DeepSeek no_trace baseline

| Condition | Accuracy | Lift |
|-----------|----------|------|
| deepseek_no_trace | 73.36% | +1.8pp |
| **deepseek_full_trace (fixed)** | **10.59%** | **-60.9pp** |

**结论：DeepSeek full_trace LoRA 本身是坏的**，不是 evaluate.py 的问题。截断修复反而暴露了更严重的问题——当输入被正确截断到 2048 tokens（保留 chat template 结构），模型产生大量无关 token 而非分类标签。训练可能失败或未收敛。建议检查 DeepSeek full_trace 的训练日志和 checkpoint。

---
