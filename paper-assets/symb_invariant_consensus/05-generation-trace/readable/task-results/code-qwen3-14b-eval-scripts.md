# code qwen3 14b eval scripts

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen3-14b-eval-scripts_20260518T132000_result.json`
- **Structured JSON:** [`4f07cd85e3043fac0cf0.json`](../../sessions/4f/4f07cd85e3043fac0cf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### 状态

| 项目 | 状态 |
|---|---|
| Qwen3-14B 模型 | `/root/autodl-tmp/models/Qwen3-14B/`，28GB，8/8 shard 齐全。下载进程 PID 5399 仍在运行（5h49m），但 temp 目录为空，文件应已完整 |
| vLLM | 0.21.0，支持 `Qwen3ForCausalLM`、`--reasoning-parser qwen3`、`--default-chat-template-kwargs` |
| GPU 占用 | GPU 0: exp-026 (Qwen2.5-14B, port 8000)；GPU 1-3: 空闲 |

### 创建的脚本

**`scripts/run_qwen3_14b_nonthinking.sh`** (exp-027)
- GPU 1, port 8001, `enable_thinking: false`
- K=12, T=0.7, max_tokens=4096, seed=42, max-model-len=8192
- FOLIO 204 题，与 exp-026 直接对比

**`scripts/run_qwen3_14b_thinking.sh`** (exp-028)
- GPU 2, port 8002, thinking 默认开启
- K=12, T=0.7, max_tokens=**8192**（留给 thinking 开销）, seed=42, max-model-len=**16384**
- FOLIO 204 题，测试原生推理对 constraint 质量影响

### 注意事项

1. 两个脚本可以**同时运行**（不同 GPU 和端口），也可以和 exp-026 并行
2. thinking 模式下 vLLM 的 `qwen3` reasoning-parser 会自动剥离 `&lt;think>` 内容，pipeline 收到的是纯 answer，无需修改代码
3. thinking 模式生成更慢且 token 消耗更大（约 2-3x），需要更多耐心
4. 建议先跑 exp-027（非 thinking）确保 pipeline 正常，再跑 exp-028

---
