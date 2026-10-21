# 磁盘清理与 Ray 重定向报告

**服务器**: bjb1-17606  
**时间**: 2026-05-14 ~09:00 UTC  

## 1. 根分区使用情况

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 8.5G (29%) | 9.8G (33%) |
| 可用 | 22G | 21G |

> **注意**: 实际磁盘状态与任务描述（3.2G / 90%）不符，根分区有 21G+ 可用，并非紧急状态。清理后可用空间略降是因为训练进程持续写入。

## 2. 清理内容

| 清理项 | 释放空间 |
|--------|---------|
| 旧 Ray sessions（28 个历史 session） | ~105M |
| /tmp 日志文件（exp 日志、download 日志等） | ~1.5M |
| Hydra 历史 outputs（29 个旧目录） | ~1.4M |
| pip cache | 已清理 |
| conda cache | 已清理 |
| apt cache | 已清理 |
| Python __pycache__ | 已清理 |

总释放约 108M。根分区大部分空间被 miniconda3（12G）占用，其余都很小。

## 3. Ray 临时文件重定向

- 当前活跃 session: `/tmp/ray/session_2026-05-14_08-50-39_244352_178842`（2.5M，保留不动）
- 已创建数据盘目录: `/root/autodl-tmp/ray_tmp/`
- 已在 `.bashrc` 添加 `export RAY_TMPDIR=/root/autodl-tmp/ray_tmp`，后续 Ray 启动将自动使用数据盘
- 当前训练的 Ray session 仍在 `/tmp/ray/`，体积很小，不影响

## 4. 监控脚本

- 脚本路径: `/root/autodl-tmp/disk_monitor.sh`
- PID: **183184**
- 每 30 分钟检查根分区可用空间，记录到 `/root/autodl-tmp/disk_monitor.log`
- 低于 2G 时自动清理旧 Ray 日志和非活跃 Hydra outputs

## 5. 训练进程状态

- exp007 训练正常运行中（PID 178842）
- 配置: `_alfworld_exp007_fixed`，CUDA_VISIBLE_DEVICES=0,1
- 日志输出到: `/root/autodl-tmp/exp007_formal.log`
- Ray workers 全部活跃（TaskRunner + WorkerDict + 40 IDLE workers）
