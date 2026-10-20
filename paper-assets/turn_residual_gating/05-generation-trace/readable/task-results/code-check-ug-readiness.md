# code check ug readiness

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_ug_readiness_20260518T162748_result.json`
- **Structured JSON:** [`33feb9d0c57517160a36.json`](../../sessions/33/33feb9d0c57517160a36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码确认完毕。结果如下：

```
SSH 状态: 连接失败（端口 20861 不可达）
UniformGateNetwork 类: 存在（本地 artifacts/src/threadgate.py:53）
方案A实现: 已完成
  - down_proj: Linear(3584→16)（LORA_RANK=16）
  - constant_vector: nn.Parameter(16d)（TURN_EMBED_DIM=16）
  - 后续层与 GateNetwork 完全一致（fc1, fc2, sigmoid）
train_phase2.py --gate-type uniform 支持: 是（line 95, choices=["threadgate", "uniform"]）
需要同步: 无法确认（SSH 不可达，无法对比远程文件）
就绪状态: 需要以下操作——
  1. 恢复 westd-20861 SSH 连接
  2. 将本地 artifacts/src/{threadgate.py, train_phase2.py, config.py} 同步到远程 /root/turn_residual_gating/src/
  3. 同步后方可提交训练
```

代码逻辑本身已就绪，`UniformGateNetwork` 用 `constant_vector`（可学习但不依赖 turn 信息）替代 `TurnEmbedding`，其余结构（`down_proj` → `cat` → `fc1` → `fc2` → `sigmoid`）与 `GateNetwork` 完全一致，参数量匹配。阻塞项是服务器不可达。

---
