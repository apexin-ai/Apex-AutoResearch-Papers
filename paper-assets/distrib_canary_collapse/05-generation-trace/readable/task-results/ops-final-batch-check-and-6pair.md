# ops final batch check and 6pair

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_final-batch-check-and-6pair_20260524T000447_result.json`
- **Structured JSON:** [`864e8889889279909ebe.json`](../../sessions/86/864e8889889279909ebe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个步骤已完成：

1. **实验完成确认** — t10_a045_s44 和 t15_a075_s43 均已完成，metrics 已导出，registry 已标记 DONE
2. **D102 快速分析** — 两个新实验的 distinct_3 2-pair 初步分析完成
3. **6-pair 统一 D102** — 全部 8 个实验的 5-method lead-lag 分析完成（mauve 排除）
4. **本地 artifacts 复制** — 8 个 6-pair JSON 已写入 `artifacts/` 目录
5. **汇总表** — `artifacts/_project/14b_6pair_summary_20260524.md` 已生成，含 phase diagram 分析
6. **Registry 更新** — 全部 8 个实验的 `d102_6pair` metrics 已写入 registry

关键发现：α=0.60 是 robust detection 的可靠边界（T=10 已 5/6, T=15 达 6/6）。α=0.45-0.50 是 transition/blind zone，ece 比 entropy 更灵敏。T=10 α=0.50 暴露了 PermG 单方法在短时序下的 false positive 风险（PermG 6/6 vs robust 0/6）。

---
