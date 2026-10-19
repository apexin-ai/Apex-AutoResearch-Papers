# OpenPI Native LIBERO Eval - Preparation Report

**Date**: 2026-05-16  
**Server**: westd-34142  
**Status**: READY (pending GPU availability)

## 结论

1. **openpi ���生 eval 可以直接用 safetensors checkpoint** — 检测��� `model.safetensors` 自动走 PyTorch 路径
2. **需要 key format 转换**：LeRobot 格式有 `model.` 前缀，openpi 格式没有。���写好转换脚本。
3. **lerobot 版本冲突**：当前装的是 0.5.1（无 `lerobot.common`），openpi 需要旧版。已��� wrapper 绕过。
4. **所有准备完成**，一旦 GPU 空闲可��即启动。

## Copy-Paste 启动命令

### Server��1 GPU）:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/openpi
CUDA_VISIBLE_DEVICES=3 python scripts/serve_policy_wrapper.py \
  --port 8000 policy:checkpoint \
  --policy.config pi0_libero \
  --policy.dir /root/autodl-tmp/checkpoints/pi0_libero_finetuned_openpi
```

### Client（另一个 terminal，CPU + EGL）:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/openpi
MUJOCO_GL=egl python examples/libero/main.py \
  --args.host localhost \
  --args.port 8000 \
  --args.task-suite-name libero_spatial \
  --args.num-trials-per-task 1
```

## Checkpoint 对���

| 路径 | 来源 | 格式 | 用途 |
|------|------|------|------|
| `pi0_libero_finetuned_openpi` | lerobot/pi0_libero_finetuned 转换 | openpi (777 keys, no prefix) | **������试**: 官方 fine-tuned, �� >0% |
| `pi0_libero_openpi` | lerobot/pi0_libero_base 转换 | openpi (777 keys, no prefix) | pipeline 验证, 预期 ~0% |

所有 checkpoint 位于 `/root/autodl-tmp/checkpoints/`

## 已创建的文件

| 文件 | 作用 |
|------|------|
| `/root/openpi/scripts/serve_policy_wrapper.py` | 带 lerobot shim 的 server 启动脚本 |
| `/root/openpi/scripts/convert_lerobot_to_openpi.py` | LeRobot → openpi 格式转换器 |
| `/root/openpi/scripts/run_libero_eval.sh` | 一键启动脚本 (server/client) |
| `/root/autodl-tmp/checkpoints/pi0_libero_finetuned_openpi/` | 转换好的 fine-tuned checkpoint |

## Blockers & 注意事项

1. **LIBERO 版本**: 装的是 LIBERO-plus (2402 tasks/suite)，不是标准 LIBERO (10 tasks)。`num_trials_per_task=1` 仍需 2402 episodes。快速验证建议手动 Ctrl-C 看前几个 task 的结果。

2. **不要改 lerobot 版本**: 如果 `pip install lerobot@旧commit` 会破坏 MetaBrain 训练。wrapper 脚本已解决此问题。

3. **MetaBrain LoRA 评估**: MetaBrain 训练产���的是 LoRA adapter (`adapter_model.safetensors`)，不是 full model。要用 openpi eval 需要先 merge adapter → full model → 转换格式。这是后续步骤。

## 验证通过的���节

- [x] EGL 渲染 (NVIDIA EGL)
- [x] LIBERO benchmark 初始化
- [x] openpi_client 包
- [x] PI0Pytorch 模型导入
- [x] Norm stats 加载
- [x] Checkpoint 格式兼容性 (777 keys match)
- [x] tyro CLI 参数解析
- [x] serve_policy_wrapper.py shim
