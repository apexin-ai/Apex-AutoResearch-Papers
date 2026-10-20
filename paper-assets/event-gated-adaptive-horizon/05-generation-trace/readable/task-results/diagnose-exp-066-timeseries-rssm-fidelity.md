# diagnose exp 066 timeseries rssm fidelity

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_066_timeseries_rssm_fidelity_20260524T222916_result.json`
- **Structured JSON:** [`01952d240f0973f12f46.json`](../../sessions/01/01952d240f0973f12f46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 1. 完整错误信息

日志只有两行：
```
bash: line 1: cd: /root/dreamerv3-torch: No such file or directory
EXIT_CODE=1
```

### 2. 根因

**工作目录不存在。** 实验启动脚本试图 `cd /root/dreamerv3-torch`，但 `bjb1-40020` 上根本没有这个目录。该服务器的 `/root/autodl-tmp/` 下只有 `event-gated-adaptive-horizon/`，代码仓库从未被 clone 到这台机器上。

这不是代码 bug、依赖问题或 GPU 问题——实验还没跑到 Python 就挂了。

### 3. 修复方案

在 `bjb1-40020` 上把 dreamerv3-torch 代码 clone 到 `/root/dreamerv3-torch`（或 `/root/autodl-tmp/dreamerv3-torch` 然后软链接），安装依赖后重跑。或者把实验调度到已经有代码的 `bjb1-45299` 上执行。

---
