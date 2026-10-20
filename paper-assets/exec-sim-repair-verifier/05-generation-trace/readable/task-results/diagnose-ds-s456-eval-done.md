# diagnose ds s456 eval done

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ds-s456-eval-done_20260522T021402_result.json`
- **Structured JSON:** [`d0f51e22360f7f7b81e9.json`](../../sessions/d0/d0f51e22360f7f7b81e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。

---

## DS CWM s456 Eval 结果

**状态**: 成功完成（9784/9784 样本）

| Metric | DS s456 | DS s42 (baseline) | Delta |
|---|---|---|---|
| **Accuracy** | 56.11% | 61.49% | **-5.38pp** |
| **Unparseable rate** | 56.97% | 62.5% | -5.53pp |
| **Parseable-only acc** | 32.45% | 38.7% | **-6.25pp** |
| **F1-macro** | 50.60% | — | — |
| **Fail recall** | 41.99% | — | — |
| **Pass recall** | 61.35% | — | — |

**Confusion matrix**: TP=4379, FP=1535, FN=2759, TN=1111

**结论**: s456 在所有指标上均低于 s42 baseline，accuracy 差 5.38pp，parseable-only accuracy 差 6.25pp。不过 unparseable rate 略低（57.0% vs 62.5%），说明 s456 的格式遵循稍好但判断准确性更差。两个种子的 CWM 方法都低于 majority baseline（72.96%），跨种子鲁棒性存疑。

**Registry**: `deepseek-cwm-repo-s456-e3-eval` → DONE/success，metrics 已写入。Cron 已无需删除（不在当前 session）。

---
