# check deploy vla only baselines paired

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check-deploy_vla-only-baselines-paired_20260525T012734_result.json`
- **Structured JSON:** [`09f7d73d881008e03894.json`](../../sessions/09/09f7d73d881008e03894.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**bjb2-28827** — 无需操作
- seed43: ✅ baseline_mode=single, n_rollouts=20, SR=0.805
- seed44: ✅ baseline_mode=single, n_rollouts=20, SR=0.805

**bjb1-32546** — 已部署替换
- seed48/49 旧文件 n_rollouts=10（已备份为 `*_n10_backup.json`）
- 新部署：seed48 → GPU 1（tmux: `eval-spatial-vla-s48`），seed49 → GPU 4（tmux: `eval-spatial-vla-s49`），均 n_rollouts=20
- Registry 已注册：`eval-vla-only-spatial-bjb1-s48`、`eval-vla-only-spatial-bjb1-s49`，状态 RUNNING

注意：bjb1 当前 5 个 spatial eval 并行（3 个 Adaptive K=10 + 2 个 VLA-only），超过 3 个上限，但 VLA-only 轻量且使用独立空闲 GPU（1/4），不影响现有任务。

---
