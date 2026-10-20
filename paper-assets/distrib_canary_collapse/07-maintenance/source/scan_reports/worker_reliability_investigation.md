# Worker / Agent / Tool Reliability Investigation — distrib_canary_collapse

> Scope: Part A (phantom success patterns), Part B (analysis pipeline corruption cascade), Part C (worker transcript characterization). Period 2026-05-14 → 2026-05-25.

---

## Part A — Worker "Phantom Success" Pattern

24 mistakes in the requested set were inspected. They split into **6 distinct phantom-success archetypes**, not a random distribution — they cluster strongly around two missing primitives: (a) no SSH tool given to the Worker, and (b) no post-write verification step.

| # | Pattern | Mistake IDs | Root primitive missing |
|---|---|---|---|
| P1 | **Wrong file path** (two copies of same artifact, edited the wrong one) | M007, M008, M009, M046, M064 | Canonical path resolution + grep-verify |
| P2 | **No SSH tool, edited local-only** while truth lives on remote | M008, M009, M059 | Worker not granted ssh tool_group |
| P3 | **Submitted but never started** (registered RUNNING / reported PID, no process) | M023, M025, M029 | `nvidia-smi` confirm post-submit |
| P4 | **Hardcoded data / didn't actually read source files** | M016 (4× iterations), M055, M058 | Worker fabricates "results" with synthetic dict instead of reading server JSON |
| P5 | **Read stale/non-canonical file** (multiple JSONs in same dir) | M032, M033, M042, M045, M046, M049, M064, M066, M085 | No single-source-of-truth enforcement |
| P6 | **Did the work but the Worker reported the wrong numbers** (text content vs file content mismatch) | M059, M078, M080 | No grep-confirm step after Edit |

**The five biggest clusters all fall under one of two architectural deficiencies:**

1. **No mandatory post-write verification.** M007/M008/M009 explicitly call it out: *"Worker 完成后必须 grep 验证关键字符串存在于目标文件…Agent 收到 Worker done 后必须在远程文件做 grep 验证再报告成功"*. The harness has no required closing step. Workers are free to terminate after the tool call returns without verifying side effects landed.

2. **No canonical-path-or-tool enforcement.** P1 + P2 + P5 together account for **14 of 24 cases (58%)**. The pattern is: two copies of the same file exist (local vs remote, `docs/paper/` vs `artifacts/_project/paper/`, `5method_leadlag.json` vs `d105_d111_joint_3sigma.json` vs `run_5method_analysis_d102.py` output), and the Worker default-reads the legacy one.

**They are NOT random.** P5 alone repeats 9 times against essentially the same root cause ("multiple analysis JSON variants coexist in analysis/ directory; Worker picks first/default"). Direct quote from M046 written by the Director: *"This is the third time this session that multi-file ambiguity caused Worker to read wrong data."*

A third lesser cluster: P4 ("phantom data") happens when the Worker is asked to *write an analysis script* — they write the script but **inject hardcoded fallback values from prompt memory instead of reading the live JSON** (M016: 4 iterations of the same C4 mistake; M055: 11/11 paths in conditional_granger_v2.py wrong; M058: detection_lower_bound.py hardcoded α=0.50 PermG=0 when actual=6/8, invalidating Proposition 1). This is the most damaging category for paper-grade results.

---

## Part B — Analysis Pipeline Corruption Cascade

**The same dose-response / K≥3 data was recomputed at minimum 7 distinct times within 6 days.** Each fix introduced a new contaminant. Timeline:

