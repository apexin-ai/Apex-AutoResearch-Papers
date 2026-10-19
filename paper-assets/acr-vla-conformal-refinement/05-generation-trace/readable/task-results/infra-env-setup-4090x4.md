# infra env setup 4090x4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env-setup-4090x4_20260513T043505_result.json`
- **Structured JSON:** [`af36dbf03d343a897cd8.json`](../../sessions/af/af36dbf03d343a897cd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证通过。最终状态报告：

---

## ACR-VLA 环境搭建报告 — `bjb1-18228`

### 1. 基础环境

| 项目 | 值 |
|------|-----|
| Python | 3.12.3 (conda base, `/root/miniconda3`) |
| CUDA | 12.8 |
| PyTorch | 2.10.0+cu128 |
| `torch.cuda.is_available()` | True |

### 2. GPU 可见性

| GPU | 型号 | 显存 |
|-----|------|------|
| GPU 0 | NVIDIA GeForce RTX 4090 | 23GB |
| GPU 1 | NVIDIA GeForce RTX 4090 | 23GB |
| GPU 2 | NVIDIA GeForce RTX 4090 | 23GB |
| GPU 3 | NVIDIA GeForce RTX 4090 | 23GB |

### 3. 项目代码

所有 11 个源文件已写入 `/root/acr-vla-conformal-refinement/`：

| 文件 | 行数 | 大小 | 状态 |
|------|------|------|------|
| `src/__init__.py` | — | 133B | OK |
| `src/cgs.py` | — | 4080B | OK |
| `src/aci.py` | — | 3628B | OK |
| `src/crm.py` | — | 1959B | OK |
| `src/utils.py` | 186 | 6661B | OK |
| `src/smolvla_wrapper.py` | 177 | 6585B | OK |
| `src/train_crm.py` | 361 | 13624B | OK |
| `src/evaluate.py` | — | 10108B | OK |
| `scripts/verify_pipeline.py` | 324 | 11762B | OK |
| `mvp/run_mvp.py` | — | 5846B | OK |
| `tests/test_aci_sign.py` | 46 | 2284B | OK |

### 4. 组件验证

- **CGS** (ConformilizedGaussianScoring): K=10, horizon=5, action_dim=6 — 实例化成功
- **CRM** (ConformalRefinementModule): 337,438 参数, forward pass (2,30)→(2,30) — 通过
- **ACI** (AdaptiveConformalInference): 符号修正测试 3/3 通过（cover→alpha↑, miss→alpha↓, 稳定性）
- `ACTION_DIM=6, H_EFF=5, OBS_DIM=960, CHUNK_SIZE=50` — 常量正确

### 5. 依赖

transformers, accelerate, datasets, mujoco, gymnasium, robomimic, h5py, sklearn, einops, wandb, tmux — 全部已安装。

### 6. 磁盘

- 根分区: ~24GB 可用 (30GB 总)
- 数据盘 (`/root/autodl-tmp/`): ~250GB 可用

### 7. 遗留问题

无。环境就绪，可开始训练。

---
