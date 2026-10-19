# code prepare ablation scripts

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-ablation-scripts_20260516T174340_result.json`
- **Structured JSON:** [`75d759e725a3d0d74d8e.json`](../../sessions/75/75d759e725a3d0d74d8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个脚本全部 dry-run 通过。

## 结果汇总

| 脚本 | 状态 | 关键参数 |
|------|------|----------|
| `run_acib_on_plus.sh` | 已更新（补充环境变量，统一格式） | model=plus, α=0.01, β=0.01, ctr=0.1, div=0.1 |
| `run_contrastive_only.sh` | 新建 | α=0, β=0, ctr=0.1, div=0.1 |
| `run_ib_only.sh` | 新建 | α=0.01, β=0.01, ctr=0, div=0.1 |

修正内容：`run_acib_on_plus.sh` 原脚本缺少 `WANDB_MODE=disabled`、`MUJOCO_GL=egl`、`PYOPENGL_PLATFORM=egl` 环境变量导出，已补齐；去掉多余的 `CUDA_VISIBLE_DEVICES=0`（`--gpu 0` 已处理）；升级为 `set -euo pipefail`。

eval 跑完后可直接 `bash /root/acib/scripts/run_*.sh` 启动对应 ablation。

---
