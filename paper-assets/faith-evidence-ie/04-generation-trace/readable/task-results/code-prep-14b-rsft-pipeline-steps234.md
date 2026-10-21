# code prep 14b rsft pipeline steps234

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_14b_rsft_pipeline_steps234_20260519T192430_result.json`
- **Structured JSON:** [`ce6dbb1180b2740de642.json`](../../sessions/ce/ce6dbb1180b2740de642.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个脚本已创建，全部通过 `bash -n` 语法验证。

| 脚本 | 用途 | GPU |
|------|------|-----|
| `step2_ced_score_14b.sh` | CED scoring + top_k=1 筛选 | 单卡（默认 0） |
| `step3_rsft_train_14b.sh` | RSFT LoRA 训练（accelerate + ZeRO-3） | 双卡（默认 2,3） |
| `step4_eval_14b_rsft.sh` | D076 eval（with evidence） | 双卡（默认 2,3） |
| `step4b_eval_14b_rsft_no_evidence.sh` | D076 eval no-evidence 变体 | 双卡（默认 2,3） |

注意事项：
- **step3 前需先合并 SFT adapter**：`Qwen3-14B-sft-merged` 不存在，脚本里有 pre-flight check 和提示，需先运行 `python scripts/merge_sft_adapter_14b.py`
- 所有脚本支持 `GPU=x,y` 环境变量覆盖默认 GPU 分配
- eval 脚本遵守 C001（提交前须确认 GPU 空闲）、C002（显式设 CUDA_VISIBLE_DEVICES）、C005（no-evidence 变体传 `--no_evidence`）

---
