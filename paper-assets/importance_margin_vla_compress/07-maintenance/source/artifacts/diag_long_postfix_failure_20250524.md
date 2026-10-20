# Long Post-fix 实验批量"失败"诊断报告

**日期**: 2026-05-24
**结论**: **全部为监控系统误报，实验本身运行正常**

## 根因

监控系统通过检查 sentinel 文件和 W&B run 来判断进程存活。这批 Long eval 实验不使用 W&B，也不写 sentinel 文件，导致健康检查连续 5 次找不到信号后自动判定为 "process dead"。

错误信息 "process dead 5× with no sentinel/W&B — auto-resolved as failed" 本身就描述了原因：缺少监控信号，不是进程真的死了。

## 实验实际状态

### westd-38929（已完成 + 运行中）

| 实验 | 状态 | 结果 |
|------|------|------|
| random k=0.7 libero_10 50ep | ✅ 完成 | SR=65.8% |
| l2norm k=0.95 libero_10 50ep | ✅ 完成 | SR=87.0% |
| random k=0.5 libero_10 50ep | 🔄 运行中 (T9 ep=40) | ~进行中 |
| random k=0.3 libero_10 50ep | 🔄 运行中 (T8 ep=10) | ~进行中 |

### westd-41074（已完成 + 运行中）

| 实验 | 状态 | 结果 |
|------|------|------|
| random k=0.85 libero_10 50ep | ✅ 完成 | SR=45.2% |
| random k=0.95 libero_10 50ep | ✅ 完成 | SR=63.2% |
| l2norm k=0.85 libero_10 50ep | ✅ 完成 | SR=78.4% |
| random k=0.9 libero_10 50ep | 🔄 运行中 (T8 ep=30) | ~进行中 |
| l2norm k=0.3 libero_10 50ep | 🔄 运行中 (T2 ep=30) | ~进行中 |

## 日志检查结果

- **无 Error / Exception / Traceback / OOM / CUDA 错误 / segfault / killed**
- 所有日志内容均为正常评估输出（task progress, success rate）
- 已完成的实验都正常写入了 JSON 结果文件到 `eval_results/`
- 进程 PID 确认存活，CPU 占用 >400%（正常多线程推理）

## 是否所有失败共享同一根因

**是**。全部是同一个问题：eval 脚本不写 sentinel 文件，不连 W&B，监控系统无法通过这两个渠道确认进程存活。

## 正在运行的实验是否有风险

**无风险**。4 个仍在运行的实验进程健康，日志持续输出，无任何异常信号。预计各在 1-3 小时内完成。

## 修复建议

1. **短期（无需改动）**: 已完成的实验结果已保存到 `eval_results/` 目录，可直接使用。仍在运行的实验不需要干预。
2. **长期**: 如果后续还要大批量跑 Long eval，可在 eval 脚本中添加简单的 sentinel 心跳（如定期 touch 一个文件），避免监控系统误报。

## 已完成实验结果汇总

| Method | k | SR (libero_10, 50ep) |
|--------|-----|-----|
| l2norm | 0.95 | 87.0% |
| l2norm | 0.85 | 78.4% |
| random | 0.7 | 65.8% |
| random | 0.95 | 63.2% |
| random | 0.85 | 45.2% |
