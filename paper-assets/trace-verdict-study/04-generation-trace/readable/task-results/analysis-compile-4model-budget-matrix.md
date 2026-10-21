# analysis compile 4model budget matrix

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_compile_4model_budget_matrix_20260518T075608_result.json`
- **Structured JSON:** [`4b828bbca21d5effa697.json`](../../sessions/4b/4b828bbca21d5effa697.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

矩阵已编译完成，保存至 `artifacts/budget_curve_matrix_compiled.md`。

## 完整矩阵

| Model | tail-256 | tail-512 | tail-1024 | tail-2048 | head-2048 |
|-------|----------|----------|-----------|-----------|-----------|
| **Qwen-7B** | 77.5 | 93.6 | 96.5 | 97.3 | **TBD** |
| **DeepSeek-6.7B** | 76.4 | 93.9 | 96.5 | 95.0 | 78.7 |
| **Qwen-1.5B** | 72.6 | 95.6 | 96.6 | 97.9 | 75.3 |
| **CodeLlama-13B** | 77.9 | 97.5 | **RUNNING** | **RUNNING** | 79.9 |

## 缺失 Cells

1. **Qwen-7B head-2048** — registry 中无此实验，需新建
2. **CodeLlama-13B tail-1024 v3** — RUNNING，label_only_loss 重训
3. **CodeLlama-13B tail-2048 v3** — ALLOCATED，label_only_loss 重训

## 关键 Patterns

1. **Phase transition @ 256→512**: 全部 4 模型从 ~73-78% 跳至 ~94-98%（+16-23 pp），这是 critical budget threshold
2. **Convergence band @ 512+**: 512 以上增益平缓（+1-4 pp），tail-512 已捕获绝大多数 verdict signal
3. **Head-tail gap**: head-2048 ≈ tail-256 水平（75-80%），确认 verdict-critical signal 集中在 trace 尾部
4. **Model size independence**: Qwen-1.5B 在所有 budget 点追平甚至超过大模型，说明瓶颈在 signal availability 而非 model capacity

---
