# code lora perturbation

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lora_perturbation_20260518T064041_result.json`
- **Structured JSON:** [`5e41062b21c721374fd0.json`](../../sessions/5e/5e41062b21c721374fd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证通过。运行环境没有 torch/peft/sklearn（这些是 GPU 服务器上的依赖），但 AST 解析确认无语法错误。

脚本已写入 `artifacts/data/lora_perturbation_test.py`，核心设计：

- **复用** `extract_activations.py` 的 `load_samples` 和 `process_batch`，避免重复代码
- **LoRA 扰动**：`peft.get_peft_model` 随机初始化 rank-16 adapter 在 q_proj/v_proj 上，种子可控
- **AUROC 计算**：逐层将激活投影到方向向量上，取最佳层的 AUROC 与原始值比较
- **判定**：|delta| < 0.05 → ROBUST，否则 NOT_ROBUST
- **`--original-auroc`** 支持浮点数或 JSON 报告路径两种输入
- **OOM 处理**：与 extract_activations.py 相同的自动降 batch_size 策略

---
