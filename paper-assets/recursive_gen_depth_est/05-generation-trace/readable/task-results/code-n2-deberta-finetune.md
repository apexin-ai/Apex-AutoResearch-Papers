# code n2 deberta finetune

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_n2_deberta_finetune_20260515T112648_result.json`
- **Structured JSON:** [`299a5955781a61a2960f.json`](../../sessions/29/299a5955781a61a2960f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

52M/499M，有进展了。让它继续后台下载。现在提供报告。

---

## 报告

### 脚本路径
- 本地：`src/n2_deberta_finetune.py`
- 服务器：`/root/autodl-tmp/recursive_gen_depth_est/src/n2_deberta_finetune.py`

### 数据路径确认
- `data/depth_{0,1,2,3}.jsonl` — 每个 5000 行，包含 `text` 和 `depth` 字段
- 总计 20000 samples，4 classes 均衡

### 模型缓存
- **deberta-v3-base**: `/root/autodl-tmp/models/deberta-v3-base/` (371MB, fp16 权重，已验证无 NaN)
- **roberta-base**: 正在后台下载到 HF cache (52M/499M)，PID=124867

### Dry-run 结果
- DeBERTa-v3-base dry-run **通过** — loss=1.5 (正常 4-class CE)，pipeline 端到端无错误，耗时 3s
- 本地 checkpoint 是 fp16，脚本强制 `dtype=torch.float32` 加载避免 NaN

### 提交命令

**DeBERTa-v3-base：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recursive_gen_depth_est && python src/n2_deberta_finetune.py --model_name /root/autodl-tmp/models/deberta-v3-base --output_dir results/n2_deberta_finetune --gpu 0
```

**RoBERTa-base（需等模型下载完成）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recursive_gen_depth_est && python src/n2_deberta_finetune.py --model_name /root/autodl-tmp/models/roberta-base --output_dir results/n2_roberta_finetune --gpu 0
```

### 预估运行时间
- 每 fold：16000 train / 16 batch = 1000 steps/epoch × 3 epochs = 3000 steps
- DeBERTa-v3-base max_len=512, batch=16 on RTX PRO 6000：约 ~3-4 min/epoch → ~10-12 min/fold
- 5-fold 总计：**~50-60 分钟**（每个模型）
- RoBERTa-base 速度类似

### 注意事项
- roberta-base 模型还在下载（后台 PID=124867），提交前需确认 `/root/autodl-tmp/models/roberta-base/` 下有 `model.safetensors` 或 `pytorch_model.bin`
- 如果 roberta-base 下载失败，可直接用 HF cache：`--model_name roberta-base`（需 network_turbo 代理）

---
