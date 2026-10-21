# 诊断报告: eval-reconvla-spatial-v1

**日期**: 2026-05-14
**服务器**: bjb1-18228
**结论**: 误报——实验仍在正常运行

## 失败根因

**不存在失败。** EXIT_CODE=129 是监控系统的误报（race condition）。进程 PID 87787 当前状态为 `Rl`（running），exit code 文件 `/tmp/agent-ml-exit/eval-reconvla-spatial-v1.exit` 不存在，证明进程从未退出。

## 证据

### 进程状态
```
PID 87787  状态: Rl  CPU: 273%  RSS: ~12GB
python -u src/evaluate.py --mode reconvla --benchmark spatial ...
```

### GPU 状态
```
GPU 2: NVIDIA RTX 4090, 1414MiB / 24564MiB, PID 87787
```

### tmux session
```
eval-reconvla-spatial-v1: 1 windows (created Thu May 14 04:26:52 2026) — 存活
```

### 日志内容（全部 14 行）
日志在 `[eval] 10 tasks loaded.` 后结束，无 traceback、无 OOM、无 segfault。这是正常的——代码在 rollout 循环中每 5 轮才打印进度，第一批尚未完成。

### exit code 文件
```
/tmp/agent-ml-exit/eval-reconvla-spatial-v1.exit — 不存在（进程未退出）
```

## 代码路径验证

- `reconvla` 模式不需要 `--checkpoint`（代码正确跳过 CRM 加载）
- `reconvla_baseline.py` 存在且已成功导入
- SmolVLA 模型加载成功（489/489 weights loaded）
- LIBERO spatial 环境加载成功（10 tasks）

## 修复建议

无需修复。等待实验自然完成即可。每个 task 10 rollouts × 10 tasks × max 300 steps，预计总运行时间 1-3 小时。

## 是否可以直接重试

不需要重试——实验正在运行中。

## 根因分析：为什么报了 EXIT_CODE=129

可能原因：
1. 监控轮询在进程启动初期读取了尚未创建的 exit code 文件，误判为异常退出
2. wrapper shell 的 `trap 'exit 129' HUP` 被监控系统误读为已触发的退出码
3. 存在同名的旧 exit code 文件残留（但 wrapper 启动时 `rm -f` 已清理）

建议检查监控逻辑中对 "exit code 文件不存在" 这一状态的处理。
