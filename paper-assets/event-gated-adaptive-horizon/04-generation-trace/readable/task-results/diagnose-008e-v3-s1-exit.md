# diagnose 008e v3 s1 exit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_008e_v3_s1_exit_20260515T004340_result.json`
- **Structured JSON:** [`9d7a04955f66cf783f56.json`](../../sessions/9d/9d7a04955f66cf783f56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在，无需删除。

---

**诊断结论：exp_008e_v3_walker_s1 正常完成 (SUCCESS)**

| 项目 | 值 |
|---|---|
| EXIT_CODE | 0 |
| 训练总步数 | 112,000（超过 target 105K） |
| 最终 eval_return@105K | **869.9** |
| value_mean@105K | 457.9 |
| v/e ratio@105K | **0.527**（健康，无 delusional critic） |
| gate_dt | 全程 dt=1（gate_dt_1_frac=1.0） |
| GPU 时间 | 5.92 小时 |

**Eval 轨迹**：31→131→156→276→382→487→581→574→657→**852→870**

Crown jewel C6 seed 1 与 seed 0 高度一致，确认 trained dt_emb + dt=1 imagination 安全，不触发 delusional critic。Registry 已更新为 DONE/success。

---
