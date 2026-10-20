# diagnose cutoff 45k s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cutoff_45k_s1_20260524T213601_result.json`
- **Structured JSON:** [`a1c1e1e61a20c716d902.json`](../../sessions/a1/a1c1e1e61a20c716d902.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：cutoff_45k_s1

### 失败原因
**磁盘空间不足。** 在保存 step 30000 checkpoint 时，`safetensors` 序列化写入失败：
```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```
数据盘 `/root/autodl-tmp` 已 **100% 占满**（350G/350G，剩余 4KB）。

### 训练进度
- 日志最后记录的训练 step：**~30000**（在保存 30000 checkpoint 期间崩溃）
- 实际训练到 30000 步，但 checkpoint 写入时磁盘满了

### Checkpoint 状态
| Checkpoint | 状态 |
|---|---|
| 10000_chkpt | 存在（未验证完整性，但早于磁盘满） |
| 20000_chkpt | **完整** — 4/4 safetensor shards 齐全，约 14.4GB |
| 30000_chkpt | **不完整** — 仅写入 1/4 shard（915MB vs 应有的 ~14.4GB），需删除 |

### GPU 状态
- cuda:0（RTX PRO 6000 Blackwell 96GB）：空闲，进程已死。正常。
- cuda:1/2/3 被其他实验占用（99% utilization）

### 恢复方案
1. 删除损坏的 30000_chkpt（~1.2GB）释放少量空间
2. 但核心问题是 **350G 盘不够**——每个完整 checkpoint 约 14.4GB，3 个 checkpoint + 模型 + 数据已占满
3. 恢复训练前需要：
   - 删除不需要的旧 checkpoint（如 10000_chkpt）腾出空间
   - 或清理其他占用空间的文件
   - 预估还需保存 step 30000/40000/50000 三个 checkpoint ≈ 43GB，至少需要腾出这么多空间
4. 代码支持从 checkpoint 恢复的话，可从 **20000_chkpt** 继续训练

---
