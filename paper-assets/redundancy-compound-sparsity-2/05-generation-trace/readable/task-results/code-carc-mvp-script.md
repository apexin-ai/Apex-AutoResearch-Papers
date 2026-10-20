# code carc mvp script

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_carc_mvp_script_20260512T081925_result.json`
- **Structured JSON:** [`272099eb9516438f467e.json`](../../sessions/27/272099eb9516438f467e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件全部完成并注册。

**产出清单：**

| 文件 | 路径 | 说明 |
|------|------|------|
| `carc_utils.py` | `artifacts/carc_utils.py` | 共享工具：`EMAAnchorManager`（variance-aware α + EMA anchor 更新）、`WelfordVariance`、`sparsify()`、`compute_perturbation()`、`threshold_from_histogram()`、`load_eval_data()` |
| `carc_calibrate.py` | `artifacts/carc_calibrate.py` | 校准脚本：hook gate/up/down_proj 输入，收集绝对值 histogram（1000 bins），从 CDF 插值计算 40%/55% 阈值，输出 JSON |
| `carc_mvp.py` | `artifacts/carc_mvp.py` | MVP 验证：3 pass（baseline / sparse@55% / sparse@40%），per-token per-layer 收集 (S_score, perturbation)，计算 Pearson/Spearman 相关性 + perturbation_diff，输出 2×2 判定 |

**关键设计点：**
- EMA 在 k_proj/v_proj 输出（pre-RoPE）上计算，避免位置编码干扰内容相似度判断
- 校准 histogram 用首 batch 确定 range（1.2× max），后续 outlier 归入末 bin，对 40%/55% 低百分位阈值无影响
- MVP 的 sparsified pass 对所有层同时施加 sparsity，per-layer perturbation 包含级联效应（更接近实际部署）
- KV capture 只在 baseline pass 激活，避免 sparsified pass 覆盖 baseline K/V
- 所有中间张量及时 `.cpu()` 释放 GPU 显存

---
