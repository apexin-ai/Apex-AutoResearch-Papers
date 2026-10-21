# diag scale 14b sigterm

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_scale_14b_sigterm_20260522T091030_result.json`
- **Structured JSON:** [`d7dc880ecd26496af0e4.json`](../../sessions/d7/d7dc880ecd26496af0e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结论

### 四个 1.4B 实验实际涉及两种不同失败模式

**GPU 0 & 1 — t15_a060 / t15_a050 (EXIT_CODE=143, SIGTERM)**
- **根因**: 被外部 SIGTERM 杀死，**不是 OOM**
  - OOM killer 发 SIGKILL (exit code 137)，而这里是 SIGTERM (143)
  - 两个进程在完全相同的时间被杀：`2026-05-22T09:07:58Z`
  - GPU 显存仅用 ~10GB / 98GB，远未耗尽
- **进度**: 完成 gen 0 + gen 1（含 checkpoint、metrics、MAUVE），gen 2 刚开始生成合成数据时被杀
- **gen_1 metrics 完整可用**: a060 ppl=30.40, a050 ppl=20.89
- **最可能原因**: 另一个 agent session 或手动 kill（同秒杀死两个进程 = 人为/脚本操作）

**GPU 2 & 3 — t10_a060 / t10_a075 (EXIT_CODE=1, 代码 bug)**
- **根因**: `iterative_train.py:358` 的 MAUVE None 格式化 bug
  ```
  TypeError: unsupported format string passed to NoneType.__format__
  f"mauve={metrics['mauve']:.4f}"  # mauve 为 None 时崩溃
  ```
- 离线模式下 MAUVE 下载模型失败 → 返回 None → f-string 格式化崩溃
- 退出时间: `08:29:02Z` / `08:29:04Z`（比 t15 早 ~40 分钟）

### 当前状态

- **全部 4 个实验已被重启**，`--start_gen 2`，当前在 GPU 0-3 正常运行中
- GPU 4 & 5 上的 410M 实验不受影响，持续运行中
- gen_0 和 gen_1 的 partial results（checkpoint + metrics）完整可用

### 风险提醒

**t10 实验的 MAUVE bug 未修复**。重启的 t10_a060 和 t10_a075 在 gen 2 完成 metrics 计算时会再次触发同一个 `NoneType.__format__` 崩溃，除非：
1. 代码已被 patch（需确认 `iterative_train.py:358` 是否已修复）
2. 或者这次 MAUVE 恰好能连上 HuggingFace 下载成功

建议检查代码是否已修复 MAUVE None 的处理。

---
