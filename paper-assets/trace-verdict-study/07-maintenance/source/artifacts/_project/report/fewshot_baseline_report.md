# Few-shot Prompting Baseline Report (plan_020)

## Status: Scripts Ready, Awaiting API Keys

服务器 westd-11235 上**未配置** `OPENAI_API_KEY` 和 `ANTHROPIC_API_KEY`，无法执行 GPT-4o / Claude API 评估。

### 已部署的脚本

| 文件 | 说明 |
|------|------|
| `/root/trace-verdict-study/eval/fewshot_api_eval.py` | API 版 few-shot 评估脚本（支持 OpenAI / Anthropic） |
| `/root/trace-verdict-study/eval/run_fewshot_api.sh` | 一键运行 4 组实验的 shell 脚本 |

### 需要的 API Keys

在服务器上设置环境变量后即可运行：

```bash
export OPENAI_API_KEY="[REDACTED]"
export ANTHROPIC_API_KEY="[REDACTED]"
bash /root/trace-verdict-study/eval/run_fewshot_api.sh
```

### 计划评估矩阵

| Model | 0-shot | 3-shot |
|-------|--------|--------|
| GPT-4o | 待执行 | 待执行 |
| Claude Sonnet 4 | 待执行 | 待执行 |

### Prompt 模板

**System Prompt:**
```
You are a software testing expert. Given code and its test cases along with execution trace information, determine whether the code passes all tests.

Rules:
- If the execution trace shows "[No exception data in trace]" or "[No trace available]", it means the trace does not contain exception information. You must still judge based on the code and tests.
- If the execution trace shows error/exception information, the code likely fails.
- Answer with exactly one word: pass or fail.
```

**0-shot**: 直接给 test input + "Answer with exactly one word: pass or fail."

**3-shot**: 附带 3 个训练集示例（indices=[1851, 875, 30]，labels=[pass, fail, fail]），与已有本地模型 few-shot 实验使用相同示例。

### 已有基线结果（用于对比）

| Method | Model | Accuracy | 95% CI | Pass F1 | Fail F1 |
|--------|-------|----------|--------|---------|---------|
| SFT (exception_only) | Qwen-7B | **99.83%** | [99.58, 100.0] | 0.999 | 0.997 |
| Regex baseline | - | 93.61% | - | - | - |
| 3-shot (local) | Qwen-7B | 90.84% | [89.08, 92.44] | 0.937 | 0.834 |
| 0-shot (logit) | DeepSeek-6.7B | 90.59% | [88.99, 92.18] | 0.931 | 0.851 |
| 0-shot (logit) | Qwen-1.5B | 93.45%* | [92.02, 94.79] | 0.969 | 0.873 |
| 0-shot (gen) | Qwen-7B | 0.00%** | - | - | - |

\* Qwen-1.5B 使用 lenient yes/no mapping（原始输出为 "yes, the..." / "no, this..." 格式）
\** Qwen-7B zero-shot 生成模式下所有 1190 个样本输出均无法解析为 pass/fail

### 测试集信息

- 数据路径: `/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl`
- 样本数: 1190 (851 pass / 339 fail)
- 训练集: 4720 samples (3107 pass / 1613 fail)
- 多数类基线: 71.51% (全部预测 pass)

### 数据格式示例

每条样本包含：代码 + 测试用例 + 执行 trace（exception_only 条件下为异常信息或 "[No exception data in trace]"），输出为 "pass" 或 "fail"。

### 预期分析

GPT-4o 和 Claude 作为强推理模型，预期在 0-shot 条件下即能达到 90%+ accuracy（因为 exception trace 提供了强信号）。关键对比点：
1. 闭源大模型 vs 开源小模型 SFT 的差距（预期 SFT 99.83% 仍然领先）
2. 3-shot 相比 0-shot 的增益
3. 大模型在 "[No exception data in trace]"（需要代码推理）样本上的表现

### 下一步

1. 获取 OPENAI_API_KEY 和 ANTHROPIC_API_KEY
2. 在服务器上运行 `run_fewshot_api.sh`
3. 用结果更新此报告
