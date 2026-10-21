# ops sft qwen14b s0 sweep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sft-qwen14b-s0-sweep_20260520T092931_result.json`
- **Structured JSON:** [`0eb58064eb10fdda2ff3.json`](../../sessions/0e/0eb58064eb10fdda2ff3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动，d000 训练进行中。

**汇总：**
- 脚本：`/root/autodl-tmp/exp001/run_qwen14b_s0.sh`
- 任务：`sft_qwen14b_s0_sweep` on westd-29999 cuda:3
- 流程：d000→d005→d025→d050→d100，每个 dosage 训完后自动跑 MMLU eval
- 配置：Qwen2.5-14B, LoRA r=16 α=32, lr=5e-5, bs=1 ga=16, seed=0
- 日志：`~/runs/contamcal-irt-calibration/sft_qwen14b_s0_sweep.log`
- timeout：48h

**注意：** evaluate.py 当前 37775 bytes，C009 reference 是 37591 bytes。如果近期更新过 evaluate.py 且所有 eval 都用同一版本，则无问题；否则需确认版本一致性。

---
