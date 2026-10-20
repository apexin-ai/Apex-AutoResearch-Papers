# diagnose failed 10894 v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_failed_10894_v2_20260526T180252_result.json`
- **Structured JSON:** [`d013ff84b35dd3903c16.json`](../../sessions/d0/d013ff84b35dd3903c16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 共同根因：数据盘 `/root/autodl-tmp` 100% 满

```
Filesystem   Size  Used  Avail  Use%
/dev/md0     250G  250G    40K  100%
```

**checkpoints 目录占 229G / 250G**，是主要元凶。

---

### 实验 1: full_occ_ln_v2_s0 (cuda:1)

- **失败位置**: step 20000 checkpoint 保存，`merged_vla.save_pretrained()` 写 safetensors 时
- **错误**: `safetensors_rust.SafetensorError: I/O error: No space left on device (os error 28)`
- **时间**: 2026-05-27 02:00:57
- **部分写入**: 20G 已占用（完整 checkpoint ~15G，多出来的是不完整的写入）

### 实验 2: detach_ln_v2_s0 (cuda:3)

- **失败位置**: step 20000 checkpoint 保存，`processor.save_pretrained()` → tokenizer save 时
- **错误**: `Exception: No space left on device (os error 28)`
- **时间**: 2026-05-27 02:01:07
- **部分写入**: 15G 已占用

### 对照: full_occ_ln_v2_s1 (cuda:2)

- 当前在 step ~20001，**正在保存 step 20000 checkpoint**
- **极大概率也会失败**——磁盘仅剩 40K
- GPU 2 仍有进程（62GB VRAM），暂未崩溃

### GPU 状态

| GPU | VRAM | Util | 状态 |
|-----|------|------|------|
| 0 | 62194MiB | 92% | 有进程运行（非本次三个实验） |
| 1 | 0MiB | 0% | 空闲（full_occ_ln_v2_s0 已崩） |
| 2 | 62194MiB | 0% | full_occ_ln_v2_s1 正在存盘 |
| 3 | 0MiB | 0% | 空闲（detach_ln_v2_s0 已崩） |

### 空间明细 `/root/autodl-tmp/checkpoints/`

| 目录 | 大小 | 备注 |
|------|------|------|
| reverse_cutoff_s2_v2 | 45G | 历史 |
| ablation_occ_detach_s3_v2 | 30G | 历史 |
| cutoff_45k_s2_v2 | 30G | 历史 |
| full_occ_ln_s3_v2 | 30G | 历史 |
| mvp_occ_s3_v2 | 30G | 历史 |
| full_occ_ln_v2_s0 | 20G | 本次失败（含不完整写入） |
| full_occ_ln_s0 | 15G | 历史 |
| full_occ_ln_v2_s1 | 15G | 本次正在运行 |
| detach_ln_v2_s0 | 15G | 本次失败（含不完整写入） |
| **合计** | **~229G** | |

---

### 建议修复方案

1. **紧急**：清理历史 checkpoint 释放空间。如果以下实验已完成评估，可删除：
   - `reverse_cutoff_s2_v2` (45G)、`ablation_occ_detach_s3_v2` (30G)、`cutoff_45k_s2_v2` (30G)、`full_occ_ln_s3_v2` (30G)、`mvp_occ_s3_v2` (30G)、`full_occ_ln_s0` (15G)
   - 总计可释放 **~180G**

2. **清理失败实验的不完整 checkpoint**：`full_occ_ln_v2_s0` 和 `detach_ln_v2_s0` 的 20000 step checkpoint 目录是不完整的，需删除后重新保存

3. **重启两个失败实验**：清理空间后用 `--resume` 从最近完整 checkpoint 继续（需确认 resume 逻辑是否适用于这两个实验——注意 C002 约束只禁止 cutoff/reverse_cutoff 实验用 resume，这两个不受限）

4. **监控 full_occ_ln_v2_s1**：它大概率也会因磁盘满而失败，需尽快清理空间

---
