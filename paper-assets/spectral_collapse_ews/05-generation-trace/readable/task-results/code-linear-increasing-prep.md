# code linear increasing prep

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_linear-increasing-prep_20260517T192515_result.json`
- **Structured JSON:** [`148b1ed7107396abd84b.json`](../../sessions/14/148b1ed7107396abd84b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结：

### 产出

**1. run_phase1.py 无需修改** — 已完整支持 `linear_increasing` 条件（argparse choices、r_min/r_max 参数、build_config 分支、run_tag 逻辑、summary 保存）。

**2. Launch script 已创建**：`/root/spectral_collapse_ews/scripts/launch_linear_increasing.sh`

**3. 验证结果**：
```
condition=linear_increasing, seed=42, generations=10
r_min=0.2, r_max=0.8
run_tag=linear_increasing_seed42
ratio_schedule=[0.2, 0.2667, 0.3333, 0.4, 0.4667, 0.5333, 0.6, 0.6667, 0.7333, 0.8]
```

路径格式：`checkpoints_phase1/linear_increasing_seed42/`

**4. submit_training_job 命令（不启动）**：
```
bash /root/spectral_collapse_ews/scripts/launch_linear_increasing.sh 0
```

或直接用 `submit_training_job`：
```python
submit_training_job(
    server="rtx6000-diagprobe",
    command="source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/spectral_collapse_ews && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python run_phase1.py --condition linear_increasing --seed 42 --generations 10 --signal log_det --tau 0.002 --k 0 --signal_mode per_gen --r_min 0.20 --r_max 0.80 --gpu 0",
    job_name="exp_linear_increasing_seed42",
    account="root"
)
```

---
