# analysis review p2f cross ref bias

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_review-p2f-cross-ref-bias_20260515T134152_result.json`
- **Structured JSON:** [`af4c9a3c7ae52e76e3bb.json`](../../sessions/af/af4c9a3c7ae52e76e3bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `results/review_p2f_cross_ref_bias.json`。

**核心发现：Same-family bias 不成立。**

| Reference Model | Pythia-1B F1 | 其他4gen平均 | Pythia-1B偏差 | Pythia-1B排名 |
|----------------|-------------|-------------|--------------|--------------|
| Pythia-410M (同族) | 0.856 | 0.790 | +0.065 | **#1** |
| OLMo-2-1B (跨族) | 0.845 | 0.798 | +0.048 | **#1** |
| Qwen3-0.6B (跨族) | 0.848 | 0.808 | +0.041 | **#1** |

- Pythia-1B 在**所有三种** reference model 下都排名第一
- 同族→跨族 F1 下降仅 0.009（0.856→0.847），远在 CI 范围内
- Pythia-1B 的高可检测性是其生成模式的内在特征，不是 reference model 家族偏差

---
