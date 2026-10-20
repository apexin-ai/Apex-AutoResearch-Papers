# ssh fix analyze gates

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-analyze-gates_20260515T173145_result.json`
- **Structured JSON:** [`acc1bf591f84bdaa2177.json`](../../sessions/ac/acc1bf591f84bdaa2177.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证通过。结果汇总：

### 关键 diff

| 项 | 修改前 | 修改后 |
|---|---|---|
| `--acc_gate` 默认值 | 0.50 | **0.40** |
| `--gap_gate` 默认值 | 0.40 | **0.25** |
| Sanity-GC | 不存在 | **新增** `--sanity_gate 0.25`，DINO acc ≤ 25% |
| G3-GC | 不存在 | **新增** `--g3_gate 0.10`，Δ(trained-untrained) > 10pp |
| Gate 输出格式 | 单条 PASS/FAIL | **4 条独立 Gate** + Overall 汇总 |
| untrained 缺失处理 | 无 | G3-GC 输出 **SKIP** |
| DINO 缺失处理 | gap 按 0 算 | Sanity-GC/G2-GC 输出 **SKIP** |

### 4 Gate 实现确认

- **Sanity-GC**: DINO best acc ≤ `sanity_gate`(0.25） → PASS；> 0.25 → FAIL + "visual ambiguity not confirmed"
- **G1-GC**: trained best acc > `acc_gate`（0.40）→ PASS
- **G2-GC**: Δ(trained - DINO) > `gap_gate`（0.25）→ PASS；DINO 缺失 → SKIP
- **G3-GC**: Δ(trained - untrained) > `g3_gate`（0.10）→ PASS；untrained 缺失 → SKIP

### 语法验证
```
SYNTAX OK
```
所有 4 个新参数（`--acc_gate`, `--gap_gate`, `--sanity_gate`, `--g3_gate`）均正常注册。

---
