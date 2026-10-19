# test paper switch dryrun

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_test_paper_switch_dryrun_20260527T201242_result.json`
- **Structured JSON:** [`bbcda0a6ea555df8bdd0.json`](../../sessions/bb/bbcda0a6ea555df8bdd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

恢复完整，原文无损。

---

## 汇报

| | Scenario B (s2=55) | Scenario C (s2=58) |
|---|---|---|
| 替换数 | **11/11** (3 files) | **12/12** (3 files) |
| 编译 | PDF compiled OK | PDF compiled OK |
| 页数 | 15 | 15 |
| 3-seed CAR | 57.17 ± 1.89 | 58.17 ± 0.29 |
| permutation p (one-tail) | **0.071** (>= 0.05) | **0.012** (< 0.05) |
| permutation p (two-tail) | 0.155 | 0.036 |
| 叙事 | full redundancy | modest but significant |
| delta | +2.5 pp | +3.5 pp |

**Scenario B vs C 替换数差异**：B 有 11 个替换，C 有 12 个——差异来自 `discussion L3 scope` 仅在 Scenario C 触发（将 "not geometric supervision, account for all" 改为 "with EE-only SDF contributing at most a modest increment"）。这是代码设计如此，不是 bug。

**未发现问题**：所有替换位置唯一匹配，无遗漏、无编译警告、两个场景页数一致。

---
