# code parsing symmetry fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_parsing-symmetry-fix_20260513T005032_result.json`
- **Structured JSON:** [`4b56b9dc7b4a9a901153.json`](../../sessions/4b/4b56b9dc7b4a9a901153.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改已完成并验证。总结：

**4 处修改 (`eval_repo_level.py`)**：

| 位置 | 修改前 | 修改后 |
|------|--------|--------|
| L115 `parse_cwm_prediction` | `return 0  # default fail for CWM` | `return -1  # ambiguous — unified fallback via majority_class` |
| L227 `run_inference` 返回值 | `return results` | `return results, n_unparseable` |
| L482/L491 main 推理调用 | `cls_results = run_inference(...)` | `cls_results, n_cls_unparseable = run_inference(...)` (两处) |
| L498-499 predictions-only 模式 | (无) | `n_cls_unparseable = None; n_cwm_unparseable = None` |
| L550-551 output JSON | (无) | 新增 `n_cls_unparseable` 和 `n_cwm_unparseable` 字段 |

**效果**：CLS 和 CWM 的 unparseable/ambiguous 预测现在都返回 -1，统一走 `majority_class` fallback，消除了系统性偏向 CLS 的问题。unparseable 计数写入 summary JSON 供审计。

备份文件: `eval_repo_level.py.bak`  
md5: `2849d934ce94d27ef72b50378e45c166`

---
