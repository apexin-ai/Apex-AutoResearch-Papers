# eval openpi native gpu3

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_openpi_native_gpu3_20260516T153723_result.json`
- **Structured JSON:** [`effdf772fa37ab2c490f.json`](../../sessions/ef/effdf772fa37ab2c490f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### Server 启动
✅ 正常启动，加载 checkpoint 和 norm_stats 成功

### 发现的问题（已修复）

| 问题 | 修复 |
|------|------|
| `env_wrapper.py` PosixPath 类型错误 | 加 `bddl_file_name = str(bddl_file_name)` |
| `gemma_pytorch.py` 图像 HWC→NCHW 缺失 | `embed_image` 中加 permute |
| `model.py` safetensors 加载 strict 失败 | 改为 `strict=False` |

### 核心发现：0% success 的两个原因

**1. LIBERO-Plus 环境不兼容（主因）**
- LIBERO-Plus 将 `libero_spatial` 从原版 10 tasks 替换为 **2402 个** "table_N" 增广变体
- pi0_libero 从未在这些变体上训练
- **即使官方 pi0_libero checkpoint（权重正常）也是 0%**——证明不是 checkpoint 问题而是环境不匹配

**2. Finetuned checkpoint 转换 bug（副因）**
- `pi0_libero_finetuned_openpi` 的 `lm_head.weight` std=0.003（几乎全 0）
- 官方 checkpoint `lm_head.weight` std=0.020（正常）
- 原因：JAX→PyTorch 转换时，因为 HuggingFace PaliGemma weight tying（embed_tokens = lm_head），转换脚本保存了无意义的 lm_head 值
- 导致模型无法编码 language prompt → 输出 mode collapse（对任何输入输出几乎相同动作）

### 验证：官方 checkpoint 行为

| 测试 | Finetuned (broken) | Official |
|------|-------------------|----------|
| 不同图像 action diff | 0.035（无响应） | **0.818**（有响应） |
| Trajectory 多样性 | 无（first≈last） | 有（t=0≠t=25≠t=49） |
| LIBERO-Plus eval | 0% | 0%（环境不兼容） |

### 结论
- **Checkpoint 本身**：finetuned 版有转换 bug（lm_head 归零），需要从原始 JAX checkpoint 正确重新转换
- **Eval pipeline**：即使修复 checkpoint，LIBERO-Plus 环境也不兼容。要得到有效 eval，需安装**原版 LIBERO**（而非 LIBERO-Plus）

---
