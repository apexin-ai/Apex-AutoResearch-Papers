# fix cleanup rogue processes

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cleanup_rogue_processes_20260515T114032_result.json`
- **Structured JSON:** [`8326fdfe869a5d0557fd.json`](../../sessions/83/8326fdfe869a5d0557fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告如下：

### 1. PID 112847 状态
**已不存在。** `ps -p 112847` 返回空，进程已终止，无需 kill。

### 2. 其他活跃旧进程
**无。** `ps aux | grep trace_distill_repair` 和 `tmux list-sessions` 均无匹配结果，没有残留旧进程或 tmux session。

### 3. phase2_line_scores.json 验证

| 项目 | 值 |
|------|-----|
| 时间戳 | 2026-05-15 17:08 |
| 文件大小 | 2.17 MB |
| `num_instances` | **33** (符合预期) |
| `results` 条目数 | **33** |
| `scored_segments` | 3902 / 4091 total |
| `failed_segments` | 189 |
| `excluded` | `['fastapi_3', 'fastapi_5']` |
| `annotations` | 7 条 (httpie_1, luigi_5/10/14, scrapy_4/7, tqdm_2) |
| 备份文件 | `phase2_line_scores_v1_stale.json` 存在 (同大小, 时间戳 17:11) |

**结论：** 文件完整，33 实例齐全。189 个 segment 评分失败，2 个实例被排除（fastapi_3, fastapi_5），需要关注是否需要重跑。

---
