# code create 4b no evidence eval script

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_create_4b_no_evidence_eval_script_20260519T135844_result.json`
- **Structured JSON:** [`cb8a7fc79c86ab0e7c4d.json`](../../sessions/cb/cb8a7fc79c86ab0e7c4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本 `scripts/d112/eval_4b_rsft_no_evidence.sh` 已存在，权限可执行（`-rwxr-xr-x`），创建于 2026-05-19 21:45。

内容摘要：
- 基于 `eval_d112_rsft_bf16.sh`，添加了 `--no_evidence` 参数（符合 C005 约束）
- `output_dir` 改为 `/root/autodl-tmp/eval_results/d112_rsft_bf16_no_evidence`
- GPU 使用 `${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`（符合 C002 约束）
- checkpoint 路径指向 `/root/autodl-tmp/rsft_output_4b_sft_s44_bf16`
- SFT adapter 路径 `/root/autodl-tmp/sft_output_seed44`

脚本内容正确，无需额外修改。之前 eval 失败（EXIT_CODE=127）可能是路径拼写不同——任务提交时引用的路径需与实际文件路径一致。

---
