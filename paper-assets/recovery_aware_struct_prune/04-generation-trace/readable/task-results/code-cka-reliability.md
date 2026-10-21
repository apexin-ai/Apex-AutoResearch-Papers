# code cka reliability

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cka-reliability_20260515T024807_result.json`
- **Structured JSON:** [`8003058c270774fdca4b.json`](../../sessions/80/8003058c270774fdca4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Syntax check 和 dry-run 均通过。

**运行命令**（需要 GPU 时执行）：
```bash
cd /root/recovery_aware_struct_prune/src && python run_cka_reliability.py \
  --original_model /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
  --pruned_model /root/autodl-tmp/pruned_rasp_20 \
  --num_samples 1024 \
  --output /root/recovery_aware_struct_prune/artifacts/cka_reliability.json
```

**预估 GPU 运行时间：~4-5 分钟**
- 模型加载+1024 样本前向传播（原始模型）：~1.5 min
- 模型加载+1024 样本前向传播（剪枝模型）：~1.5 min
- CPU 上计算 CKA（112 groups × 8 子集 = ~900 次 CKA 调用）：~1 min

---
