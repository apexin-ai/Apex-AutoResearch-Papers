# exp_047_frozen_dt_emb_walker_s1 诊断报告

## 结论：训练已成功完成，监控误报

exp_047 **并未失败**。训练正常运行至 step 224000（超过目标 210000），所有数据完整。监控系统因缺少 sentinel 文件和 W&B 日志而将其标记为失败，属于 **false positive**。

## 证据

### 训练进度
- **服务器**: bjb1-40020（非 bjb1-45299）
- **metrics.jsonl**: 290 条记录，step 0 → 224000
- **Checkpoints**: 25k, 75k, 125k, 175k, 225k + latest.pt（每个 221MB）
- **最后 checkpoint 时间**: 2026-05-23 02:47
- **最后 metrics 时间**: 2026-05-23 02:45
- **进程状态**: 已自然退出（当前 GPU 上运行的是 exp_050/051）

### Eval Return 曲线
| Step | Eval Return |
|------|-------------|
| 5k   | 36.7        |
| 25k  | 158.4       |
| 65k  | 226.9       |
| 105k | 248.6       |
| 125k | **408.8** (peak) |
| 145k | 304.4       |
| 165k | 335.9       |
| 185k | 326.2       |
| 195k | 303.4       |
| 205k | 263.6       |
| 215k | 144.2       |

训练有正常学习信号，125k 达到峰值 408.8。后期（205k-215k）eval 下降可能是正常 variance 或 late-training instability。

### GPU 状态
- 服务器 bjb1-40020: 2× RTX 4090 (24GB)，正常工作
- 无异常 GPU 进程

## 失败误报原因

| 检查项 | exp_047 | exp_046 (对照) |
|--------|---------|----------------|
| sentinel 文件 | ❌ 无 | ❌ 也没有 |
| W&B 日志 | ❌ 未配置 | ❌ 也未配置 |
| train.log | ❌ 无（命令未重定向 stdout） | ✅ 有 |
| metrics.jsonl | ✅ 完整 (step 224k) | ✅ 完整 (step 224k) |
| checkpoints | ✅ 5个 + latest.pt | ✅ 5个 + latest.pt |

**核心原因**: 训练命令缺少 stdout 重定向（`> train.log 2>&1`），且 dreamer.py 本身不写 sentinel 文件。进程正常退出后，监控 5 次轮询均发现进程不存在，判定为 crashed。

## 是否需要重试

**不需要。** 训练数据完整，可直接使用：
- `checkpoint_225000.pt` / `latest.pt` 可用于评估
- `metrics.jsonl` 包含完整训练曲线（22 个 eval 点）

## 建议

1. **后续实验统一加 stdout 重定向**（已在 exp_050/051 中修正）：
   ```bash
   nohup bash -c '...' > logdir/exp_XXX/train.log 2>&1 &
   ```

2. **考虑在 dreamer.py 添加 completion sentinel**：训练结束后 `touch logdir/.../DONE`，方便监控区分正常退出 vs 崩溃。

3. **注意 eval 后期下降**：215k eval_return (144.2) 明显低于 125k-185k 区间（326-409），需对比其他 seed 确认是否系统性趋势。
