# code full pipeline rerun

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full-pipeline-rerun_20260514T083623_result.json`
- **Structured JSON:** [`d02b7a6e5af60f46d279.json`](../../sessions/d0/d02b7a6e5af60f46d279.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 执行完毕，汇报如下：

### SFT 文件

| 文件 | 行数 | 大小 | MD5 |
|------|------|------|-----|
| `sft_vanilla.jsonl` | 162 | 716,814 B | `0adbe32defd88e3c0f9061f6f4eebd45` |
| `sft_taxei.jsonl` | 164 | 719,492 B | `84d106779f93904ff91d4cb21bcd7735` |

行数和 MD5 均不同，taxei (164) > vanilla (162)，差值 = 2 条注入变体。

### 注入样本抽检

- 无 `&lt;injection_detected>` 标签
- 含真实 ALFWorld 环境观测（countertop, fridge 等物品描述）
- 含 `&lt;think>...&lt;/think>` + `&lt;action>...&lt;/action>` 格式
- 注意：因 `--dry_run` 模式，recovery 部分为 `[DRY_RUN] Would generate recovery reasoning/action here` 占位符。正式数据需去掉 `--dry_run` 调 API 生成真实 recovery

### 轨迹收集进度

| 指标 | 值 |
|------|-----|
| 成功轨迹 | 162 条 |
| 失败轨迹 | 47 条 |
| 目标 | 500 条 |
| PID 11045 | 仍在运行（已运行 1h55m） |
| 完成率 | 162/500 = 32.4% |

收集进程正常运行中，当前轨迹已从 161 增长到 162。

---
