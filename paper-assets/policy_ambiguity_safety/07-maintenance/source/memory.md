# Memory — policy_ambiguity_safety

## 竞品实验参考
（见 literature_map.yaml）

## 经验教训

### 5-Model Error Analysis 发现 (2026-05-21)
- **Layer mechanism 不是 clean dichotomy**：2-model 分析说 spec-layer = guess-and-act, linguistic-layer = misparse-and-apply。但 5-model 数据显示 conditional_precedence (spec-layer) 的 dominant FM 是 scope_misapplication（5/5 unanimous），与 linguistic-layer 一致。Failure mode 是 **type-specific** 而非 layer-specific。
- **Disambiguation awareness 有 model family 差异**：Claude 11.0%, GPT-4.1 10.7%（有一定 awareness），Qwen3 0%, DeepSeek 0%（完全 blind）。Overall 4.6%。
- **Claude conservative profile**：scope_misapplication dominant (50.5%), conservative_refusal highest (8.8%)，与低 violation rate (30.3%) 一致。
- **Inter-coder kappa 下降**：5-model κ=0.517 vs 2-model κ=0.594。新 3 模型的 traces 可能更难分类。

### 已验证的模型 ID (OpenRouter proxy)
- `gpt-5.4` — 直接用，无 provider prefix
- `gpt-4.1` — 直接用
- `anthropic/claude-sonnet-4-6` — 需要 provider prefix
- `qwen/qwen3-235b-a22b` — 需要 provider prefix
- `deepseek/deepseek-chat-v3-0324` — 需要 provider prefix
- Base URL: `http://47.94.22.126/v1`

### 运行脚本注意事项
- 必须用 `.venv/bin/python3` 而非系统 `python3`，因为 `core.crypto` 依赖 `cryptography` 包只在 venv 中
- 必须设置 `PYTHONUNBUFFERED=1` 否则 nohup 输出为空（Python stdout buffering）
- `core.crypto` 模块在 `/home/ubuntu/agent-ml-research/core/crypto.py`，脚本通过 `sys.path.insert(0, "/home/ubuntu/agent-ml-research")` 加载
