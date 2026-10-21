# analysis r12 task2 wikievents bootstrap

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r12_task2_wikievents_bootstrap_20260520T174558_result.json`
- **Structured JSON:** [`12e835ff748e1d400912.json`](../../sessions/12/12e835ff748e1d400912.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bootstrap CI 完成。结果保存在 `westd-16980:/root/autodl-tmp/schema_outputs/r12_wikievents_bootstrap.json`。

汇总（point estimate [95% CI]）：

| Model | Mode | T-F1 | A-F1 | RoV | AC |
|-------|------|------|------|-----|-----|
| **Qwen FT** | unc | 0.3208 [0.253, 0.372] | 0.0785 [0.049, 0.113] | 0.3831 [0.254, 0.467] | 0.0345 [0.016, 0.074] |
| **Qwen FT** | con | 0.2672 [0.211, 0.328] | 0.0818 [0.059, 0.111] | 0.0 [0, 0] | 0.0 [0, 0] |
| **Llama FT** | unc | 0.2752 [0.230, 0.323] | 0.0998 [0.066, 0.125] | 0.1107 [0.038, 0.182] | 0.0503 [0.017, 0.073] |
| **Llama FT** | con | 0.2691 [0.209, 0.326] | 0.0891 [0.059, 0.122] | 0.0 [0, 0] | 0.0078 [0, 0.017] |

关键观察：
- 20 docs 的 CI 宽度约 ±0.05-0.06 (T-F1)，符合预期的小样本不确定性
- Constrained 的 RoV 全部为 0（CI 也为 0），验证了约束解码完全消除了 role vocabulary violations
- T-F1/A-F1 的 unc vs con CI 高度重叠，说明 F1 差异在统计上不显著

脚本位于两个服务器的 `scripts/bootstrap_wikievents_ci.py`，文件来源：Qwen FT 在 westd-21461，Llama FT 在 westd-16980。

---