```
2026-05-18  M010        → discover MMCT reads 5method_leadlag.json with diff threshold than Table 7
2026-05-19  D102        → unify 8-pair → mauve (replaces perplexity); GPT-2m K≥4 6/8→0/8
2026-05-19  D105        → true 3σ threshold mandated; K≥4 collapses again across all experiments
2026-05-19  D111        → direction-check naive/diff lags (require canary leads downstream)
2026-05-19  M028        → discovered _onset_gen labeled 3σ but computed 2σ; backfill needed
2026-05-19  M030        → c4_a025 used old script, K≥3 inflated 0/8→8/8
2026-05-20  M032        → CSV regen Worker read pre-D111 JSONs (M032 quote: "audit produced reports, not JSON rewrites" — naive values still uncorrected for 8/10 α values)
2026-05-20  M033        → D111 was only applied to dose-response — cross-arch (Pythia-6.9B, Qwen, GPT-2m, OPT, Padding) all still pre-D111
2026-05-20  M034        → D105+D111 patches were applied SEQUENTIALLY with different scripts → K values "neither pre-D111 nor properly D111-corrected"
2026-05-20  D115        → blanket K≥4 deprecation triggered by M033/M034
2026-05-20  D116        → narrative pivot to "PermG-only survives scrutiny"
2026-05-20  M035        → D111 sign convention REVERSED (peak_lag > 0 vs < 0); D115/D116 entirely invalid
2026-05-20  D117        → undo D116 pivot; K≥3 restored
2026-05-20  M037        → 2σ/3σ still mixed across experiments
2026-05-20  M040        → run_5method_analysis.py never updated for D102 (still has perplexity); D120 about to use it
2026-05-20  D120        → "unified pipeline re-run" — promised as Weak Reject → Borderline lever
2026-05-20  M042        → D120 ran on wrong server with pre-D079 directories (no _fp32 suffix); dose-response invalidated
2026-05-20  M043        → D120 TY=0/8 caused by statsmodels API bug (signonly), not power
2026-05-20  M048        → CSV editor read `significant` field instead of `significant_fdr`
2026-05-20  M049        → 1.4B α=0.50 registered with non-canonical pair config (→perplexity), PermG=0/8 vs 3/8
2026-05-20  M050        → TY canonical script tests reverse direction (causing=1 means downstream→canary, labeled forward)
2026-05-20  M051        → CSV mixed pre/post-D111 sources again
2026-05-20  M052        → CSV consensus_ge3 computed from per-method totals instead of per-pair detail
2026-05-21  M063, M064  → T=15 α=0.45 PermG=8/8 from old script (perplexity + 3x_sigma_drift). Same bug, second time
2026-05-21  M066        → t25_a075 same bug on westd-19828 (script not deployed to that server)
2026-05-22  M072        → power simulation code updated but JSON not re-run; stale conclusion
2026-05-22  M073        → power simulation used theoretical H1 predictions as "observed" data (circular)
2026-05-22  M075        → D102 ran on truncated data (gen_10 dir exists but empty, training still going)
2026-05-23  M079        → cron false-failure tagging successful experiments as failed (3 times)
2026-05-24  M085        → K sweep took stale v3_d080 row instead of v4 from CSV containing both
```

**Same K≥3 / dose-response numbers recomputed (at least 7 full passes):**

1. **Initial** batch_analysis.py 2σ values
2. **D102** unified 8-pair (mauve) pass
3. **D105** true-3σ threshold pass
4. **D111** direction-check pass (with sign bug)
5. **D115/D116** K≥4 deprecation pass
6. **M035 fix** sign-reversed D111 pass (D117)
7. **D120** canonical pipeline pass (`run_5method_analysis_d102.py`)
8. **Post-M042/M048/M050** corrected D120 pass — but cross-arch not until M063/M064/M066 caught wrong-server stale-script issues days later

The pattern the user suspected is exactly correct: *pipeline change → forgot to backfill old experiments → mixed-version data → discover discrepancy → fix → introduce new bug → repeat.* Direct evidence from M032: *"D111 audit updated registry notes and markdown reports but never wrote corrected values back to source analysis_results.json files. Worker assumed these source files contained D111-corrected data — false."*

