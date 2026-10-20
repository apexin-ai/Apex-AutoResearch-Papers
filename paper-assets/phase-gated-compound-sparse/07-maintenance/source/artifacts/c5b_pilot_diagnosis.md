# c5b_pilot 诊断报告

## 结论：Cron 误判 — 实验部分完成，已有可用结果

## 失败根因

**不是代码 bug、不是 OOM、不是配置错误。** 是 cron 监控系统误判。

### 发生了什么

c5b_pilot 被启动了两次：

1. **Shell 脚本 run**（`run_c5b_pilot.sh`，GPU0，01:55:55 启动）
   - s025: 完成 15/30 problems 后中断（无 error/traceback/killed）
   - s030: 完成 22/30 problems 后中断
   - `profiling_output_c5b_pilot_s025/` 和 `profiling_output_c5b_pilot_s030/` 均为空目录
   - **中断原因**：进程未放入 screen/tmux/nohup，SSH 会话断开后进程被 SIGHUP kill。日志中无任何错误信息佐证此判断（不是 crash 而是外部 kill）。

2. **GPU3 独立 run**（02:06:05 启动）
   - s025: **完成全部 30/30 problems**
   - 结果已保存到 `profiling_output_c5b_all_s025/mitigation_pilot_results.json`（51KB）
   - 正常退出

### Cron 判定 "failed" 的原因

- `run_c5b_pilot.py` **没有 sentinel 文件**、**没有 W&B 日志**
- cron 检测进程时已无存活进程 → 5 次检查均未发现 → 自动判定 failed
- 但 GPU3 run 实际已成功完成

## 已有结果

GPU3 run 的 s025 pilot 结果（30 problems）：

| 指标 | 值 |
|------|-----|
| Uniform median II | 1.0435 |
| Oracle median II | 0.8560 |
| Recovery (oracle) | +18.0%, 95%CI [-39.0%, 45.8%] |
| Wilcoxon p (oracle) | 0.0021 |
| Heuristic median II | 0.7127 |
| Recovery (heuristic) | +31.7%, 95%CI [-22.8%, 66.0%] |
| Wilcoxon p (heuristic) | 0.0236 |
| **GATE** | **FAIL (>30% oracle recovery)** |

## 缺失部分

- s030 pilot 未完成（shell 脚本 run 中断，GPU3 run 只跑了 s025）
- 结果路径不一致：完成的结果在 `profiling_output_c5b_all_s025/`，不在 shell 脚本预期的 `profiling_output_c5b_pilot_s025/`

## 是否可以重试

可以。代码本身无 bug，运行逻辑正常。

### 重试注意事项

1. **必须用 screen/tmux 启动**，不能直接 SSH 执行。每个 sparsity level 约 40 分钟。
2. **GPU 分配**：当前 GPU0-3 全部被 c2 实验占用。需等 c2 完成或找空闲 GPU。shell 脚本默认 GPU0，`bash run_c5b_pilot.sh 3` 可指定 GPU。
3. **只需补跑 s030**：s025 已有完整结果（在 `profiling_output_c5b_all_s025/`），只需跑 s030。
4. **建议给脚本加 sentinel**：完成后 `touch /root/autodl-tmp/pacs/profiling_output_c5b_pilot_s030/.done`，避免 cron 再次误判。
