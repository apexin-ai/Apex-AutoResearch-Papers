# audit stale running experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_stale-running-experiments_20260521T010415_result.json`
- **Structured JSON:** [`84dd9d5c26a6b251bbac.json`](../../sessions/84/84dd9d5c26a6b251bbac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

你列出的 15 个实验已经全部不是 RUNNING 了（14 个 DONE，1 个 PREPARING）。这些已经被处理过了。

当前 registry 实际有 **22 个 RUNNING** 实验。以下是审计结果：

---

## 审计结果

### bjb2-28827（9 个实验）

| 实验 | PID | 判定 | 说明 |
|------|-----|------|------|
| eval-obs-only-object-norm01-seed71 | 922504 | **ALIVE** | 运行 19min |
| eval-obs-only-object-norm005-seed72 | 922712 | **ALIVE** | 运行 19min |
| eval-obs-only-object-norm003-seed73 | 922982 | **ALIVE** | 运行 19min |
| eval-obs-only-object-norm01-seed74 | 923256 | **ALIVE** | 运行 19min |
| eval-obs-only-object-norm005-seed75 | 923398 | **ALIVE** | 运行 19min |
| eval-obs-only-object-norm003-seed56 | 865274 | **COMPLETED** | JSON: `logs/eval_obs_only_object_norm003_seed56.json` |
| eval-obs-only-object-norm01-seed61 | 915187 | **DEAD** | 日志停在 rollout 5/10，无 JSON，conclusion 已标 "killed" |
| eval-obs-only-object-norm005-seed62 | 915391 | **DEAD** | 日志停在 rollout 5/10，无 JSON |
| eval-obs-only-object-norm005-seed63 | 915981 | **DEAD** | 日志停在 rollout 5/10，无 JSON |

### bjb1-32546（9 个实验）

| 实验 | PID | 判定 | 说明 |
|------|-----|------|------|
| eval-obs-only-object-norm003-seed64 | 723784 | **ALIVE** | 运行 31min |
| eval-obs-only-object-norm003-seed65 | 725722 | **ALIVE** | 运行 29min |
| eval-obs-only-object-norm01-seed64 | 726800 | **ALIVE** | 运行 28min |
| eval-obs-only-object-norm01-seed65 | 728057 | **ALIVE** | 运行 28min |
| eval-obs-only-object-norm005-seed64 | 729873 | **ALIVE** | 运行 27min |
| eval-obs-only-object-norm01-seed51-r3 | 731912 | **ALIVE** | 运行 26min |
| eval-obs-only-object-norm01-seed52-r3 | 733203 | **ALIVE** | 运行 26min |
| eval-obs-only-object-norm003-seed62-r2 | 734631 | **ALIVE** | 运行 25min |
| eval-obs-only-object-norm003-seed63-r2 | 735998 | **ALIVE** | 运行 25min |

### bjb1-18228（4 个实验）

| 实验 | PID | 判定 | 说明 |
|------|-----|------|------|
| eval-obs-only-object-norm003-seed59 | 599925 | **ALIVE** | 运行 1h41m |
| eval-obs-only-object-norm005-seed65 | 622479 | **ALIVE** | 运行 31min |
| eval-obs-only-object-norm005-seed58 | 596867 | **COMPLETED** | JSON: `logs/eval_obs_only_object_norm005_seed58.json` |
| eval-obs-only-object-norm01-seed57 | 594635 | **COMPLETED** | JSON: `logs/eval_obs_only_object_norm01_seed57.json` |

---

## 汇总

- **ALIVE**: 16 个，正常运行中
- **COMPLETED**: 3 个，需要收割结果并标记 DONE
  - `eval-obs-only-object-norm003-seed56`
  - `eval-obs-only-object-norm005-seed58`
  - `eval-obs-only-object-norm01-seed57`
- **DEAD**: 3 个，需要标记 DONE(failed)
  - `eval-obs-only-object-norm01-seed61`（已有 conclusion="killed"）
  - `eval-obs-only-object-norm005-seed62`
  - `eval-obs-only-object-norm005-seed63`

要我执行 `update_registry` 处理这 6 个实验吗？

---
