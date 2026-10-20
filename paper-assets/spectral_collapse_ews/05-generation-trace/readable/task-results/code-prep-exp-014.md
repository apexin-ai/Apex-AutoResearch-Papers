# code prep exp 014

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_exp_014_20260520T204957_result.json`
- **Structured JSON:** [`f56772fcc71e1a6f14b0.json`](../../sessions/f5/f56772fcc71e1a6f14b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Script created and validated. Here's the summary:

---

**1. exp_009 原始启动命令**
```bash
CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 \
python run_phase1.py --condition fixed_mix --seed 42 --generations 10 \
  --signal log_det --tau 0.002 --k 0 --signal_mode per_gen --real_ratio 0.25 --gpu 0
```

**2. exp_014 脚本**
- 路径: `/root/spectral_collapse_ews/scripts/launch_fixed_mix_r025_seed43.sh`
- 与 exp_009 唯一差异: `--seed 43`
- 输出会自动生成为:
  - Results: `results/phase1_fixed_mix_r025_seed43_results.json`
  - Summary: `results/phase1_fixed_mix_r025_seed43_summary.json`
  - Checkpoints: `/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed43/`
- `bash -n` 语法检查通过，checkpoint 目录存在

**3. 启动命令**
```bash
cd /root/spectral_collapse_ews && nohup bash scripts/launch_fixed_mix_r025_seed43.sh 0 > logs/exp_014.log 2>&1 &
```

---
