# code alpha sweep extension config

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpha_sweep_extension_config_20260514T213020_result.json`
- **Structured JSON:** [`0a801b3d04e26a77766c.json`](../../sessions/0a/0a801b3d04e26a77766c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。报告如下：

---

## 验证结果

### 1. `--synthetic_ratio` 支持任意浮点数
`type=float`，0.10 和 0.60 解析正常，无范围限制（仅 `mix_datasets` 内部对 0/1 做边界处理）。

### 2. `mix_datasets` 双向逻辑验证

| α | syn 样本 | real 样本 | 总量 | 实际比例 | 走哪条路径 |
|---|---------|----------|------|---------|-----------|
| 0.10 | 555 | 5000 | 5555 | 0.0999 | 保全 real + subsample syn |
| 0.60 | 5000 | 3333 | 8333 | 0.6000 | 保全 syn + subsample real |

两个 α 值分别触发双向逻辑的两条路径，均正确。

### 3. 6 个 run 的完整启动命令

基于现有 a000_s42 的 config，参数模板：

```bash
# α=0.10, 3 seeds
cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python iterative_train.py \
  --model_name EleutherAI/pythia-410m \
  --data_dir data/wikitext103_5k \
  --synthetic_ratio 0.10 \
  --num_generations 10 \
  --steps_per_gen 5000 \
  --output_dir results/alpha_sweep/a010_s42 \
  --seed 42

# seed 43
... --output_dir results/alpha_sweep/a010_s43 --seed 43

# seed 44
... --output_dir results/alpha_sweep/a010_s44 --seed 44

# α=0.60, 3 seeds
... --synthetic_ratio 0.60 --output_dir results/alpha_sweep/a060_s42 --seed 42
... --synthetic_ratio 0.60 --output_dir results/alpha_sweep/a060_s43 --seed 43
... --synthetic_ratio 0.60 --output_dir results/alpha_sweep/a060_s44 --seed 44
```

### 4. 注意事项

- **`--accumulate` 未启用**：现有 a000/a025 的 config 显示 `accumulate: false`，新 run 保持一致（不加 `--accumulate`）
- **a000_s42 正在跑 gen_6**（截至检查时），a025_s42 也在跑。排队顺序建议：先完成 a050/a075，再加 a010/a060
- **α=0.10 数据量较小**（每 gen 仅 555 syn 样本混入 5000 real），训练会很快，约为 α=0.60 的 2/3 时间

---
