# validate libero integration

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validate_libero-integration_20260515T114808_result.json`
- **Structured JSON:** [`f68ce4da23c50554cb0e.json`](../../sessions/f6/f68ce4da23c50554cb0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总结果：

---

## 产出报告

### 1. PERTURBATION_SUFFIXES 匹配报告

旧的简单后缀匹配已替换为 **正则解析**（`_classify_task()`），100% 覆盖所有 4 个 LIBERO-Plus 套件：

| 扰动类型 | libero_spatial | libero_object | libero_goal | libero_10 |
|---|---|---|---|---|
| **nominal** (base) | 390 | 354 | 410 | 383 |
| **camera_viewpoints** | 376 | 396 | 408 | 419 |
| **robot_initial_states** | 350 | 398 | 409 | 393 |
| **sensor_noise** | 351 | 422 | 379 | 449 |
| **light_conditions** | 292 | 297 | 279 | 274 |
| **background_textures** | 258 | 248 | 281 | 289 |
| **objects_layout** | 385 | 403 | 425 | 312 |
| **TOTAL** | **2402/2402** | **2518/2518** | **2591/2591** | **2519/2519** |

命名格式解析：
- 复合后缀：`{base}_view_{H}_{V}_{S}_{R}_{E}_initstate_{I}[_noise_{N}]` → 通过参数值判断类型
- 简单后缀：`_light_\d+`, `_table_\d+`/`_tb_\d+`, `_add_\d+`/`_level\d+` → 末尾正则匹配

### 2. sensor_noise 实现确认

**LIBERO-Plus 内置**，非自实现。已删除 `_apply_sensor_noise()`。

环境层应用（`env_wrapper.py` L288-342），5 种噪声 × 10 级 severity = 50 级别：
| noise 值 | 类型 | 参数 |
|---|---|---|
| 1-10 | motion_blur | radius/sigma 递增 |
| 11-20 | gaussian_blur | sigma 1-10 |
| 21-30 | zoom_blur | zoom range 递增 |
| 31-40 | fog | plasma fractal |
| 41-50 | glass_blur | sigma/delta/iter |

通过任务名后缀 `_noise_N` 选择，env.step() 自动对 agentview 和 wrist 图像施加噪声。

### 3. 模型加载修复

原始报错 `openpi.models_pytorch.model_config.get_model_config` 不存在 — 因为该 API 根本不存在。正确 API：
```python
from openpi.training.config import get_config         # config_name="pi0_libero"
from openpi.policies.policy_config import create_trained_policy
```

已修复：
- `load_pi0_for_collection()` 使用正确的 API 路径（本就正确）
- 添加 `_ensure_openpi_imports()` stub 掉 lerobot（训练依赖，推理不需要）
- 安装缺失依赖：augmax, chex, tqdm-loggable, openpi-client, lerobot 等
- 升级 orbax-checkpoint 到 0.11.39（兼容 jax 0.10.0）
- OpenPI config 获取验证通过：`get_config("pi0_libero")` → OK

### 4. 代码部署状态

| 文件 | 远程路径 | 语法 | 导入 |
|---|---|---|---|
| libero_integration.py | `/root/meta_brain_lora_routing/phase0/` | ✓ | ✓ |
| collect_activations.py | `/root/meta_brain_lora_routing/phase0/` | ✓ | ✓ |

关键变更：
- 删除 `PERTURBATION_SUFFIXES` → 替换为 `_classify_task()` 正则解析
- 删除 `_apply_sensor_noise()` → env 内置
- `obs_to_model_input()` 移除 `sensor_noise`/`rng` 参数
- 默认 task_suite 从 `libero_90` 改为 `libero_spatial`（libero_90 无扰动变体）
- `collect_activations.py` 新增 `--task_suite` 参数

---
