# 环境搭建报告 — cost-verify-agent-rl

**日期**: 2026-05-14
**服务器**: bjb1-17606 (AutoDL)

## 硬件

| 项目 | 详情 |
|------|------|
| GPU | 2x NVIDIA RTX PRO 6000 Blackwell Server Edition (94GB each) |
| CUDA Driver | 590.44.01 |
| CUDA Toolkit | 12.8 (nvcc V12.8.93) |
| 根分区 | 30G (23G 可用, 25% used) |
| 数据盘 | 250G (224G 可用, 11% used) |

## 软件环境

| 组件 | 版本 | 状态 |
|------|------|------|
| Python | 3.12.3 (conda base) | OK |
| PyTorch | 2.10.0+cu128 | OK, CUDA available |
| verl | 0.6.1 (commit d62da495) | OK |
| RAGEN | 0.1 (commit 20daedc) | OK |
| vLLM | 0.18.1 | OK |
| transformers | 4.57.6 | OK |
| ray | 2.55.1 | OK |
| alfworld | installed | OK |
| accelerate | 1.13.0 | OK |
| flashinfer | 0.6.6 | OK |
| wandb | 0.26.0 | OK |

## 模型

| 模型 | 路径 | 大小 |
|------|------|------|
| Qwen3-1.7B | `/root/cost-verify-agent-rl/models/Qwen3-1.7B` -> `/root/autodl-tmp/models/Qwen/Qwen3-1.7B` | 3.8G |

模型文件完整：2 个 safetensors shard + tokenizer (vocab_size=151643)

## 项目结构

```
/root/cost-verify-agent-rl/
├── models/
│   └── Qwen3-1.7B -> /root/autodl-tmp/models/Qwen/Qwen3-1.7B
└── RAGEN/                    (178M)
    ├── verl/                 (v0.6.1, commit d62da495)
    ├── data/                 (6.2M, 9 datasets downloaded)
    ├── external/
    │   ├── webshop-minimal/
    │   └── kimina-lean-server/
    └── ragen/
```

## 环境激活命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
```

## 遇到的问题和解决方案

1. **verl submodule checkout 失败**: git submodule 的 verl 指向的 commit 无法自动 checkout。解决：手动 git clone verl 仓库后 git checkout d62da495。
2. **版本冲突警告**: RAGEN setup.py 固定 vllm==0.8.2 和 faiss-cpu==1.11.0，但服务器已装 vllm 0.18.1 和 faiss-cpu 1.13.2。通过 pip install -e . --no-deps 绕过版本约束。
3. **SSH 命令超时**: 大文件克隆和包安装超过 30s SSH 超时，统一用 nohup 后台执行 + 轮询。
4. **ModelScope 下载**: AutoDL 代理下 HuggingFace 慢，改用 ModelScope CDN 下载 Qwen3-1.7B。

## 注意事项

- vllm 版本差异大（0.18.1 vs RAGEN 期望的 0.8.2），后续训练可能需要适配 API 变更
- 模型存放在数据盘 /root/autodl-tmp/，通过软链接映射到项目目录
- 连接服务器需先 source /etc/network_turbo 启用代理加速
