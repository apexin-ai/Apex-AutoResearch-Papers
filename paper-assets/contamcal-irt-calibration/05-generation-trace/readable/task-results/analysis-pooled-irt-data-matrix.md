# analysis pooled irt data matrix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pooled-irt-data-matrix_20260515T120014_result.json`
- **Structured JSON:** [`9936228170246947abb3.json`](../../sessions/99/9936228170246947abb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总结果

### 总体数据

| 类别 | 数量 |
|------|------|
| 总 eval 目录（有结果） | 52 |
| 非 deprecated | 48 |
| **Aligned + 非 deprecated（主矩阵）** | **35**（去重后，去掉 3B_d000_v2_s42_para_aligned 的 v2/v3 重复） |
| 仍在运行/失败的空目录 | 9 |

### 按 Benchmark 可用 N

| Benchmark | Aligned 可用 N | IRT 可用 N（排除约束后） |
|-----------|---------------|------------------------|
| **MMLU** | 35 | **25**（排除 0.5B 的 12 条，D045 position bias；保留 0.5B-Instruct） |
| **GSM8K** | 35 | **22**（排除 d000 的 13 条，D044 format confound） |
| **ARC** | **0** | 0 |
| **HumanEval** | **0** | 0 |

### N≥16 判断

- **MMLU**: N=25 ✅ 达标
- **GSM8K**: N=22 ✅ 达标
- **ARC**: N=0 ❌ 完全缺失——没有任何 config 跑过 ARC
- **HumanEval**: N=0 ❌ 完全缺失——没有任何 config 跑过 HumanEval

### 按 model_scale 分布（aligned, non-deprecated, 去重）

| Scale | N | 含 para |
|-------|---|---------|
| 0.5B | 12 | 4 para |
| 0.5B-Instruct | 1 | 0 |
| 1.5B | 10 | 4 para |
| 3B | 12 | 5 para |

### 缺口列表

**空目录（eval 未完成或失败）:**
- `Qwen2.5-0.5B_base_pretrained` / `_aligned` — 空
- `Qwen2.5-1.5B_d005_s123_aligned` — 空
- `Qwen2.5-1.5B_d025_s123_aligned` — 空
- `Qwen2.5-3B_d000_s123_aligned` — 空
- `Qwen2.5-3B_d000_v3_s42_aligned` — 空
- `Qwen2.5-3B_d005_s42_aligned` — 仅有 eval.log（可能正在运行）

**结构性缺口:**
- 1.5B 缺 s123 seed 的 d005/d025 aligned（目录存在但空）
- 3B d005 缺非 para 的 aligned（deprecated 版本已废弃，新版仅有 para）
- 3B d025 缺 seed 标注（`d025_v2_aligned` 无 seed）

**关键问题: ARC 和 HumanEval 完全没有评测结果，如果 pooled IRT 需要这两个 benchmark，需要补跑全部 config 的 ARC/HumanEval eval。**

CSV 已保存至服务器 `/root/autodl-tmp/exp001/eval_summary_matrix.csv`，包含 35 条主矩阵行（aligned, non-deprecated, 去重）。

---
