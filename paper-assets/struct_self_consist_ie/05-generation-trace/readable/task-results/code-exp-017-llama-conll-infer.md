# code exp 017 llama conll infer

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_017_llama_conll_infer_20260514T173127_result.json`
- **Structured JSON:** [`1f7989f5efefe1aab34d.json`](../../sessions/1f/1f7989f5efefe1aab34d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理正在运行。vLLM 已成功加载模型（14.99 GiB），正在渲染 3453 个 prompts（已到 79%）。

汇总：

| 步骤 | 状态 |
|------|------|
| LoRA merge | 完成（15GB，4 shards） |
| Registry `exp_017_llama_conll_infer` | RUNNING |
| 推理任务 PID | 98661 |
| 日志路径 | `output/exp_017_llama_conll_infer.log` |
| 输出目录 | `output/exp_017_llama_conll_infer/` |
| 数据 | CoNLL-2003 NER, 3453 test, N=8, T=1.0 |

模型加载正常，prompt 渲染速度 ~550 it/s，接下来进入 vLLM 批量推理阶段。可稍后用 `tail` 查看日志跟踪进度。

---
