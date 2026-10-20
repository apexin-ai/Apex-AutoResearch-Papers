# westd-11672 诊断报告 (2026-05-18)

## 连接状态：不可达

- **SSH 连接**: 失败 — `Unable to connect to port 11672 on 36.103.198.204`（耗时 1.21s）
- **Ping 测试**: 成功 — 3/3 packets, RTT avg 70.3ms, 0% packet loss
- **端口扫描**: port 11672 关闭（nc -z 超时）

## 诊断结论

主机 IP 36.103.198.204 网络层可达，但 SSH 端口 11672 无响应。可能原因：
1. **AutoDL 实例被关机/休眠** — 最常见原因，账户余额不足或手动关机
2. **SSH 服务崩溃** — 主机在线但 sshd 未运行
3. **端口映射失效** — AutoDL 平台侧网络配置异常

## 受影响实验（4 个）

以下结果文件状态未知（无法连接确认）：
- `/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_standard_20.json`
- `/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_rasp_20_v3.json`
- `/root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20.json`
- `/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20.json`

## 建议

1. **需要人工介入**: 登录 AutoDL 控制台检查 westd-11672 实例状态（是否关机/欠费）
2. **如果是关机**: 重新开机后，SSH 端口映射通常会自动恢复
3. **结果可恢复性**: 取决于实验在中断前是否已写入结果文件。连接恢复后需立即检查上述 4 个 JSON 文件和对应 log
4. **备选方案**: 如果短期无法恢复，可在 westb-23072 上重跑失败实验（但需注意 GPU 资源调度）
