# code prewrite s123 scripts to server

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prewrite-s123-scripts-to-server_20260516T022733_result.json`
- **Structured JSON:** [`e5548d8dccc66991db9d.json`](../../sessions/e5/e5548d8dccc66991db9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已在服务器上创建完毕，语法验证通过：

| 脚本 | 路径 | 大小 |
|------|------|------|
| 0.5B s123 | `/root/contamcal-irt-calibration/exp002/run_05B_s123_signals.sh` | 1346 bytes |
| 1.5B s123 | `/root/contamcal-irt-calibration/exp002/run_15B_s123_signals.sh` | 1346 bytes |

每个脚本遍历 4 dose × 3 benchmark = 12 组合，参数名与 `compute_signals.py --help` 一致。脚本已 `chmod +x`，等 GPU 释放后可直接提交。

---
