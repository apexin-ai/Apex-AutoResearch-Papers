# infra westd 48478 readiness

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-48478-readiness_20260512T205406_result.json`
- **Structured JSON:** [`9ee23add1ab41e16002f.json`](../../sessions/9e/9ee23add1ab41e16002f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/westd_48478_readiness.md`。

## 结论：⚠️ 可以跑，需注意 2 点

**具备条件**：
- 4x RTX 5090 全空闲，cuda:2/3 显存 32G 无占用
- PyTorch 2.10+cu128、transformers/peft/accelerate 已装
- Qwen3-4B 已下载，训练脚本和数据（80k 条）就位
- RAM 617G 可用（cgroup 360G），单进程训练足够

**需要注意**：
1. **根分区仅剩 11G**（v3 死因）。训练 checkpoint 已配置写数据盘（143G free），但**必须设 `HF_HOME=/root/autodl-tmp/.hf_cache`** 防止 HF cache 撑爆根分区
2. **SSH**: `westd-48478` 认证失败，需用 `seetacloud-westd-4x5090` 作为 server name

报告中包含了完整的训练启动命令。

---
