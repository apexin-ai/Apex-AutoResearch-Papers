# monitor phase2 tg s42 v4 check1

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_phase2_tg_s42_v4_check1_20260518T153156_result.json`
- **Structured JSON:** [`38ceb60f7af8fb30f31e.json`](../../sessions/38/38ceb60f7af8fb30f31e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SSH 连接中断，无法继续查询。基于中断前收集的数据汇报：

---

```
训练状态: 运行中（但日志不可读）
当前步数: 未知（日志被缓冲，无法读取）
参数确认: ✓ lambda_gar=1.0, init_bias=1.5, gate_lr_multiplier=10, 
          gar_loss_mode=maximize, epochs=3, grad_accum=8, batch_size=1
总 loss 趋势: 未知（日志缓冲问题）
GAR 稳态: 未知
Gate 分化: 未知
L4 状态: 无数据
预计完成: 无法估算（不知道当前步数）
```

**异常：两个问题**

**1. 日志缓冲（关键问题）**
`train_phase2.py` 所有 `print()` 都没有 `flush=True`。进程通过 `| tee file.log` 运行，Python 检测到 stdout 不是 TTY，自动切换为 8KB block buffering。结果：日志文件只有模型加载的 8 行输出，32 分钟的训练指标全部卡在内存缓冲区里。

**2. SSH 连接中断**
最后几次查询开始，westd-20861 SSH 端口无法连接。可能是云平台临时网络问题。

**GPU 状态（中断前最后一次读取）：**
- GPU 利用率 96%，VRAM 85GB/98GB
- 进程运行 32 分钟，CPU 时间 33 分钟（几乎 100% CPU）
- 训练在正常计算，只是看不到日志

**建议操作：**
1. SSH 恢复后，在 tmux 里用 `tmux capture-pane -t phase2_tg_s42_v4 -p -S -500` 读 tmux 缓冲区获取实时输出（tee 缓冲了，但 tmux 的 pane 里应该也有 Python 的缓冲，所以可能同样看不到）
2. 实际上 Python pipe 缓冲意味着连 tmux pane 也看不到输出。最可靠的方案：等训练结束时缓冲自动 flush，日志会一次性全部写入
3. 如果需要立刻看到指标，可以 `kill -USR1` 或在下次实验中启动时加 `PYTHONUNBUFFERED=1` 环境变量，或在代码中加 `flush=True`

---
