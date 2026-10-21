# ops falcon3 cqa1 signals or gsm8k

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-cqa1-signals-or-gsm8k_20260522T141728_result.json`
- **Structured JSON:** [`2a8f11902a001640f832.json`](../../sessions/2a/2a8f11902a001640f832.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。汇总结果：

## 调查结果

**1. compute_signals.py**
- 路径：`/root/contamcal-irt-calibration/exp002/compute_signals.py`
- 参数：`--model-path`, `--adapter-path`, `--benchmark` (mmlu/gsm8k/arc_challenge/humaneval), `--signal` (s1/s2/s3/s4/all), `--output-dir`, `--batch-size`
- S2 (minkpp) 先加载 target model 计算完再 del + empty_cache，然后加载 reference model——7B 模型可在 24GB 4090 上串行运行
- S3 无 eval paths 时自动跳过，`--signal all` 安全

**2. cqa1 Falcon3 资源**
- Base model: `/root/autodl-tmp/.hf_cache/Falcon3-7B-Base/` ✓
- Checkpoint: `Falcon3-7B-Base_d100_s42/lora_adapter` (lora_alpha=32) ✓
- d000 checkpoint: 不在 cqa1（s2 会用 base model 无 adapter 作为 reference）
- 无已有 Falcon3 signals

**3. 数据集**
- MMLU: 已缓存 ✓
- ARC-Challenge: 已缓存 ✓
- GSM8K: **未缓存**，需先下载

**4. 方案：运行 Signals（Option A）**

准备好的完整命令（先下载 GSM8K 数据集，再依次对 3 个 benchmark 计算 s1/s2/s4 信号）：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
source /etc/network_turbo && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_HUB_DISABLE_XET=1 && \
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && \
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && \
cd /root/contamcal-irt-calibration && \
python -c "from datasets import load_dataset; load_dataset('openai/gsm8k', 'main', split='test', cache_dir='/root/autodl-tmp/.hf_cache'); print('GSM8K downloaded')" && \
for bench in mmlu arc_challenge gsm8k; do \
  echo "===== Computing signals for $bench =====" && \
  CUDA_VISIBLE_DEVICES=0 python exp002/compute_signals.py \
    --model-path /root/autodl-tmp/.hf_cache/Falcon3-7B-Base \
    --adapter-path /root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_d100_s42/lora_adapter \
    --benchmark $bench \
    --signal all \
    --output-dir /root/autodl-tmp/exp002/signals/Falcon3-7B-Base_d100_s42/ \
    --batch-size 4; \
done
```

- 输出目录：`/root/autodl-tmp/exp002/signals/Falcon3-7B-Base_d100_s42/`
- 预计产出：每 benchmark 3 个 signal 文件（s1_embedding, s2_minkpp, s4_selfcritique）+ merged json
- batch_size=4（7B 模型在 24GB 上的安全值）
- 预计运行时间：2-4 小时（3 benchmarks × 3 signals，每次 model load ~2min + inference）

---
