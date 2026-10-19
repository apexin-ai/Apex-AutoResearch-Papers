# ops verify m007 and deploy caclr

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_m007_and_deploy_caclr_20260520T221124_result.json`
- **Structured JSON:** [`7326c217b83da1502fd3.json`](../../sessions/73/7326c217b83da1502fd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

| 检查项 | 结果 |
|--------|------|
| 文件部署 `code/train_caclr.py` | OK |
| 文件部署 `train_caclr.py` (根目录) | OK |
| `requires_grad` | `True` |
| `grad_fn` | `&lt;SubBackward0 object at 0x7ff63c1743d0>` |
| `probe weight grad norm` | `0.641441` |
| **全部检查** | **ALL GRADIENT CHECKS PASSED** |

MMD loss 梯度正常回传到 probe 权重，修复有效。

---
