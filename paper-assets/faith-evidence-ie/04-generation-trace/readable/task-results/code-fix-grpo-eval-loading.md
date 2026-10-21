# code fix grpo eval loading

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-grpo-eval-loading_20260514T150037_result.json`
- **Structured JSON:** [`97b9de28104e557e051d.json`](../../sessions/97/97b9de28104e557e051d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Smoke test 通过。加载流程正确执行：

1. Base model (Qwen3-4B) 4-bit 量化加载
2. SFT adapter 加载并 merge_and_unload()
3. GRPO adapter (checkpoint-480) 加载到 merged model 上
4. `model.generate()` 正常输出

修改完成。`inference.py` 新增 `--sft_adapter` 参数，评估 GRPO checkpoint 时用法：

```bash
python -m freige.eval.inference \
  --model_path /root/autodl-tmp/grpo_ced_r5/checkpoint-480 \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_path &lt;data_dir> --output_dir &lt;output_dir>
```

不传 `--sft_adapter` 时行为与之前完全一致。

---
