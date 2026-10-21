# infra env setup sync

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env-setup-sync_20260513T174954_result.json`
- **Structured JSON:** [`c61a1935aa6de137c72e.json`](../../sessions/c6/c61a1935aa6de137c72e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 步完成。最终报告：

---

**服务器环境搭建完成 — westd-47453**

| 项目 | 状态 |
|------|------|
| **GPU** | 4× NVIDIA RTX PRO 6000 Blackwell Server Edition (94GB each) |
| **PyTorch** | 2.10.0+cu128, CUDA=True |
| **transformers** | 4.57.6 |
| **datasets** | 4.8.4 |
| **accelerate** | 1.13.0 |
| **lm_eval** | 0.4.11 |
| **wandb** | 0.26.0 |

| 模型 | 路径 | 参数量 |
|------|------|--------|
| **Qwen3-0.6B** | `/root/provenance_weight_training/models/Qwen/Qwen3-0.6B` | 596.0M |
| **ModernBERT-base** | `/root/provenance_weight_training/models/modernbert/` (HF cache) | 149.6M |

| 代码文件 | 大小 | 状态 |
|----------|------|------|
| `weighting/__init__.py` | 0B | OK |
| `weighting/alpha_eff.py` | 6,863B | OK |
| `data_generation/generate_synthetic.py` | 9,111B | OK |
| `detector/train_detector.py` | 13,594B | OK |
| `training/pretrain_weighted.py` | 14,685B | OK |
| `evaluation/eval_pipeline.py` | 13,872B | OK |
| `evaluation/compare_results.py` | 6,077B | OK |

**alpha_eff 模块测试通过**: `find_optimal_b([0.1,0.3,0.8,0.9,0.2], tau=0.9, n_min=2)` → b*=7.88, alpha_eff=0.856, ESS=2.0

**注意**: ModernBERT 加载需要 `TORCHDYNAMO_DISABLE=1`（torch 2.10.0 的 `torch.compile` 兼容性问题），离线加载需要 `HF_HUB_OFFLINE=1`。

---
