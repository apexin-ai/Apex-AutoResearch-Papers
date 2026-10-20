# 实验失败诊断报告

**日期**: 2026-05-16
**服务器**: westd-47453

## 根因：根分区磁盘满（30G/30G, 0 bytes free）

```
Filesystem      Size  Used Avail Use%
overlay          30G   30G     0 100%  ← 根分区（已满）
/dev/md0        250G  194G   57G  78%  ← 数据盘 autodl-tmp
```

### 根分区空间占用

| 目录 | 大小 | 说明 |
|------|------|------|
| /root/miniconda3 | 12G | conda 环境 |
| /root/provenance_weight_training/data | 11G | 训练数据 |
| /root/provenance_weight_training/models | 8.8G | 基础模型 Qwen3-0.6B |
| /root/provenance_weight_training/wandb | 71M | offline wandb 日志 |
| /root/runs | 354M | 训练日志 |
| **合计** | **~32.2G** | **超出 30G 限制** |

`output/models/` 已正确 symlink 到 autodl-tmp（171G checkpoints 在数据盘上），不是问题。

---

## 各实验错误摘要

### 1. threshold_q03_seed42（主要目标）
- **停止位置**: 38% (3198/8477 steps, epoch ~0.38)
- **日志末尾**: 进度条正常输出，无 Traceback / Error / "No space left"
- **死亡方式**: 进程被静默杀死（无法写入错误信息到已满的磁盘）
- **GPU**: cuda:3（当前已空闲，0 MiB）
- **脚本**: `--weighting_method uniform --data_path scored_data_filtered_q03.jsonl`

### 2. random_reweight_seed42
- **停止位置**: 72% (6092/8477 steps, epoch ~0.72)
- **日志末尾**: 进度条正常输出，无 Traceback
- **死亡方式**: EXIT_CODE=1，同样无错误日志输出
- **GPU**: cuda:2（当前已空闲）
- **差异**: 未启用 `--use_wandb`，使用 `--weighting_method random`

### 3. threshold_q07_seed42
- **停止位置**: 37% (2235/6103 steps, epoch ~0.19, 训练 4h19m)
- **日志末尾**: 大量 per-batch weighting metrics 输出（`weighting/b`, `alpha_eff`, `ess` 等），无 Traceback
- **死亡方式**: 进程静默终止
- **GPU**: 当前已空闲
- **差异**: 数据集 `scored_data_filtered_q07.jsonl`，total steps 6103（非 8477，因为过滤后数据量不同）

---

## 共性问题

三个实验 **完全相同的失败模式**：
1. 进度条正常推进 → 突然中断
2. 无 Traceback、无 Error、无 "No space left on device"
3. 日志无法记录错误（因为日志文件本身也写不进去）

这是典型的 **磁盘满导致的静默进程死亡**。当根分区剩余 0 bytes 时：
- checkpoint save 失败 → 进程 crash
- 甚至 Python 的异常处理也无法将 traceback 写入 stderr/log
- 进程被内核终止（SIGKILL），无任何善后输出

---

## 当前风险

**rho02_uniform_seed42 正在 GPU 1 上运行**（PID 316988, 75007 MiB），同样面临磁盘满风险。下次触发 checkpoint save 时可能也会死掉。

---

## 修复建议

### 立即操作（紧急）

1. **迁移 data/ 和 models/ 到 autodl-tmp**：
```bash
# 迁移训练数据（释放 11G）
mv /root/provenance_weight_training/data /root/autodl-tmp/provenance_weight_training/data
ln -s /root/autodl-tmp/provenance_weight_training/data /root/provenance_weight_training/data

# 迁移基础模型（释放 8.8G）
mv /root/provenance_weight_training/models /root/autodl-tmp/provenance_weight_training/models
ln -s /root/autodl-tmp/provenance_weight_training/models /root/provenance_weight_training/models
```
这将释放 ~19.8G 空间，根分区使用率降至 ~40%。

2. **迁移 wandb/ 到 autodl-tmp**：
```bash
mv /root/provenance_weight_training/wandb /root/autodl-tmp/provenance_weight_training/wandb
ln -s /root/autodl-tmp/provenance_weight_training/wandb /root/provenance_weight_training/wandb
```

### 迁移后

3. **重跑三个失败实验**（迁移完成、确认磁盘空间后）

4. **清理旧 checkpoints**（autodl-tmp 上 171G 模型，按需保留）：
   - 已完成评估的旧实验只保留 best checkpoint
   - save_total_limit=3 只限制单个实验的 checkpoint 数量，但历史实验累积仍很大

### 长期预防

5. **所有大文件统一放 autodl-tmp**：data、models、wandb、logs 全部 symlink
6. **脚本中增加磁盘空间预检查**：训练开始前检查根分区剩余空间 > 5G
