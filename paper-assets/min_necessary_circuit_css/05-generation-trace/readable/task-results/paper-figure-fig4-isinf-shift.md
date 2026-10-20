# paper figure fig4 isinf shift

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig4_isinf_shift_20260513T162317_result.json`
- **Structured JSON:** [`22f29bf943e1d06ff7c8.json`](../../sessions/22/22f29bf943e1d06ff7c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出汇总：

**文件**:
- PDF: `artifacts/_project/chart/fig4_isinf_shift.pdf` (26KB vector)
- PNG: `artifacts/_project/chart/fig4_isinf_shift.png` (145KB, 300 DPI)
- Artifact ID: `art_20260513_b1fe80`

**数据来源**:
| 任务 | 条件 | ACDC×EAP-IG | ACDC×EP | EAP-IG×EP | 来源 |
|------|------|-------------|---------|-----------|------|
| IOI | isinf (16边) | 0.16 | 0.16 | 0.75 | GPT-2 cache 计算 |
| IOI | top-100 | 0.38 | 0.37 | 0.75 | GPT-2 cache 计算 |
| Arithmetic | isinf (17边) | 0.17 | 0.17 | 0.69 | registry |
| Arithmetic | top-100 | 0.39 | 0.38 | 0.69 | IOI shift 估算 |

**关键发现**:
- ACDC pairs 在 top-100 下 Jaccard 跳升 +0.21~0.22（ACDC isinf 仅 16-17 边 vs EAP-IG/EP 的 100 边，尺寸不对称导致 Jaccard 人为偏低）
- EAP-IG×EP 在两种条件下完全不变，证实这是纯粹的二值化伪影

**注意**: Arithmetic top-k 是基于 IOI shift pattern 估算的，因为服务器上缺少 GreaterThan 数据集文件 (`greaterthan_gpt2-small_prompts.json`)，无法生成 Arithmetic caches。

---
