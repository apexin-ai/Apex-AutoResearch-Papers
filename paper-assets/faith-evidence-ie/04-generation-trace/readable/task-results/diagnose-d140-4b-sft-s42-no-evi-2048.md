# diagnose d140 4b sft s42 no evi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d140_4b_sft_s42_no_evi_2048_20260521T073628_result.json`
- **Structured JSON:** [`94503ace9da85748bdbf.json`](../../sessions/94/94503ace9da85748bdbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根因：进程被 SIGKILL 终止（无 traceback），最可能是 GPU 资源竞争导致的 CUDA OOM。**

关键事实：
- 日志在 inference 13%（31/247）处截断，无任何错误信息
- 同时段至少有 8B no-evi eval 在运行（14:28–15:36），与 4B 进程（15:06–15:24）完全重叠
- 无法从日志确认是否设置了 `CUDA_VISIBLE_DEVICES`
- Adapter 配置正确，非代码/配置 bug

**可以直接重试**，条件：
1. `CUDA_VISIBLE_DEVICES=1`（当前 GPU 1 空闲 0MiB）
2. 提交前 `nvidia-smi` 确认 GPU 1 仍空闲（C001）
3. 必须传 `--no_evidence`（C005）
4. stderr 重定向到日志（`2>&1`）以捕获 CUDA 错误

诊断已写入 `artifacts/d140_4b_sft_s42_no_evi_2048_diagnosis.md`。

---
