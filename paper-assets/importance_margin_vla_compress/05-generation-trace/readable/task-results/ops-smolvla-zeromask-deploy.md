# ops smolvla zeromask deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_smolvla_zeromask_deploy_20260522T112240_result.json`
- **Structured JSON:** [`465e20b8b4d0c44b3d72.json`](../../sessions/46/465e20b8b4d0c44b3d72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功部署并正常运行。

## 部署结果

**服务器**: westd-27271 (2x RTX PRO 6000 Blackwell, 98GB each)

| 实验 | GPU | PID | 日志 |
|------|-----|-----|------|
| zero_mask random k=0.95 | GPU 0 | 396732 | `logs/smolvla_zeromask_random_k095.log` |
| zero_mask l2norm k=0.95 | GPU 1 | 398985 | `logs/smolvla_zeromask_l2norm_k095.log` |

**脚本**: `eval_smolvla_pruning_official.py`（已有完整的 `random_prune` / `l2norm_prune` + `zero_mask` / `true_removal` 支持，**无需修改代码**）

**结果输出**:
- `eval_results/zeromask_random_k095_obj_s42.json`
- `eval_results/zeromask_l2norm_k095_obj_s42.json`

**早期信号**: random zero_mask 实验已跑到 Task 0 Ep 12/50，目前全部 FAIL（280 steps max）。l2norm 刚开始加载，hook 确认 N=64 → k=60（保留 95%，置零 4 tokens），norm range [83, 299]。

**注意**: GPU 0 上还有一个先前的实验（PID 387588, l2norm k=0.9 10ep），VRAM 充裕无冲突。

---
