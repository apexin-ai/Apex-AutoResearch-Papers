# code exp28 data efficiency

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp28-data-efficiency_20260520T152040_result.json`
- **Structured JSON:** [`efd6b4e023b95a777d33.json`](../../sessions/ef/efd6b4e023b95a777d33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp28 完成。**

结果汇总（macro F1）：

| Condition | N | IID | DD OOD | AA OOD |
|-----------|----:|:----:|:------:|:------:|
| **9class** | 50 | 1.00 | 1.00 | 0.99 |
| **9class** | 125 | 1.00 | 1.00 | 0.99 |
| **9class** | 250 | 1.00 | 1.00 | 1.00 |
| **9class** | 350 | 1.00 | 1.00 | 1.00 |
| vanilla | 125 | 0.53 | 0.24 | 0.24 |
| vanilla | 350 | 1.00 | 0.36 | 0.49 |

核心发现：
- **9class DAPT 仅需 50 条数据（14%）就达到 DD OOD=1.0, AA OOD=0.99**，比 vanilla 用全量 350 条数据（DD=0.36, AA=0.49）高出 64pp 和 50pp
- OOD 泛化优势完全来自 persuasion-grounded representation 本身，而非数据量
- 训练集扩大到 250+ 后 AA OOD 从 0.99 提升到 1.00，但即使最小子集也已接近上限
- Vanilla baseline 即使在 IID 上表现完美（n=350 时 IID=1.0），OOD 仍然严重衰退

---
