# code cosinesim check

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cosinesim-check_20260514T111134_result.json`
- **Structured JSON:** [`5be5f23a67c25547802c.json`](../../sessions/5b/5be5f23a67c25547802c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。核心结果：

**Test Macro-F1 = 0.5606 ✓ 已确认**（threshold=0.61, invert=True，由 val 搜索得出）

分布分析要点：
- **Stagnation 的 cosine sim 更高**（0.692 vs 0.613）——停滞时 agent 重复操作、embedding 变化小
- Cohen's d = 0.70（中等效应量），但两类分布在 0.50-0.75 区间重叠严重
- Val 上 separation 仅 0.014，远小于 test 的 0.079，threshold 迁移不稳定
- Oracle best on test = 0.7439（远高于实际 0.5606），说明 val/test 分布差异是主要瓶颈
- 将整个 embedding 序列压缩为单一标量是根本限制，GRU probe 能利用完整时序信息

报告已写入 `artifacts/cosinesim_analysis_report.md`。

---
