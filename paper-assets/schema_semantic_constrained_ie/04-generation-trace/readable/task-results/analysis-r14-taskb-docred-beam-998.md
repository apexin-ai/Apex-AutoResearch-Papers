# analysis r14 taskB docred beam 998

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_taskB_docred_beam_998_20260520T201641_result.json`
- **Structured JSON:** [`5ad95270e7ff0b3c3757.json`](../../sessions/5a/5ad95270e7ff0b3c3757.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3/998 docs 已完成。推理正在稳定进行。根据之前 beam=4 实验的经验（~20-40s/doc），预计总时间 6-11 小时。

任务已启动，状态总结：

- **实验 ID**: `r14_qwen_docred_beam4_998`
- **服务器**: westd-21461, GPU 0 (RTX PRO 6000 Blackwell, 98GB)
- **配置**: Qwen3-8B ZS, beam=4, full_s1, max_new_tokens=4096, 998 docs
- **输出**: `/root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.jsonl`
- **日志**: `/root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.log`
- **进度**: 3/998 (刚启动)
- **预计完成**: ~6-11 小时后

监控命令：
- 进度: `wc -l /root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.jsonl`
- 评估: `cd /root/schema_semantic_constrained_ie && python3 scripts/eval_d064.py --dataset docred --pred_file /root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.jsonl`

---
