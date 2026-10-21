# ssh p1 qwen merge and infer

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p1_qwen_merge_and_infer_20260518T221937_result.json`
- **Structured JSON:** [`99f1245b9b225001745c.json`](../../sessions/99/99f1245b9b225001745c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

## P1 EE FT Pipeline 执行结果

| Step | Status |
|------|--------|
| 0. 清理磁盘 | OK (11G 可用) |
| 1. Merge adapter | OK (16G → /root/autodl-tmp/) |
| 2. Unconstrained inference | OK (5/20 parsed) |
| 3. Full_s1 constrained inference | OK (2/20 parsed) |
| 4. Eval | OK |
| 5. Violation check | OK |

### Eval F1

| Metric | Unconstrained | Full_s1 |
|--------|--------------|---------|
| Entity F1 | 0.0000 | **0.5823** |
| Trigger F1 | 0.4598 | **0.6000** |
| Argument F1 | 0.1581 | **0.4667** |

### Violation Rates

| Type | Unconstrained | Full_s1 |
|------|--------------|---------|
| RoV | 25.1% | **0.0%** |
| AC | 6.0% | **0.0%** |
| CF | 0.0% | 3.0% |
| Go/No-go (RoV+AC) | 0.3115 | **0.0000** |

**关键发现：** constrained decoding (full_s1) 将 RoV+AC 违规率从 31.15% 降至 0%，且在成功解析的样本上 F1 全面高于 unconstrained。但 parse failure rate 很高（unconstrained 75%, full_s1 90%），这是主要瓶颈。

Registry `p1_ee_ft_composability_r4` 已更新 metrics，artifact 已注册 (art_20260518_1a2da2)。

---
