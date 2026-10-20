# ops llama rsft s44 pipeline

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama_rsft_s44_pipeline_20260520T010402_result.json`
- **Structured JSON:** [`c68add79eccf43c9b436.json`](../../sessions/c6/c68add79eccf43c9b436.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**汇总：**

| 项目 | 详情 |
|------|------|
| 脚本 | `/root/autodl-tmp/freige/scripts/seed_expansion/llama_rsft_s44_pipeline.sh` |
| tmux session | `llama_rsft_s44` |
| GPU | cuda:3（0 MiB → 已确认空闲） |
| 日志 | `/root/autodl-tmp/freige/logs/llama_rsft_s44_pipeline.log` |
| Registry | `llama_rsft_s44_pipeline` → RUNNING |
| 数据 | 复用 s42 CED-scored data（2952 samples），Method A |
| 流程 | Step 1: RSFT train (seed=44) → Step 2: D076 eval |
| 预估耗时 | 训练 ~50min + eval ~2.3h ≈ **3-4 小时** |

注意：任务描述中提议的 generation/CED scoring 步骤已跳过——现有 s42/s43 均复用同一份 CED-scored 数据（Method A），s44 保持一致。

---
