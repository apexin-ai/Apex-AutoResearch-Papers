# eval plan005 s43 stratified

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan005-s43-stratified_20260515T075311_result.json`
- **Structured JSON:** [`1fd4523c23bd683d630c.json`](../../sessions/1f/1fd4523c23bd683d630c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**方案 B 完成。**

### 结果

| 项目 | 状态 |
|------|------|
| GPU | 两卡 100% 占用（PID 337267: Qwen M2, PID 519791: StarCoder M2） |
| 方案选择 | **方案 B**（GPU 满，准备脚本等空闲） |
| Checkpoint | ✅ 两个都在 `/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/{random,embedding_distance}_s43/best_by_recall_at_1/` |
| stratification_index.json | ✅ `/root/autodl-tmp/structfuse/stratification_index.json` |
| evaluate_stratified.py | ✅ `/root/structfuse/scripts/evaluate_stratified.py`，dry-run 通过（3052 samples） |
| analyze_stratified.py | ✅ `/root/structfuse/scripts/analyze_stratified.py`，dry-run 通过（5 维 + 5 PDF） |
| Ready-to-run 脚本 | ✅ `/root/structfuse/scripts/run_plan005_s43.sh` |

### 执行命令（GPU 空闲后）

```bash
# 单卡执行（默认 cuda:0）
nohup bash /root/structfuse/scripts/run_plan005_s43.sh > /root/structfuse/results/plan005_s43.log 2>&1 &

# 或指定 GPU
CUDA_DEVICE=cuda:1 nohup bash /root/structfuse/scripts/run_plan005_s43.sh > /root/structfuse/results/plan005_s43.log 2>&1 &
```

脚本会对 2 个策略 × 4 个 pool_size 跑 evaluate，然后对每个 pool_size 分别跑 analyze 生成 JSON + CSV + PDF。

---
