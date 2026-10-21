# Backup Discovery: westd-16980

**Date**: 2026-05-25  
**Server**: westd-16980

## 1. 需要 rsync 的路径

| 路径 | 大小 | 说明 |
|------|------|------|
| `/root/schema_semantic_constrained_ie/` | 596M | 项目根目录（代码 + outputs + data） |
| `/root/autodl-tmp/schema_outputs/` | 98M | 数据盘上的实验输出 |
| **合计** | **~694M** | |

### 子目录明细

| 子目录 | 大小 | 内容 |
|--------|------|------|
| `outputs/` | 469M | 实验结果（.jsonl、violation reports、eval reports 等，~250+ 文件） |
| `data/` | 122M | 数据集（ace05, docred, wikievents, rams, sft, synthetic, processed_data） |
| `paper/` | 968K | 论文 LaTeX 源码 |
| `scripts/` | 552K | 运行脚本 |
| `artifacts/` | 540K | 分析产出 |
| `figures/` | 476K | 论文图表 |
| `logs/` | 468K | 实验日志 |
| `compiler/` | 444K | 约束编译器代码 |
| `prompts/` | 12K | 提示模板 |
| `checkpoints/` | 0 | 空目录（llama_8b_lora_wikievents 子目录为空） |
| 根目录 .py/.sh/.json/.md | ~3M | 分析脚本、配置文件 |

### autodl-tmp/schema_outputs/ 内容

实验输出（70b results、beam sweep、unified eval 等），包含子目录 `d066_beam_sweep/`, `r15_verification/`, `r16_70b_lora_docred/`, `r16_70b_lora_scierc/`, `unified_eval/`。

## 2. 需要 --exclude 的路径

| 排除项 | 原因 |
|--------|------|
| `__pycache__/` | Python 缓存（5 个目录） |
| `.pytest_cache/` | pytest 缓存（16K） |
| `*.pyc` | 编译字节码 |
| `/root/autodl-tmp/models/` | 公开预训练模型，103G，不需要备份 |

### 不存在（无需排除）

- `.git/` — 不存在（非 git 仓库）
- `.venv/` / `venv/` — 不存在
- `wandb/` — 不存在
- LoRA adapters — 未找到 adapter_config.json

### autodl-tmp/models/ 明细（排除）

```
LLM-Research/
Llama-8B-DocRED-FT-AWQ-INT4/
Llama-8B-SciERC-FT-AWQ-INT4/
Mistral-7B-Instruct-v0.3-ms/
Mistral-7B-Instruct-v0.3/
Qwen3-8B-DocRED-FT-AWQ-INT4/
Qwen3-8B-SciERC-FT-AWQ-INT4/
Qwen3-8B-link/
Qwen3-8B-ms/
```

注意：`*-FT-AWQ-INT4` 是自己微调后量化的模型。如需保留这些权重，需单独备份（预估 ~4-8G/模型）。

## 3. 建议的 rsync 命令

```bash
# 目标目录
DEST=~/schema_semantic_constrained_ie_archive/westd-16980

# (1) 主项目目录
rsync -avz --progress \
  --exclude='__pycache__/' \
  --exclude='.pytest_cache/' \
  --exclude='*.pyc' \
  westd-16980:/root/schema_semantic_constrained_ie/ \
  "$DEST/schema_semantic_constrained_ie/"

# (2) 数据盘实验输出
rsync -avz --progress \
  westd-16980:/root/autodl-tmp/schema_outputs/ \
  "$DEST/autodl-tmp_schema_outputs/"

# (3) 可选：备份自训练的 FT-AWQ 模型
# rsync -avz --progress \
#   westd-16980:/root/autodl-tmp/models/Llama-8B-DocRED-FT-AWQ-INT4/ \
#   "$DEST/models/Llama-8B-DocRED-FT-AWQ-INT4/"
# rsync -avz --progress \
#   westd-16980:/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/ \
#   "$DEST/models/Llama-8B-SciERC-FT-AWQ-INT4/"
# rsync -avz --progress \
#   westd-16980:/root/autodl-tmp/models/Qwen3-8B-DocRED-FT-AWQ-INT4/ \
#   "$DEST/models/Qwen3-8B-DocRED-FT-AWQ-INT4/"
# rsync -avz --progress \
#   westd-16980:/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ \
#   "$DEST/models/Qwen3-8B-SciERC-FT-AWQ-INT4/"
```

**预计传输量**：~694M（不含 FT 模型），含 FT 模型约 +16-32G。
