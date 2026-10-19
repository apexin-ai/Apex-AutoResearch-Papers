# prep openpi native eval fallback

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_openpi_native_eval_fallback_20260516T152158_result.json`
- **Structured JSON:** [`3f7021b56764ecff6d4b.json`](../../sessions/3f/3f7021b56764ecff6d4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

准备工作完成。总结：

**已就绪**：
- `serve_policy_wrapper.py` — 解决了 lerobot 版本冲突，���需改动已安装的包
- `convert_lerobot_to_openpi.py` — LeRobot → openpi 格式转换器
- `pi0_libero_finetuned_openpi` — 官方 fine-tuned checkpoint 已转换为 openpi 格式
- EGL 渲染、LIBERO benchmark、openpi_client 全部验证通过

**启动方式**（GPU 空闲后）：
```bash
# Terminal 1 (Server, 1 GPU):
cd /root/openpi && CUDA_VISIBLE_DEVICES=3 python scripts/serve_policy_wrapper.py \
  --port 8000 policy:checkpoint --policy.config pi0_libero \
  --policy.dir /root/autodl-tmp/checkpoints/pi0_libero_finetuned_openpi

# Terminal 2 (Client, CPU):
cd /root/openpi && MUJOCO_GL=egl python examples/libero/main.py \
  --args.host localhost --args.port 8000 \
  --args.task-suite-name libero_spatial --args.num-trials-per-task 1
```

**注意**：当前 LIBERO 是 "LIBERO-plus" ���本（2402 tasks），即使 `num_trials=1` 也要跑较久。快速验证可以观察前几个 task 后 Ctrl-C。MetaBrain 自己的 LoRA checkpoint 需要先 merge adapter 再转换格式才能用此 pipeline。

---
