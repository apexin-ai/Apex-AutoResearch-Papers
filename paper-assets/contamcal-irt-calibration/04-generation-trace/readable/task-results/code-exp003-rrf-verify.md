# code exp003 rrf verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp003-rrf-verify_20260514T092902_result.json`
- **Structured JSON:** [`0d95fbbffdeedab036b9.json`](../../sessions/0d/0d95fbbffdeedab036b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RRF 代码验证结果

### 1. 脚本状态: 就绪

`/root/contamcal-irt-calibration/exp002/aggregate_rrf.py` 存在（7657B, 今天 09:47 更新），代码完整，有 `main()` + argparse。注意：没有独立的 `exp003/` 目录，RRF 聚合代码直接在 `exp002/` 下。

### 2. 输入输出约定

**输入** (`--signal-files`):
- `compute_signals.py` 输出的 JSON 文件，格式为 list of dicts，每个 dict 含 `index`, `benchmark`, `s1_embedding`, `s2_minkpp`, `s3_constat`, `s4_selfcritique`
- 文件名模式: `signals_merged_{benchmark}_{model_id}.json` 或单独的 `signal_{name}_{benchmark}_{model_id}.json`

**输出** (`--output-dir`):
- `rrf_scores_{model_name}.json` — list of `{"index", "benchmark", "rrf_score", "rank_s1_embedding", ...}`
- `rank_avg_scores_{model_name}.json` — 消融用
- `single_signal_scores_{model_name}.json` — 消融用
- `signal_auc_{model_name}.json` — 可选（需 `--labels-file`）

**运行命令**:
```bash
python aggregate_rrf.py --signal-files &lt;merged_signals.json> --output-dir &lt;dir> --model-name &lt;name> [--k 60] [--labels-file &lt;labels.json>]
```

### 3. 格式 GAP — 需要填补

exp-006 的 `load_exposure_scores()` 期望的输入格式:
```json
{"mmlu": [0.023, 0.015, ...], "gsm8k": [0.042, ...]}
```
即 `{benchmark_name: [per_item_tau_floats]}`

但 `aggregate_rrf.py` 输出的是:
```json
[{"index": 0, "benchmark": "mmlu", "rrf_score": 0.023, ...}, ...]
```
即 flat list of per-item dicts。

**缺一个格式转换步骤**：将 aggregate_rrf 的 per-item RRF scores 按 benchmark 分组，提取 `rrf_score` 值组成 per-benchmark 数组，输出为 exp-006 期望的 `{bench: [float]}` JSON。

这个转换很简单（~15 行 Python），可以加在 `aggregate_rrf.py` 的 `main()` 末尾作为额外输出，或写一个独立的小脚本。

### 结论

| 项目 | 状态 |
|------|------|
| RRF 核心代码 | 就绪 |
| 消融变体 (rank avg, single signal) | 就绪 |
| Signal AUC 矩阵 | 就绪（需 labels） |
| 导入无误 | 未验证（ssh_read_only 禁止 python -c 带分号） |
| **RRF → exp-006 格式转换** | **缺失，需补** |

---
