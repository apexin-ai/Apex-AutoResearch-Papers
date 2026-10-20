# 诊断报告：plan019 三个实验状态 (2026-05-19 11:32)

## 总结

**三个实验都不是真正失败。** 监控系统误判，根因是缺少 sentinel 文件和 W&B 集成。

| 实验 | 监控状态 | 实际状态 | 根因 |
|------|---------|---------|------|
| plan019_1_7b_rsft_s43 | failed | **已完成** (567/567 steps) | 无 sentinel + 无 W&B |
| d112_rsft_s44_ced_score | failed | **仍在运行** (3500/24216) | 监控误判存活进程 |
| plan019_1_7b_rsft_s44 | running(miss 1/5) | **已完成** (567/567 steps) | 无 sentinel + 无 W&B |

---

## 实验 1: plan019_1_7b_rsft_s43

- **实际状态**: 训练正常完成，567/567 steps，3 full epochs
- **PID 601718**: 已退出（正常退出，非崩溃）
- **tmux session**: `plan019_1_7b_rsft_s43` 已不存在
- **输出目录**: `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43/`
  - `adapter_model.safetensors` (278MB) - 最终 adapter
  - `checkpoint-550/`, `checkpoint-567/` - 含 trainer_state.json, optimizer.pt 等
  - 无 `train.log`（stdout 输出到 tmux，session 销毁后丢失）
- **最终训练指标** (from trainer_state.json):
  - step 560: loss=0.5526, token_accuracy=0.8695
  - step 550: loss=0.5481, token_accuracy=0.8702
- **Checkpoint 有效**: 是，最终 adapter 已保存

### 为什么被标记 failed

1. **无 W&B**: `rsft_trainer.py` 检查 `if "WANDB_API_KEY" in os.environ`，服务器环境无此变量 → `report_to="none"`
2. **无 sentinel**: `rsft_trainer.py` 没有写 sentinel 文件的逻辑
3. **无 train.log**: 训练脚本未 redirect stdout
4. 进程正常退出后，监控检测到 "process dead + no sentinel + no W&B" → 误判为 failed

---

## 实验 2: d112_rsft_s44_ced_score

- **实际状态**: 仍在运行，正常推进
- **进程**: PID 604576 (python) 存活，GPU 0 占用 1492MiB
- **tmux session**: `d112_ced_score` 存在
- **进度**: 3500/24216 records scored (截至 11:30:36)
- **速率**: ~500 records / 1.5 min
- **预计完成**: ~12:33 (约 62 分钟后)
- **日志**: `/root/autodl-tmp/logs/d112_ced_score.log`

### 为什么被标记 failed

监控系统对 CED scoring 任务也用了同样的 "sentinel + W&B" 检测逻辑，但 scoring 是长时间运行的批处理任务，不产生 W&B run 也不写 sentinel。进程实际存活但监控未正确识别。

---

## 实验 3: plan019_1_7b_rsft_s44

- **实际状态**: 训练正常完成，567/567 steps，3 full epochs
- **PID 602749**: 已退出（正常退出）
- **tmux session**: `rsft_1_7b_s44` 已不存在
- **输出目录**: `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s44/`
  - `adapter_model.safetensors` (278MB) - 最终 adapter
  - `checkpoint-550/`, `checkpoint-567/`
  - 无 `train.log`
- **最终训练指标**:
  - step 560: loss=0.5539, token_accuracy=0.8707
  - step 550: loss=0.5638, token_accuracy=0.8664
- **Checkpoint 有效**: 是

### 根因同实验 1

---

## 共同根因分析

### 1. 缺少 WANDB_API_KEY

`rsft_trainer.py` 中的逻辑：
```python
if args.wandb_project and "WANDB_API_KEY" in os.environ:
    ...
    report_to="wandb" if "WANDB_API_KEY" in os.environ else "none",
```

服务器环境无 `WANDB_API_KEY`，所以所有训练 run 都 `report_to="none"`。

### 2. 无 sentinel 文件机制

`rsft_trainer.py` 中无任何写入 sentinel/done 标记的代码。`grep` 搜索 sentinel/DONE/completed 均无结果。

### 3. 训练脚本无日志重定向

`train_1_7b_s43.sh` 和 `train_1_7b_s44.sh` 直接 `python -m freige.training.rsft_trainer ...`，stdout 输出到 tmux pane。tmux session 关闭后日志丢失。

---

## GPU 当前状态

| GPU | 显存占用 | 进程 |
|-----|---------|------|
| 0 | 1501MiB/32607MiB | PID 604576 (d112 CED scoring) |
| 1 | 0MiB | 空闲 |
| 2 | 0MiB | 空闲 |
| 3 | 18891MiB/32607MiB | PID 598911 (其他任务) |

---

## 修复建议

1. **在训练脚本中设置 WANDB_API_KEY**（或在服务器 `.bashrc` 中全局设置）
2. **在 rsft_trainer.py 末尾添加 sentinel 写入**：训练完成后 `touch output_dir/DONE`
3. **训练脚本加日志重定向**：`python -m ... 2>&1 | tee $OUTPUT_DIR/train.log`
4. **s43 和 s44 无需重跑**：两个训练已正常完成，可直接用于下游 eval
5. **d112 CED scoring 无需干预**：正在正常运行，等待完成即可
