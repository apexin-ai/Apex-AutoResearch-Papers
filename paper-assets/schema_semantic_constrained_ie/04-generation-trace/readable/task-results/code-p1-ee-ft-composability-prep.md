# code p1 ee ft composability prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p1_ee_ft_composability_prep_20260518T190505_result.json`
- **Structured JSON:** [`7080ef9e8fd6bc20e6c6.json`](../../sessions/70/7080ef9e8fd6bc20e6c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## P1 EE FT Composability 实验准备汇报

```
数据位置：/root/schema_semantic_constrained_ie/data/wikievents/
  all.jsonl: 246 docs (全量)
  test.jsonl: 20 docs
  SFT train: data/sft/wikievents_sft_train.jsonl (214 docs, 3586 events)
  SFT dev:   data/sft/wikievents_sft_dev.jsonl (19 docs, 365 events)

EE schema：27 entity types, 56 event types, 80 argument roles

LoRA 训练脚本：scripts/train_lora_wikievents.py
  dry-run loss: step1=0.5483, step2=0.5844
  mean token accuracy: 92.6%
  grad_norm: ~1.05

推理脚本：run_constrained_extraction.py --dataset wikievents (已有)
  dry-run 输出格式确认 ✓ (events + arguments)
  eval_event_extraction.py 兼容 ✓
  violation_checker_wikievents.py 兼容 ✓

Dry-run 状态：PASS
  训练: 2 steps OK (loss 正常, gradient 稳定)
  推理: 2 docs OK (1 parsed, 1 parse fail on long doc)
  评估: pipeline 全通

预估训练时间：~16 min (3 epochs, ~39 steps @ 24s/step)
预估推理时间：~25 min/mode (20 test docs × ~75s avg)

硬件：westd-21461 cuda:0 (RTX PRO 6000 98GB, 当前空闲)
模型：Qwen3-8B (HF cache: /root/.cache/huggingface/hub/models--Qwen--Qwen3-8B/...)
LoRA: r=16, alpha=32, dropout=0.05, max_length=4096 (6.5% truncation)

实验已注册：p1_ee_ft_composability (PREPARING)
```

**待 APPROVAL 后执行命令：**
```bash
# 1. Full training (~16 min)
CUDA_VISIBLE_DEVICES=0 python scripts/train_lora_wikievents.py \
  --model_path /root/.cache/huggingface/hub/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218

# 2. Unconstrained inference
python run_constrained_extraction.py --dataset wikievents --mode unconstrained \
  --model_path checkpoints/qwen3_8b_lora_wikievents_merged \
  --data_path data/wikievents/test.jsonl \
  --output_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl --device cuda:0

# 3. Constrained inference
python run_constrained_extraction.py --dataset wikievents --mode full_s1 \
  --model_path checkpoints/qwen3_8b_lora_wikievents_merged \
  --data_path data/wikievents/test.jsonl \
  --output_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl --device cuda:0

# 4. Evaluate + violation check
python eval_event_extraction.py --input_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl
python eval_event_extraction.py --input_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl
python violation_checker_wikievents.py --input_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl \
  --constraints_path data/wikievents/ontology_constraints_wikievents.json
```

---
