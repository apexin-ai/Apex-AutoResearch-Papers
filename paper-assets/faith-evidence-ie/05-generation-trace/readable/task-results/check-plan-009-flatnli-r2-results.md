# check plan 009 flatnli r2 results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_plan_009_flatnli_r2_results_20260515T203004_result.json`
- **Structured JSON:** [`d71724d4f92b1cafe1a0.json`](../../sessions/d7/d71724d4f92b1cafe1a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
实际完成状态: 失败

Checkpoint 评估结果:
  checkpoint-20: OOM killed (exit -9), inference 仅完成 2% (1/62 batches), 输出目录为空
  checkpoint-40: 同样 OOM killed, inference 阶段日志截断, 输出目录为空
  checkpoint-60: 未执行 (脚本在 checkpoint-40 挂掉后终止)
  checkpoint-80: 未执行
  checkpoint-100: 未执行

缺失 checkpoints: 全部 5 个 (20, 40, 60, 80, 100)
```

**原因**: `--no-quantize` + `batch_size 16` + `max_new_tokens 1024` 在单张 RTX 5090 (32GB) 上 OOM。日志显示只用了 device 0，虽然机器有 4 张卡。

**修复选项**:
1. 降 batch_size（如 4 或 2）
2. 去掉 `--no-quantize` 改用 4-bit 量化
3. 用多卡分摊显存

需要我用哪种方式重跑？

---
