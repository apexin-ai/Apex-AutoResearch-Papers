# urgent westd41074 gpu03 deploy long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_westd41074_gpu03_deploy_long_20260526T013854_result.json`
- **Structured JSON:** [`eaf24f5d43f193edf2a2.json`](../../sessions/ea/eaf24f5d43f193edf2a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署成功。汇总结果：

---

### 1. Kill 259256
**已成功 force kill**

### 2. 两个实验部署结果

| 实验 | GPU | Bash PID | Python PID | 显存 | 状态 |
|------|-----|----------|------------|------|------|
| Random k=0.85 | GPU0 | 303188 | 303189 | 16169 MiB | 运行中，Task 1/10 |
| Attn k=0.85 | GPU3 | 303981 | 303982 | 16169 MiB | 运行中，Task 1/10 |

### 3. nvidia-smi 输出

```
GPU 0: 32372 / 97887 MiB  (PID 300693: 16169 MiB + PID 303189: 16169 MiB)
GPU 1: 15980 / 97887 MiB  (PID 76492: 15961 MiB)
GPU 2: 15980 / 97887 MiB  (PID 259181: 15961 MiB)
GPU 3: 16188 / 97887 MiB  (PID 303982: 16169 MiB)
```

### 4. 日志确认

**GPU0 Random**:
```
[Pruning] 256 -> 217 vision tokens (k=0.85)
```

**GPU3 Attn**:
```
[Attn Pruning] 256 -> 217 vision tokens (k=0.85), importance range=[0.7189, 1.6595]
```

### 5. 注意事项
- GPU0 上有一个旧进程 PID 300693（16169 MiB），是之前 attn k=0.85 v3 实验残留。A100 98GB 空间充足，不影响新实验。
- 两个实验注册已完成（PREPARING 状态）。

---
