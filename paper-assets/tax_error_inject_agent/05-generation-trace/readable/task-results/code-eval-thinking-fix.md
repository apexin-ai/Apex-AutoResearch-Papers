# code eval thinking fix

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-thinking-fix_20260514T072643_result.json`
- **Structured JSON:** [`37d0001dbf7f9645136c.json`](../../sessions/37/37d0001dbf7f9645136c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 汇报

**1. 修改位置**
- `eval/recovery.py` 第 180 行：`enable_thinking=True` → `enable_thinking=False`（`apply_chat_template` 调用处）
- 全文件唯一一处 `enable_thinking`，无 `generation_config` 相关设置

**2. `&lt;think>` 格式一致性 — 三者已一致**
| 文件 | `&lt;think>` 格式 | `enable_thinking` |
|------|---------------|-------------------|
| `data/collect_trajectories.py` | 纯文本标签（prompt 中 `&lt;think>&lt;/think>`，regex 解析） | 无 |
| `data/formatter.py` | 纯文本标签（`f"&lt;think>{think}&lt;/think>"`） | 无 |
| `eval/recovery.py` | 纯文本标签（prompt 中 `&lt;think>&lt;/think>`，regex 解析） | **已改为 False** |

三者均使用纯文本 `&lt;think>` 标签，不依赖 Qwen3 原生 thinking mode。

**3. 验证**
- `py_compile` 通过
- `eval/recovery.py` 中无残留 `enable_thinking=True`
- `collect_trajectories.py` 和 `formatter.py` 中无 `enable_thinking`

---
