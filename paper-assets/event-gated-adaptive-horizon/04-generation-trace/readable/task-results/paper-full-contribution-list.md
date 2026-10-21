# paper full contribution list

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_full-contribution-list_20260518T062246_result.json`
- **Structured JSON:** [`53e462c32ba728ac2253.json`](../../sessions/53/53e462c32ba728ac2253.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Edit complete. No em-dashes found. Here's the summary:

## 修改内容

**Lines 8-9 (原 inline findings paragraph):**
- 删除了与贡献列表重叠的 inline items (3) feedback architecture 和 (4) detector
- 保留了 item (1) seed analysis 和 item (2) dt=1 restriction finding（后者不在贡献列表中，是独立发现）
- 去掉了 "Four further findings complicate the picture:" 的列举式结构，改为两句自然段

**Lines 10-16 (contribution list):**
- 1 条 → 4 条，完整覆盖 CIVO identification、gradient decomposition、online detector、feedback architecture

## Abstract 一致性问题（需要关注）

| 指标 | Abstract | Contribution bullet | 状态 |
|------|----------|-------------------|------|
| Detector sensitivity | 5/5 cases, 2/5 predictive | 3/3 CIVO cases, 2/3 predictive | **不一致** |
| Seed count | n=4 (single env) | 6 seeds (two envs), 6/6 exceed NVE, 5/6 collapse | 范围不同，可兼容 |
| Gradient % | 38--49% / 16--22% | 38--49% / 16--22% | 一致 |
| Feedback architecture | imagination-based bootstrapping vs re-planning | 同 | 一致 |

**Detector 数字 5/5 vs 3/3 是硬冲突**，需要确认哪组数字正确，然后统一 abstract 和 contribution bullet。

---
