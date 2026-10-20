# code urgent all server status check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_urgent_all_server_status_check_20260517T234951_result.json`
- **Structured JSON:** [`394624adc66d962255ce.json`](../../sessions/39/394624adc66d962255ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all data. The Llama retry already completed (246 lines, up from 212→215 parse success). The Qwen retry is still running (232/246). Let me compile the final report.

## westd-16980

### GPU 状态
- cuda:0: **运行中** — Qwen constrained retry (27187MiB/97887MiB, 82% util)
- cuda:1: **空闲** (0MiB, 0% util)

### Qwen Constrained (retry 进行中)
- **retry 状态**: 运行中，当前 232/246（还差 14 docs）
- 以下为 **pre-retry (backup)** 数据，retry 完成后会改善：
  - Parse Success: **197/246** (80.1%)
  - Violation: ET=0%, EV=0%, **RoV=0.4%**, AC=2.4%, CF=19.5%
  - F1: Trigger=0.138, Argument=0.018, Entity=0.138

### Llama Constrained (retry 已完成 ✓)
- **retry 状态**: 完成，246/246 lines
- Parse Success: **215/246** (87.4%) [之前 212/246=86.2%, 改善 +3 docs]
- Violation: ET=0%, EV=0%, **RoV=0%**, AC=3.4%, CF=15.5%
- F1: Trigger=0.078, Argument=0.011, Entity=0.178

### 对比：Unconstrained baselines
| | Llama Uncon | Qwen Uncon |
|---|---|---|
| Parse | 226/246 | 218/246 |
| RoV | **88.8%** | **74.9%** |
| EV | 10.5% | 24.0% |
| Trigger F1 | 0.057 | 0.118 |
| Arg F1 | 0.0 | 0.001 |
| Entity F1 | 0.0 | 0.0 |

---

## westd-21461

### GPU 状态
- cuda:0: **运行中** — Mistral constrained v2 (19535MiB/97887MiB, 80% util)
- cuda:1: **空闲** (0MiB, 0% util)

### Mistral Constrained v2 (cuda:0)
- 进度: **191/246** (77.6%), 运行中
- Violation (191 partial): ET=0%, EV=0%, **RoV=0.03%** (1/3010), AC=17.2%, CF=13.9%
- Parse failures: 53/191 (27.7%) — 较高

### Mistral Grammar_only (cuda:1) — 已完成 ✓
- 进度: **246/246** 完成
- Parse Success: 184/246 (74.8%) — 62 parse failures
- Violation: ET=0%, EV=0%, **RoV=54.8%** (!), AC=19.2%, CF=0.7%
- RoV+AC rate: 0.74 — grammar-only 约束完全没有抑制 role violations

### 空闲 GPU 列表
- westd-16980 cuda:1
- westd-21461 cuda:1

---

## 关键发现

1. **Qwen RoV**: pre-retry 仍有 0.4%，retry 完成后需重新检查（目标降到 0%）
2. **Llama constrained**: retry 将 parse success 从 212→215，RoV 已为 0% ✓
3. **Mistral grammar_only 失败**: RoV=54.8%，说明纯语法约束无法控制 role vocabulary，只有 semantic constraint (v2) 有效（v2 RoV≈0%）
4. **Mistral v2 parse failure 高** (53/191=27.7%): 需关注，可能需要后续 retry
5. **F1 全面偏低**: Entity/Trigger/Argument F1 都很低，可能是 eval 脚本的 matching 标准非常严格，或 output format 与 gold 不完全对齐

---
