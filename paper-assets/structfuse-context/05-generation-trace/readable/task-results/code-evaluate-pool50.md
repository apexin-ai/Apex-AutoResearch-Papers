# code evaluate pool50

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_evaluate-pool50_20260515T021152_result.json`
- **Structured JSON:** [`19bf026d3af9a34e40a1.json`](../../sessions/19/19bf026d3af9a34e40a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

- **数据加载**：2980 条验证样本正常解析
- **Checkpoint 发现**：找到 10 个 best checkpoint（6 个 qwen + 4 个 starcoder，含 best_by_recall_at_1 和 best_by_val_loss）
- **Pool 评估逻辑**：dummy embedding 测试中，注入信号后 R@1=0.96, R@5=1.0，符合预期

脚本已写入 `/root/structfuse/evaluation/evaluate_pool50.py`。GPU 空闲后可直接运行，例如：

```bash
# 单 checkpoint
python evaluate_pool50.py \
  --checkpoint-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1 \
  --data-path /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl \
  --pool-size 50 --num-samples 5 --gpu 0 \
  --output /root/structfuse/results/pool50_qwen_s42_r1.json

# 批量模式
python evaluate_pool50.py \
  --checkpoint-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/ \
  --data-path /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl \
  --batch-mode --pool-size 50 --gpu 0 \
  --output /root/structfuse/results/pool50_qwen_all.json
```

---
