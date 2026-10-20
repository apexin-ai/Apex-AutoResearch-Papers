# westd-25068 模型下载与实验状态报告

**时间**: 2026-05-19 01:07 UTC

---

## 1. 磁盘空间状态

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 系统盘 `/` | 30G | 12G | 19G | 38% |
| 数据盘 `/root/autodl-tmp` | 250G | 204G | 47G | 82% |

已有模型 (`/root/autodl-tmp/models/`, 共 ~206G):
- Qwen2.5-72B-Instruct: 100G
- Qwen2.5-14B-Instruct: 28G
- Qwen3-14B: 28G
- Llama-3.1-8B-Instruct: 19G
- Mistral-7B-Instruct-v0.3: 16G
- Qwen2.5-7B-Instruct: 15G

## 2. 模型下载状态

**网络环境**: HuggingFace 官方不可达（国内 autodl 平台），使用 `HF_ENDPOINT=https://hf-mirror.com` 镜像下载。

| 模型 | 优先级 | 预估大小 | 状态 | 备注 |
|------|--------|----------|------|------|
| deepseek-ai/DeepSeek-R1-0528-Qwen3-8B | P0 | ~16GB | **下载中** | 进度正常 |
| microsoft/Phi-4-reasoning | P0 | ~28GB | **下载中** | 进度正常 |
| google/gemma-3-27b-it | P0 | ~54GB | **下载中** | 进度正常 |
| deepseek-ai/DeepSeek-R1-Distill-Llama-8B | Extra | ~16GB | **下载中** | 进度正常 |
| meta-llama/Llama-4-Scout-17B-16E-Instruct | P1 | ~109GB | **失败 (403)** | Gated model，需在 HF 页面申请 Meta 授权 |

**磁盘空间风险**: 4 个下载中的模型总计约 114GB，但仅剩 47G 可用空间。预计：
- DeepSeek-R1-0528-Qwen3-8B (~16G) 和 DeepSeek-R1-Distill-Llama-8B (~16G) 可以完成（共 ~32G）
- Phi-4-reasoning (~28G) 大概率磁盘不足
- gemma-3-27b-it (~54G) 肯定无法完成
- **需要清理旧模型或扩容数据盘才能容纳大模型**

tmux session: `model_dl_25068`

## 3. 需要 Token/授权的模型

| 模型 | 要求 |
|------|------|
| meta-llama/Llama-4-Scout-17B-16E-Instruct | 需在 huggingface.co 申请 Meta Llama 4 授权 |
| google/gemma-3-27b-it | HF token 已配置，当前下载正常（Gemma 3 已开放） |

## 4. 实验状态

### GPU 使用情况

| GPU | 显存使用 | 利用率 | 实验 |
|-----|---------|--------|------|
| cuda:0 | 0 MiB / 97887 MiB | 0% | **空闲** (exp-007 已失败) |
| cuda:1 | 88287 MiB / 97887 MiB | 97% | exp-027 运行中 |
| cuda:2 | 88287 MiB / 97887 MiB | 98% | exp-028 运行中 |
| cuda:3 | 0 MiB / 97887 MiB | 0% | **空闲** (exp-004-rerun 已失败) |

### exp-007 (Qwen2.5-72B AWQ, cuda:0) — 已失败
- **错误**: `ConnectError: [Errno 101] Network is unreachable`
- **原因**: HuggingFace 直连不可达，模型下载失败导致实验未启动
- **日志**: `/root/runs/symb_invariant_consensus/exp-007-qwen72b-awq.log` (5.6K)

### exp-004-rerun (Qwen2.5-7B, cuda:3) — 已失败
- **错误**: `FileDownloadError: 3 file(s) failed to download out of 14`
- **原因**: Modelscope 下载 Qwen2.5-7B-Instruct 时部分文件失败
- **日志**: `/root/runs/symb_invariant_consensus/exp-004-qwen7b-rerun.log` (1.9M)

### exp-027 (Qwen3-14B non-thinking, cuda:1) — 运行中
- vLLM 推理服务正常运行
- 吞吐量: prompt 313 tok/s, generation 549 tok/s
- 并发: 10 reqs, KV cache 3.1%, prefix cache hit 64.9%

### exp-028 (Qwen3-14B thinking, cuda:2) — 运行中
- vLLM 推理服务正常运行
- 吞吐量: prompt 209-258 tok/s, generation 700-725 tok/s
- 并发: 19-21 reqs, KV cache 9-12%, prefix cache hit 67.6%

### 已完成实验
- exp-029 (contrastive-folio204): 完成于 23:12
- exp-030 (crossmodel-mistral-folio204): 完成于 23:53
