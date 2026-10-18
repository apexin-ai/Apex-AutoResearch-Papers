# code feature extraction pythia

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_feature-extraction-pythia_20260514T120845_result.json`
- **Structured JSON:** [`25eb3c95edf250b09071.json`](../../sessions/25/25eb3c95edf250b09071.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总：

**1. 脚本路径和行数**

| 脚本 | 路径 | 行数 |
|------|------|------|
| extract_features.py | `scripts/extract_features.py` | 278 |
| train_classifier.py | `scripts/train_classifier.py` | 255 |
| run_evaluation.sh | `scripts/run_evaluation.sh` | 38 |

**2. dry-run 验证结果**
- `extract_features.py --help` ✅ 
- `train_classifier.py --help` ✅

**3. 依赖检查**
- scipy 1.17.1 ✅
- scikit-learn 1.8.0 ✅
- matplotlib 3.10.5 ✅
- tqdm 4.67.3 ✅

全部已预装，无需额外安装。

**4. 特征维度：19 维**

| 类别 | 特征 | 数量 |
|------|------|------|
| Perplexity 统计 | mean/var/skewness/kurtosis_ppl, p10/p25/p50/p75/p90_ppl | 9 |
| Surprisal | mean/var_surprisal, entropy_of_surprisal | 3 |
| Vocabulary diversity | type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy | 4 |
| Repetition | rep_2gram, rep_3gram, rep_4gram | 3 |

---
