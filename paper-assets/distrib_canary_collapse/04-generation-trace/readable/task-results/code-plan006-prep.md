# code plan006 prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-prep_20260514T215142_result.json`
- **Structured JSON:** [`dbf96f54a4a13169cd30.json`](../../sessions/db/dbf96f54a4a13169cd30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## Summary

### Part 1: 训练命令（验证通过，可直接提交）

**Seed 42:**
```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_HUB_DISABLE_XET=1 && \
export HF_ENDPOINT=https://hf-mirror.com && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
PYTHONUNBUFFERED=1 python -u iterative_train.py \
  --seed 42 \
  --data_dir data/wikitext103_5k \
  --steps_per_gen 5000 \
  --num_generations 20 \
  --synthetic_ratio 1.0 \
  --output_dir results/extended_20gen/s42
```

**Seed 43:**
```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_HUB_DISABLE_XET=1 && \
export HF_ENDPOINT=https://hf-mirror.com && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
PYTHONUNBUFFERED=1 python -u iterative_train.py \
  --seed 43 \
  --data_dir data/wikitext103_5k \
  --steps_per_gen 5000 \
  --num_generations 20 \
  --synthetic_ratio 1.0 \
  --output_dir results/extended_20gen/s43
```

### Part 2: analyze_extended.py

已部署到 `/root/autodl-tmp/distrib_canary_collapse/analyze_extended.py`，包含 5 个分析模块：
1. **Full cross-corr** (raw + first-diff, max_lag=10, 5000 permutation p-value)
2. **Permutation Granger** + BH FDR 校正
3. **Rolling window** (gen 5-end，排除 gen 0→1 跳变)
4. **TY supplementary** (d_max=0,1,adaptive)
5. **MVP 10-gen 对比** (lag 稳定性 + power gain 检测)

运行方式：
```bash
# 20-gen 数据就绪后
python analyze_extended.py --seeds 42 43 --max_lag 10
```

### Part 3: Dry-run 结果

MVP seed_42 数据验证通过。输出格式正确，import 链无报错。关键发现（10-gen MVP baseline）：
- `token_entropy→perplexity`: raw lag=-5, |r|=0.812 (large), Granger p=0.71 (n.s.)
- `token_entropy→distinct_1`: raw lag=-1, |r|=0.993, Granger p=0.006 (FDR sig)
- Rolling window (gen 5-10, N=6) 数据点太少，所有 pair 均不显著 — 20-gen 时 (gen 5-20, N=16) 将有足够统计功效

### 训练时长估算

MVP 10-gen (5000 steps/gen) 耗时 ~4.1 小时。20-gen 预估 **~8 小时/run**，两个 seed 串行 ~16 小时。

---
