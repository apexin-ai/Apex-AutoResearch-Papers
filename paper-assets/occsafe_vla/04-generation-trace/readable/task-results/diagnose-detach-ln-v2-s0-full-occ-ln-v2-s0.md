# diagnose detach ln v2 s0 full occ ln v2 s0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_detach_ln_v2_s0_full_occ_ln_v2_s0_20260526T180318_result.json`
- **Structured JSON:** [`dfb15d2052dc16956e39.json`](../../sessions/df/dfb15d2052dc16956e39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 诊断报告

### 失败根因

**两个实验失败原因相同：`/root/autodl-tmp` 磁盘 100% 满（250G/250G，仅剩 40K）。**

都在 **step 20000 保存 checkpoint 时** 触发 `No space left on device (os error 28)`：

| 实验 | 具体崩溃位置 |
|------|-------------|
| detach_ln_v2_s0 | `processor.save_pretrained()` → `tokenizer.save()` 写 tokenizer.json 失败 |
| full_occ_ln_v2_s0 | `merged_vla.save_pretrained()` → `safe_save_file()` 写 model shard 2/4 时失败 |

### 训练进度

| 实验 | 到达步数 | 总步数 | 进度 |
|------|---------|--------|------|
| detach_ln_v2_s0 | 20000 | 50005 | 40% |
| full_occ_ln_v2_s0 | 20000 | 50005 | 40% |

### Checkpoint 情况

| 实验 | 10000_chkpt | 20000_chkpt |
|------|-------------|-------------|
| detach_ln_v2_s0 | 15G, **完好可用** | 532K, **损坏**（tokenizer.json=0字节，无模型权重） |
| full_occ_ln_v2_s0 | 15G, **完好可用** | 5G, **不完整**（仅 1/4 safetensors shard，缺 3 个） |

### 磁盘占用分析

`/root/autodl-tmp` 250G 总容量分布：

| 目录 | 大小 | 说明 |
|------|------|------|
| checkpoints/ | **229G** | 所有实验 checkpoint |
| models/ | 15G | 预训练模型 |
| libero_datasets/ | 5.9G | 数据集 |
| data/ | 2G | 数据 |

Checkpoint 明细（229G）：

| 实验 | 大小 | 备注 |
|------|------|------|
| reverse_cutoff_s2_v2 | 45G | 旧实验 |
| ablation_occ_detach_s3_v2 | 30G | 旧实验 |
| cutoff_45k_s2_v2 | 30G | 旧实验 |
| full_occ_ln_s3_v2 | 30G | 旧实验 |
| mvp_occ_s3_v2 | 30G | 旧实验 |
| full_occ_ln_v2_s0 | 20G | 当前（含损坏的 20k ckpt） |
| detach_ln_v2_s0 | 15G | 当前（含损坏的 20k ckpt） |
| full_occ_ln_v2_s1 | 15G | |
| full_occ_ln_s0 | 15G | 旧实验 |
| cutoff_15k_s1 | 463M | |
| 其他空目录 | ~0 | |

### GPU 状态

- GPU 0: 被另一个进程占用 (PID 170698, 62GB/98GB)
- **GPU 1, 2, 3: 空闲可用**

### 重启条件

1. **必须先清磁盘**。每个实验后续还需保存 3 个 checkpoint（30k, 40k, 50k），每个约 15G，两个实验共需 ~90G 空间
2. **删除损坏的 20000_chkpt**：立即释放 ~5.5G
3. **删除旧实验 checkpoint**：以下旧实验如果不再需要，删除后可释放 ~180G
   - `reverse_cutoff_s2_v2` (45G)
   - `ablation_occ_detach_s3_v2` (30G)
   - `cutoff_45k_s2_v2` (30G)
   - `full_occ_ln_s3_v2` (30G)
   - `mvp_occ_s3_v2` (30G)
   - `full_occ_ln_s0` (15G)
4. **从 10000_chkpt resume**（这两个不是 cutoff 实验，不受 C002 约束），剩余 40005 步，约 11 小时/实验
5. 时间预算：现在到 DDL 还有 ~34 小时，两个实验并行跑 ~11 小时，**时间充足**

请确认哪些旧 checkpoint 可以删除，我来执行清理和重启。

---
