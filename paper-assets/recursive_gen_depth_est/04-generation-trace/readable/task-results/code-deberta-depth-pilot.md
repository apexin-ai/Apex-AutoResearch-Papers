# code deberta depth pilot

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deberta-depth-pilot_20260519T145724_result.json`
- **Structured JSON:** [`094bee514baeaec30488.json`](../../sessions/09/094bee514baeaec30488.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

- LoRA targets: `["query_proj", "value_proj"]` ✓
- Trainable params: 592,900 / 185M (0.32%) ✓
- Tokenizer 正常 ✓
- 分类 head 正确初始化（MISSING 是正常的，from pretrained MLM → seq classification）

**汇总：**

| 项目 | 状态 |
|------|------|
| 环境 | Python 3.10.12, torch 2.10+cu128, transformers 5.8.1, peft 0.7.1 |
| GPU | 2x RTX PRO 6000 (98GB), 任务用 cuda:1 |
| 模型 | `/root/autodl-tmp/models/deberta-v3-base` 已缓存 |
| 数据 | 每 cell 4×5000 条 JSONL |
| 脚本 | `/root/autodl-tmp/recursive_gen_depth_est/scripts/deberta_depth_pilot.py` |
| dry-run | `--help` + 模型加载 + LoRA 均通过 |

**需要确认**：`pythia_nucleus` 目录不存在。可用 pythia cells: `pythia_seed43`, `pythia_temp05/07/09/11`, `pythia_topk50`。建议用 `pythia_temp09` 替代，还是你有其他偏好？

训练命令示例（未启动）：
```bash
CUDA_VISIBLE_DEVICES=1 python scripts/deberta_depth_pilot.py --cell gpt2xl_temp09 --gpu 0
CUDA_VISIBLE_DEVICES=1 python scripts/deberta_depth_pilot.py --cell pythia_temp09 --gpu 0
```
（`--gpu 0` 因为 `CUDA_VISIBLE_DEVICES=1` 已将物理 GPU1 映射为逻辑 GPU0）

---
