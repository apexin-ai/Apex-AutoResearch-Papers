# infra env setup westd

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env-setup-westd_20260515T112129_result.json`
- **Structured JSON:** [`f1fb676ef2777bd4a188.json`](../../sessions/f1/f1fb676ef2777bd4a188.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 0 环境搭建汇报

### 服务器状态
| 项目 | 状态 |
|------|------|
| Python | 3.12.3 (conda base) |
| CUDA | 12.8 (driver 580.119.02) |
| PyTorch | 2.8.0+cu128 |
| GPU | 4× NVIDIA RTX PRO 6000 Blackwell 94GB |

### 依赖安装
| 包 | 版本 | 状态 |
|------|------|------|
| OpenPI (--no-deps + 手动补依赖) | 0.1.0 | PI0Pytorch 导入 OK |
| LIBERO-Plus (替代 LIBERO) | 0.1.0 | `import libero` OK |
| safetensors | 0.7.0 | OK |
| einops | 0.8.2 | OK |
| scikit-learn | 1.8.0 | OK |
| umap-learn | 0.5.12 | OK |
| transformers | 5.8.1 | OK |
| accelerate | 1.13.0 | OK |
| flax + jax | 0.12.7 / 0.10.0 | OK (openpi 依赖) |
| matplotlib | 3.10.5 | OK |

### Phase 0 代码
4 个文件已部署到 `/root/meta_brain_lora_routing/phase0/`，语法检查全部通过：
- configs.py, collect_activations.py, train_classifier.py, eval_classifier.py

### 进行中
- **π₀ checkpoint 下载**：wget 后台运行中（PID=3207），13GB 模型文件，当前 ~252MB，预计 2-3 小时完成。路径：`/root/autodl-tmp/checkpoints/pi0_base/model.safetensors`
- **标准 LIBERO clone**（可选，PID=4447）：网络不稳定多次失败，LIBERO-Plus 已替代

### 已知限制
- `collect_activations.py` 引用 `openpi.models_pytorch.model_config.get_model_config`，但该模块在当前 openpi 版本中不存在，实际运行时需适配
- openpi 版本约束（torch==2.7.1, transformers==4.53.2）与实际安装版本不完全匹配，但导入测试通过

### 查看下载进度
```bash
ls -lh /root/autodl-tmp/checkpoints/pi0_base/model.safetensors
ps -p 3207 -o pid,etime
```

---
