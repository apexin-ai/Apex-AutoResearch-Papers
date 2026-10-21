# 诊断报告: exp_002_signals_3B_d000_s123_cuda2

## 失败原因（一句话）

**误报 (False Positive)**：进程实际正常运行在 GPU 0，但监控系统因 sentinel 文件名/路径不匹配而 5 次 poll 失败后自动标为 failed。

## 详细分析

### 1. 进程状态

- **进程存活**：PID 780943 在 GPU 0 占用 6707MiB，正在执行 `Self-critique mmlu` 分块推理
- **启动时间**：2026-05-16 20:32:23 CST
- **已完成任务**：8/9（s1, s2, s4 × mmlu, gsm8k, arc_challenge）
- **输出目录**：`/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_s123_a32/` 已有 9 个信号文件

### 2. 根因：GPU 分配错误 + Sentinel 不匹配

| 问题 | 详情 |
|------|------|
| 声明 GPU | cuda:2 |
| 实际 GPU | GPU 0（日志明确写 `START d000_s123_a32 signals (9 tasks) on GPU 0`） |
| 期望日志 | `/tmp/3B_d000_s123_signals_cuda2.log`（不存在） |
| 实际日志 | `/tmp/3B_d000_s123_signals.log`（903KB，持续更新中） |
| Sentinel | `/tmp/agent-ml-exit/` 下无 `exp_002_signals_3B_d000_s123_cuda2.exit` |

监控系统 5 次检查 sentinel + W&B 均未找到匹配条目 → 自动判定 "process dead" → 标为 failed。

### 3. 非致命错误（不影响执行）

```
[ERROR] bitsandbytes.cextension: bitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file
```
bitsandbytes 尝试加载 CUDA JIT 库失败，fallback 到 CPU 模式。不影响信号计算。

### 4. GPU 2 当前状态

cuda:2 完全空闲（0MiB / 0% utilization），无任何进程占用。

## 修复建议

1. **无需重新提交**：进程仍在正常运行，预计很快完成（仅剩 s4_selfcritique_mmlu 的剩余 chunks）
2. **更新实验状态**：将 exp_002 从 "failed" 改为 "running"，关联实际日志路径 `/tmp/3B_d000_s123_signals.log`
3. **根因修复（C004 违规）**：提交脚本未正确传递 `CUDA_VISIBLE_DEVICES=2`，导致进程落到 GPU 0。未来必须在 nohup/tmux 命令中显式 `export CUDA_VISIBLE_DEVICES=N`
4. **监控系统改进**：sentinel 检测应支持模糊匹配日志文件名，或通过 PID 追踪而非文件名匹配

## 约束违规记录

- **C004 违规**：声明 cuda:2 实际跑在 cuda:0（未显式设置 CUDA_VISIBLE_DEVICES）
- 这是 C004 约束记录的同类事故
