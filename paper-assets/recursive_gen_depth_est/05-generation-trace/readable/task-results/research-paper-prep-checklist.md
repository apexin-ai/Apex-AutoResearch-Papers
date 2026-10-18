# research paper prep checklist

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-prep-checklist_20260515T091715_result.json`
- **Structured JSON:** [`79d2e26691fccbeebb1a.json`](../../sessions/79/79d2e26691fccbeebb1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Checklist 已写入 `artifacts/paper_prep_checklist.md`。

**总结**：D002 硬约束 8 项中 3 项完全通过、3 项部分完成、2 项缺失。

关键发现：
- **4 张主图已齐**（fig1–fig4 PDF+PNG），bibliography 35 refs 超额
- **最大风险**：paper_framing 声称 z-score 恢复 linear model d1v2 AUC（0.13→0.68, 0.25→0.83），但服务器上只有 RF 的 z-score 数据（delta<0.01pp），linear model 恢复效果无实验支撑。需在 May 17 前跑 LR cross-strategy LOO + z-score 实验验证
- **k-NN inference**（D002-6）完全缺失——无代码、无结果，需确认是否仍为硬约束
- **Surprisal reference model specification**（D002-4）纯写作缺口，Phase 2 必修

---
