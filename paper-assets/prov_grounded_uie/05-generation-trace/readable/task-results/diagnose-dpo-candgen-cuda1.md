# diagnose dpo candgen cuda1

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_dpo_candgen_cuda1_20260513T110104_result.json`
- **Structured JSON:** [`48ae42165ce4c053f206.json`](../../sessions/48/48ae42165ce4c053f206.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因明确：**参数名错误**。

脚本接受的是 `--data_file`，但启动命令传的是 `--train_file`。同时 `--seed` 也不是合法参数。

具体错误：
```
generate_dpo_candidates.py: error: unrecognized arguments: --train_file ./data/docred_train.jsonl --seed 42
```

**修复**：将启动命令中的 `--train_file` 改为 `--data_file`，删除 `--seed 42`：
```bash
python -u generate_dpo_candidates.py \
  --model_path ./outputs/sft/merged \
  --data_file ./data/docred_train.jsonl \
  --num_candidates 8 \
  --max_new_tokens 2048 \
  --top_k 20 \
  --top_p 0.95 \
  --device cuda:0 \
  --resume_from 0 \
  --max_samples 1514 \
  --output_file ./outputs/dpo_candidates_part1.jsonl
```

脚本在参数解析阶段就退出了（EXIT_CODE=2 = argparse 报错），没有进入模型加载或推理，因此**无部分产出**。

---
