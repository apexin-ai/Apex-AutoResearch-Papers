# check d065 server status 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d065_server_status_21461_20260520T092418_result.json`
- **Structured JSON:** [`efe481919eeb4a6d6227.json`](../../sessions/ef/efe481919eeb4a6d6227.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## d065 实验状态汇总

### Unconstrained (unc) — 已完成
- **文件**: `/root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_unc_4096.jsonl`
- **行数**: 998/998（完整）
- **结果**: success=930, fail=68
- **完成时间**: May 20 17:03 CST

### Constrained (con) — 仍在运行
- **文件**: `/root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_con_4096.jsonl`
- **当前行数**: 132 行（JSONL 可能在缓冲写入）
- **日志进度**: 823/998（82.4%）
- **每样本耗时**: ~10-20s（FAIL 样本 ~77s）
- **剩余**: 175 样本，预计 ~45 分钟完成（约 CST 18:10-18:20）

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 18,919 / 97,887 MiB | 83% |
| 1 | 18,919 / 97,887 MiB | 85% |

### d066 beam sweep — 已完成
SciERC beam sweep（beam 1/2/4/8 × unc/con）全部完成，评估 JSON 已生成。DocRED beam sweep 也有产出（beam4 × 200 样本 + beam1 unc）。

### 注意
con JSONL 只有 132 行但日志显示 823/998，可能是输出缓冲未 flush 或前一次中断的残留行数、当前 run 在 append。任务完成后 JSONL 应为 998 行。

---
