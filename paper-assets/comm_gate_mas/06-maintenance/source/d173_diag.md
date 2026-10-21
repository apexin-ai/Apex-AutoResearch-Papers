# D173 Oracle Online 诊断报告

**日期**: 2026-04-27  
**实验**: oracle_online_llama_gsm8k (seed 42, 200 tasks)

## 失败根因：两个 vLLM 实例被外部 SIGTERM 同时杀死

### 时间线

| 时间 | 事件 |
|------|------|
| 08:55 | vLLM Llama-8B 启动 port 8001 (PID 553674, gpu_mem=0.22) |
| 09:02 | vLLM Qwen72B-AWQ 启动 port 8002 (PID 558580, gpu_mem=0.85) |
| 09:06:34 | 实验启动 (seed=42, 200 tasks) |
| 09:09:32 | Task 1/200 完成 |
| 09:11:53 | Task 2/200 完成 |
| 09:12:57 | 最后一条实验日志（正在处理 task 3） |
| **09:13:34** | **两个 vLLM 同时 `Shutdown initiated (timeout=0)` → EngineDeadError** |
| 09:28 | 新 Llama vLLM 启动 (PID 567489) 但很快也死亡，无错误日志 |

### 关键证据

两个独立 vLLM 进程在同一秒被 graceful shutdown：
```
vllm_llama_8b.log:   (EngineCore pid=553963) Shutdown initiated (timeout=0) @ 09:13:34
vllm_qwen72b.log:    (EngineCore pid=559255) Shutdown initiated (timeout=0) @ 09:13:34
```

这是 SIGTERM（非 OOM/内部崩溃）。OOM 不会产生 graceful shutdown，内部错误不会让两个独立进程同时死亡。

**最可能的原因**：服务器上其他项目的 agent/worker 执行了 `pkill -f vllm` 或类似命令，误杀了 comm_gate_mas 的 vLLM 进程。

## 次要问题

### 1. 无 GPU 绑定
两个 vLLM 都**没有设置 `CUDA_VISIBLE_DEVICES`**：
- Llama: `{port: 8001, gpu_memory_utilization: 0.22}` — 无 GPU 指定
- Qwen72B: `{port: 8002, gpu_memory_utilization: 0.85}` — 无 GPU 指定

项目分配的是 cuda:1，但 vLLM 默认用 cuda:0。

### 2. Oracle 推理极慢
Qwen72B-AWQ 生成吞吐约 2.2-2.5 tokens/s。单个 task 需要约 2-3 分钟（含 baseline + oracle 两轮对话）。200 tasks × 10 seeds ≈ 70-100 小时。

### 3. 无崩溃恢复
vLLM 死亡后实验直接挂起/崩溃，无自动重连或重启逻辑。

## cuda:1 当前状态

- 空闲：3MiB / 97887MiB, 0% 利用率
- 无残留进程
- 模型文件完整：Llama-3.1-8B-Instruct (15GB), Qwen2.5-72B-Instruct-AWQ (41GB)
- 数据盘 84% 已用 (58GB 剩余)

## 修复建议

1. **启动 vLLM 时必须指定 GPU**：`CUDA_VISIBLE_DEVICES=1 vllm serve ...`
   但 Qwen72B-AWQ (gpu_mem=0.85=83GB) + Llama (gpu_mem=0.22=21.5GB) = 104.5GB > 98GB，无法同放一张卡。

2. **方案 A：双 GPU（需协调）**
   - Llama 放 cuda:1，Qwen72B 放 cuda:0 或 cuda:3
   - 需与其他项目协调 GPU 分配

3. **方案 B：预计算 oracle 标签（推���）**
   - 先用 Qwen72B 离线计算所有 task 的 oracle labels
   - 实验时只需 Llama vLLM（gpu_mem=0.22，cuda:1 完全够用）
   - 大幅减少运行时间

4. **方案 C：缩小规模验证**
   - 先跑 num_tasks=20 验证 pipeline 端到端正确
   - 确认无误后再上完整规模

5. **增加韧性**：实验脚本加 vLLM 存活检测 + 自动重试
