# ops check pythia code result

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-pythia-code-result_20260519T002403_result.json`
- **Structured JSON:** [`162032d275b676f7bc59.json`](../../sessions/16/162032d275b676f7bc59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron job，无需删除。

---

**exp_code_pythia1b4 实验完成，registry 已更新。结果摘要：**

| Depth Pair | AUC (mean ± std) | 5-Fold AUCs |
|---|---|---|
| 0 vs 1 | **0.9592 ± 0.0036** | 0.958, 0.958, 0.966, 0.960, 0.955 |
| 1 vs 2 | 0.5983 ± 0.0050 | 0.601, 0.588, 0.600, 0.600, 0.602 |
| 2 vs 3 | 0.5215 ± 0.0128 | 0.524, 0.512, 0.531, 0.502, 0.538 |
| 3 vs 4 | 0.5152 ± 0.0120 | 0.498, 0.533, 0.509, 0.512, 0.524 |
| 4 vs 5 | 0.5046 ± 0.0137 | 0.498, 0.482, 0.507, 0.522, 0.513 |

**K\* = 1**（θ=0.60），与预期的 K\*=2 不一致。1v2 AUC = 0.5983 极其接近阈值但未达到。Pythia-1.4B 在 Code domain 的深度饱和比 Qwen 更早（depth 1 即饱和），这暗示 K\* 可能与模型架构/预训练数据有关，而非纯粹的 domain 属性。

关键文件路径：
- 结果目录：`/root/autodl-tmp/gen-depth-contamination/results/exp_code_pythia1b4/`
- Features CSV：`/root/autodl-tmp/gen-depth-contamination/data/exp_code_pythia1b4/features.csv`
- 训练日志：`results/exp_code_pythia1b4/train.log`

---
