# ops prep vllm eval westd

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep-vllm-eval-westd_20260518T215515_result.json`
- **Structured JSON:** [`f4b2300232896bbd6bcd.json`](../../sessions/f4/f4b2300232896bbd6bcd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

### 环境状态
| 组件 | 版本 | 状态 |
|------|------|------|
| torch | 2.8.0+cu128 | 系统已有 |
| peft | 0.19.1 | 系统已有 |
| transformers | 5.8.1 | 系统已有 |
| lm_eval | 0.4.12 | 已安装到 `/root/vllm_eval_env/` |
| vllm | - | **未安装**（需 torch 2.11，与系统 torch 2.8 不兼容）|

### vllm 问题
vllm 0.21.0 强制要求 torch 2.11.0 + 大量 CUDA 库（nvidia-cudnn-cu13 366MB 等），且 Aliyun 镜像下载缓慢。在训练进行中不宜升级系统 torch。

### 替代方案
脚本自动检测后端：vllm 可用时用 vllm（merge+推理），否则回退到 **HF 后端 + peft 直接加载 LoRA**（无需 merge，torch SDPA 加速）。当训练结束后可升级 torch 并安装 vllm。

### 已部署文件（`/root/contamcal-irt-calibration/exp001/`）

| 文件 | 用途 |
|------|------|
| `run_vllm_eval_batch1.sh` | cuda:2, 5 adapters: d000_s42/s123, d005_s42/s123, d025_s42 |
| `run_vllm_eval_batch2.sh` | cuda:0, 5 adapters: d025_s123, d050_s42/s123, d100_s42/s123 |
| `merge_adapter.py` | LoRA merge 工具（vllm 模式使用） |
| `convert_lm_eval_to_irt.py` | lm_eval 输出 → IRT 格式转换 |

### 运行方式
GPU 释放后：
```bash
# 确认 GPU 空闲 (C001/C002)
nvidia-smi

# Batch 1: cuda:2
nohup bash /root/contamcal-irt-calibration/exp001/run_vllm_eval_batch1.sh > /root/autodl-tmp/exp001/eval_vllm/batch1.log 2>&1 &

# Batch 2: cuda:0
nohup bash /root/contamcal-irt-calibration/exp001/run_vllm_eval_batch2.sh > /root/autodl-tmp/exp001/eval_vllm/batch2.log 2>&1 &
```

### 预估运行时间
HF 后端 + 7B model + Blackwell 98GB GPU：~30-45 min/adapter，每 batch ~2.5-3.5h。如后续升级到 vllm，预计 ~15-20 min/adapter。

---
