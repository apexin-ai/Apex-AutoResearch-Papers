# code datagen and detector

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_datagen_and_detector_20260513T174351_result.json`
- **Structured JSON:** [`ac330d469bd28eb3c63a.json`](../../sessions/ac/ac330d469bd28eb3c63a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已创建，语法正确，参数解析验证通过。

**`generate_synthetic.py`** — FineWeb streaming 加载 → 截取 128 tokens prompt → nucleus sampling 续写 → JSONL 输出。支持 depth 1/2/3 递归生成、multi-GPU（device_map="auto"）、checkpoint 恢复。

**`train_detector.py`** — 加载 human/synthetic JSONL → 平衡采样 → 80/10/10 split → ModernBERT-base + classification head → HF Trainer 训练（early stopping on AUC）→ TemperatureScaling 校准 → 输出 calibration_results.json + predictions.jsonl + 模型（含 temperature.pt）。校准后 `q(x) = sigmoid(logit / T)` 供下游 alpha_eff.py 使用。

---
