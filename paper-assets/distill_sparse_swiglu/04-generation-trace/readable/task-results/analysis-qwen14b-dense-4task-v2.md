# analysis qwen14b dense 4task v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_dense_4task_v2_20260519T181935_result.json`
- **Structured JSON:** [`5b200f50dca64752535f.json`](../../sessions/5b/5b200f50dca64752535f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 结果文件完整，所有数据已拿到。

## 结果汇总

| 指标 | v2 结果 | baseline 参考值 | 差异 |
|------|---------|----------------|------|
| wikitext2 PPL | **5.1854** | 5.1854 | 0 (完全一致) |
| arc_challenge acc | **0.6493** | — | — |
| arc_challenge acc_norm | **0.6758** | 0.6758 | 0 (完全一致) |
| winogrande acc | **0.8106** | 0.8106 | 0 (完全一致) |
| mmlu acc | **0.7977** | 0.7977 | 0 (完全一致) |

### 完整精度数值
- arc_challenge: acc=0.6493 (±0.0139), acc_norm=0.6758 (±0.0137)
- winogrande: acc=0.8106 (±0.0110)
- mmlu: acc=0.7977 (±0.0032)

### 异常检查
- EXIT_CODE=0，正常退出
- 无 OOM/CUDA error
- 所有 4 个任务均完整评估（sample counts: arc=1172, winogrande=1267, mmlu=14042）
- 有一条 `fatal: not a git repository` 的无害警告（lm-eval-harness 试图读 git info）
- 使用了离线缓存的 MMLU 数据集（HF Hub offline mode），数据一致性无问题

### 与 baseline 对比
所有 4 个指标与 `qwen14b_dense_baseline` **完全一致**（精确到小数点后 4 位），符合预期——同一模型的 dense eval 是确定性的。

### 结论：**Success**
v2 成功复现了 v1 未能完成的 dense baseline 4-task 评估，所有指标与独立 baseline run 完全吻合。这组数据可以作为论文中 Qwen-14B dense baseline 的权威参考值。

---
