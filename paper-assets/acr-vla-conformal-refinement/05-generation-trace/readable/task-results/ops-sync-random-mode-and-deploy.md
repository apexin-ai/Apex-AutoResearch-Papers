# ops sync random mode and deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync-random-mode-and-deploy_20260517T231313_result.json`
- **Structured JSON:** [`984f7c1bbc63cfceb6b7.json`](../../sessions/98/984f7c1bbc63cfceb6b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 实验 | 服务器 | GPU | PID | exp_id |
|------|--------|-----|-----|--------|
| random_selection seed43 | bjb2-28827 | cuda:0 | 492536 (tmux) / 492545 (GPU) | `eval-random-selection-object-seed43` |
| obs_only norm005 seed44 | bjb1-32546 | cuda:1 | 549432 (GPU) | `eval-obs-only-object-norm005-seed44` |

- `random_selection` 代码已同步到 bjb2-28827，import 验证通过
- bjb2-28827 实验刚启动，正在加载 LIBERO 环境
- bjb1-32546 实验此前已提交且正在运行（模型已加载，进入 rollout）

---
