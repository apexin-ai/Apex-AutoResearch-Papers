# experiment wild3 problem perturbation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_wild3-problem-perturbation_20260520T080205_result.json`
- **Structured JSON:** [`ee8899b387d76733fbbc.json`](../../sessions/ee/ee8899b387d76733fbbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Wild 3 完成。

**结果**：

| Group | K | κ | Eff-K | SC Acc |
|---|---|---|---|---|
| Original-only | 4 | 0.5896 | 1.44 | 80.00% |
| Perturbed-only | 4 | 0.6962 | 1.30 | 76.67% |
| Mixed (Orig+Pert) | 8 | 0.6269 | 1.48 | 80.00% |

**关键发现**：
- κ(mixed) - κ(original) = **+0.037** — 混合原始+扰动 traces 后 κ 不降反升
- 仅 10% 的题目 majority answer 发生变化（3/30）
- 扰动版本 κ 更高（0.696 vs 0.590），说明名字替换+前提重排后模型反而更一致

**结论**：trace 相关性**主要来自模型偏置**，而非问题的表面形式。这支持论文中 κ≈0.44 反映了模型固有推理模式而非表层干扰的论点。

**注意**：因 Mistral-7B 与 Blackwell GPU 的 flashinfer 不兼容，实际使用 Qwen2.5-7B-Instruct（同 7B 级别）。服务器上的 intermediates 和 perturbation_data.json 已保存在 `results/wild3_perturbation/`。

---