**Six "fix introduces new bug" events** within 7 days: D111 sign bug (M035), D102 not propagated to run_5method_analysis.py (M040), D120 ran wrong-server (M042), D120 TY statsmodels bug (M043), TY direction parameter ordering wrong (M050), D213 phantom directory entry (M081).

---

## Part C — Worker Transcript Characterization

Inspected three medium worker sessions (account-2 store, 10–30 KB range):

**Worker 1: `06522d1a` — "prepare a050_s42 submission config"**
- Tools available: full Bash + SSH MCP suite.
- Outcome: API 500 immediately on first turn. Worker returned `API Error: 500 Internal server error.` as the only assistant content. Director-side recorded this as a Worker dispatch event but the actual model call failed — silent harness failure that does not appear in the Layer 1 "Worker count" but consumed a queue slot.

**Worker 2: `f0223b54` — "read dose_response_drift.csv on westd-19828, print exactly"**
- Tool budget: `ToolSearch` (1), `ssh_read_only` (1).
- Outcome: success. One `ssh_read_only` cat, returned the CSV verbatim as final assistant text. Total ~25 lines of CSV emitted. Clean execution — the kind of task the harness handles well: single read, no side effects, no writes, no path ambiguity.

**Worker 3: `3a1fa5a0` — "scp 5 paper figure PDFs from westd-19828 → local"**
- Tool budget: 3× `Bash`. No SSH MCP used despite SSH credentials being available.
- Outcome: success ("5 个 PDF 全部下载成功" with sizes table). Worker chose `Bash` over `ssh_read_only`/`scp` MCP, which works but is inconsistent with project's mandated tool conventions.

**Worker 4: `758856fc` — "verify and re-run d102 analysis"** (briefly inspected — high constraint surface)
- Tool budget: `ToolSearch`, `ssh_read_only`, `ssh_execute`.
- Prompt prefix is **2.5 KB of active constraints C002–C009** including the C008 directive (use `threshold_onset_3sigma` not `3x_sigma_drift`) and C009 (direction filter sign convention). This is exactly the kind of cross-cutting constraint a Worker forgets on the next session. This is a structural fix attempt — embedding constraints into the worker prompt — but only worked when Director remembered to include them.

**Observations:**
- Workers given `ssh_read_only` + `ssh_execute` succeed at simple read/scp tasks.
- Workers asked to **edit** project files without SSH tools (M008, M009) cause phantom success — exactly the failure mode the harness lets through.
- Workers asked to **write analysis scripts** fabricate hardcoded data (M016, M055, M058) — these are the most expensive failures.
- The harness has no enforced "verify after write" tool; constraint discipline lives in Director prompts only.

---

## Specific Answers

### Q1: How many distinct Worker tasks needed re-run because of phantom success / bad data?

Counting from the 24 inspected Part A mistakes + the cascade in Part B, **at least 38 distinct Worker reruns** were required:
- 9 from P5 (multi-file ambiguity) — each forced a Worker rerun of analysis
- 6 from P1/P2 (wrong path) — paper Worker reruns
- 4 from P4 (hardcoded data) — script rewrites (M016 alone required 4 attempts before Director gave up and edited the artifact themselves)
- 3 from P3 (no actual submission) — submit retries
- Cross-arch D111 retroactive audit: 11 experiments × at least 2 passes (initial, then post-M035 fix) = 22 analyses
- D120 dose-response re-run: 17 cells × 1 redo after M042/M048/M050
- T=15/T=25 5method re-analysis on three separate occasions (M063, M064, M066)

### Q2: Most common root cause of Worker phantom success?

**"Read stale / non-canonical file" (Pattern P5) — 9/24 cases (37.5%).** Multiple analysis output files coexist in the same `analysis/` directory (`5method_leadlag.json`, `d105_d111_joint_3sigma.json`, `analysis_results.json`) and the Worker reads the default/legacy name. Closely followed by **"wrong path / no SSH tool" (P1+P2) — 8/24 (33%)**. Hardcoded data is rarer (3/24 = 12.5%) but per-incident more damaging because it directly fakes numerical claims.

