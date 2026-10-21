# d067: Seed Variance 推理脚本准备报告

## 脚本路径

两台服务器（westd-16980, westd-21461）均已部署：

| 文件 | 路径 |
|------|------|
| 单次推理脚本 | `/root/schema_semantic_constrained_ie/scripts/d067_seed_variance.sh` |
| 批量运行脚本 | `/root/schema_semantic_constrained_ie/scripts/d067_run_all.sh` |

### 用法

```bash
# 单次运行
bash scripts/d067_seed_variance.sh <GPU_ID> <CONFIG> <SEED>
# 例: bash scripts/d067_seed_variance.sh 0 qwen_scierc 123

# 全量运行（2 GPU 并行）
bash scripts/d067_run_all.sh
```

## Checkpoint 路径

三个 checkpoint 在两台服务器上均已确认存在：

| Config | Checkpoint |
|--------|-----------|
| qwen_scierc | `/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged` |
| llama_scierc | `/root/autodl-tmp/checkpoints/llama_lora_scierc_merged` |
| qwen_docred | `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged` |

## 数据路径

| Dataset | Data | Constraints | Samples | max_new_tokens |
|---------|------|-------------|---------|----------------|
| SciERC | `data/processed_data/test.json` | `ontology_constraints.json` | 551 | 2048 |
| DocRED | `data/docred/dev.json` | `data/docred/ontology_constraints_docred.json` | 998 | 4096 |

## Seed 实现方式

`run_constrained_extraction.py` 第 793 行：`--seed` 参数（default=42）
第 826 行：`torch.manual_seed(args.seed)`

greedy decoding（temperature=0.0）下 seed 仅影响初始化，输出应完全确定性。已有 `run_stability_test.sh`（zero-shot Qwen3-8B SciERC × 3 seeds）验证了这一点——三个 seed 输出 MD5 一致。

**LoRA fine-tuned 模型可能不同**——如果存在 dropout 或其他随机组件，seed 可能产生差异。这正是本实验要验证的。

## 每个配置预估运行时间

基于现有日志（每 SciERC sample ~2s unconstrained / ~3s constrained; 每 DocRED sample ~4-5s）：

| Config | Unconstrained | Constrained (S1) | 每 seed 合计 | 2 seeds 合计 |
|--------|--------------|-------------------|-------------|-------------|
| qwen_scierc | ~18 min | ~27 min | ~45 min | ~1.5 h |
| llama_scierc | ~18 min | ~27 min | ~45 min | ~1.5 h |
| qwen_docred | ~70 min | ~100 min | ~170 min | ~5.5 h |

## 运行计划（d067_run_all.sh）

2 GPU 并行，每台服务器只需跑一轮：

| GPU | Task 1 | Task 2 | Task 3 | 预估总时长 |
|-----|--------|--------|--------|-----------|
| GPU 0 | qwen_scierc seed=123 | qwen_scierc seed=456 | qwen_docred seed=123 | ~4.5 h |
| GPU 1 | llama_scierc seed=123 | llama_scierc seed=456 | qwen_docred seed=456 | ~4.5 h |

## 输出文件

```
outputs/d067_seed_variance/
├── qwen_scierc_seed123_unconstrained.jsonl
├── qwen_scierc_seed123_unconstrained_violations.json
├── qwen_scierc_seed123_full_s1.jsonl
├── qwen_scierc_seed123_full_s1_violations.json
├── qwen_scierc_seed456_unconstrained.jsonl
├── qwen_scierc_seed456_unconstrained_violations.json
├── qwen_scierc_seed456_full_s1.jsonl
├── qwen_scierc_seed456_full_s1_violations.json
├── llama_scierc_seed123_*.jsonl / *.json
├── llama_scierc_seed456_*.jsonl / *.json
├── qwen_docred_seed123_*.jsonl / *.json
└── qwen_docred_seed456_*.jsonl / *.json
```

## 验证状态

- [x] 两台服务器脚本语法检查通过（`bash -n`）
- [x] 错误参数处理正确（unknown config → exit 1）
- [x] 所有 checkpoint 路径已确认存在
- [x] 所有数据路径已确认存在
- [x] `run_constrained_extraction.py --help` 确认 `--seed` 参数可用
- [ ] 实际推理（等 GPU 释放后启动）
