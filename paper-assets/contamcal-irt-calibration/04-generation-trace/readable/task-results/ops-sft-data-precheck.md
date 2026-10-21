# ops sft data precheck

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sft-data-precheck_20260518T094049_result.json`
- **Structured JSON:** [`cf4f67aebdfc06adae5b.json`](../../sessions/cf/cf4f67aebdfc06adae5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本中无 tokenizer/model 相关引用。所有证据已收集完毕。

---

## 结论

**数据是模型无关的，所有模型共用同一套 JSONL，不需要为新模型单独生成数据。**

### 依据

1. **数据格式是纯 chat messages**（未 tokenize）：`{"messages": [{"role": "system", ...}, {"role": "user", ...}, {"role": "assistant", ...}]}`。没有 token IDs，没有 attention masks。

2. **`prepare_sft_data.py` 不涉及任何 tokenizer/model 参数**：grep tokenizer 和 model 均无匹配。脚本只做文本拼接（base SFT + paraphrased benchmark items → chat format JSONL）。

3. **`data_meta.json` 无模型绑定信息**：只记录 dosage levels、benchmark 来源、QC stats，无 tokenizer/model 字段。

4. **base 数据来自 Open-Orca/SlimOrca**（通用 chat 数据集），格式标准。

### 现有文件清单

| 文件 | 行数 | 大小 |
|---|---|---|
| `sft_dosage_000.jsonl` (0% contam) | 50,000 | 89M |
| `sft_dosage_005.jsonl` (5%) | 50,826 | 89M |
| `sft_dosage_025.jsonl` (25%) | 54,133 | 91M |
| `sft_dosage_050.jsonl` (50%) | 58,266 | 93M |
| `sft_dosage_100.jsonl` (100%) | 66,533 | 97M |

Contamination labels: 12 个文件（3 benchmarks × 4 dosages），覆盖 arc_challenge / gsm8k / mmlu。

### 对新模型矩阵的影响

Phi-4、OLMo-2、Gemma-2 等新模型直接使用现有 5 个 JSONL 文件即可。训练脚本（SFTTrainer）在加载时会用各模型自己的 tokenizer 做 on-the-fly tokenization。**无需额外数据生成步骤，20 个 SFT run 可以直接启动。**

---
