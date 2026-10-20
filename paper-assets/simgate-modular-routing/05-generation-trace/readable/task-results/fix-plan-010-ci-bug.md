# fix plan 010 ci bug

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan-010-ci-bug_20260515T182058_result.json`
- **Structured JSON:** [`fcca3241e08757cae918.json`](../../sessions/fc/fcca3241e08757cae918.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

**Bug**: `bootstrap_ci` 对 binary correct/incorrect 值取 `sample.mean()`，计算的是 raw accuracy 的 CI，但被标注为 balanced accuracy 的 CI。physical→life cross_domain 的旧 CI [0.5485, 0.6008] 下界高于点估计 0.4979，暴露了这个 mismatch。

**修复内容**:
1. `cross_task_transfer.py`: 将 `bootstrap_ci` 替换为 `bootstrap_balanced_acc_ci`，每次 resample 计算 balanced_acc（per-class recall 的均值）
2. 两个方向的 `results.json` 已更新
3. Registry `plan-010-cross-task-v2` metrics 已更新

**修正后 metrics**:

| 方向 | 指标 | 值 | CI95 |
|------|------|----|------|
| phys→life | in_domain_balanced_acc | 0.4242 | [0.2424, 0.6061] |
| phys→life | cross_domain_balanced_acc | 0.4979 | [0.4547, 0.5382] |
| life→phys | in_domain_balanced_acc | 0.5770 | [0.4531, 0.6894] |
| life→phys | cross_domain_balanced_acc | 0.4924 | [0.4240, 0.5593] |

注：physical→life in-domain balanced_acc=0.4242 < 0.5 (chance level)，n=612 训练样本中 internal 仅 9 个 eval sample，CI 极宽 [0.24, 0.61]。

---