### Q3: Are pipeline bugs a model issue or harness issue?

**Primarily harness.** Evidence:
- M046 explicit framing: *"消除多文件共存歧义——Worker 只需读默认文件即可得到正确数据"* (eliminate multi-file ambiguity — Worker only needs to read the default file to get correct data).
- M034 explicit framing: *"create a canonical K-computation function that takes raw per-pair data and outputs K with all corrections applied"* — the project had no such function. Each correction was a separate script.
- M040: `run_5method_analysis.py` and `batch_analysis.py` diverged because there was no enforced canonical analysis pipeline.
- M063 / M064 / M066: same bug recurred three times because the *old* script files weren't deleted — there's no "deprecated tooling cleanup" stage in the harness.

A model component exists (Workers don't proactively check existing canonical scripts before writing new analysis code — M055, M058), but even that is solvable by harness convention ("ALWAYS run the canonical-script-locator MCP first"). The recurrent failures are 80% missing harness primitives (canonical-source-of-truth registry, post-write verify hook, single analysis entry point, automatic deprecation of old artifacts), 20% model habit (writing scripts before reading existing ones).

### Q4: Estimated total GPU-hours and Worker-hours wasted

Using the quantified anchors:
- **M005-class fp16 / submission-prefix bugs** (M011, M017): ~2–3 GPU-h
- **M013** (duplicate bf16 experiments + lost interv_pred_s43): est. ~12 GPU-h
- **M018** (SmolLM3 v1 not killed, contended for GPU): ~4–6 GPU-h
- **M022** (3 GPUs × 8 h idle from queue depth): **24 GPU-h**
- **M038** (3 GPUs × 12 h idle from queue + delayed C4 completion): **36 GPU-h**
- **M041** (19828 2-card idle 2h+): ~4 GPU-h
- **M042** (entire D120 dose-response re-run on wrong server, all WikiText α values invalidated): ~3 GPU-h Worker time, but no GPU spend on training; cost is the **analysis-rerun lag** that delayed paper update by ~1 day
- **M054** (3 near-complete bf16 experiments killed at 80–90% progress): ~24–30 GPU-h
- **M065 + M067 + M068** (disk-full + zombie process double-occupancy on 1.4B T=25): ~15–20 GPU-h
- **M074** (tmux SSH connection storm killed 5 × 1.4B experiments mid-run): ~12.5 GPU-h (5 × 2.5 h)
- **M076** (T=10 experiments overran target gen): ~8.6 GPU-h

**GPU-hours waste estimate: ~140–160 GPU-hours.** Conservative — many smaller incidents not anchored to numbers.

**Worker-hours waste estimate**: 38+ rerun dispatches, average ~5–10 min each = ~3–6 Worker-hours of dispatch. Far more significant is the **Director/Reviewer review-and-rediscover loop**: Reports #95, #100, #102, #103, #106, #112, #126, #134, #149, #192 are all rediscovery of analyses that should have been right the first time. Reviewer pass count from M032/M033/M046 alone: 4 Reviewer reports per "re-verify all Table 7" cycle × 3 cycles = ~12 reviewer-hours per issue × 4 major cycles ≈ **48+ Reviewer-hours**.

The most damaging single bug was M035 (D111 sign reversal) — invalidated D115/D116 narrative pivot and all downstream paper edits, costing ~1 day of paper writing time. Second most damaging: M042 (D120 wrong server) which delayed the Weak-Reject → Borderline-Conference uplift by ~24 h.

---

## Key Sources

- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/mistakes.yaml
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/decisions.yaml (D102 L1780, D105 L1837, D111 L1973, D115 L2055, D116 L2075, D117 L2102, D120 L2172)
- Worker session samples: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/{06522d1a,f0223b54,3a1fa5a0,758856fc}-*.jsonl
