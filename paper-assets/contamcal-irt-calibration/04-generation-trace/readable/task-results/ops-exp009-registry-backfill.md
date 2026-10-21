# ops exp009 registry backfill

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp009_registry_backfill_20260517T104501_result.json`
- **Structured JSON:** [`1fae2eb609e045a1813d.json`](../../sessions/1f/1fae2eb609e045a1813d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry补全完成。

## 已补建的 Registry Entries (8 条)

### Eval (4 条)

| exp_id | Model | Status | Metrics |
|--------|-------|--------|---------|
| `exp_009_05b_instruct_eval` | Qwen2.5-0.5B-Instruct | DONE/success | MMLU 0.343, ARC 0.500, GSM8K 0.388 |
| `exp_009_15b_instruct_eval` | Qwen2.5-1.5B-Instruct | DONE/success | MMLU 0.577, ARC 0.765, GSM8K 0.593 |
| `exp_009_3b_instruct_eval` | Qwen2.5-3B-Instruct | DONE/success | MMLU 0.605, ARC 0.811, GSM8K 0.760 |
| `exp_009_deepseek_eval` | DeepSeek-R1-Distill-Qwen-1.5B | DONE/**negative** | MMLU 0.229, ARC 0.226 (broken), GSM8K 0.608 |

### Signals (4 条)

| exp_id | Model | Status | Coverage |
|--------|-------|--------|----------|
| `exp_009_05b_instruct_signals` | Qwen2.5-0.5B-Instruct | DONE/success | s1+s2+s4+merged × 3 benchmarks |
| `exp_009_15b_instruct_signals` | Qwen2.5-1.5B-Instruct | DONE/success | s1+s2+s4+merged × 3 benchmarks |
| `exp_009_3b_instruct_signals` | Qwen2.5-3B-Instruct | DONE/success | s1+s2+s4+merged × 3 benchmarks |
| `exp_009_deepseek_signals` | DeepSeek-R1-Distill-Qwen-1.5B | DONE/success | s1+s2+s4+merged × 3 benchmarks |

## 未完成/异常项

- **DeepSeek MMLU/ARC eval 无效**: 所有预测都�� "A"，accuracy 低于 random (0.229/0.226)。已标记 `conclusion=negative`。仅 GSM8K (0.608) 可用于 IRT。Director 已决定排除 MMLU/ARC。
- **数据重复**: 0.5B/1.5B-Instruct 信号同时存在�� `exp002/signals/` (旧格式) 和 `exp009/signals/` (新格式)。Registry 指向 exp009 作为 canonical。

---
