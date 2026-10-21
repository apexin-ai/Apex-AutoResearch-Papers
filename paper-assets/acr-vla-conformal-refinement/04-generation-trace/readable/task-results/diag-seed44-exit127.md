# diag seed44 exit127

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_seed44-exit127_20260516T013231_result.json`
- **Structured JSON:** [`df57d8d43d871b5f7e69.json`](../../sessions/df/df57d8d43d871b5f7e69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个日志全部一致。诊断结果：

## 失败根因

命令格式 `bash -c "cd ... && python -u ..."` 未激活 conda 环境。两台服务器的 `python` 都在 `/root/miniconda3/bin/python`，不在默认 PATH 上。非交互 `bash -c` 不会加载 `.bashrc`，所以 conda 没初始化，`python` 找不到。

成功实验 `eval-perdof-object-seed43` 的日志确认它在 conda base 环境下运行（包从 `/root/miniconda3/lib/python3.12/site-packages/` 加载）。

## 正确的环境激活命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
```

## 修复后的重新提交命令

三个实验的命令都需要在 `cd` 前加上 conda 激活：

**1. eval-obs-only-object-norm02-seed44** (bjb1-18228, cuda:2)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json"
```

**2. eval-argmin-object-seed44** (bjb1-18228, cuda:3)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_argmin --benchmark object --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/argmin/crm_best.pt --output_file logs/eval_object_argmin_seed44.json"
```

**3. eval-vla-only-object-seed44** (bjb2-40593, cuda:0)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode vla_only --benchmark object --seed 44 --output_file logs/eval_object_vla_only_seed44.json"
```

> 注意：具体的 `--crm_checkpoint` 路径和其他参数我是从实验名推断的，你需要核对原始提交命令中的完整参数，确保与 seed=42/43 的同类实验一致。提交系统本身也需要修复，让所有后续实验命令都包含 conda 激活步骤。

---
