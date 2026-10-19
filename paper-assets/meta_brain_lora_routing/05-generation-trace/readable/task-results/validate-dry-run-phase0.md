# validate dry run phase0

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validate_dry-run-phase0_20260515T121842_result.json`
- **Structured JSON:** [`f05ed6de72d7bf89f39e.json`](../../sessions/f0/f05ed6de72d7bf89f39e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Phase 0 Dry-run 全部 3 个阶段通过。**

### 结果汇总

| 阶段 | 状态 | 耗时 |
|------|------|------|
| Phase 1: 模型加载 | **PASS** | ~46s (PI0Pytorch on cuda:0) |
| Phase 2: Hook 注册 | **PASS** | <1s (12/12 hooks) |
| Phase 3: Episode rollout | **PASS** | ~37s (220 steps) |

### Activation shapes（全部正确）

**PaliGemma 层 (×8):** layers 2,4,6,8,10,12,14,16
- mean/first/last: `(1, 2048)` — 符合 `PALIGEMMA_HIDDEN_DIM=2048`
- first_last: `(1, 4096)` — concat 正确

**Expert 层 (×4):** layers 2,6,10,14
- mean/first/last: `(1, 1024)` — 符合 `EXPERT_HIDDEN_DIM=1024`
- first_last: `(1, 2048)` — concat 正确

### Episode 详情
- Task: `pick up the black bowl next to the plate and place it on the plate view 0 0 189 0 0 initstate 0`
- Perturbation: camera_viewpoints (FOV=189, 非默认 100)
- Steps: 220, Success: False（单次 rollout 不成功属正常）
- LIBERO-Plus suite: 2402 tasks, 376 matched camera_viewpoints

### 注意事项
- `DeprecationWarning: swigvarlink` — MuJoCo/SWIG 的无害警告
- `Gym unmaintained` — libero 依赖旧版 gym，不影响功能
- `No OpenGL_accelerate` — 纯渲染性能提示，EGL 模式正常工作

管线验证完成，可以启动正式数据收集。

---
