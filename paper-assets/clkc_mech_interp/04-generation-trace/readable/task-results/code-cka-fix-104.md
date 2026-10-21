# code cka fix 104

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cka-fix-104_20260522T080733_result.json`
- **Structured JSON:** [`7a3bf0d65107cefa6370.json`](../../sessions/7a/7a3bf0d65107cefa6370.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 结果汇报

### 1. Conflict aligned vs XNLI aligned（公平对比 1：都是 index-paired 平行语料）

| 模型 | Conflict aligned CKA | XNLI aligned CKA | Diff |
|------|---------------------|-------------------|------|
| **Qwen3** | mean=**0.652**, range=[0.32, 0.86] | mean=**0.094**, range=[0.02, 0.15] | **+0.558** |
| **Llama31** | mean=**0.778**, range=[0.52, 0.91] | mean=**0.151**, range=[0.08, 0.24] | **+0.627** |

差异巨大。同一内容的 EN/ZH 对，conflict 的 CKA 远高于 XNLI。

### 2. Conflict shuffled vs XNLI shuffled（公平对比 2：都是随机配对，打破内容对齐）

| 模型 | Conflict shuffled CKA | XNLI shuffled CKA | Diff |
|------|----------------------|-------------------|------|
| **Qwen3** | mean=**0.124** | mean=**0.096** | **+0.028** |
| **Llama31** | mean=**0.080** | mean=**0.165** | **-0.085** |

差异接近零甚至**反转**（Llama31 上 XNLI shuffled > conflict shuffled）。

### 3. 控制配对后差异是否仍存在？

**Aligned 模式下差异巨大（0.56-0.63），shuffled 模式下差异消失或反转。** 这说明：

- conflict 的高 CKA 完全来自 **index-pairing**（同一问题的 EN/ZH 版本）
- 一旦打破配对，conflict 和 XNLI 的 CKA 处于同一水平
- 有趣的是 XNLI aligned ≈ XNLI shuffled（~0.09-0.16），说明模型对 NLI 前提的 EN/ZH 表示本就不相似，即使是同一 premise 的翻译

### 4. 结论：CKA 证据是否支持 C3？

**不直接支持 C3 的 "conflict-specific" 叙事。** 

aligned 模式的巨大差异（conflict >> XNLI）是真实的，但反映的是**任务/内容类型效应**：短事实性问题在 EN/ZH 中获得高度相似的表示，而 NLI 前提即使是平行翻译也不相似。这是 factual question 的共性，不是 knowledge conflict 的特性。

要证明 C3，需要一个**无冲突的事实性问题对照组**——如果非冲突事实问题的 aligned CKA 同样高，则 CKA 差异不是 conflict 特有的。

---
