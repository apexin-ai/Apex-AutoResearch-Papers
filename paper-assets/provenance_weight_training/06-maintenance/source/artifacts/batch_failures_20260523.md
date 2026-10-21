# 批量实验失败诊断 — 2026-05-23

## 根因

**同一个根因：3个实验均指定 `--resume_from_checkpoint checkpoint-1000`，但 checkpoint-1000 在所有 output_dir 中都不存在。**

前次运行的 step_metrics 显示训练推进到 step ~999-1000，但 checkpoint-1000 从未成功保存（进程在保存期间被中断或崩溃）。

## 各实验具体错误

### 1. bs8_nmin4_adaptive_seed123
- **错误**: `safetensors_rust.SafetensorError: Error while deserializing header: incomplete metadata, file not fully covered`
- **含义**: checkpoint-1000 的 model.safetensors 文件存在但不完整（写入被中断）
- **现存 checkpoint**: checkpoint-500（完好，model.safetensors ~1.1GB）
- **step_metrics**: 2000 行，最后记录到 step 999

### 2. bs8_nmin4_uniform_seed123
- **错误**: 同上 — `SafetensorError: incomplete metadata, file not fully covered`
- **现存 checkpoint**: checkpoint-500（完好）
- **step_metrics**: 2000 行，最后记录到 step ~999

### 3. rho03_adaptive_seed456
- **错误**: `FileNotFoundError: .../checkpoint-1000/trainer_state.json`
- **含义**: checkpoint-1000 目录完全不存在（可能 save_total_limit=1 在尝试保存 checkpoint-1000 前删除了 checkpoint-500，而 checkpoint-1000 保存失败，导致零 checkpoint）
- **现存 checkpoint**: 无
- **step_metrics**: 4000 行，最后记录到 step 999

## 环境状态（无异常）

| 项目 | 状态 |
|------|------|
| 磁盘 /root/autodl-tmp | 250G 已用 152G，剩余 99G (61%) — 正常 |
| GPU | 4× RTX PRO 6000 (98GB)，GPU 0/2 在跑其他任务 (98-99% util)，GPU 1/3 空闲 |

## 修复方案

| 实验 | 方案 |
|------|------|
| bs8_nmin4_adaptive_seed123 | `--resume_from_checkpoint checkpoint-500`（从 step 500 恢复，损失 ~500 步） |
| bs8_nmin4_uniform_seed123 | `--resume_from_checkpoint checkpoint-500`（同上） |
| rho03_adaptive_seed456 | **移除 `--resume_from_checkpoint`**，从头开始（无可用 checkpoint） |

如果不想区分处理，最简单的方案：**3个实验全部移除 `--resume_from_checkpoint` 从头跑**，max_steps=6103 对 Qwen3-0.6B 训练时间可控。

### 防止复发
检查启动脚本中 `--resume_from_checkpoint` 的值是否硬编码为 `checkpoint-1000`。建议改为 `--resume_from_checkpoint True`（让 Trainer 自动找最新的有效 checkpoint）或在脚本中加存在性检查。
