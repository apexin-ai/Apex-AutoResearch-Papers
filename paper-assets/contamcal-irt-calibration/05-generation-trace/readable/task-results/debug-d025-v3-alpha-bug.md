# debug d025 v3 alpha bug

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_d025_v3_alpha_bug_20260515T203933_result.json`
- **Structured JSON:** [`58af0efd1ef98f692477.json`](../../sessions/58/58af0efd1ef98f692477.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完毕。结果明确。

## 调查结论

### 根因：不是 argparse bug

**当前 `train_sft.py` 代码没有 bug。** argparse 链路完全正确：

- 第 97 行：`parser.add_argument("--lora-alpha", type=int, default=DEFAULT_LORA_CONFIG["lora_alpha"], ...)` — 默认值 32
- 第 137 行：`LoraConfig(lora_alpha=args.lora_alpha, ...)` — 正确使用 `args.lora_alpha`
- 第 207 行：`"lora_alpha": args.lora_alpha` — 正确保存到 train_config.json

`--lora-alpha` → `args.lora_alpha` 的 hyphen-to-underscore 转换工作正常。

### d025_v3 的真实原因

**`Qwen2.5-3B_d025_s42` 运行时，`DEFAULT_LORA_CONFIG["lora_alpha"]` 还是 16，且 CLI 没有传 `--lora-alpha 32`。**

证据链：
| Checkpoint | lora_alpha | 时间 | 说明 |
|---|---|---|---|
| `Qwen2.5-3B_d025_s42` | **16** | 5/15 11:56 | 旧默认值，路径名无 `_a32` |
| `Qwen2.5-3B_d100_s42` | **16** | 早期 | 同批次，同样受旧默认值影响 |
| `Qwen2.5-3B_d025_v3_s42` | **32** | 更晚 | 修正后的重跑，alpha=32 |
| `Qwen2.5-3B_d025_s123` | **32** | 5/15 19:58 | 默认值已改为 32 |

路径命名也佐证：带 `_a32` 的目录（如 `d100_a32_s42_v3`）是后来显式传了 `--lora-alpha 32` 的运行；不带 `_a32` 的（如 `d025_s42`、`d100_s42`）是旧默认值时期的运行。

### 当前运行的 d100 实验：不受影响

两个实验日志都确认 alpha=32：
- `exp_001_sft_3B_d100_s42_a32_v3.log`: `LoRA config: r=16, alpha=32` ✅
- `exp_001_sft_3B_d100_s123_a32_v2.log`: `LoRA config: r=16, alpha=32` ✅

**不需要停止，没有浪费 GPU 时间。**

### 修复建议

无需修复代码——代码是正确的。问题是 `DEFAULT_LORA_CONFIG` 在项目早期用了 PEFT 默认的 `lora_alpha=16`，后来改为 32 但旧实验未重跑。`Qwen2.5-3B_d025_s42` 是过期产物，`Qwen2.5-3B_d025_v3_s42` 已经是修正后的结果。

---
