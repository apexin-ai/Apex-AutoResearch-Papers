# viz fig1 pipeline pb

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig1-pipeline-pb_20260524T091141_result.json`
- **Structured JSON:** [`44463b5b68e62b77eb41.json`](../../sessions/44/44463b5b68e62b77eb41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

输出文件：
- **PNG**: `docs/paper/figures/fig1_pipeline_pb.png` (2752x1536, 300 DPI, 2.8MB)
- **PDF**: `docs/paper/figures/fig1_pipeline_pb.pdf` (172KB)

**迭代总结**：4 轮外部迭代。
- R1: 结构正确但 box 过大、蓝色偏深
- R2: 更紧凑但颜色变成紫色（不符合要求）
- R3: 颜色修正为蓝灰色，但缺少 a* 星号、MAX-SAT 边框过重
- R4（最终版）: 全部问题修复——a* 星号正确、蓝灰色 box、红色虚线框精确围住 stage 2-3 并有微妙粉色填充、MAX-SAT 中等灰边框、SC/Oracle 分支正确。达到顶会发表质量。

---
