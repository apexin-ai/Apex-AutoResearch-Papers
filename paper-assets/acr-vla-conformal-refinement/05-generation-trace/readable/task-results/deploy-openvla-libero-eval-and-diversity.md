# deploy openvla libero eval and diversity

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_openvla-libero-eval-and-diversity_20260519T163931_result.json`
- **Structured JSON:** [`82e9ca358ba227aaa931.json`](../../sessions/82/82e9ca358ba227aaa931.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有任务完成。总结：

## 完成状态

**1. 模型下载** ✓
- OpenVLA-7B fine-tuned (libero-object) 已下载到 `/root/autodl-tmp/models/openvla-libero-object/`（4 个 safetensors 分片，约 14.5GB）

**2. 环境依赖** ✓
- base conda env (Python 3.12, torch 2.10+cu128)
- transformers 4.40.1 (从 5.8.0 降级，并 patch 了版本检查)
- timm 0.9.10, tensorflow 2.21.0
- 无 flash_attn（编译填满磁盘被中止，使用 sdpa 回退）
- config/preprocessor/tokenizer 中的 `auto_map` 已移除（offline 兼容）
- prismatic 训练模块 `__init__.py` 已精简（避免 dlimp/tfds 等训练依赖）

**3. Baseline eval** ✓ RUNNING
- `eval-openvla-object-baseline-seed42` 已通过 submit_training_job 提交
- GPU4 (RTX 4090), 22.4GB VRAM 占用
- 10 tasks × 50 trials = 500 episodes，首个 episode 已成功（Success: True）
- 预计总时长 ~5-6h（6h timeout）
- Registry 状态: RUNNING

**4. K-sample diversity 脚本** ✓
- `/root/autodl-tmp/openvla-repo/test_diversity.py` 已写入
- 测试 T = [0.0, 0.3, 0.5, 0.7, 1.0]，K=10 samples，3 个 tasks
- 通过 `do_sample=True, temperature=T` 调用 `predict_action`，计算 per-DOF std
- 可在 eval 跑完后用同一 GPU 运行，或用另一个空闲 GPU 并行

**注意事项**
- GPU0 和 GPU5 空闲，可用于并行跑 diversity 测试
- 根分区清理后有 18GB 可用（flash_attn 编译临时文件已删除）

---
