# ssh untrained timestep accuracy

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_untrained-timestep-accuracy_20260515T190533_result.json`
- **Structured JSON:** [`e53190554004469dee24.json`](../../sessions/e5/e53190554004469dee24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。

## 结果：Untrained VLA Per-Timestep Goal Classification Accuracy

**Layer 1（best layer），所有 10 个 bin 均为 100.0% accuracy。**

| Bin | Range | Trained VLA | DINO | **Untrained VLA** |
|-----|-------|-------------|------|--------------------|
| 0 | [0.0, 0.1) | 100% | 43.3% | **100%** |
| 1 | [0.1, 0.2) | 100% | — | 100% |
| 2 | [0.2, 0.3) | 100% | — | 100% |
| 3 | [0.3, 0.4) | 100% | — | 100% |
| 4 | [0.4, 0.5) | 100% | — | 100% |
| 5 | [0.5, 0.6) | 100% | — | 100% |
| 6 | [0.6, 0.7) | 100% | — | 100% |
| 7 | [0.7, 0.8) | 100% | — | 100% |
| 8 | [0.8, 0.9) | 100% | — | 100% |
| 9 | [0.9, 1.0] | 100% | — | 100% |

### 核心结论

**Untrained VLA bin 0 = 100%**，与 Trained VLA 相同，远高于 DINO 的 43.3%。

这意味着 **language grounding 来自 LLM 预训练而非 VLA action 训练**——核心 claim 成立。未经 action 训练的 VLA（仅有 LLM 预训练权重）已经能在所有 timestep 上完美区分不同 goal，说明 language-conditioned goal representation 是 LLM backbone 带来的，不是 robot data finetuning 学到的。

JSON 已保存至 `/root/autodl-tmp/vla-ssd/results/untrained_libero_goal/goal_classification/timestep_accuracy.json`。

---
