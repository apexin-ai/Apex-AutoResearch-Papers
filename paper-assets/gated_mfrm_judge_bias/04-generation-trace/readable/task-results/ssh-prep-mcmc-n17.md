# ssh prep mcmc n17

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prep-mcmc-n17_20260524T092601_result.json`
- **Structured JSON:** [`28f5d56b17a88319a95c.json`](../../sessions/28/28f5d56b17a88319a95c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有检查完成。以下是完整汇报。

---

## 汇报：N=17 MCMC Fitting 准备状态

### 1. MCMC fitting 脚本 (`run_exp003_n17.py`) — 存在但需修复

**问题 A**: `CUDA_VISIBLE_DEVICES = "0"`，需改为 `"0,3"` 以使用 cuda:0 + cuda:3

**问题 B**: 系统 python3 **没有** jax/numpyro。必须用 conda 环境运行：
```
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
```
conda base 中依赖完整：jax 0.10.1, numpyro 0.21.0, 4x RTX PRO 6000 (98GB) 全部可见

### 2. 数据准备 (`prepare_n17_data.py`) — 需要重新运行

- 当前 `judgment_data_n17/` 只有 **6 个 judge**（claude-sonnet-4.6-proxy, deepseek-v4-pro-proxy, gemini-2.5-pro-proxy, llama-3.3-70b, qwen2.5-72b, qwen3-235b-proxy）
- exp001/results 中已有 7 个 `*_n17` 数据源（多了 mistral-large-2-local_n17）
- exp-020 完成后需重新 `python prepare_n17_data.py` 刷新 symlinks

### 3. qwen3-8b 方案 B — **未实现**

需要在 3 个地方添加过滤逻辑：

| 脚本 | 现状 | 需要做的 |
|------|------|---------|
| `run_exp003_n17.py` | MCMC 用所有模型 | **不需要改**（方案 B 就是 fitting 包含 qwen3-8b） |
| `evaluation.py` | `arena_correlation()` 自动匹配 ARENA_ELO，qwen3-8b 在 ARENA_ELO 中会被包含 | 添加 `exclude_models=["qwen3-8b"]` 参数，τ 计算时排除 |
| `bootstrap_delta_tau.py` | 硬编码 N=8 的 MODEL_NAMES 和 ARENA_ELO | 完全不适用 N=17，需要用数据驱动（从 idata 获取模型列表）并加 qwen3-8b 排除 |
| `run_n17_downstream.py` | bootstrap wrapper 知道会 break 但没修 | 需重写 bootstrap 部分 |

**注意**: 当前 judgment data 中实际有 **18 个目标模型**（非 17），模型名与 ARENA_ELO 存在命名不匹配（如 `gemma-2-9b-it` vs `gemma-2-9b`，`gpt-4o-2024-05-13` vs `gpt-4o`），需要添加 name mapping。

### 4. 依赖 — conda 中完整，系统 python 缺失

| 包 | conda base | 系统 python3 |
|---|---|---|
| jax | 0.10.1 | 未安装 |
| numpyro | 0.21.0 | 未安装 |
| arviz | (已有) | 未检查 |

### 5. 路径 bug

`run_n17_downstream.py` 中 `JUDGMENT_DIR_N17 = "/root/gated_mfrm_judge_bias/exp001_n17/results"` — **该路径不存在**。应改为 `/root/gated_mfrm_judge_bias/exp003/judgment_data_n17` 或根据实际情况调整。

### 6. 一键启动命令（修复后）

```bash
# Step 1: 数据准备（judge eval 完成后执行）
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/gated_mfrm_judge_bias/exp003
python prepare_n17_data.py

# Step 2: MCMC fitting（nohup 后台运行）
nohup python run_exp003_n17.py \
  --judgment-dir /root/gated_mfrm_judge_bias/exp003/judgment_data_n17 \
  --exposure-csv /root/gated_mfrm_judge_bias/exp002/results/exposure_scores.csv \
  --output-dir /root/gated_mfrm_judge_bias/exp003/output_n17 \
  --warmup 6000 --samples 4000 --chains 4 --target-accept 0.95 \
  --device gpu \
  > /root/gated_mfrm_judge_bias/exp003/run_n17.log 2>&1 &

# Step 3: Downstream（MCMC 完成且 convergence OK 后）
python run_n17_downstream.py
```

### 7. 需要修复的问题清单

1. **`run_exp003_n17.py` L5**: `CUDA_VISIBLE_DEVICES = "0"` → `"0,3"`
2. **`run_n17_downstream.py` L22**: `JUDGMENT_DIR_N17` 路径不存在，需修正
3. **`evaluation.py` `arena_correlation()`**: 添加 qwen3-8b 排除参数 + ARENA_ELO name mapping（18 个模型名对齐）
4. **`bootstrap_delta_tau.py`**: 需重写为数据驱动（不再硬编码 MODEL_NAMES），添加 qwen3-8b 排除
5. **`run_n17_downstream.py` `run_bootstrap()`**: 当前 wrapper hack 不可用，需配合 bootstrap 脚本更新
6. **所有脚本启动前**: 必须先 `conda activate base`，否则 import 失败

需要我开始修复这些问题吗？

---
