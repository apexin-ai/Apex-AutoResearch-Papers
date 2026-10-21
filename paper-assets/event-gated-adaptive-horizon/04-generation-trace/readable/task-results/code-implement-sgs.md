# code implement sgs

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_implement_sgs_20260515T142040_result.json`
- **Structured JSON:** [`87d72a49ea3e31a764d9.json`](../../sessions/87/87d72a49ea3e31a764d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实现完成。

**修改总结**：

1. **configs.yaml**: 添加 `reward_dt_emb_detach: false` (line 120)
2. **models.py**: 
   - 在 `self._model_opt()` 调用前插入 SGS 核心逻辑 (lines 337-355)：先用 `torch.autograd.grad` 计算 reward loss 对 dt_emb 的梯度，注册 backward hook 减去该梯度，optimizer step 后移除 hook
   - 添加诊断 metrics：`dt_emb_reward_grad_norm`/`dt_emb_decoder_grad_norm` (每 1000 步)，`dt_emb_weight_norm`/`dt_emb_weight_diff_dt1_dt2` (每 5000 步)

**验证结果**：
- 语法检查通过
- Config 解析正确（`--reward_dt_emb_detach True` → `bool True`）
- 梯度正确性单元测试通过：SGS 后 dt_emb 梯度精确等于 decoder-only 梯度

**使用方式**：新实验加 `--reward_dt_emb_detach True`，不影响正在运行的 009d/015b。

---
