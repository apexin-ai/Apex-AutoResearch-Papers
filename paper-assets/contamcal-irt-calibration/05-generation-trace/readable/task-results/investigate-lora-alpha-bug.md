# investigate lora alpha bug

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_lora-alpha-bug_20260515T150214_result.json`
- **Structured JSON:** [`58e19e270ed380dfa61f.json`](../../sessions/58/58e19e270ed380dfa61f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成，以下是结论。

---

## 调查报告：`--lora-alpha` 参数传递问题

### 结论：`train_sft.py` 本身无 bug

argparse 定义和传递链完全正确：

```
--lora-alpha → dest=lora_alpha → args.lora_alpha → LoraConfig(lora_alpha=args.lora_alpha)
```

代码逻辑无误，`--lora-alpha 16` 如果被正确传入，会按预期工作。

### 真正的问题

**`exp_001_sft_3B_d025_s123` 的实际提交命令没有传入 `--lora-alpha 16`**（或该参数被忽略/遗漏），导致使用了 `DEFAULT_LORA_CONFIG["lora_alpha"] = 32` 的默认值。

三重证据确认：
1. **训练日志**：`LoRA config: r=16, alpha=32`
2. **train_config.json**：`"lora_alpha": 32`
3. **adapter_config.json**：`"lora_alpha": 32`

### 全量影响扫描（26 个实验）

| alpha 值 | 实验数 | 涉及模型 |
|---------|--------|---------|
| **32**（默认值）| **21** | 全部 0.5B (8), 全部 1.5B (8), 3B d000/d005/d025_s123 (5) |
| **16**（手动指定）| **5** | 3B d000_v2 (2), 3B d025_s42 (1), 3B d100 (2) |

**关键问题：alpha 在实验间不一致。** 同一 dosage 的不同 seed 之间 alpha 不同（如 3B_d025_s42 用 16，3B_d025_s123 用 32），这会污染 seed 间的可比性。

### 附加发现

`run_exp001.sh` 中的训练调用：
```bash
python3 "$SCRIPT_DIR/train_sft.py" \
    --model-name "$model" \
    --data-path "$data_file" \
    --output-dir "$run_dir" \
    --seed "$seed" \
    --gpu "$gpu_id" \       # ← train_sft.py 没有 --gpu 参数
    --cache-dir "$CACHE_DIR"
    # ← 没有 --lora-alpha，没有 --lora-r
```

脚本没有暴露 LoRA 超参数，且传了一个不存在的 `--gpu` 参数（说明实验可能不是通过此脚本提交的，而是手动/任务系统单独提交）。

### 建议

不需要修 `train_sft.py`（代码正确）。需要决定的是：

1. **alpha=32 和 alpha=16 哪个是实验的 intended 值？** 这决定了哪些实验需要重跑
2. 如果 intended 是 16，可以把 `DEFAULT_LORA_CONFIG["lora_alpha"]` 从 32 改为 16，减少未来遗漏的风险
3. `run_exp001.sh` 的 `run_train()` 需要补上 `--lora-alpha` 参数转发

需要我改默认值或修 `run_exp001.sh` 吗？

---
