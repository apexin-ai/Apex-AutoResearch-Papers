# infra exp015 readiness check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp015-readiness-check_20260515T013155_result.json`
- **Structured JSON:** [`a5f30ed42fe356cca687.json`](../../sessions/a5/a5f30ed42fe356cca687.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕。汇报如下：

---

## exp-015 Neural Probe 重跑就绪状态

### 1. 脚本 ✅
`scripts/run_exp015_neural_probe.py` 存在，v2 版本，包含：
- **Bootstrap CI**: `--bootstrap_resamples` (默认 1000)
- **Permutation test**: `--permutation_resamples` (默认 500)
- **Peak VRAM logging**: 每次 embedding extraction 和每个 fold MLP 训练都记录 peak VRAM
- **OOM-safe batch adapt**: embedding 阶段 OOM 时自动 batch_size 减半

### 2. 模型 ✅
| 模型 | 路径 | 状态 |
|------|------|------|
| Qwen-2.5-1.5B | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct/` | model.safetensors 存在 |
| Pythia-1.4B | `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b/` | model.safetensors + pytorch_model.bin 存在 |
| OLMo-1B | `/root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf/` | model.safetensors 存在 |

### 3. 数据 ✅
| 数据集 | 路径 | depth 0-5 各 5000 条 |
|--------|------|---------------------|
| Qwen-cont | `data_exp017_qwen_cont/` | 30,000 ✅ |
| Pythia | `data_exp001_pythia/` | 30,000 ✅ |
| OLMo | `data_exp002_olmo/` | 30,000 ✅ |

### 4. 已有结果
`exp015_neural_probe_results.json` 存在，仅含 **Qwen-cont** 的 v1 结果（有 fold_stats，**无 bootstrap_ci / permutation_test**）。K\*=3, acc=0.4335。需要用 v2 脚本重跑以补全统计检验。

### 5. 显存预估 ✅ 安全
- GPU: **RTX 4090 D, 24564 MiB (24GB)**
- 最大模型 Qwen-1.5B fp16 ≈ 3GB + embedding 激活 (bs=16, max_len=512) ≈ 3-4GB → **峰值 ~7GB**
- Pythia-1.4B / OLMo-1B 更小，峰值更低
- MLP 训练阶段 LLM 已释放，VRAM 占用极低
- **远低于 20GB 安全线**

### 6. Python 依赖 ✅
torch 2.10.0+cu128、transformers、sklearn、lightgbm、tqdm 均已安装（Python 3.12, conda base 环境）。

### 7. 注意事项
- 脚本每次运行只加载**一个模型**。3 个模型需要 **3 次独立运行**，否则会覆盖输出文件。
- 需要指定不同的 `--output` 路径避免覆盖。

---

## 推荐启动命令

3 个模型顺序执行，用 nohup 防止 SSH 断连：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

cd /root/autodl-tmp/gen-depth-contamination

# 1. Qwen-cont (重跑以补 bootstrap CI + permutation test)
nohup python scripts/run_exp015_neural_probe.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct \
  --data_dir data_exp017_qwen_cont \
  --label Qwen-cont \
  --output artifacts/exp015_neural_probe_qwen_cont.json \
  > logs/exp015_qwen_cont.log 2>&1 &

# 2. Pythia-1.4B
nohup python scripts/run_exp015_neural_probe.py \
  --model_path /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b \
  --data_dir data_exp001_pythia \
  --label Pythia-1.4B \
  --output artifacts/exp015_neural_probe_pythia.json \
  > logs/exp015_pythia.log 2>&1 &

# 3. OLMo-1B
nohup python scripts/run_exp015_neural_probe.py \
  --model_path /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf \
  --data_dir data_exp002_olmo \
  --label OLMo-1B \
  --output artifacts/exp015_neural_probe_olmo.json \
  > logs/exp015_olmo.log 2>&1 &
```

**注意**：3 个任务不能并行跑（共用 1 块 GPU）。建议串行，即等前一个完成后再启动下一个。或写成一个脚本依次执行。

---
