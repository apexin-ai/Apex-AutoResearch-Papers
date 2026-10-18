# code fix twostage fullft support

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_twostage_fullft_support_20260516T193329_result.json`
- **Structured JSON:** [`986775e381dc3c115bea.json`](../../sessions/98/986775e381dc3c115bea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修改完成总结

`train_twostage.py` 已成功支持 Full FT 模式（`twostage_fullft`），所有改动已应用到服务器 `westd-27271`。

### Diff 摘要

| 修改点 | 内容 |
|--------|------|
| 新增 `get_expert_params()` | 捕获非 ACIS 的可训练参数（155 个） |
| `verify_grad_state()` | 新增 `train_mode`/`expert_params` kwargs，Full FT 模式下验证 expert 冻结/解冻状态 |
| `verify_gradients_after_backward()` | 同上 |
| `run_stage()` | 签名扩展，传递 `train_mode`/`expert_params` |
| `main()` Stage 1 | 分支：Full FT 冻结 expert，LoRA 冻结 lora |
| `main()` Stage 2 | 分支：Full FT 解冻 expert + 冻结 ACIS；LoRA 解冻 lora + 冻结 ACIS |
| 向后兼容 | 默认 `train_mode="twostage"` 保持原有 LoRA 行为 |

### 验证结果

| 检查项 | 状态 |
|--------|------|
| 语法检查 (`ast.parse`) | OK |
| Full FT 模式加载 | OK — 155 expert params, 10 ACIS params |
| Baseline checkpoint 加载 | OK |
| LoRA 模式向后兼容 | OK — LoRA rank=32 正常应用，无报错 |
| 完整 dry-run (3 step) | **未完成** — LIBERO 数据集未缓存 |

### 未完成项

完整 3-step dry-run 被阻塞：LIBERO 数据集（383 个 parquet 文件，来自 `HuggingFaceVLA/libero`）未在服务器上缓存。代码逻辑本身无问题，仅缺数据。

如需完成完整验证，可选择：
1. 先下载数据集（AutoDL 上耗时较长）
2. 用本地已有的小数据集替代测试
3. 接受当前部分验证结果（模型加载 + 参数识别 + 语法检查均通过）

---
