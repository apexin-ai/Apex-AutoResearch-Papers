# urgent deadline check all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_deadline_check_all_servers_20260528T095908_result.json`
- **Structured JSON:** [`03f13c1e21abc083c7fa.json`](../../sessions/03/03f13c1e21abc083c7fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full status report. Current time: ~18:02 BJT (10:02 UTC). Deadline: 20:00 BJT (12:00 UTC), ~118 min left.

---

## westd-27271 (2 GPUs)

| GPU | Experiment | Progress | Time | ETA (BJT) | Status |
|-----|-----------|----------|------|-----------|--------|
| 0 | OV l2norm k0.95 long s43 | 290/500 (T5 ep40) | ~4.5h | ~21:30 | **WILL MISS DEADLINE** (1.0 ep/min) |
| 1 | π0.5 l2norm k0.95 long s46 strict | 310/500 (T6 ep10) | 62min | ~18:30 | On track |

**Completed earlier (in logs/):**
- `random_k085_s45` → SR=44.2% (done 10:57)
- `l2norm_k075_s45` → SR=68.4% (done 10:32)

---

## cqa1-33015 (4 GPUs, all active)

| GPU | Experiment | Progress | Time | ETA (BJT) | Status |
|-----|-----------|----------|------|-----------|--------|
| 0 | π0.5 attn k0.9 long s46 strict | 410/500 (T8 ep10) | ~206min | ~19:00 | On track |
| 1 | π0.5 attn k0.7 long s46 strict | 400/500 (T7 done) | ~212min | ~19:01 | On track |
| 2 | OV random k0.95 goal s42 v4 | 460/500 (T9 ep10) | — | ~18:25 | On track |
| 3 | π0.5 l2norm k0.5 long s46 strict | 370/500 (T7 ep20) | ~192min | ~19:23 | On track |

**Completed earlier (in logs/):**
- `pi05_random_k09_long_s43_strict` → SR=32.4% (done 02:20)
- `pi05_l2norm_k09_long_s43_strict` → SR=81.2% (done 01:52)
- `pi05_l2norm_k095_long_s43_strict_w38` → SR=85.8% (done 00:00, this log was on w38)

---

## westd-41074 (4 GPUs, all active)

| GPU | Experiment | Progress | Time | ETA (BJT) | Status |
|-----|-----------|----------|------|-----------|--------|
| 0 | π0.5 l2norm k0.85 long s46 strict | 390/500 (T7 ep40) | — | ~18:30 | On track |
| 1 | π0.5 l2norm k0.7 long s46 strict (PID 923767) | 130/500 (T2 ep30) | 38min | **~19:50** | **Tight** |
| 2 | π0.5 random k0.95 long s46 strict | 200/500 (T3 done) | 63min | ~19:34 | On track |
| 3 | π0.5 random k0.5 long s46 strict | 190/500 (T3 ep40) | — | ~19:25 | On track |

---

## westd-38929 (GPU 1 idle, GPUs 0/2/3 active)

| GPU | Experiment | Progress | Time | ETA (BJT) | Status |
|-----|-----------|----------|------|-----------|--------|
| 1 | — | — | — | — | **IDLE** |
| 0/2/3 | π0.5 random k0.75 long s46 strict | 430/500 (T8 ep30) | ~119min | ~18:21 | On track |
| 0/2/3 | π0.5 attn k0.75 long s46 strict | 400/500 (T7 done) | ~129min | ~18:30 | On track |
| 0/2/3 | π0.5 attn k0.95 long s46 strict | 270/500 (T5 ep20) | ~60min | ~18:55 | On track |

**Completed just now:**
- `random_k09_long_s46_strict_w38` → SR=33.4% (done 17:46)
- `attn_k05_long_s46_strict` → SR=48.0% (done 17:42)

---

## Summary

- **14 experiments running** across 4 servers, 13 GPU slots active
- **1 idle GPU**: westd-38929 cuda:1
- **1 at-risk**: westd-27271 GPU 0 — OV l2norm k0.95 long s43 at 1.0 ep/min, needs ~210 min, **will miss deadline by ~1.5h**
- **1 tight**: westd-41074 GPU 1 — π0.5 l2norm k0.7 long s46, ETA ~19:50 BJT (10 min margin)
- **12 on track**: all π0.5 experiments should finish before 19:30 BJT
- **4 experiments completed** since last check with results harvested

**Action needed**: The OV experiment on westd-27271 GPU 0 will not finish. Decide whether to let it run past deadline or kill it. westd-38929 cuda:1 is idle and could potentially run a short experiment if needed.

---
