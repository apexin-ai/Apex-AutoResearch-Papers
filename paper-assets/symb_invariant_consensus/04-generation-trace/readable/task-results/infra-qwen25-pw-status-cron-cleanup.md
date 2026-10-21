# infra qwen25 pw status cron cleanup

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_qwen25-pw-status-cron-cleanup_20260522T110830_result.json`
- **Structured JSON:** [`e1238d7b1d81f7612efd.json`](../../sessions/e1/e1238d7b1d81f7612efd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，全局清晰。

## 诊断结果

### 1. cuda:0 PW 进程状态
**PID 552333: ALIVE**，GPU 利用率 97%，显存 90159 MiB。

### 2. PW seeds 进度
| Seed | 状态 | 说明 |
|------|------|------|
| 123 | **190/600 运行中** | intermediates 有真实数据（SICA answer 正常、constraints 正常提取） |
| 456 | 未开始 | intermediates 600 个文件都是 cuda:1 垃圾数据（全空） |
| 789 | 未开始 | intermediates 600 个文件都是 cuda:1 垃圾数据（全空） |

### 3. "0% accuracy" 来源解释
**来自 cuda:1 master 脚本，不是 cuda:0。** Master 脚本在 cuda:1 上跑了 6 个实验（3 FOLIO + 3 PW）：
- FOLIO 3 seeds：正常完成（SICA=72.5-74%, SC=74-74.5%）
- PW 3 seeds：全部失败，`BadRequestError: maximum context length is 4096 tokens`——cuda:1 的 vLLM 配置了 max_model_len=4096，PW 的 prompt 超长导致 400 错误，所有问题 0 分

这些 0% 的 `results.json` 和 intermediates 是 cuda:1 留下的垃圾，cuda:0 正在逐个覆写。

### 4. ETA
- 平均 68.2s/problem
- seed=123 剩余：410 × 68.2s ≈ **7.8h**
- seed=456 + 789：1200 × 68.2s ≈ **22.7h**
- **总剩余 ≈ 30.5h，预计完成时间：~5月24日 01:40 CST**

### 5. 风险
三个 seed 目录的 `results.json` 当前都是 0% 垃圾数据。cuda:0 脚本完成每个 seed 后会覆写，不需要手动清理。但如果脚本中途挂了，需要注意区分哪些 intermediates 是真实数据、哪些是垃圾。

---
