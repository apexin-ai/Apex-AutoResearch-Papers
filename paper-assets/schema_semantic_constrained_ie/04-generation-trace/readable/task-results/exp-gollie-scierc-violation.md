# exp gollie scierc violation

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gollie-scierc-violation_20260523T051232_result.json`
- **Structured JSON:** [`43f7daedd26eddba9f47.json`](../../sessions/43/43f7daedd26eddba9f47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已注册。以下是完整对比结果：

## GoLLIE vs OntoCoDec — SciERC Violation Rate 对比

### Doc-level 评估（100 docs）

| Method | DR% | RV% | ET% | CF% | E-F1 | R-F1 | #Pred Ent | #Pred Rel |
|---|---|---|---|---|---|---|---|---|
| **GoLLIE-7B (ZS)** | 0 | 0 | 0 | 0.83 | 9.17 | 0.0 | 241 | 5 |
| OntoCoDec Qwen ZS unc | — | — | 0.43 | 2.95 | 31.39 | 8.25 | 2342 | 1721 |
| OntoCoDec Qwen ZS S1 | — | — | 0 | 2.95 | 31.45 | 8.38 | 2342 | 1726 |
| **OntoCoDec Qwen FT S1** | 0 | 0 | 0 | 0.61 | 66.43 | 43.69 | 1639 | 1121 |
| **OntoCoDec Llama FT S1** | 0 | 0 | 0 | 0.62 | 67.09 | 45.47 | 1605 | 1070 |

### 关键发现

1. **GoLLIE 的低 violation rate 是 trivial 的**：只有 54/100 docs 产生了输出，仅预测 241 个 entity（gold 1525）和 5 个 relation（gold 971）。几乎不输出自然不会犯错。

2. **OntoCoDec FT+S1 的 violation rate 更低且有意义**：CF 仅 0.61-0.62%（低于 GoLLIE 的 0.83%），同时 E-F1 高 7x（67 vs 9），R-F1 从 0 提升到 43-45。

3. **对 R1 D4 的回应要点**：GoLLIE 通过 code-style schema 约束确实能避免 ET/RV 类 violation，但代价是极低的 recall。OntoCoDec 的约束解码在保持高 F1 的同时实现了同等甚至更低的 violation rate，证明了 decode-time 约束的有效性。

---
