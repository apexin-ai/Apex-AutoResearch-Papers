# bjb2-4x5090-b 环境验证状态

**检查时间**: 2026-04-29
**状态**: ❌ BLOCKED — SSH 认证失败

## 问题

SSH 连接 `bjb2-4x5090-b`（connect.bjb2.seetacloud.com:10838, user=root）失败：

```
Permission denied (publickey,password)
```

## 原因分析

AutoDL 实例重启后 SSH 端口会变。当前 `~/.ssh/config` 中配置的端口 **10838** 可能已过期。

## 需要的操作

1. 登录 AutoDL 控制台，确认 bjb2-4x5090-b 实例状态（是否在运行）
2. 获取当前 SSH 端口号
3. 更新 `~/.ssh/config` 中 `bjb2-4x5090-b` 的 Port 字段
4. 重新执行环境验证

## 待验证项（SSH 恢复后执行）

- [ ] 代码版本（git log）
- [ ] Qwen2.5-7B-Instruct 模型路径
- [ ] Gemma-2-9B-it 模型路径（可能需要下载，~18GB）
- [ ] vLLM 版本
- [ ] GPU 状态（4x RTX 5090）
- [ ] 端口占用（8000-8009）
- [ ] AG2/autogen 依赖
