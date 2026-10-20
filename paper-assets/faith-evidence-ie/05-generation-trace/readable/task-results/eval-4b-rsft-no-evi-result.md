# eval 4b rsft no evi result

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_4b-rsft-no-evi-result_20260523T000332_result.json`
- **Structured JSON:** [`75d4e17620ed6b9746be.json`](../../sessions/75/75d4e17620ed6b9746be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前 session 无 cron，已在之前 session 过期或清理。

## 4B RSFT no-evi test 结果
状态: **success** (进程已退出，结果完整)

| 指标 | 值 |
|------|-----|
| ign_f1 | **0.2652** |
| f1 | 0.2652 |
| precision | 0.3557 |
| recall | 0.2115 |
| evi_f1(DREEAM) | 0.0014 |
| evi_f1(TP) | 0.0074 |
| EDCR | 0.80 |
| truncated | 224/500 (44.8%) |
| format_ok | 500/500 (100%) |

**RSFT test evidence tax: no_evi(0.2652) - with_evi(0.2501) = +1.51pp**

no-evidence 反而比 with-evidence 高 1.5pp，与 dev 上观察到的 evidence tax 方向一致（去掉 evidence 输出要求后，模型可以把更多 token budget 用于关系抽取本身）。

Registry 已更新为 DONE/success。

## 14B s43 generation 状态
状态: **进行中** (PID 194682, 运行 5h47m)
进度: **993/3027 docs (32.8%)**
预计剩余: ~20s/doc × 2034 docs ≈ **11-12 小时**

---
