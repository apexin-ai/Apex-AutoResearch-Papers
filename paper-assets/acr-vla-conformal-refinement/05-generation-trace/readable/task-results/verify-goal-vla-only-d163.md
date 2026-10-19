# verify goal vla only d163

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_goal-vla-only-d163_20260526T161800_result.json`
- **Structured JSON:** [`8b19b0a5276d1a15bcd0.json`](../../sessions/8b/8b19b0a5276d1a15bcd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

# 结论：两组数据都不是 D163 (a594db5) 版本

## 证据：runtime args 都包含 `unified_obs_dim`

两组实验的 `[evaluate] args:` 行都打印了 `'unified_obs_dim': None, 'n_action_steps': 10`。但 a594db5 的 evaluate.py **不包含** `unified_obs_dim` / `openvla_oft` / `SUITE_MAX_STEPS`（已在 bjb1-18228 上验证：`git show a594db5:src/evaluate.py` 的 grep counts 全为 0，现行 evaluate.py 分别为 3/6/2）。a594db5 与当前 c15065ec 相差 +82/-19 行。

## 详细对比

| Group | exp_id | Date (UTC) | Server | Runtime args | SR | D163? |
|---|---|---|---|---|---|---|
| **May 22 r4** | seed42-r4 | 05-22 12:22 | bjb1-18228 | has `unified_obs_dim`, `n_action_steps` | 98.0 | ❌ |
| | seed43-r4 | 05-22 15:19 | bjb1-32546 | 同上 | 98.0 | ❌ |
| | seed44-r4 | 05-22 15:19 | bjb1-32546 | 同上 | 97.5 | ❌ |
| **May 24** | s42 | 05-24 18:17 | bjb1-32546 | 与 r4 完全一致 | 95.5 | ❌ |
| | s43 | 05-24 18:17 | bjb1-32546 | 与 r4 完全一致 | 97.0 | ❌ |
| | s44 | 05-25 09:10 | bjb2-28827 (HEAD=446587c, 非 a594db5) | 与 r4 完全一致 | 97.5 | ❌ |

两组的 args dict 字段、值完全一致 → **使用的是同一族 evaluate.py**（带 `unified_obs_dim`/`openvla_oft` 补丁的后续版本，非 a594db5）。

a594db5 commit 时间 = 05-22 05:02 UTC；r4 实验 05-22 12:22 UTC 启动时，bjb1-18228 working copy 已 modified（`git status -s src/evaluate.py` 显示 `M`），且 args 中有 a594db5 不存在的 `unified_obs_dim` 字段——所以即便最贴近 commit 时间的 r4 也不是 a594db5 版本。

## 真正的 D163-compliant Goal VLA-only 数据

只有 `westd-pi05-vla-only-goal-s4X-paired`（05-26，westd-49937 = RTX PRO 6000 Blackwell）在 registry 中显式记录了 `reproduce.code_commit = a594db578deeeeddc0ab068549e315c5a3bb4d6a`：
- s42-paired: 97.5%
- s43-paired: 96.5%
- s44-paired: 95.5%
- mean ≈ 96.5%

但这批数据是 **Blackwell 系统性偏差 ~3pp**（loop_26/27 已警告），不能与 4090 集群其它行混表。

## 建议

如果 D163 严格要求 = a594db5，**两组都不达标**，4090 上的 Goal VLA-only 需重跑。如果实际可接受的是"两组之间 evaluate.py 一致"，则：
- 两组的 effective args 完全相同 → **可以选其中一组**；
- 1.1pp 差异（96.7% vs 97.8%）几乎全部来自 seed42——s42-r4=98.0% vs s42=95.5%，差 2.5pp，更像是 bjb1-18228 与 bjb1-32546 跨服务器的偶然漂移；
- 建议向 Director 确认 D163 红线的严格度，再决定是否需要派 Worker 在 4090 集群上 revert 到 a594db5 后重跑 Goal VLA-only 3 seeds。

---
