# code llama retry check and qwen status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_retry_check_and_qwen_status_20260517T235409_result.json`
- **Structured JSON:** [`4375bd9ad32649b4a88b.json`](../../sessions/43/4375bd9ad32649b4a88b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the report:

---

## Llama Retry 验证

**--resume 逻辑**：对 non-`full_s2` 模式，resume 仅检查 `doc_id` 是否存在于输出文件中（不检查 parse_success）。Worker 正确地在 retry 前删除了 34 条 failure 行，使 resume 识别出 212 已处理、34 待重跑。

**Retry 执行结果**：
- 重跑了全部 34 个 failure docs
- 成功恢复 3 个 → 总 parse OK: 215/246 (87.4%)
- 仍然失败 31 个

**31 docs 失败根因**：全部是 JSON 截断（mid-output truncation），不是 parse error。每个 failure doc 的 raw_output 为 23K-34K chars，生成时间一致为 ~143s（成功 docs ~75s），说明都 hit 了 max_new_tokens 上限。

**关键疑问**：`max_new_tokens` 的 **默认值是 2048**（代码中 `default=2048`）。Log 中没有记录实际使用的值，bash history 不存在。如果 retry 未显式传 `--max_new_tokens 8192`，则用的是默认 2048——和第一次跑一模一样，retry 等于白跑。

**建议**：确认后用 `--max_new_tokens 8192`（甚至 16384）重新 retry 这 31 docs。或者接受 215/246 = 87.4% parse rate。

---

## Qwen Retry 状态

**运行中**：234/246 完成，parse OK: 203/234 so far。GPU cuda:0 active (27GB, 84% utilization)。预计还需跑 12 个 docs。

---

## Grammar_only 完整报告 (Mistral, westd-21461)

**Parse**: 184/246 (74.8%)，62 parse failures

**Violation 汇总** (基于 184 个 parsed docs):

| 类型 | 数量 | 比例 |
|------|------|------|
| ET (Entity Type) | 0 | 0.0% |
| EV (Event Vocab) | 0 | 0.0% |
| **RoV (Role Vocab)** | **2314** | **54.8%** |
| **AC (Arg Constraint)** | **813** | **19.2%** |
| CF (Cross-Field) | 33 | 0.7% |
| **Go/No-go (RoV+AC)** | — | **74.1%** |

**RoV 违规最严重的 event types**：
- ArrestJailDetain.Unspecified: 97.2% 违规率 (136 RoV / 143 args)
- EndPosition.Unspecified: 98.6% (118 RoV / 140 args)
- StartPosition.Unspecified: 96.2% (91 RoV / 104 args)
- FireExplosion.Unspecified: 91.5% (97 RoV / 117 args)
- ImpedeInterfereWith.Unspecified: 91.9% (113 RoV / 197 args)
- Contact.Unspecified: 89.4% (126 RoV / 141 args)

**所有 54 个 event types 都有违规**，0 个 clean。核心问题：grammar-only 约束只保证 JSON 格式合法，不限制 role 名称是否属于对应 event type 的合法 role 集合。模型自由生成了大量无效 role（如对 Broadcast 用了 Target/Source）。

**RoV 典型案例**：`role 'Target' not valid for 'Broadcast'`, `role 'Source' not valid for 'Contact.Unspecified'`——模型在用语义上"合理"但 ontology 不认可的 role 名。

---

## Mistral v2 进度

**199/246**，parse OK: 144/199 (72.4%)。仍在运行中。

---
