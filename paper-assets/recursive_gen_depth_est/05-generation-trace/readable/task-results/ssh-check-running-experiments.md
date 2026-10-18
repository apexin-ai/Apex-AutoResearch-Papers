# ssh check running experiments

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_running_experiments_20260514T200924_result.json`
- **Structured JSON:** [`3bd8da69a40fb4239dc4.json`](../../sessions/3b/3bd8da69a40fb4239dc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

### GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 (pythia) | 45% | 15.4 / 97.9 GB |
| 1 (gpt2xl) | 91% | 35.0 / 97.9 GB |

---

### pythia_topk50_001 (cuda:0) — Pythia-1.4B top-k k=50

**Pipeline: 6 步 (3轮 finetune + 3轮 generate)**

| 步骤 | 状态 |
|------|------|
| Step 1: LoRA finetune depth-0 | ✅ 完成 |
| Step 2: Generate depth-1 | ✅ 完成 |
| Step 3: LoRA finetune depth-1 | ✅ 完成 |
| Step 4: Generate depth-2 | ✅ 完成 |
| Step 5: LoRA finetune depth-2 | ✅ 完成 (loss=1.437, 355s) |
| **Step 6: Generate depth-3** | **🔄 进行中 — 模型已加载，生成中** |

**进度**: 5/6 步完成，~85%。最后一步（depth-3 生成）从 03:41 UTC 开始，预计还需 ~10-15 分钟。

---

### gpt2xl_temp09_001 (cuda:1) — GPT-2 XL temp τ=0.9

**Pipeline: 同样 6 步**

| 步骤 | 状态 |
|------|------|
| Step 1: LoRA finetune depth-0 | ✅ 完成 |
| Step 2: Generate depth-1 | ✅ 完成 (5000 samples) |
| **Step 3: LoRA finetune depth-1** | **🔄 进行中 — 622/939 steps (66%), ~1.15s/it** |
| Step 4: Generate depth-2 | ⏳ 待执行 |
| Step 5: LoRA finetune depth-2 | ⏳ 待执行 |
| Step 6: Generate depth-3 | ⏳ 待执行 |

**进度**: 2.66/6 步，~44%。当前 finetune 剩 ~6 分钟，之后还有 3 步（gen+ft+gen），预计还需 ~50-60 分钟。

---

### 结果文件
`results/` 下尚无 `pythia_topk50/` 或 `gpt2xl_temp09/` 目录（两个 pipeline 只做生成链，不含 feature_extract/classify 步骤）。pipeline 完成后产出在 `data/` 和 `checkpoints/` 下。

---
