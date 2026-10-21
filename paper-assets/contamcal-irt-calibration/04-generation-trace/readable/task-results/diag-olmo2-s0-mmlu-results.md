# diag olmo2 s0 mmlu results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_olmo2-s0-mmlu-results_20260520T110503_result.json`
- **Structured JSON:** [`e79f960293d52fce74c6.json`](../../sessions/e7/e79f960293d52fce74c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d050_s0 目录刚创建（18:57），空的——eval 可能刚启动或正在进行。服务器上正在跑的是 SFT 训练（phi4、qwen14b），没看到 OLMo MMLU eval 进程。

## OLMo-2-7B seed=0 MMLU 结果

| Dosage | Accuracy | Correct/Total |
|--------|----------|---------------|
| d000 | **0.5534** | 7771/14042 |
| d005 | **0.5662** | 7951/14042 |
| d025 | **0.5652** | 7937/14042 |
| d050 | 进行中（目录已创建，结果未生成） |  |
| d100 | 缺失（目录不存在） |  |

s123 seed MMLU eval 结果：全部不存在。

服务器上无 OLMo MMLU eval 活跃进程，当前 GPU 在跑 phi4 s123 SFT（cuda:0）和 qwen14b s0 SFT（cuda:3）。d050 的空目录可能是某个 eval 脚本刚创建输出目录后尚未写入结果，或进程已结束但未产出。

---
