# exp exp 005 priority1 v2

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_exp-005-priority1-v2_20260522T144606_result.json`
- **Structured JSON:** [`c676209d508bd6d14220.json`](../../sessions/c6/c676209d508bd6d14220.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job 正常启动，正在下载 DeltaNet h3-1。

**当前状态：**
- **GLA h3-1**: 已下载 ✅，待评估
- **DeltaNet h3-1**: 正在下载（~50min @ 400KB/s）
- **HGRN h3-1**: 待下载（DeltaNet 完成后开始）

**预估时间线：**
- 下载 2 个模型：~100 min
- 评估 3 个模型：~15-20 min/model = ~60 min
- 总计：~2.5-3 小时

脚本流程：下载 DeltaNet → 下载 HGRN → 验证全部 3 个模型文件 → 逐个评估（LAMBADA + ARC-Easy, `--log_samples`）。全程在 tmux 中运行，不怕 SSH 断连。

可以过 30-60 分钟后 `tail` 日志文件检查进度：
```
tail -30 /root/runs/entrainment_gated_ft/exp-005-p1-v4.log
```

---
