# analysis plan 001b revised proposal

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-001b-revised-proposal_20260513T214131_result.json`
- **Structured JSON:** [`4ff40bb6cda0df6a2d02.json`](../../sessions/4f/4ff40bb6cda0df6a2d02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

提案已写入 `artifacts/plan_001b_revised_proposal.md`。

**数据概览**:
- 预筛完成 22/24 tasks：**16 death-dom, 5 genuine-det, 1 internal-pref**
- 2 tasks 仍在跑（~30min 完成）
- MVP 4 tasks 已有 20 eps，可直接复用

**方案 A（最小方案，立即可启动）**:
- 15 tasks = 5 genuine-det + 1 int-pref + 5 death-dom + 4 MVP 复用
- 新增 185 episodes，双卡 ~6-7h
- find-non-living-thing 扩到 40 eps 以增加 internal labels

**关键发现**：genuine-det 从之前的 0 个增加到 5 个（find-animal, identify-life-stages-1, lifespan 系列, measure-melting-point），这对论文 framing 很关键——证明 router 不只是 death detector。

---
