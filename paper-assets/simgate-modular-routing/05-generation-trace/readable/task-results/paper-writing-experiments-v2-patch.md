# paper writing experiments v2 patch

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_v2_patch_20260514T112634_result.json`
- **Structured JSON:** [`c5dbdb6164848d990d69.json`](../../sessions/c5/c5dbdb6164848d990d69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出已注册为 `art_20260514_c1b3b2`。

两处修改摘要：

1. **Table 1**: `Implicit Router` → `Trained Router`，填入 $-10.70$, CI [$-15.25$, $-6.38$], death 17.6% [A]。baselines 段新增一段解释 trained router 结果（低于 always-det 1.23 points，death rate 可比，避免退化但未改善）。

2. **Section 3.3**: 替换 placeholder，新增两段：
   - **End-to-end evaluation**: score $-10.70$，97.0% sim ratio → 仅 3% 路由到 internal，近 always-det 行为 [A]
   - **Seed stability**: 4 seeds balanced acc $58.1 \pm 0.8\%$（稳定，仅高于 random 8pp），internal recall 51.5%–81.8%（30+ pp range，seed-dependent boundary）[A]

所有数字标注 [A] 表示 A-source 数据。

---
