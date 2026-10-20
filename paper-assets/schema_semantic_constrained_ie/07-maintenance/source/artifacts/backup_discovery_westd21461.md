# Backup Discovery: westd-21461

**探测时间**: 2026-05-25
**项目根目录**: `/root/schema_semantic_constrained_ie/` (2.6G)
**无 .git / 无 venv / 无 wandb**

---

## 需要 rsync 的路径

### 1. 项目根目录 `/root/schema_semantic_constrained_ie/`

| 路径 | 大小 | 内容 |
|------|------|------|
| `checkpoints/qwen3_8b_lora_wikievents/` | 1.2G | LoRA adapter (3 版本: best + checkpoint-26 + checkpoint-39) |
| `checkpoints/llama_lora_docred/` | 1.2G | LoRA adapter (3 版本: best + checkpoint-382 + checkpoint-573) |
| `outputs/` | 140M | 实验结果 (.jsonl), violation reports, 子目录 d067_seed_variance / d068_guided_beam / prompt_sensitivity_70b |
| `data/` | 88M | 数据集 |
| `compiler/` | 444K | 约束编译器代码 |
| `logs/` | 400K | 实验日志 |
| `scripts/` | 320K | 工具脚本 |
| `paper/` | 84K | 论文相关 |
| `artifacts/` | 20K | 产出物 |
| `prompts/` | 12K | prompt 模板 |
| 根目录 `.py/.sh/.json/.md` 文件 | ~1M | 分析/运行脚本、配置文件 |

### 2. 数据盘 `/root/autodl-tmp/schema_outputs/` (145M)

实验输出文件，包含：
- 70b 模型推理结果 (scierc/docred)
- beam sweep 实验 (d062/d064/d065/d066 系列)
- seed variance 实验 (d067)
- trie baseline 结果 (r16 系列)
- 事件抽取 fine-tune 日志 (p1/p8 系列)
- `d066_beam_sweep/` — 14M
- `d066_docred_beam_sweep/` — 5.6M
- `r16_70b_lora_docred/` — 2.1M

---

## 需要 --exclude 的路径

| 路径 | 大小 | 原因 |
|------|------|------|
| `/root/autodl-tmp/models/` | 72G | 公开预训练模型 (Mistral-7B-Instruct-v0.3, Qwen3-8B-ms, LLM-Research, hugging-quants, mistralai) |
| `__pycache__/` | 132K | 编译缓存 (4 个目录) |
| `.pytest_cache/` | 16K | 测试缓存 |
| `*.bak` / `*.bak_*` 文件 | ~100K | 备份文件 (可选排除) |

---

## 大小汇总

| 分类 | 大小 |
|------|------|
| LoRA checkpoints | 2.4G |
| 实验结果 (outputs/) | 140M |
| 数据盘实验结果 (schema_outputs/) | 145M |
| 数据集 (data/) | 88M |
| 代码 + 脚本 + 配置 | ~2M |
| **需备份总量** | **~2.8G** |
| 需排除 (公开模型) | 72G |

---

## 建议的 rsync 命令

```bash
# 目标目录
DEST=~/schema_semantic_constrained_ie_archive/westd-21461

# 1. 同步项目根目录
rsync -avz --progress \
  --exclude='__pycache__/' \
  --exclude='.pytest_cache/' \
  --exclude='*.pyc' \
  westd-21461:/root/schema_semantic_constrained_ie/ \
  ${DEST}/schema_semantic_constrained_ie/

# 2. 同步数据盘实验输出
rsync -avz --progress \
  westd-21461:/root/autodl-tmp/schema_outputs/ \
  ${DEST}/autodl-tmp_schema_outputs/
```

**预计传输量**: ~2.8G（首次全量），后续增量传输。

### 可选：排除 .bak 文件

```bash
# 如果不需要 .bak 文件，追加：
  --exclude='*.bak' \
  --exclude='*.bak_*' \
```

### 可选：仅备份 LoRA adapter 最终版本（省 ~1.6G）

```bash
# 排除中间 checkpoint，只保留最终 adapter
  --exclude='checkpoints/*/checkpoint-*/' \
```
