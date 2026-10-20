# code cwm baseline run

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cwm-baseline-run_20260511T212020_result.json`
- **Structured JSON:** [`43349a057ceb19129dc9.json`](../../sessions/43/43349a057ceb19129dc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

## 数据构建统计

| Split | 总数 | Pass | Fail |
|-------|------|------|------|
| train | 15,290 | 7,957 (52.0%) | 7,333 (48.0%) |
| val | 1,896 | 983 (51.8%) | 913 (48.2%) |
| test | 1,890 | 978 (51.7%) | 912 (48.3%) |

主要错误类型：AssertionError 占绝大多数 (~82%)，其次 SyntaxError、IndexError、TypeError。

## 训练状态

- Job `cwm-baseline` 已提交并启动
- GPU 0: 94% 利用率, 18.3/32.6 GB 显存
- LoRA trainable params: 11.8M (0.29%)
- 总 steps: 1,434（3 epochs × 15290 / (2×16)）
- 预估 ~2.97s/step → ~71 min
- 日志：`~/runs/exec-sim-repair-verifier/cwm-baseline.log`

---
