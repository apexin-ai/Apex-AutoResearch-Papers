# code fix tau remaining callsites

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_tau_remaining_callsites_20260514T135309_result.json`
- **Structured JSON:** [`7d0d79a60e1fc962c366.json`](../../sessions/7d/7d0d79a60e1fc962c366.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成。

## Diff 摘要

**run_exp006.py** (3 处):
- L88: `load_exposure_scores(args.exposure_file, data["benchmarks"])` → 加 `model_id=args.tau_model_id`
- L282: `run_joint_fit(...)` 调用增加 `tau_model_id=args.tau_model_id`
- L323-328: argparse 新增 `--tau-model-id` 和 `--tau-source`

**joint_fit.py** (4 处):
- L101: `run_joint_fit()` 签名增加 `tau_model_id=None`
- L107: `load_exposure_scores(...)` 加 `model_id=tau_model_id`
- L210-214: argparse 新增 `--tau-model-id` 和 `--tau-source`
- L236: `main()` 中调用 `run_joint_fit()` 传入 `tau_model_id=args.tau_model_id`

## 全量扫描

所有 `load_exposure_scores` 调用点（4 个入口文件）均已传入 `model_id`：
| 文件 | 行号 | 状态 |
|------|------|------|
| `run_irt_calibration.py` | 483 | ✓ 已有 |
| `run_irt_stan.py` | 407 | ✓ 已有 |
| `run_exp006.py` | 88 | ✓ 本次修复 |
| `joint_fit.py` | 107 | ✓ 本次修复 |

## Dry-run

两个文件语法检查通过，`--help` 均正确显示 `--tau-model-id` 和 `--tau-source` 参数。

---
