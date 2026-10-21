# 训练状态快照 — 2026-05-23

## 实验状态总览

| 实验 | PID | GPU | 状态 | 当前 Step | 进度 | train_loss | 预计剩余 |
|------|-----|-----|------|-----------|------|------------|----------|
| rho03_adaptive_seed456 | 832974 | cuda:0 | ❌ 崩溃 | — | — | — | — |
| rho03_uniform_seed456 | 833051 | cuda:2 | ✅ 运行中 | 1080/6103 | 18% | 10.06 | ~3h 23min |
| bs8_nmin4_adaptive_seed123 | 833474 | cuda:1 | ❌ 崩溃 | — | — | — | — |
| bs8_nmin4_uniform_seed123 | 833558 | cuda:3 | ❌ 崩溃 | — | — | — | — |

## 存活实验详情

### rho03_uniform_seed456 ✅
- **进程运行时间**: ~3 分钟（刚从 checkpoint-1000 恢复）
- **当前 step**: 1080 / 6103 (18%)
- **训练速度**: ~2.42 s/step
- **最新 train_loss**: 10.06（step 1080）
- **loss 趋势**: 9.58 → 9.84 → 10.25 → 10.33 → 10.59 → 9.62 → 10.21 → 10.06（波动中，尚未稳定下降）
- **learning_rate**: 4.333e-05（线性衰减中）
- **预计完成时间**: ~3h 23min 后

## 崩溃实验详情

### rho03_adaptive_seed456 ❌
- **错误**: `FileNotFoundError: '.../checkpoint-1000/trainer_state.json'`
- **原因**: checkpoint-1000 目录缺少 trainer_state.json
- **修复**: 检查 checkpoint 完整性或从其他 checkpoint 恢复

### bs8_nmin4_adaptive_seed123 ❌
- **错误**: `SafetensorError: incomplete metadata, file not fully covered`
- **原因**: checkpoint-1000 的 safetensors 权重文件损坏（不完整）
- **修复**: 重新保存 checkpoint 或从更早的 checkpoint 恢复

### bs8_nmin4_uniform_seed123 ❌
- **错误**: 同上 — safetensors 文件损坏
- **修复**: 同上

## GPU 使用率

| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| GPU 0 | 0% | 0 MiB | 97887 MiB |
| GPU 1 | 0% | 0 MiB | 97887 MiB |
| GPU 2 | 98% | 26227 MiB | 97887 MiB |
| GPU 3 | 0% | 0 MiB | 97887 MiB |

## 磁盘使用率

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根分区) | 30G | 9.7G | 21G | 33% |
| /root/autodl-tmp | 250G | 153G | 98G | 62% |

## 总结

- **4 个实验中仅 1 个存活**（rho03_uniform_seed456），预计 ~3.5 小时后完成
- **3 个实验启动即崩溃**，均因 checkpoint-1000 文件损坏/不完整
- GPU 0/1/3 完全空闲，可修复 checkpoint 后重启崩溃的实验
