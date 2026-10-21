# ssh verify cuda0 olmo d050

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-cuda0-olmo-d050_20260519T052724_result.json`
- **Structured JSON:** [`9ca68635a8813b3e7129.json`](../../sessions/9c/9ca68635a8813b3e7129.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

OLMo-2 d050 is confirmed running on cuda:0. Summary:

**GPU 0 status:**
- PID **111720** (child of tmux wrapper 111715, which is alive) using **37,236 MiB / 97,887 MiB**
- GPU utilization: **56%**, Temp: 60°C, Power: 345W/600W

**Training progress:**
- Step **34 / 3,642** (~1%), ~2.07 s/it, ETA ~2h
- Loss: 2.27, grad_norm: 0.86, mean_token_accuracy: 0.574, lr warmup in progress (7.9e-6)

**All 4 GPUs confirmed as RTX PRO 6000 Blackwell with 97,887 MiB each.** GPUs 1-3 also have active processes.

---
