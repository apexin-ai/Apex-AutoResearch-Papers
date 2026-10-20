# writing consistency audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_consistency-audit_20260514T045042_result.json`
- **Structured JSON:** [`720ec7de94b45f476ca2.json`](../../sessions/72/720ec7de94b45f476ca2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成，结果已写入 `artifacts/drafts/consistency_audit.md`。

发现 **4 个 Critical、6 个 Warning、5 个 Info** 问题：

**Critical：**
1. OBD 名称冲突——related_work 写 "Ordinal Boundary Detection"，method/conclusion 写 "Ordinal Binary Decomposition"
2. discussion 中 2v3 AUC 上界 0.5917 与 Table 3 最大值 0.5893 不符
3. 阈值敏感性描述 method 与 discussion 矛盾（θ=0.55 时 K* 是 "2-3" 还是 "3"，θ=0.65 时是否所有 config 都给 K*=2）
4. discussion 的 `\paragraph{Graduated Filtering.}` 只有 TODO 注释，渲染为空标题

**Warning 重点：**
- Neural probe 对比中 LightGBM AUC 写 0.6114 但 Table 3 是 0.6112
- appendix bootstrap resamples 写 500 而非主文的 1000
- appendix 使用裸文本 AUC 和硬编码 Figure~2

Notation、θ 值、模型名称、transfer retention 数值、cite 完整性等方面均验证通过。

---
