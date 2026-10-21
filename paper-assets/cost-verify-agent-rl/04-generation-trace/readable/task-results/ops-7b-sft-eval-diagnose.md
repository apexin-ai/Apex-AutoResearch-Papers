# ops 7b sft eval diagnose

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_7b-sft-eval-diagnose_20260519T074256_result.json`
- **Structured JSON:** [`7ef23f85e9ac6414ba2b.json`](../../sessions/7e/7ef23f85e9ac6414ba2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**进程退出原因**：Eval 正常完成后退出。W&B teardown 时发生 `BrokenPipeError`（asyncio stream close），导致 W&B 数据未上传，但不影响 eval 结果。

**Eval 结果（Qwen3-8B SFT on ALFWorld OOD 134 tasks）**：

| 指标 | 值 |
|---|---|
| **success rate** | **80.6%** |
| pass@1 | 80.6% |
| num_actions | 20.18 |
| action_is_valid | 96.3% |
| action_is_effective | 100% |
| reward mean@134 | 8.06 |
| best@2 mean | 9.53 |
| best@8 mean | 10.0 |

对比 1.7B SFT baseline (~6.25%)，8B SFT 在 OOD 上达到 80.6%，model scale 优势显著。

**GPU cuda:2,3**：已释放，0MiB 占用，空闲可用。四张卡全部空闲。

**磁盘**：/root/autodl-tmp 165G/250G (66%)，剩余 86G。

**已完成操作**：registry 更新为 DONE/success + metrics，cron 已删除。

---
