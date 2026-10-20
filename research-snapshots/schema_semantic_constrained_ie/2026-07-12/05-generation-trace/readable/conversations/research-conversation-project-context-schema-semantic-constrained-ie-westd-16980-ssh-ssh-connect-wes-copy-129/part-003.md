# Research conversation: <project_context> # 项目: schema_semantic_constrained_ie ## 运行环境 - 服务器名: westd-16980 - SSH 连接命令: ssh connect.westd.seetacl — Part 3 of 3

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../research-conversation-project-context-schema-semantic-constrained-ie-westd-16980-ssh-ssh-connect-wes-copy-129.md) · [Structured JSON](../../../sessions/57/57abf1e1f6fabab53643.json)

## Round 1

### Assistant

_source line 718 · 2026-05-17T17:09:43.671Z_

All changes verified. Here's the complete report:

---

## 修改总结

### 1. 代码修改

**`compiler/type_mask_processor.py`** (3 处修改):

| 行号 | 修改 |
|------|------|
| L36 | 新增 `import logging` |
| L47 | 新增 `logger = logging.getLogger(__name__)` |
| L272 | `__init__` 中新增 `self._fallback_count = 0` |
| L456-479 | `__call__` 内部：整个 batch_idx 循环体包裹在 `try/except Exception`，初始化 `position = FieldPosition.UNKNOWN`，错误时记录诊断日志（step、position、event_type、role、ids_tail、error type+message），不修改 scores（grammar-only fallback） |

**`run_constrained_extraction.py`** (1 处修改):

| 行号 | 修改 |
|------|------|
| L582-585 | `run_single_pass` 中 generate() 后、decode 前：遍历 processors 找 TypeConstraintProcessor，如 `_fallback_count > 0` 则打印统计 |

### 2. 诊断日志格式

```
Semantic fallback step=N pos=POSITION evt=EVENT_TYPE role=ROLE ids_tail=[...last 20 ids...] err=ExceptionType: message
```

### 3. Re-Dry-Run 对比表 (10 docs, Qwen3-8B)

| 指标 | unconstrained | full_s1 (per-step fallback) |
|------|:------------:|:---------------------------:|
| Parse success | 9/10 (90%) | 9/10 (90%) |
| EV (Event Vocab) | 38.5% | **0.0%** |
| RoV (Role Vocab) | 59.8% | **28.6%** |
| AC (Arg Constraint) | 0.0% | 1.9% |
| CF (Cross-Field) | 0.0% | 12.2% |
| Entity F1 | 0.00 | **0.145** |
| Trigger F1 | 0.129 | **0.137** |
| Argument F1 | 0.000 | **0.006** |

### 4. Fallback 触发频率

**0 次**。10 个 doc 全部完成，没有触发任何 per-step semantic fallback。`_GRAMMAR_MASK_THRESHOLD` 安全检查在 mask 层面已经阻止了所有可能导致 assertion error 的情况。try/except 作为安全网存在，未需要实际触发。

### 关键发现

- **EV 从 38.5% 降至 0%**：event type 约束完全消除了 event vocab violations
- **RoV 从 59.8% 降至 28.6%**：显著下降但未完全消除，剩余 28.6% 来自 position detection 未识别到 role 位置的 step（非 fallback 导致，是 detector coverage 问题）
- **之前的 generate-level fallback 导致整个 sample 放弃 semantic masking；现在这不再发生**（per-step fallback 粒度更细，但本次实验中未触发）
- 之前的 full_s1 在 doc 3 崩溃（assertion error），现在 10/10 完成

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65a0469a-8ec5-480f-a332-a807d28277c7",
  "isSidechain": false,
  "requestId": "req_011Cb8WZCKvKuLHP3VFw5YeN",
  "type": "assistant",
  "uuid": "c886cb1a-15fe-4a1e-ba7c-cf16eccd011f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b64bbb2d-1360-407a-b095-c5bd6e9b0769",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDNRY79o4iwaScG7KAppuU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2784,
      "cache_read_input_tokens": 146396,
      "output_tokens": 944,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 944,
          "cache_read_input_tokens": 146396,
          "cache_creation_input_tokens": 2784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2784
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 719_

```json
{
  "type": "last-prompt",
  "leafUuid": "c886cb1a-15fe-4a1e-ba7c-cf16eccd011f",
  "sessionId": "b64bbb2d-1360-407a-b095-c5bd6e9b0769"
}
```

---


### Runtime record

_source line 720_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix WikiEvents per-token semantic mask fallback",
  "sessionId": "b64bbb2d-1360-407a-b095-c5bd6e9b0769"
}
```

---
