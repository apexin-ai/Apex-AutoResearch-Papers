# ssh diagnose gemini deepseek errors

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_gemini_deepseek_errors_20260522T102615_result.json`
- **Structured JSON:** [`f42d07db655255afa391.json`](../../sessions/f4/f42d07db655255afa391.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### Part 1: Gemini/DeepSeek 错误原因

| Judge | 失败/总计 | 根因 | 当前状态 |
|-------|-----------|------|----------|
| Gemini | 394/855 (46%) | **输出截断** — 模型分析写太长，`[[A]]/[[B]]/[[C]]` 标签被截断掉，`_parse_verdict()` 返回 None | 最近条目（18:27+）正常 |
| DeepSeek | 189/638 (30%) | **空响应 + 500 错误** — 大量 `raw_output: ""` + 日志可见 `Error code: 500 - Internal Server Error` | 最近条目正常，偶发 500 重试后成功 |

**不是 402 残留**，是今天早期（12:25~17:00）proxy 不稳定导致的截断/空响应。proxy 现已恢复。

**证据**：
- Gemini 失败条目的 `raw_output` 有实质分析内容但中途断句，无 verdict tag
- DeepSeek 失败条目多数 `raw_output: ""`，少数有部分内容也截断
- 最近 1h 两个 judge 产出全部 status=ok

### Part 2: Auto-restart 配置问题

**严重配置缺陷**：所有 config 文件（llama/qwen/gemini/deepseek 全部）target_models 只有 3 个：

```yaml
target_models:
  - gpt-3.5-turbo-0125
  - gpt-4-0314
  - gpt-4-0613
```

但 responses 目录有 **10 个模型**：gpt-3.5-turbo-0125, gpt-4-0314, gpt-4-0613, gpt-4o, gpt-4o-mini, gpt-5.5, llama-3.3-70b, qwen2.5-72b, claude-opus-4.7, mistral-large-2

**结论**：auto-restart 启动的 judge-llama/judge-qwen **不会**评估 llama/qwen 作为 target model。它们只评估那 3 个 GPT 模型。

**Auto-restart 当前状态**：
- llama response 500/500 完成 → judge-llama 已启动（18:26:04）
- qwen response 496/500 → 还差 4 条，未触发

### 建议修复方案

1. **失败条目不需要手动修复**：`load_completed()` 跳过 failed 条目，重启 collect 进程即可自动重试

2. **必须更新 config 的 target_models**：将所有 config 中 target_models 改为完整的 10 个模型列表（或至少加上 gpt-4o, gpt-4o-mini, gpt-5.5, llama-3.3-70b, qwen2.5-72b, claude-opus-4.7, mistral-large-2）

3. **DeepSeek 偶发 500**：当前 retry 逻辑能处理（`max_retries: 3`），无需降 workers。但可考虑将 `max_tokens` 从 4096 提高到 8192 防止 Gemini 截断

---
