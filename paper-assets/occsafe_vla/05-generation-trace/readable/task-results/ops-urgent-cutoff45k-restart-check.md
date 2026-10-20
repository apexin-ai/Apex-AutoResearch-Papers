# ops urgent cutoff45k restart check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_cutoff45k_restart_check_20260524T041840_result.json`
- **Structured JSON:** [`de6355bc7c8f2f5b5593.json`](../../sessions/de/de6355bc7c8f2f5b5593.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论

### cutoff_45k_s0 **未被重启**，一切正常

**关键证据：**

1. **原始 PID 456023 仍在运行**，启动时间 02:34:10，从未中断
2. **子进程 PID 456097** 在 GPU 0 上活跃，占用 63004 MiB
3. **训练进度连续**：step 0 (line 78) → 当前 ~31000+，无间断
4. **"Loading checkpoint shards" 全部是正常行为**：
   - **Line 30**：启动时加载基础模型（openvla-7b 的 3 个 shard）
   - **Lines 193, 311, 429**：分别对应 **step 10000/20000/30000 的 checkpoint 保存**。每次前面都有 PEFT 的 `save_embedding_layers` 警告——这是 LoRA checkpoint save 时 PEFT 库重新加载 base model shards 的标准行为，不是重启
   - 总计 13 行匹配 = 4 个事件 × 每事件 3-4 行进度条，完全吻合
5. 日志中无任何 "Resuming"/"restart"/"recovering" 关键词

**Checkpoints 状态：**
- 20000_chkpt (May 24 08:58)
- 30000_chkpt (May 24 12:16)
- 10000_chkpt 已被 checkpoint_rotation.sh 清理

### 其余 3 个实验状态

| 实验 | 当前 step | 进度 | 速度 | 状态 |
|------|-----------|------|------|------|
| cutoff_15k_s0 | ~31007/50005 | 62% | ~1.07 it/s | 正常 |
| cutoff_25k_s1 | ~17187/50005 | 34% | ~1.08 it/s | 正常 |
| reverse_cutoff_s1 | ~17217/50005 | 34% | ~1.06 it/s | 正常 |

**结论：4 个实验全部正常运行，无重启，无异常。** Reviewer 看到的 "Loading checkpoint shards" 是 checkpoint 保存时的正常日志，非重启信号。

---
