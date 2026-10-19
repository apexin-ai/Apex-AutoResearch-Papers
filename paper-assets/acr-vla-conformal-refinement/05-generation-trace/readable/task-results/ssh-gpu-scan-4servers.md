# ssh gpu scan 4servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-scan-4servers_20260517T112514_result.json`
- **Structured JSON:** [`8e29558aecf02c997b9a.json`](../../sessions/8e/8e29558aecf02c997b9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== bjb1-18228 (4 GPU) ===
cuda:0 — PID 474319 — mode=crm_obs_only, norm=0.1, seed=45, benchmark=object, n_rollouts=default | GPU util 21%, mem 1942 MiB
cuda:1 — PID 612853 — mode=crm_obs_only, norm=0.3, seed=47, benchmark=object, n_rollouts=10 | GPU util 20%, mem 5664 MiB
cuda:2 — PID 587763 — mode=crm_obs_only, norm=0.1, seed=46, benchmark=object, n_rollouts=10 | GPU util 23%, mem 4268 MiB
cuda:3 — PID 588037 — mode=crm_obs_only, norm=0.1, seed=47, benchmark=object, n_rollouts=10 | GPU util 19%, mem 4268 MiB

=== bjb1-32546 (6 GPU) ===
cuda:0 — PID 421086 — mode=crm_perdof, norm=0.3, seed=44, benchmark=object, n_rollouts=10 | GPU util 21%, mem 5665 MiB
cuda:1 — PID 414824 — mode=crm_perdof, norm=0.1, seed=47, benchmark=object, n_rollouts=10 | GPU util 23%, mem 5665 MiB
cuda:2 — PID 416568 — mode=crm_obs_only, norm=0.3, seed=46, benchmark=object, n_rollouts=10 | GPU util 21%, mem 5665 MiB
cuda:3 — PID 422357 — mode=crm_obs_only, norm=default, seed=46, benchmark=object, n_rollouts=10 | GPU util 21%, mem 5665 MiB
cuda:4 — PID 393646 — mode=crm_perdof, norm=0.1, seed=46, benchmark=object, n_rollouts=10 | GPU util 21%, mem 4269 MiB
cuda:5 — PID 423767 — mode=crm_perdof, norm=default, seed=46, benchmark=object, n_rollouts=10 | GPU util 19%, mem 5665 MiB

=== bjb2-28827 (6 GPU) ===
cuda:0 — PID 224628 — mode=crm_scalar, norm=0.1, seed=45, benchmark=object, n_rollouts=default | GPU util 17%, mem 1941 MiB
cuda:1 — PID 222830 — mode=crm_perdof, norm=0.2, seed=45, benchmark=object, n_rollouts=default | GPU util 17%, mem 1942 MiB
cuda:2 — PID 392856 — mode=crm_perdof, norm=0.3, seed=46, benchmark=object, n_rollouts=10 | GPU util 19%, mem 5664 MiB
cuda:3 — PID 242264 — mode=crm_obs_only, norm=default, seed=45, benchmark=object, n_rollouts=default | GPU util 19%, mem 2410 MiB
cuda:4 — PID 389051 — mode=crm_perdof, norm=0.2, seed=46, benchmark=object, n_rollouts=10 | GPU util 18%, mem 5664 MiB
cuda:5 — PID 326081 — mode=crm_perdof, norm=0.2, seed=44, benchmark=object, n_rollouts=10 | GPU util 17%, mem 2875 MiB

=== bjb2-40593 (1 GPU) ===
cuda:0 — PID 388460 — mode=crm_perdof, norm=0.1, seed=47, benchmark=object, n_rollouts=10 | GPU util 12%, mem 5628 MiB
```

**汇总**：4 台服务器共 17 张卡，全部在跑 `src/evaluate.py`，0 张空闲。全部是 benchmark=object，覆盖三种 mode（crm_obs_only / crm_perdof / crm_scalar）和多种 norm（0.1 / 0.2 / 0.3 / default）× 多 seed（44-47）的网格评估。

---
