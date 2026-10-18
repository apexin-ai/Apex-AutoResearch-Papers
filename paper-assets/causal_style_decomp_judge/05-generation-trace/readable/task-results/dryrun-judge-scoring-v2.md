# dryrun judge scoring v2

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_dryrun_judge_scoring_v2_20260520T121704_result.json`
- **Structured JSON:** [`5e92eee17d01051ee348.json`](../../sessions/5e/5e92eee17d01051ee348.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry run 完成，结果汇总：

| 项目 | 状态 |
|------|------|
| API 连通性 | **通过** — `http://47.94.22.126/v1` 可达，`gpt-4o` 在模型列表中 |
| 认证 | **通过** — API key 有效，9 次请求全部 200 OK |
| 评分解析 | **通过** — 所有评分均为 1-10 整数 |
| identity transform 一致性 | **基本符合预期** — mvp_0000 (5/5/5) 和 mvp_0001 (9/9/9) 三个评分完全一致；mvp_0002 orig=6, cf=6, dr=5 有 1 分偏差 |
| 延迟 | 每次 API 调用约 8-10 秒（endpoint 响应较慢） |

---
