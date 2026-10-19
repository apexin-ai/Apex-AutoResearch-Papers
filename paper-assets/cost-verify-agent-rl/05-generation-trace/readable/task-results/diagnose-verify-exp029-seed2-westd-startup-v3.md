# diagnose verify exp029 seed2 westd startup v3

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_verify-exp029-seed2-westd-startup-v3_20260518T225518_result.json`
- **Structured JSON:** [`3dae71f49d7428be761e.json`](../../sessions/3d/3dae71f49d7428be761e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果：失败

**根因**：启动脚本直接调用 `python`，但未先激活 conda 环境。`python`/`python3` 不在裸 PATH 中。

**环境诊断**：
- Python 位置：`/root/miniconda3/bin/python`（miniconda3 存在但未加入 PATH）
- `which python` / `which python3`：均为空
- conda 需手动激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`

**hsweep_h10 的正确启动方式**（从 `ps aux` 提取）：
```bash
bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
  export TMPDIR=/root/autodl-tmp/tmp && \
  export WANDB_DIR=/root/autodl-tmp/wandb && \
  export WANDB_TMPDIR=/root/autodl-tmp/tmp && \
  export TORCH_COMPILE_DISABLE=1 && \
  export PYTHONUNBUFFERED=1 && \
  mkdir -p $TMPDIR && \
  cd /root/cost-verify-agent-rl/RAGEN && \
  python train.py --config-name _alfworld_hsweep_h10 seed.train=10000 \
    trainer.experiment_name=hsweep-h10-seed1 \
  2>&1 | tee /root/autodl-tmp/cost-verify-agent-rl/logs/hsweep_h10_seed1.log'
```

**exp029_seed2_westd_resume 的启动脚本缺少** `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` 这一步，导致 `python: command not found`（exit code 127）。

**GPU 状态**：
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 3/97887 MiB (空闲) |
| 1 | 0% | 3/97887 MiB (空闲) |
| 2 | 91% | 27473/97887 MiB (hsweep_h10) |
| 3 | 98% | 27473/97887 MiB (hsweep_h10) |

**修复方向**：重新启动 exp029_seed2 时，需要照搬 hsweep_h10 的环境初始化前缀（conda activate + 环境变量导出），并使用 `CUDA_VISIBLE_DEVICES=0,1` 限定到空闲 GPU。

---
