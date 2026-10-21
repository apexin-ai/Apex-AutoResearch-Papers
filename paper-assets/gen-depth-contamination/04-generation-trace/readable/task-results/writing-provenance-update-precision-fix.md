# writing provenance update precision fix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_provenance-update-precision-fix_20260514T060337_result.json`
- **Structured JSON:** [`57caed5a5c820d3b958d.json`](../../sessions/57/57caed5a5c820d3b958d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**Part 1 — conclusion.tex:**
- `$T{=}0.7$` → `$T{=}0.70$` (line 18)。注意：当前文件中没有 `θ=0.7`，唯一的裸 0.7 是温度参数 T。0.7039 未改。

**Part 2 — paper_provenance.yaml（9 项修改）:**

| 条目 | 修改内容 |
|------|---------|
| C028 | 0.6114 → 0.6112 |
| C052 | 91-92% → 90-92% |
| C056 | universally → across all tested model pairs |
| C083 | uniformly → consistently |
| C085 | 0.5496-0.5893 → 0.5496-0.5917 across all 8 model×decoding conditions |
| C097 | universally → across all tested model pairs |
| C015 | 0.55->K\*=2-3 → 0.55->K\*=3 uniformly across all 4 decoding configs |
| C138 | 新增 neural probe claim (exp_015) |
| C139 | 新增 LLM zero-shot claim (exp_011) |

claims 计数 30 → 32。

---
