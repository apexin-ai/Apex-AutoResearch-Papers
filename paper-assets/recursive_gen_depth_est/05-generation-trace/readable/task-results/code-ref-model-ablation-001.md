# code ref model ablation 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ref_model_ablation_001_20260516T074944_result.json`
- **Structured JSON:** [`15f43fa4d9bd8cf1a7ff.json`](../../sessions/15/15f43fa4d9bd8cf1a7ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，结果总结：

## ref_model_ablation_001 结果

| Reference Model | Type | 5-fold CV Accuracy |
|---|---|---|
| **Pythia-1.4B** | self-model (generator = ref) | 78.55% ± 0.59% |
| **OLMo-1B** | cross-model (generator ≠ ref) | 74.51% ± 0.73% |

**Delta: 4.04 pp < 5pp 阈值 → Reference model choice is ROBUST**

关键论证价值：
- 换用完全不同架构的 OLMo-1B 作为 reference model，分类准确率仅下降 4pp
- ��明 depth signal 不是 self-model bias 的产物，而是 text 本身的内在属性
- 直接堵住 "你的方法只因为 generator 和 detector 是同一模型才 work" 这个审稿攻击向量

---
