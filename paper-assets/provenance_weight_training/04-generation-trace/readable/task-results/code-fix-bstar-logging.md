# code fix bstar logging

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_bstar_logging_20260515T000054_result.json`
- **Structured JSON:** [`0696bfbf980a400506c0.json`](../../sessions/06/0696bfbf980a400506c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改已生效，第 155 行添加了 `if model.training:` 守卫。

---

## 产出总结

### 根因分析

seed42 记录数异常（51913 条 vs 6103 unique steps）**不是**多次运行拼接，而是 `compute_loss` 在 **eval 和训练时都被调用**，每次调用都 append 记录：

| 记录数/step | step 数量 | 来源 |
|---|---|---|
| 4 | 5718 | 正常训练（gradient_accumulation_steps=4） |
| 8 | 272 | 训练 4 + eval batch 4 |
| 12/16 | 85/24 | 训练 + 更多 eval batch |
| **8481/8493** | **3** | eval checkpoint，整个 eval dataset 过一遍 compute_loss |

**三个 seed 都有此问题**，只是 eval 触发次数和 eval batch 数量略有差异（seed123: 51353, seed456: 44356）。

### 代码修改 diff

```diff
-        step_info = {
-            "step": self.state.global_step if self.state else 0,
-            ...
-        }
-        self._step_metrics.append(step_info)
-
-        if self.log_path and len(self._step_metrics) % 10 == 0:
-            self._flush_metrics()
+        if model.training:
+            step_info = {
+                "step": self.state.global_step if self.state else 0,
+                ...
+            }
+            self._step_metrics.append(step_info)
+
+            if self.log_path and len(self._step_metrics) % 10 == 0:
+                self._flush_metrics()
```

`model.training` 在 eval 时为 `False`（HuggingFace Trainer 在 eval 前调用 `model.eval()`），只有训练 forward pass 才记录 b* metrics。修复后每个 step 应有恰好 `gradient_accumulation_steps`（4）条记录，即 6103 × 4 = 24412 条。

### 验证
- 服务器上语法检查: **SYNTAX_OK**
- 本地 artifacts 同步修改: **已完成**
- 不影响当前运行中的训练

---
