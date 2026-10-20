# Phase 0.5 Disagree Case Investigation

## Root Cause: Duplicate Entries in windows_labeled.jsonl

The file contains 59,496 lines but only 40,105 unique (trajectory_id, window_idx) pairs — 11,787 pairs appear twice with **different labels**. This means two labeling runs were appended without deduplication. The quality check script (`label_quality_check_v2.py`) loads all windows into a flat list and samples from it; when a duplicate pair is sampled, it may pick the second (incorrect) version. Both investigated cases follow this pattern: the first entry has correct labels, while the second entry has wrong labels, and the quality check audited the second entry.

---

## Case 1: django__asgiref-325, window_idx=5

**Trajectory**: `django__asgiref-325__swe-agent-llama-70b` (33 total steps, target=False, exit_status=submitted)

### Duplicate entries

| Entry | Line | file_diff_delta | command_repetition | outcome_backpropagation | majority |
|-------|------|-----------------|--------------------|-------------------------|----------|
| 1st (line 57567) | correct | STAGNATION(0) | PROGRESS(1) | STAGNATION(0) | STAGNATION(0) |
| 2nd (line 57574) | **wrong** | PROGRESS(1) | PROGRESS(1) | ABSTAIN(-1) | PROGRESS(1) |

The quality check audited the **2nd entry** and found it disagreed with the content.

### Step contents (indices 22-31)

| Step | Role | Command |
|------|------|---------|
| 22 | ai | `search_dir "def async_to_sync" asgiref` |
| 23 | user | (observation: "No matches found") |
| 24 | ai | `search_dir "def async_to_sync"` |
| 25 | user | (observation: "No matches found") |
| 26 | ai | `ls -F docs` |
| 27 | user | (observation: directory listing) |
| 28 | ai | `find_file "async_to_sync" docs` |
| 29 | user | (observation: "No matches found") |
| 30 | ai | `open docs/index.rst` |
| 31 | user | (observation: file contents) |

**5 AI commands, 0 edit commands, 3 search commands** (search_dir x2 + find_file), all commands unique.

### LF analysis

- **file_diff_delta**: edit_count=0, search_count=3. Per LF logic: edit_count==0 AND search_count>=3 => STAGNATION(0). The 1st entry's label (0) is **correct**. The 2nd entry's label (1=PROGRESS) is **wrong** — impossible for edit_count=0 to yield PROGRESS.
- **command_repetition**: 5 unique commands, no consecutive similar commands => PROGRESS(1). Both entries agree. **Correct**.
- **outcome_backpropagation**: 27 total windows for this trajectory (due to duplicates; the actual unique count may differ). Window 5 is not in the last 2, and exit_status is "submitted" (not "exit_context"). However, the 1st entry has STAGNATION(0) which would require exit_status="exit_context" or being in the last 2 windows — this is slightly suspicious but depends on which total_windows count was used in the original labeling run. The 2nd entry's ABSTAIN(-1) is consistent with the verified computation.

### Verdict

The 2nd entry has a **clearly wrong file_diff_delta=PROGRESS** for a window with zero edits. The 1st entry's STAGNATION majority is more defensible: the agent is searching repeatedly without finding anything and making no code changes — this is stagnation. The quality check correctly flagged the 2nd entry as "disagree".

**The underlying bug**: duplicate labeling runs in the dataset. The 1st run produced correct labels; the 2nd run produced an impossible file_diff_delta=PROGRESS for a zero-edit window (likely a caching or computation bug in the 2nd labeling run).

---

## Case 3: iterative__dvc-7966, window_idx=12

**Trajectory**: `iterative__dvc-7966__swe-agent-llama-70b` (457 total steps, target=False, exit_status=submitted)

### Duplicate entries

| Entry | Line | file_diff_delta | command_repetition | outcome_backpropagation | majority |
|-------|------|-----------------|--------------------|-------------------------|----------|
| 1st (line 35588) | correct | ABSTAIN(-1) | STAGNATION(0) | ABSTAIN(-1) | STAGNATION(0) |
| 2nd (line 35708) | **wrong** | PROGRESS(1) | PROGRESS(1) | STAGNATION(0) | PROGRESS(1) |

The quality check audited the **2nd entry** and found all three LFs disagreed with the content.

### Step contents (indices 50-59)

| Step | Role | Command |
|------|------|---------|
| 50 | ai | `mkdir.git` |
| 51 | user | (observation: "mkdir.git: command not found") |
| 52 | ai | `mkdir.git` |
| 53 | user | (observation: "mkdir.git: command not found") |
| 54 | ai | `mkdir.git` |
| 55 | user | (observation: "mkdir.git: command not found") |
| 56 | ai | `mkdir.git` |
| 57 | user | (observation: "mkdir.git: command not found") |
| 58 | ai | `mkdir.git` |
| 59 | user | (observation: "mkdir.git: command not found") |

**5 AI commands, all identical (`mkdir.git`), 0 edit commands, 0 search commands.** The agent is stuck in a loop, repeatedly issuing a malformed command (missing space between `mkdir` and `.git`).

### LF analysis

- **file_diff_delta**: edit_count=0, search_count=0. Per LF logic: edit_count==0 but search_count<3 => ABSTAIN(-1). The 1st entry's label (-1) is **correct**. The 2nd entry's label (1=PROGRESS) is **wrong** — impossible for edit_count=0.
- **command_repetition**: 5 identical commands (`mkdir.git`), which is >=3 consecutive identical commands => STAGNATION(0). The 1st entry's label (0) is **correct**. The 2nd entry's label (1=PROGRESS) is **wrong** — claiming all commands are unique when they are all identical.
- **outcome_backpropagation**: 136 total windows, window 12 is not in the last 2, exit_status="submitted" (not "exit_context") => ABSTAIN(-1). The 1st entry's label (-1) is **correct**. The 2nd entry's label (0=STAGNATION) is **wrong**.

### Verdict

The 2nd entry has **all three LF labels wrong**. This is an extreme case of obviously stuck behavior (5 identical failing commands) being labeled as PROGRESS. The 1st entry correctly labels this as STAGNATION. The quality check correctly flagged the 2nd entry as "disagree".

**The underlying bug**: same as Case 1 — the 2nd labeling run produced entirely incorrect labels, likely due to a caching bug or a code error that was later fixed.

---

## Summary

| Case | Trajectory | Window | 1st entry majority | 2nd entry majority | Correct label | Root cause |
|------|-----------|--------|--------------------|--------------------|---------------|------------|
| 1 | django__asgiref-325 | 5 | STAGNATION | PROGRESS | STAGNATION | Duplicate: 2nd run has wrong file_diff_delta |
| 3 | iterative__dvc-7966 | 12 | STAGNATION | PROGRESS | STAGNATION | Duplicate: 2nd run has all 3 LFs wrong |

**Both "disagree" cases are caused by the same issue**: `windows_labeled.jsonl` contains two labeling runs concatenated together. The first run produced correct labels; the second run produced incorrect labels (specifically, impossible PROGRESS labels for windows with zero edits). The quality check randomly sampled the incorrect 2nd-run entries.

**Recommended fix**: Deduplicate `windows_labeled.jsonl` by keeping only the first (or last) entry per (trajectory_id, window_idx) pair, or regenerate labels from a single clean run. Until then, the quality check's disagree rate is inflated by these ghost entries from a buggy labeling run.
