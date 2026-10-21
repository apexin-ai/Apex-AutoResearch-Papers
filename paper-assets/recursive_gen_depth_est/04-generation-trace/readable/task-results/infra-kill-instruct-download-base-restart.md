# infra kill instruct download base restart

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill-instruct-download-base-restart_20260514T110510_result.json`
- **Structured JSON:** [`c4e29c7a408be1980c36.json`](../../sessions/c4/c4e29c7a408be1980c36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**depth-1 域一致性结果**（95 条已生成，还在继续）：
- **自然语言: 82.1%** (78/95)
- **代码: 17.9%** (17/95)
- **垃圾: 0%**

对比 Instruct 版本（几乎 100% 代码/HTML），base 模型大幅改善。17.9% 的代码内容可能来自 depth_0 种子数据本身含有的代码样本。

---

## 产出报告

### 1. Instruct pipeline 杀掉确认
- tmux session `mvp_pipeline_004` 已杀（kill_job 成功）
- GPU 利用率 0%，显存 0 MiB（确认释放）
- 旧数据 depth_1/2/3.jsonl + checkpoints/lora_depth_0 已删除

### 2. Base 模型下载
- 路径: `/root/autodl-tmp/models/Qwen2.5-1.5B/`
- 大小: 2.9GB model.safetensors + config/tokenizer 全套
- 方案: ModelScope CDN wget（3 分 16 秒，平均 15 MB/s）
- 验证: 模型加载成功 1543.7M params，生成自然语言（AI 历史文本），code_ratio=0.000

### 3. Pipeline 启动
- 实验 ID: `mvp_pipeline_base_003`（tmux session 同名）
- GPU0 100% 利用率，训练 3 epoch 完成
- Loss: 2.163 → 2.061（稳定下降）
- LoRA adapter 保存: `checkpoints/lora_depth_0/adapter_model.safetensors` (4.2MB)

### 4. depth-1 域一致性
- **82.1% 自然语言**，17.9% 代码
- 比 Instruct 版本（~100% 代码/HTML）大幅改善
- 代码污染可能来自种子数据，后续可通过数据过滤优化

### 5. 错误
- `transformers` 4.37.2 与 `accelerate` 1.13.0 不兼容（`dispatch_batches` 参数），已升级 transformers 到 5.8.1 修复
- Pipeline 正常运行中，后续 depth 2/3 会自动生成

---
