# diag exp012 crash

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp012_crash_20260515T141936_result.json`
- **Structured JSON:** [`1749c10a099ac50c0eb2.json`](../../sessions/17/1749c10a099ac50c0eb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 根因

**系统 CUDA toolkit 版本过低**：`/usr/local/cuda` 是 CUDA 12.8，而 flashinfer JIT 编译 Blackwell (SM 12.0) FP8 GEMM 内核需要 **CUDA >= 12.9**。

调用链：
1. vLLM 加载 FP8 模型 → flashinfer `bmm_fp8` → `gen_gemm_sm120_module()` JIT 编译
2. flashinfer `get_cuda_version()` 找到 `/usr/local/cuda/bin/nvcc` 返回 **12.8**
3. `is_cuda_version_at_least("12.9")` 返回 `False` → SM 12.0 架构未注册
4. `get_nvcc_flags_list([12])` 找不到目标架构 → `RuntimeError`

关键版本：
| 组件 | 版本 | 需要 |
|------|------|------|
| GPU | RTX PRO 6000 Blackwell (SM 12.0) | — |
| Driver | 13.1 | OK |
| torch.version.cuda | 13.0 | OK |
| **nvcc (`/usr/local/cuda`)** | **12.8** | **>= 12.9** |
| flashinfer | 0.6.8.post1 | — |

## 修复方案

需要把 flashinfer 用到的 nvcc 升级到 >= 12.9。`CUDA_HOME` 环境变量可以覆盖 flashinfer 的 CUDA 路径查找。

**方案 A（推荐）：pip 安装 CUDA 13 nvcc + 设置 CUDA_HOME**

```bash
source /etc/network_turbo
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# 安装 CUDA 13 nvcc 和编译依赖
pip install nvidia-cuda-nvcc-cu13 nvidia-cuda-cccl-cu13

# 获取安装路径
NVCC_HOME=$(python3 -c "import nvidia.cuda_nvcc; import os; print(os.path.dirname(os.path.dirname(nvidia.cuda_nvcc.__file__)))")
echo "NVCC_HOME=$NVCC_HOME"
$NVCC_HOME/bin/nvcc --version  # 确认 >= 12.9
```

然后在 `run_exp012_llama.sh` 中加上：
```bash
export CUDA_HOME=$(python3 -c "import nvidia.cuda_nvcc; import os; print(os.path.dirname(os.path.dirname(nvidia.cuda_nvcc.__file__)))")
```

**方案 B（备选）：安装系统级 CUDA 13 toolkit**

```bash
source /etc/network_turbo
apt-get update && apt-get install -y cuda-toolkit-13-0
export CUDA_HOME=/usr/local/cuda-13.0
```

**同时建议升级 flashinfer** 到 0.6.11.post2 以获得更好的 Blackwell 支持：
```bash
pip install flashinfer-python==0.6.11.post2
```

---

是否要我直接在服务器上执行方案 A 修复？

---
