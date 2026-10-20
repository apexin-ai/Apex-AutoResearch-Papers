# code write phase3 repair

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_write_phase3_repair_20260514T200522_result.json`
- **Structured JSON:** [`72399df4508664375de3.json`](../../sessions/72/72399df4508664375de3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--help` 正常，缺少 `phase2_line_scores.json` 时 graceful 报错。脚本已写入 `/root/trace_distill_repair/run_phase3_repair.py`，功能包括：

- **4 conditions 对比**：no_trace / full_trace / structural_filtered / line_filtered
- **复用** mvp_pipeline 的 prompt 模板、API client、评估逻辑
- **Token 统计**：从 API response.usage 获取 prompt_tokens + completion_tokens
- **断点续跑**：checkpoint JSON 文件，跳过已完成 instance
- **并发**：ThreadPoolExecutor，默认 max_workers=3
- **分层分析**：>2K token 子集、>=5 structural segments 分层、structural vs line head-to-head
- **输出**：CSV + JSON summary + 终端打印

---
