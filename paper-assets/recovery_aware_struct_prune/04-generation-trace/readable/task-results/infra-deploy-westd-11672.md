# infra deploy westd 11672

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_deploy-westd-11672_20260515T061730_result.json`
- **Structured JSON:** [`d4e338c38d867e2ab458.json`](../../sessions/d4/d4e338c38d867e2ab458.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。环境报告：

| 项目 | 值 |
|------|-----|
| **服务器** | westd-11672 |
| **Python** | 3.12.3 (conda base) |
| **PyTorch** | 2.11.0+cu128 |
| **CUDA Driver** | 580.119.02 (CUDA 13.0) |
| **GPU** | 2× NVIDIA RTX PRO 6000 Blackwell (94GB each) |
| **transformers** | 5.8.1 |
| **datasets** | 4.8.5 |
| **accelerate** | 1.13.0 |
| **trl** | 1.4.0 |
| **项目代码** | `/root/recovery_aware_struct_prune/` (49 files, git tracked) |
| **数据盘** | `/root/autodl-tmp/` (250GB, 几乎全空) |
| **根分区** | 30GB, 已用 6.5GB (22%) |
| **HF_HOME** | `/root/autodl-tmp/.hf_cache` (已配置) |
| **conda 激活** | `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` |

注意事项：
- `python3` 不在 PATH，需通过 conda 环境使用 `python`
- 无 nvcc（CUDA toolkit 未安装，但 PyTorch 自带 CUDA runtime 足够）
- 临时传输密钥已清理

---
