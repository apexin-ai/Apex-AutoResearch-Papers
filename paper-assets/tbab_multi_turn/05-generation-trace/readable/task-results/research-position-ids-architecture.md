# research position ids architecture

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_position-ids-architecture_20260518T051041_result.json`
- **Structured JSON:** [`12c6aa20884ccd8e2a89.json`](../../sessions/12/12c6aa20884ccd8e2a89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/position_ids_architecture_report.md` 并注册。

核心结论：

1. **position_ids 可以自定义传入**，无需修改模型代码，但**必须同时传入 4D attention mask**绕过 packed sequence 检测（否则 turn 间 attention 被阻断）

2. **rope_theta 实际是 1,000,000**（非 10000），频段恢复理论的距离阈值需要重新计算

3. **MVP 实现路径**：词表扩展 + PEFT `trainable_token_indices`（原生支持 bridge token embedding 训练和序列化），LoRA `target_modules="all-linear"`, r=32, lora_alpha=64

4. **Bridge token position 推荐**：归属前一 turn 末尾（position 继续累加），reset 在 bridge 之后发生

5. **主要风险**：4D mask 的显存开销（seq_len^2）、FlashAttention 兼容性、KV cache 推理需要自定义 generate 逻辑

---
