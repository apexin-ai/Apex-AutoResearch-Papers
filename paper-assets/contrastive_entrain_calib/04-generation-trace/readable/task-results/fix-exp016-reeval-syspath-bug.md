# fix exp016 reeval syspath bug

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp016-reeval-syspath-bug_20260519T090158_result.json`
- **Structured JSON:** [`cc2a042c1b9964b1b862.json`](../../sessions/cc/cc2a042c1b9964b1b862.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 汇报

| 项目 | 结果 |
|------|------|
| **修复前** | `sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "eval"))` → 解析为 `/root/contrastive_entrain_calib/results/eval/`（不存在） |
| **修复后** | `sys.path.insert(0, "/root/contrastive_entrain_calib/eval")` |
| **sklearn** | 已安装，版本 1.8.0 |
| **import 验证** | `from nli_utils import get_entailment_idx, get_contradiction_idx` → OK |

---
