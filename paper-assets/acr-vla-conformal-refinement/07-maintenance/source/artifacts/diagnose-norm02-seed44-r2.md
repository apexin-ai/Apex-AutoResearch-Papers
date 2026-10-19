# 诊断: eval-obs-only-object-norm02-seed44-r2

## 结论：实验已正常完成，EXIT_CODE=129 是误报

### 根因

实验脚本**已完整执行完毕**，所有 10 个 task × 10 rollouts = 100 次评估全部完成。SIGHUP (exit code 129) 是在脚本输出结果并退出后，wrapper/tmux session 收到的挂断信号，不影响实验结果。

### 证据

1. Log 最后几行显示正常结束：
```
============================================================
Overall success rate (crm_obs_only): 16.0% (16/100)
============================================================
[eval] Results saved to logs/eval_object_obs_only_norm02_seed44.json
```

2. 结果文件存在且完整：
```
-rw-r--r-- 1 root root 1490 May 16 22:38 logs/eval_object_obs_only_norm02_seed44.json
```

3. 所有 10 个 task 的结果均已记录到 JSON 中。

### 实验结果

- **Overall success rate: 16.0% (16/100)**
- obs_only CRM, norm=0.2, seed=44, benchmark=object

### 是否需要重试

**不需要重试。** 实验已成功完成，结果已保存。可直接用于 3-seed Fisher test。
