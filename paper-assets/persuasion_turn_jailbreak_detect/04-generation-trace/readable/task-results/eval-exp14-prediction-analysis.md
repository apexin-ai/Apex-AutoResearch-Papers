# eval exp14 prediction analysis

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp14-prediction-analysis_20260519T081359_result.json`
- **Structured JSON:** [`25a3f8bf13bb2764cc61.json`](../../sessions/25/25a3f8bf13bb2764cc61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常清晰。以下是完整分析：

## exp14 Prediction Distribution 分析

### Confusion Matrix — exp14 (Llama all), DD Full

| | Pred Benign | Pred Jailbreak |
|--|------------|---------------|
| **True Benign (Llama)** | | |
| vanilla | TN=35.3 | FP=14.7 |
| jb_mlm | TN=6.0 | FP=44.0 |
| 9class | TN=5.0 | FP=45.0 |
| **True Jailbreak (Llama)** | | |
| vanilla | FN=50.0 | TP=0.0 |
| jb_mlm | FN=16.0 | TP=34.0 |
| 9class | FN=0.0 | TP=50.0 |

### Confusion Matrix — exp14b (Llama JB + Qwen benign), DD Full

| | Pred Benign | Pred Jailbreak |
|--|------------|---------------|
| **True Benign (Qwen)** | | |
| vanilla | TN=38.0 | FP=0.0 |
| jb_mlm | TN=37.7 | FP=0.3 |
| 9class | TN=38.0 | FP=0.0 |
| **True Jailbreak (Llama)** | | |
| vanilla | FN=50.0 | TP=0.0 |
| jb_mlm | FN=16.0 | TP=34.0 |
| 9class | FN=0.0 | TP=50.0 |

### 对比摘要 — DD Full (exp14/exp14b)

| 指标 | vanilla | jb_mlm | 9class |
|------|---------|--------|--------|
| FP rate (full) | **29.3% / 0.0%** | **88.0% / 0.9%** | **90.0% / 0.0%** |
| FP rate (k3) | 35.3% / 0.0% | 100.0% / 0.9% | 97.3% / 0.0% |
| FP rate (k1) | 61.3% / 1.8% | 100.0% / 7.0% | 99.3% / 0.0% |
| TP rate (full) | 0.0% / 0.0% | 68.0% / 68.0% | **100.0% / 100.0%** |
| TP rate (k3) | 0.0% / 0.0% | 100.0% / 100.0% | 96.0% / 96.0% |
| TP rate (k1) | 2.0% / 2.0% | 99.3% / 99.3% | 88.7% / 88.7% |

### 结论

**1. F1 崩溃 100% 来自 FP rate 爆炸，不是 jailbreak 检测失败。**

- **TP rate 在 exp14 和 exp14b 中完全一致**（同样的 jailbreak 数据，同样的检测率）。jailbreak 检测能力完全跨 LLM 可迁移。
- **FP rate 是唯一差异**：Llama benign 被 88-100% 误判为 jailbreak（jb_mlm/9class），Qwen benign 几乎 0% 被误判。

**2. 失败机制：detector 学到了 "Llama style = jailbreak"。**

- 训练集中 jailbreak 全部来自 Qwen 生成，benign 也来自 Qwen。模型隐式学到了：non-Qwen 文本风格 → jailbreak。
- 当 Llama benign 出现时，其风格与训练集 benign（Qwen）不同，触发 jailbreak 预测。
- Qwen benign（exp14b）保持同域，FP 接近 0。

**3. vanilla 模型情况特殊：**

- vanilla 完全无法检测 jailbreak（TP=0），FP 也相对低 → 它实际上什么都没学到，偏向预测 benign，但 Llama 文本的 stylistic shift 反而让它预测 jailbreak（FP 29-61%）。

**4. 9class 是最极端的案例：**

- DD Full: TP=100%, FP on Llama benign=90% → 把所有 Llama 文本都判为 jailbreak
- 换成 Qwen benign 后: TP=100%, FP=0% → F1 直接 1.000

结果文件已保存：
- `/root/persuasion_turn_jailbreak_detect/results/exp14_prediction_analysis.json`
- `/root/persuasion_turn_jailbreak_detect/results/exp14_confusion_summary.txt`

---
