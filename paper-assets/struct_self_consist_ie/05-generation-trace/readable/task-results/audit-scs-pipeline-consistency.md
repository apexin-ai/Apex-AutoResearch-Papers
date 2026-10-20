# audit scs pipeline consistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_scs_pipeline_consistency_20260518T030739_result.json`
- **Structured JSON:** [`2386bc88936d3d0a76e0.json`](../../sessions/23/2386bc88936d3d0a76e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核查完毕。以下是完整报告。

---

## Pipeline 一致性核查报告

### 根因确认

**5-epoch baseline 使用了 `max_tokens=512` 的旧推理输出，而 3-epoch 和 10-epoch 使用了 `max_tokens=1024` 的当前默认值。** 这是唯一的 pipeline 不一致点，直接解释了 4pp 的非单调 dip。

### 证据链

| 参数 | 3-epoch (029a) | 5-epoch (baseline实际使用) | 10-epoch (029b) | 一致? |
|------|---------------|-------------------|----------------|-------|
| N samples | 8 | 8 | 8 | ✅ |
| Temperature | 1.0 | 1.0 | 1.0 | ✅ |
| top_p | default (1.0) | default (1.0) | default (1.0) | ✅ |
| **max_tokens** | **1024** (current default) | **512** (old default) | **1024** (current default) | ❌ **不一致** |
| 推理引擎 | vLLM | vLLM | vLLM | ✅ |
| 推理脚本 | run_mvp_pilot.py | 旧版 run_mvp_pilot.py | run_mvp_pilot.py | ⚠️ 不同代码版本 |
| 评估脚本 | 03_analyze_fixed.py | 03_analyze_fixed.py (动态计算) | 03_analyze.py (同逻辑) | ✅ |
| Gold-filter 逻辑 | gold_nonempty (529/551) | gold_nonempty (529/551) | gold_nonempty (529/551) | ✅ |
| 实例数 | 551 | 551 | 551 | ✅ |
| LoRA rank | 32 | 32 | 32 | ✅ |
| LoRA alpha | 64 | 64 | 64 | ✅ |
| 训练数据 | scierc_uie_train | scierc_uie_train | scierc_uie_train | ✅ |
| 训练 seed | 42 | 42 | 42 | ✅ |
| Greedy F1 (当前) | 0.6501 | **0.6094** | 0.6467 | ❌ 非单调 |
| Greedy F1 (修正后) | 0.6501 | **0.6439** | 0.6467 | ✅ 合理 |

### 数据溯源

- **5-epoch baseline 使用的文件**: `output/exp_012_logprob/samples_with_logprobs.jsonl` (May 14, 3.3MB)
  - 在 `comparison.json` 中被标记为 `"exp_012_old_max512"`
  - 无 run.log，无 top-level logprobs 数组
  
- **5-epoch 正确版本**: `output/exp_012_rerun_1024/samples.jsonl` (May 15, 3.8MB)
  - 在 `comparison.json` 中被标记为 `"exp_012_rerun_max1024"`
  - 有 run.log，确认模型为 `qwen3-8b-scierc-merged-v2`，vLLM v0.18.1
  - 有 top-level logprobs 数组（与 029a/029b 结构一致）

### 修正后的 ablation curve

```
当前 (有 bug):  3ep=0.6501  5ep=0.6094  10ep=0.6467  (5ep dip = 4.1pp)
修正后:         3ep=0.6501  5ep=0.6439  10ep=0.6467  (差异仅 0.6pp, 合理)
```

### 结论

**Pipeline 不完全一致。** `03_analyze_fixed.py` 误用了旧推理输出 (`exp_012_logprob`, max_tokens=512) 作为 5-epoch baseline，而非使用参数一致的重跑版本 (`exp_012_rerun_1024`, max_tokens=1024)。

**修复方案**: 将 `03_analyze_fixed.py` 的 `BASELINE_PATH` 从 `exp_012_logprob/samples_with_logprobs.jsonl` 改为 `exp_012_rerun_1024/samples.jsonl`，然后重跑分析。修正后 5-epoch greedy F1 从 0.6094 升至 0.6439，非单调 dip 从 4.1pp 降至 0.6pp（在正常随机波动范围内）。

---
