# vanilla_v2_s1 诊断报告

## 结论：训练已成功完成，Cron 监控误报

## 失败原因
**无实际失败。** 进程正常退出（训练完成后退出），但 Cron 监控未检测到 sentinel 文件或 W&B run，将正常退出误判为 crash，触发 "process dead 5x — auto-resolved as failed"。

## 训练进度
- **完成度：100%**（50005/50005 steps）
- 最后一条 AUX log：`step=50000, occ_loss=0.0000, depth_loss=0.0000, action_loss=0.0889`
- 日志末尾：`Max step 50005 reached! Stopping training...`
- 总训练时间：约 13h46m

## Checkpoint 状态
| Checkpoint | 路径 | 时间 |
|-----------|------|------|
| step 40000 | `vanilla_v2_s1/...-40000_chkpt/` | May 27 03:49 |
| step 50000 | `vanilla_v2_s1/...-50000_chkpt/` | May 27 06:32 |

LoRA adapter + merged model 均已保存。

## GPU 状态（诊断时 May 27 06:44 UTC）
- cuda:0：空闲，0MiB 占用，无残留进程
- cuda:1：空闲
- cuda:2：空闲
- cuda:3：被 PID 453661 占用（62194MiB，另一个实验）

## 对比 vanilla_v2_s2
vanilla_v2_s2（cuda:1, seed 44）日志结尾与 s1 完全一致：
- 同样跑完 50005 步，输出 "Max step 50005 reached!"
- 同样有 `destroy_process_group` warning（无害）
- s2 的 action_loss=0.0708 vs s1 的 0.0889（正常种子间差异）

## 是否需要重启
**否。** 训练已完成，无需任何操作。

## 建议
修复 Cron 监控逻辑：当进程退出且最终 checkpoint 已保存到 max_steps 时，应判定为成功而非失败。
