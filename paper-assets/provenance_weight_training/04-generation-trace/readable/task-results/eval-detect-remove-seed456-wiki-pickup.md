# eval detect remove seed456 wiki pickup

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_detect_remove_seed456_wiki_pickup_20260522T142112_result.json`
- **Structured JSON:** [`1789097045edb48d014e.json`](../../sessions/17/1789097045edb48d014e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:3 占用 7.3GB，符合 fp32 模型大小。eval 正在跑。

**状态总结：**
- `detect_remove_q05_v2_seed456` 的 wiki eval 原始结果是 NaN/Infinity（fp16 精度溢出）
- 已在 cuda:3 上启动 fp32 重跑，PID=783753
- 预计 12-15 分钟完成
- 结果会写入 `/root/autodl-tmp/provenance_weight_training/output/eval_results/detect_remove_q05_v2_seed456/eval_wiki_fp32.json`

需要等完成后读取结果并更新 registry。要我过几分钟回来检查吗？

---
