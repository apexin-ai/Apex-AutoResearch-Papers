# ops wait cuda1 long

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_wait_cuda1_long_20260517T031227_result.json`
- **Structured JSON:** [`adcf5fcff5fc7da98aa5.json`](../../sessions/ad/adcf5fcff5fc7da98aa5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Step 1 — s43 eval 完成**
- PID 390436 已退出
- 结果：1000 docs, 27119 predictions, format_ok 99.8%, 697 truncated
- 输出在 `/root/autodl-tmp/eval_results/plan_002_test_rsft_s43/`（test split，需提交 CodaLab 获取分数）

**Step 3 — 1.7B RSFT 训练已提交**
- PID: 406515, tmux session: `rsft_1_7b`, GPU: cuda:1
- 模型: Qwen3-1.7B, 数据: 9042 samples, 3 epochs, bf16
- CED scores: min=0.000, max=0.998, mean=0.650
- trainable params: 69.7M (3.9%)
- Registry: `plan_006_qwen3_1_7b_rsft_train` → RUNNING

---
