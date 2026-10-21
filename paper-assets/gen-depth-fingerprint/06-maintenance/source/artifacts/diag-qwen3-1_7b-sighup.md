# 诊断报告：Qwen3-1.7B 生成实验 SIGHUP 失败

**日期**: 2026-05-14
**服务器**: autodl-5090 (RTX 5090 × 4)
**实验**: plan-002-qwen3-1_7b-s0/s1

## 失败现象

两个 shard 同时在 ~21 分钟后终止：
- s0: 完成 104/498 seeds (21%), EXIT_CODE=129 (SIGHUP)
- s1: 完成 95/498 seeds (19%), EXIT_CODE=129 (SIGHUP)

日志末尾仅有 "Terminated"，无 Python 异常、无 OOM、无 CUDA 错误。

此前还有一次更早的尝试（plan-002-qwen17b），EXIT_CODE=143 (SIGTERM)，仅跑了 19 个 seeds。

## 直接原因

进程收到 SIGHUP 信号（信号 1），被操作系统终止。

## 根因分析

**SSH 会话断开导致 SIGHUP 广播。**

证据链：
1. 两个独立进程在完全相同的时间点（05:13）同时死亡 → 会话级事件，非进程级问题
2. EXIT_CODE=129 = 128+1 = SIGHUP，这是终端断开时内核发给前台进程组的标准信号
3. 排除项：
   - 磁盘空间充足：根分区 22GB 可用，数据盘 161GB 可用
   - GPU 正常：两卡空闲无报错
   - 非 OOM：日志无内存相关错误
   - 同服务器 pythia-1b 实验成功完成 → 服务器本身无问题
4. AutoDL 网络环境已知不稳定

## 附带问题

1. **输出全部丢失**：`data/qwen3-1.7b/` 目录为空。脚本使用 Python 默认缓冲写入，SIGHUP 时用户态缓冲区未 flush，~100 个 seeds 的生成结果全部丢失。

2. **两个 shard 都在 cuda:0**：两份日志均显示 "Model loaded on cuda:0"。脚本默认 `--device cuda:0`，启动命令未给 s1 指定 `--device cuda:1`，导致两个 1.7B 模型挤在同一张 GPU 上。

## 修复建议

### 必须修复
1. **用 tmux/nohup 隔离进程**：防止 SSH 断连杀死实验进程
   ```bash
   # 方案 A: tmux
   tmux new-session -d -s qwen3-s0 'python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --shard-id 0 --num-shards 2 --device cuda:0 > ~/runs/gen-depth-fingerprint/plan-002-qwen3-1_7b-s0.log 2>&1'
   tmux new-session -d -s qwen3-s1 'python generate_chain.py --model-name qwen3-1.7b --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base --shard-id 1 --num-shards 2 --device cuda:1 > ~/runs/gen-depth-fingerprint/plan-002-qwen3-1_7b-s1.log 2>&1'
   
   # 方案 B: nohup
   nohup python generate_chain.py ... > logfile 2>&1 & disown
   ```

2. **给 s1 显式指定 `--device cuda:1`**

### 建议修复
3. **给脚本加 flush**：在 `f.write()` 后加 `f.flush()`，或用 `open(path, "w", buffering=1)` 行缓冲，防止崩溃丢数据
