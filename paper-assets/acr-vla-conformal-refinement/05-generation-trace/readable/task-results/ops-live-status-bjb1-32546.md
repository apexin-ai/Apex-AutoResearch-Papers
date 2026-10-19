# ops live status bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_live-status-bjb1-32546_20260515T170456_result.json`
- **Structured JSON:** [`2b9f91913e235322fb20.json`](../../sessions/2b/2b9f91913e235322fb20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the combined status:

---

## bjb1-32546

```
cuda:0 — eval-mag-obsonly-norm003-object — task 0/10 (just loaded) — PID 121334 — 99%/5645MiB
cuda:0 — eval-vla-only-object-seed43 🔴 — task 3/10 — PID 123062 — (shared GPU 0)/4214MiB
cuda:1 — eval-vla-mean-object-seed43 🔴 — task 1/10 — PID 111718 — 21%/5146MiB
cuda:2 — eval-scalar-object-seed43 🔴 — task 1/10 (rollout 5/10) — PID 114673 — 20%/5645MiB
cuda:3 — eval-obs-only-object-norm02-seed43 🔴 — running (LOG NOT FOUND) — PID 118214 — 20%/5645MiB
cuda:4 — eval-acr-object-obs-only-norm02 — task 10/10 (orange_juice 5/10, almost done) — PID 44270 — 22%/1923MiB
cuda:5 — eval-mag-perdof-norm02-object (NEW) — task 0/10 (just loaded) — PID 127741 — 23%/5645MiB
```

**注意:** GPU 5 不再空闲，新启动了 `eval-mag-perdof-norm02-object` (crm_perdof, seed=42, norm=0.2)。GPU 3 的 obs-only-seed43 没有日志文件在 `~/runs/` 目录中（cmdline 确认是 `--mode crm_obs_only --seed 43 --max_correction_norm 0.2`，正在运行但输出未重定向到 runs 目录）。

## bjb1-18228

```
cuda:0 — eval-mag-obsonly-norm03-r2 — ✅ DONE (36.0%, 36/100) — IDLE
cuda:1 — eval-perdof-object-seed43 🔴 — task 3/10 (salad_dressing 5/10) — PID 365930 — 21%/4717MiB
cuda:2 — eval-obs-only-object-seed43 🔴 — task 4/10 done — PID 356495 — 23%/3785MiB
cuda:3 — eval-argmin-object-seed43 🔴 — task 4/10 done — PID 356701 — 23%/3749MiB
```

**空闲 GPU:** bjb1-18228 cuda:0 已释放（eval-mag-obsonly-norm03-r2 完成）。

---
