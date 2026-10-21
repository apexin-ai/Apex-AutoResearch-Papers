# code exp002 deploy verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002-deploy-verify_20260514T071140_result.json`
- **Structured JSON:** [`8af153ec83d3496ce7f1.json`](../../sessions/8a/8af153ec83d3496ce7f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verifications pass. Here's the deployment summary:

---

## 修复验证 + 部署结果

### Problem 1: `--ref-adapter-path` 支持

| 文件 | Before | After |
|------|--------|-------|
| `signal_minkpp.py` | `compute_minkpp_signal()` 无 `ref_adapter_path` 参数；ref model 加载不传 adapter | 新增参数 `ref_adapter_path: str = None`（L142）；ref model 加载传 `adapter_path=ref_adapter_path`（L182）；CLI 新增 `--ref-adapter-path`（L220）；`main()` 调用传参（L241） |
| `compute_signals.py` | ref model 路径解析忽略 adapter；minkpp 调用不传 ref_adapter_path | CLI 新增 `--ref-adapter-path`（L163）；ref model 解析走 `resolve_model_paths(ref_model_path, ref_adapter_path)` + auto-detect（L175-179）；minkpp 调用传 `ref_adapter_path`（L220） |

### Problem 2: `CUDA_VISIBLE_DEVICES` 移除

| 文件 | Before (远程旧版) | After |
|------|-------------------|-------|
| `compute_signals.py` | 有 `os.environ["CUDA_VISIBLE_DEVICES"]` | 无 |
| `signal_minkpp.py` | 有 | 无 |
| `signal_selfcritique.py` | 有 | 无 |

grep `CUDA_VISIBLE_DEVICES` 返回空（exit code 1），确认全部清除。

### 远程验证结果

- `grep -n ref_adapter signal_minkpp.py` → L142, L182, L241
- `grep -n ref_adapter compute_signals.py` → L175-179, L220
- `grep -n ref-adapter-path` (CLI arg) → `compute_signals.py:163`, `signal_minkpp.py:220`
- `grep CUDA_VISIBLE_DEVICES` 3 files → **empty** (no matches)

---
