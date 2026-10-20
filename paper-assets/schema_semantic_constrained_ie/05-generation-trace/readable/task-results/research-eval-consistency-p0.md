# research eval consistency p0

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_eval_consistency_p0_20260520T011114_result.json`
- **Structured JSON:** [`8aaf18ce298fa4456fbf.json`](../../sessions/8a/8aaf18ce298fa4456fbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/_project/report/eval_consistency_investigation.md`。

核心发现：

**两个根因叠加导致差异：**

1. **不同 JSONL 文件**：w5 原始运行（25 parse failures）vs d064 重跑（50 parse failures），同一 checkpoint 但不同代码版本导致推理输出不同

2. **不同 F1 计算方法**：Table 2 的 registry 数据 **跳过 parse failures 不计入 FN**（E-F1=85.23），eval_d064.py **计入 FN**（E-F1=83.94 on same file）

**更严重的问题**：Table 2 对 Qwen 和 Llama 使用了不同的 parse failure 处理——Qwen E_F1=81.43（含 parse failures），Llama E_F1=85.23（排除 parse failures）——模型间比较不公平。

**建议**：用 eval_d064.py（parse failures 计入 FN）统一重新评估所有 w5 文件，更新 Table 2。

---
