# code block corr accuracy audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_block-corr-accuracy-audit_20260512T083934_result.json`
- **Structured JSON:** [`6ae6d2d2c56c39d670e8.json`](../../sessions/6a/6ae6d2d2c56c39d670e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整对比已完成。以下是分析结果。

---

## 推理逻辑逐项对比

| 项目 | eval_verifier.py | block_correlation_analysis.py | 差异 |
|------|-----------------|------------------------------|------|
| **模型精度** | **bfloat16（无量化）** | **NF4 4-bit 量化** | **根因** |
| attn_implementation | flash_attention_2 / sdpa | 未指定（由 device_map="auto" 决定） | 次要 |
| device | `model.cuda()` | `device_map="auto"` | 次要 |
| batch_size | 16（default） | **4**（default） | 可能有影响 |
| max_new_tokens | 10 | 10 | 一致 |
| tokenization | apply_chat_template, enable_thinking=False | 同 | 一致 |
| padding | left-pad, pad_token=eos_token | 同 | 一致 |
| parse_prediction | 完全相同 | 同 | 一致 |
| eos_ids guard | `!= tokenizer.eos_token_id` | `!= tokenizer.unk_token_id` | 对 Qwen3 等效 |
| do_sample | False | False | 一致 |
| SYSTEM_PROMPT | 相同 | 相同 | 一致 |
| unparseable | 0 | 0 | 一致 |

## 根因：4-bit 量化

`block_correlation_analysis.py` 第 206-209 行用了 `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_quant_type="nf4")`，而 `eval_verifier.py` 用的是原始 bfloat16 权重。

4-bit NF4 量化将权重从 16-bit 压缩到 4-bit，精度损失约 1-2pp accuracy 在小模型上完全符合预期。29 个额外错误（1.53%）正好在这个范围内。

## 次要差异

1. **batch_size 4 vs 16**：不同 batch 内的 padding 长度不同，理论上不影响 greedy decoding 结果（attention mask 正确处理了 padding）。但与量化交互时，可能放大数值差异。
2. **attn_implementation**：eval_verifier 显式选择 flash_attention_2/sdpa，block_corr 未指定（交给 device_map="auto" 默认选择），可能选到不同实现。
3. **eos_ids guard 条件不同**：对 Qwen3 tokenizer 实际无区别（`<|im_end|>` 既不是 eos 也不是 unk）。

## 修复建议

把 `block_correlation_analysis.py` 的模型加载改为与 `eval_verifier.py` 一致（bfloat16，无量化），即可消除偏差。两个方案：

**方案 A（推荐）**：修改 `block_correlation_analysis.py`，去掉 4-bit 量化，改为 bfloat16 + flash_attn/sdpa，然后重跑。

**方案 B**：不重跑推理。用 `eval_verifier.py` 输出 per-sample predictions，然后在 block_correlation_analysis.py 中直接读取 predictions 做 block-correlation 分析（跳过推理）。

GPU 当前被占用（PID 2598022, 14572 MiB），无法立即重跑。需要等 GPU 空闲，或用方案 B 避免推理。

是否现在修改脚本？

---
