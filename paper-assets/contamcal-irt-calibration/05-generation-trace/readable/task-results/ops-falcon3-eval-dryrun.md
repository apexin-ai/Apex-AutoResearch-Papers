# ops falcon3 eval dryrun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-eval-dryrun_20260522T072823_result.json`
- **Structured JSON:** [`6b416799000a9055346b.json`](../../sessions/6b/6b416799000a9055346b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查通过。汇报如下：

---

## Falcon3-7B-Base Eval Pipeline 兼容性检查结果

### 1. evaluate.py 兼容性：✅ 完全兼容，无需修改

| 检查项 | 结果 |
|--------|------|
| Tokenizer 加载 | `PreTrainedTokenizerFast`, vocab=131072, `trust_remote_code=True` ✓ |
| pad_token | None → 自动设为 eos (`<|endoftext|>`, id=11) ✓ |
| chat_template | None → 走 raw prompt 路径，不套 chat 格式 ✓ |
| LLAMA3_CHAT_TEMPLATE fallback | 不触发（路径不含 "llama"） ✓ |
| is_instruct | False（路径不含 "instruct"） → MCQ 用 logprob 比较 ✓ |
| ABCD choice tokens | 全部单 token（2056-2059），logprob 计算无问题 ✓ |
| mc_suffix 位置 | raw prompt 末尾 `"The answer is "` → 与其他模型一致 ✓ |
| `--max-items` | 支持（default=0 表示不限制） ✓ |

### 2. Dry-run：✅ CPU 上验证通过

- Tokenizer 加载 + prompt 构建 + token 化全部正常
- 5-shot MMLU prompt 格式 = 其他模型完全一致（raw text，无 chat wrapping）
- 未做 GPU inference（cqa1 GPU 0 在 98% 训练中），但 forward path 无 architecture-specific 分支

### 3. 分析 Pipeline：✅ 无需修改

- **compute_signals.py**：`--model-path` + `--adapter-path` 参数化，模型无关
- **IRT calibration**：`parse_model_dir_name()` 用 regex 提取 model_name，对 `Falcon3-7B-Base_d000_s42` / `Falcon3-7B-Base_d025_v3_s42` / `Falcon3-7B-Base_d100_a32_s123` 全部正确解析
- 无 model whitelist 或 hardcoded model list

### 4. 注意事项

- **SFT 后的 tokenizer**：训练后如果 adapter 目录保存了 chat_template，eval 会自动走 chat-wrapped prompt 路径（mc_suffix 在 chat 外拼接）。需确认 SFT 训练是否向 adapter 写入 chat_template — 如果是 base model LoRA 微调通常不会，但值得训练完成后验证一次。
- **7B 模型显存**：bf16 约 14GB，单卡 4090D (24GB) 足够。batch_size=8 可能偏大，建议首次用 batch_size=4。

---
