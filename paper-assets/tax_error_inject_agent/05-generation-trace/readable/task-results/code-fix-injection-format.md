# code fix injection format

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-injection-format_20260514T082216_result.json`
- **Structured JSON:** [`7a0c2a4a486f12b33265.json`](../../sessions/7a/7a0c2a4a486f12b33265.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。`data/inject_and_generate.py` 做了 4 处修改：

| 修改 | 位置 | 内容 |
|------|------|------|
| 字段名统一 | `inject_single` 返回值 | `task_desc` → `task_description`（读取时兼容两种源字段名） |
| API 调用适配 | `call_recovery_api` | `record["task_desc"]` → `record["task_description"]` |
| 输出格式重构 | `_serialize_record` | 原来把 `corrupted_history` 压成字符串；改为构建 `steps` 列表（含 observation/think/action），末尾追加 recovery step，输出 `{task_description, steps, injection_info, success}` |
| DRY_RUN 占位符 | `run` 方法 | `"DRY_RUN"` → 描述性占位文本 |

验证结果：
- Vanilla SFT: 139 条
- TaxEI SFT: 141 条（139 + 2 注入）
- 注入样本含完整 `&lt;think>` + `&lt;action>` 多轮对话格式
- formatter.py 无需修改

**附注**：源轨迹数据（`collect_trajectories.py` 产出）用的也是 `task_desc`，formatter.py 期望 `task_description`。vanilla 轨迹的 task description 行目前会被跳过（`if task_desc:` 为空）。如果需要 vanilla SFT 数据也包含任务描述，需要另改 `collect_trajectories.py` 或 formatter.py。

---
