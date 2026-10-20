# ops rebuttal mistral prep

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rebuttal-mistral-prep_20260524T035109_result.json`
- **Structured JSON:** [`73b49d04536b1f14ee0c.json`](../../sessions/73/73b49d04536b1f14ee0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。以下是汇报。

---

## 1. prepare_data.py 完整内容

```python
"""
prepare_data.py — Generate training data for 3 controlled contamination conditions (Mistral).
Uses existing mmlu_items.json from pilot to avoid re-downloading MMLU.
Contamination item selection uses seed=999 (same as Llama for cross-model comparability).
"""

import json, os, random

BASE_DIR = "/root/autodl-tmp/ctrl_contam_mistral"
PILOT_DIR = "/root/autodl-tmp/ctrl_contam_pilot"
DATA_DIR = os.path.join(BASE_DIR, "data")
ALPACA_LOCAL = os.path.join(BASE_DIR, "alpaca_data.json")

CHOICES = ["A", "B", "C", "D"]

def mmlu_item_to_qa(item):
    # 格式化为 "Question: ...\nA. ...\nB. ...\nC. ...\nD. ...\nAnswer: X"
    ...

def main():
    # 加载 MMLU items (from pilot)
    mmlu_items = json.load(open(PILOT_DIR + "/data/mmlu_items.json"))
    
    # Alpaca: seed=42 shuffle, 取前 5000 条
    alpaca_indices = list(range(len(alpaca_raw)))
    rng_alpaca = random.Random(42)
    rng_alpaca.shuffle(alpaca_indices)
    alpaca_indices = alpaca_indices[:5000]
    
    # Item selection: seed=999
    n_50 = n_mmlu // 2
    n_15 = int(n_mmlu * 0.15)
    rng_contam = random.Random(999)      # ← 确认 seed=999
    all_indices = list(range(n_mmlu))
    rng_contam.shuffle(all_indices)
    indices_50 = sorted(all_indices[:n_50])
    indices_15 = sorted(all_indices[:n_15])
    
    # 3 conditions: clean, contam_15, contam_50
    conditions = {
        "clean":      {"mmlu_indices": [],          "seed": 42},
        "contam_15":  {"mmlu_indices": indices_15,  "seed": 42},
        "contam_50":  {"mmlu_indices": indices_50,  "seed": 42},
    }
    # 输出 train.jsonl + seen_items JSON
```

## 2. train.py 完整内容

- **模型**: Mistral-7B-Instruct-v0.3, QLoRA (4bit NF4)
- **LoRA**: r=16, alpha=32, target=q/k/v/o_proj, dropout=0.05
- **训练**: 3 epochs, bs=4, grad_accum=4, lr=2e-4, warmup=0.1, max_length=512
- **SEED_MAP**: clean=42, clean_s2=123, clean_s3=456, clean_s4-s10=301-307, contam_15=42, contam_50=42
- **DATA_DIR_MAP**: clean_s2~s10 → 都读 clean 目录的数据

## 3. eval_lz.py 完整内容

- 3-shot MMLU evaluation，计算 choice logits
- MLE 估计 theta，计算 lz* (Snijders 2001 variance-corrected)
- 输出: accuracy (overall/seen/unseen), theta, lz* (overall/seen/unseen)
- 加载 seen_items: `seen_items_{pct}pct.json`

## 4. Item Selection Seed 确认

**seed=999** ✅ — `rng_contam = random.Random(999)`

与 Llama pipeline 一致，与 pilot (seed=42) 不同。

## 5. 现有数据和 Checkpoint

**数据目录** (`/root/autodl-tmp/ctrl_contam_mistral/data/`):
| 目录 | 行数 | 组成 |
|------|------|------|
| clean | 5,000 | 5000 Alpaca |
| contam_15 | 7,106 | 5000 Alpaca + 2106 MMLU (15%) |
| contam_50 | 12,021 | 5000 Alpaca + 7021 MMLU (50%) |

→ **n_mmlu = 14,042**（反推: 7021×2 = 14042, int(14042×0.15) = 2106）

**Checkpoints**: clean, clean_s2, clean_s3, clean_s8, clean_s9, clean_s10, contam_15, contam_50

## 6. 修改方案：添加 contam_5 和 contam_25

prepare_data.py 的 item selection 设计为嵌套子集（从同一个 seed=999 shuffle 序列取前 N 个）：

```
indices_5 ⊂ indices_15 ⊂ indices_25 ⊂ indices_50
```

新增的计算：
```python
n_5 = int(n_mmlu * 0.05)    # = int(14042 * 0.05) = 702
n_25 = int(n_mmlu * 0.25)   # = int(14042 * 0.25) = 3510

indices_5 = sorted(all_indices[:n_5])    # 702 items
indices_25 = sorted(all_indices[:n_25])  # 3510 items
```

**修改 conditions dict：**
```python
conditions = {
    "clean":      {"mmlu_indices": [],           "seed": 42},
    "contam_5":   {"mmlu_indices": indices_5,    "seed": 42},  # 新增
    "contam_15":  {"mmlu_indices": indices_15,   "seed": 42},
    "contam_25":  {"mmlu_indices": indices_25,   "seed": 42},  # 新增
    "contam_50":  {"mmlu_indices": indices_50,   "seed": 42},
}
```

**新增 seen_items 输出：**
```python
with open(os.path.join(DATA_DIR, "seen_items_5pct.json"), "w") as f:
    json.dump(indices_5, f)
with open(os.path.join(DATA_DIR, "seen_items_25pct.json"), "w") as f:
    json.dump(indices_25, f)
```

**预期数据量：**
| Condition | Alpaca | MMLU | Total |
|-----------|--------|------|-------|
| contam_5 | 5,000 | 702 | 5,702 |
| contam_25 | 5,000 | 3,510 | 8,510 |

**注意**：可以只生成 contam_5 和 contam_25 两个新目录，不需要重新生成 clean/contam_15/contam_50（已有数据不变，因为 seed 和子集关系保证确定性）。

## 7. 训练命令模板

train.py 也需添加新 condition 到 SEED_MAP：
```python
SEED_MAP = {
    ...
    "contam_5": 42,
    "contam_25": 42,
}
```

然后训练：
```bash
# contam_5
CUDA_VISIBLE_DEVICES=0 python train.py --condition contam_5 --gpu 0

# contam_25
CUDA_VISIBLE_DEVICES=0 python train.py --condition contam_25 --gpu 0
```

eval 时 eval_lz.py 会自动根据 condition 名加载 `seen_items_5pct.json` / `seen_items_25pct.json`（需确认 eval_lz.py 中 seen_items 文件名的拼接逻辑，可能需要小幅调整）。

---
