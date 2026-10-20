# ops prep sft standard 25

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep-sft-standard-25_20260516T051945_result.json`
- **Structured JSON:** [`4cf1f254416f98708907.json`](../../sessions/4c/4cf1f254416f98708907.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成，cuda:1 已释放。

---

## 准备报告

| 检查项 | 状态 | 详情 |
|--------|------|------|
| **模型完整性** | ✅ | `model.safetensors` (11GB), `config.json`, `tokenizer.json`, `tokenizer_config.json`, `chat_template.jinja` 均存在 |
| **磁盘空间** | ✅ | `/root/autodl-tmp/` 52GB 可用（250GB 总量，80% 使用） |
| **cuda:1 状态** | ✅ | 当前空闲 (0 MiB / 0%) |
| **SFT 脚本** | ✅ | `sft_recovery.py` 参数解析正常 |
| **Dry-run 训练** | ✅ | 1 step 完成：loss=3.342, grad_norm=38.5, token_accuracy=0.5154 |
| **EOS 验证** | ✅ | token=`<｜end▁of▁sentence｜>`, id=151643 |
| **峰值显存** | ~19.5 GB（2 samples, bs=1, seq_len=2048） |

### 发现的问题及修正

1. **`--gpu` 参数冲突**：脚本内部会用 `--gpu` 值覆盖 `CUDA_VISIBLE_DEVICES`。正确用法是直接 `--gpu 1`（不需要外部设置 `CUDA_VISIBLE_DEVICES=1`）。

2. **网络依赖**：`load_dataset("openai/gsm8k")` 需要网络。正式运行前必须 `source /etc/network_turbo` 并设置：
   ```
   HF_HOME=/root/autodl-tmp/.hf_cache
   HF_HUB_DISABLE_XET=1
   REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
   SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
   ```

3. **输出目录**：正式实验必须写到 `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/`（不要用 /tmp，tmpfs 空间不够存 11GB 模型）。

### 正式运行命令（审批后执行）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
cd /root/recovery_aware_struct_prune

python -u src/sft_recovery.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 \
  --gpu 1 \
  --num_train_epochs 2 \
  --learning_rate 2e-5 \
  --batch_size 1 \
  --gradient_accumulation_steps 8 \
  --max_seq_length 2048 \
  --logging_steps 10 \
  --seed 42
```

实验就绪，等待 Director 审批。

---
