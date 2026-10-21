# 诊断报告：mvp-p1-gpu1-v2 失败

**日期**：2026-05-13
**服务器**：westb-13313
**运行时长**：~115 秒
**退出码**：1

## 根因

**GPU 0 显存被其他进程占满，vLLM 无法启动。** GPU 0 上有残留 python 进程（PID 20301）占用 15816 MiB，仅剩 3.51 GiB 空闲，而 vLLM 要求 26.65 GiB（85% × 31.36 GiB）。

## 关键日志

```
(EngineCore pid=283218) ValueError: Free memory on device cuda:0 (3.51/31.36 GiB) on startup
is less than desired GPU memory utilization (0.85, 26.65 GiB).
Decrease GPU memory utilization or reduce GPU memory used by other processes.
```

```
RuntimeError: Engine core initialization failed. See root cause above.
```

## 当前 GPU 状态（故障时刻后）

| GPU | 进程 | 显存占用 |
|-----|------|----------|
| 0 | python (PID 20301) | 15816 MiB / 32607 MiB |
| 1 | VLLM::EngineCore (PID 163319) | 28004 MiB / 32607 MiB |

两块 GPU 都被先前实验（mvp-p1-gpu1 / mvp-p1-gpu1-vllm 被 kill 后）的残留进程占据。`kill` 命令可能只杀了主进程，vLLM 的 EngineCore 子进程和 GPU 0 上的 python 进程未被清理。

## 部分产出

`results/mvp/chemistry-mix-paint-secondary-color/episodes.jsonl`（29 KB）存在，可能来自先前运行或崩溃前的短暂输出。

## 修复建议

**无需修改代码，清理 GPU 后重跑即可。**

1. 杀掉两个残留进程：
   ```bash
   kill -9 20301 163319
   ```
2. 确认 GPU 释放：
   ```bash
   nvidia-smi
   ```
3. 清理可能的残留输出（避免与新结果混淆）：
   ```bash
   rm -rf /root/autodl-tmp/simgate-modular-routing/results/mvp/chemistry-mix-paint-secondary-color/
   ```
4. 重跑实验（命令不变）：
   ```bash
   python src/phase1_signal.py --task_types 'chemistry-mix-paint-secondary-color,grow-plant' \
     --episodes 20 --gpu_id 0 --max_steps 30 --output_dir results/mvp/ \
     --model_path /root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct/ --use_vllm
   ```

## 防复发建议

在训练脚本或提交脚本中加入启动前 GPU 检查：
```python
# 启动前检查目标 GPU 是否有足够显存
free_mem = torch.cuda.mem_get_info(gpu_id)[0] / 1024**3
if free_mem < 20:  # GiB
    raise RuntimeError(f"GPU {gpu_id} only has {free_mem:.1f} GiB free, need ≥20 GiB")
```
