# fix westd41074 dup kill and gpu3 redeploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd41074_dup_kill_and_gpu3_redeploy_20260524T212435_result.json`
- **Structured JSON:** [`1c2e124a78851f09e1a5.json`](../../sessions/1c/1c2e124a78851f09e1a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出

```
操作1: PID 877990=dead, PID 898331=dead（两个原始进程均已消失）
        GPU1 当前进程: PID 959698 (OpenVLA Attn k=0.9 Spatial s42, 运行 1h43m)
        GPU1 进程数=1 ✓

操作2: 部署失败 ❌
        原因: westd-27271 只有 2 块 GPU (GPU0, GPU1)，不存在 GPU3
        - GPU0: PID 958937 (OpenVLA Attn k=0.9 Goal s42)
        - GPU1: PID 959698 (OpenVLA Attn k=0.9 Spatial s42)
        两块 GPU 均被占满，无空闲 GPU 可用

根因: 未发现自动重启机制（无 crontab、无 systemd 服务、无 tmux session）
      重复进程大概率是手动/agent 重复发起导致
```

**需要你决策**：Random k=0.9 Spatial s43 需要等当前 GPU 上的任务跑完后再部署，或者部署到其他有空闲 GPU 的服务器。

---
