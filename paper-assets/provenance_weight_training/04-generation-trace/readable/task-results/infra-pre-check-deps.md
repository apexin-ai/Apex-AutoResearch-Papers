# infra pre check deps

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_pre-check-deps_20260513T184651_result.json`
- **Structured JSON:** [`9d3892654ee47874f217.json`](../../sessions/9d/9d3892654ee47874f217.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ModernBERT 下载并验证成功。所有检查完成，汇总报告如下：

---

## 预检报告 — westd-47453

| # | 检查项 | 状态 | 详情 |
|---|--------|------|------|
| 1 | **Python 包依赖** | **PASS** | torch=2.10.0+cu128, transformers=4.57.6, datasets=4.8.4, accelerate=1.13.0, scikit-learn=1.8.0, tqdm=4.67.3, lm_eval=0.4.11, wandb=0.26.0, einops=0.8.2 均已安装 |
| 1a | flash-attn | **WARN** | 未安装（有 flashinfer=0.6.6），可选项，不阻塞 |
| 2 | **代码完整性** | **PASS** | 8 个文件全部存在 |
| 3a | **Qwen3-0.6B** | **PASS** | 模型文件完整（model.safetensors, tokenizer, config 等） |
| 3b | **ModernBERT-base** | **PASS** | 已下载至 HF cache，tokenizer + model 均可加载（需 `TORCHDYNAMO_DISABLE=1` + `HF_HUB_DISABLE_XET=1`） |
| 4a | **人类数据** | **PASS** | train.jsonl=164,889行, detector.jsonl=67,960行, eval_holdout.jsonl=67,823行, 共 300,672 行 |
| 4b | **合成数据** | **IN PROGRESS** | GPU 0 正在生成（PID 7156），~843K/130M tokens（0.65%），~3.3K tok/s，ETA ~10.7h，当前 2,300 行 |
| 5 | **GPU 状态** | **PASS** | 4× NVIDIA RTX PRO 6000 Blackwell（98GB）。GPU 0 占用（合成数据生成，14.7GB），GPU 1-3 空闲 |
| 6 | **accelerate 配置** | **PASS** | 已创建 default_config.yaml（MULTI_GPU, 4 卡, bf16） |
| 7 | **缺失包安装** | **N/A** | 所有关键包已就绪，无需安装 |
| 8 | **TORCHDYNAMO_DISABLE** | **WARN** | torch=2.10.0，ModernBERT 的 `torch.compile` 装饰器触发 `duplicate template name` 断言错误。**所有涉及 ModernBERT 的脚本必须设置 `TORCHDYNAMO_DISABLE=1`** |

### 需要注意的环境变量

后续 pipeline 脚本中涉及 ModernBERT 或 HF 下载时，需设置：
```bash
export TORCHDYNAMO_DISABLE=1
export HF_HUB_DISABLE_XET=1
```

### 阻塞项

**无硬性阻塞**。合成数据生成需约 10 小时完成，但 pipeline 其他步骤（pretrain 用人类数据、detector 训练等）可先行。

---
