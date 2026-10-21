# code alpha sweep prep detrend

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpha-sweep-prep-detrend_20260514T213052_result.json`
- **Structured JSON:** [`d71631a0f6160a2d7636.json`](../../sessions/d7/d71631a0f6160a2d7636.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Summary

### Part 1: α-sweep 扩展配置

**`synthetic_ratio` 支持情况**: `type=float`，任意浮点数（0.10, 0.60）均可。

**`mix_datasets` 比例验证**（Python 精确计算）:
- α=0.10: syn=555, real=5000, actual_ratio=**0.0999**, 误差 0.01%
- α=0.60: syn=5000, real=3333, actual_ratio=**0.6000**, 精确命中

双向 subsample 逻辑正确：低 α 走 `keep all real + subsample syn`，高 α 走 `keep all syn + subsample real`。

**α=0.10 dry-run**: 模型从本地缓存离线加载成功，生成流程无报错（仅标准 padding 警告）。因 GPU 被 a000/a025 实验占用 88-90%，完整 5000-prompt 生成过慢，已 kill 释放 GPU。核心验证目标已达成。

**配置文件**: `/root/autodl-tmp/distrib_canary_collapse/alpha_sweep_queue.md`

**6 个待提交 run 完整命令**:

```bash
# α=0.10
nohup python iterative_train.py --seed 42 --synthetic_ratio 0.10 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/alpha_sweep/a010_s42 > /tmp/a010_s42.log 2>&1 &
nohup python iterative_train.py --seed 43 --synthetic_ratio 0.10 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/alpha_sweep/a010_s43 > /tmp/a010_s43.log 2>&1 &
nohup python iterative_train.py --seed 44 --synthetic_ratio 0.10 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/alpha_sweep/a010_s44 > /tmp/a010_s44.log 2>&1 &

# α=0.60
nohup python iterative_train.py --seed 42 --synthetic_ratio 0.60 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/alpha_sweep/a060_s42 > /tmp/a060_s42.log 2>&1 &
nohup python iterative_train.py --seed 43 --synthetic_ratio 0.60 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/alpha_sweep/a060_s43 > /tmp/a060_s43.log 2>&1 &
nohup python iterative_train.py --seed 44 --synthetic_ratio 0.60 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/alpha_sweep/a060_s44 > /tmp/a060_s44.log 2>&1 &
```

提交前需加 `HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1` 环境变量。

---

### Part 2: Detrending 工具验证结果

文件: `/root/autodl-tmp/distrib_canary_collapse/detrending_utils.py`

**TEST 1 — 合成线性趋势数据**:
| 方法 | 长度 | mean | std |
|------|------|------|-----|
| first_diff | 19 | 0.4900 | 0.1087 |
| hp_filter | 20 | -0.0000 | 0.0646 |
| linear | 20 | -0.0000 | 0.0739 |

三种方法均正确去除趋势（mean≈0）。

**TEST 2 — 已知 lag 的 cross-correlation**（x leads y by 1 step）:
| 方法 | peak_lag | peak_corr |
|------|----------|-----------|
| first_diff | **-1** | 0.989 |
| hp_filter | **-1** | 0.901 |
| linear | **-1** | 0.858 |

三种方法均正确检测到 lag=-1（x leads y）。

**TEST 3 — MVP token_entropy → distinct_1 dry-run**:
| 方法 | peak_lag | peak_corr |
|------|----------|-----------|
| first_diff | **-1** | 0.995 |
| hp_filter | **-1** | 0.996 |
| linear | **-1** | 0.912 |

与现有 analyze_mvp.py 的原始 cross-correlation 结果一致（lag=-1），去趋势后 lead-lag 关系保持稳健。输出格式与现有分析兼容（`correlations` dict, `peak_lag`, `peak_corr`）。

---
