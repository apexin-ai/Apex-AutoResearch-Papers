# prep multi seed configs

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_multi-seed-configs_20260515T120315_result.json`
- **Structured JSON:** [`3ddd629b4638fa2d95a3.json`](../../sessions/3d/3ddd629b4638fa2d95a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 数据已确认。4 个实验 spec 完整，参数与 a075_s42 一致（仅 seed/synthetic_ratio/output_dir 不同）。a075_s42 未显式传 `--model_name`（默认 pythia-410m），4 个实验同理。

---

## 实验 1: alpha_sweep_a025_s43
- **exp_id**: alpha_sweep_a025_s43
- **spec 核验**: model=pythia-410m, data=wikitext103_5k, α=0.25, seed=43, gen=10, steps=5000 ✓
- **command**:
```
bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43"
```
- **gpu_ids**: ["cuda:1"]
- **server**: westd-19828
- **timeout_hours**: 6

## 实验 2: alpha_sweep_a050_s43
- **exp_id**: alpha_sweep_a050_s43
- **spec 核验**: model=pythia-410m, data=wikitext103_5k, α=0.50, seed=43, gen=10, steps=5000 ✓
- **command**:
```
bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s43"
```
- **gpu_ids**: ["cuda:1"]
- **server**: westd-19828
- **timeout_hours**: 6

## 实验 3: alpha_sweep_a025_s44
- **exp_id**: alpha_sweep_a025_s44
- **spec 核验**: model=pythia-410m, data=wikitext103_5k, α=0.25, seed=44, gen=10, steps=5000 ✓
- **command**:
```
bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44"
```
- **gpu_ids**: ["cuda:1"]
- **server**: westd-19828
- **timeout_hours**: 6

## 实验 4: alpha_sweep_a050_s44
- **exp_id**: alpha_sweep_a050_s44
- **spec 核验**: model=pythia-410m, data=wikitext103_5k, α=0.50, seed=44, gen=10, steps=5000 ✓
- **command**:
```
bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s44"
```
- **gpu_ids**: ["cuda:1"]
- **server**: westd-19828
- **timeout_hours**: 6

---

4 组配置就绪，命令格式与 a075_s42 完全一致，可直接用于 `allocate_and_submit` 串行提交。

---
