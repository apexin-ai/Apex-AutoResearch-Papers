# Phase 1 GRPO 训练诊断报告

**日期**: 2026-05-14
**服务器**: westd-39279 (2× NVIDIA RTX PRO 6000 Blackwell 96GB, 1TB RAM)
**cgroup memory.max**: 240 GiB

---

## 根因分析

### r3 (EXIT_CODE=137/SIGKILL): GPU 内存争用 — 两个进程抢占同一 GPU

**直接原因**: 启动命令**未设置 `CUDA_VISIBLE_DEVICES`**，导致两个 GRPO 进程都加载到 GPU 0，GPU 显存不足被驱动级 SIGKILL。

**证据链**:

1. 启动命令无 GPU 隔离:
   ```
   # 实际启动（无 CUDA_VISIBLE_DEVICES）
   timeout 7200 env bash -c '... python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml'
   timeout 7200 env bash -c '... python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml'
   ```
   对比脚本文档推荐用法:
   ```
   CUDA_VISIBLE_DEVICES=0 python scripts/train_grpo.py ...  # GPU 0
   CUDA_VISIBLE_DEVICES=1 python scripts/train_grpo.py ...  # GPU 1
   ```

2. 两个进程日志都显示 `We will use 90% of the memory on device 0` — 均加载到物理 GPU 0

3. 两个进程**同时**在 step 25 被杀（exec-only 4:09, exec-sta 4:10），同步性表明共享资源耗尽

4. 单进程 GRPO (Qwen3-4B) 显存需求估算:
   - Policy model (bf16): ~8 GB
   - Reference model (bf16): ~8 GB
   - AdamW optimizer states (fp32): ~32 GB
   - Gradients (bf16): ~8 GB
   - KV cache + activations: ~10-15 GB
   - **单进程合计: ~66-71 GB** (可装入 96 GB GPU)
   - **两进程合计: ~132-142 GB** → **超出 96 GB GPU 显存**

5. cgroup `memory.events` 显示 `oom_kill=0` → 排除 CPU 内存 OOM，确认是 GPU 侧问题

6. 渐进式 OOM: GRPO 训练中 optimizer states 惰性分配，completion 长度从 step 5 的 151 token 增长到 step 25 的 212 token，GPU 内存逐步填满直到崩溃

### r2 (EXIT_CODE=1): wandb 认证失败

YAML 配置的 `no_wandb: true` 未被正确应用到 argparse。`wandb.init()` 被调用但无 API key。

```
wandb.errors.errors.UsageError: No API key configured. Use `wandb login` to log in.
```

### r1 (EXIT_CODE=2): 配置解析失败

`--config` 参数或 YAML 加载逻辑有 bug，必需参数 (model_path, data_path, reward_mode, output_dir) 未从 YAML 注入到 argparse。

```
train_grpo.py: error: the following arguments are required: --model_path, --data_path, --reward_mode, --output_dir
```

### 三轮失败关联

r1 → r2 → r3 是迭代修 bug 的过程，每轮修复了上一轮的问题后暴露下一层问题:
- r1: 脚本基础功能 (config parsing) 未就绪
- r2: config 修好但 wandb 开关未生效
- r3: wandb 修好但启动方式缺少 GPU 隔离 → 两进程争 GPU → OOM SIGKILL

---

## 修复建议

### 必须修复 (r3 根因)

**1. 启动命令添加 CUDA_VISIBLE_DEVICES**:
```bash
# 实验 1: exec-only → GPU 0
CUDA_VISIBLE_DEVICES=0 python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml

# 实验 2: exec-sta → GPU 1
CUDA_VISIBLE_DEVICES=1 python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml
```

### 建议优化 (降低单卡显存压力)

**2. 开启 gradient checkpointing** — GRPOConfig 添加 `gradient_checkpointing=True`，可减少 30-50% 激活内存

**3. 降 batch size 保安全余量**（如果仍紧张）:
```yaml
per_device_batch_size: 2      # 4 → 2
gradient_accumulation_steps: 4 # 2 → 4，保持等效 batch size 不变
```

**4. 脚本内增加 GPU 分配参数** — 在 YAML 配置中支持 `device` 字段，脚本内部设置 `CUDA_VISIBLE_DEVICES`，避免依赖外部启动命令:
```python
if args.device is not None:
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.device)
```

**5. 添加显存监控回调** — 训练过程中记录 `torch.cuda.max_memory_allocated()`，提前发现内存趋势

---

## 关键日志片段

### r3 最后输出 (exec-only)
```
 25%|██▌       | 25/100 [04:09<19:43, 15.79s/it]
{'loss': 0.048, 'grad_norm': 0.0, 'learning_rate': 7.6e-07, 'num_tokens': 78133.0,
 'completions/mean_length': 212.825, 'reward': 0.3, 'step_time': 13.978}
...
bash: line 1: 67229 Killed  timeout 7200 env bash -c '...'
EXIT_CODE=137
```

### r3 最后输出 (exec-sta)
```
 25%|██▌       | 25/100 [04:10<19:44, 15.80s/it]
{'loss': 0.048, 'grad_norm': 0.0, 'num_tokens': 78058.0,
 'completions/mean_length': 210.95, 'reward': 0.2625, 'step_time': 13.993}
...
bash: line 1: 67310 Killed  timeout 7200 env bash -c '...'
EXIT_CODE=137
```

### 系统状态
```
GPU: 2× NVIDIA RTX PRO 6000 Blackwell, 96 GB each, CUDA 13.2
RAM: 1.0 TiB total, cgroup limit 240 GiB
Disk: 30G root (27% used)
cgroup memory.events: oom 0, oom_kill 0 (非 CPU OOM)
```
