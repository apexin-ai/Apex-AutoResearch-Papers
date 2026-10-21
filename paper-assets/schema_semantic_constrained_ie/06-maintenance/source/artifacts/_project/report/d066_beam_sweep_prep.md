# d066: Beam Width Sweep 推理脚本准备报告

**日期**: 2026-05-19
**状态**: 脚本已部署，等待 d064 GPU 释放

## 脚本路径

| 服务器 | 脚本 | 位置 |
|--------|------|------|
| westd-21461 | SciERC beam sweep | `/root/schema_semantic_constrained_ie/scripts/d066_beam_sweep_scierc.sh` |
| westd-16980 | DocRED beam sweep | `/root/schema_semantic_constrained_ie/scripts/d066_beam_sweep_docred.sh` |
| 两台 | 分析脚本 | `scripts/d066_analyze_beam_sweep.py` |

## Checkpoint 路径

| 模型 | 数据集 | westd-21461 | westd-16980 |
|------|--------|-------------|-------------|
| Qwen3-8B LoRA | SciERC | `/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged` | 同 |
| Qwen3-8B LoRA | DocRED | `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged` | 同 |
| Llama-3.1-8B LoRA | SciERC | `/root/autodl-tmp/checkpoints/llama_lora_scierc_merged` | 同 |
| Llama-3.1-8B LoRA | DocRED | `/root/autodl-tmp/checkpoints/llama_lora_docred_merged` | 同 |

## 实验配置

- **Beam widths**: k=1, 2, 4, 8（全部用 `--decoding_strategy beam --num_beams k`）
- **Modes**: unconstrained + full_s1 (constrained)
- **Datasets**: SciERC test (100 docs) + DocRED dev (998 docs)
- **Models**: Qwen3-8B LoRA + Llama-3.1-8B LoRA
- **Total configs**: 2 models × 2 datasets × 4 beams × 2 modes = 32 runs

## GPU 分配

| 服务器 | GPU0 | GPU1 |
|--------|------|------|
| westd-21461 | Llama SciERC (8 runs) | Qwen SciERC (8 runs) |
| westd-16980 | Llama DocRED (8 runs) | Qwen DocRED (8 runs) |

## 预估运行时间

基于 d064 实测数据（DocRED: Llama greedy ~14s/doc, Qwen beam-4 ~21.5s/doc）：

### SciERC (100 docs, westd-21461)

| Config | 预估单次 | 每 GPU 8 runs 合计 |
|--------|---------|-------------------|
| beam-1 | ~2-3 min | |
| beam-2 | ~3-4 min | |
| beam-4 | ~5-7 min | |
| beam-8 | ~8-12 min | |
| **合计** | | **~40-60 min** |

### DocRED (998 docs, westd-16980)

| Config | 预估单次 | 每 GPU 8 runs 合计 |
|--------|---------|-------------------|
| beam-1 unc/con | ~230 min × 2 | |
| beam-2 unc/con | ~280 min × 2 | |
| beam-4 unc/con | ~350 min × 2 | |
| beam-8 unc/con | ~500 min × 2 | |
| **合计** | | **~45 hours** |

**SciERC 1 小时内完成，DocRED 需要 ~2 天。**

## 输出路径

```
/root/autodl-tmp/schema_outputs/d066_beam_sweep/
├── {model}_{dataset}_beam{k}_{mode}.jsonl      # 推理输出
├── violations/
│   └── {model}_{dataset}_beam{k}_{mode}_violations.json  # violation reports
├── d066_scierc_gpu0.log / gpu1.log              # 运行日志
├── d066_docred_gpu0.log / gpu1.log
└── d066_summary.json                            # 分析汇总
```

## Latency 记录方式

推理脚本 `run_constrained_extraction.py` 已内置 per-sample 计时，每条 JSONL 记录包含：
- `inference_time_seconds`: 单样本推理耗时
- `decoding_strategy`: "beam"
- `num_beams`: 实际 beam width

分析脚本 `d066_analyze_beam_sweep.py` 汇总 mean/median/P90 latency + violation rates + F1。

## Violation Rate 计算

使用现有 checker：
- SciERC: `violation_checker.py` → ET%, RV%, DR%, CF% + Entity/Relation F1
- DocRED: `violation_checker_docred.py` → ET%, RV%, DR%, CF%

已集成到 beam sweep 脚本中，推理完成后自动运行。

## Dry-run 验证结果

| 检查项 | westd-21461 | westd-16980 |
|--------|-------------|-------------|
| 数据文件 | ✅ | ✅ |
| Constraints 文件 | ✅ | ✅ |
| Checkpoint 目录 | ✅ | ✅ |
| Compiler imports | ✅ | ✅ |
| 输出目录可写 | ✅ | ✅ |
| 分析脚本 | ✅ | ✅ |

## 启动命令

GPU 释放后执行：

```bash
# westd-21461 (SciERC, ~1h)
nohup bash scripts/d066_beam_sweep_scierc.sh > /root/autodl-tmp/schema_outputs/d066_beam_sweep/d066_scierc_main.log 2>&1 &

# westd-16980 (DocRED, ~45h)
nohup bash scripts/d066_beam_sweep_docred.sh > /root/autodl-tmp/schema_outputs/d066_beam_sweep/d066_docred_main.log 2>&1 &
```

## 注意事项

1. **beam=1 vs greedy**: 本实验统一用 beam search code path（`--decoding_strategy beam --num_beams 1`），与 greedy 有微小差异（beam search 开销），但保证公平对比
2. **Resume 支持**: 脚本检查输出文件行数，已完成的配置会跳过
3. **DocRED 耗时长**: 建议优先跑完 SciERC，DocRED 可以在后台持续运行
4. **d064 部分结果可复用**: d064 已有 Llama/Qwen DocRED beam-4 和 greedy 的数据，但输出路径不同，分析时可交叉验证
