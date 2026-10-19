# prep plan005 analysis script

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_plan005-analysis-script_20260515T010617_result.json`
- **Structured JSON:** [`fc0421151e3753a7a671.json`](../../sessions/fc/fc0421151e3753a7a671.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

### 脚本状态
- **实际路径**：`/root/structfuse/evaluation/analyze_stratified.py`（1308 行，完整可用）
- **功能**：覆盖 Plan 005 所有 5+2 维度：repo_size, pool_size, similarity, dataflow, neg_difficulty + pool_size_controlled + dataflow×pool_size 交叉分析
- **已有产出**：`stratified_dryrun_v4`（今天 05:06 生成），刚重新验证生成了 `stratified_dryrun_v5`

### 现在就能跑的（0 GPU）
| 步骤 | 状态 |
|------|------|
| `--dry-run` 全流程（mock predictions） | ✅ 已验证通过，21秒完成 |
| 数据分层标签生成（5 维度 bin assignment） | ✅ dry-run 中已含 |
| cross_tabulation（dataflow × pool_size） | ✅ 产出中有 |
| bootstrap CI 计算 | ✅ 用 mock 数据验证了 |
| 分层统计摘要 CSV + PDF 图 | ✅ 三个文件均已生成 |
| confound 分析（`scripts/analyze_confound.py`） | ✅ 16秒完成，report 已存 |
| BM25 overlap stratified 分析 | ✅ 20秒完成 |

### 必须等 M2 checkpoint 的步骤
| 步骤 | 依赖 |
|------|------|
| 真实模型 embedding 编码 | 需 `--checkpoints-dir` 中的 M2 权重 |
| 真实 R@1/R@5/MRR 计算 | 需真实 predictions |
| 正式 similarity bins（基于 cosine sim 而非 text overlap） | 需模型 encode |

### 数据就绪性
- M1 metadata: ✅ 44173 instances, 123 repos
- Val JSONL: ✅ 4 strategies × 3 seeds × 2980 samples
- Dataflow graph: ✅ 376069 file entries
- Confound analysis report: ✅ 已生成

**结论**：数据预处理和脚本验证已全部完成。dry-run pipeline 端到端通过。等 M2 checkpoint 就绪后，只需将 `--dry-run` 替换为 `--checkpoints-dir &lt;path>` 即可获得真实评估结果。

---
