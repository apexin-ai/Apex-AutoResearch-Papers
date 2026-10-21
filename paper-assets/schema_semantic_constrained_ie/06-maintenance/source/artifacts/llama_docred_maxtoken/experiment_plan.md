# Llama DocRED max_tokens 截断测试实验计划

## 背景

llama_docred_full_s1 的 parse failures 从 unconstrained 的 68 增至 91（+33.8%）。假设原因是约束解码增加了 token 开销，导致更多文档在 max_tokens=4096 处被截断、JSON 不完整。增大 max_tokens 50% 后如果 parse failures 显著下降，则 E-F1 下降 (-0.64pp) 可能是 truncation artifact。

## 当前参数

| 参数 | 值 |
|------|-----|
| max_new_tokens | **4096** |
| 脚本 | `run_constrained_extraction.py` (line 614: `--max_new_tokens`) |
| 模型 | `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct` |
| 数据 | `data/docred/dev.json` (998 docs) |

## 新参数

| 参数 | 原值 | 新值 | 倍率 |
|------|------|------|------|
| max_new_tokens | 4096 | **6144** | 1.5x |

## 实验命令

### 组 A：unconstrained + max_tokens 6144

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144"
```

### 组 B：full_s1 + max_tokens 6144

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144"
```

> **与原实验唯一差异**：`--max_new_tokens 4096 → 6144`，`--output_path` 带 `_mt6144` 后缀避免覆盖原结果。

## 服务器状态（2026-05-15 验证）

| 项目 | 状态 |
|------|------|
| 服务器 | westd-16980 |
| GPU | 2x NVIDIA RTX PRO 6000 Blackwell (98GB)，**均空闲** |
| 磁盘 | 22GB 可用（充足） |
| 模型文件 | ✓ 存在 |
| 数据文件 | ✓ dev.json + ontology_constraints_docred.json 存在 |
| 脚本 | ✓ run_constrained_extraction.py 存在，`--max_new_tokens` 为标准 CLI 参数 |
| 原结果 | ✓ llama_docred_unconstrained.jsonl + llama_docred_full_s1.jsonl 存在，不会被覆盖 |

## 运行时间预估

| 实验 | 原耗时 | 预估新耗时 | 说明 |
|------|--------|-----------|------|
| 组 A (unconstrained) | 5.4h | **5.5–6.5h** | 仅截断文档（~68/998）会多生成 tokens |
| 组 B (full_s1) | 5.74h | **6.0–7.0h** | 截断文档更多（~91/998），约束解码逐 token 开销不变 |

两组可并行跑在 cuda:0 和 cuda:1 上，总墙钟约 **6–7 小时**。

## 并行执行建议

两组实验无依赖关系，可分别分配到 cuda:0 和 cuda:1 同时执行：
- 组 A → `--device cuda:0`
- 组 B → `--device cuda:1`

## 验证标准

| 指标 | 原 unconstrained | 原 full_s1 | 预期（截断假设成立时） |
|------|-----------------|-----------|----------------------|
| parse_failures | 68/998 | 91/998 | full_s1 降至 ≤68（接近或低于 unconstrained 原值） |
| E-F1 | 55.65% | 55.01% | full_s1 与 unconstrained 差距缩小至 <0.3pp |

### 判定逻辑

- **截断假设成立**：full_s1 parse failures 从 91 降至 ≤70，且 E-F1 差距缩小 → parse failure 增加确实是 truncation artifact，E-F1 下降非约束解码本身问题
- **截断假设部分成立**：parse failures 下降但 E-F1 差距不变 → truncation 只影响解析成功率，不影响 F1
- **截断假设不成立**：parse failures 基本不变 → 原因不在 max_tokens，需另查（如约束解码产生畸形 JSON 的其他路径）

## 注意事项

1. 输出文件使用 `_mt6144` 后缀，不会覆盖原实验结果
2. 分析阶段需用同版本 `violation_checker.py`（checker_version: `fixed_20260514_v2`）
3. 建议同时记录每个文档的实际生成 token 数，以确认哪些文档确实触及了 4096 上限（如脚本不支持，可后续对比原输出和新输出的 parse failure 文档 ID 差异）
