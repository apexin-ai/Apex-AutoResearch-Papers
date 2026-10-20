# audit s123 eval final collection

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_s123-eval-final-collection_20260516T152927_result.json`
- **Structured JSON:** [`5020f407d7712bdf5513.json`](../../sessions/50/5020f407d7712bdf5513.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个 eval 结果已收集完毕，registry 已更新。

## LLaMA s123 Eval 结果汇总

| # | Eval | Status | Rate | Episodes |
|---|------|--------|------|----------|
| 1 | vanilla-s123 clean | DONE ✓ | SR=72.3% | 47 |
| 2 | vanilla-s123 injected | DONE ✓ | RR=70.2%, DR=21.3% | 47 |
| 3 | taxei-s123 clean | DONE ✓ | SR=61.7% | 47 |
| 4 | taxei-s123 injected | DONE ✓ | RR=59.6%, DR=36.2% | 47 |
| 5 | random-s123 clean | DONE ✓ | SR=76.6% | 47 |
| 6 | random-s123 injected | DONE ✓ | RR=78.7%, DR=25.5% | 47 |

**关键发现：**
- Random baseline 在 clean 和 injected 上表现最好（SR=76.6%, RR=78.7%）
- TaxEI 的 detection rate 最高（36.2%），但 recovery rate 最低（59.6%）
- Vanilla 居中（RR=70.2%, DR=21.3%）

Registry 修正：`llama31-taxei-s123-eval` 从 failed→success 并补充 metrics；新建 `llama31-random-s123-eval` 条目。GPU 2/3 上仍有两个 eval 进程在运行（可能是重复执行），已有结果文件完整。

---
