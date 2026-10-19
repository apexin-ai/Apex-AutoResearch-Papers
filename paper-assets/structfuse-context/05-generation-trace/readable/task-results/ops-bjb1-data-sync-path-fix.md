# ops bjb1 data sync path fix

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-data-sync-path-fix_20260513T033421_result.json`
- **Structured JSON:** [`3c4029e022fbcb94d578.json`](../../sessions/3c/3c4029e022fbcb94d578.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出汇报：

```
=== 模型路径 ===
symlink 创建: OK
验证: safetensors 文件可访问 YES (2 files)
路径: /root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B → 嵌套 ModelScope 目录

=== 数据同步 ===
方案: B (bjb1 直接 scp 拉取 cqa1，同账户 SSH key 互通)
数据位置: /root/autodl-tmp/structfuse/m2_pilot_data/
文件: dataflow_graph.json(41M), train_dataflow.jsonl(239M), train_embedding.jsonl(274M), train_random.jsonl(242M), val.jsonl(86M)
train_random.jsonl: 2670 行
val.jsonl: 748 行

=== Dry-run ===
模型加载: OK (Qwen2.5-Coder-3B, 2 shards)
数据读取: OK (random negatives)
训练进展: 150+ steps in 90s (被 timeout 正常终止)
  step  50: loss=0.3716  lr=7.37e-06
  step 100: loss=0.3516  lr=1.47e-05
  step 150: loss=0.4246  lr=2.00e-05
GPU 1 显存: 8262 MiB
结论: READY FOR FULL TRAINING
```

---
