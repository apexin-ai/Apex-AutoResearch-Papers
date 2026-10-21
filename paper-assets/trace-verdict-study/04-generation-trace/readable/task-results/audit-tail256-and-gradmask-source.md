# audit tail256 and gradmask source

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_tail256-and-gradmask-source_20260523T193943_result.json`
- **Structured JSON:** [`914fba4ac1cc76ba49a0.json`](../../sessions/91/914fba4ac1cc76ba49a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部找到。以下是完整调查结果：

---

## 问题 1: Qwen-7B tail-256 两表不一致

**原因：两个表引用了同一条件的两次不同训练 run。**

服务器上存在两个几乎同名的 checkpoint 目录（注意下划线差异）：

| Checkpoint 目录 | Accuracy | 来源 eval_results.json |
|---|---|---|
| `full_trace_tail_256_seed42`（有下划线） | **77.48%** (0.77479) | condition: `full_trace_tail_256` |
| `full_trace_tail256_seed42`（无下划线） | **78.91%** (0.78908) | condition: `full_trace_tail_256` |

论文中的使用：
- **tab:trace_length** (appendix.tex L380): 使用 **77.48%** ← 来自 `full_trace_tail_256_seed42`
- **tab:tail_cross_model** (appendix.tex L466): 使用 **78.9%** ← 来自 `full_trace_tail256_seed42`

Registry 只收录了 `full_trace_tail_256_seed42` = 0.7748。

**结论：这是同一实验条件的两次独立 run，产生了 1.43pp 的差异。论文中两个表各取了不同 run 的值，造成数据不一致。** 需要选定一个 canonical run，两个表统一使用。

另外还有第三个实验 `full_trace_256tok`（78.82%），这是 **head 截断**（condition: `full_trace`），对应 tab:trace_length 中 Head 256 = 78.82%，这个没问题。

---

## 问题 2: Gradient masking seed42

**实际 eval_results.json 原始值：**

| Seed | 文件路径 | Accuracy |
|---|---|---|
| 42 | `gradient_masking_qwen7b_seed42/final/eval_results.json` | **98.99%** (0.98992) |
| 123 | `gradient_masking_qwen7b_seed123/final/eval_results.json` | **99.33%** (0.99328) |
| 456 | `gradient_masking_qwen7b_seed456/final/eval_results.json` | **99.33%** (0.99328) |

**Registry 记录的值：** seed42 = **0.9933 (99.33%)** — **错误**。Registry 注释写着 `"NOTE: metrics empty (None conclusion) — see seed123/456 for canonical"`，说明 seed42 的 registry entry 被错误地用 seed123/456 的值填充。

**论文 Table 3 (tab:density)：** 只报了 3-seed mean **99.22% ± 0.20%**，**不包含** 个别 seed 的值。`98.99%` 这个数字没有出现在论文 .tex 文件中。

**验证计算：**
- 正确 mean = (98.99 + 99.33 + 99.33) / 3 = **99.22%** ✓ — 论文的 mean 是对的
- 正确 std = 0.20% ✓ — 也是对的
- Registry 用的错误 mean = 99.33%（因为三个 seed 都被记成了 99.33%）

**结论：eval_results.json 确认 seed42 = 98.99%，论文的 mean 值 99.22% 正确（因为是从原始 eval 文件算的），registry 被错误覆写。** 如果论文中有其他位置引用了 seed42 的单独值为 99.33%，那是错误的，应为 98.99%。

---
