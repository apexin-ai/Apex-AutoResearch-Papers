# debug westd38929 mujoco egl

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_westd38929-mujoco-egl_20260520T092712_result.json`
- **Structured JSON:** [`35448f554b33975f464c.json`](../../sessions/35/35448f554b33975f464c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 4 个 eval 都在正常运行，没有崩溃。**

## 诊断结论

**westd-38929 上没有 MuJoCo/EGL 崩溃问题。** 当前状态：

| GPU | 任务 | 进度 | 状态 |
|-----|------|------|------|
| 0 | `eval_xvla_pruning_libero.py --keep_ratio 1.0` | ~29/50 ep (Task 0) | 正常，全 SUCCESS |
| 1 | `eval_xvla_pruning_libero.py --keep_ratio 0.95` | ~29/50 ep (Task 0) | 正常，全 SUCCESS |
| 2 | `eval_xvla_pruning_libero.py --keep_ratio 0.9` | ~15/50 ep (Task 0) | 正常，全 SUCCESS |
| 3 | `eval_xvla_pruning_libero.py --keep_ratio 0.7` | ~49/50 ep (Task 0) | 运行中（部分 FAIL，max_steps=800） |

**关于之前的 segfault：** log 文件 `eval_openvla_sc_m128_vtconly_20k_seed42.log`（17:00 启动）只有 17 行，在 Task 0 开始后就断了——这个进程确实崩溃了。但那个用的是 `eval_openvla_smart_compress.py`（OpenVLA 7B 模型），不是当前运行的 `eval_xvla_pruning_libero.py`。之后的 xvla 评估（17:16 启动）已经正常跑起来了。

可能的解释：
1. 之前的 OpenVLA eval 崩溃是因为 OpenVLA 7B 模型加载后 GPU 内存不足（虽然 96GB 应该够），或者是代码 bug
2. 当前的 xvla pruning eval 用了不同的代码路径，不存在这个问题
3. MuJoCo/EGL 本身没有问题——我的测试全部通过（单环境、50 并发环境都正常）

如果需要排查 OpenVLA eval 的崩溃，需要重新运行 `eval_openvla_smart_compress.py` 并捕获 core dump 或 faulthandler 输出。

---
