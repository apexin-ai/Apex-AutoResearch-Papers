# fix c2 qw n500 dup kill

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_c2_qw_n500-dup-kill_20260514T135932_result.json`
- **Structured JSON:** [`16cab2761803299945c9.json`](../../sessions/16/16cab2761803299945c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**重复进程清理完成，数据完好，实验可正常继续。**

| 项目 | 状态 |
|------|------|
| 重复进程 (132389, 132392) | 已杀掉 |
| 重复链父进程 (132372→132375, 132378→132382) | 已杀掉 |
| 重复链衍生的 s020 进程 (133732, 133666) | 已杀掉（杀 s015 后父脚本自动启动了 s020，一并清理） |
| 重复链 tmux sessions (c2_qw_n500_gpu2/gpu3) | 已自动清理 |
| 原始进程 131864 (imp s015) | 正常运行，screen `c2_qw_gpu2` |
| 原始进程 132002 (rand s015) | 正常运行，screen `c2_qw_gpu3` |
| s015 输出目录 | 空（profiling 尚在处理中，完成后写入）|
| s020 输出目录 | 空（重复进程未来得及写入数据，无污染）|
| GPU 2/3 显存 | 各 ~25 GB，仅原始进程占用，重复进程显存已释放 |

**无需重启任何实验。** s015 和 s020 的输出目录均未被污染，原始 screen 进程会按顺序正常完成所有 sparsity level。

---
