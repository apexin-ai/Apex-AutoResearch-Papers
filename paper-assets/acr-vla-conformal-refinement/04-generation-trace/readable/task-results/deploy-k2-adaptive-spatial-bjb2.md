# deploy k2 adaptive spatial bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_k2-adaptive-spatial-bjb2_20260525T025205_result.json`
- **Structured JSON:** [`e20f7ac8f7745cd5e52f.json`](../../sessions/e2/e20f7ac8f7745cd5e52f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

| exp_id | GPU | mem | tmux | log 状态 |
|--------|-----|-----|------|---------|
| eval-k2-adaptive-spatial-s45 | 1 | 5671 MiB | ✓ | 10 tasks loaded |
| eval-vla-only-spatial-bjb2-s45 | 3 | 5665 MiB | ✓ | 10 tasks loaded |
| eval-k2-adaptive-spatial-s47 | 4 | 6211 MiB | ✓ | 10 tasks loaded |
| eval-vla-only-spatial-bjb2-s47 | 5 | 6205 MiB | ✓ | 10 tasks loaded |

cuda:0 / cuda:2 保持 1977 MiB（τ-sweep s42 r2 / r3 未受影响）。

中途插曲：首次 `CUDA_VISIBLE_DEVICES=1 source ...` 的语法令变量仅对 source builtin 生效，进程落到了 cuda:0。立即 kill tmux session 后恢复 cuda:0 内存到 1977 MiB，并改用 `CUDA_VISIBLE_DEVICES=N python` 的直接前缀重新部署，验证 GPU 映射全部正确。

---
