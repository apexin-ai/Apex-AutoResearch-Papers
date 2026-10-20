# code multi seed prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multi_seed_prep_20260515T065911_result.json`
- **Structured JSON:** [`2e5d66142a63e27c9596.json`](../../sessions/2e/2e5d66142a63e27c9596.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

| 检查项 | 状态 |
|--------|------|
| conda 环境 | ✅ 正常 |
| `--seed` 参数 | ✅ 支持，config 正确记录 seed=43 |
| 4 个目标目录不存在 | ✅ 无覆盖风险 |
| Dry-run（脚本启动、参数解析、数据加载） | ✅ 模型加载、数据加载、输出目录创建均正常 |
| 磁盘空间 | ✅ 111GB 可用，需 ~12GB |

## 4 个提交命令

**1. alpha_sweep_a025_s43** (α=0.25, seed=43)
```
bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43"
```

**2. alpha_sweep_a050_s43** (α=0.50, seed=43)
```
bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s43"
```

**3. alpha_sweep_a025_s44** (α=0.25, seed=44)
```
bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44"
```

**4. alpha_sweep_a050_s44** (α=0.50, seed=44)
```
bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s44"
```

全部验证通过，a075 完成后可零延迟顺序提交。

---
