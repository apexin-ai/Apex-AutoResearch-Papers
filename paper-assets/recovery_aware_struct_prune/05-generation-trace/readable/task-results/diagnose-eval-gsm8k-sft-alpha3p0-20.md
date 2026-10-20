# diagnose eval gsm8k sft alpha3p0 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_gsm8k_sft_alpha3p0_20_20260522T123726_result.json`
- **Structured JSON:** [`52f2a1ca1aa7474bbcc6.json`](../../sessions/52/52f2a1ca1aa7474bbcc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**实验成功完成。** Cron 误判。

| 项目 | 值 |
|------|-----|
| GSM8K Accuracy | **64.14% ± 1.32%** (846/1319) |
| EOS Rate | 98.79% (1303 natural, 16 truncated) |
| Avg Response Length | 188.63 tokens |
| 失败原因 | 无——评估全部完成，仅写结果 JSON 时磁盘满导致非零退出码 |

中间进度 (~64.15%@1300) 与最终结果一致，数据可靠。

Registry 已更新：补充了 metrics（含 stderr/eos_rate）、log_path、checkpoint_path、notes。conclusion 维持 `success`。

**Dose-response SFT 列现有数据**：α=0.5 → 60.73% | α=2.0 → 64.97% | α=3.0 → **64.14%** | α=4.0 → 61.94%。α=3.0 SFT 位于 α=2.0 和 α=4.0 之间，符合预期的非单调趋势。

---
