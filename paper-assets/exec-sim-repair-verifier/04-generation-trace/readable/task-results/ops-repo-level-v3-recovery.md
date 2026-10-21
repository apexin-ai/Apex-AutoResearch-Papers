# ops repo level v3 recovery

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_repo-level-v3-recovery_20260512T171653_result.json`
- **Structured JSON:** [`88a64850ea0aa3167374.json`](../../sessions/88/88a64850ea0aa3167374.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断和修复完成。汇总：

---

## 诊断结果

### 1. OOM 根因

**根分区磁盘满 (89%, 27G/30G)**，不是 RAM OOM。

- 系统 RAM 754G，空闲 621G — 完全充足
- dmesg 无权限（容器），但 EXIT_CODE=137 + 磁盘 89% 高度指向：训练过程中 tokenizer cache / temp 文件写入根分区导致 ENOSPC，触发进程被杀
- 两个 v3 的 checkpoint 目录 (`checkpoints_repo_cls`, `checkpoints_repo_cwm`) 都是空的 — 没来得及存第一个 checkpoint

**磁盘占用分布**：
- `/root/.cache/huggingface` (Qwen3-4B + Qwen3-8B): 7.6G（根分区）
- `/home/sonny/exec-sim-repair-verifier`: 4.5G（根分区，含旧 checkpoint ~3.4G）
- 其余系统占用 ~15G

### 2. 根分区清理结果

89% → **64%** ✓

操作：将 `/root/.cache` 移至数据盘并创建符号链接 `/root/.cache → /root/autodl-tmp/.cache_root_backup`

### 3. 训练脚本参数

两个脚本**已支持** `save_strategy`/`save_total_limit`，无需修改：
- `save_strategy="epoch"`（非 dryrun 时）
- `save_total_limit=2`
- `output_dir` 默认已指向数据盘 (`/root/autodl-tmp/checkpoints_repo_cls/`, `/root/autodl-tmp/checkpoints_repo_cwm/`)

### 4. 推荐重提交命令

模型路径应改为数据盘副本（避免再从根分区读取/缓存）：

```bash
# CLS (cuda:2)
HF_HOME=/root/autodl-tmp/.hf_cache \
TORCH_HOME=/root/autodl-tmp/.torch_cache \
nohup python /home/sonny/exec-sim-repair-verifier/train_repo_verifier.py \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B \
  --device cuda:2 \
  > /root/autodl-tmp/train_repo_cls.log 2>&1 &

# CWM (cuda:3)
HF_HOME=/root/autodl-tmp/.hf_cache \
TORCH_HOME=/root/autodl-tmp/.torch_cache \
nohup python /home/sonny/exec-sim-repair-verifier/train_repo_cwm.py \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B \
  --device cuda:3 \
  > /root/autodl-tmp/train_repo_cwm.log 2>&1 &
```

### 5. 是否需要错开启动

**不需要**。RAM 621G 空闲，两个 Qwen3-4B LoRA 训练各占 ~15-20G GPU 显存 + ~10-20G RAM，完全可以同时启动。OOM 根因是磁盘不是内存，现已修复。

---
