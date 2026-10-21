# GPU Status Report — 2026-05-18 06:41 (server time)

## seetacloud-westd-4x5090 (4x RTX 5090)

All 4 GPUs active, all 3 monitored PIDs alive.

| GPU | PID | Task | VRAM | Util | Progress | Acc | ETA (server) |
|-----|--------|------|------|------|----------|-----|--------------|
| 0 | 664774 | eval_repo_cls (v4, seq8192) | 24565/32607 MiB | 91% | 6360/9784 (65.0%) | 71.1% | ~10:30 |
| 1 | 662946 | eval_repo_cwm (s42, test) | 17519/32607 MiB | 51% | 1892/9784 (19.3%) | 57.7% | ~May 19 09:00 |
| 2 | 665019 | eval_repo_cls (s123, seq8192) | 24565/32607 MiB | 90% | 5560/9784 (56.8%) | 74.9% | ~11:10 |
| 3 | 668680 | eval_repo_cwm (s123, test) | 17519/32607 MiB | 56% | 1561/9784 (16.0%) | 62.1% | ~May 19 10:00 |

### Throughput

- CLS evals: ~15 samples/min (batch_size=4), finishing in ~4h
- CWM evals: ~5 samples/min (batch_size=1, generative), finishing in ~26-27h

### tmux sessions

- `cls-v4-eval-8192` (created 00:28)
- `cls-s123-eval-8192` (created 00:28)
- `cwm-s123-eval` (created 01:32)
- CWM s42 runs as a background process (no tmux), PID 662946

### Key observations

1. CLS s123 (74.9%) significantly outperforms CLS v4 (71.1%) at the same seq_len=8192
2. CWM s42 (57.7%) lower than CWM s123 (62.1%), but s42 is running on "best" checkpoint vs s123 on checkpoint-8844
3. CWM evals are ~3x slower than CLS due to generative decoding (batch_size=1, max_new_tokens=512)
4. All processes healthy, no OOM or stalls observed

---

## home-1x5090 (1x RTX 5090)

| GPU | Status | VRAM | Util |
|-----|--------|------|------|
| 0 | **Idle** | 0/32607 MiB | 0% |

### Running processes

- `eval_re_repair.py` (PID 3577037, started May 16) — smoke test, CPU-only, likely finished or hung
- HTTP file servers on ports 18888, 19876, 18765 (utility)
- No GPU workload

### Anomaly

`eval_re_repair.py` has been running since May 16 with only 0.3% memory and 0% CPU in recent snapshot. Likely idle/waiting or completed but not exited. Worth investigating if results are needed.
