# code gradient conflict analysis

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gradient_conflict_analysis_20260519T112257_result.json`
- **Structured JSON:** [`59b1dcadea48b12372c1.json`](../../sessions/59/59b1dcadea48b12372c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已部署到 `/root/turn_residual_gating/src/gradient_conflict_analysis.py`，`--help` 验证通过。

脚本逻辑：
- 加载 v7 checkpoint（ThreadGatedModel + LoRA + gate_params.pt）
- 遍历 ultrachat 样本，对每个样本分别 backward NTP loss 和 GAR loss（`mse_target`, target=0.5）
- 两次 backward 之间 `model.zero_grad()` 清零
- 收集 28 层 gate 参数梯度，逐层计算 cosine similarity 和 magnitude ratio
- 输出 JSON 到 `results/gradient_conflict_analysis.json` + 打印逐层分析表

默认参数匹配 v7 训练配置（`init_bias=1.5`, `gar_target=0.5`, `gar_loss_mode=mse_target`）。GPU 空闲后直接运行即可。

---
