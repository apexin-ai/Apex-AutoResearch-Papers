# ssh scan bjb2 28827 cqa1 32758

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scan-bjb2-28827-cqa1-32758_20260524T004847_result.json`
- **Structured JSON:** [`b5537c9d578271d3d9be.json`](../../sessions/b5/b5537c9d578271d3d9be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### bjb2-28827 (6x 4090) — 全满

| GPU | PID | 实验 | 运行时长 | Registry ID |
|-----|------|------|----------|-------------|
| cuda:0 | 991470 | Goal VLA-only s46 | 1h46m | eval-supp-goal-vla-only-s46 |
| cuda:1 | 994768 | Goal K2mean s46 | 1h45m | eval-supp-goal-k2mean-s46 |
| cuda:2 | 992072 | Goal Reconvla s46 | 1h46m | eval-supp-goal-reconvla-s46 |
| cuda:3 | 2648 | Goal CRM s46 | 1h44m | eval-supp-goal-crm-norm005-s46 |
| cuda:4 | 924226 | **Long K2mean s45** | 4h30m | eval-supp-long-k2mean-s45 |
| cuda:5 | 995593 | Goal Adaptive s46 | 1h45m | eval-supp-goal-adapt-tau025-s46 |

### cqa1-32758 (6x 4090) — 全满

| GPU | PID | 实验 | 运行时长 | Registry ID |
|-----|------|------|----------|-------------|
| cuda:0 | 590633 | Spatial CRM s46 | 28m | eval-supp-spatial-crm-norm005-s46 |
| cuda:1 | 604298 | Spatial VLA-only s46 | 15m | eval-supp-spatial-vla-only-s46 |
| cuda:2 | 560493 | Spatial Adaptive s46 | 1h04m | eval-supp-spatial-adapt-tau025-s46 |
| cuda:3 | 601536 | Long VLA-only s46 | 17m | eval-supp-long-vla-only-s46 |
| cuda:4 | 502821 | Spatial Adaptive s45-r3 | 2h26m | eval-supp-spatial-adapt-tau025-s45-r3 |
| cuda:5 | 588065 | Spatial Reconvla s46 | 30m | **eval-supp-spatial-reconvla-s46** (新建) |

### 收割
无 — 所有 12 个实验仍在运行中。

### 部署
无 — 0 个空闲 GPU。

### Registry 修正
- 补建了 `eval-supp-spatial-reconvla-s46`（cqa1 cuda:5, PID 588065），之前漏注册。

### 最先完成的实验
1. **Long K2mean s45** (bjb2 cuda:4) — 已完成 8/10 tasks，预计 **30-60 分钟**后完成并释放 cuda:4
2. **Spatial Adaptive s45-r3** (cqa1 cuda:4) — 已跑 2.5h，应接近完成
3. **Goal s46 五件套** (bjb2 cuda:0-3,5) — 约 2-3 小时完成

建议 30-60 分钟后再扫一次，收割 Long K2mean s45 并在 bjb2 cuda:4 上部署 Long s46 系列。

---
