# ssh eval 15B d000 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval-15B-d000-s42_20260513T213024_result.json`
- **Structured JSON:** [`ae7be883d39345beffda.json`](../../sessions/ae/ae7be883d39345beffda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估正常运行中。

**总结：**

1. **提交命令**：
```bash
source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && \
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && \
export CUDA_VISIBLE_DEVICES=4 && \
python /root/contamcal-irt-calibration/exp001/evaluate.py \
  --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter/ \
  --benchmarks mmlu gsm8k arc_challenge humaneval \
  --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42 \
  --cache-dir /root/autodl-tmp/.hf_cache
```

2. **PID**: 221672

3. **初始日志确认**：模型加载成功，MMLU 评估已开始，速度 ~62-65 it/s，14042 items 预计约 3.5 分钟完成 MMLU。4 个 benchmark 总计预计 5-8 分钟完成。bitsandbytes 的 libnvJitLink 警告无影响。

---
