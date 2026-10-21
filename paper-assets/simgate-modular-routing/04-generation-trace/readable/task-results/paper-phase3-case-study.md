# paper phase3 case study

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_phase3-case-study_20260522T233759_result.json`
- **Structured JSON:** [`effae3621ce21bcf3c8d.json`](../../sessions/ef/effae3621ce21bcf3c8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据提取完成。文件写入 `artifacts/phase3_case_study_data.md`，包含 4 个案例：

| Episode | Label | Det | Int | Gap | 核心差异 |
|---------|-------|-----|-----|-----|---------|
| EP3 (var 3) | det-preferred | 67 | 0 | +67 | Internal 全程发无效 `connect` 指令，从未 focus 任何物体；Det 正确 focus orange (+58) 并打开厨房门 (+9) |
| EP17 (var 17) | det-preferred | 58 | 50 | +8 | 两边都成功，但 Det 选了 orange (58分)，Internal 选了 fountain (50分)——物体选择质量差异 |
| EP12 (var 12) | internal-preferred | 58 | 67 | −9 | Det 犯语义错误——focus 了目标容器 "red box" 而非找一个独立的 non-living thing；Internal 正确区分目标与容器，选了 orange |
| EP16 (var 16) | internal-preferred | 0 | 58 | −58 | Det 陷入 task 查询循环（9次），从未 focus 任何物体；Internal 成功 focus orange |

---
