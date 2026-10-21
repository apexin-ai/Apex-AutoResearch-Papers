# code docred sft data prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_docred_sft_data_prep_20260515T172731_result.json`
- **Structured JSON:** [`129eebf27d28b802fe19.json`](../../sessions/12/129eebf27d28b802fe19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有脚本和数据均已就绪，dry-run 成功。汇总：

### 产出

**1. SFT 数据统计**
| 指标 | 值 |
|------|-----|
| 样本数 | 3053 (train), 998 (dev) |
| 平均 chars | 5535 |
| 估算平均 tokens | ~1384 |
| 估算最大 tokens | ~3326 |
| 超 4096 tokens | 0 (0.0%) |
| 平均 entities/doc | 19.5, max 41 |
| 平均 relations/doc | 12.5, max 70 |

**2. 脚本路径**
- 数据生成：`/root/schema_semantic_constrained_ie/scripts/prepare_sft_data_docred.py`
- 训练脚本：`/root/schema_semantic_constrained_ie/scripts/train_lora_docred.py`

**3. Dry-run 结果**
- 2 steps 完成，耗时 32.9s（~16.4s/step）
- loss=0.34, mean_token_accuracy=0.956
- 无报错，模型加载和数据流正常
- `completion_only_loss=True` 生效

**4. 关键配置确认**
- max_length=4096（实际最大 ~3326 tokens，充裕）
- batch_size=2, grad_accum=8 (effective=16)
- merged 模型输出到数据盘 `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged`
- prompt 通过 import `run_constrained_extraction.py` 的 `build_messages` 保证 train/eval byte-identical

全训练预计 3053 samples × 3 epochs / 16 effective_bs ≈ 573 steps，按 ~16s/step 约 **2.5 小时**（比预估 40-60min 长，因为 max_length=4096 序列更长）。

---
