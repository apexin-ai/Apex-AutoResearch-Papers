# code exp002 signal pipeline

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002_signal_pipeline_20260514T032305_result.json`
- **Structured JSON:** [`8f9a8dfa5d1344c6df01.json`](../../sessions/8f/8f9a8dfa5d1344c6df01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成。结果：

| 模块 | 状态 | 说明 |
|------|------|------|
| **embedding** | PASS | s1_embedding=0.3293 |
| **minkpp** | FAIL → **已修复** | bfloat16→numpy bug，已加 `.float()` |
| **constat** | PASS | s3_constat=0.0000（同文件对比，符合预期） |
| **selfcritique** | PASS | s4_selfcritique=-0.6803 |
| **merge** | PASS | 输出 keys 正确：`[index, benchmark, s1_embedding, s2_minkpp, s3_constat, s4_selfcritique]` |

minkpp 的 bfloat16 bug 已在 dry-run 进行中修复（`signal_minkpp.py:77` 加了 `.float()`）。

**产出汇总：**

1. **6 个文件部署在** `/root/contamcal-irt-calibration/exp002/`：
   - `signal_embedding.py` — Embedding near-duplicate retrieval (FAISS)
   - `signal_minkpp.py` — Min-K%++ membership inference（已修 bfloat16 bug）
   - `signal_constat.py` — ConStat performance gap
   - `signal_selfcritique.py` — Self-Critique entropy collapse
   - `compute_signals.py` — 主编排脚本（支持 `--dry-run --max-items`）
   - `aggregate_rrf.py` — RRF 聚合 + ablation baselines

2. **新增功能**：所有 4 个信号模块 + 主脚本支持 `--dry-run`/`--max-items` 参数

3. **依赖**：全部已安装（sentence-transformers 5.4.1, faiss-cpu 1.13.2, sklearn 1.8.0）

4. **sentence-transformers 模型** `all-mpnet-base-v2` 已缓存到服务器

---
