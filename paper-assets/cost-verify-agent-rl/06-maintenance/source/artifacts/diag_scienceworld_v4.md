## scienceworld_grpo_cell_c_v4 失败诊断

### 错误摘要

TaskRunner 进程在训练步骤 0 的 rollout 阶段 silent crash（无 Python traceback），validation 阶段已成功完成。stderr 未被日志捕获，直接根因无法从现有日志确定。

### 错误详情

**时间线**：
- 12:06:02 — 实验启动（日志文件创建）
- 12:09:48 — Ray session 启动，WorkerDict(pid=389842,389843) 开始加载模型
- 12:10:28 — vLLM 初始化完成
- 12:10:38 — wandb 初始化，stdout 重定向到 wandb
- 12:10:40 — 进入 validation（val_before_train=True）
- 12:13:30 — validation 完成（耗时 174.85 秒）
- 12:13:31 — 打印 step:0 validation 指标 + `Training Progress: 0%`
- 12:13:31~12:15:56 — 训练 rollout 执行中，wandb 持续发送心跳
- ~12:15:56 — wandb 心跳停止，进程已死亡

**Validation 指标（step 0）**：
```
success: 0.0  |  final_score: 4.84/10  |  action_is_valid: 0.52
num_actions: 7.53  |  pass@1: 0.0  |  reward_mean@32: 0.484
```

**最后一行输出**（wandb output.log 第 534 行）：
```
Training Progress:   0%|          | 0/15 [00:00<?, ?it/s]
```
此后进程 silent exit，无任何 traceback 或 error 信息。

### 根因分析

**直接原因无法确定**——因为 stderr 未被日志捕获。主日志文件仅记录 stdout（通过 Ray log dedup），wandb output.log 也只有 stdout。

**基于证据的推断**：

1. **崩溃位置**：`agent_proxy.rollout(batch, val=False)` —— 训练 rollout（128 环境 = 8 groups × 16 group_size），明确在这行代码执行期间
2. **WorkerDict 未崩溃**：两个 WorkerDict 进程（pid=389842, 389843）仍在 GPU 上运行（各占 37.6GB/97.9GB），说明 vLLM 推理和 FSDP 模块正常
3. **TaskRunner(pid=389637) 是崩溃的进程**：负责环境管理和 rollout 协调
4. **ScienceWorld JVM 共享问题**：128 个 `ScienceWorldTXTEnv` 实例通过 `_ENV_CACHE`（per-thread）共享同一个 JVM gateway。训练需要 128 环境同时活跃（vs validation 只有 32），JVM 资源压力 4 倍
5. **最可能的崩溃原因**（按概率排序）：
   - **JVM segfault / Py4J gateway crash**：128 个 ScienceWorld 实例共享一个 JVM（`-Xmx8g`），快速连续的 `load()`/`reset()`/`step()` 调用导致 JVM 内部状态损坏或内存不足，segfault 直接终止 TaskRunner 进程（无 Python traceback）
   - **CUDA OOM 在 vLLM 推理中**：训练 rollout 首轮需要同时推理 128 个序列（val 只有 32），虽然理论上 KV cache 容量足够，但存在碎片或峰值占用风险
   - **Ray 通信超时**：TaskRunner 调用 WorkerDict 的 remote 方法超时，Ray 框架终止 TaskRunner

### JVM 共享的架构缺陷

`ragen/env/scienceworld/env.py` 第 34-36 行：
```python
def _get_cached_env(force_new=False):
    tid = threading.current_thread().ident
    ...
    _ENV_CACHE[tid] = scienceworld.ScienceWorldEnv("")
    return _ENV_CACHE[tid]
```

128 个环境实例共享一个 `ScienceWorldEnv` 对象。虽然 `reset()` 时各自调用 `load(task, variation)` 捕获初始 observation，但在 multi-turn rollout 的 `step()` 阶段，所有环境对同一个 JVM 对象调用 `step(action)`，导致：
- 游戏状态被最后一个 `load()` 覆盖（只有最后加载的任务是活跃的）
- `step()` 的结果基于错误的游戏状态
- 这也解释了 validation 的 success=0%（32 个环境共享一个 JVM，action_is_valid 仅 0.52）

### 历史对比

- v2/v3 日志不在 bjb1-17606 服务器上，无法直接对比
- v3 结果为 "step 3 success=0%"，与 v4 validation 的 success=0% 一致，可能也受 JVM 共享问题影响
- v3 使用 `model_path: scienceworld_sft`，v4 改为 `qwen3_scienceworld_sft`（不同模型）

### 修复建议

**P0 — 立即修复（让实验能运行）**：
1. **捕获 stderr**：启动脚本改为 `python train.py ... 2>&1 | tee log.log` 或 `> log.log 2>&1`，确保下次崩溃时有 traceback
2. **清理残留 GPU 进程**：`ray stop` 终止当前仍在 GPU 上的 WorkerDict 进程（pid=389842, 389843）

**P1 — 根本修复**：
3. **修复 JVM 共享 bug**：每个 `ScienceWorldTXTEnv` 实例应持有独立的 `ScienceWorldEnv` JVM 对象，或在 `step()` 前调用 `load(self.current_task, self.current_variation)` 恢复正确的游戏状态
4. **减少同时活跃的 JVM 数量**：group_size 16 → 4 或 8，降低 128 → 32-64 环境
5. **增加 JVM heap**：`-Xmx8g` → `-Xmx16g`，或为不同线程分配独立 JVM

**P2 — 防御性措施**：
6. **训练 rollout 添加 try-except**：在 `agent_trainer.py:1251` 处 wrap `agent_proxy.rollout` 调用，捕获并记录异常
7. **vLLM 内存监控**：在 rollout 前后打印 `torch.cuda.memory_allocated()` 追踪 GPU 内存变化

### 日志路径

| 文件 | 路径 | 说明 |
|------|------|------|
| 主日志（stdout only） | `/root/runs/cost-verify-agent-rl/scienceworld_grpo_cell_c_v4.log` | 220KB, 仅 stdout |
| wandb output.log | `/root/cost-verify-agent-rl/RAGEN/wandb/run-20260522_121038-u063bcz2/files/output.log` | 90KB, 534 行, 包含完整 validation 和 training 开始 |
| wandb debug-internal | `.../run-20260522_121038-u063bcz2/logs/debug-internal.log` | wandb 心跳日志 |
| Ray session | `/tmp/ray/ray/session_2026-05-22_12-09-48_615030_386369/logs/` | WorkerDict .err/.out |
| 实验配置 | `/root/cost-verify-agent-rl/RAGEN/config/_scienceworld_cell_c_grpo_v4.yaml` | |
| Hydra 输出 | `/root/cost-verify-agent-rl/RAGEN/outputs/2026-05-22/12-09-48/` | train.log 为空 |
