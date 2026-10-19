# ops verify seed2 step output

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-seed2-step-output_20260516T033024_result.json`
- **Structured JSON:** [`e9dee65ef2490193ac8f.json`](../../sessions/e9/e9dee65ef2490193ac8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**seed2 (PID 750952) 已死，但 GPU 1 上有新 PID 754159 在跑（疑似 launcher 自动重启）**

### log tail（seed2.log，43 字节→实际持续写入）
```
Loading base model: lerobot/smolvla_libero
Loading  HuggingFaceTB/SmolVLM2-500M-Video-Instruct weights ...
Loading weights: 100%|██████████| 489/489 [00:01<00:00, 409.21it/s]
```
**未见 Step X/20000 行**。log 文件 11:34 刚被截断重写。

### GPU 占用
| GPU | PID | Mem |
|---|---|---|
| GPU 0 (b869d87a) | 675231 | 5910 MiB |
| GPU 0 | 682233 | 16214 MiB |
| **GPU 1 (5c8261d6)** | 733616 | 6601 MiB |
| **GPU 1** | **754159** | **16216 MiB** |

### 关键异常
1. **原 PID 750952 不存在**（/proc/750952 No such file）
2. **GPU 1 上 754159 是新进程**，与任务声称的 750952 不符
3. **`acib_v5_div_reg_seed2_recovered.log`** 含 wandb.init Traceback + Step 100/200 训练记录 + 末尾一段 shell 命令字符串泄漏，状态混乱
4. seed2.log 11:34 被截断 — 与 754159 启动时间一致（cmdline access time 11:32:29）

### 建议
按 C001 约束，不擅自 kill。但当前状态需要 director 决定：
- 是否 kill 754159（来源不明）
- 或让其完成模型加载后观察是否出 Step 行（再等 60-120s）

---
