# 诊断: eval_math500_sft_random_20 失败

**日期**: 2026-05-22  
**实验**: eval_math500_sft_random_20  
**服务器**: westd-29022  

## 失败根因

**westd-29022 服务器宕机，SSH 完全无法连接。**

连接测试结果：
```
[Errno None] Unable to connect to port 29022 on 36.103.198.204
```

实验未能启动或在运行中因服务器宕机而中断。无法读取日志确认具体错误，因为服务器不可达。

## westd-29022 当前状态

| 项目 | 状态 |
|------|------|
| SSH 连接 | ❌ 失败 (port 29022 unreachable) |
| GPU 可用性 | 未知 (无法连接) |
| 磁盘空间 | 未知 (无法连接) |
| 对比 westb-23072 | ✅ 正常连接 |

结论：westd-29022 仍处于宕机状态，非网络问题（westb-23072 同时间连接正常）。

## 是否可以重新提交

**不可以。** westd-29022 仍然离线，需等待服务器恢复或将实验迁移到其他可用 GPU。

可选方案：
- 等待 westd-29022 恢复
- 将 eval_math500_sft_random_20 迁移至 westb-23072（需确认 GPU 空闲 + checkpoint 可访问）

## 受影响的待处理实验

以下实验分配在 westd-29022 上，同样无法提交：
- eval_gsm8k_grpo_alpha4_20_v2 (cuda:1)
- 其他待提交至 westd-29022 的实验
