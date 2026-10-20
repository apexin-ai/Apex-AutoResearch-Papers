# ops redocred rsft eval cuda1

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_redocred_rsft_eval_cuda1_20260516T141930_result.json`
- **Structured JSON:** [`fcb91e21ea979549056b.json`](../../sessions/fc/fcb91e21ea979549056b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并注册完成。

**实验详情：**
- **exp_id**: `plan_007_redocred_rsft_eval`
- **PID**: 352684, cuda:1
- **模型**: Qwen3-4B + SFT adapter + CED-RSFT(s43) LoRA (`rsft_output_ced_s43/checkpoint-510`)
- **数据**: Re-DocRED dev (500 docs, 7473 samples)
- **日志**: `/root/runs/faith-evidence-ie/plan_007_redocred_rsft_eval.log`

**对比基线**: Re-DocRED SFT eval (`plan_007_redocred_4b_sft_eval_r2`) Ign-F1=0.3659, Evi-F1=0.8170

**DocRED 上的增益参考**: CED-RSFT(s43) ign_f1=0.4512 vs SFT baseline ign_f1=0.3974（+5.38pp）。预计 Re-DocRED 上有类似方向的增益。

预计运行 ~55 分钟（参考 SFT eval 耗时 54 分钟，RSFT 多一层 LoRA 略慢）。

---
