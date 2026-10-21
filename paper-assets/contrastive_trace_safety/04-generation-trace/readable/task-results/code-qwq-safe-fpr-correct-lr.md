# code qwq safe fpr correct lr

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwq_safe_fpr_correct_lr_20260517T210912_result.json`
- **Structured JSON:** [`3a86b226e6a4f52bec9a.json`](../../sessions/3a/3a86b226e6a4f52bec9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果总结：

## QwQ-32B Safe-trace FPR（正确方法：LogisticRegression lbfgs）

| Method | CV Acc | Step-level FPR | Trace-level FPR (K=5) |
|--------|--------|----------------|----------------------|
| **HS L60 static** | 93.5% | 27.9% | 47.5% |
| **Text MiniLM** | 66.7% | 39.4% | 50.0% |

**结论**：

1. HS probe 的 FPR 确实很高（step 28%，trace 47.5%），用正确的 LogisticRegression 方法重算后比之前 SGDClassifier 的 50% 略好但本质相同——QwQ-32B 的 L60 hidden state probe 在 safe traces 上有严重的 false positive 问题。

2. HS probe 虽然 CV acc 高达 93.5%（在 jailbreak 内部的 pre/post-CP 分类很好），但泛化到 safe traces 时大量误判为 unsafe。

3. Text probe 更差：CV acc 仅 66.7%（连 jailbreak 内部分类都不行），safe trace FPR 也是 50%（等同随机）。

4. HS probe 优于 Text probe（step FPR 28% vs 39%），但两者的 trace-level FPR 都接近 50%，说明 QwQ-32B 的 safe trace representations 与 jailbreak pre-CP steps 确实存在系统性差异，probe 无法有效区分"safe trace 正常推理"和"jailbreak 正在 comply"。

结果已保存到 `artifacts/qwq_safe_fpr_correct_lr.json`。

---
