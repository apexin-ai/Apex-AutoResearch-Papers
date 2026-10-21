# infra env setup

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env-setup_20260514T161432_result.json`
- **Structured JSON:** [`03eec179fe7116e16416.json`](../../sessions/03/03eec179fe7116e16416.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

## 环境搭建结果

| 项目 | 详情 |
|------|------|
| **GPU** | 2x NVIDIA RTX PRO 6000 Blackwell Server Edition, 94GB 显存/卡 |
| **CUDA** | 12.8 |
| **Python** | 3.12.3 (conda base) |
| **torch** | 2.10.0+cu128 |
| **vllm** | 0.18.1 |
| **transformers** | 4.57.6 |
| **peft** | 0.19.0 |
| **datasets** | 4.8.4 |
| **accelerate** | 1.13.0 |
| **wandb** | 0.26.0 |
| **根分区** | 30G (7.5G 可用) |
| **数据盘** | 250G (201G 可用, `/root/autodl-tmp`) |
| **模型** | Qwen2.5-Coder-7B-Instruct 下载完成 (15GB) |

**关键决策：**
- 所有依赖均预装，无需安装
- 模型通过软链放在数据盘避免撑爆根分区：`/root/trace-verdict-study/models → /root/autodl-tmp/trace-verdict-study-models`
- HuggingFace 下载太慢 (~1.3 MB/s)，切换到 ModelScope CDN (~6-10 MB/s)，约 15 分钟完成

---
