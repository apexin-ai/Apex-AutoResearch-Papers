# ops d066 llama scierc beam2 unc 551

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d066_llama_scierc_beam2_unc_551_20260520T141357_result.json`
- **Structured JSON:** [`e17fc97f355ea0d36601.json`](../../sessions/e1/e17fc97f355ea0d36601.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动完成。

**汇报：**
- **PID**: 213203 @ westd-21461 GPU1
- **状态**: RUNNING，GPU1 占用 18.4 GB / 89% utilization，模型已加载并在推理
- **数据路径**: `data/processed_data/test.json` — **100 docs**（SciERC test set）
- **输出**: `/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam2_unconstrained.jsonl`
- **Cron 监控已注册**

**⚠️ 数据量修正**: 任务描述说 551 docs，实际 SciERC test set 是 **100 docs**（train=350, dev=50, test=100）。已有的 beam1 unc 输出是 275 行（100 docs 的多行输出，非 275 个 doc）。数据路径 `data/processed_data/test.json` 确认是正确的 test set。

---
