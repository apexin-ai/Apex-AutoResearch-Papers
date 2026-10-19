# ops bjb1 starcoder flash check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-starcoder-flash-check_20260513T043717_result.json`
- **Structured JSON:** [`3704c98899f6b0615d4b.json`](../../sessions/37/3704c98899f6b0615d4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 任务 1: StarCoder2-3B 下载 — **完成**

模型位于 `/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b/`，包含：
- `model.safetensors` (11.3GB，单文件)
- `config.json`, `tokenizer.json`, `tokenizer_config.json`, `vocab.json`, `special_tokens_map.json`

文件完整，无下载进程在运行。

**注意**：项目代码的 models 目录 (`/root/autodl-tmp/structfuse/models/`) 里只有 Qwen2.5-Coder-3B 的软链接，StarCoder2 在 `/root/autodl-tmp/models/bigcode/` 下，未链接到 structfuse 项目目录。如需使用需创建软链接或修改配置路径。

### 任务 2: flash-attn 编译 — **失败**

编译报错，ninja 构建失败：
```
ninja: build stopped: subcommand failed.
ERROR: Could not build wheels for flash-attn
```
`-j 85` 并行度过高可能是原因之一（内存不足导致编译器崩溃）。flash-attn 未安装成功，site-packages 中不存在该包。无编译进程在运行。

### 任务 3: GPU 状态 — **正常**

| GPU | 型号 | 显存 | 温度 | 利用率 |
|-----|------|------|------|--------|
| 0 | NVIDIA RTX PRO 6000 Blackwell | 97,887 MiB | 27°C | 0% (空闲) |
| 1 | NVIDIA RTX PRO 6000 Blackwell | 97,887 MiB | 26°C | 0% (空闲) |

CUDA 13.1，两张卡均空闲，无 GPU 进程。

---
