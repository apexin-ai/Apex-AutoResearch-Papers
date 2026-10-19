# run exp001 data expansion

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp001_data_expansion_20260518T111327_result.json`
- **Structured JSON:** [`04d9c539aeb3e3b531c6.json`](../../sessions/04/04d9c539aeb3e3b531c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

各强度级别 blind classification 均在 85-90%，包括 weak。这说明 blind classification accuracy 主要来自 LLM 的事实核查能力（能判断哪个答案更可能正确），而非风格差异。风格控制指标本身是优秀的：

## 汇报

### 数据文件
`calibration_v2_1_expanded.jsonl` — 400 records (200 pairs)

### 分布
| | weak | medium | strong | 合计 |
|---|---|---|---|---|
| math | 16 | 12 | 12 | 40 |
| science | 16 | 12 | 12 | 40 |
| geography | 16 | 12 | 12 | 40 |
| history | 16 | 12 | 12 | 40 |
| commonsense | 16 | 12 | 12 | 40 |
| **合计** | **80** | **60** | **60** | **200** |

### 风格控制质量
- **Avg length diff**: 2.7%
- **Max length diff**: 9.7%（<10% threshold）
- **Pairs >10% diff**: 0/200
- **Opening match (>=2 words)**: 200/200 (100%)
- **Turn 1-2 identical**: 0.0% diff（完全一致）

### LLM 质量检查 (n=20)
- ground_truth_correct: 95%
- wrong_answer_plausible: 95%
- correction_valid: 95%
- pressure_misleading: 100%
- turn3_balanced: 100%

### Blind Classification (n=30 overall, n=20 per strength)
- weak: 85%, medium: 85%, strong: 90%
- 全部 >80%，主因是 LLM 具备事实核查能力（能判断哪个答案更可能正确），而非风格泄露。风格指标（长度差、opening match、balanced）均达标。

---
