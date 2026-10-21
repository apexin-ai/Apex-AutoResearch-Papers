# analysis 5paired bootstrap prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_5paired-bootstrap-prep_20260512T131741_result.json`
- **Structured JSON:** [`1a42b76167f664c876a1.json`](../../sessions/1a/1a42b76167f664c876a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### 已部署到服务器 `/home/sonny/exec-sim-repair-verifier/`

**1. `analysis_5paired_bootstrap.py`** — 主分析脚本
- 接受 N 对 CLS/CWM predictions 文件 (`--pairs CLS1 CWM1 CLS2 CWM2 ...`)
- 按 `problem_id` 聚类重采样（114 个 problem clusters，平均每 cluster 16.6 个 variants）
- 输出：mean diff、95% CI、bootstrap SE、TOST 等价检验（±2pp）
- 支持 JSONL 和 JSON array 两种格式，自动识别 `pred`/`prediction` 字段

**2. `extract_predictions_generic.py`** — 通用 predictions 提取
- 支持 `--mode cls` 和 `--mode cwm`
- 从任意 LoRA checkpoint 提取 per-sample predictions

### 已生成的 predictions 文件
| 文件 | 来源 | Acc |
|------|------|-----|
| `predictions_cls_seed42.jsonl` | 从 `eval_results_bf16_predictions.json` 转换 | 87.51% |
| `predictions_cls_seed0.jsonl` | 已有 | 87.78% |
| `predictions_cwm_seed123.jsonl` | 刚从 `checkpoints_cwm_seed123/best` 提取 | 87.30% |

### Dry-run 结果（2 pairs, preliminary）
```
Mean diff (CLS − CWM):  +0.344pp
95% CI:                  [-0.733, +1.413]pp
TOST ±2pp:               Equivalent (p=0.001)
Min equiv margin:        1.210pp
```

### 待办：补齐 5 pairs
缺少的 predictions 需用 `extract_predictions_generic.py` 提取：
- CLS seed=789 — 需要找到对应 checkpoint（服务器上未看到 `checkpoints_cls_seed789/`）
- CWM seed=42 — 需要找到对应 checkpoint
- CWM seed=456 — 需要找到对应 checkpoint
- CWM seed=789, seed=0 — 等训练完成后提取

---
