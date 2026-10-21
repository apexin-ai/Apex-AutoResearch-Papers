# code plan017 14b rsft train prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan017_14b_rsft_train_prep_20260520T191330_result.json`
- **Structured JSON:** [`8ce5c467ef1ac9858cf3.json`](../../sessions/8c/8ce5c467ef1ac9858cf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据格式正确。汇总如下：

---

## 14B RSFT 训练准备状态

### 脚本（全部就绪）

| 脚本 | 路径 | 状态 |
|---|---|---|
| CED 打分 | `scripts/plan017/step2_ced_score_14b.sh` | ✅ 已完成 |
| RSFT 训练 | `scripts/plan017/step3_rsft_train_14b.sh` | ✅ 语法通过 |
| Eval (with evidence) | `scripts/plan017/step4_eval_14b_rsft.sh` | ✅ 就绪 |
| Eval (no-evidence) | `scripts/plan017/step4b_eval_14b_rsft_no_evidence.sh` | ✅ `--no_evidence` 已加 (C005) |

### 关键路径

| 项 | 路径 | 状态 |
|---|---|---|
| Qwen3-14B base | `/root/autodl-tmp/models/Qwen/Qwen3-14B/` (56GB) | ✅ |
| 14B SFT adapter | `/root/autodl-tmp/sft_output_14b/` (r=64, α=128) | ✅ |
| **Merged SFT model** | `/root/autodl-tmp/models/Qwen3-14B-sft-merged/` | ❌ 不存在 |
| CED 训练数据 | `/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl` | ✅ 3015 样本 |
| RSFT 输出 | `/root/autodl-tmp/rsft_output_14b/` | 待生成 |

### 训练参数（step3）

- **策略**: accelerate + DeepSpeed ZeRO-3 (CPU offload) × 2 GPU
- **LoRA**: rank=64, alpha=128, dropout=0.05, bf16（非 QLoRA）
- **训练**: lr=2e-5, epochs=3, batch=1/gpu, grad_accum=8, warmup=100
- **数据**: 3015 样本，CED top_k=1，selected combined_score mean=0.768
- **seed**: 42

### ⚠️ 启动前需执行的前置步骤

**1. 合并 SFT adapter**（必须先完成，预计 ~10 分钟，CPU 运行，产出 ~28GB）:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/freige
CUDA_VISIBLE_DEVICES=0 python scripts/merge_sft_adapter_14b.py
```

**2. 确认 GPU 空闲**（C001/C002）— 当前 GPU 0-3 都有占用（GPU0: 38GB, GPU1-3: ~19GB），提交前需确认目标 GPU 空闲。

**3. 启动训练**:
```bash
GPU=2,3 nohup bash /root/autodl-tmp/freige/scripts/plan017/step3_rsft_train_14b.sh > /tmp/rsft_14b_train.log 2>&1 &
```

### VRAM 预估

14B bf16 ≈ 28GB base → ZeRO-3 分两卡各 ~14GB + LoRA(r=64) + activations + gradient checkpointing → 每卡约 35-45GB。97GB/卡足够，但需要 GPU 干净。

### 磁盘

可用 114GB，merged model ~28GB + RSFT output ~1GB，充裕。

---
