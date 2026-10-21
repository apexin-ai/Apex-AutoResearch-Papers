# code verify lora only readiness

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_lora_only_readiness_20260519T011410_result.json`
- **Structured JSON:** [`bafc1e6603dde5f74a25.json`](../../sessions/ba/bafc1e6603dde5f74a25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**远程代码版本**：三个文件均已有 `gate_type="none"` 支持，无需同步 ✓

**Eval 参数解析**：`--gate-type none` 正常接受，help 输出正确 ✓

**Dry-run 训练**：OOM 失败，但代码逻辑本身没有问题。具体情况：
- 模型加载成功（Qwen2.5-7B-Instruct）
- LoRA 注入成功：`trainable params: 5,046,272 (0.07%)`，`Gate params: 0`（符合 none 模式预期）
- 数据加载成功（8000 samples）
- 在 forward pass 时 OOM：UG 训练占 63.28 GiB，dry-run 占 17.26 GiB，总共超出 95 GiB 显存

**结论**：LoRA-only 训练和 eval 代码已就绪。等当前 UG 训练结束释放显存后即可启动正式训练，单独运行预计需要 ~18 GiB 显存，没有问题。

---
