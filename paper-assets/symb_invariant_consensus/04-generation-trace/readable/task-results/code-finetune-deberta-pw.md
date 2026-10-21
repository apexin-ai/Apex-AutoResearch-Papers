# code finetune deberta pw

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_finetune-deberta-pw_20260522T141015_result.json`
- **Structured JSON:** [`509ee59c1a2b79da5ce9.json`](../../sessions/50/509ee59c1a2b79da5ce9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出总结：

### 产出文件
1. **`/root/symb_invariant_consensus/scripts/finetune_deberta_pw.py`** (341行) — 训练脚本
2. **`/root/symb_invariant_consensus/scripts/eval_finetuned_nli.py`** (323行) — 评估+combo脚本

### Token 长度分布
| 指标 | 值 |
|------|-----|
| Mean | 151 |
| Median | 136 |
| P95 | 220 |
| P99 | 239 |
| Max | 263 |
| >512截断率 | **0%** |

max_length=512 完全够用，无需扩展。

### Dry-run 结果
仅 2 步训练（在 val 数据 80/20 split 上），已观察到 Unknown 类显著改善：

| 类别 | 预训练 (55%) | 2步后 (69.2%) |
|------|------------|--------------|
| True | 64.0% | 94.1% |
| False | 97.5% | 74.4% |
| Unknown | **3.5%** | **46.8%** |

核心瓶颈确认：预训练模型几乎不预测 Unknown（9/600），fine-tune 能修复。

### 启动训练的命令
```bash
cd /root/symb_invariant_consensus
export CUDA_VISIBLE_DEVICES=&lt;free_gpu>
export LD_LIBRARY_PATH=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13/lib:$LD_LIBRARY_PATH

# 训练（需先等 HF 数据下载完成，或手动放到 data/proofwriter_train_hf.jsonl）
python3 scripts/finetune_deberta_pw.py --epochs 5 --lr 2e-5 --batch-size 16

# 评估
python3 scripts/eval_finetuned_nli.py \
    --model-path checkpoints/deberta-large-pw-finetuned/best \
    --sc-sources llama8b qwen14b
```

### 预估训练时间
- DeBERTa-large fp32, batch_size=16, ~600 val 示例推理 ~7秒
- HF 训练集大小待确认（下载仍在后台进行，PID 626998）
- 单 GPU fp32, 预计 OWA 全深度数据 5 epoch ~10-30分钟

### 待解决
- HF 数据集下载慢（后台运行中），下载完成后会保存为 `data/proofwriter_train_hf.jsonl`
- 所有 GPU 当前被占用（仅 ~9GB 空闲），正式训练需要专用 GPU 或等现有任务结束
- DeBERTa v1 不支持 fp16/bf16 混合精度，已改为 fp32 训练

---
