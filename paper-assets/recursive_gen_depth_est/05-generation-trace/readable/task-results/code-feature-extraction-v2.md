# code feature extraction v2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_feature-extraction-v2_20260514T114749_result.json`
- **Structured JSON:** [`bdba3974c191f43fa54a.json`](../../sessions/bd/bdba3974c191f43fa54a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 产出

| 脚本 | 路径 | 状态 |
|------|------|------|
| `extract_features.py` | `scripts/extract_features.py` | 语法 OK, argparse OK |
| `train_classifier.py` | `scripts/train_classifier.py` | 语法 OK, argparse OK |
| `run_evaluation.sh` | `scripts/run_evaluation.sh` | 已写入 + chmod +x |

**extract_features.py** — 加载各 depth jsonl，自动计算统一截断长度（各 depth token 中位数的最小值），用 frozen Qwen2.5-1.5B 提取 13 维特征（perplexity 统计 4 维 + surprisal 分布 4 维 + 词汇多样性 4 维 + token_count），输出 CSV。

**train_classifier.py** — 4 个分类器（Random baseline、Binary+Random baseline、Logistic Regression 4-class with 5-fold CV、Random Forest 4-class），输出 metrics.json + confusion_matrix.png + feature_importance.png，Pass/Fail 判定（acc>40% 且 auc_1v2>0.6）。

**run_evaluation.sh** — 串联两个脚本的一键评估流水线。

Pipeline 跑完 depth_0~3 数据后，`bash scripts/run_evaluation.sh` 即可执行。

---
