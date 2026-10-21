# fix plan014 downstream nli

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan014-downstream-nli_20260514T035317_result.json`
- **Structured JSON:** [`4d9bb1b3d0648a6da4c1.json`](../../sessions/4d/4d9bb1b3d0648a6da4c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**修改摘要：**

1. **`load_model` 函数** (line 67)：新增 `base_model` 参数。检查 checkpoint 目录是否有 `tokenizer_config.json`——有则从 checkpoint 加载 tokenizer，没有则回退到 `base_model` 路径加载；`base_model` 也未提供时抛出明确的 `ValueError`。

2. **新增 `--base_model` CLI 参数**：可选参数，指定 base model 路径用于 tokenizer 加载。

3. **调用处** (line 451)：`load_model(args.checkpoint_path, base_model=args.base_model)`。

**验证结果：**
- checkpoint 有 tokenizer → 直接加载成功
- checkpoint 无 tokenizer 且无 `--base_model` → 抛出清晰的 ValueError
- base model tokenizer 从 `/root/autodl-tmp/models/Qwen3-4B` 加载正常，vocab_size=151643

使用示例（当 checkpoint 缺 tokenizer 时）：
```bash
python scripts/eval_downstream.py \
  --checkpoint_path /path/to/checkpoint-500 \
  --base_model /root/autodl-tmp/models/Qwen3-4B \
  --data_path data/proofwriter_fol_100.jsonl \
  --output_path results/downstream.json
```

---
