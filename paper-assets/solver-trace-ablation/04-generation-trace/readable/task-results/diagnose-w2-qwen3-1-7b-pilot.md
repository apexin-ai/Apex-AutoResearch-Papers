# diagnose w2 qwen3 1 7b pilot

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w2-qwen3-1_7b-pilot_20260516T111933_result.json`
- **Structured JSON:** [`6837029a8d500d48d978.json`](../../sessions/68/6837029a8d500d48d978.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常跑：

- **exec-pilot** (cuda:0): step 76/500, reward=0.25
- **isr-pilot** (cuda:1): step 75/500, reward=0.51

cron 报 failed 纯粹是 exp_id 含点号导致 tmux session 命名不合法的跟踪问题，训练进程不受影响。预计还需 ~65 分钟完成。

报告已写入 `artifacts/diagnose_w2_1.7b_pilot.md`。

---
