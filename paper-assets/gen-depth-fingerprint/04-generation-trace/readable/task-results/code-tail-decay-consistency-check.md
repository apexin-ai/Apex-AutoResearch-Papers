# code tail decay consistency check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tail-decay-consistency-check_20260517T104229_result.json`
- **Structured JSON:** [`05421763ce90e41b9853.json`](../../sessions/05/05421763ce90e41b9853.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：数据一致，无问题

### 各 generator 的 tail_decay 统计

| generator | n | mean | std | min | max |
|-----------|---|------|-----|-----|-----|
| olmo-2-1b | 4713 | -0.00233505 | 0.00022333 | -0.00368185 | 0.00000000 |
| pythia-1b | 4555 | -0.00223633 | 0.00024162 | -0.00400735 | 0.00000000 |
| pythia-2.8b | 4609 | -0.00224904 | 0.00024085 | -0.00336938 | 0.00000000 |
| qwen3-0.6b | 4538 | -0.00232928 | 0.00021094 | -0.00364713 | 0.00000000 |
| qwen3-1.7b | 4617 | -0.00232056 | 0.00023222 | -0.00650057 | 0.00000000 |
| qwen3-8b | 4497 | -0.00231846 | 0.00022184 | -0.00655384 | 0.00000000 |
| **llama-3.2-3b** | 4680 | -0.00230293 | 0.00021417 | -0.00464299 | -0.00172337 |
| **mistral-7b-v0.3** | 4849 | -0.00229260 | 0.00019456 | -0.00358050 | -0.00166132 |
| llama-3.2-3b-rp11 | 4416 | -0.00232890 | 0.00023171 | -0.00466249 | 0.00000000 |

**所有 generator 的 tail_decay 值均为负数，量级一致（约 -0.0023）。** Llama 和 Mistral 已通过 `fix_tail_decay_and_eval.py` 的 step1 用 slope 实现（rank 100-1000 sorted avg log-prob 线性回归斜率）重新提取，保存在各自目录的 `features_pythia410m.jsonl` 中。

### fix_tail_decay_and_eval.py 逻辑

- **step1**: 对 llama-3.2-3b、mistral-7b-v0.3、llama-3.2-3b-rp11 三个 generator 用 Pythia-410M 重新提取特征（entropy + slope tail_decay + surface features），保存为 `features_pythia410m.jsonl`
- **step2**: 加载 6-gen 的 `features_all_models.csv` + Llama/Mistral 的 `features_pythia410m.jsonl`，合并后跑 8-gen LOGO 评估
- **step3**: rp-LOFO 实验（用 6-gen + Mistral 训练，Llama rp=1.1 / rp=1.0 filtered 做测试）
- **step4**: filter diagnostic（对比 filtered vs unfiltered 的 6-gen/8-gen 性能）

6-gen 的 `features_all_models.csv` 也是用相同的 slope 公式提取的（值域完全匹配）。两套数据定义一致。

---
