# analysis read router f1

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_read_router_f1_20260517T012633_result.json`
- **Structured JSON:** [`2188c84ca1afbcb27534.json`](../../sessions/21/2188c84ca1afbcb27534.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**Checkpoint 内容：**
- Keys: `model_state_dict`, `config`
- **F1 = 0.6850**（存在 `config['f1']` 中）

**模型配置：**
- 架构: `deep_router`
- 输入维度: 16384
- 隐藏层维度: 1024
- 类别数: 3
- Dropout: 0.2
- 抽取层: [2, 4, 6, 8, 10, 12, 14, 16]
- Pooling: first_token
- Normalize: True
- LR: 0.001

**网络结构（从 state_dict 推断）：**
- `net.0`: Linear (16384 → 1024)
- `net.1`: BatchNorm1d (1024)
- `net.4`: Linear (1024 → ?)
- `net.5`: BatchNorm1d
- `net.8`: Linear (? → 3) — 输出层

**结论：3 分类 Router，best F1 = 0.685。**

---
