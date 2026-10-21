# diagnose eval sft rasp 20 full

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_sft_rasp_20_full_20260517T012539_result.json`
- **Structured JSON:** [`e7e5c5e183cc7ef24bbb.json`](../../sessions/e7/e7e5c5e183cc7ef24bbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估**正常完成**，无任何 error/traceback。

**日志路径**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_20_full.log`

**关键结果**:
- **Accuracy: 61.56% (812/1319)**，95% CI ± 1.34%
- EOS rate: 98.41% (natural_eos=1298, truncated=21)
- 平均生成长度: 210.95 tokens
- 总耗时: ~2h53m
- 结果 JSON: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_20_full_n1319.json`

**日志末尾关键行**:
```
2026-05-17 09:22:53,824 [INFO] GSM8K Accuracy: 0.6156 ± 0.0134 (812/1319)
2026-05-17 09:22:53,837 [INFO] Results saved to .../eval_sft_rasp_20_full_n1319.json
```

进程正常退出，只是没有写 sentinel 文件导致 cron 误判为异常。N=100 预估 57% → 全量 61.56%，略有上升。

---
