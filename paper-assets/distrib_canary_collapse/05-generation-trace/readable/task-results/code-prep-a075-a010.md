# code prep a075 a010

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-a075-a010_20260515T020601_result.json`
- **Structured JSON:** [`e14a931076f1088370ca.json`](../../sessions/e1/e14a931076f1088370ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

| 检查项 | 结果 |
|--------|------|
| `a075_s42/` 目录 | 不存在 ✓ |
| `a010_s42/` 目录 | 不存在 ✓ |
| `data/wikitext103_5k/` | 存在（含 eval, prompts, train） ✓ |
| `iterative_train.py` 参数 | `--synthetic_ratio`, `--seed`, `--steps_per_gen`, `--num_generations`, `--output_dir` 全部支持 ✓ |

两条提交命令参数正确，输出目录干净，可以直接使用：

**a075_s42** (α=0.75):
```
bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.75 --output_dir results/alpha_sweep/a075_s42"
```

**a010_s42** (α=0.10):
```
bash -c "cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.10 --output_dir results/alpha_sweep/a010_s42"
```

---
