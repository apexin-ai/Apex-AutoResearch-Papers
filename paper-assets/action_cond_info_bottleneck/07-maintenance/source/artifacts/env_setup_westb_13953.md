# 环境搭建报告: westb-13953

**日期**: 2026-05-15
**状态**: ❌ 失败 — SSH 连接超时

## SSH 连接测试

| 尝试 | 工具 | 结果 | 耗时 |
|------|------|------|------|
| 1 | ssh_read_only | timed out | 10.51s |
| 2 | ssh_read_only | timed out | 10.10s |
| 3 | ssh_read_only | timed out | 10.07s |
| 4 | ssh_execute | timed out | 10.10s |
| 5 | detect_image | SSH error: timed out | — |

## 错误详情

- **错误类型**: timeout（非 connection refused，非 auth failure）
- **目标**: `ssh -p 13953 root@connect.westb.seetacloud.com`
- **每次超时**: ~10 秒（SSH 工具默认超时）
- **尝试的工具**: ssh_read_only、ssh_execute、detect_image — 全部超时

## 可能原因

1. AutoDL 实例已关机或休眠
2. 端口 13953 已变更（AutoDL 重启后端口会变）
3. 服务器端 sshd 未运行
4. 网络路由问题（connect.westb.seetacloud.com 不可达）

## 建议

- 登录 AutoDL 控制台确认实例状态（运行中 vs 已关机）
- 确认当前 SSH 端口是否仍为 13953
- 如端口已变，更新 `~/.ssh/config` 和项目配置后重试

## 未完成步骤

- [ ] 镜像检测
- [ ] 环境探测（Python/torch/CUDA/GPU/磁盘）
- [ ] 安装 lerobot[smolvla]、wandb、einops、accelerate
- [ ] 安装 LIBERO
- [ ] 安装验证
