# diagnose v2 rebuild failures

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v2_rebuild_failures_20260525T134259_result.json`
- **Structured JSON:** [`d56f8b007a1f1e7e3e31.json`](../../sessions/d5/d56f8b007a1f1e7e3e31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因

**3 个实验为同一根因：`--occ_norm_type bn` 参数未被 `finetune.py` 的 argparse 识别。**

### 错误关键行

```
finetune.py: error: unrecognized arguments: --occ_norm_type bn
```

exitcode=2（argparse 标准退出码，表示参数解析失败）。

### 分类

**代码 bug（参数缺失）**——`finetune.py` 的 argparse 中没有定义 `--occ_norm_type` 参数。v2 rebuild 启动命令引入了这个新参数，但代码侧未同步添加。

### 环境状态确认

- conda 环境 `occsafe` 存在且正常
- `finetune.py` 存在（57KB，最后修改 May 25 12:33）
- `occ_data/` 目录完整
- GPU 0-3 各约 62GB/98GB 已用（dose-response 实验在跑，正常）

### 修复

在 `finetune.py` 的 argparse 定义中添加 `--occ_norm_type` 参数。需要检查 westd-34685 上 `/root/occsafe_vla/openvla-oft/vla-scripts/finetune.py` 中 argparse 部分，确认是否已有该参数定义但未 push，还是确实遗漏。

要我现在去检查 `finetune.py` 的 argparse 定义并添加 `--occ_norm_type` 参数吗？

---
