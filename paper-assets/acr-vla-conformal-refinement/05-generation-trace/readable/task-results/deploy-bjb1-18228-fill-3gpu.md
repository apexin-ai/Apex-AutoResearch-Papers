# deploy bjb1 18228 fill 3gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-fill-3gpu_20260520T172904_result.json`
- **Structured JSON:** [`61a63b4d8e4aaf8c4079.json`](../../sessions/61/61a63b4d8e4aaf8c4079.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部启动成功，正在加载模型：

| GPU | exp_id | PID | 状态 |
|-----|--------|-----|------|
| cuda:0 | eval-random-selection-spatial-seed42-r3 | 477008 | 运行中 (tmux: eval-random-spatial-r3) |
| cuda:2 | eval-obs-only-object-norm005-seed44 | 477286 | 运行中 (tmux: eval-norm005-seed44) |
| cuda:3 | eval-obs-only-object-norm003-seed44 | 477496 | 运行中 (tmux: eval-norm003-seed44) |

**已 harvest 的结果：**
- `eval-k20-obs-only-object-seed42`: SR = 0.20 → registry DONE
- `eval-random-selection-object-seed47`: SR = 0.07 → registry DONE

---
