# diagnose exp 039 14b pw600 16639

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-039-14b-pw600-16639_20260519T045511_result.json`
- **Structured JSON:** [`b68c5640b4b4b5ce9abf.json`](../../sessions/b6/b68c5640b4b4b5ce9abf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心发现：

**exp-039 不是失败，是 cron 监控误报。** 实验已成功跑完 600/600，结果完整。

- **根因**: 推理脚本正常完成后进程退出，cron 检测到 process dead 但未检查完成标记，误判为失败
- **无 OOM/无脚本错误/无 vLLM 崩溃**（dmesg 空，log 零错误）
- **结果完整可用**: results.json 含全部 600 条结果 + summary，intermediates/ 有 600 个 JSON
- **最终指标**: SICA 71.5% (429/600), SC 73.5% (441/600), extraction rate 99.2%
- **GPU 0 已释放**，可分配给新实验

报告已写入 `artifacts/diagnose_exp039.md`。

---
