# Structural Feature ↔ LF Overlap Classification

## Methodology

Each of the 30 structural features is classified as overlapping with a specific LF
if it directly encodes the same signal that the LF uses to generate labels.
The classification is **conservative**: indirect correlations are counted as overlap.

## The 3 Labeling Functions

| LF | Signal used |
|----|-------------|
| **cmd_rep** (command_repetition) | SequenceMatcher similarity between consecutive commands; flags ≥3 consecutive commands with sim ≥ 0.9 or 1.0 as stagnation; all-unique commands as progress |
| **file_diff** (file_diff_delta) | Counts edit commands (edit/str_replace/create/insert) and unique files edited; ≥2 edits + ≥1 file → progress; 0 edits + ≥3 search-only commands → stagnation |
| **outcome_bp** (outcome_backpropagation) | Uses trajectory exit_status (exit_context/timeout/stuck → stagnation for all windows) and final outcome (target resolved → progress for last 2 windows) |

## Feature Classification

### cmd_rep overlapping (5 features)

| Idx | Feature | Overlap rationale |
|-----|---------|-------------------|
| 14 | unique_cmd_ratio | Unique commands / total commands — directly measures the same uniqueness signal that cmd_rep uses (all-unique → progress) |
| 15 | max_repeat_ratio | Most-repeated command count / total — direct repetition magnitude, the core cmd_rep signal |
| 22 | avg_adjacent_cmd_sim | Mean SequenceMatcher similarity between consecutive commands — uses the *exact same function* as the LF |
| 23 | max_adjacent_cmd_sim | Max adjacent command similarity — same function, peak value |
| 24 | max_consecutive_similar | Longest run of consecutive commands with sim ≥ 0.9 — same threshold and logic as LF's `_has_consecutive_similar()` |

### file_diff overlapping (5 features)

| Idx | Feature | Overlap rationale |
|-----|---------|-------------------|
| 16 | num_edit_cmds | Counts edit/str_replace/create/insert commands — same command set as `_extract_edited_files()` |
| 17 | num_search_cmds | Counts search_dir/search_file/find_file/find/grep/view — LF uses `_count_search_only()` with the same set for stagnation signal (≥3 search-only → stagnation) |
| 20 | edit_ratio | edit commands / total commands — normalized version of num_edit_cmds |
| 21 | search_ratio | search commands / total commands — normalized version of num_search_cmds |
| 27 | num_file_displays | Counts "[File:" pattern in text — these appear in edit command outputs, indirectly reflecting file modification activity |

### outcome_bp overlapping (1 feature)

| Idx | Feature | Overlap rationale |
|-----|---------|-------------------|
| 29 | is_short_trajectory | Short trajectories correlate with early termination (exit_context, AgentStuckInLoop, Timeout) — the same exit statuses that outcome_bp uses to label ALL windows as stagnation |

### No overlap (19 features)

| Idx | Feature | Why no overlap |
|-----|---------|----------------|
| 0 | num_steps | Window size; no LF uses raw step count |
| 1 | num_actions | Count of AI turns; no LF uses this |
| 2 | num_observations | Count of user/env turns; no LF uses this |
| 3 | action_ratio | Proportion of actions; no LF uses this |
| 4 | mean_text_len | Text length statistics; no LF examines text lengths |
| 5 | std_text_len | Text length variability |
| 6 | max_text_len | Longest text in window |
| 7 | min_text_len | Shortest text in window |
| 8 | mean_action_len | Average action text length |
| 9 | mean_obs_len | Average observation text length |
| 10 | text_len_trend | Linear slope of text lengths over time |
| 11 | num_commands | Total command count (not specific to any LF signal) |
| 12 | mean_cmd_len | Average command character length |
| 13 | max_cmd_len | Longest command character length |
| 18 | num_nav_cmds | Navigation commands (cd/ls/cat/open/goto/scroll); no LF uses these |
| 19 | num_submit_cmds | Submit command count; no LF checks for submit |
| 25 | num_errors | Traceback/Error count; no active LF uses error signals |
| 26 | num_test_outputs | Test output count (PASSED/FAILED); deprecated LF used this but it's not in ALL_LFS |
| 28 | num_nonzero_exits | Non-zero exit codes; no LF uses exit codes from individual commands |

## Summary

| Category | Count | Features removed |
|----------|-------|-----------------|
| cmd_rep overlap | 5 | unique_cmd_ratio, max_repeat_ratio, avg_adjacent_cmd_sim, max_adjacent_cmd_sim, max_consecutive_similar |
| file_diff overlap | 5 | num_edit_cmds, num_search_cmds, edit_ratio, search_ratio, num_file_displays |
| outcome_bp overlap | 1 | is_short_trajectory |
| **Total LF overlap** | **11** | |
| **No overlap (residual)** | **19** | |
