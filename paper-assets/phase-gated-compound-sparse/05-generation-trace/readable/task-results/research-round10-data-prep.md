# research round10 data prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_round10_data_prep_20260516T013334_result.json`
- **Structured JSON:** [`ba2c3e2bc02c902ef0db.json`](../../sessions/ba/ba2c3e2bc02c902ef0db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据编译和一致性检查完成。Artifact 已注册: `art_20260516_2f776c`。

## 结果摘要

**数据规模**: 120 个实验全部 DONE，覆盖 13 个 claims。

### 关键发现

**数据就绪度 85% — 条件性可进入 Round 10**

3 个需关注的一致性问题:

| # | 问题 | 严重度 |
|---|------|--------|
| P1 | Batch1 v2 rescore 未完成，QW accuracy 可能变化 | 🟡 |
| P2 | DS n=50 引用值与 PPI_low_median 差 ≤0.03（s020: 1.15 vs 1.13, s030: 9.94 vs 9.97），需确认计算方式 | 🟡 |
| P3 | G× 21-64× 的 appendix_b_precise_gx 不在 registry，数据源不可追溯 | 🟡 |

4 个非阻塞微调项:
- "3-15×" 范围下界应为 ~2.7×（QW s025 n=500）
- Cohen's d_z QW s015: framing 引 0.28 vs registry 0.37
- DS 8k s030 缺失（已降为定性 D086）
- GSM8K QW rand s030 gradient > importance（已在 framing 中处理）

**Claim-Evidence Matrix**: 11/13 claims 数据完整（C8 LLaMA 受限于 n=50 功效，C9 仅需 §2 引用），所有 negative results 正确归类。

**建议**: 可以开始 Round 10，并行解决 P1-P3。

---
