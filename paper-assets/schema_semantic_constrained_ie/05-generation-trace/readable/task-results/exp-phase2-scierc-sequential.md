# exp phase2 scierc sequential

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_phase2_scierc_sequential_20260513T214939_result.json`
- **Structured JSON:** [`74b7b8aa466b143a6a8c.json`](../../sessions/74/74b7b8aa466b143a6a8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载完毕，grammar_only 实验 (551 samples) 正在推理中。

**状态汇总：**
- **PID**: 123425
- **GPU**: cuda:1（通过 `CUDA_VISIBLE_DEVICES=1`，脚本内用 `cuda:0`）
- **当前进度**: [1/3] grammar_only 正在运行
- **预估时间**: 每个实验约 1-1.5 小时，3 个实验共 3-5 小时
- **日志文件**: `/root/schema_semantic_constrained_ie/outputs/phase2_batch.log`

**监控命令**：
```bash
# 查进度
tail -5 /root/schema_semantic_constrained_ie/outputs/phase2_batch.log
# 查进程
ps -p 123425 -o pid,etime --no-headers
```

---
