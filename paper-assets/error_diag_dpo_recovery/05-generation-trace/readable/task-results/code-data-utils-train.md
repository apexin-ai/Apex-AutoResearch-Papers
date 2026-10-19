# code data utils train

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data-utils-train_20260512T114319_result.json`
- **Structured JSON:** [`d6e846a8e034f789d249.json`](../../sessions/d6/d6e846a8e034f789d249.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个文件和 dry-run 验证结果：

**`src/data_utils.py`** — 数据管线：
- `load_dpo_dataset()`: JSONL → 会话格式 HF Dataset，含 γ 列
- `parse_trajectory_to_messages()`: ALFWorld 轨迹文本 → ChatML assistant/user 消息
- `build_turn_ids_for_ids()`: 根据 `<|im_start|>assistant\n` 边界构建 turn_ids
- `add_turn_ids_to_dataset()`: 对 DPOTrainer 已 tokenize 的数据集追加 turn_ids 列
- `ETADNDataCollator`: 扩展 DPO collator，处理 turn_ids（padding -1）和 gamma

**`src/train_etadn.py`** — 训练入口：
- argparse CLI（所有要求的参数）
- QLoRA: 4-bit NF4 + LoRA(r=16, alpha=32)
- DPOConfig 设 `remove_unused_columns=False` 保留 gamma/turn_ids 列
- ETADNTrainer 初始化后 post-process 添加 turn_ids
- dry-run: max_steps=1, report_to="none"

**Dry-run 结果：**
```
Loss:    0.6931  (= ln(2), ✓)
VRAM:    8.0 GB
Time:    3.1s
grad_norm: 6.3125
Loss OK: True
```

---
