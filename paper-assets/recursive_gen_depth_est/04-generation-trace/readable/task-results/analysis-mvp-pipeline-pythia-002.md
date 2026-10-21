# analysis mvp pipeline pythia 002

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_pipeline_pythia_002_20260514T135037_result.json`
- **Structured JSON:** [`841262b4da2d78fbedc2.json`](../../sessions/84/841262b4da2d78fbedc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整分析。

---

## 实验结果摘要

### Pipeline 执行情况

| Step | 描述 | 状态 | 时间戳 |
|------|------|------|--------|
| 0 | Add seed_id to depth_0 | ✅ skipped (already present) | - |
| 1 | LoRA finetune depth-0 | ✅ loss=2.2411, 268s | 20:14 |
| 2 | Generate depth-1 | ✅ 5000 samples | 20:41 |
| 3 | LoRA finetune depth-1 | ✅ loss=1.3894, 268s | 20:45 |
| 4 | Generate depth-2 | ✅ 5000 samples | 21:14 |
| 5 | LoRA finetune depth-2 | ✅ loss=1.0250, 268s | 21:18 |
| 6 | Generate depth-3 | ✅ 5000 samples | 21:47 |

- **总运行时间**: ~1h47m (20:00 → 21:47)
- **每次 finetune**: ~268s (939 steps, 3 epochs, ~3.5 it/s)
- **每次生成**: ~27-29 min (5000 samples, batch_size=32×5=160)
- **训练 loss 趋势**: 2.241 → 1.389 → 1.025 (逐 depth 下降 38%→26%，模式收窄)

### 域一致性

**代码/非自然语言污染逐 depth 升级：**

| 标志 | depth-1 | depth-2 | depth-3 |
|------|---------|---------|---------|
| "Copyright" | 233 (4.7%) | 432 (8.6%) | 564 (11.3%) |
| "import java" | 63 (1.3%) | 110 (2.2%) | 189 (3.8%) |
| "#include" | 132 (2.6%) | 206 (4.1%) | 234 (4.7%) |
| "GNU General Public License" | 35 (0.7%) | 70 (1.4%) | 77 (1.5%) |

保守估计代码污染率（含 Java/C++/License 的 sample 比例）：
- **depth-1: ~5%**
- **depth-2: ~9%**
- **depth-3: ~12%**

depth-0 为纯 Wikipedia，0% 代码污染。

**样本示例（各 depth 头 2 条前 100 字符）：**

- **depth-0**: `Anarchism is a political philosophy and movement that is skeptical of all justifications for auth...` / `Albedo (; ) is the fraction of sunlight that is diffusely reflected by a body...`
- **depth-1**: `I hope you guys have a blast with it. Also I hope to see everyone posting again in the near future...` / `Background\n==========\n\nMammalian sperm acquire most of their unique characteristics...`
- **depth-2**: `I hope you guys have a nice Sunday morning. It's going to be a\nvery busy one for me as well...` / `/* * Copyright (c) 2017, 2018, Oracle and/or its affiliates. All rights reserved...` ⚠️ Java 代码
- **depth-3**: `I hope you guys have a good week and if you haven't been on Instagram you might be missing out...` / `/* * Copyright (c) 2017, 2018, Oracle and/or its affiliates. All rights reserved...` ⚠️ Java 代码

### 数据量

| depth | 样本数 | 文件大小 |
|-------|--------|----------|
| depth-0 | 5,000 | 10.5 MB |
| depth-1 | 5,000 | 8.8 MB |
| depth-2 | 5,000 | 8.9 MB |
| depth-3 | 5,000 | 9.3 MB |

### 分类结果

**未执行。** `run_pipeline.sh` 只包含 finetune→generate 循环，不包含 feature extraction 和 classifier training。

已有脚本但未被调用：
- `scripts/extract_features.py` — 特征提取（仅 depth_0_features.jsonl 已生成，depth 1-3 未提取）
- `scripts/train_classifier.py` — 分类器训练
- `scripts/run_evaluation.sh` — 评估

depth_0_features.jsonl 含 20 维特征（perplexity 统计量、surprisal、TTR、hapax ratio、n-gram entropy、重复率等），格式正确。

### Checkpoint 路径

```
checkpoints/lora_depth_0/adapter_model.safetensors
checkpoints/lora_depth_1/adapter_model.safetensors
checkpoints/lora_depth_2/adapter_model.safetensors
```

每个目录下还有 `checkpoint-939/` 子目录（中间 checkpoint）。

### W&B Run ID

无。未使用 W&B。

---

### 结论建议

**conclusion: incomplete**

**理由：**

1. **生成链完整执行**，所有 step 正常退出，数据量正确（4×5000）。但 **缺少分类评估步骤**，无法判断 PASS/FAIL。

2. **两个严重信号**：
   - **代码污染随 depth 单调递增**（5%→9%→12%），Pythia-1.4B 从预训练分布中"泄漏"出代码/license 内容，LoRA finetune 在 Wikipedia 上不足以抑制这一漂移
   - **训练 loss 快速坍缩**（2.24→1.39→1.03），模型越来越容易拟合自己生成的分布，暗示多样性衰减/模式窄化

3. **下一步**：
   - 对 depth 1-3 运行 `extract_features.py` + `train_classifier.py` 完成评估
   - 即使分类器达标，代码污染问题也会混淆"depth 信号"与"域漂移信号"——后续实验需加域过滤或 constrained decoding

---
