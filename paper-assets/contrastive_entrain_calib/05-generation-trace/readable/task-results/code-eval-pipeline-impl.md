# code eval pipeline impl

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_pipeline_impl_20260518T111418_result.json`
- **Structured JSON:** [`b43acf51a945d14f9395.json`](../../sessions/b4/b43acf51a945d14f9395.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部实现完成，dry-run 和指标计算均验证通过。各 benchmark 实现状态和关键设计决策：

---

### 1. SYCONBench (多轮 sycophancy)
- **指标**: ToF (valid correction 后修改率), NoF (invalid pressure 下坚持率), SYCONScore (调和平均)
- **设计**: 多轮对话循环，每轮用 `classify_behavior()` 判断 revise/maintain/ambiguous。分 `valid_correction` 和 `invalid_pressure` 两类 scenario 分别计算
- **数据**: 支持 JSONL 文件输入 (`--sycon-data-path`)，dry-run 用内置 mock（3 valid + 2 invalid）
- **关键决策**: 复用 `extract_activations_v2.py` 的 heuristic 分类器而非 NLI 模型，保持评估管线轻量

### 2. SycophancyEval (单轮 sycophancy, meg-tong 数据集)
- **三个子任务**: `answer` (Answer Priming), `are_you_sure` (Follow-up Doubt), `feedback` (Ownership Bias)
- **数据源**: HuggingFace `meg-tong/sycophancy-eval` 或本地 JSONL (`--sycophancy-eval-data-dir`)
- **分类逻辑**: 按子任务差异化判断。answer/are_you_sure 用 correct answer 匹配 + behavior 分类；feedback 用 uncritical praise 模式检测
- **关键决策**: HF 数据格式中 prompt 是 `{"type": "human", "content": ...}` 格式，转换为标准 `role/content` 格式

### 3. MT-Bench (通用对话质量)
- **协议**: 两轮对话生成 → GPT-4 judge 打分 1-10
- **Judge**: 通过 OpenAI API 调用，支持 `--judge-model` 切换。从 response 中提取 `[[score]]` 格式分数
- **数据**: 优先从 FastChat 包加载完整 80 题，fallback 用内置 5 题子集
- **关键决策**: judge 不可用时返回 null scores 而非报错，允许在无 API key 环境下验证管线

### 4. MMLU (知识保留)
- **双模式**: 优先用 `lm_eval.simple_evaluate()` (标准化、可复现)；fallback 用 native logit-based 评分
- **配置**: 5-shot，支持 `--mmlu-subjects` 筛选子集，`--no-lm-eval` 强制 native 模式
- **指标**: overall accuracy + by_category (STEM/Humanities/Social Sciences/Other) + by_subject
- **关键决策**: lm-eval 模式下将 model 对象直接传给 `HFLM`，避免重复加载

### 统一设计
- 所有结果格式: `{benchmark_name, metrics, per_sample, metadata}`
- `--dry-run` 每个 benchmark 加载 mock 数据验证管线连通性
- `BenchmarkBase` 新增 `dry_run_mode` 属性，子类据此决定数据源
- 新增 CLI 参数: `--sycon-data-path`, `--sycophancy-eval-data-dir`, `--mt-bench-data-path`, `--no-lm-eval`

---
