# data table7 draft

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_table7_draft_20260519T025439_result.json`
- **Structured JSON:** [`9cbcce27029b2c43af95.json`](../../sessions/9c/9cbcce27029b2c43af95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入完成。

**产出**: `artifacts/table7_draft.md`

**核心数据**:
- 39 个 success 实验中，19 个有 5method lead-lag 分析数据，5 个有 registry 部分数据，15 个缺失
- 8 个实验 RUNNING (含 6 个 D080 fp32 修复重跑 + Qwen3.5 + SmolLM3 新架构)
- 表格按 7 个分区组织：Main axis / Cross-arch / Cross-dataset / Scale / Intervention / bf16 supplementary / Analysis-only

**关键 gaps**:
1. α=0.25 s42 和 α=1.00 mvp×4 缺 lead-lag 分析
2. 全部 4 个 intervention 实验缺分析
3. scale_14b_a050_s42 缺分析
4. MMCT 覆盖率极低（仅 2 个实验有数据）
5. α=0.10 只有 s43 一个 seed

---
