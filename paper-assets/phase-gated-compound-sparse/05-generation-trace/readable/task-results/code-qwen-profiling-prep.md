# code qwen profiling prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen-profiling-prep_20260514T000438_result.json`
- **Structured JSON:** [`8e9d43cd90d06eb3dc0a.json`](../../sessions/8e/8e9d43cd90d06eb3dc0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 完整跑通。输出格式与原版一致，可直接被 `analyze_v4_comparison.py` 读取。

## 总结

### 代码改动点
1. **新文件**: `/root/autodl-tmp/pacs/run_profiling_qwen.py` — 独立脚本（无需 `python -m`）
2. **与原版差异**:
   - 独立运行，`sys.path` 自动处理包导入
   - 默认 model_path 指向 Qwen2.5-7B（`/root/autodl-tmp/models/Qwen2.5-7B/Qwen/Qwen2___5-7B`）
   - 新增 `--device` 参数（CPU dry-run 用）和 `--max_problems` 参数
   - 其他所有逻辑（II 公式、masking、quantile 分段、输出格式）**完全一致**

### Qwen2.5-7B 模型
已在服务器上，4 个 safetensors shard，完整可用。

### 已知限制
- **Phase segmentation 与 reasoning 模型的区别**：原代码本身就用 quantile-based 分段（不依赖 `&lt;think>` tag），所以 Qwen2.5-7B base 模型直接适用。但 base 模型的 attention sparsity 分布可能更均匀，phase 间差异可能不如 reasoning 模型明显。
- **生成长度**：base 模型可能生成较短的 math 解答（sparsity trace 短），如果每题 token 太少会影响 phase segmentation 质量。`max_new_tokens=2048` 足够大。

### Dry-run 验证
```
CUDA_VISIBLE_DEVICES="" python run_profiling_qwen.py --device cpu --max_problems 1 --max_new_tokens 30
```
成功通过，JSON 输出格式与 DeepSeek 版本完全兼容。

### 预估运行时间
单卡 RTX 6000 Pro 96GB 跑 50 题（importance masking, 3 sparsity levels）：
- 每题：生成 ~1-2k tokens + 1 次 dense forward w/ attention + 3 levels × 3 phases × 3 sparse forward = ~30s-60s
- 总计：**约 25-50 分钟**（与 DeepSeek 版本相近，模型参数量相同）

### GPU 运行命令
```bash
# importance masking (3 levels 一次跑完)
python run_profiling_qwen.py --sparsity_levels 0.1,0.2,0.3 --output_dir ./profiling_output_qwen_imp

# random masking baseline
python run_profiling_qwen.py --masking_method random --sparsity_levels 0.1,0.2,0.3 --output_dir ./profiling_output_qwen_rand
```

---
