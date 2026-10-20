# diag mvp2 eval rsft s43

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_mvp2_eval_rsft_s43_20260515T112747_result.json`
- **Structured JSON:** [`5d18105f95dc19220b8d.json`](../../sessions/5d/5d18105f95dc19220b8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

### 1. 关键错误行
```
inference.py: error: the following arguments are required: --model_path, --data_path
EXIT_CODE=2
```

### 2. 根因
原始命令缺少两个 **required** 参数：`--model_path` 和 `--data_path`，同时使用了不存在的参数 `--rsft_adapter` 和 `--data_dir`。

脚本实际参数接口：
| 原始命令用的 | 脚本实际要求 |
|---|---|
| ❌ `--rsft_adapter` | 不存在此参数，adapter 应通过 `--model_path` 传入 |
| ❌ `--data_dir` | `--data_path`（required） |
| ❌ 未传 `--model_path` | `--model_path`（required）— 即 adapter 路径 |

脚本逻辑：`--model_path` 是 adapter 路径（或完整模型路径），`--base_model` 是底座模型路径（默认已是 Qwen3-4B），`--sft_adapter` 是可选的 SFT adapter（先合并再加载 RSFT adapter）。

### 3. 修复命令
```bash
cd /root/autodl-tmp && python -m freige.eval.inference \
  --model_path /root/autodl-tmp/rsft_output_s43 \
  --base_model /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_path /root/autodl-tmp/data/docred \
  --output_dir /root/autodl-tmp/eval_results/rsft_s43 \
  --no-quantize
```

变更：
- `--rsft_adapter` → `--model_path`（RSFT adapter 路径）
- `--data_dir` → `--data_path`
- 移除不存在的 `--gpu 0`（脚本用 `device_map="auto"`，不接受此参数）

---
