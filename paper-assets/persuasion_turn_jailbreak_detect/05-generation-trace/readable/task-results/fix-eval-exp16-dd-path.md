# fix eval exp16 dd path

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval-exp16-dd-path_20260519T162529_result.json`
- **Structured JSON:** [`712511be605391624ec2.json`](../../sessions/71/712511be605391624ec2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 汇报

**修复完成。**

- **修复前** 第 34 行：`"dd_ood": PROJ / "data/dd_ood_perturbed/perturbed.jsonl"`
- **修复后** 第 34 行：`"dd_ood": PROJ / "data/generated/deceptive_delight_all.jsonl"`
- docstring（第 6 行）也同步更新了。
- `eval_exp16.py` 中已无 `dd_ood_perturbed` 残留。

**eval_exp17.py 无此问题**——grep `dd_ood_perturbed` 和 `perturbed` 均无匹配。

---
