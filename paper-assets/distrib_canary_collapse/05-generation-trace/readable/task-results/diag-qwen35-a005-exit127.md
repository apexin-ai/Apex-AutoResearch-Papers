# diag qwen35 a005 exit127

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen35_a005_exit127_20260518T220930_result.json`
- **Structured JSON:** [`8ad1e757b2723d3abf14.json`](../../sessions/8a/8ad1e757b2723d3abf14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结果

### 实际错误信息

两个实验 log 内容完全相同：
```
bash: line 1: python: command not found
EXIT_CODE=127
```

### 根因

`.bashrc` 中没有 `conda init` 块，miniconda3 未加入 PATH。裸 `python` 命令不存在，系统也没有 `/usr/bin/python*`。Python 3.12.3 只存在于 `/root/miniconda3/bin/python`，但该路径不在默认 shell 的 `$PATH` 中。

此外 `.bashrc` 开头有 `[ -z "$PS1" ] && return`，非交互式 shell（如 ssh remote command）会直接跳过后续所有内容，即使加了 conda init 也不会生效。

### 正确的环境激活命令前缀

```bash
export PATH="/root/miniconda3/bin:$PATH"
```

无 conda 虚拟环境（`/root/miniconda3/envs/` 为空），直接用 base 环境即可。

### 项目代码位置

`/root/autodl-tmp/distrib_canary_collapse/iterative_train.py`

### 重提交命令

**实验 1: qwen35_08b_wiki_a100_s42**
```bash
export PATH="/root/miniconda3/bin:$PATH" && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name /root/autodl-tmp/models/Qwen3.5-0.8B-Base/ --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 1.0 --output_dir results/generalize/qwen35_08b_wiki_a100_s42_fp32
```

**实验 2: alpha_sweep_a005_s42**
```bash
export PATH="/root/miniconda3/bin:$PATH" && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.05 --output_dir results/alpha_sweep/a005_s42_fp32
```

---
