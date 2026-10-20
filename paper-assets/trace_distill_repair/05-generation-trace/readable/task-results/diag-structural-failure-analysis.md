# diag structural failure analysis

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_structural_failure_analysis_20260515T023340_result.json`
- **Structured JSON:** [`cc851f4ae11d3dfe9799.json`](../../sessions/cc/cc851f4ae11d3dfe9799.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果如下：

---

### Failure 类型分布

| 类型 | 数量 | 占比 |
|------|------|------|
| **PARSE_FAILURE** | 117 | 83.6% |
| **API_FAILURE_FALLBACK** | 23 | 16.4% |
| API_NONE | 0 | 0% |

### 关键发现

1. **PARSE_FAILURE 主因是 max_tokens 截断**：117 个 PARSE_FAILURE 中，111 个 (94.9%) 的 reasoning 不以 `}` 或 `"` 结尾，即 JSON 在生成中途被截断。样本显示典型的截断模式：reasoning 字段写到一半就断了（如 `"reasoning": "The trace segment shows a Modul"`）。

2. **API_FAILURE_FALLBACK 是 API None 重试耗尽**：日志中 160 次 "API returned None content" 警告，23 次 "All 3 attempts failed"。这 23 个 segment 在 3 次重试后仍返回 None，被标记为 API_FAILURE_FALLBACK。

3. **所有 140 个 error segment 的 confidence 均为 0.0**。

4. **33/38 个实例受影响**，只有 5 个实例零 failure。失败最多的：scrapy_2、tqdm_1、youtube-dl_1 各 10 个，youtube-dl_10 有 9 个。

### 结论

- **117/140 (83.6%) 确认与 max_tokens 截断相关**，和 line scoring 是同一个问题
- **23/140 (16.4%) 是 API 返回空内容**，与 max_tokens 无关，是 API 稳定性问题
- Reviewer 在中间检查点报告 0 PARSE_FAILURE 是因为当时处理的 batch 恰好没触发截断（或日志中不记录 PARSE_FAILURE 关键字——grep 确认日志中 0 次出现 "PARSE_FAILURE"，说明 PARSE_FAILURE 标签是解析时在代码中标注的，不写日志）

---
