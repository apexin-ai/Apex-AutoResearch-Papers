# experiment d135 frontier adjust

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_d135-frontier-adjust_20260521T142812_result.json`
- **Structured JSON:** [`2f8f7f32ef1dc2362213.json`](../../sessions/2f/2f8f7f32ef1dc2362213.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

o3 恢复了，刚完成 folio_10 (12/12)。综合报告如下：

---

## D135 Frontier SCB 当前状态

### gpt-4.1 — 52/204, ETA ~52min
- **SC Accuracy: 74.0%** (37/50)
- Fleiss' κ = **0.813** (strong agreement)
- Full agreement (12/12 unanimous): 64%
- Per-label: True=77.8%, False=83.3%, **Unknown=65.0%**（最弱）
- 错误模式：主要是 Unknown↔False 混淆（folio_25, 29, 43, 45 都是 gold=Unknown 被判 False）和 True→Unknown（folio_18, 19, 28, 40）
- 偶尔 502 但恢复正常，运行稳定

### gpt-5.5 — 12/204, ETA ~253min
- SC Accuracy: 9/10 = 90.0%（样本太少）
- 每题耗时 ~60-140s，非常慢（conc=4）
- folio_5 只拿到 3/12 answers（502 导致）

### o3 — 11/204, ETA ~265min
- SC Accuracy: 7/10 = 70.0%
- **Answer yield: 60%**（72/120 成功）
- 3 个问题完全空答案（folio_1, 2, 5 全部 500 error）
- 刚从连续 502 中恢复，folio_10 拿到 12/12
- 数据质量差：空答案题的 SC 结果不可信

## o3 评估

Answer completion rate = 60%，技术上 > 50% 阈值。但实际问题：
1. **3/10 题完全无数据**（不是部分缺失，是全部 12 次调用都失败）
2. 速度极慢，0.7 q/min，预计 4.4 小时
3. 服务不稳定，刚经历连续 502

**建议**：o3 继续跑，但同时启动 gemini-2.5-pro 作为补充/备选。如果 o3 后续稳定下来，两个结果都能用；如果继续崩，gemini 数据可替代。需要你确认是否这样做，还是直接 kill o3 换 gemini。

---
