# TurnKV Memory

## [2026-05-13] DEFINITIVE KILL — role labels 与 token importance 无相关性

4 轮实验（v1→v2→v3a→v3b）一致 negative。v3b 最终轮消除了所有 confound（full KIRR=100%、正确 agent traces、加法偏置），TurnKV 仍劣于 Uniform EA -4.5pp。

**根因**：Pure structural 0% KIRR 是决定性反证。Role 是 coarse 标签（5 种），token importance 是 fine-grained 的。给整个段加权无法捕捉段内少数关键 token。ExpectedAttention 已经通过注意力模式捕获了 token importance，叠加 role prior 只添噪声。

**教训**：static prior（如 role labels）在 token-level eviction 中没有增量——因为 EA 本身就是 data-driven 的 importance signal，static bias 只会干扰。未来如果要改进 token eviction，应从 EA 本身的统计特性入手（如 per-segment variance/entropy），而非外部标签。

## [2026-05-13] Agent trace 必须包含完整角色结构

问题：v3 traces 只有 system/user/assistant 三种角色，缺少 ipython (TOOL_RESULT) 和 think (THINKING_TRACE)。在普通多轮对话上跑 MVP 无法支撑 "role-aware compression for agent conversations" 的 claim。

修复：v4 traces 增加了 ipython 角色（模拟工具调用返回，Llama-3.1 chat template 原生支持）和 `<think>` 标签（模拟 CoT 推理）。

规则：TurnKV 的 agent trace 必须包含至少 4 种角色结构（system, user, assistant, ipython），且至少部分 trace 包含 thinking 段。Adversarial trace 应将关键信息放在低 B_prior 段。

## [2026-05-13] Planted info 必须用模型可复述的值

8B 模型无法逐字复述随机字母数字串（API keys、passwords）。使用简单可记忆值：公司名、金额（$12,450）、短代码（order-7742）、状态码（HTTP 200）。这将 full KIRR 从 14.4% 提升到 100%。

## [2026-05-13] 乘法调制导致 KIRR 反降

**问题**：`modulated_score = ea_score × B_final` 中，B_final < 1.0 的段在全局 top-k 中被系统性压制。SYSTEM_PROMPT (B_prior=1.0) 独占 44-53% 保留预算。EASS z-scoring 进一步放大偏差（高 EA 均值段获正 z → 更高 B_final）。

**修复**：token-weighted 归一化 B_final（均值=1.0），变压制为重分配。

**教训**：对 scoring-based eviction，乘法调制不能用原始 budget 值（< 1.0 意味着在全局竞争中打折），必须归一化使总量守恒。

## [2026-05-13] PPL 评估需要两步 forward

单次 `model(full_input_ids)` 中 KV cache 压缩发生在 attention 输出后，对同一 forward pass 的 logits 无影响。必须：(1) prefix forward → 触发 KV 压缩 (2) target forward with past_key_values → 用压缩 KV 计算 loss。

## [2026-05-13] kvpress press(model) 上下文管理器不 yield model

kvpress 0.5.3 的 `with press(model) as m:` 中 m=None。正确用法：`with press(model):` 然后直接用 `model`。hook 修改 model in-place。

## [2026-05-13] 文件传输策略

SSH heredoc 传大文件 (>10KB) 极慢且不可靠。替代方案：
- 小文件 (<5KB)：heredoc 可行
- 中文件 (5-50KB)：用 python regex/sed 直接修改服务器上已有文件
- 大文件 (>50KB)：在服务器上生成（如 traces），或用 tar+base64 一次性传输
- 不要用 base64 分块传输，Worker 会卡在文件 I/O 上

## [2026-05-13] Blackwell GPU 不兼容 flash-attn

RTX PRO 6000 Blackwell (compute_120) 不支持 flash-attn。使用 flashinfer 0.6.6 替代。模型加载不要指定 `attn_implementation="flash_attention_2"`。
