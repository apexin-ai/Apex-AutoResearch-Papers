# diagnose c5b pilot

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_c5b_pilot_20260514T184009_result.json`
- **Structured JSON:** [`55278712434c49ac3195.json`](../../sessions/55/55278712434c49ac3195.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `artifacts/c5b_pilot_diagnosis.md`。

**核心结论：cron 误判，不是实验失败。**

- c5b_pilot 代码无 bug，运行正常
- Shell 脚本 run 因未放入 screen/tmux 而在 SSH 断连时被 kill（s025 完成 15/30，s030 完成 22/30）
- 另一个 GPU3 独立 run **已成功完成 s025 全部 30 problems**，结果在 `profiling_output_c5b_all_s025/mitigation_pilot_results.json`
- GATE 判定为 FAIL（oracle recovery +18.0%，heuristic +31.7%）
- **只需补跑 s030**（等 c2 实验释放 GPU 后用 screen 启动）

---
