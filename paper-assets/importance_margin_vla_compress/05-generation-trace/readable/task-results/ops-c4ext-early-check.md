# ops c4ext early check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c4ext-early-check_20260520T115345_result.json`
- **Structured JSON:** [`c19282e5d3e219ca25d8.json`](../../sessions/c1/c19282e5d3e219ca25d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已 kill。汇总：

```
cqa1-33015 C4-ext (PID 858901):
  状态: 已 kill
  进度: Task 0/10 (pick up alphabet soup → basket), Ep 44/50
  已完成 episode SR: 0/44 = 0% (全部 FAIL，每个都跑满 280 步超时)
  判断: ❌ overfitting，已终止

westd-41074 C4-ext backup:
  状态: 已崩溃
  原因: LIBERO assets 缺失 (libero_floor_base_style.xml)
        HF 下载失败 — HF_HUB_OFFLINE 未关闭，代理下无法下载 assets
  进度: 0（未开始任何 episode）
  判断: 需修复 assets 路径或设 HF_HUB_OFFLINE=0 后重跑
```

两边 eval 都无效。cqa1 是模型本身不工作（0% SR），westd 是环境配置问题（assets 缺失）。

---
