# diagnose 14b no evi failure

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_14b-no-evi-failure_20260521T004242_result.json`
- **Structured JSON:** [`c968fa1ac789e6bd175b.json`](../../sessions/c9/c968fa1ac789e6bd175b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Eval 没有失败——它已成功完成。**

日志显示推理跑完了全部 247 batch（耗时 2h37m），结果已写入：

```
/root/autodl-tmp/eval_results/plan017_14b_rsft_no_evidence_eval/metrics.json
/root/autodl-tmp/eval_results/plan017_14b_rsft_no_evidence_eval/predictions.json
```

## 结果

| 指标 | 值 |
|------|-----|
| F1 | 0.5536 |
| Ign-F1 | 0.5432 |
| Evi-F1 | 0.0000 (预期，no-evidence 不输出 evidence) |
| Format OK | 953/985 (96.8%) |
| Truncated | 106/985 |

## 为什么看起来"失败"

输出目录路径不匹配：
- 你检查的路径：`/root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_no_evidence_eval/`
- 实际输出路径：`/root/autodl-tmp/eval_results/plan017_14b_rsft_no_evidence_eval/`

脚本用的是 `eval_results/` 而非 `eval_outputs/`。PID 55039 正常退出（进程完成后自然消失），cuda:2 空闲也符合预期。

**结论：eval 成功完成，无需重跑。**

---
