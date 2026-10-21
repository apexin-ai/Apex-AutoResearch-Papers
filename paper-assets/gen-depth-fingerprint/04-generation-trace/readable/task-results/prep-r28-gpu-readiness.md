# prep r28 gpu readiness

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_r28-gpu-readiness_20260520T054116_result.json`
- **Structured JSON:** [`5db909b47a7b3558a95e.json`](../../sessions/5d/5db909b47a7b3558a95e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

框架脚本已创建。以下是三个方向的就绪状态报告：

---

## R28 补实验预准备状态

### 1. Scale (7B+) — ✅ 就绪

| 项目 | 状态 |
|------|------|
| Qwen3-8B-Base 模型 | 已下载，`/root/autodl-tmp/models/Qwen/Qwen3-8B-Base/Qwen/Qwen3-8B-Base/`，16GB，5 shards 完整 |
| plan-014 生成数据 | 已存在，`/root/gen-depth-fingerprint/data/qwen3-8b/generations.jsonl`，4.9MB / 4497 行 |
| 磁盘空间 | `/root/autodl-tmp/` 剩余 63GB，充足 |

**下一步**：直接跑 feature extraction + 分类实验即可，无需额外准备。

### 2. TOST extra seeds — ⚠️ 需少量改造

| 项目 | 状态 |
|------|------|
| 现有脚本 | `scripts/tost_equivalence.py`、`scripts/tost_per_generator.py`、`tost_multi_margin.py` |
| seed 参数 | **不支持** — 三个脚本均为纯参数化 TOST（基于 t 分布），无随机性，无 `--n_seeds` 参数 |
| 已有 seed 稳定性脚本 | `scripts/multi_seed_stability.py` — 但仅针对 XGBoost LOGO F1（5 seeds），不涉及 TOST |

**改造评估**：约 20-30 行代码。在现有 TOST 脚本外加 bootstrap resampling 层（带 `--n_bootstrap` / `--seed` 参数），对 TOST p-value 计算 bootstrap CI。改造量小。

### 3. DDR causality — 🆕 框架已创建

| 项目 | 状态 |
|------|------|
| 现有脚本 | 无（无 causal/granger/intervention 相关文件） |
| 相关资源 | `scripts/lofo_ablation.py`（LOFO 消融）、`plot_appendix_ddr_trends.py`（DDR 趋势图）可复用 |
| 框架脚本 | 已创建 `scripts/ddr_causal_analysis.py`，含 4 个模块 stub：feature intervention、permutation importance、Granger causality、mediation analysis |

**下一步**：Worker 填充 4 个 `TODO` 函数实现。数据格式已对齐 `features_8gen.csv`（columns: model_name, seed_id, depth, 7 features）。优先实现 permutation importance（最直接、reviewer 最容易接受）和 Granger causality（因果性论证最强）。

---
