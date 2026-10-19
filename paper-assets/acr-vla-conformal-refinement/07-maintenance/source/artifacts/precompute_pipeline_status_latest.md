# π0.5 CRM Precompute + Pipeline-Auto Status — 2026-05-21 17:22 UTC (May 22 01:22 CST)

## TL;DR
- **All 17 precompute processes still alive and progressing.** ETA ~50min–2.5h to full completion.
- **🚨 pipeline-auto SSH detection bug CONFIRMED — and it is dangerous.** Log shows `bjb1-32546=0 bjb2-40593=0 bjb2-28827=0 local=4 total=4` since 00:37 CST. The only thing currently preventing premature merge is the non-zero `local` count from wrapper processes. **When spatial s6 finishes in ~50–60 min, local→0, TOTAL→0, and pipeline-auto will trigger merge while object dir is EMPTY and spatial s0–s5 are only ~66% done.**
- **Recommended action: kill pipeline-auto NOW and fix the remote ps-grep-pipe (or rebuild with sentinel files), before s6 finishes.**

## Per-server precompute status

Cache root: `/root/autodl-tmp/crm_cache_pi05/` (note: **not** `crm_cache_k1_pi05` as listed in the task brief).

### bjb1-32546 — Object s1–s9 (9 procs, 6 GPUs)
- All 9 python processes alive. etime: s5,s7,s8,s9 ~3h17m; s1–s4 ~3h03m; s6 ~2h18m.
- Sample progress (per-shard total = 7251):
  - s1: 5000/7251 = 69% (ETA ~85min) — log `…-obj-s1-r2.log`
  - s4: 5300/7251 = 73% (ETA ~70min)
  - s5: 6000/7251 = 83% (ETA ~40min) — `…-obj-s5-fix.log`
  - s9: 5900/7250 = 81% (ETA ~45min) — `…-obj-s9-fix.log`
  - s2/s3/s6/s7/s8 in between (60+ partials each on disk)
- GPUs: 0/2/3 at 98–99% util (active), 1/4/5 at 21–25% (lighter). All ~19GB/24GB on hot ones.
- **Note**: earlier `precompute-pi05-obj-s5-r2.log` shows `Terminated EXIT_CODE=143` at sample 3200 → restarted as `-fix.log`. Current process is healthy.

### bjb2-40593 — Object s0 (1 proc, 1 GPU, batch_size=1)
- 1 python process alive, etime 5h05m.
- Partials show 55 files for s0 = ~5400/7251 = **~74%** done. ETA ~80–110 min (slow due to bs=1).
- GPU 0: 14% util, 9.8GB/24GB.
- **History**: `precompute-pi05-obj-s0-r2.log` shows earlier `torch.OutOfMemoryError` + EXIT_CODE=1, restarted with bs=1. Current run is the OOM-recovery and is healthy.

### bjb2-28827 — Spatial s0–s5 (6 procs, 6 GPUs)
- All 6 python processes alive, etime ~3h36m each.
- s0 log: 5700/8608 = **66%** (ETA ~110 min, 2.27s/sample). Other shards similar.
- GPUs 0–5: each 20–21% util, 9.8GB/24GB (balanced one-process-per-GPU).

### bjb1-18228 — Spatial s6 (1 proc, 1 GPU) + pipeline-auto
- 1 python process alive (etime ~4h52m).
- Log: 6800/8607 = **79%** (ETA ~56 min at 1.88s/sample, finish ~02:18 CST / 18:18 UTC).
- 13 partials on disk (`partial_s6_*.pt`, 500-each, latest `s6_6000_6500.pt`).
- GPUs 0/1/2 idle (0 MiB), GPU 3 in use by s6.

## Merge / output state

- **Object** (`/root/autodl-tmp/crm_cache_pi05/object/` on bjb1-18228): **empty directory**. No partials, no merged `obs_features.pt`/`k_samples.pt`/`expert_actions.pt`/`manifest.json`. Merge has NOT happened yet.
- **Spatial** (`…/spatial/` on bjb1-18228): only 13 local s6 partials. No merged file. No partials yet from bjb2-28827.
- `find … -name manifest.json -o -name obs_features.pt …` returned empty on bjb1-18228.

## pipeline-auto status (bjb1-18228)

- Script tmux session `precompute-pi05-spatial-shard6` is host; pipeline-auto is the child bash (PID 790737) launched at `00:37:32 CST 2026`.
- Log `/root/runs/acr-vla-conformal-refinement/crm-pipeline-auto.log` last entry `Fri May 22 01:22:35 CST 2026: precompute processes remaining: bjb1-32546=0 bjb2-40593=0 bjb2-28827=0 local=4 total=4`.
- Every poll (10 polls so far, every 5 min) the **remote counts are 0**. Local count is 4 (wrapper processes around the s6 python).
- The polling check uses `ssh <host> 'ps aux | grep train_crm | grep precompute | grep -v grep | wc -l'`. The remote ssh-with-quoted-pipe must be failing (most likely the inline `grep -v grep` matches nothing because the SSH command itself is being quoted/escaped such that `train_crm` doesn't appear in remote ps output, or ssh non-interactive PATH/env issue).
- **Hazard timeline**:
  - **~50–60 min from now (≈02:18 CST / 18:18 UTC)**: spatial s6 python finishes → tmux wrappers exit → local count drops to 0 → `total=0` → pipeline-auto enters Phase 2 (clean partials), Phase 3 (rsync), Phase 4 (merge).
  - At that moment: object shards s0,s1,s2,s3,s4,s6 still not done (50–110 min remaining each); spatial s0–s5 also not done (~110 min remaining).
  - Phase 3 rsync would copy mid-progress partial files; Phase 4 merge would either fail (missing shards) or produce truncated features.

## Conclusion + recommended next step

**DO NOT WAIT.** The 50-minute window before spatial s6 finishes is the safety margin. Three options, in order of preference:

1. **Best — kill pipeline-auto now, leave precompute running, restart pipeline-auto with fixed remote check.** Use `tmux send-keys -t precompute-pi05-spatial-shard6 …` or `kill 790737` (the bash wrapper PID). Then start a corrected pipeline that either (a) escapes the ssh inner command properly (e.g. `ssh host bash -lc \"…\"` or write the polling logic into a small remote script file), or (b) drops ssh-grep entirely and instead checks for sentinel files: each remote precompute writes `…/done.s{id}` on exit; pipeline waits until all 17 sentinels exist.

2. **Acceptable — disable the auto-merge phase, keep monitoring only.** Edit the script live by killing it, then re-launch a watch-only loop. Run merge manually once all 17 shards are confirmed done via direct ssh_read_only checks.

3. **Worst — do nothing.** Premature merge will trash the object cache (rm + partial rsync), and the still-running remote shards will keep writing to remote cache; you'd need to re-rsync and re-merge after everything finishes, but you also risk the pipeline-auto then attempting to start CRM training on a broken merged file.

**Other findings worth noting**:
- bjb2-40593 s0 was OOM-restarted at bs=1; that's why it's the slowest of the 17 shards (~5h vs ~3h elapsed for the others).
- Cache dir is `crm_cache_pi05`, not `crm_cache_k1_pi05` — update task brief / docs if needed.
- GPUs on bjb1-18228 (0/1/2) and bjb2-40593 (other 5 if present, only 1 visible here) are idle — CRM training will have headroom once merge is ready, but **do not let pipeline-auto auto-start training**.
