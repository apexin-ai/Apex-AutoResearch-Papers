# Diagnosis: eval-obs-only-object-norm003-seed43

**Server**: bjb1-18228, cuda:1  
**Date**: 2026-05-18  
**Exit code**: 129 (SIGHUP)

## Root Cause: SIGHUP from parent session termination

The process was killed by SIGHUP (signal 1). Evidence:

1. **No OOM**: No error/exception/OOM messages in the log. The last log line before `EXIT_CODE=129` is a normal rollout progress line.
2. **No tmux**: `tmux ls` returns "no server running". The tmux server that hosted this job is completely gone.
3. **Other experiments survive**: Two other eval jobs (perdof-object-default-seed43 on GPU3, perdof-object-norm003-seed44 on GPU2) are still running as detached processes. These were likely launched in a separate session or after the tmux crash.
4. **Repeated failure**: This is the second time (first PID 621127). Both failures are consistent with the same session/tmux instability.
5. **dmesg inaccessible**: Container environment blocks `dmesg`, so kernel-level OOM kill cannot be directly confirmed, but the absence of any memory-related warnings in the process log and the clean SIGHUP exit make OOM unlikely.

**Conclusion**: The tmux server (or SSH session) that launched this job crashed or was killed, sending SIGHUP to all child processes. The job wrapper's `trap 'exit 129' HUP` caught the signal and exited cleanly. This is an infrastructure/session management issue, not a code or resource issue.

## Progress at Time of Death

| Task | Rollouts Completed | Successes | Rate |
|------|-------------------|-----------|------|
| pick_up_the_alphabet_soup | 10/10 | 0 | 0% |
| pick_up_the_cream_cheese | 10/10 | 1 | 10% |
| pick_up_the_salad_dressing | 10/10 | 2 | 20% |
| pick_up_the_bbq_sauce | 10/10 | 4 | 40% |
| pick_up_the_ketchup | **6/10** | 0 | - |
| tasks 6-10 | not started | - | - |

**Total**: 4/10 tasks completed, 5th task interrupted at rollout 6/10.

## Partial Results

- **No JSON output file** exists. The script writes output only on completion.
- **Log-extractable results**: The 4 completed tasks' success rates are in the log and can be parsed if needed. However, re-running is cleaner since only 4/10 tasks finished.

## GPU State (current)

- GPU 0: idle (1 MiB)
- GPU 1: idle (1 MiB) -- freed after this job died
- GPU 2: perdof-object-norm003-seed44 running (3342 MiB)
- GPU 3: perdof-object-default-seed43 running (2410 MiB)

## Retry Recommendations

1. **Use GPU 0 or 1** (both free) for the retry.
2. **Launch via `nohup` or a fresh `tmux` session** to prevent SIGHUP on SSH disconnect. The current job wrapper traps HUP to `exit 129` (terminates cleanly but still dies). Consider wrapping with `nohup` or changing the trap to `trap '' HUP` (ignore).
3. **No parameter changes needed**: The failure is purely infrastructure-related. Same command can be re-run as-is.
4. **Full re-run recommended**: Since only 4/10 tasks completed and there's no checkpoint/resume mechanism, re-run from scratch. ~6h expected runtime for 10 tasks.
5. **Monitor tmux health**: Check if the tmux server is stable before relying on it for long jobs. Alternative: use `nohup ... &` with output redirection instead of tmux.
