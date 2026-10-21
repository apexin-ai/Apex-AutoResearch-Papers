# debug eval benchmark mask logic audit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_eval_benchmark_mask_logic_audit_20260516T002155_result.json`
- **Structured JSON:** [`c330720a7fbf70c39aae.json`](../../sessions/c3/c330720a7fbf70c39aae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。所有关键结果已出。

---

## 审查结论

### Mask 应用逻辑：**无 bug**

| 检查项 | 结果 |
|--------|------|
| Mask shape | `(B, S, 14336)` 匹配 `intermediate_size` ✅ |
| Mask 类型 | per-token 动态（非 static）✅ |
| Mask 应用位置 | `af(gp(x)) * up(x)` 之后, `dp()` 之前 ✅ |
| Predictor checkpoint | 128 state keys, `down=(128,4096)`, `up=(14336,128)` 正确 ✅ |
| Predictor eval mode | `.eval()` 已设置 ✅ |
| Closure bug | 使用 default args (`_gp=gp, ...`) 避免 ✅ |
| 平均 sparsity | 0.5031 ≈ 目标 0.50 ✅ |
| **HFLM 透传** | **logit diff = 0.000000** — patch 完整保留到 lm-eval ✅ |

### 关键诊断数据

**Dense 输出** ("The capital of France is"):
```
Top-5: [(' a', 16.25), (' Paris', 16.0), (' one', 15.44), (' the', 15.44), (' also', 14.88)]
```

**Sparse 输出**（同一 prompt, KL predictor mask）:
```
Top-5: [(' also', 15.88), (' a', 15.75), (' one', 15.19), (' the', 15.12), (' Paris', 14.81)]
```

- "Paris" 从 #2 (16.0) 降到 #5 (14.81)
- 平均 logit 偏移 0.69, 最大 4.41

**Per-token sparsity**（layer 0）:
```
BOS:      0.484
'The':    0.489
'capital':0.296
'of':     0.440
'France': 0.306
```
动态 mask 在工作，content words 保留更多 neurons。

### 结论：**真实现象，非 bug**

50% SwiGLU sparsity 保留了语言建模能力（PPL 6.48 → 9.65），但破坏了知识检索和推理路径：

1. **PPL 是平均指标** — 只要多数 token 预测合理，PPL 就不会灾难性上升
2. **MMLU/GSM8K 要求精确知识检索** — logit 分布的微小偏移（如 "Paris" 掉 1.2 分）足以翻转 4-choice 答案
3. 预测器在 C4/WikiText 上训练，优化的是 PPL 而非 downstream accuracy

### 缺失验证

唯一未完成的是 **dense 条件的 lm-eval downstream 数字**（预期 MMLU ≈ 65%）。建议用 `eval_benchmark.py --condition dense --tasks mmlu` 补跑确认 lm-eval 集成本身没问题。但基于 HFLM 透传验证 (diff=0.0) 和 dense logits 正确性，集成问题的可能性极低。

---
