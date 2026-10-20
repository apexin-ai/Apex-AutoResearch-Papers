# Failure Diagnosis: alpha_sweep_c4_a050_s42_bf16

**Date**: 2026-05-18
**Server**: westd-17855 (cuda:5)
**Reported Issue**: EXIT_CODE=129 (SIGHUP)

## Diagnosis: FALSE ALARM - Experiment Completed Successfully

### Evidence

1. **Sentinel file `EXIT_CODE` contains "0"** (not 129). The Python script writes "0" only after `main()` completes without exception.

2. **All 11 generations present** (gen_0 baseline + gen_1 through gen_10), each with checkpoint/, metrics.json, synthetic_data/, trainer/.

3. **`all_metrics.json` has complete entries for all 11 generations.**

4. **Log confirms completion**: last meaningful lines are "All metrics saved to ..." and "Sentinel written: ...", indicating `main()` ran to its final line.

5. **EXIT_CODE=129 source**: shell-level exit code appended by the launcher/monitor, not by the Python script. Reflects SIGHUP (signal 1, 128+1=129) received by the process group.

### Root Cause of SIGHUP

The tmux session that hosted this job no longer exists (not in `tmux list-sessions`). The session was killed or the SSH connection dropped after the training completed. SIGHUP was delivered to the process group during post-completion shell cleanup. The Python script had already finished all work and written EXIT_CODE=0.

dmesg was inaccessible (permission denied), journalctl showed no relevant entries. No OOM or kernel kill involved.

### Training Progress

| Gen | PPL | MAUVE | Entropy | Eff Rank | ECE |
|-----|------|-------|---------|----------|------|
| 0 | 24.44 | 0.691 | 3.14 | 69.9 | 0.011 |
| 1 | 27.04 | 0.632 | 2.78 | 79.7 | 0.047 |
| 2 | 32.64 | 0.259 | 2.60 | 89.0 | 0.084 |
| 3 | 40.18 | 0.329 | 2.46 | 97.8 | 0.117 |
| 4 | 49.17 | 0.236 | 2.35 | 104.4 | 0.147 |
| 5 | 58.98 | 0.100 | 2.27 | 109.9 | 0.171 |
| 6 | 69.51 | 0.200 | 2.19 | 115.0 | 0.192 |
| 7 | 81.04 | 0.106 | 2.11 | 119.3 | 0.212 |
| 8 | 94.22 | 0.068 | 2.05 | 122.7 | 0.230 |
| 9 | 107.93 | 0.132 | 2.00 | 126.0 | 0.245 |
| 10 | 122.79 | 0.078 | 1.94 | 128.6 | 0.258 |

Clear collapse trajectory: PPL 5x increase, MAUVE 0.69 to 0.08, entropy monotonically decreasing.

### Status

- **All results complete and usable.** No corrupt/partial data.
- **No rerun needed.**
- Registry updated: conclusion changed from "failed" to "success", failure_reason documents the false alarm.
