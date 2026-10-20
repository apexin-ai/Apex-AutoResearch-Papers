# eval 1 7b dual eval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_1_7b-dual-eval_20260516T204715_result.json`
- **Structured JSON:** [`19bbcf41385480314ac9.json`](../../sessions/19/19bbcf41385480314ac9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练仍在进行中：

| 实验 | 进度 | 预计剩余时间 |
|------|------|-------------|
| Random β=0.1 | 425/500 (85%) | ~10 min |
| ISR β=0.3 | 212/500 (42%) | ~67 min |

关键指标快照：
- **Random** step 425: prove_rate≈0.75-1.0, mean reward≈0.79-1.06, ISR 低（0.014-0.15）
- **ISR** step 212: prove_rate 极低（0.0-0.375），reward 接近 0，出现大量 frac_reward_zero_std=1.0 步。ISR β=0.3 的强惩罚似乎在严重压制学习。

ISR β=0.3 实验需要约 67 分钟才能完成。我无法在当前会话中持续轮询——需要你稍后让我回来检查，或者用 `/loop` 模式让我定期检查状态。

预计两个实验全部完成时间：**约 70 分钟后**。

---
