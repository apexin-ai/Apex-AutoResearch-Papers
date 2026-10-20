# submit exp002 3B signals cuda3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp002_3B_signals_cuda3_20260515T183047_result.json`
- **Structured JSON:** [`52e1478420d5729c4844.json`](../../sessions/52/52e1478420d5729c4844.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这是 exp001 的 3B d100_s123 paraphrase-aligned evaluation，运行了约 13 分钟。这是正在进行的 eval 任务，不能随意 kill。

**当前状态：cuda:3 被 exp001 eval 占用（PID 608814，3B d100_s123 para_aligned eval），无法启动 exp-002 signal computation。**

需要等这个 eval 完成后才能提交。选项：
1. **等待** — 这个 eval 一般需要多久取决于 benchmark 数量（mmlu/gsm8k/arc/humaneval 四个），可能还需 30-60 分钟
2. **换 GPU** — 检查其他 GPU 是否有空闲的
3. **用户决策** — 是否要 kill 这个 eval 来优先跑 signal computation

要我检查其他 GPU 的状态，还是等这个 eval 跑完？

---
