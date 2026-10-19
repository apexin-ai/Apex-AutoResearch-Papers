# setup check bjb2 40593 readiness

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_check-bjb2-40593-readiness_20260523T065434_result.json`
- **Structured JSON:** [`1753d436ac25deb79d3b.json`](../../sessions/17/1753d436ac25deb79d3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复已确认。以下是 bjb2-40593 检查报告：

## bjb2-40593 检查结果

| 项目 | 状态 |
|------|------|
| **GPU** | RTX 4090 D, 24GB 显存, 0% 利用率, 空闲 |
| **代码** | 存在，evaluate.py 已修复（刚删除 `args.K = 10` 覆盖） |
| **根分区** | 30G 用了 24G，剩 6.7G (78%) — 偏紧但够用 |
| **数据盘** | 250G 用了 133G，剩 118G (53%) — 充足 |
| **Python/PyTorch** | Python 3.12.3, torch 2.10.0+cu128, CUDA 可用, 1 GPU |
| **CRM checkpoint** | `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` **不存在**。有其他版本：`crm_v3/perdof`、`crm_v3/scalar_unc`、`crm_v3/obs_only`、`crm_v3_norm/*`、`crm_spatial_only` |
| **SmolVLA 模型** | 存在于 `/root/autodl-tmp/models/smolvla_base/` 和 `smolvla_libero/` |

## 综合判断

**可以立即部署 K=2 mean 实验**，前提是实验用的 CRM checkpoint 路径与服务器上已有的某个版本匹配。如果实验需要 `crm_smolvla_3suite_v1/crm_best.pt`，需要从其他服务器拷贝或重新训练。

---
