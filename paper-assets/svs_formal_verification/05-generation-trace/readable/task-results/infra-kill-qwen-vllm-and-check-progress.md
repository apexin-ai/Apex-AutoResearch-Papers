# infra kill qwen vllm and check progress

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill_qwen_vllm_and_check_progress_20260514T120142_result.json`
- **Structured JSON:** [`0bf890c5851d81e8ded2.json`](../../sessions/0b/0bf890c5851d81e8ded2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 任务 1：杀 vLLM 服务 ✓

- PID 41815/41816 已 kill
- GPU 2+3 显存已释放：均为 **3 MiB, 0%** 利用率
- （GPU 0+1 仍在使用：31459 MiB, 99%）

### 任务 2：mvp_003 进度

`/root/autodl-tmp/svs_formal_verification/outputs/results_partial.json` **不存在**，`outputs/` 目录也不存在。

项目中找到的 JSON 文件及 `grep -c gold_label` 原始输出：

| 文件 | gold_label 计数 |
|------|----------------|
| `outputs_dryrun/cross_model_dry_run.json` | **5** |
| `outputs_dryrun/sc_baseline_dryrun.json` | **10** |

这些都是 dryrun 输出，mvp_003 的正式 results 文件尚未生成。

---
