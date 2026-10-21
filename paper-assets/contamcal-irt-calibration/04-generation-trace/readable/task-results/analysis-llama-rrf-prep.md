# analysis llama rrf prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_rrf_prep_20260516T193752_result.json`
- **Structured JSON:** [`ad2ca992cc533feae4e8.json`](../../sessions/ad/ad2ca992cc533feae4e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Llama-3.2-3B_d000_s42 Signals 状态

| Benchmark | s1_embedding | s2_minkpp | s4_selfcritique | signals_merged |
|-----------|:---:|:---:|:---:|:---:|
| ARC Challenge | ✅ | ✅ | ✅ | ✅ |
| GSM8K | ✅ | ✅ | ✅ | ✅ |
| MMLU | ✅ | ✅ | ⏳ 6/~14 chunks (43%) | ❌ |

MMLU s4_selfcritique 以 ~10min/chunk 速度推进，剩余 ~80min。

### exposure_scores.json 状态
- 已有 Llama-3.2-3B_d000_s42: **mmlu + arc_challenge** ✅
- **缺 gsm8k**（文件生成于 02:58，gsm8k merged 于 03:25 才完成）
- MMLU s4 完成后需**整体重新生成**

### RRF 脚本兼容性 (`exp003/rrf_aggregation.py`)
- ✅ `aggregate_all_models` 遍历所有 signal 目录，自动包含 Llama
- ✅ `generate_exposure_json` 完全通用
- ⚠️ `parse_model_dir` regex 硬编码 `Qwen2.5-` 模式 → Llama CSV 元数据显示 "unknown"（**不阻塞** IRT，仅影响 CSV）

### IRT 脚本兼容性 (`exp006/run_pooled_rrf_irt.py`)
- ✅ `DOSAGE_PATTERN` 正确匹配 `Llama-3.2-3B_d000_s42_aligned`
- ✅ `strip_aligned` + `resolve_rrf_key` 正确映射 eval→signal key
- ✅ `filter_models_for_benchmark` 优雅跳过无 RRF 数据的模型
- ⚠️ 默认 `--scales ["0.5B", "1.5B"]` 不含 3B，需传 `--scales 0.5B 1.5B 3B`

### 需要修改的代码
`parse_model_dir` 可选修复（不阻塞，仅优化 CSV 输出）。其余脚本**无需修改**即可兼容 Llama。

### Cross-family IRT 就绪路径

| 步骤 | 耗时 | 阻塞 |
|------|------|------|
| 1. 等 MMLU s4_selfcritique 完成 | ~80 min | ⏳ |
| 2. 合并 MMLU signals + 重新生成 exposure_scores.json | ~5 min | — |
| 3. 运行 `run_pooled_rrf_irt.py --scales 0.5B 1.5B 3B` | ~30 min/bench | — |
| **总计** | **~2.5h** | — |

### Eval Results
Llama 4 个 dosage 全部有 eval 结果（d000/d005/d025/d100 `_aligned`）。但只有 d000 有 signals，因此 cross-family IRT 中 Llama d005/d025/d100 将通过 `filter_models_for_benchmark` 被跳过（除非后续也计算它们的 signals）。

---
