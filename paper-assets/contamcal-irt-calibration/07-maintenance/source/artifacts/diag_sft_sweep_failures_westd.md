# 诊断报告：westd-29999 SFT Sweep 失败

**日期**: 2026-05-20  
**服务器**: westd-29999  
**根因**: 根分区磁盘满 (`overlay 30G → 100% used`)

---

## 根因分析

`/root/.cache/huggingface` 占用 20GB（主要是 datasets cache），根分区 30GB 全满。两个 sweep 各自完成了 4 个 dosage（d000/d005/d025/d050）后，累积的 HF datasets cache 填满了根分区，导致第 5 个 dosage（d100）均失败。

**修复**：将 HF cache 迁移到数据盘（`HF_HOME=/root/autodl-tmp/.hf_cache`），然后清理 `/root/.cache/huggingface`。

---

## 实验 1: sft_qwen14b_s123_sweep (Qwen2.5-14B, cuda:1)

**失败原因**: `OSError: [Errno 28] No space left on device`  
**失败阶段**: d100 数据集预处理（`datasets.map()` → pyarrow writer 写入时磁盘满）  
**训练未开始**: d100 目录为空，无任何 checkpoint

### Checkpoint 状态

| Dosage | 状态 | train_config.json | .done | lora_adapter |
|--------|------|-------------------|-------|--------------|
| d000 | ✅ 完成 | ✅ | ✅ | ✅ |
| d005 | ✅ 完成 | ✅ | ✅ | ✅ |
| d025 | ✅ 完成 | ✅ | ✅ | ✅ |
| d050 | ✅ 完成 | ✅ | ✅ | ✅ |
| d100 | ❌ 失败 | ❌ | ❌ | ❌（目录空） |

**恢复**: 清磁盘后直接重跑 `run_qwen14b_s123.sh`（脚本有 skip 逻辑，会跳过已完成的 d000-d050，只跑 d100）。需先删除空的 `Qwen2.5-14B_d100_s123/` 目录。

---

## 实验 2: sft_gemma2_s123_sweep (gemma-2-9b, cuda:3)

**失败原因**: Traceback（详细错误被日志截断，根因同为磁盘满）  
**失败阶段**: d100 训练中途（step 888/4159, 21%, ~41 分钟）  
**部分产出**: `lora_adapter/` 目录存在但为空，无 checkpoint 保存

### Checkpoint 状态

| Dosage | 状态 | train_config.json | .done | lora_adapter |
|--------|------|-------------------|-------|--------------|
| d000 | ✅ 完成 | ✅ | ✅ | ✅ |
| d005 | ✅ 完成 | ✅ | ✅ | ✅ |
| d025 | ✅ 完成 | ✅ | ✅ | ✅ |
| d050 | ✅ 完成 | ✅ | ✅ | ✅ |
| d100 | ❌ 失败 | ❌ | ❌ | ❌（目录空） |

**恢复**: 同上，清磁盘 + 删除空的 `gemma-2-9b_d100_s123/` 目录 + 重跑脚本。

---

## 当前服务器状态

### 磁盘

| 分区 | 大小 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| overlay (根) | 30G | 30G | 0 | **100%** |
| /dev/sda2 (数据盘) | 879G | 407G | 427G | 49% |

**根分区空间占用**: `/root/.cache/huggingface` = 20GB（datasets cache）

### GPU

| GPU | 型号 | 显存占用 | 状态 |
|-----|------|----------|------|
| 0 | RTX PRO 6000 (96GB) | 0 MiB | 空闲 |
| 1 | RTX PRO 6000 (96GB) | 0 MiB | 空闲 |
| 2 | RTX PRO 6000 (96GB) | 67209 MiB | **占用** (PID 238804) |
| 3 | RTX PRO 6000 (96GB) | 0 MiB | 空闲 |

---

## 重试步骤

1. 清理根分区：
   ```bash
   rm -rf /root/.cache/huggingface/datasets
   # 或整个 cache: rm -rf /root/.cache/huggingface
   ```
2. 设置 HF cache 到数据盘（加到两个 run script 里）：
   ```bash
   export HF_HOME=/root/autodl-tmp/.hf_cache
   ```
3. 删除失败的空目录：
   ```bash
   rm -rf /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s123
   rm -rf /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d100_s123
   ```
4. 重跑两个脚本（分别在 cuda:1 和 cuda:3 上），只会训练 d100
5. 预计耗时：Qwen14B ~3h, gemma-2-9b ~3h（基于 d050 的训练时长估算）

---

## 脚本问题备注

两个 shell 脚本有 `set -x` 但没有 `set -e`，Python 进程崩溃后 `$?` 被后续 `echo` 命令覆盖为 0，导致脚本报告 `exit code=0` 和 `ALL_DONE`（假成功）。建议修复为 `set -ex` 或在 Python 调用后检查退出码。
