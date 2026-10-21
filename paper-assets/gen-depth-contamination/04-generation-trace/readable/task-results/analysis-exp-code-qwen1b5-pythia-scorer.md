# analysis exp code qwen1b5 pythia scorer

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_code_qwen1b5_pythia_scorer_20260519T065306_result.json`
- **Structured JSON:** [`7f6218e52ac7df617540.json`](../../sessions/7f/7f6218e52ac7df617540.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。分析总结：

## exp_code_qwen1b5_pythia_scorer 结果

**K\* = 2，与 Qwen self-scorer 一致，确认 Code domain K\*=2 是 scorer-independent。**

### AUC 对比（Qwen scorer → Pythia scorer）

| Pair | Qwen scorer | Pythia scorer | Δ |
|------|-------------|---------------|---|
| 0v1 | 0.9388 | 0.9076 | -0.031 |
| 1v2 | 0.7382 | 0.7197 | -0.019 |
| 2v3 | 0.5300 | 0.5308 | +0.001 |
| 3v4 | 0.5022 | 0.5236 | +0.021 |
| 4v5 | 0.5219 | 0.5084 | -0.014 |

Pythia 在 discriminable 区间（0v1, 1v2）AUC 略低 2~3%（Pythia 1.4B 特征提取能力稍弱于 Qwen 1.5B），但 K\* 边界处（1v2→2v3）的跳变完全一致：1v2 远高于 θ=0.6，2v3 远低于 θ。JSD 也呈相同模式，depth 2→3 处急剧坍缩（0.0358→0.0043）。

### 对 domain ceiling 理论的支撑

1. **Code K\*=2 text-intrinsic**：换 scorer 后 K\* 不变，排除 Qwen family bias 导致的虚高。
2. **与 arXiv 一致的 pattern**：arXiv LLaMA-8B/Mistral-7B cross-scorer 也确认 K\*=3 不变。跨域、跨 scorer 验证均通过。
3. **Domain complexity hierarchy 稳固**：C4/Code K\*=2 < arXiv K\*=3，这个排序不受 scorer 选择影响，是文本本身结构复杂度的反映。

---
