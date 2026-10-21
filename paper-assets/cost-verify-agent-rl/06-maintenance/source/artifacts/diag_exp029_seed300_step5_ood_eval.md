# Diagnosis: exp029_seed300_step5_ood_eval

## 错误信息

```
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpjqaf9lrywandb-media/1rrzyo8l.table.json'
```

完整调用链：
```
train.py:326                  → trainer.fit()
agent_trainer.py:1156         → val_metrics = self._validate()
agent_trainer.py:730          → self._maybe_log_generations(...)
agent_trainer.py:572          → self.generations_logger.log(...)
ragen/utils.py:63             → wandb.log({f"{_type}/generations": new_table}, step=step)
wandb/.../table.py:607        → codecs.open(tmp_path, "w", encoding="utf-8")
→ FileNotFoundError: /tmp/tmpjqaf9lrywandb-media/1rrzyo8l.table.json
```

## 根因分析

**直接原因**：wandb 在序列化 `wandb.Table` 时需要将数据写入临时目录 `/tmp/tmpjqaf9lrywandb-media/`，该目录已不存在。

**底层原因**：`wandb-core` 后台进程已变为僵尸进程（PID 433602, `<defunct>`）。这可能导致其管理的 `/tmp` 临时目录被清理（AutoDL 或 systemd-tmpfiles 的 `/tmp` 定期清理机制）。wandb-core 死后，SDK 尝试写入已清理的 temp dir 时触发 FileNotFoundError。

**关键点**：OOD 评估本身已成功完成（134 个 AlfworldSG_OOD 任务的 reward 已计算完毕，日志中可见大量 `Skipping non-numeric metric 'anchor_obs'` 警告），但崩溃发生在 `_validate()` 返回 metrics 之前——具体在 `_maybe_log_generations`（行 730），即 wandb Table 日志记录步骤。这导致：

1. eval 指标**未返回**给调用方（`fit()` 中的 `val_metrics` 未赋值）
2. generations **未 dump 到本地文件**（`_dump_generations` 在行 733+ 之后，未执行到）
3. W&B 上无指标 → CRON 报 "no valid W&B metrics"

**不是 OOM、checkpoint 缺失、或代码逻辑 bug。**

## 环境状态

| 项目 | 状态 |
|------|------|
| Checkpoint | ✅ 存在 `/root/autodl-tmp/checkpoints/exp029_seed300_step5_hf/`（3.8GB model.safetensors） |
| 磁盘 | ✅ root 22G 可用，数据盘 33G 可用（87%） |
| GPU | ✅ 2× RTX PRO 6000 96GB，空闲，0MiB 占用 |
| 残留进程 | ⚠️ `ray::TaskRunner` PID 433097 仍在运行（60% CPU, 6.4GB RAM），`wandb-core` PID 433602 僵尸 |

## 修复建议

### 1. 清理残留进程（立即）
```bash
kill -9 433097 433602
```

### 2. 代码修复：让 wandb Table 日志失败不阻塞 eval（推荐）

在 `ragen/utils.py` 的 `log_generations_to_wandb` 中加 try-except：

```python
def log_generations_to_wandb(self, samples, step, _type='val'):
    import wandb
    try:
        # ... existing code ...
        wandb.log({f"{_type}/generations": new_table}, step=step)
        self.table = new_table
    except Exception as e:
        logging.warning(f"Failed to log generations table to wandb: {e}")
```

### 3. 环境修复：防止 /tmp 清理影响 wandb（可选）

启动脚本中设置 `WANDB_DATA_DIR`：
```bash
export WANDB_DATA_DIR=/root/autodl-tmp/wandb_tmp
mkdir -p /root/autodl-tmp/wandb_tmp
```

### 4. 重跑实验
先执行修复 1+2，然后重跑。Checkpoint 完好，可直接重启。
