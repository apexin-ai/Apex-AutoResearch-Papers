# research m1 prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_m1-prep_20260513T190440_result.json`
- **Structured JSON:** [`319f07f43739255e91aa.json`](../../sessions/31/319f07f43739255e91aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案已写入 `memory.md`。核心要点：

**提交命令**：`python -m pacs.profiling.run_profiling` + 6 个参数，推荐用 nohup 后台执行防 SSH 断连。

**资源估算**：单 GPU ~55-75 分钟，峰值显存 ~20-22GB，96GB 单卡足够，不需要多 GPU。

**关键风险**：模型下载未完成、代码 bug 未修完（已知），SSH 断连（用 nohup 防护）。降级方案：减 max_new_tokens 到 1024 可将时间减半。

---
