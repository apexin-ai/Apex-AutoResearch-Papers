# ops pool50 eval assessment

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pool50_eval_assessment_20260516T031710_result.json`
- **Structured JSON:** [`e0bd2c1904c17c28c468.json`](../../sessions/e0/e0bd2c1904c17c28c468.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正在运行，发现 12 个 checkpoints（6 × best_by_recall_at_1 + 6 × best_by_val_loss）。

## GPU 需求
- **需要 GPU**: yes — 加载 Qwen2.5-Coder-3B 做 embedding inference
- **VRAM 需求**: ~16GB（base model ~6GB + LoRA weights + inference activations with batch_size=32, max_seq_length=2048）
- **能否与训练并行**: yes — GPU 0 原剩余 ~47GB，eval 占 ~16GB 后仍剩 ~31GB
- **预估运行时间**: ~10-12 min/checkpoint（encoding ~9min + pool50 eval ~1-2min）。12 个 checkpoints → 总计 ~2-2.5 小时

## 可用 Checkpoints（全部存在且完整）
| Checkpoint | 路径 |
|---|---|
| random_s42/best_by_recall_at_1 | `/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1` |
| random_s43/best_by_recall_at_1 | `…/random_s43/best_by_recall_at_1` |
| random_s44/best_by_recall_at_1 | `…/random_s44/best_by_recall_at_1` |
| embedding_distance_s43/best_by_recall_at_1 | `…/embedding_distance_s43/best_by_recall_at_1` |
| embedding_distance_s44/best_by_recall_at_1 | `…/embedding_distance_s44/best_by_recall_at_1` |
| dataflow_aware_s43/best_by_recall_at_1 | `…/dataflow_aware_s43/best_by_recall_at_1` |

model.pt 大小: 5.8GB/each。另外 `--batch-mode` 还发现了 6 个 `best_by_val_loss` checkpoint，一并评估。

## Eval 启动状态
- **测试运行**: pass — 脚本正常加载模型、编码中，GPU 0 VRAM 从 50.3GB → 66.6GB，与训练安全并行
- **批量运行**: 已启动（nohup，PID=138134）
  - 脚本: `/root/structfuse/evaluation/evaluate_pool50.py --batch-mode`
  - GPU: `CUDA_VISIBLE_DEVICES=0`（cuda:0）
  - Val data: `val_random_s42.jsonl`（2980 queries，所有 checkpoints 统一用同一 val set）
  - pool=50, 5 trials, batch_size=32
  - 日志: `/tmp/pool50_eval.log`
  - 结果输出: `/root/autodl-tmp/structfuse/results/pool50_eval_qwen_all.json`
  - 预计完成: ~2-2.5 小时后（约 08:00 UTC）

轮询命令：`tail -20 /tmp/pool50_eval.log`

---
