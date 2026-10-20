# 实验诊断: mvp_collapse_decoupling

## 失败根因

**wandb API key 未配置。** `train.py:79` 调用 `wandb.init()` 时抛出异常：

```
wandb.errors.errors.UsageError: No API key configured. Use `wandb login` to log in.
```

`train.py` 硬编码了 `wandb.init()`，无 offline/disabled fallback。`run_pipeline.py` 也没有设置 `WANDB_MODE` 环境变量。

## 失败阶段

**Generation 1, Step 3 (Training)**。pipeline 执行到训练阶段时，两个 seed 的 `train.py` 进程同时因 wandb auth 失败而崩溃。

Pipeline 执行时间线：
1. ✅ Data preparation — 跳过（已存在）
2. ✅ Data splitting — `real_pool.jsonl` (579255 lines) → 3 chunks
3. ✅ Gen1 Step 1: Synthetic generation — 两个 seed 并行，耗时 135.3 min
4. ✅ Gen1 Step 2: Data mixing — seed42 (583734 samples), seed137 (583739 samples)
5. ❌ Gen1 Step 3: Training — `train.py` 启动即崩溃（wandb.init 失败）

## 部分产出

### 可用
| 产出 | 路径 | 大小 |
|------|------|------|
| Gen0 信号 (seed42) | `results/signals_gen0_seed42.json` | 209 KB |
| Gen0 信号 (seed137) | `results/signals_gen0_seed137.json` | 209 KB |
| Gen0 可视化 | `results/fig_*.pdf` (3 个) | — |
| Gen1 合成数据 (seed42) | `synthetic/synthetic_gen1_seed42.jsonl` | 335 MB |
| Gen1 合成数据 (seed137) | `synthetic/synthetic_gen1_seed137.jsonl` | 335 MB |
| Gen1 混合数据 (seed42) | `mixed/mixed_gen1_seed42.jsonl` | 942 MB |
| Gen1 混合数据 (seed137) | `mixed/mixed_gen1_seed137.jsonl` | 942 MB |

### 缺失
- `checkpoints/` 为空 — 无任何训练 checkpoint
- Gen1 及后续 generation 的信号、训练结果均无

### 可复用
合成数据和混合数据已完整生成（耗时约 2.25 小时），重跑时可跳过 Gen1 的 Step 1 和 Step 2。

## 修复建议

**方案 A（推荐）：设置 WANDB_MODE=offline**

在训练命令环境中加 `export WANDB_MODE=offline`，跳过 wandb 远程登录。日志仍会写到本地 `wandb/` 目录，后续可用 `wandb sync` 上传。

修改 `run_pipeline.py` 的训练启动命令前加入：
```python
env = os.environ.copy()
env["WANDB_MODE"] = "offline"
```
或在启动脚本中全局设置 `export WANDB_MODE=offline`。

**方案 B：配置 wandb API key**

```bash
wandb login <YOUR_API_KEY>
# 或
export WANDB_API_KEY=[REDACTED]
```

**方案 C：修改 train.py 增加 fallback**

```python
# train.py:79
try:
    wandb.init(project="prism-collapse-mixing", ...)
except wandb.errors.errors.UsageError:
    wandb.init(project="prism-collapse-mixing", ..., mode="offline")
```

### 重跑建议

由于 Gen1 的合成和混合数据已存在，pipeline 应能自动检测并跳过这两步。建议修复 wandb 问题后原样重跑，确认 pipeline 的断点续跑逻辑是否正确识别已有数据。

## 关键日志摘录

```
Traceback (most recent call last):
  File "/root/prism_collapse_mixing/train.py", line 149, in <module>
    main()
  File "/root/prism_collapse_mixing/train.py", line 79, in main
    wandb.init(
  ...
  File "/root/miniconda3/lib/python3.12/site-packages/wandb/sdk/lib/wbauth/authenticate.py", line 139, in authenticate_session
    raise UsageError(
wandb.errors.errors.UsageError: No API key configured. Use `wandb login` to log in.

  FAILED (exit 1): python /root/prism_collapse_mixing/train.py --data_dir /root/prism_collapse_mixing/mixed/gen1_seed42 ...
EXIT_CODE=1
```
