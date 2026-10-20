# code prep r015 script

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-r015-script_20260520T010702_result.json`
- **Structured JSON:** [`6c4708c2c7373b99fa26.json`](../../sessions/6c/6c4708c2c7373b99fa26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**脚本**: `/root/spectral_collapse_ews/scripts/launch_mixed_r0.15.sh`

```bash
#!/bin/bash
# Launch fixed_mix r=0.15 ablation
# Usage: bash launch_mixed_r0.15.sh [GPU_ID]

GPU_ID=${1:-0}
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/spectral_collapse_ews

CUDA_VISIBLE_DEVICES=${GPU_ID} \
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 \
python run_phase1.py \
  --condition fixed_mix --seed 42 --generations 10 \
  --signal log_det --tau 0.002 --k 0 --signal_mode per_gen \
  --real_ratio 0.15 --gpu 0
```

**Dry-run 结果**:
| 检查项 | 结果 |
|--------|------|
| `bash -n` 语法检查 | 通过 |
| `--real_ratio 0.15` 参数 | `run_phase1.py:98` 接受，type=float |
| 输出 run_tag | `fixed_mix_r015_seed42` |
| 结果文件 | `results/phase1_fixed_mix_r015_seed42_results.json` |
| checkpoint 目录 | `/root/autodl-tmp/.../checkpoints_phase1/fixed_mix_r015_seed42/` |

两块 GPU 都在跑实验，未实际启动。等 GPU 空闲后执行 `bash launch_mixed_r0.15.sh &lt;GPU_ID>`。

---
