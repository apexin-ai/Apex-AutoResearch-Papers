# diagnose westd 34685 mvp occ failure

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-34685-mvp-occ-failure_20260521T045440_result.json`
- **Structured JSON:** [`f99755e3c3d93b456252.json`](../../sessions/f9/f99755e3c3d93b456252.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全貌清晰了。

## 诊断结果

### 三个实验全部死亡，GPU 全空闲

| 实验 | 状态 | 死因 | 最新 checkpoint |
|------|------|------|-----------------|
| **mvp_occ_s0** | 死亡 | `FileNotFoundError` (刚才 12:53 UTC 重启失败) | 42500 |
| **mvp_occ_s1** | 死亡 | SIGTERM (09:15 UTC 被外部杀死) | 17500 |
| **mvp_occ_s2** | 死亡 | `FileNotFoundError` (刚才 12:54 UTC 重启失败) | 42500 |

### 详细分析

**mvp_occ_s1** — 在 09:15 UTC 收到 SIGTERM (signal 15) 被外部杀死。从 17500 checkpoint resume 后只跑了 5894 步（到约 step 23394），没有生成新 checkpoint。这是第 4 次从 17500 重跑失败，**不是磁盘满**，是被某个进程/cron 发了 kill 信号。

**mvp_occ_s0 / s2** — `occ_s0_resume2.log` 和 `occ_s2_resume2.log` 显示它们刚在几分钟前（12:53/12:54 UTC）尝试重启，但**立即崩溃**：

```
FileNotFoundError: No such file or directory: '/root/autodl-tmp/models/openvla-7b/proprio_projector--42500_checkpoint.pt'
```

Resume 脚本的 `vla_path` 指向了基础模型目录 `/root/autodl-tmp/models/openvla-7b/`，但 42500 checkpoint 文件实际在：
- `/root/autodl-tmp/checkpoints/occ_s0/openvla-7b+...--42500_chkpt/`
- `/root/autodl-tmp/checkpoints/occ_s2/openvla-7b+...--42500_chkpt/`

### 服务器状态

| 资源 | 状态 |
|------|------|
| 磁盘(根) | 12G/30G (40%) — 正常 |
| 磁盘(数据) | 15G/879G (2%) — 充裕 |
| GPU | 4× RTX PRO 6000 96GB，全空闲 0MiB |
| 内存 | 21G/1TB — 正常 |

### 需要的操作

1. **s0/s2**: 修正 resume 命令的 `vla_path`，指向 checkpoint 目录而非基础模型目录，然后重新启动
2. **s1**: 需要从 17500 checkpoint 第 5 次 resume。但首先要搞清楚谁发的 SIGTERM——否则重跑还会被杀。可能是 cron 误杀或其他用户的操作

---
