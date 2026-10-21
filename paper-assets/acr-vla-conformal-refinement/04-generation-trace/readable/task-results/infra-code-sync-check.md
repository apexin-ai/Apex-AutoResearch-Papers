# infra code sync check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_code-sync-check_20260514T031545_result.json`
- **Structured JSON:** [`71d8ff44d3c5f7ef6360.json`](../../sessions/71/71d8ff44d3c5f7ef6360.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 代码同步报告

**两台服务器均无 git 仓库**（`.git` 不存在），无法对比 commit。

### 文件 MD5 对比

| 文件 | bjb1-18228 | bjb2-40593 | 状态 |
|------|-----------|-----------|------|
| `src/__init__.py` | `5d989330...` | `5d989330...` | 一致 |
| `src/cgs.py` | `96d4e530...` | `96d4e530...` | 一致 |
| `src/aci.py` | `7bfe3b8f...` | `7bfe3b8f...` | 一致 |
| **`src/crm.py`** | `a76e37e6...` | `374c74aa...` | **不一致** |
| `src/utils.py` | `440fb67d...` | `440fb67d...` | 一致 |
| `src/smolvla_wrapper.py` | `2e0b7c45...` | `2e0b7c45...` | 一致 |
| **`src/train_crm.py`** | `fa207317...` | `f081b61a...` | **不一致** |
| **`src/evaluate.py`** | `5da05f00...` | `e9990231...` | **不一致** |
| `src/reconvla_baseline.py` | `391cdf15...` | `391cdf15...` | 一致 |
| `mvp/run_mvp.py` | `2b227cf8...` | `2b227cf8...` | 一致 |
| `scripts/verify_pipeline.py` | `4aa9adef...` | `4aa9adef...` | 一致 |
| `tests/test_aci_sign.py` | `7f7cdb28...` | `7f7cdb28...` | 一致 |

### 结构差异
- bjb1 独有：`run_eval_gpu.py`、`src/sanity_check_reset.py`
- bjb2 独有：`artifacts/` 目录、`mvp/mvp_results.log`

### 结论

**代码不同步 ✗** — 3 个核心文件不一致：`crm.py`、`train_crm.py`、`evaluate.py`。需要确定哪台是最新版本并同步到另一台。建议用 `diff` 查看具体差异后决定同步方向。

---
