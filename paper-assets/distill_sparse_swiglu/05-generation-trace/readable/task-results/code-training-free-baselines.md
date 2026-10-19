# code training free baselines

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_training_free_baselines_20260515T171125_result.json`
- **Structured JSON:** [`a9706db1d5b75c8c1223.json`](../../sessions/a9/a9706db1d5b75c8c1223.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 全部通过。最终结果：

---

## 报告

### 1. Scoring Formulas（论文确认）

| 方法 | 公式 | 来源 |
|------|------|------|
| **Vanilla TEAL** | `score_j = mean(|act(gate(x))_j · up(x)_j|)` | Liu et al., ICLR 2025, arXiv 2408.14690 |
| **WINA** | `score_j = mean(|h_j|) · ‖W_down[:, j]‖₂` | Chen et al., arXiv 2505.19427 |
| **R-Sparse** | `score_j = mean(|h_j|) · Σ_{i<r} σ_i · |Vh[i,j]|` | Zhang et al., ICLR 2025, arXiv 2504.19449 |

三者共享 `h_j = act(gate(x))_j · up(x)_j` 的 calibration pass，区别在权重信息的利用方式。

### 2. 修改文件

**`/root/distill_sparse_swiglu/src/evaluate.py`**（原 284 行 → 403 行）

新增函数：
- `_collect_swiglu_magnitudes()` — 共享 calibration，收集 per-neuron 平均激活幅度
- `_global_topk_masks()` — 通用 global top-K 分配
- `vanilla_teal_global_masks()` — Vanilla TEAL（+ alias `teal_activation_magnitude_masks`）
- `wina_global_masks()` — WINA
- `rsparse_global_masks()` — R-Sparse
- `_print_mask_stats()` — 统一输出格式

CLI 新增参数：`--baseline_mode`（逗号分隔：`teal_vanilla,wina,rsparse`）、`--svd_rank`（默认 256）、`--checkpoint` 改为可选。

### 3. Dry-run 结果

```
vanilla TEAL: 32 layers, sparsity=0.498
WINA:         32 layers, sparsity=0.500
R-Sparse:    32 layers, sparsity=0.500

Mask diffs: TEAL-WINA=9917, TEAL-RSparse=78849, WINA-RSparse=76894
ALL DRY-RUN TESTS PASSED
```

三组 mask 两两不同，R-Sparse 与另外两个差异最大（SVD 权重信息的影响），符合预期。

### 4. 已知局限

- **R-Sparse SVD 耗时**：对 32 层 `[4096, 14336]` 矩阵做 SVD，在 GPU 上约需数分钟。`svd_rank` 参数控制截断秩，但 `torch.linalg.svd` 仍计算完整分解
- **Calibration 数据**：dry-run 使用随机 token，正式评估需用 WikiText-103 calibration 数据（`--use_random_data` 或默认 WikiText）
- **GPU 内存**：SVD 在 float32 下运行，单层峰值约 ~500MB 额外显存，逐层计算避免 OOM
- 备份文件 `evaluate.py.bak` 留在服务器上

---
