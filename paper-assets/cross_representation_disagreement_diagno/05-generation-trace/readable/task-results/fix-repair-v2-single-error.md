# fix repair v2 single error

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_repair_v2_single_error_20260515T072658_result.json`
- **Structured JSON:** [`75caa1003f4163533dda.json`](../../sessions/75/75caa1003f4163533dda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

10 个 SINGLE_ERROR 样本，`stability` 全部为 None，确认了退化问题。

修改完成：

**pipeline.py**（第 135-137 行）：在 stability check 块之后、错误分类之前，新增：
```python
if dis.agreement_type == AgreementType.SINGLE_ERROR:
    rec["stability"] = {"predicted_error_side": dis.error_side}
```

**repair_only.py**（第 80-81 行）：在 `repair_one()` 中 `dis = rec["disagreement"]` 之后，新增：
```python
if dis.get("agreement_type") == AgreementType.SINGLE_ERROR and "stability" not in rec:
    rec["stability"] = {"predicted_error_side": dis["error_side"]}
```

**处理流程**：SINGLE_ERROR 样本的崩溃侧由 `detect_disagreement` 确定性推断（`error_side`），直接赋值给 `predicted_error_side`，跳过 stability check。downstream 的 `targeted_repair` 读取 `rec["stability"]["predicted_error_side"]` 得到 `"fol"` 或 `"code"`，不再因 None 退化为 blind fallback。

---
