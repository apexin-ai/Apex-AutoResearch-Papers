# code shortgpt prune westd cuda3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_shortgpt_prune_westd_cuda3_20260519T141510_result.json`
- **Structured JSON:** [`98fce73680f18dad85e8.json`](../../sessions/98/98fce73680f18dad85e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SFT 训练已启动并正常运行：
- 7473 samples tokenized, 2 epochs, 1870 steps
- ~1.15 it/s, 预计 ~27 分钟完成
- cuda:3 占用 52.8GB, 88% 利用率

**总结：**

1. **ShortGPT pruning 完成** ✓
   - 模型：DeepSeek-R1-Distill-Qwen-7B, 28 → 23 层
   - 移除层：[15, 16, 17, 24, 25]（BI 最低的 5 层）
   - 参数：7.62B → 6.45B (15.30% sparsity)
   - 输出：`/root/autodl-tmp/recovery_aware_struct_prune/shortgpt_20`

2. **SFT warmup 训练已提交** ✓
   - exp_id: `sft_shortgpt_20`，westd-29022 cuda:3，PID 112015
   - 超参与其他方法一致：2 epochs, lr=2e-5, batch=1, grad_accum=8, seq_len=2048
   - Registry 状态：RUNNING
   - 预计 ~27 分钟完成

---
