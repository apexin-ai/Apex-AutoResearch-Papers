# SSH 连通性检查 — autodl-5090

- **日期**: 2026-05-14
- **连接状态**: ❌ 失败
- **错误信息**: `No authentication methods available`
- **耗时**: 0.87s

## 错误分析

`No authentication methods available` 表明 SSH 客户端无法用 `~/.ssh/config` 中配置的密钥完成认证。常见原因：

1. **AutoDL 实例重启后端口变化**（最可能）— AutoDL 实例重启后 SSH 端口会变，旧端口指向的服务已不存在或指向其他实例
2. 密钥文件权限或路径问题（可能性低，之前同样报错）
3. 实例已关机或被释放

## 建议操作

1. 登录 [AutoDL 控制台](https://www.autodl.com/console/instance/list)，查看 autodl-5090 实例当前状态和 SSH 端口
2. 如果端口已变，更新 `~/.ssh/config` 中 `autodl-5090` 的 `Port` 字段
3. 更新后重新执行本检查任务验证连通性
