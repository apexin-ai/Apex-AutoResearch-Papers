# code impl event gate

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_impl-event-gate_20260513T012450_result.json`
- **Structured JSON:** [`5ffac03c659527d5fcf1.json`](../../sessions/5f/5ffac03c659527d5fcf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实现完成。总结：

**修改了 4 个文件 + 1 个变更文档：**

- **`configs.yaml`** — 添加 14 个 `gate_*` 超参数（`gate_enabled: false` 默认关闭）
- **`networks.py`** — RSSM 增加 `max_dt`/`dt_embed_dim` 参数和 dt embedding（`max_dt=1` 时不创建，保持原版行为）；新增 `EventGate` 类（MLP + Gumbel-Softmax，τ 从 5.0 退火到 0.5）
- **`tools.py`** — 新增 `lambda_return_variable_dt`（γ^dt 折扣）和 `subsample_variable_dt`（log-uniform dt 采样 + 累积折扣 reward）
- **`models.py`** — WorldModel 集成 EventGate + 变量 dt 子采样 + gate supervision loss（3 阶段 curriculum + λ_H 退火）；ImagBehavior 在 imagination 中用 gate 决策 dt + 适配的 lambda-return
- **`CHANGES.md`** — 逐行变更说明

**验证通过的测试：**
- 所有模块 import 正常
- EventGate 前向/后向、entropy 计算
- RSSM img_step/obs_step/observe/imagine_with_action 在有/无 dt 时均正确
- `lambda_return_variable_dt` 在 dt=1 时与原版 `lambda_return` 输出一致
- `subsample_variable_dt` 正确计算累积折扣 reward
- `gate_enabled=false` 时 RSSM 无 dt_embedding，行为与原版完全一致

---
