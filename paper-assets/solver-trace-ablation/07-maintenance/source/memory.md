# Memory — solver-trace-ablation

## Phase 0 结果与发现

### 正交性检查结论（phase0_score_v3, 2026-05-13）
- **Overall: PASS** — 所有 Pearson |r| < 0.35，LC vs Confidence |r| = 0.303 < 0.5
- **关键发现：Quality vs Confidence Spearman ρ = -0.998**（近乎完美负单调关系）
  - 原因：Quality = base model PPL = exp(-avg_log_prob)，Confidence = finetuned model avg_log_prob，两者本质上是同一信号的非线性变换
  - Pearson r = -0.287（低）因为关系是非线性的（指数），但 Spearman（基于 rank）捕捉到完美单调性
  - **对 PGPF 的影响**：Quality 和 Confidence 提供冗余信息，多属性过滤中同时用两者无增益。Phase 1 应考虑：(a) 只保留其中一个，或 (b) 将冗余性作为论文 finding 讨论
- LC、SN 与其他属性相关性低（|r| < 0.34），确认它们提供独立信息维度

### 模型缓存路径（AutoDL）
- Qwen 通过 ModelScope 下载，缓存在 `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B`（ModelScope 格式，非 HF Hub 格式）
- `HF_HUB_OFFLINE=1` + `from_pretrained("Qwen/Qwen2.5-1.5B")` 会失败——必须用绝对路径
- stella 缓存在 `/root/autodl-tmp/.hf_cache/models--dunzhang--stella_en_1.5B_v5/snapshots/...`（HF Hub 格式）
- **教训**：混用 ModelScope 和 HF 下载时，离线模式需要对每个模型分别处理路径

## Phase 1 实验备忘

### GPU 分配注意事项
- **训练阶段设 `CUDA_VISIBLE_DEVICES=0`**：避免 HF Trainer 自动检测双卡走 DDP 并行，浪费显存且 1.5B 模型不需要多卡训练
- **生成阶段显式传 `attention_mask`**：当前 pad_token=eos_token 会触发 HF 警告，必须在 tokenize 时返回 attention_mask 并传给 generate()（V2 代码已修复此问题）

### Phase 0 经验教训
- Worker 不得在循环中高频轮询 SSH 日志，会耗尽 context window（V1 Worker 805 turns / 659 tool calls 后死亡）
- `SFTConfig` 参数名是 `max_length` 不是 `max_seq_length`（trl 版本差异）
- AutoDL 上 ModelScope 下载 Qwen 比 HF 快很多（HF 代理大文件 ~200KB/s）
- 批量生成（batch_size=8）比逐样本生成效率高很多，且更稳定（单样本异常不会中断全流程）
