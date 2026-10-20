# code prep exp014 deepseek r1

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp014-deepseek-r1_20260517T113200_result.json`
- **Structured JSON:** [`baa107f96400213146f0.json`](../../sessions/ba/baa107f96400213146f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本就绪。验证报告：

**模型验证**
- 实际路径：`/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`（嵌套 modelscope 目录结构）
- 文件完整：`config.json` + `tokenizer.json` + 2 个 safetensors 分片
- 架构：`Qwen2ForCausalLM`，vLLM 原生支持，无需 `--trust-remote-code`

**数据验证**
- `data/proofwriter_30.json` ✓（注意：不是 `proofwriter_d5_30.json`）
- `data/folio_30.json` ✓（已是 30 题，无需 `--folio-limit`）
- `data/empty.json` ✓（用于跳过 MATH 数据，`--math-data` 是必填项）

**脚本与用户模板的差异**（按实际 argparse 修正）
- `--model-url` → `--api-base`
- `--model-name` → 不需要（mode=vllm 时 model 默认 auto，自动检测）
- `--proofwriter-data` → `--pw-data`
- `--output-dir` + `--output-file` → `--output`（单个路径）
- 无 `--folio-limit` 参数（直接用 `folio_30.json`）
- PORT 用 8000（与默认 `--api-base` 一致）

**语法检查**：通过

脚本路径：`/root/symb_invariant_consensus/scripts/run_exp014_deepseek_r1_7b.sh`

---
