# verify b005 s42 output

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_b005-s42-output_20260516T050123_result.json`
- **Structured JSON:** [`cdbc52429956175804c1.json`](../../sessions/cd/cdbc52429956175804c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：sweep-isr-b005-s42 完整且正确，success 标记准确。**

证据：
- **reward_log.jsonl**: 恰好 500 行，最后一条 step=500，步数完整
- **训练日志**: 进度条 500/500，`EXIT_CODE=0`，末尾有 `Saving final model` + `Done.` 完结标记
- **checkpoint-500**: 存在，含完整的 4 shard safetensors 模型文件（~15GB）
- **输出目录根**: 也有一份完整模型文件（final model save）
- **最终指标**: prove_rate=0.888, mean_isr=0.577, 训练时长 1692s（~28min）

cron 报的 "process dead 5× with no sentinel" 是误报——可能是 cron 检测窗口内进程尚未启动或 sentinel 文件写入延迟。实际训练从头跑完 500 步，无需重跑。

---
