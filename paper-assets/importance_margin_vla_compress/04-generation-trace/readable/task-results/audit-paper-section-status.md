# audit paper section status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper_section_status_20260527T042940_result.json`
- **Structured JSON:** [`8e93a07a875ffa41f05b.json`](../../sessions/8e/8e93a07a875ffa41f05b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

盘点完成。核心发现：

**论文整体成熟度高** — Abstract/Intro/Related Work/Method/Discussion/Conclusion 均已定稿，figures 全在位，claims 与 paper_framing 一致。

**3 个需立即处理的问题**：

1. **[P0] π0.5 Goal/Long 数据污染** — cqa1 宽松 success 条件影响 Table 2 整行 π0.5 Goal 数据和 Long k≤0.85 数据。建议加脚注说明，并用 X-VLA（不受影响）独立支撑 task complexity claim
2. **[P1] "Five" vs "six" architectures** — Abstract 说 five，Method 说 six，需统一
3. **[P1] SmolVLA Spatial baseline 三个不同值** (43.8%/44.6%/51.8%) — VTR cross-suite table 需加脚注区分 checkpoint 来源

Table 2 有 19+ "--" 缺口，但核心叙事围绕 k=0.9 展开，数据完整，缺口不阻塞。

---
