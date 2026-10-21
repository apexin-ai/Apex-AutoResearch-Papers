# experiment e6 closed model api

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_e6-closed-model-api_20260521T092521_result.json`
- **Structured JSON:** [`cca3f2d981cfe2484142.json`](../../sessions/cc/cca3f2d981cfe2484142.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

11 API calls, still on problem 1 trace generation. 实验正常运行。

**当前状态总结:**

| 项目 | 状态 |
|------|------|
| **API 连通性** | ✅ gpt-4o via `http://47.94.22.126/v1` 工作正常 |
| **westd-25068** | ❌ SSH 连不上（端口不可达） |
| **Dry-run (3问题)** | ✅ 3/3 正确, ~110s/问题 |
| **全量 FOLIO-204** | 🔄 PID 418902 在 westd-16639 上运行中 |
| **预计完成时间** | ~6小时（约 23:30 UTC） |

实验参数:
- 模型: `gpt-4o` (via closed-source API)
- 数据: FOLIO-204 (204 problems)
- K=12, temperature=0.7
- 含 `--save-intermediates` 和 `--resume`（可断点续跑）

实验完成后需要:
1. 从 `results.json` 读取 SC accuracy 和 SICA accuracy
2. 在 intermediates 上跑 `compute_fleiss_kappa_unified.py` 得到 Process-κ
3. 从 `per_trace_constraints` 计算 BR
4. 保存结果到 artifacts 并 register

要现在定期检查进度，还是等实验完成后再处理？

---
