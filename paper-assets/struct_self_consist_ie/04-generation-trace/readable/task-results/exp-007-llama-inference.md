# exp 007 llama inference

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp-007_llama-inference_20260514T134945_result.json`
- **Structured JSON:** [`856cf46f0194ffa9bcb5.json`](../../sessions/85/856cf46f0194ffa9bcb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

1. **sampling.py 修复** — `format_chat_prompt` 增加 try/except，兼容 LLaMA tokenizer 不支持 `enable_thinking` 参数
2. **LoRA 合并** — base model + adapter → `/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-merged/` (~15GB, bf16)
3. **Dry-run 验证** — 3 个实例 × 2 samples，JSON 格式正确，entities/relations 输出合理
4. **完整推理任务已提交** — tmux session `exp_007_llama_inference`，参数: `--n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --subtask joint`
5. **Registry 已注册** — `exp_007_llama_inference` 状态 RUNNING，server autodl-5090

SciERC test 集约 551 个实例，每个 8+1 samples，预计运行 30-60 分钟。可用 `check-training-status` 查看进度。

---
