# prep exp008 data setup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp008_data_setup_20260514T151351_result.json`
- **Structured JSON:** [`8a554880f396dcb844d6.json`](../../sessions/8a/8a554880f396dcb844d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。

---

## 产出汇总

### 1. Symlink 设置 ✅

6 个 symlinks 全部创建成功：
- `sft_clean/{mmlu,gsm8k,arc_challenge}/` → exp-002 `d000_s42` signals
- `sft_contam/{mmlu,gsm8k,arc_challenge}/` → exp-002 `d005_s42` signals

### 2. 数据格式验证 ✅

| Benchmark | Records | 格式 |
|-----------|---------|------|
| mmlu | 14,042 | ✓ |
| gsm8k | 1,319 | ✓ |
| arc_challenge | 1,172 | ✓ |

每条记录字段：`index, benchmark, s1_embedding, s2_minkpp, s3_constat (null), s4_selfcritique`。s3_constat 为 null（3sig 模式），与 run_exp008.sh 的 `SIGNALS="embedding minkpp selfcritique"` 一致。

### 3. base + rl_aligned Signal 计算命令

两个 regime 的目录尚不存在，需要计算。模型已就位。

**base regime（3 benchmarks）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export CUDA_VISIBLE_DEVICES=&lt;GPU_ID>

for bench in mmlu gsm8k arc_challenge; do
  mkdir -p /root/autodl-tmp/exp008/signals/base/${bench}
  python /root/contamcal-irt-calibration/exp002/compute_signals.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
    --benchmark ${bench} \
    --ref-model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
    --sft-data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl \
    --output-dir /root/autodl-tmp/exp008/signals/base/${bench} \
    --signals embedding minkpp selfcritique
done
```

**rl_aligned regime（3 benchmarks）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export CUDA_VISIBLE_DEVICES=&lt;GPU_ID>

for bench in mmlu gsm8k arc_challenge; do
  mkdir -p /root/autodl-tmp/exp008/signals/rl_aligned/${bench}
  python /root/contamcal-irt-calibration/exp002/compute_signals.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct \
    --benchmark ${bench} \
    --ref-model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
    --sft-data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl \
    --output-dir /root/autodl-tmp/exp008/signals/rl_aligned/${bench} \
    --signals embedding minkpp selfcritique
done
```

或者**一步到位**运行完整 pipeline（会自动跳过已有 sft_clean/sft_contam signals）：
```bash
bash /root/contamcal-irt-calibration/exp008/run_exp008.sh &lt;GPU_ID>
```

### 4. 预计 GPU 时间

从 exp-002 日志（4090D 单卡）：
- d000（clean adapter，类似 base）：3 benchmarks ~11 min
- base/rl_aligned 是 full model（无 adapter merge 开销），预计 **~10-15 min/regime**
- 两个 regime 串行：**~20-30 min**
- 如分两张卡并行：**~15 min**

### 5. 风险与问题

| 问题 | 状态 |
|------|------|
| **所有 6 GPU 被占用** | GPU 2/5 负载最轻（3.7GB），正在跑 exp001 evaluate.py（d100/d025），预计短时间内完成 |
| **base regime: model=ref-model** | 设计如此——Min-K++ z-score 趋近 0，作为 clean baseline |
| **C001 约束** | 提交前需 `nvidia-smi` 确认目标 GPU 无 exp008 同类进程 |
| **run_exp008.sh 完整 pipeline** | 包含 Step 2 signal survival analysis（`run_signal_survival.py` 已就位），signal 计算完成后可直接跑 |

---
