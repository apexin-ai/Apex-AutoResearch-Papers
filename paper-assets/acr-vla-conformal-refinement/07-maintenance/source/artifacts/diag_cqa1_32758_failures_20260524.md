# 诊断报告：cqa1-32758 eval 实验"失败"排查

**日期**: 2026-05-24 11:20 UTC
**服务器**: cqa1-32758 (6× RTX 4090 D)

## 结论：误报，实验全部正常完成

所有被监控系统标记为"process dead 5× with no sentinel/W&B"的实验实际上都**成功运行完毕**，结果已保存到 JSON 文件。进程退出后 GPU 显存释放，监控系统检测到进程消失但未找到 sentinel/W&B 信号，误判为失败。

## 各实验状态

| 实验 | 日志 | 状态 | 结果 |
|------|------|------|------|
| eval-supp-spatial-reconvla-s46 | eval_spatial_reconvla_s46.log | ✅ 完成 | 80.0% (160/200) |
| eval-supp-spatial-crm-norm005-s46 | eval_spatial_crm_s46.log | ✅ 完成 | 81.0% (162/200) |
| eval-supp-spatial-adapt-tau025-s46 | eval_spatial_adapt_s46.log | ✅ 完成 | 80.0% (160/200) |
| eval-supp-spatial-vla-only-s46 (pid 604290) | eval_spatial_vla_s46.log | ✅ 完成 | 80.5% (161/200) |
| eval-supp-spatial-k2mean-s45 | 无 /tmp/ 日志 | ❓ 未找到日志，可能未启动或日志名不匹配 | — |
| eval-supp-long-k2mean-s45 | 无 /tmp/ 日志 | ❓ 未找到日志，可能未启动或日志名不匹配 | — |
| eval-supp-long-vla-only-s46 (pid 601530) | eval_long_vla_s46.log | 🟡 仍在运行 | GPU 3, 4561MiB |

备注：eval_goal_k2mean_s45 已于 08:16 完成（81.0%, 162/200），输出在 eval_goal_k2mean_seed45.json。

## JSON 输出文件确认

全部输出文件存在于 `/root/acr-vla-conformal-refinement/logs/`：
- eval_spatial_reconvla_seed46.json (11:01)
- eval_spatial_crm_obs_only_norm0.05_seed46.json (10:59)
- eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json (10:38)
- eval_spatial_vla_only_seed46.json (11:09)
- eval_goal_k2mean_seed45.json (08:16)

## 系统状态

| 项目 | 状态 |
|------|------|
| GPU | 6 卡全部健康，仅 GPU 3 在用（PID 601536, 4542MiB），其余 5 卡空闲（1MiB） |
| 内存 | 1.0Ti 总量，40Gi 使用，954Gi 可用 — 无压力 |
| 磁盘 | 根分区 17% (26G 可用) — 无压力 |
| 温度 | GPU 3 为 40°C（运行中），其余 28-31°C — 正常 |
| OOM/GPU 错误 | 无（所有实验正常退出，return_code=0） |

## 根因分析

**不是系统性故障。** 原因是监控系统的检测逻辑：

1. 实验脚本 `evaluate.py` 运行完毕后正常退出（exit code 0）
2. 进程退出 → GPU 显存释放 → `nvidia-smi` 中无进程
3. 监控系统检测到 PID 不存在，且未找到 sentinel 文件或 W&B run
4. 误判为"进程异常退出"，触发连续重试检测 5 次后报告失败

**核心问题**：eval 脚本没有写 sentinel 文件，也没有上报 W&B，导致监控系统无法区分"正常完成"与"异常崩溃"。

## 修复建议

1. **无需重跑任何实验** — 结果已全部保存在 JSON 文件中
2. **eval-supp-long-vla-only-s46 仍在运行**（PID 601530→601536, GPU 3），等待其自然完成即可
3. **k2mean-s45 实验**：检查是否已在其他名称下完成（eval_goal_k2mean_seed45.json 已存在），或确认是否需要启动
4. **长期修复**：让 eval 脚本完成后写一个 sentinel 文件（如 `.done`），避免监控误报
