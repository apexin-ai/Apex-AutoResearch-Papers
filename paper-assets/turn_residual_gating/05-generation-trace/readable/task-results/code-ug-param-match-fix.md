# code ug param match fix

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ug_param_match_fix_20260518T153937_result.json`
- **Structured JSON:** [`52a5dc096ce5f000556f.json`](../../sessions/52/52a5dc096ce5f000556f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

服务器持续不可达。

**已完成的工作：**

1. **本地 `threadgate.py` 已修改** (`artifacts/src/threadgate.py`)：
   - `down_proj`: `Linear(hidden_dim, LORA_RANK)` （从 32 降回 16）
   - 新增 `constant_vector = nn.Parameter(torch.zeros(TURN_EMBED_DIM))` （16d 可训练向量）
   - `forward` 中将 `down_proj` 输出与 `constant_vector` 广播拼接后送入 fc1

2. **参数量验证通过**：修复后 UniformGateNetwork 1,667,036 vs GateNetwork 1,666,860，差异 **0.01%**（目标 <1%）

**未完成：**
- 服务器 westd-20861 SSH 连接持续失败（已尝试 10+ 次），无法将修改同步到远程 `/root/turn_residual_gating/src/threadgate.py`，也无法在服务器上运行验证脚本

服务器恢复后需要执行：
```bash
# 用修改后的内容覆盖远程文件，然后验证参数量
```

---
