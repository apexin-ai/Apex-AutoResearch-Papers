# analysis plan 001b task selection prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-001b-task-selection-prep_20260513T195656_result.json`
- **Structured JSON:** [`d011cbd37167dfcc6f1c.json`](../../sessions/d0/d011cbd37167dfcc6f1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/plan_001b_task_selection.md`。

**核心发现：15% internal label 目标以当前 task pool 不可行。**

对全部 175 个 paired episodes 做 death-aware labeling 后：
- **69 个 deterministic labels, 1 个 internal label, 105 个 discard（tie/both-died）**
- Internal ratio: **1.4%**

原因：
1. Internal 模型在 40-60% episodes 中死亡，deterministic 极少死亡 → 绝大部分 labeled episodes 都是 "int 死了 det 活着" → deterministic label
2. 双方都存活时，scores 几乎总是 tied（都是 0 或相同值）→ 丢弃
3. **唯一产出 internal label 的 task 是 find-non-living-thing**（0% death, int 偶尔 outscores det），但也只有 33% internal

**推荐方案（Option 4）**：
1. 等 prescreening 跑完（还有 ~18 tasks，6-8h），看是否有更多 internal-preferred tasks
2. find-non-living-thing 跑 40+ episodes
3. 4-5 个 death-dominated tasks 各 20 episodes
4. **SFT 训练时用 class weight 对 internal samples 加权 3-5x** 补偿 ratio 不足
5. prescreening + MVP 数据格式兼容，可直接复用（省 ~35 episodes 的 GPU 时间）

GPU 时间估算：Option 4 需 ~3.7 hours（双卡）。

---
