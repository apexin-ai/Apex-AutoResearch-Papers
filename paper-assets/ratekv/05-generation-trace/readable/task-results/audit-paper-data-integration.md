# audit paper data integration

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper_data_integration_20260516T023911_result.json`
- **Structured JSON:** [`115775fa6491af91ae1d.json`](../../sessions/11/115775fa6491af91ae1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。总结：

**3/5 项已集成，2 项缺失：**

| 项目 | 状态 |
|------|------|
| Compounding curves (Fig 2) — 3 曲线 + 最新 sweep 数据 | ✅ |
| §3.3 compounding 讨论 — 引用和数值匹配 | ✅ |
| Qwen 3-seed downstream CI — ±1σ error bars | ✅ |
| **Llama 3-seed downstream CI** — `experiments.tex:123` 无 ±std | ❌ |
| **Phi-3-medium-14B Table 1** — 无占位行 | ❌ |

两个缺失项的修复点：
- Llama CI → `experiments.tex:123` 添加 `±X.X` 格式 error bars，更新 caption (line 115)
- Phi-3 → `experiments.tex:58` 插入新行，同步更新 Models 段落 (line 7-16) 和 Table 1 caption (line 44)

报告已写入 `artifacts/paper_data_audit.md`。

---
