# code fix recovery api errors

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-recovery-api-errors_20260514T090218_result.json`
- **Structured JSON:** [`ed7ae02ab1cc662ff264.json`](../../sessions/ed/ed7ae02ab1cc662ff264.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

---

## 汇报

### 1. API auth 问题根因和修复

**根因**：`call_recovery_api` 每次调用都新建 `OpenAI(api_key=[REDACTED], base_url=...)` client（L260-270）。频繁创建/销毁 client 导致连接不稳定，加上 API 端未必对每个新连接一致处理 auth header，造成间歇性 422。

**修复**：
- `__init__` 中一次性创建 `self.client = OpenAI(api_key=[REDACTED], base_url=base_url)`，全局复用
- `call_recovery_api` 改用 `self.client`，加入 3 次重试 + 2 秒间隔

### 2. Recovery 失败处理修改

**原问题**：API 异常时 `except` 块把错误写入 `record["recovery_think"] = f"API_ERROR: {e}"`，然后 `return record`，`_serialize_record` 始终标 `success: True`，导致 API 错误被当作训练数据。

**修复**：
- `call_recovery_api` 返回类型改为 `Optional[Dict]`
- API 失败时打印 warning 后 `return None`（跳过记录，不写入输出）
- `run()` 中 `process_one` 的 `None` 返回已被正确处理为 `failed += 1; continue`

### 3. formatter.py 安全检查

在服务器和本地的 `formatter.py` 中，DRY_RUN 检查旁新增：
```python
if "API_ERROR" in content or "Error code:" in content:
    raise ValueError(f"API error content detected in SFT data. Content: {content[:100]}")
```

### 4. 10 条重测结果

| 指标 | 结果 |
|------|------|
| Generated | 9/10（1 条因 inject_single 返回 None 跳过，非 API 错误） |
| API errors | 0 |
| 输出记录 success=true | 9/9 |
| SFT 数据中 API_ERROR/Error code/DRY_RUN | 无 |
| SFT 总量 | 19 条（10 vanilla + 9 injected） |
| Recovery 内容质量 | 正常推理（如"history inconsistency detected"→合理 action） |

---
