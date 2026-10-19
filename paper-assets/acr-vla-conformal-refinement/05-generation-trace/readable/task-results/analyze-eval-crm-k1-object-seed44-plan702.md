# analyze eval crm k1 object seed44 plan702

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-crm-k1-object-seed44-plan702_20260520T143118_result.json`
- **Structured JSON:** [`0bd04e734f1a6bf0c0e5.json`](../../sessions/0b/0bd04e734f1a6bf0c0e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：`eval-crm-k1-object-seed44-plan702`

**状态：FAILED**

实验在加载 CRM 模型后立即崩溃，未产生任何 rollout 结果。

### 错误信息

```
File "/root/acr-vla-conformal-refinement/src/evaluate.py", line 466, in evaluate
    uncertainty_dim=unc_dim,
UnboundLocalError: cannot access local variable 'unc_dim' where it is not associated with a value
```

`unc_dim` 变量在 `crm_k1_accg` 模式的代码路径中未被赋值就被引用了。

### 汇总

| 指标 | 值 |
|------|-----|
| Success Rate | N/A（未执行任何 rollout） |
| 每 task 成功率 | N/A |
| JSON 输出 | 不存在（未生成） |
| 报错 | `UnboundLocalError: unc_dim` at evaluate.py:466 |

**结论：failed** — 代码 bug 导致实验未运行。需要在 `evaluate.py` 的 `crm_k1_accg` 分支中补上 `unc_dim` 的赋值逻辑后重跑。

---
