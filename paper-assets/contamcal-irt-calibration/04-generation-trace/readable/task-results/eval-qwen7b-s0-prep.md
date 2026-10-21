# eval qwen7b s0 prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen7b-s0-prep_20260521T070823_result.json`
- **Structured JSON:** [`b172d0b09d51e4157a31.json`](../../sessions/b1/b172d0b09d51e4157a31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. s0 Checkpoint 验证

cqa1 上 5 个 dosage 的 adapter 全部存在且完整，已复制到 westd：

| Dosage | adapter_model.safetensors | lora_alpha | 状态 |
|--------|--------------------------|------------|------|
| d000 | 161,533,192 bytes | 32 | ✅ |
| d005 | 161,533,192 bytes | 32 | ✅ |
| d025 | 161,533,192 bytes | 32 | ✅ |
| d050 | 161,533,192 bytes | 32 | ✅ |
| d100 | 161,533,192 bytes | 32 | ✅ |

路径：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d{dosage}_s0/lora_adapter/`

### 2. westd GPU 状态

| GPU | 状态 | 备注 |
|-----|------|------|
| cuda:0 | 空闲 | 0 MiB |
| cuda:1 | 占用 | 32735 MiB / 93% — 跑 Qwen-14B d100_s0 GSM8K eval |
| cuda:2 | 空闲 | 0 MiB — MMLU 脚本分配 |
| cuda:3 | 空闲 | 0 MiB — ARC 脚本分配 |

### 3. Qwen-7B Base Model 路径

`/root/autodl-tmp/models/Qwen2.5-7B`

### 4. evaluate.py MD5

`17673bf373f00f83ccc41fc1d355a4cd` — 与 reference hash 一致 (C009)

### 5. Eval 脚本

**MMLU** (已有): `/root/contamcal-irt-calibration/scripts/eval_qwen7b_s0_mmlu.sh`
- CUDA_VISIBLE_DEVICES=2
- benchmarks: mmlu, batch-size 8

**ARC** (新建): `/root/contamcal-irt-calibration/scripts/eval_qwen7b_arc_s0_batch.sh`
- CUDA_VISIBLE_DEVICES=3
- benchmarks: arc_challenge, batch-size 8

两个脚本都包含 C009 md5 校验 + C006 lora_alpha=32 检查。

### 6. 推荐执行命令

MMLU 和 ARC 可以并行跑（分别用 cuda:2 和 cuda:3）：

```bash
# MMLU on cuda:2
cd /root/contamcal-irt-calibration && mkdir -p logs && nohup bash scripts/eval_qwen7b_s0_mmlu.sh > logs/eval_qwen7b_s0_mmlu.log 2>&1 & echo "PID=$!"

# ARC on cuda:3
cd /root/contamcal-irt-calibration && mkdir -p logs && nohup bash scripts/eval_qwen7b_arc_s0_batch.sh > logs/eval_qwen7b_arc_s0_batch.log 2>&1 & echo "PID=$!"
```

---
