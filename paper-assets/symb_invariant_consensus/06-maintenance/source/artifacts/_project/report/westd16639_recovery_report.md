# westd-16639 恢复报告

**日期**: 2026-05-19 01:10 UTC

## 1. 稳定性验证

| 项目 | 状态 |
|------|------|
| GPU 硬件 | 4× RTX PRO 6000 Blackwell 97GB，全部正常，温度 28-31°C |
| CUDA 计算测试 | 4 张 GPU 全部通过 matmul 测试 ✅ |
| 模型推理测试 | Qwen2.5-14B-Instruct transformers 推理通过 ✅ |
| vLLM 0.21.0 | CUDA graph capturing 阶段崩溃 ❌（Blackwell 兼容性问题） |
| 平台限制 | 无 AutoDL 状态文件、无 cgroup 限制 |
| 系统 | uptime 220 天，内存充足，SSH 连接偶有不稳定 |

**结论**: GPU 完全可用，直接 transformers/HF 推理没问题。vLLM 在 Blackwell 上 CUDA graph 有 bug，如需 vLLM 可尝试 `--enforce-eager` 跳过 CUDA graph。

## 2. 磁盘空间

| 挂载点 | 总量 | 已用 | 可用 |
|--------|------|------|------|
| / (overlay) | 30G | 13G | 18G |
| /root/autodl-tmp | 350G | 66G | 285G |
| /dev/sda2 | 879G | 333G | 502G |

**已有模型** (`/root/autodl-tmp/models/`):
- Qwen2.5-14B-Instruct: 28G
- Qwen3-14B: 28G
- Mistral-7B-Instruct-v0.3: 10G

**空间评估**: autodl-tmp 285GB 可用，足够下载全部 4 个新模型（~130GB）。

## 3. 模型下载状态

| 模型 | 状态 | 说明 |
|------|------|------|
| DeepSeek-R1-0528-Qwen3-8B | 下载中 ✅ | ~16GB，通过 hf-mirror 下载 |
| Phi-4-reasoning | 下载中 ✅ | ~30GB，公开模型，通过 hf-mirror 下载 |
| gemma-3-27b-it | 需要 HF Token ❌ | gated model，报 "Cannot access content" |
| Llama-4-Scout-17B-16E-Instruct | 需要 HF Token ❌ | gated model，报 "Cannot access content" |

**操作**: tmux session `model_dl` 中 2 个下载进程运行中。需要在 HF 上接受 gemma-3 和 Llama-4 的 license，然后 `hf auth login` 后重新下载。

**注意**: 原始 `huggingface-cli` 已废弃，当前使用 `hf` CLI (v1.15.0)。已配置 `HF_ENDPOINT=https://hf-mirror.com`。

## 4. 可恢复实验 Intermediates

| 实验 | Intermediates 文件数 |
|------|---------------------|
| exp032_qwen25_14b_pw600 | 509 |
| qwen3_14b_pw600_nonthinking | 518 |
| qwen25_14b_arc60 | 18 |
| qwen25_14b_strategyqa200 | 3 |
| folio_204_14b | 155 |

**注意**: 实际结果路径为 `/root/autodl-tmp/sica_project/symb_invariant_consensus/results/`，不是 `/root/symb_invariant_consensus/results/`。

## 待办

1. 在 HF 网站接受 gemma-3-27b-it 和 Llama-4-Scout 的 model license
2. 在 westd-16639 上执行 `hf auth login` 配置 token
3. 重新下载 gemma-3 和 Llama-4
4. 如需 vLLM，测试 `--enforce-eager` 模式绕过 CUDA graph bug
