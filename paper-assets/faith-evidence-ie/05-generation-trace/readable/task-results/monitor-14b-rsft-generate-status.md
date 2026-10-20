# monitor 14b rsft generate status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_14b_rsft_generate_status_20260521T091137_result.json`
- **Structured JSON:** [`70a5955093892ca840c6.json`](../../sessions/70/70a5955093892ca840c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

14B RSFT pipeline 全部 4/5 阶段完成：

| 阶段 | 状态 | 关键数据 |
|------|------|----------|
| Generation | ✅ | 3027 docs, 24216 outputs, format 100%, diversity 7.28/8 |
| CED Scoring | ✅ | 3015 selected (top-k=1), combined mean=0.768 |
| RSFT Training | ✅ | 3 epochs, loss=0.500, token_acc=0.878, checkpoint-1131 |
| Eval no-evidence | ✅ | **F1=55.36, ign_F1=54.32**, format_ok=96.8% |
| Eval with-evidence | ❌ | 未执行 |

**下一步**: 需要运行 with-evidence eval 获取 evi_f1_joint 和 EDCR 指标，然后与 14B SFT baseline 汇总对比。

---
