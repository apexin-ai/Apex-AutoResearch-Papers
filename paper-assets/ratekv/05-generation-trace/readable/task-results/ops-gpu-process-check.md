# ops gpu process check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_process_check_20260516T033355_result.json`
- **Structured JSON:** [`66366c28b1fa2be2cf62.json`](../../sessions/66/66366c28b1fa2be2cf62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报如下：

---

## GPU 状态

| GPU | 状态 | 进程 |
|-----|------|------|
| cuda:0 (RTX PRO 6000 Black, 98GB) | **空闲** | 无 |
| cuda:1 (RTX PRO 6000 Black, 98GB) | **空闲** | 无 |

唯一活跃 Python 进程：PID 393106 正在 CPU 上下载 Qwen2.5-32B（modelscope），不占 GPU。

## 实验状态

| 实验 | 状态 | 结论 | 关键指标 |
|------|------|------|----------|
| **codellama_constrained_mckp** | DONE ✅ | negative | MCKP 9.014 vs Uniform 9.035 (Δ=+0.02, Spike 无收益，符合预期) |
| **mistral_8k_eval** | DONE ✅ | negative | MCKP 4.921 vs Uniform 4.917 (Δ=-0.004, Flat 8K 无收益，符合预期) |
| **internlm2_constrained_mckp_v2** | DONE ✅ (已在 registry) | success | MCKP 9.901 vs Uniform 9.919 (Δ=-0.018, Flat 边界) |

注意：InternLM2 v2 的 `_v2_results.json` 不存在，结果写入了 `internlm2_constrained_mckp_results.json`（旧文件名），但 registry 已正确记录。

**两块 GPU 当前完全空闲，可调度新任务。**

---
