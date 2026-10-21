# 诊断报告：latency-profile-n1000

## 结论：实验成功完成，监控误报

实验 `latency-profile-n1000` **实际上已成功运行并产出完整结果**。被报告为"失败"是监控系统的 false positive。

## 根本原因

**脚本不创建 sentinel 文件。** `profile_latency.py` 中没有任何 sentinel 文件创建逻辑（grep 确认），但 submit_training_job 的 cron 监控系统以 sentinel 文件存在作为实验成功的判据。因此：

1. 脚本正常运行 → 正常退出（exit code 0）
2. 监控检查 `logs/sentinels/` → 空目录，无对应 sentinel
3. 监控判定实验失败 → 重启进程
4. 循环 5 次后放弃

## 关键证据

### 日志完整输出（`logs/latency_profile_n1000.log`）
- 所有 9 个 profiling 阶段全部完成
- 打印了完整的 LATENCY PROFILE SUMMARY 表格
- 最后一行：`[profile] Results saved to logs/latency_profile_n1000.json`

### JSON 输出完整（`logs/latency_profile_n1000.json`, 5589 bytes）
- 包含 17 个组件的完整延迟测量数据
- 每个组件 1000 次迭代，统计量齐全（mean/std/min/max/median/p95/p99）

### Sentinel 目录为空
```
/root/acr-vla-conformal-refinement/logs/sentinels/  → 空目录
```

### 脚本无 sentinel 逻辑
```bash
grep -r "sentinel" src/profile_latency.py → 无匹配
```

### GPU 状态正常
- cuda:4 空闲（1MiB, 0% util），进程已正常退出释放资源

## 实验结果摘要（RTX 4090, N=1000, warmup=100）

| 组件 | Mean (ms) | P95 (ms) |
|------|-----------|----------|
| VLA encode_prefix | 43.4 | 71.2 |
| VLA sample K=1 | 213.8 | 220.9 |
| VLA sample K=10 | 211.2 | 215.9 |
| VLA e2e K=1 | 256.5 | 281.0 |
| VLA e2e K=10 | 253.2 | 273.4 |
| CGS compute_features | 5.7 | 6.3 |
| CRM forward | 0.28 | 0.31 |
| Full pipeline K=10 | 249.0 | 270.6 |
| Adaptive fast (K=2, no CRM) | 252.9 | 279.1 |
| Adaptive full (K=2→10 + CRM) | 459.6 | 491.4 |

GPU 峰值显存：1005 MB

## 修复建议

在 `profile_latency.py` 的 `main()` 末尾（保存 JSON 之后）添加 sentinel 文件创建：

```python
# After saving JSON results
sentinel_dir = Path("logs/sentinels")
sentinel_dir.mkdir(parents=True, exist_ok=True)
sentinel_file = sentinel_dir / f"latency_profile_{'n' + str(args.n_measure)}.done"
sentinel_file.write_text(f"completed at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
```

或者，在提交实验时使用自定义的 sentinel 检测逻辑（检查输出 JSON 文件是否存在且非空），而不是依赖脚本自建 sentinel。
