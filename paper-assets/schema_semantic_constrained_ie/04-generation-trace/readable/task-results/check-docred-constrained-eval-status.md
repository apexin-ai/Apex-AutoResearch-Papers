# check docred constrained eval status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_docred_constrained_eval_status_20260516T021048_result.json`
- **Structured JSON:** [`09d7e72e0583781faae9.json`](../../sessions/09/09d7e72e0583781faae9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 进程状态：全部存活

| 实验 | Wrapper PID | GPU PID | 状态 | 已运行 |
|------|------------|---------|------|--------|
| llama | 317464 (Ss+) | 317469 (Rl) | 运行中 | 1h44m |
| qwen | 321563 (Ss+) | 321568 (Rl) | 运行中 | 16m27s |

**注意：** 实际运行时间远低于预期的 14h+。llama 约 08:27 启动，qwen 约 09:55 启动（今日）。

### GPU 使用

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 16825 MiB | 85% |
| cuda:1 | 17265 MiB | 83% |

### 输出文件进度

| 实验 | 已完成 | 目标 | 进度 |
|------|--------|------|------|
| llama | **410/998** | 998 | 41.1% |
| qwen | **48/998** | 998 | 4.8% |

### ETA 估算

- **llama**: 414 samples / 104 min ≈ 4 samples/min → 剩余 584 samples → **~2.4h**
- **qwen**: 48 samples / 16 min ≈ 3 samples/min (最后一条 inference_time=20s) → 剩余 950 samples → **~5.3h**

### 日志状态

- **llama**: 正常运行，持续输出 `Setting pad_token_id to eos_token_id:128001` 信息（每 sample 一条）
- **qwen**: 模型加载完成，已进入推理阶段。日志显示 `Device: cuda:0`（与预期 cuda:1 不符，但 GPU 1 确实在使用中）

### 输出数据格式确认

Qwen 输出数据包含完整字段：`doc_id`, `input_text`, `gold_entities`, `gold_relations`, `raw_output`, `parsed_output` (entities + relations), `inference_time_seconds`, `mode: "full_s1"`。关系类型使用自然语言（如 "educated at", "date of birth"）而非 Wikidata P-code。

### 结论

两个实验均正常运行中，尚未完成。预计 llama 还需约 2.4h，qwen 还需约 5.3h 完成全部 998 条评估。

---
