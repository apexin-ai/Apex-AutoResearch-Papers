# research gen resource assessment

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_gen-resource-assessment_20260517T080740_result.json`
- **Structured JSON:** [`02f3fe36ecc5701e6ade.json`](../../sessions/02/02f3fe36ecc5701e6ade.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。

## 硬件确认

| 项目 | 详情 |
|------|------|
| GPU | 4× NVIDIA RTX PRO 6000 Blackwell (96GB VRAM each), 全部空闲 |
| 磁盘 | `/root` 30GB (26GB free), **`/root/autodl-tmp` 350GB (空)** |
| RAM/SHM | 220GB |
| 网络 | hf-mirror.com 可达, DeepSeek API 可达 |
| Python 环境 | `/root/miniconda3/bin/python3.12`, PyTorch 2.8.0+cu128, transformers 5.8.1, accelerate 1.13.0 |
| 缺失 | vllm 未安装; Llama 系列需 gated token |

## 模型大小 (实测)

| 模型 | 磁盘大小 | VRAM (FP16) | 可下载 |
|------|---------|-------------|--------|
| Qwen3-30B-A3B (MoE) | ~64GB | ~60GB (fits 1×96GB) | Yes |
| DeepSeek-R1-Distill-Qwen-14B | ~35GB | ~30GB | Yes |
| Qwen2.5-7B-Instruct | ~16GB | ~15GB | Yes |
| Llama-3.1-8B-Instruct | ~16GB | ~15GB | **No** (gated, 需 token) |

## 推荐方案

### 首选: 方案 A — 全本地

- **Attacker**: Qwen3-30B-A3B on GPU 0
  - MoE 架构: 30B total / 3B active per token, 推理速度接近 3B dense 模型
  - ~60GB VRAM, 单卡 96GB 轻松放下
  - Qwen3 系列 reasoning 能力强, 适合规划 persuasion strategy
- **Target**: Qwen2.5-7B-Instruct on GPU 1
  - 16GB VRAM, 有 safety guardrails, instruction following 好
  - 作为被攻击目标合适
- 模型缓存: `HF_HOME=/root/autodl-tmp/hf_cache` (350GB 空间充足)
- 下载: 80GB total @ ~200MB/s ≈ **7 min**
- 需安装 vllm 加速推理
- **预估时间**: 250 conversations × 10 turns
  - With vllm: attacker ~2s/turn + target ~0.5s/turn → ~2,500 × 2.5s ≈ **1.7 hours**
  - Without vllm (plain transformers): attacker ~8s + target ~3s → **7-8 hours**
  - 可用 GPU 2-3 跑第二组并行, 时间再减半

### 备选: 方案 C — 混合 (API attacker + 本地 target)

- **Attacker**: DeepSeek API (deepseek-reasoner, R1 模型)
- **Target**: Qwen2.5-7B-Instruct (本地 GPU 0)
- 预估成本: 5,000 turns × ~700 tokens/turn ≈ 3.5M tokens → **<$2**
- 速度取决于 API 并发限制, 可能 2-4 hours
- 风险: API 限流, 网络不稳

### 不推荐: 方案 B (全 API)

Target 模型用 API 不合适: Crescendo 需要有 safety guardrails 的模型, 商业 API 的 safety filter 可能导致对话直接被截断。本地模型可以观察 raw logits 和完整输出。

## 需要的资源/审批

1. **安装 vllm** — 推理加速核心依赖, 约 5 min pip install
2. **磁盘**: 使用 `/root/autodl-tmp` 存模型 (350GB 充足, 无需额外申请)
3. **DeepSeek API key** — 仅方案 C 需要; 方案 A 不需要
4. **无需额外 GPU** — 4 卡足够同时跑 attacker + target + 预留 2 卡并行

---
