# analysis structural data scaling

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_structural-data-scaling_20260514T194312_result.json`
- **Structured JSON:** [`8c454543d45b26e0910c.json`](../../sessions/8c/8c454543d45b26e0910c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总结果：

| 比例 | Probe macro_f1 | RF macro_f1 | GB macro_f1 |
|------|---------------|-------------|-------------|
| 10% | 0.8054 | **0.9909** | **0.9873** |
| 25% | 0.8203 | **0.9916** | **0.9930** |
| 50% | 0.8715 | **0.9951** | **0.9951** |
| 100% | 0.9055 | 0.9951 | 0.9951 |

结论：structural RF/GB 对数据量几乎不敏感。即使只用 10% 训练数据（138 个 instance, 1107 个 window），RF macro_f1 仅从 0.9951 降至 0.9909（-0.0042），GB 降至 0.9873（-0.0078）。而 GRU probe 在同样条件下从 0.9055 降至 0.8054（-0.1001），下降幅度是 structural 的 ~20 倍。50% 处 structural 已完全饱和（与 100% 相同）。

结果已写入 `results_structural_data_scaling.json`，artifact 和 registry 已更新。

---
