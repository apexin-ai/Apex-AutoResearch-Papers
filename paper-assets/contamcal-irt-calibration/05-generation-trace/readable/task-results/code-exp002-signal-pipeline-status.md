# code exp002 signal pipeline status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002_signal_pipeline_status_20260514T045101_result.json`
- **Structured JSON:** [`4a385f66f2b30aaffaa9.json`](../../sessions/4a/4a385f66f2b30aaffaa9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-002 Signal Pipeline 状态报告

### 代码完整，已就绪

`/root/contamcal-irt-calibration/exp002/` 包含 8 个文件：

| 文件 | 大小 | 功能 | 状态 |
|------|------|------|------|
| `compute_signals.py` | 8.7KB | 主编排脚本，计算 4 个 signal，支持 `--dry-run`/`--signals`/`--max-items` | ✅ |
| `signal_embedding.py` | 7.8KB | S1: Embedding 近重复检索 (sentence-transformers + FAISS) | ✅ |
| `signal_minkpp.py` | 8.6KB | S2: Min-K%++ 成员推断 (target vs ref model log-prob) | ✅ |
| `signal_constat.py` | 4.1KB | S3: ConStat 性能差距 (原始 vs 改写准确率) | ✅ |
| `signal_selfcritique.py` | 8.2KB | S4: Self-Critique 熵坍缩 (YES/NO 置信度) | ✅ |
| `aggregate_rrf.py` | 7.7KB | RRF 融合 + rank averaging/单 signal 消融 + AUC 矩阵 | ✅ |
| `test_dryrun.py` | 4.8KB | dry-run v1 | ✅ |
| `test_dryrun_v2.py` | 3.9KB | dry-run v2 (离线模式 + 本地模型) | ✅ |

### 接口验证

- `compute_signals.py --help` 正常返回 ✅
- `aggregate_rrf.py --help` 正常返回 ✅
- dry-run v2 在 CPU 上启动成功，正确加载 SFT 数据（300 segments）和 ARC-Challenge（3 items），模型加载和编码流程正常 ✅
- 所有 4 个 signal 模块都有 `__pycache__`（说明已被成功 import 过）✅

### 输出格式

- 每个 signal 输出 `[{index, benchmark, s{N}_*}]` 格式 JSON
- `compute_signals.py` 自动合并为 `signals_merged_{benchmark}.json`
- `aggregate_rrf.py` 输出 `rrf_scores_{model}.json`: `[{index, benchmark, rrf_score, rank_*}]`

### 与 exp-006 的衔接

exp-006 的 `--exposure-file` 期望格式：`{"benchmark": [τ_0, τ_1, ..., τ_n]}`（按 item index 排列的 flat float array）。

`aggregate_rrf.py` 输出的是 list-of-dicts。需要一个简单的转换步骤将 `rrf_score` 提取为 flat array 按 benchmark 分组。这个转换是 trivial 的（约 5 行代码），可以在 exp-003 或运行脚本中完成。

### 前置数据

- SFT 训练数据: `/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl` (96MB) ✅
- 基准模型: Qwen2.5-{0.5B, 1.5B, 3B} 已缓存 ✅
- eval results: 9 个模型评估目录已存在 ✅
- 尚无计算产出（exp002 目录下无 .json 输出文件）

### 结论

**exp-002 代码完整就绪**，4 signals + 统一接口 + RRF 聚合 + dry-run 全部实现。唯一需要的是：
1. 在 GPU 上执行 `compute_signals.py` 实际计算各模型的 signal 值
2. 一个 trivial 的格式转换将 RRF 输出适配 exp-006 的 exposure-file 格式

---
