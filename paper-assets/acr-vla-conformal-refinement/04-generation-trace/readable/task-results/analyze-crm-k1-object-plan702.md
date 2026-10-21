# analyze crm k1 object plan702

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_crm-k1-object-plan702_20260520T143045_result.json`
- **Structured JSON:** [`521e199bb7120258560e.json`](../../sessions/52/521e199bb7120258560e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 实验 1: eval-crm-k1-object-seed42-plan702
```
exp_id: eval-crm-k1-object-seed42-plan702
SR: N/A
per_task: N/A
conclusion: failed
备注: 启动后立即崩溃 — UnboundLocalError: cannot access local variable 'unc_dim' (evaluate.py:466)。无 JSON 输出。
```

### 实验 2: eval-crm-k1-object-seed43-plan702
```
exp_id: eval-crm-k1-object-seed43-plan702
SR: N/A
per_task: N/A
conclusion: failed
备注: 同上，完全相同的 UnboundLocalError。
```

### 实验 3: eval-crm-k1-object-seed44-plan702
```
exp_id: eval-crm-k1-object-seed44-plan702
SR: N/A
per_task: N/A
conclusion: failed
备注: 同上，完全相同的 UnboundLocalError。
```

### 实验 4: eval-obs-only-spatial-norm02-seed42
```
exp_id: eval-obs-only-spatial-norm02-seed42
SR: N/A (incomplete)
per_task: [task1(pick_bowl_between)=9/10, task2(pick_bowl_next_to)=10/10, task3-10=未执行]
conclusion: failed
备注: 进程 exit code=0，但只完成了 2/10 tasks 就退出。无 JSON 输出，无 "Overall success rate"。
      退出时间 2026-05-20T11:06:05Z。疑似脚本逻辑 bug 导致提前退出。
      logs/ 和 runs/ 有两份不同日志（不同次运行），task2 结果分别为 9/10 和 10/10。
```

---

### K=1 CRM Object 汇总

**无法计算均值和标准差** — 三个 seed (42/43/44) 全部因相同 bug 崩溃。

**根因**: `evaluate.py:466` 的 `unc_dim` 变量在 `crm_k1_accg` mode 下未被赋值。三个实验加载模型成功后，在构建评估环境时触发 `UnboundLocalError`。需要修复 `evaluate.py` 中该分支的 `unc_dim` 定义，然后重跑。

**当前服务器上还在跑的相关进程**: `eval-obs-only-spatial-norm02-seed49` (GPU2)、`openvla-precompute-k1` (GPU0)、`eval_random_selection_object_seed44` (GPU4)、`dryrun_crm_k1_seed42` (dry run)。

---
