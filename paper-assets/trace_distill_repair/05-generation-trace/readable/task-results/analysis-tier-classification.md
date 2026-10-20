# analysis tier classification

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tier_classification_20260515T122736_result.json`
- **Structured JSON:** [`4a401d611789d3d47d4d.json`](../../sessions/4a/4a401d611789d3d47d4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| Tier | 数量 | 实例 |
|------|------|------|
| **Tier 1** | 15 | black_1, cookiecutter_{1,2,3}, fastapi_{1,2}, luigi_5, sanic_2, scrapy_{2,7}, tornado_2, youtube-dl_{1,2,5,20} |
| **Tier 2** | 0 | — |
| **Tier 3** | 18 | httpie_{1,2}, luigi_{1,2,10,14}, sanic_1, scrapy_{1,3,4}, thefuck_{1,2,4}, tornado_{1,4,5,7}, youtube-dl_10 |

文件已写入 `/root/trace_distill_repair/pipeline_output/instance_tiers.json`。Tier 2 为空——所有有 structural signal 的实例都能成功提取 buggy code，直接进入 Tier 1。Tier 3 的 18 个实例 structural_keep=0，与 no_trace 条件无差别。

---
