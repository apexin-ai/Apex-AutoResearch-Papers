# prep exp 010 mistral script

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp-010-mistral-script_20260517T025620_result.json`
- **Structured JSON:** [`c9d5268056817547aa7e.json`](../../sessions/c9/c9d5268056817547aa7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本创建完成，语法验证通过。

**产出汇总：**

- **脚本**: `/root/symb_invariant_consensus/scripts/run_exp010_mistral.sh` ✓ 已创建并可执行
- **模型状态**: `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/` 完整（28G，含 3 个 safetensors 分片 + config + tokenizer）
- **与 exp-011 的差异**: MODEL 路径指向 Mistral，PORT=8000，输出到 `results/exp010_mistral/`，日志写 `/tmp/vllm_exp010.log`，其余参数（K=12, T=0.7, 60题, seed=42）一致

---
