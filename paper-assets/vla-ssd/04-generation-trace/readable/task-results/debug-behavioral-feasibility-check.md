# debug behavioral feasibility check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_behavioral_feasibility_check_20260518T092651_result.json`
- **Structured JSON:** [`b9d2c08e0b46ac2e4907.json`](../../sessions/b9/b9d2c08e0b46ac2e4907.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有检查完成。

```
=== Behavioral Feasibility Check ===

Check 1 (LIBERO headless): FAIL
  Detail:
  - LIBERO benchmark 定义加载: OK（libero_goal 10 tasks, 如 "open the middle drawer of the cabinet"）
  - 环境创建/渲染: FAIL
  - 根因: EGL 库加载失败 — PyOpenGL 找不到可用的 EGL platform
    `AttributeError: 'NoneType' object has no attribute 'eglQueryString'`
  - 完整调用链: robosuite import → mujoco.rendering → mujoco.egl → OpenGL.EGL → FAIL
  - 服务器有 libEGL_nvidia.so 但缺少 libEGL_mesa0; libOSMesa 未安装
  - OSMesa 同样失败（`'NoneType' object has no attribute 'glGetError'`）
  - mujoco 3.8.1 + PyOpenGL 组合在此镜像上无法完成 headless GL context 初始化

Check 2 (OpenVLA inference): PASS
  Detail:
  - 模型路径: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b
  - 模型类型: OpenVLAForActionPrediction
  - 模型加载耗时: 7.7s
  - generate() 耗时: 4.77s (max_new_tokens=256)
  - 输出 shape: [1, 262]
  - Peak GPU 显存: 15.2 GB
  - GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition × 2

Check 3 (L1 patch + inference): PASS
  Detail:
  - Patch 方式: 全局替换 llama_mod.eager_attention_forward（非 register_hook）
  - Attention 实现: eager（config 指定），与 patch 兼容
  - Patch 后 generate() 耗时: 4.87s（与未 patch 基本一致）
  - 输出 shape: [1, 262]，正常
  - KV cache 兼容: OK（autoregressive generation 完整跑通 256 tokens）
  - Peak GPU 显存: 15.2 GB

Overall: BLOCKED by Check 1 (LIBERO headless rendering)
```

**修复 Check 1 的方向**（仅供参考，未执行）：
- `apt install libegl-mesa0 libegl-dev` 或 `apt install libosmesa6-dev` 安装缺失的 GL 库
- 或降级 mujoco 到 2.x 版本（渲染后端不同）
- 或设置 `PYOPENGL_PLATFORM=egl` + 确保 nvidia EGL ICD 可被 PyOpenGL 发现

---
