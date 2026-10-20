# M2/M4 代码就绪度报告

> 检查时间: 2026-05-13 | 服务器: westd-22162 | 路径: /root/autodl-tmp/pacs/

## 代码结构

```
/root/autodl-tmp/pacs/
├── __init__.py                          (空)
├── profiling/
│   ├── __init__.py                      (空)
│   ├── phase_segmentation.py            (~350行, Phase/PhaseAnnotation/PhaseSegmenter)
│   ├── interaction_index.py             (~400行, InteractionIndexCalculator/bootstrap CI)
│   └── run_profiling.py                 (~450行, MVP pipeline: load→segment→II→pass/fail)
├── utils/
│   ├── __init__.py                      (空)
│   ├── data_utils.py                    (~30行, MATH-500 stratified sampling)
│   └── metrics.py                       (~80行, compute_perplexity/ppl_from_cached_losses)
├── checkpoints/
│   └── DeepSeek-R1-Distill-Qwen-7B -> symlink
├── data/
│   └── math500.json                     (458KB)
├── profiling_output/
│   └── profiling_results.json           (MVP 结果, 全 NaN — KV sparse 未工作)
├── logs/                                (空)
└── output/                              (空)
```

**总计**: 7 个 Python 文件, ~1310 行代码, 全部属于 M1 profiling。

## M2: Per-phase Grid Search

- **就绪度: 5%**
- **已有**:
  - `InteractionIndexCalculator.compute_interaction_index()` 可计算单个 (sparsity_level, phase) 的 II
  - `compute_per_phase_ii()` 支持按 phase 批量计算
  - Phase segmentation 完整 (KDE + tri-modal)
  - Head masking hook (`_HeadMaskHook`) 可工作
  - MATH-500 数据和模型 checkpoint 已就位
- **缺失**:
  - **grid_search.py**: 参数空间定义 (5 levels × 3 axes × 3 phases = 375 candidates)
  - **多轴联合评估**: 当前只有 attn 单轴 + 粗粒度 KV 二值 mask；缺少 KV retention ratio 参数化和 MLP top-k 参数化
  - **KV eviction 实现有 bug**: MVP 结果中所有 KV sparse ppl = NaN，说明 `kv_mask` 路径未正常工作
  - **MLP sparsity 模块**: 完全缺失（无 MLP neuron selection/masking 代码）
  - **结果收集 + Pareto 分析脚本**
  - **多 GPU 并行调度**（4 GPU → ~8h 需要分布式调度）

## M4: Kernel Integration

- **就绪度: 0%**
- **已有**: 无
- **缺失**:
  - **Polar Sparsity Triton 内核适配**: 需从 github.com/susavlsh10/Polar-Sparsity 移植 Selective Head Attention kernel，适配 Qwen 架构
  - **R-KV KV eviction 集成**: 需从 github.com/Zefan-Cai/R-KV 集成 attention-score-based KV eviction
  - **SeerAttention-R TileLang 集成** (仅 Qwen3-8B 验证模型): 需从 github.com/microsoft/SeerAttention 集成 block-sparse decoding kernel
  - **MLP top-k PyTorch kernel wrapper**
  - **Kernel 兼容性**: 服务器 GPU 为 H20-NVLink (sm_90 Hopper)，需确认 Triton/TileLang kernel 对 sm_90 的兼容性
  - **Throughput benchmarking 框架** (trace sharing for throughput, fresh generation for accuracy)
  - **Kernel 正确性验证** (vs dense baseline 数值对比)

## M3: Controller Training

- **就绪度: 0%**
- **已有**: 无
- **缺失**:
  - **Controller 网络定义**: per-layer single-FC router，输入 (attn output norms, MLP activation stats, phase embedding) → 输出 {head_mask, mlp_sparsity_ratio, kv_retention_budget}
  - **Gumbel-Softmax 可微分分配**
  - **Knowledge distillation 训练循环**: 用 M2 grid search 得到的 phase-optimal triplets 作为 teacher labels
  - **Calibration trace 生成** (~2K traces)
  - **训练脚本 + checkpoint 管理**

## 关键 TODO/FIXME

代码中无 TODO/FIXME/HACK 标记。

## 关键问题

1. **无 requirements.txt / pyproject.toml** — 依赖关系未锁定
2. **MVP KV sparse 路径全 NaN** — `profiling_results.json` 显示所有 phase 所有 level 的 `kv` 和 `both` ppl 均为 NaN，II 全部 NaN，pass_fail=FAIL。KV masking 实现有 bug，这是 M2 grid search 的前置阻塞项
3. **MLP 轴完全缺失** — 三轴联合搜索中 MLP 维度零代码

## 建议优先级

| 优先级 | 任务 | 预估工作量 | 阻塞关系 |
|--------|------|-----------|----------|
| **P0** | 修复 KV sparse NaN bug | 2-4h | 阻塞 M1 通过, M2, M4 |
| **P1** | 写 requirements.txt | 0.5h | 环境可复现性 |
| **P2** | MLP sparsity 模块 (top-k activation masking) | 4-6h | M2 三轴搜索 |
| **P3** | Grid search 框架 (参数空间 + 多GPU调度) | 8-12h | M2 核心 |
| **P4** | Polar Sparsity kernel 移植 + Qwen 适配 | 12-20h | M4 核心 |
| **P5** | R-KV 集成 | 6-10h | M4 KV 轴 |
| **P6** | Controller 网络 + 训练循环 | 8-12h | M3 核心 |
| **P7** | SeerAttention-R 集成 (Qwen3-8B only) | 8-12h | M4 验证模型 |

**总结**: 仓库目前只有 M1 profiling 代码，且 MVP 结果中 KV 轴有 bug 导致全 NaN。M2/M3/M4 代码均需从零编写。在 12 天 deadline 内，P0 (KV bug 修复) 是最紧急的阻塞项——修复前 M1 无法 pass，所有后续 milestone 无法启动。
