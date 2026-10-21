# infra post exp006 readiness

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_post-exp006-readiness_20260514T110455_result.json`
- **Structured JSON:** [`31afd08ed3536d72c3df.json`](../../sessions/31/31afd08ed3536d72c3df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。以下是就绪报告。

---

## exp-006 / exp-015 / exp-004 就绪报告

### 前置发现：exp-006 仍在运行

⚠️ **PID 61363 已不存在，但 exp-006 并未完成。** 实际运行进程是 PID 70982（由 tmux session `exp_006_graduated_filtering` 管理）。

- 当前：`graduated_a0.1_s789` 训练中，2586/2814 steps (92%)，~3min 后完成训练
- 已完成 eval：19/50 runs（base + no-filter×5 + binary-ours×5 + binary-drayson×5 + graduated_a0.1×3）
- 剩余：~31 runs（graduated_a0.1 剩 2 + graduated×4 alphas×5 seeds + surprisal×5 + dsir×5）
- 每 run ~45min → **剩余约 23 小时，修正 ETA ≈ May 15 ~18:00 UTC**（非 10:43）

---

### A. exp-006 分析脚本 ✅

| 检查项 | 结果 |
|--------|------|
| 文件存在 | ✅ `scripts/exp006_analyze.py`（注意：不是 `analyze_exp006.py`） |
| 读取路径 | ✅ 默认 `outputs/exp006/*/eval_results.json`，与实际输出目录匹配 |
| 功能 | ✅ 策略聚合、paired t-test、alpha sensitivity、one-sample vs base |
| 依赖 | ✅ numpy, scipy（conda base 已有） |
| 输出 | ✅ stdout 表格 + 可选 `--output` JSON |

**启动命令：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/gen-depth-contamination
python3 scripts/exp006_analyze.py --results-dir outputs/exp006 --output outputs/exp006/analysis_summary.json
```

---

### B. exp-015 Neural Probe ✅

| 检查项 | 结果 |
|--------|------|
| 脚本 | ✅ `scripts/run_exp015_neural_probe.py` |
| Pythia-1.4B 权重 | ✅ `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b` (5.5G, symlink → `pythia-1___4b`) |
| OLMo-1B 权重 | ✅ `/root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf` (4.4G) |
| Qwen2.5-1.5B 权重 | ✅ `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct` (2.9G) |
| 数据 | ✅ `data/depth_{0..5}.jsonl` + `features.csv` |
| MLP input_dim | ✅ 动态从 embedding shape 读取，适配不同 hidden_dim |

**启动命令（3 模型串行，每次加载 LLM→提取 embedding→释放→训练 MLP）：**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/gen-depth-contamination

# Qwen2.5-1.5B
CUDA_VISIBLE_DEVICES=0 python3 scripts/run_exp015_neural_probe.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct \
  --data_dir data \
  --label qwen1.5b \
  --output outputs/exp015/neural_probe_qwen1.5b.json \
  --max_depth 5 --n_folds 5

# Pythia-1.4B
CUDA_VISIBLE_DEVICES=0 python3 scripts/run_exp015_neural_probe.py \
  --model_path /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b \
  --data_dir data \
  --label pythia1.4b \
  --output outputs/exp015/neural_probe_pythia1.4b.json \
  --max_depth 5 --n_folds 5

# OLMo-1B
CUDA_VISIBLE_DEVICES=0 python3 scripts/run_exp015_neural_probe.py \
  --model_path /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf \
  --data_dir data \
  --label olmo1b \
  --output outputs/exp015/neural_probe_olmo1b.json \
  --max_depth 5 --n_folds 5
```

---

### C. exp-004 7B Cross-Scale ✅

| 检查项 | 结果 |
|--------|------|
| 脚本 | ✅ `scripts/run_exp004_qwen7b_depth.py` |
| Qwen2.5-7B 权重 | ✅ `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-7B-Instruct` (15G, 4 shard files 完整) |
| 显存估算 | ✅ 7B fp16 ≈ 14GB + generation KV cache ≈ 16-18GB → 24GB 4090D 可以跑 |
| 4-bit fallback | ✅ 脚本支持 `--quantize 4bit`（如 fp16 OOM 可用） |

**启动命令：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/gen-depth-contamination

CUDA_VISIBLE_DEVICES=0 python3 scripts/run_exp004_qwen7b_depth.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-7B-Instruct \
  --n_docs 1000 \
  --max_depth 3 \
  --batch_size 1 \
  --feat_batch_size 1 \
  --device cuda:0
```

如 fp16 OOM，加 `--quantize 4bit`。

---

### D. 磁盘空间 ✅

```
/dev/md0   150G   32G   119G   22%   /root/autodl-tmp
```

119G 空余，7B 生成数据 + exp-015 embedding 输出预计 <5G，无压力。

---

### 总结

| 项目 | 状态 |
|------|------|
| exp-006 分析脚本 | ✅ 就绪（文件名 `exp006_analyze.py`） |
| exp-015 脚本 + 模型 + 数据 | ✅ 就绪 |
| exp-004 脚本 + 7B 模型 | ✅ 就绪 |
| 磁盘空间 | ✅ 119G 可用 |
| GPU (4090D 24GB) | ✅ 可跑 7B fp16 |
| **exp-006 完成时间** | ⚠️ **修正 ETA: ~May 15 18:00 UTC（非 10:43）**，还剩 ~31 runs |

**唯一阻塞项**：exp-006 还在跑，占用 cuda:0 (~15.2GB VRAM)。exp-015 和 exp-004 都需要 GPU，必须等 exp-006 完成后才能启动。

---
