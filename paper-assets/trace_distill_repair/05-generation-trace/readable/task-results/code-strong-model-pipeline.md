# code strong model pipeline

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_strong_model_pipeline_20260515T154807_result.json`
- **Structured JSON:** [`348562ad68c91115a0d2.json`](../../sessions/34/348562ad68c91115a0d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`/root/trace_distill_repair/run_phase3_repair_v3_strong.py` 已部署（784 行），语法验证通过。

**与 v2 的关键差异：**

| 项目 | v2 | v3 |
|------|----|----|
| 默认模型 | `deepseek/deepseek-v4-flash` | `anthropic/claude-sonnet-4`（可通过 `REPAIR_MODEL` 环境变量覆盖） |
| 实例列表 | 4 个（TARGET_INSTANCES 硬编码） | 全部 14 个 Tier 1 实例 |
| API read timeout | 120s | **180s** |
| API 客户端 | 通过 `MVPPipeline._get_repair_client()` | 独立创建 `OpenAI` 客户端，不依赖 Pipeline 内部方法 |
| diff 提取 | 简单 markdown 剥离 | `extract_diff_from_response()` — 更鲁棒，处理 Claude 可能的前后解释文本 |
| Oracle baseline | 仅遍历 `TARGET_INSTANCES` | 遍历 `args.instances`（与实际运行实例一致） |
| 输出文件 | `phase3_v2_*.json/csv` | `phase3_v3_*.json/csv` |
| 启动日志 | 无 | 打印模型名、实例数、条件数 |

---
