# code d004 random injector redesign

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d004-random-injector-redesign_20260514T104417_result.json`
- **Structured JSON:** [`9cb299171646b65ce74b.json`](../../sessions/9c/9cb299171646b65ce74b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D004 变更完成。

## 修改文件

| 文件 | 变更 |
|------|------|
| `injection/random_injector.py` | 完全重写：删除 6 种独立扰动函数，改为委托给 P1/P2/C1/C4 四个 TaxEI 算子 |
| `data/formatter.py` | 新增 `mode` 参数和 `_make_error_tag()`：`taxei` 模式嵌入 `[Error Type: P1_StepOrderSwap]` 等标签，`random` 模式只嵌入 `[Error occurred]` |
| `data/inject_and_generate.py` | 两种 mode 统一使用相同 4 个 TaxEI 算子 + 相同 config；`_serialize_record` 记录 mode |
| `injection/test_random_injector.py` | 更新测试：验证算子委托、分布均匀性、两种 mode 的标签差异 |

## Prompt 格式对比

**TaxEI mode（recovery step 观测）**:
```
[Error Type: P2_SubGoalDeletion]
You arrive at drawer 1. The drawer 1 is closed.
```

**Random mode（同一数据）**:
```
[Error occurred]
You arrive at drawer 1. The drawer 1 is closed.
```

## 验证结果

- 100 次注入全部通过 validate，算子分布 ~25%/each（P1:26, P2:27, C1:22, C4:25）
- 两种 mode 的算子分布完全一致（seed 相同时）
- TaxEI 标签正确包含具体类型，Random 标签仅包含 `[Error occurred]`
- 非 recovery step 的格式完全一致

---
