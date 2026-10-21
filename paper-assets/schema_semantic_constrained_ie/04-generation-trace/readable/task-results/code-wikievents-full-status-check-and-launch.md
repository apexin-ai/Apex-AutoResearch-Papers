# code wikievents full status check and launch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_full_status_check_and_launch_20260517T202659_result.json`
- **Structured JSON:** [`6d86dbfa153262795446.json`](../../sessions/6d/6d86dbfa153262795446.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全面状态报告

---

### 已完成实验

**Model: Qwen (constrained dry-run v2)**
```
Server: westd-21461:gpu1
Docs: 20/20 (14 evaluated, 6 parse failures)
Parse Success: 14/20 (70%)

Violation Rates:
  ET:  0.0%
  EV:  0.0%
  RoV: 0.0%
  AC:  0.5%
  CF:  22.3%

F1 Scores:
  Trigger F1: 0.1230
  Argument F1: 0.0213
  Entity F1: 0.1357
```

---

### 运行中实验

| 实验 | 服务器:GPU | 进度 | 速率 | 预估完成 |
|------|-----------|------|------|---------|
| Qwen constrained full | westd-16980:gpu0 | 73/246 (30%) | ~1.7 doc/min | ~06:10 UTC |
| Llama constrained full | westd-16980:gpu1 | 92/246 (37%) | ~2.1 doc/min | ~05:41 UTC |
| Mistral unconstrained full | westd-21461:gpu0 | 239/246 (97%) | — | ~几分钟内 |

---

### GPU 使用状态

| 服务器 | GPU | 显存占用 | 利用率 | 任务 |
|--------|-----|---------|--------|------|
| westd-16980 | 0 | 19043 MiB | 84% | Qwen constrained |
| westd-16980 | 1 | 18377 MiB | 84% | Llama constrained |
| westd-21461 | 0 | 19027 MiB | 89% | Mistral unconstrained |
| westd-21461 | 1 | 0 MiB | 0% | **空闲** |

---

### 待执行操作

Mistral unconstrained 即将完成 (239/246)。完成后需要：

1. **运行 violation check + eval**
2. **启动 Mistral constrained**（注意参数名与用户模板不同）：
   - `--model_name` → `--model_path`
   - `--constraint_mode` → `--mode`
   - `--ontology_path` → `--constraints_path`
   - `--output_file` → `--output_path`
   - 无 `--skip_on_error`，有 `--resume`
   - Python 路径：`/root/miniconda3/bin/python`

是否现在轮询等待 Mistral unconstrained 完成，然后自动执行 violation+eval 并启动 Mistral constrained？

---
