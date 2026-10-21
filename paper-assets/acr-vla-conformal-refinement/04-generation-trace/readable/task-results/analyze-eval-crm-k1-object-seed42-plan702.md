# analyze eval crm k1 object seed42 plan702

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-crm-k1-object-seed42-plan702_20260520T143137_result.json`
- **Structured JSON:** [`3079697affe6d48c43b5.json`](../../sessions/30/3079697affe6d48c43b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：`eval-crm-k1-object-seed42-plan702`

**状态：FAILED**

实验在加载 CRM 模型后立即崩溃，未产生任何 rollout 结果。

### 错误信息

```
File "/root/acr-vla-conformal-refinement/src/evaluate.py", line 466, in evaluate
    uncertainty_dim=unc_dim,
UnboundLocalError: cannot access local variable 'unc_dim' where it is not associated with a value
```

### 详情

- CRM 模型加载成功（327,522 params from `crm_k1_best.pt`）
- SmolVLA 加载成功
- 在调用 rollout 时，`unc_dim` 变量未被赋值就被引用，导致 `UnboundLocalError`
- JSON 输出文件不存在（未生成任何结果）
- **Success Rate: N/A**（无 rollout 执行）

### 结论

**failed** — 代码 bug，`evaluate.py:466` 处 `unc_dim` 变量在 `crm_k1_accg` mode 下缺少赋值逻辑，需要修复后重跑。

---
