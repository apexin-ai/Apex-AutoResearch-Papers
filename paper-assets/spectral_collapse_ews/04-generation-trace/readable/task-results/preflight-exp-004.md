# preflight exp 004

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_preflight_exp_004_20260517T104732_result.json`
- **Structured JSON:** [`92db43fc948f546816a5.json`](../../sessions/92/92db43fc948f546816a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_004 预检结果

| # | 检查项 | 状态 |
|---|--------|------|
| 1 | `--condition fixed_mix` argparse 支持 | ✅ 在 `CONDITION_CHOICES` 中 |
| 2 | `fixed_mix` 实现: `real_data_ratio=0.5`, `ratio_schedule=[0.5]*T` | ✅ 确认 50/50 固定比例 |
| 3 | checkpoint 目录 `fixed_mix_seed42/` | ✅ 不存在，无残留 |
| 4 | 结果文件 `phase1_fixed_mix_seed42_results.json` | ✅ 不存在，无残留 |
| 5 | 数据文件 (`train_real_50k.pt`, `eval_5k.pt`, `spectral_1k.pt`) | ✅ 就绪 |
| 6 | 模型缓存 `pythia-410m-deduped` (含 safetensors + tokenizer) | ✅ 就绪 (symlink → autodl-tmp) |
| 7 | `--help` dry-run | ✅ 通过 |

### 需注意

- **GPU 0 当前被占用**: PID 59365 — `run_phase0.py --resume_from_gen 4` (exp_001)，占用 65.9 GB VRAM，需等其完成。
- **GPU 1**: PID 88161 — exp_003 (`run_phase1.py --condition adaptive --seed 42`)，占用 23.7 GB，不影响 exp_004。
- **Python 路径**: 服务器上 `python` 不在 PATH 中，需要 conda 激活。启动命令应改为：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/spectral_collapse_ews && \
TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 \
python run_phase1.py --condition fixed_mix --seed 42 --generations 10
```

**结论: Ready to launch**，等 exp_001 (GPU 0) 完成即可启动。

---
