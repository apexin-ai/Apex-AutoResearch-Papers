# code pythia 10k qwen phase2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pythia_10k_qwen_phase2_20260522T223905_result.json`
- **Structured JSON:** [`dfa4349a525eab3d5023.json`](../../sessions/df/dfa4349a525eab3d5023.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Pythia 10K Qwen Cross-Scoring Phase 2 已经完成。** 日志确认：

- Phase 1（generation + self-features）完成后，Phase 2 于 21:35 启动
- 使用 Qwen2.5-1.5B-Instruct 作为 scorer（`/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B-Instruct`）
- 跳过生成（`Skipping generation (steps 2-3)`），仅做 feature extraction + evaluation
- 于 22:12 完成

## Pythia 10K Qwen-Scored 结果

| Pair | AUC (mean) | Folds |
|------|-----------|-------|
| 0v1 | **0.9712** ± 0.0028 | [0.9753, 0.9691, 0.9700, 0.9678, 0.9737] |
| 1v2 | **0.6175** ± 0.0036 | [0.6140, 0.6216, 0.6198, 0.6125, 0.6195] |
| 2v3 | 0.5364 ± 0.0094 | [0.5541, 0.5331, 0.5285, 0.5371, 0.5291] |
| 3v4 | 0.5134 ± 0.0066 | |
| 4v5 | 0.5088 ± 0.0094 | |

**K\* = 2**（θ=0.60，1v2=0.6175 > 0.60，2v3=0.5364 < 0.60）

## 与 5K Qwen-Scored 对比

| | 5K | 10K |
|--|-----|------|
| 1v2 AUC | 0.6074 | 0.6175 |
| K\* | 2 | 2 |

**一致。** 10K 的 1v2 AUC（0.6175）略高于 5K（0.6074），K\* 判定均为 2，与 D107 scorer 统一决策一致。无需重新运行。

---
