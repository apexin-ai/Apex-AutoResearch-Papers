# ops olmo2 rerun status collect

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_olmo2-rerun-status-collect_20260521T144828_result.json`
- **Structured JSON:** [`1251daa8fbe896476f1a.json`](../../sessions/12/1251daa8fbe896476f1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**OLMo-2 eval rerun 状态：进行中**

- **PID 531623**: 运行中，已 22 分钟
- **GPU 3**: 95% 利用率，16.7GB / 97.9GB 显存
- **当前进度**: d005 MMLU 评估中 (8756/14042 = 62%)，~17 it/s

### 已完成结果

| Dosage | MMLU (%) | ARC (%) |
|--------|----------|---------|
| d000   | **53.79** | **76.11** |
| d005   | 进行中 (62%) | 未开始 |
| d025   | 未开始 | 未开始 |
| d050   | 未开始 | 未开始 |
| d100   | 未开始 | 未开始 |

**d000 MMLU = 53.79%，与论文 53.79% 完全一致。** evaluate.py md5 已记录在 log 中 (17673bf3...)，lora_alpha=32 确认。

按当前速度，d005 MMLU 剩余 ~5300 items ÷ 17 it/s ≈ 5 分钟完成。全部 10 个 eval（5 dosage × 2 benchmark）估计还需 ~2-3 小时。

---
