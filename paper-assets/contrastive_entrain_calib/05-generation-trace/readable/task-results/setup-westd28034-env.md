# setup westd28034 env

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_westd28034_env_20260518T132157_result.json`
- **Structured JSON:** [`b6e91754686163807e32.json`](../../sessions/b6/b6e91754686163807e32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境部署完成。

## westd-28034 环境总结

| 项目 | 值 |
|---|---|
| GPU | 4× RTX 5090 (31GB), Driver 595.71.05 |
| CUDA | 12.8 |
| Python | 3.12.3 (miniconda3) |
| PyTorch | 2.8.0+cu128 |
| transformers | 5.8.1 |
| trl | 1.4.0 |
| peft | 0.19.1 |
| datasets | 4.8.5 |
| accelerate | 1.13.0 |
| scipy | 1.17.1 |
| scikit-learn | 1.8.0 |
| wandb | 0.27.0 |
| einops | 0.8.2 |

**torchaudio** 安装但有 ABI 兼容问题（`undefined symbol: torch_library_impl`），本项目不需要，可忽略。

**项目目录**: `/root/contrastive_entrain_calib/{training,data,eval,results,checkpoints}` 已创建。

**环境激活命令**:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
```

---
