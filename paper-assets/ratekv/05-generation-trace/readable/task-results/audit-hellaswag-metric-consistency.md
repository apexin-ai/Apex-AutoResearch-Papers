# audit hellaswag metric consistency

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_hellaswag_metric_consistency_20260515T215529_result.json`
- **Structured JSON:** [`3e04fd236ee0826c2afc.json`](../../sessions/3e/3e04fd236ee0826c2afc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Here's the full audit.

---

## Hellaswag Metric 一致性核查结果

### 1. 脚本 metric 提取逻辑

| 脚本 | 提取逻辑 | 实际取的 metric |
|------|---------|----------------|
| `run_qwen_3seed_downstream_ci.py` | `"acc,none" if "acc,none" in task_result else "acc_norm,none"` | `acc,none` |
| `run_llama_3seed_downstream_ci.py` | 同上 | `acc,none` |
| `run_w3_downstream_eval.py` | 同上 | `acc,none` |
| `run_w3_downstream_v2.py` | 同上 | `acc,none` |
| `run_llama_downstream_eval.py` | 同上 | `acc,none` |
| `run_yi_mistral_downstream_k2.py` | 同上 | `acc,none` |
| `run_gemma2_downstream_k2.py` | 同上 | `acc,none` |
| `run_gemma2_downstream_k8.py` | 同上 | `acc,none` |
| `run_downstream_eval.py` | 同时保存 `acc` 和 `acc_norm` | 两者都有 |

lm_eval 对 hellaswag 始终输出 `acc,none`，所以 fallback 到 `acc_norm,none` 永远不会触发。**所有 8 个脚本一致取 `acc,none`。**

### 2. 所有 artifact 中的 hellaswag 值

| Artifact 文件 | baseline | uniform | mckp | Δ(mckp-uniform) |
|--------------|----------|---------|------|-----------------|
| `qwen_3seed_downstream_ci` | 0.5887 | 0.5335 | 0.5748 (3-seed mean) | **+4.1** |
| `yi_downstream_k2` | 0.5912 | 0.5855 | 0.5818 | **-0.4** |
| `llama_downstream_eval` | 0.6073 | 0.6024 | 0.6021 | **+0.0** |
| `mistral_downstream_k2` | 0.6118 | 0.6051 | 0.6050 | **+0.0** |
| `gemma2_downstream_k8_4task` | 0.6093 | 0.6092 | 0.6089 | **+0.0** |
| `w3_downstream_yi` | 0.5913 | 0.5857 | 0.5797 | -0.6 |
| `w3_downstream_llama` | 0.6073 | 0.6026 | 0.6012 | -0.1 |
| `w3_downstream_mistral` | 0.6118 | 0.6051 | 0.6027 | -0.2 |
| `w3_downstream_gemma2` | 0.6093 | 0.6060 | 0.6089 | +0.3 |

所有值在 **0.53–0.61** 范围 = `acc,none`。没有出现 0.72–0.78 的 `acc_norm` 值。

### 3. 纸面验证

论文 Table 4 报告的是**差值**（MCKP - Uniform, pts），与 artifact 完全吻合：

| Model | 论文 HS Δ | 计算验证 | 一致？ |
|-------|----------|---------|--------|
| Qwen2.5-7B | +4.1±0.2 | (0.5748-0.5335)×100 = +4.13 | ✓ |
| Yi-1.5-9B | -0.4 | (0.5818-0.5855)×100 = -0.37 | ✓ |
| Llama-3.1-8B | +0.0 | (0.6021-0.6024)×100 = -0.03 | ✓ |
| Mistral-7B | +0.0 | (0.6050-0.6051)×100 = -0.01 | ✓ |
| Gemma-2-9B | +0.0 | (0.6089-0.6092)×100 = -0.03 | ✓ |

### 4. 关于 downstream_eval_results.json（疑似 0.7684 来源）

这是旧的 Qwen-only 实验，同时保存了两种 metric：
- hellaswag `acc` = 0.5733 / `acc_norm` = **0.7684**

**0.7684 就是 `acc_norm,none`，但这个文件未被论文 Table 4 使用。** 论文的 Qwen 行来自 `qwen_3seed_downstream_ci_results.json`（3-seed），该文件只存了 `acc,none`。

### 5. 结论

**不存在混用。** Table 4 所有模型一致使用 `acc,none`（raw accuracy）。

但有一个**报告惯例**问题值得注意：HellaSwag 的标准报告指标是 `acc_norm`（如 Open LLM Leaderboard），不是 `acc`。我们报的 ~0.59 如果被 reviewer 拿去和 model card 上的 ~0.78 对比，会觉得数字偏低。不过由于 Table 4 只报差值不报绝对值，这个问题在当前论文中不会暴露。**无需修正。**

---
