# ops cqa1 eval original only

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-eval-original-only_20260518T214436_result.json`
- **Structured JSON:** [`ace96ed661d71bc5814a.json`](../../sessions/ac/ace96ed661d71bc5814a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Monitor 已启动 (PID 159883)，正在等待 d000_s42 original 完成。

## 汇总

### 1. d000_s42 MMLU accuracy
**0.6929 (69.29%)**，9730/14042 correct。

### 2. 当前 eval 进度
- d000_s42 original 正在跑 GSM8K：194/1319 (~15%)，~9.6s/it
- GSM8K 剩余 ~3h，之后还有 arc_challenge + humaneval，d000_s42 original 总计预估还需 ~4-5h
- GPU 0: 96% utilization, 18799/24564 MiB

### 3. 已部署的切换机制
- **修复了 skip 逻辑 bug**：`run_aligned_eval_7B.sh` 的 `summary.json` → `eval_results.json`（原来永远不会 skip）
- **Monitor 脚本** (PID 159883)：轮询等待 `eval_results.json` 出现 → kill `both` 进程 → 以 `original` 模式重启，自动跳过已完成的 d000_s42

### 4. 预计完成时间
- d000_s42 original: ~4-5h (今天 ~10:00 CST)
- 切换后 original-only (9 adapters × ~5h each): ~45h → 约 2 天后全部完成

---
