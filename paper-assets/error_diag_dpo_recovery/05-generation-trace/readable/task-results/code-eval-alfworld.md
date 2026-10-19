# code eval alfworld

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-alfworld_20260512T131045_result.json`
- **Structured JSON:** [`3d9370dca370068f8775.json`](../../sessions/3d/3d9370dca370068f8775.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **文件**: `/root/autodl-tmp/error_diag_dpo_recovery/src/eval_alfworld.py`，9321 bytes
- **--help 验证通过**，所有 CLI 参数正常解析
- 复用了 `collect_trajectories.py` 的 8 个函数 + `PREFIXES` 常量
- `merge_and_unload` 失败时自动 fallback 到 PEFT 推理模式
- 评估使用 `temperature=0.0`（greedy decoding）

使用示例：
```bash
# 评估 base model
python src/eval_alfworld.py --run_name base_qwen3

# 评估 LoRA 微调模型
python src/eval_alfworld.py \
  --adapter_path outputs/etadn_seed42/checkpoint-100 \
  --run_name etadn_seed42
```

---
