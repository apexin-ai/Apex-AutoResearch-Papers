# ops disk cleanup cqa1

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_cqa1_20260517T195754_result.json`
- **Structured JSON:** [`7122ff49a253f2de4a1d.json`](../../sessions/71/7122ff49a253f2de4a1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整报告。

---

## 1. 总体磁盘状态 (df -h)

| 文件系统 | 大小 | 已用 | 可用 | 使用率 |
|---------|------|------|------|--------|
| / (overlay) | 30G | 7.4G | 23G | **25%** |
| /autodl-pub | 7.0T | 6.8T | 279G | **97%** |
| /autodl-pub/data | 4.0T | 2.6T | 1.5T | 65% |
| /dev/sda2 | 879G | 16G | 818G | 2% |

根分区压力不大(25%)。`/autodl-pub` 97% 但是共享盘，无法清理。

---

## 2. Top-20 大目录

### /root/autodl-tmp/ (仅 1 个项目)
```
1.2G    gen-depth-contamination
```

### gen-depth-contamination 内部 (按大小排序)
| 目录 | 大小 |
|------|------|
| data/ | 587M |
| data_exp022_cross_scorer/ | 94M |
| data_exp020_pythia_greedy/ | 39M |
| data_exp020_pythia_t07/ | 37M |
| data_exp020_pythia_nuc09/ | 36M |
| data_exp020_pythia_t12/ | 36M |
| data_exp016_qwen_base/ | 35M |
| data_exp019_mistral7b/ | 34M |
| logs/ | 22M |
| exp019.log | 13M |
| data_exp019b_mistral_cross/ | 8M |
| docs/ | 2M |
| artifacts/ | 1.2M |
| results/ | 1.1M |
| scripts/ | 288K |
| data_exp022_cross/ | 0 (symlinks) |

### data/ 子目录
| 目录 | 大小 |
|------|------|
| exp_009_dose_response | 109M |
| exp_021_length_512 | 46M |
| exp_wiki_olmo | 44M |
| exp_wiki_pythia | 40M |
| exp_wiki_llama8b | 38M |
| exp_wiki_mistral7b | 37M |
| exp_023_wiki | 35M |
| exp_008_retrain_chain | 32M |
| exp_021_length_256 | 33M |
| exp_018_llama8b | 33M |
| exp_021_length_128 | 24M |
| exp_arXiv_olmo | 19M |
| exp_arXiv_qwen7b | 19M |
| exp_024_arxiv | 18M |
| exp_025_pythia_arxiv | 18M |
| exp_arXiv_llama8b | 18M |
| exp_arXiv_mistral7b | 17M |
| exp_wiki_qwen7b | 15M |

### HuggingFace cache (/root/.cache/huggingface): 1.3G
| 内容 | 大小 |
|------|------|
| models--sentence-transformers--all-MiniLM-L6-v2 | 862M |
| datasets--cais--mmlu | 55M |
| datasets--Rowan--hellaswag | 36M |

---

## 3. 清理候选列表

### 类别 A: depth_1~5.jsonl (已有 features.csv 的实验)

所有已完成实验都有 features.csv，depth_1~5.jsonl 是中间生成文本，可从 depth_0 + 模型重新生成。

| 目录 | depth_1~5 估计大小 | 安全等级 | 原因 |
|------|-------------------|----------|------|
| data_exp016_qwen_base/ | ~29M | 中 | features.csv 已存在 |
| data_exp019_mistral7b/ | ~28M | 中 | features.csv 已存在 |
| data_exp020_pythia_greedy/ | ~32M | 中 | features.csv 已存在 |
| data_exp020_pythia_nuc09/ | ~30M | 中 | features.csv 已存在 |
| data_exp020_pythia_t07/ | ~31M | 中 | features.csv 已存在 |
| data_exp020_pythia_t12/ | ~30M | 中 | features.csv 已存在 |
| data/exp_008_retrain_chain/ | ~26M | 中 | features.csv 已存在 |
| data/exp_018_llama8b/ | ~27M | 中 | features.csv 已存在 |
| data/exp_021_length_128/ | ~20M | 中 | features.csv 已存在 |
| data/exp_021_length_256/ | ~27M | 中 | features.csv 已存在 |
| data/exp_021_length_512/ | ~38M | 中 | features.csv 已存在 |
| data/exp_023_wiki/ | ~29M | 中 | features.csv 已存在 |
| data/exp_024_arxiv/ | ~15M | 中 | features.csv 已存在 |
| data/exp_025_pythia_arxiv/ | ~15M | 中 | features.csv 已存在 |
| data/exp_arXiv_* (4 dirs) | ~60M | 中 | features.csv 已存在 |
| data/exp_wiki_llama8b/ | ~32M | 中 | features.csv 已存在 |
| data/exp_wiki_mistral7b/ | ~31M | 中 | features.csv 已存在 |
| data/exp_wiki_olmo/ | ~37M | 中 | features.csv 已存在 |
| data/exp_wiki_pythia/ | ~33M | 中 | features.csv 已存在 |
| **小计** | **~570M** | | |

### 类别 B: 日志文件

| 文件/目录 | 大小 | 安全等级 | 原因 |
|----------|------|----------|------|
| exp019.log (项目根) | 13M | **高** | 独立日志，实验已完成 |
| logs/ 目录 | 22M | **高** | 历史实验日志 |
| **小计** | **35M** | | |

### 类别 C: 空文件 / 零值目录

| 文件/目录 | 大小 | 安全等级 | 原因 |
|----------|------|----------|------|
| data_exp019b_mistral_cross/depth_*.jsonl (6个) | 0 bytes | **高** | 全部 0 字节空文件 |
| data_exp022_cross/ | 0 (symlinks) | **高** | 仅含指向 data_exp016 的 symlinks，无实际数据 |

### 类别 D: 缓存

| 文件/目录 | 大小 | 安全等级 | 原因 |
|----------|------|----------|------|
| scripts/__pycache__/ | 12K | **高** | Python 缓存，自动重建 |
| ~/.cache/huggingface/hub/datasets--* | 91M | 中 | mmlu+hellaswag 评测集，可重新下载 |
| ~/.cache/huggingface/hub/models--sentence-transformers | 862M | **低** | 可能仍用于特征提取，需确认 |

### 不可清理 (绝对不删)

| 目录 | 大小 | 原因 |
|------|------|------|
| data/exp_wiki_qwen7b/ | 15M | **可能正在运行**（仅 depth_0~2，未完成） |
| 所有 features.csv | ~散布 | 分析结果，必须保留 |
| 所有 results/、results_exp*/ | ~1.5M | 实验结论数据 |
| data_exp022_cross_scorer/ | 94M | 含 features.csv，cross-scorer 分析数据 |
| depth_0.jsonl (各实验) | ~散布 | 种子数据，不可再生 |

---

## 4. 预估可回收空间

| 清理级别 | 目标 | 可回收 |
|---------|------|--------|
| 保守（仅高安全等级） | 日志 + 空文件 + __pycache__ | **~35M** |
| 中度（+ depth_1~5.jsonl） | 上述 + 所有已完成实验的 depth_1~5 | **~605M** |
| 激进（+ HF cache） | 上述 + HF 评测数据集缓存 | **~700M** |
| 最大（+ sentence-transformers） | 上述 + sentence-transformers 模型 | **~1.5G** |

**结论**：根分区仅用 25%，无紧急压力。如需腾空间，中度清理(删 depth_1~5.jsonl + 日志)可回收 ~600M，是性价比最高的选择。sentence-transformers 模型(862M)清理前需确认是否仍用于特征提取流水线。

---
