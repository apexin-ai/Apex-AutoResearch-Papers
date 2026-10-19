# code caclr training framework

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_caclr_training_framework_20260520T214641_result.json`
- **Structured JSON:** [`7ac618d2c3df2350536e.json`](../../sessions/7a/7ac618d2c3df2350536e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法正确。文件已创建：

**`code/train_caclr.py`** — 代码结构：

| 部分 | 内容 |
|------|------|
| **Loss 组件** | `bce_loss` / `sb_ece_loss`（Gaussian soft-binning ECE）/ `gaussian_rbf_kernel`（median heuristic）/ `mmd_loss`（unbiased MMD²） |
| **模型** | `CaCLRProbe(nn.Module)` — 单层 Linear，暴露 `predict_proba()` 返回 (N,2) 和 `decision_function()` 返回 (N,)，与 `transfer_eval.py` 兼容；`from_sklearn()` 从 sklearn LR 热启动 |
| **训练循环** | `train_caclr()` — sklearn LR 初始化 → Adam fine-tune，MMD 子采样 512 样本提效 |
| **CLI** | `--alpha_sweep` / `--beta_sweep` 网格搜索模式（英文 held-out 选最优后全量重训）；单次训练模式 |
| **输出** | `{"model": probe, "scaler": scaler, ...}` pickle，可被 `transfer_eval.py` 直接加载评估 |

---
