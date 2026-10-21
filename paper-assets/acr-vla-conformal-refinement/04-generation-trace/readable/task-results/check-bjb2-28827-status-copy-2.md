# check bjb2 28827 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb2-28827-status_20260526T080127_result.json`
- **Structured JSON:** [`b660545701e5908cd50f.json`](../../sessions/b6/b660545701e5908cd50f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== SERVER: bjb2-28827 (6×4090) ===
服务器当前时间: 2026-05-26 16:02 CST
实验启动时间: ~15:57-16:00 (即 ~5-7 分钟前，非用户所说 1.5-2h)
tmux sessions: 全部 6 个活跃
JSON 输出: 无（均未完成）

[RUNNING] pi05-crm-k2-spatial-s42-bjb2     | GPU0 21% / 11525MB | task 2/N, rollout 5/20, task1 SR=85.0%
[RUNNING] pi05-crm-k2-spatial-s43-bjb2     | GPU1 19% / 11525MB | task 2/N, rollout 5/20, task1 SR=80.0%
[RUNNING] pi05-crm-k2-spatial-s44-bjb2     | GPU2 11% / 11525MB | task 2/N, rollout 5/20, task1 SR=80.0%
[RUNNING] pi05-adaptive-spatial-s42-bjb2   | GPU3 21% / 11489MB | task 2/N, rollout 5/20, task1 SR=85.0%
[RUNNING] pi05-adaptive-spatial-s43-bjb2   | GPU4 20% / 11489MB | task 2/N, rollout 5/20, task1 SR=95.0%
[RUNNING] pi05-adaptive-spatial-s44-bjb2   | GPU5 20% / 11489MB | task 2/N, rollout 5/20, task1 SR=80.0%
```

**关键发现**：用户说"1.5-2 小时前提交"与实际不符。服务器当前时间 16:02 CST，日志首次写入时间 15:57-16:00，**实验实际只跑了 ~5-7 分钟**，远未完成。每个实验只完成了第一个 task（20 rollouts），正在第二个 task 的 5/20 rollout 处。spatial benchmark 通常有 ~10 tasks × 20 rollouts，按当前进度推算完整运行需要 ~1-1.5 小时。

是否需要继续等待，或者你想确认提交时间是否搞错了？

---
