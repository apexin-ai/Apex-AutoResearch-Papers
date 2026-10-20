# verify docred s1 lora effectiveness

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_docred-s1-lora-effectiveness_20260522T060809_result.json`
- **Structured JSON:** [`9d7674374426d4decfab.json`](../../sessions/9d/9d7674374426d4decfab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：LoRA **已生效**

三路对比（同一个 Skai TV 样本）：

| 维度 | LoRA S1 constrained (21461) | LoRA unconstrained (16980) | ZS S1 (21461) |
|------|---|---|---|
| Entities | 10 | 10 | 10 |
| Relations | **8** | **8** | 8 |
| 日期实体 | `1st of April 2006` (TIME) | `1st of April 2006` (TIME) | `April` (TIME) + `2006` (NUM) ← 拆碎了 |
| "Greek" 实体 | ✅ 提取 (LOC) | ✅ 提取 (LOC) | ❌ 漏掉 |
| Relation type 风格 | `country`, `parent organization`, `official language` | 完全一致 | `location`, `part of`, `country of origin`, `operator` |
| 多实体对关系 | Piraeus→Greece, Athens→Greece, Skai Group→Greece, Digea→Greece 都提取 | 完全一致 | 只有 Skai TV 为 head 的关系 |

**关键证据：**

1. **westd-21461 S1 constrained 与 westd-16980 unconstrained 输出逐字一致**——相同 entities、相同 relations、相同 relation type 命名。两者都是 LoRA 模型的输出。

2. **两者与 ZS 有显著差异**：
   - LoRA 使用 DocRED 训练 schema 对齐的 relation names（`country` vs `country of origin`，`parent organization` vs `part of`）
   - LoRA 提取多实体对关系（不仅仅以主实体为 head），ZS 只做单主体关系
   - LoRA 正确处理复合日期实体，ZS 拆碎

3. **日志确认**：PEFT warning `Unsupported layer type AwqMarlinLinear` 只是 warning，不是 error。monkey-patch 方式绑定的 LoRA 仍然在权重层面生效了（跳过的只是 PEFT 的层类型检查，不是实际的权重合并）。

4. **推理已完成 25/200 样本**，正常运行中。

---
