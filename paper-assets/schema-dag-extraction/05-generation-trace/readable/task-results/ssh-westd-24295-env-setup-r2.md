# ssh westd 24295 env setup r2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-24295-env-setup-r2_20260517T073227_result.json`
- **Structured JSON:** [`a56d28c27f49643cec7e.json`](../../sessions/a5/a56d28c27f49643cec7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## westd-24295 环境部署完成

### GPU 规格
| 项目 | 值 |
|------|------|
| GPU | 2× NVIDIA RTX PRO 6000 Blackwell Server Edition |
| 显存 | 97,887 MiB (≈96 GB) × 2 |
| 架构 | SM 12.0 (Blackwell) |
| 驱动 | 595.58.03 |

### 软件版本
| 组件 | 版本 |
|------|------|
| PyTorch | 2.11.0+cu130 |
| CUDA (torch) | 13.0 |
| nvcc (JIT) | 13.0, V13.0.88 |
| vLLM | 0.21.0 |
| flashinfer | 0.6.11.post3 (JIT cached for SM 120) |

### 模型
- 路径: `/root/autodl-tmp/models/llama-3.1-70b-instruct-fp8`
- 大小: 68 GB
- 加载显存: 33.87 GiB (TP=2 分布到两张卡)

### 代码同步
4 个脚本已从 cqa1-38874 同步到 westd-24295:
- `scripts/run_d051_count_curves_llama70b.py` (18.8 KB)
- `scripts/run_bcs_controlled_llama70b.py` (14.3 KB)
- `scripts/run_llama70b_cross_model.sh` (3.0 KB)
- `scripts/exp_sdgd_routing.py` (18.8 KB)

### vLLM 验证结果
**PASSED** — 模型加载并成功生成文本。首次运行 233.7s（含 flashinfer/Triton JIT 编译），后续运行使用缓存将快很多。

### 磁盘空间
| 总量 | 已用 | 可用 | 使用率 |
|------|------|------|--------|
| 350G | 68G | 283G | 20% |

### 环境配置要点
- `CUDA_HOME=/usr/local/cuda-13.0`（解决 flashinfer SM 12.0 JIT 编译需要 nvcc ≥12.9 的问题）
- `FLASHINFER_DISABLE_VERSION_CHECK=1`（所有脚本已设置）
- `enforce_eager=True`（避免 Blackwell 上 torch.compile 兼容问题）
- 额外安装了 `cuda-nvcc-13-0`、`libcublas-dev-13-0`、`libcurand-dev-13-0`、`cuda-cudart-dev-13-0` 提供 JIT 编译所需头文件

### 运行方式
```bash
export LLAMA70B_MODEL_PATH=/root/autodl-tmp/models/llama-3.1-70b-instruct-fp8
export CUDA_HOME=/usr/local/cuda-13.0
bash scripts/run_llama70b_cross_model.sh
```

---
