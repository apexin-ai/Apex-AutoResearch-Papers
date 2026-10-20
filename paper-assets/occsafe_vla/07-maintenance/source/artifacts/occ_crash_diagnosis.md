# OCC 训练实验诊断报告

**日期**: 2026-05-20  
**服务器**: westd-34685 (AutoDL, 4x NVIDIA RTX PRO 6000 Blackwell 96GB)  
**实验**: mvp_occ_s0 / s1 / s2

## 结论：进程未崩溃，cron 误报

**三个训练进程均正常运行中。** cron 报告 "process dead" 是误报。

## 证据

### 1. GPU 状态 (nvidia-smi)

| GPU | PID | 显存占用 | GPU 利用率 |
|-----|-----|---------|-----------|
| 0 (s0) | 27740 | 62194 MiB / 97887 MiB | 99% |
| 1 (s1) | 28900 | 62194 MiB / 97887 MiB | 99% |
| 2 (s2) | 30044 | 62200 MiB / 97887 MiB | 99% |

GPU 3 空闲。

### 2. 训练进度

| 实验 | 最后可见 step | step 600 occ_loss | step 600 action_loss | 速度 |
|------|-------------|-------------------|---------------------|------|
| s0 | 656+ | 0.0192 | 0.2695 | ~1.09 it/s |
| s1 | 620+ | 0.0235 | 0.2676 | ~1.08 it/s |
| s2 | 660+ | 0.0268 | 0.2344 | ~1.08 it/s |

训练开始于 2026-05-21 00:36，正常推进中。总步数 50005，预计 ~12.7 小时完成。

### 3. 日志无错误

三个日志文件 (`occ_s{0,1,2}_train.log`) 中 grep traceback/RuntimeError/killed/OOM/segfault/fatal 全部返回空。仅有 TensorFlow GPU 注册警告和 TF-TRT 警告（无害）。

### 4. cron 误报原因

- `WANDB_MODE=disabled` → 无 W&B run 可检测
- 无 sentinel 文件写入（训练脚本未实现 sentinel 机制）
- cron 5 次检查均未发现生命信号 → 自动判定为 failed

## occ_index.json 格式

格式 **正确**，与 datasets.py 期望一致。M009 bug **不适用**。

```json
{
  "task_name": {
    "file": "occ_task_name_demo.hdf5",
    "demos": {
      "demo_0": 98,
      "demo_1": 84,
      ...
    }
  }
}
```

- 9 个 task，450 个 demo 条目
- datasets.py `_load_occ_label()` 调用 `demos.items()` 遍历 dict → 格式匹配
- 预加载成功: "Occ preload done: 9 files, 55370 samples"

## occ_loss 分析

step 600 时 occ_loss 在 0.019-0.027 范围，较低。两种可能：
1. **正常**: BEV 占用网格大部分为空（0），模型已学会预测空区域
2. **异常**: 样本匹配逻辑失败导致全部 fallback 到全零 label，模型学会输出全零

需后续通过 `_traj_len` 字段是否正确传递来验证 demo matching 是否生效。建议在训练代码中添加 fallback 计数 metric。

## 修复建议

1. **cron 监控**: 训练脚本需要写入 sentinel 文件（或 heartbeat），否则 WANDB_MODE=disabled 时 cron 无法检测进程存活
2. **occ 数据验证**: 添加 fallback rate metric，统计每 N 步中多少样本返回了全零 fallback
3. **当前操作**: 无需干预，等待训练自然完成（约 12 小时后）
