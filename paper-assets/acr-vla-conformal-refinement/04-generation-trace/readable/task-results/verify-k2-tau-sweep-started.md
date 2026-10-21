# verify k2 tau sweep started

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_k2-tau-sweep-started_20260524T215914_result.json`
- **Structured JSON:** [`1fb6c199a1f25318acd5.json`](../../sessions/1f/1fb6c199a1f25318acd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3台全部确认：

```
bjb2-40593: [OK] — K=2 确认, tmux=eval-k2-tau010-spatial-s42, PID 314307, τ=0.10 运行中 (10 tasks loaded), args显示 'K': 2
bjb1-32546: [OK] — K=2 确认, tmux=eval-k2-tau020-spatial-s42, τ=0.20 已在跑 rollout (task1: 10/10 success), args显示 'K': 2
bjb2-28827: [OK] — K=2 确认, tmux=eval-k2-tau030-spatial-s42, τ=0.30 已在跑 rollout (task1: 5/5 success), args显示 'K': 2
```

补充细节：
- bjb2-40593 的 tmux 名是 `eval-k2-tau010-015-spatial-s42`（合并了 τ=0.10 和 τ=0.15 两个任务），当前在跑 τ=0.10
- 3台的 config dump 都显示 `'K': 2, 'k_init': 2, 'k_full': 5`，命令行参数 `--K 2` 已生效
- bjb1-32546 和 bjb2-28827 进度较快，已进入 rollout 阶段

---
