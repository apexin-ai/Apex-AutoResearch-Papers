# westb-23072 磁盘清理日志 — 2026-05-15

## 清理前
- 磁盘: 188G / 250G (76%), 63G 可用

## 删除内容
| 目录 | 大小 | 说明 |
|------|------|------|
| sft_standard_20/checkpoint-935 | 35G | SFT 中间 checkpoint |
| sft_standard_20/checkpoint-1870 | 35G | SFT 中间 checkpoint |
| sft_rasp_20/checkpoint-935 | 12G | SFT 中间 checkpoint |
| sft_rasp_20/checkpoint-1870 | 35G | SFT 中间 checkpoint |
| **合计** | **~117G** | |

## 未删除（不存在）
- recovered_standard_20/, recovered_rasp_20/, recovered_standard_20_4096/, recovered_rasp_20_4096/ — 已不在 westb 上

## 保留确认
- sft_standard_20/model.safetensors — 最终模型完整
- sft_rasp_20/model.safetensors — 最终模型完整
- grpo_stage2_standard_20_v8/checkpoint-50 (12G) — 活跃训练 checkpoint
- .hf_cache (12MB) — 训练依赖
- pruned_rasp_alpha_0.0/, pruned_rasp_alpha_0.25/ (各 12G)

## 清理后
- 磁盘: 74G / 250G (30%), 177G 可用
- 释放: **114G**

## GRPO v8 状态
- PID 534667: 存活, 运行 7h24m
- GPU cuda:1: 71701 MiB / 97887 MiB, 100% 利用率
- checkpoint-50 已保存 (12G)
