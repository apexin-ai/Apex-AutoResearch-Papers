# code entropy only degradation

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_entropy-only-degradation_20260516T221023_result.json`
- **Structured JSON:** [`a0c1d9e7a876c94422f1.json`](../../sessions/a0/a0c1d9e7a876c94422f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

**Entropy-only (5 features) vs 7-feature 退化对比：**

| Rate | Entropy Binary F1 | 7-feat Binary F1 | Entropy Multi F1 | 7-feat Multi F1 |
|------|-------------------|-------------------|-------------------|-----------------|
| 0% | **0.8325** | 0.6953 | 0.6875 | **0.7371** |
| 5% | 0.7380 | 0.6496 | 0.5389 | 0.6407 |
| 10% | 0.6670 | 0.6139 | 0.4270 | 0.4916 |
| 20% | 0.5690 | 0.5912 | 0.3139 | 0.3669 |

**Binary 退化斜率：**
- Entropy-only: -0.095 / -0.166 / **-0.264**
- 7-feature: -0.046 / -0.081 / -0.104

**结论：与预期相反。** Entropy-only 退化更严重（约 2.5× 大于 7-feature）。原因：随机词替换大幅改变 token 上下文，Pythia-410M 的 surprisal 对此极度敏感。相反，lexical features（ttr/hapax）虽然有 systematic bias，但作为 summary statistics 对噪声更稳定。

7-feature multiclass 在 20% 的 0.37 并非主要由 lexical artifact 导致，entropy-only 在 20% 甚至更低（0.31）。

结果已保存至 `/root/gen-depth-fingerprint/experiments/human_edit_robustness/entropy_only_degradation.json`。

---
