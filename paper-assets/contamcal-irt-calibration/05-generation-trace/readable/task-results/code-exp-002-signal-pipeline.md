# code exp 002 signal pipeline

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-002-signal-pipeline_20260513T173246_result.json`
- **Structured JSON:** [`545bc7e3c90f43b6e34f.json`](../../sessions/54/545bc7e3c90f43b6e34f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

8 个文件全部就位，编译和 `--help` 验证通过（torch 缺失仅因本地环境无 GPU 依赖，服务器上有）。

产出清单：

| 文件 | 功能 |
|---|---|
| `compute_signals.py` | 主入口，编排 4 个信号计算并输出合并 JSON |
| `signal_embedding.py` | S1: sentence-transformers + FAISS 近重复检索，输出 max cosine sim |
| `signal_minkpp.py` | S2: Min-K%++ MIA，target vs reference z-score 归一化 |
| `signal_constat.py` | S3: ConStat 原始/改写准确率差（直接用 exp-001 结果，无需推理） |
| `signal_selfcritique.py` | S4: 自我批判 YES/NO entropy，低 entropy = 高 memorization 嫌疑 |
| `aggregate_rrf.py` | RRF 聚合 (k=60) + rank averaging + single-signal ablation + AUC matrix |
| `run_exp002.sh` | 遍历全部 exp-001 checkpoint，`--phase signals/aggregate/all` |
| `requirements.txt` | 额外依赖：faiss-gpu, sentence-transformers, scikit-learn |

---
