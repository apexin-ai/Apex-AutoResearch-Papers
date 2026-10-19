# analyze eval crm k1 object seed43 plan702

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-crm-k1-object-seed43-plan702_20260520T143048_result.json`
- **Structured JSON:** [`28a8240f0fd674bb5511.json`](../../sessions/28/28a8240f0fd674bb5511.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：`eval-crm-k1-object-seed43-plan702`

**状态：Failed**

### 报错信息

程序在 `src/evaluate.py:466` 崩溃：

```
UnboundLocalError: cannot access local variable 'unc_dim' where it is not associated with a value
```

模型加载成功（SmolVLA + CRM K=1 ACCG，327,522 params），但在进入 rollout 之前就因为 `unc_dim` 未定义而崩溃。

### 指标

- **Success Rate**: 无（未执行任何 rollout）
- **Per-task SR**: 无
- **JSON output**: 未生成（文件不存在）

### 原因

`evaluate.py` 第 466 行引用了 `unc_dim`，但在 `crm_k1_accg` mode 的代码路径中该变量未被赋值。这是一个代码 bug。

### 结论：**failed**

需要修复 `src/evaluate.py` 中 `crm_k1_accg` 模式下 `unc_dim` 的赋值逻辑后重跑。

---
