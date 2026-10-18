# exec c4 rerun launch

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_c4_rerun_launch_20260514T093438_result.json`
- **Structured JSON:** [`b3f74f2273ac768d9dc2.json`](../../sessions/b3/b3f74f2273ac768d9dc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。以下是报告：

---

## GPU 状态

| GPU | 已用 | 总量 | 空闲 |
|-----|------|------|------|
| 0 | 45,691 MiB | 97,887 MiB | **~52 GB** |
| 1 | 88,418 MiB | 97,887 MiB | **~9.5 GB** |

**GPU 1 上有两个进程：**
- **PID 204197** — `python3 run_cross_domain.py`（67,222 MiB）— 旧的被污染数据的 cross_domain，仍在运行
- **PID 209268** — `python3 -u run_c4_cross_dataset_v2.py`（28,310 MiB）— 另一个 c4_v2 进程，**未被清理**
- PID 206887 — 已清理 ✅

## 脚本检查

`run_c4_rerun.py` 检查通过：
- 使用 concatenation 方式 ✅ — `"\n\n".join()` 拼接所有 C4 条目后传入 `build_cal_ids`，tokenize 后切 2048 窗口
- 没有 FullBitwidthProfiler ✅
- `c4_calibration.json` 是真 C4 数据 ✅（200 条，无 WikiText 标记）
- **DEVICE = "cuda:0"**（line 25），不是 cuda:1

## 结论

**GPU 1 显存不足，无法启动 c4_rerun。** 仅 ~9.5 GB 空闲，需要 ~50 GB。

需要决定：
1. **Kill PID 209268**（c4_cross_dataset_v2.py，28 GB）？— 这看起来是漏杀的旧进程
2. **Kill PID 204197**（cross_domain.py，67 GB）？— 这是用被污染数据跑的旧实验
3. 或者 **改到 GPU 0 运行**（52 GB free，脚本当前 DEVICE 就是 cuda:0）？

如果 kill 掉 GPU 1 上的两个进程，GPU 1 可腾出 ~88 GB；如果只改 GPU 0，不需要 kill 任何进程，脚本 DEVICE 也不用改。

---
