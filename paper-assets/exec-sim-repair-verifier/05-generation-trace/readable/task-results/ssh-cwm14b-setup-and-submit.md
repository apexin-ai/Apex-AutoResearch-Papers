# ssh cwm14b setup and submit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm14b-setup-and-submit_20260522T202355_result.json`
- **Structured JSON:** [`0275ac13c4c132117ca5.json`](../../sessions/02/0275ac13c4c132117ca5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 2 已占用 ~14GB 显存，模型 checkpoint shards 正在加载。一切正常。

总结：
- **CWM 14B 训练** (`cwm14b-func-s42`) 已在 GPU 2 上启动
- train_unified.py 原生支持 `--quantize_4bit`，直接复用
- 配置：NF4 QLoRA, rank=16, alpha=32, bs=1×32, lr=5e-5, epochs=3, seed=42
- 数据：cwm_train 15280 条（10 条因超长被丢弃），cwm_val 1896 条
- 输出目录：`/root/autodl-tmp/checkpoints_cwm14b_func_s42/`
- 日志：`~/runs/exec-sim-repair-verifier/cwm14b-func-s42.log`

---
