# code exp fewshot bcs count16

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_fewshot_bcs_count16_20260523T140539_result.json`
- **Structured JSON:** [`4c959abf9584e8f73e92.json`](../../sessions/4c/4c959abf9584e8f73e92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理正常运行：
- Batch 1 (low_0, 0-shot): 108/192 correct (56.2%), 8.8s
- Batch 2 (low_1, 0-shot): 115/192 correct (59.9%), 5.8s  
- 吞吐 ~6.8K toks/s input, ~350 toks/s output
- 每个 batch 约 5-9 秒，150 conditions → 预估 ~15-20 分钟完成

实验已成功启动并正常运行。

**总结：**
- 脚本 `src/run_fewshot_bcs_count16.py` 已创建并部署
- Extreme batches: 25 low (BCS 0.405) + 25 high (BCS 0.739), count=16
- 实验在 tmux session `fewshot_bcs_count16` 中运行，PID 845785
- 实验 ID: `exp_fewshot_bcs_count16`，状态 RUNNING
- 预估 ~20 分钟完成 150 conditions × 192 samples = 28,800 inferences
- 结果将保存到 `/root/schema-dag-extraction/artifacts/exp_fewshot_bcs_count16/`

---
