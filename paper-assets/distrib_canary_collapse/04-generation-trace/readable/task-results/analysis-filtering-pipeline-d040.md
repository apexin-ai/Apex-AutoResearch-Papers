# analysis filtering pipeline d040

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_filtering-pipeline-d040_20260515T153235_result.json`
- **Structured JSON:** [`dcb998a5af1757c64621.json`](../../sessions/dc/dcb998a5af1757c64621.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。

**文件**: `artifacts/D040/data/filtering_pipeline_data.json` (art_20260515_4ac8b4)

**内容结构**:
- **Stage 1 (Naive)**: α=0.0 null control 8/8 sig (100% FPR)，所有 α 均 100%
- **Stage 2 (Differencing)**: α=0.0 降至 4/8 sig (50% FPR)；消除全部 ECE→downstream，保留 4 个 token_entropy→downstream 残余 FP
- **Stage 3 (Granger+FDR)**: v6 40 tests: raw 14→FDR 6；v4 32 tests: raw 10→FDR 1；null control 0% FPR 验证；6 个 FDR 存活 pair 全在 α≥0.75 的 entropy/ECE→diversity 方向
- **Stage 4 (Multi-seed)**: α=0.75 单 seed 11/16 robust → α=1.0 四 seed 6/16 robust，单 seed 高估 ~45%
- **3 个 funnel**: A=null control 漏斗(8→4→0), B=cross-alpha Granger FDR 对比(v4 vs v6), C=α=1.0 全方法漏斗(16→14→6→6)
- **最终 6 个 robust pairs**: token_entropy→d1/d2/d3 + ece→d1/d2/d3；C001 约束已标注

---
