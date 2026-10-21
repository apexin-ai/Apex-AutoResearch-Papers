# ops yi gate check eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_yi-gate-check-eval_20260522T190749_result.json`
- **Structured JSON:** [`bba3896c167be1254976.json`](../../sessions/bb/bba3896c167be1254976.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态总结：**

- **实验** `eval_yi15_9b_pretrained_mmlu` 已在 cqa1-21977 cuda:0 上运行
- **PID**: 724094 (python 子进程 724099, 17658 MiB VRAM)
- **进度**: ~17 it/s, 14042 items, 预计 ~13 分钟完成
- **离线模式**: `HF_DATASETS_OFFLINE=1` 成功使用本地 MMLU 缓存
- **日志**: `/tmp/eval_yi_pretrained_mmlu.log`
- **输出**: `/root/contamcal-irt-calibration/results/yi_pretrained_mmlu/`

**C009 注意**: evaluate.py 37978 bytes ≠ westd reference 37591 bytes。此结果仅用于独立 gate check（65-70% vulnerability band 判断），不与跨服务器数据混用。如后续需要纳入 IRT 分析，需同步到统一版本重跑。

---
