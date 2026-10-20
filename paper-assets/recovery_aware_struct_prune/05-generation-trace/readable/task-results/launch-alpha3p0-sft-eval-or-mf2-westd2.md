# launch alpha3p0 sft eval or mf2 westd2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_alpha3p0_sft_eval_or_mf2_westd2_20260522T102731_result.json`
- **Structured JSON:** [`73ec8a805bb6b8a1c869.json`](../../sessions/73/73ec8a805bb6b8a1c869.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正常运行。GPU 2 占用 24.9GB，正在推理 1319 个 GSM8K 测试样本。

```
执行路径: α=3.0 SFT eval
checkpoint-935 在 westd: 否（从 westb SCP 成功传输）
SCP: 成功（12GB model.safetensors + 6 个辅助文件完整到位）

Eval 已启动:
  PID: 37024
  脚本: eval_gsm8k.py → eval_gsm8k_sft_alpha3p0_20.json
  样本数: 1319
  nvidia-smi:
    GPU 0: 19251MiB, 98%
    GPU 1: 17651MiB, 98%
    GPU 2: 24954MiB, 91%  ← α=3.0 SFT eval
    GPU 3: 54119MiB, 93%
```

---
