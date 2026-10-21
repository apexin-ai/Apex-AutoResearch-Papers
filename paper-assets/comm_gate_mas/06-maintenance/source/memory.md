# Memory

## 🔴 P0 匿名仓库审计发现 (2026-04-30)
- `.git/config` 含活跃 GitHub PAT (`ghp_l3Hvs...`) + 用户名 `caoxiaoyuyuyuyuyu` — 必须撤销 token，匿名仓库必须 fresh repo
- 8 个源文件硬编码 `/Users/agent-001/` 或 `/root/autodl-tmp/`（d049_analysis, d051_unified_me_lrt, exp_placeholder_sensitivity, heuristic_threshold_sweep, run_llama_length_only.sh, run_p2_oracle_online.sh, restart_72b_oracle.sh, iaa_*.py）
- 36 个 config YAML 含绝对模型路径，需改为相对占位符
- requirements.txt 缺 transformers, torch, pydantic
- 远程 `artifacts/code_release/` 已有代码发布草稿可参考
- 排除清单：AGENTS.md, memory.md, registry.yaml, decisions.*, ROADMAP.*, report.md, task_context/, 内部 docs/

## R12 预扫薄弱点清单 (2026-04-27)
- **C1 (Critical)**: 72B "scale-stable" claim 基于单 seed，无法估计 seed 间方差。建议弱化为 "preliminary scale evidence" 或补跑 3-5 seeds
- **C2 (Critical)**: 双 backbone 效果 5× 差异（Llama +2.1pp vs Qwen +0.4pp），"dual mechanism" 假说未验证。Defense: non-inferiority 两个都成立，safety 比方向重要
- **M1**: Heuristic 跨域迁移差（Qwen GSM8K F1=0.845 vs StratQA 0.213）。重新定位为 "proof-of-concept" 而非 "deployment-ready"
- **M2**: Greedy decoding (t=0) 限制实用性。Llama t=0.7 heuristic -3.4pp。但 Qwen t=0.7 仍 safe (+0.6pp)
- **M3**: ~~Length-only ablation 缺 Qwen 数据~~ → **已解决** (qwen_length_only_gsm8k, 2026-04-27)
- **M4**: Qwen oracle TOST p=0.048 卡线。Defense: primary claim 是 non-inferiority δ=-3pp (p<0.001)
- **M6**: Gemma κ=0.35 低于阈值但仍计入 "three backbones"。建议改为 "two primary + one exploratory"
- 优先修复: (1) 弱化 scale-stable 措辞 (2) ~~补 Qwen length-only~~ ✅

## D202: Qwen3 重新定性为 heuristic non-transferability (2026-04-27)
- Qwen3 -14pp 不是 "cross-generational failure"，是 "heuristic non-transferability"
- v1 heuristic (char<30) 只捕获 10.2% Qwen3 消息（Δ=-1.0pp, NS）
- char<80 threshold 提高 suppress 到 66.4% 但 Δ=-14pp，confounded with non-ack suppression
- 论文全部 5 个 section + appendix 已更新叙事，grep 确认无残留

## P0 10-seed 复现完成 (2026-04-27)
- 全部 10 seeds 已完成（replication_5run: 42/123/456/789/1024; replication_10run: 2048-6144）
- 每 seed 200 tasks，论文已报告 10-seed 结果（Δ=+0.40±1.02pp）
- ~~3-seed 聚合~~ → **不再需要**，10-seed 数据已覆盖。3-seed 是更早只有 2 个 seed 时的临时方案

## Llama heuristic 5-seed: pruning 实际 beneficial (2026-04-28)
- 5 seeds (42/123/456/789/1011): Mean Δ=+2.20±1.44pp, 95% CI=[+0.41, +3.99]
- CI 完全正向 → **不仅 non-inferior，实际 beneficial**
- 3-seed→5-seed CI 下界从 -1.79 升至 +0.41，质变
- 解释：Llama 的 ack 消息实际产生噪声干扰，剪除后 checker agent 收到更干净的信号
- vs length_only (5-seed): suppress 74.88% vs 0.76% (98.5x)，confirm keyword+ngram 对 Llama verbose acks 不可或缺
- 论文可升级 claim：从 "non-inferior" → "beneficial for Llama"（但 Qwen 仍是 non-inferior）
- 注意：这不改变核心 safety claim（non-inferiority 仍是主 claim），但 beneficial 可作为 secondary finding

## Llama heuristic StrategyQA 4-seed: 跨任务效应比 GSM8K 更强 (2026-04-29)
- 4 seeds (42/0/1/2): Δ=+6.5/+6.0/+4.5/+2.5pp, mean +4.9pp, 所有 seed 正向
- vs GSM8K 5-seed (+2.20pp): StrategyQA 效应约 2x 更强
- Suppress rate ~50.6% 跨 seed 极稳定（<1pp 变异），vs GSM8K ~75% → 不同任务 coverage 自适应
- 含义：heuristic 在 StrategyQA 上更保守（只剪一半消息），但效果反而更好——说明剪掉的确实是纯噪声
- 跨任务 claim 现有双 backbone × 双任务多 seed 证据

## prompt_mod 实验教训 (2026-04-27)
- pruning_mode=none 在 L1320 硬编码 is_ack=False，完全跳过检测。不能用于测量 ack rate
- 新增 detect_only 模式：运行 heuristic 检测但不抑制消息，记录 suppressed_rounds 供分析
- 修改 argparse choices 列表时必须同步更新（L2492），否则命令行参数被拒绝

## Qwen3-8B 跨代通信风格差异 (2026-04-27)
- Qwen3-8B suppress rate 仅 10.2% vs Qwen2.5-7B 的 ~42%（4x 差异）
- 说明 Qwen3 产生更少短 ack 消息，通信风格更"实质性"
- 但剪枝仍然安全（Δ=-1.0pp），说明 heuristic 在不同通信风格下仍精准——只剪真正无信息的短消息
- 论文含义：可 claim 跨代稳定性（不仅跨规模 7B-72B，也跨代 Qwen2.5→Qwen3），但需注意 suppress rate 差异暗示 heuristic 的 coverage 依赖通信风格

## Qwen length-only vs heuristic: 长度即是 heuristic 的核心代理 (2026-04-27)
- Qwen length-only (3-seed): Δ=+0.50±1.50pp, suppress=42.2%
- Qwen heuristic (10-seed): Δ=-0.05±0.99pp, suppress=~39%
- 两者 Δ 均 ≈0，suppress rate 接近 → 确认 Qwen/GSM8K 的 heuristic 本质上是 length filter
- **但 Llama 不同**：length-only (5-seed) Δ=-0.10pp suppress 0.76%; heuristic (5-seed) Δ=+2.20pp suppress 74.88%
- 论文含义：Qwen ack 集中在短消息（length 是好 proxy），Llama 有用信息分布更均匀（length-only 误删关键短消息）→ 支持 model-specific communication pattern 论点

## P2 Cascade position control 揭示跨模型位置趋势反转 (2026-04-28)
- Qwen: position OR=1.95 (正向，后续轮次更多 ack)；Llama: position OR=0.73 (负向，后续轮次更少 ack)
- 但 prev_ack 在两个模型中均高度显著（Qwen OR=6.43, Llama OR=2.02），不受 position 方向影响
- 论文含义：ack cascade 不是位置伪影的强证据——即使 position 效应方向相反，序列依赖仍稳健存在
- 对审稿人攻击面的预防："cascade 只是因为后面的 agent 模仿前面的" → 用 Llama 反例（后续轮次 ack 更少，但 cascade 仍显著）

## Gemma 衰减效应确认 (2026-04-28)
- 排除 Gemma 后 function type → perturbation sensitivity 效应翻倍（ω²: 0.0095→0.0194）
- 与 M6 一致：Gemma κ=0.35 oracle 标注质量低，其噪声数据衰减了真实效应
- 支持 "two primary + one exploratory" 的 framing 策略

## Claude Oracle 替代 GPT-4o 的风险点 (2026-04-27)
- 论文中 GPT-4o 显式提及 15+ 处（表标题、脚注、方法节、附录），切换模型需全面修改叙述或加脚注说明交叉验证
- heuristic detector (char_threshold=30, F1=0.845) 是根据 GPT-4o 标注校准的。如果 Claude 标注的 ack 比例显著不同，阈值可能需要重新调
- 折中叙述方案：方法节脚注 "Oracle labels were generated using GPT-4o; a subset was cross-validated with Claude Sonnet 4 (κ = X.XX)"

## DeepSeek κ=0.0 不可用 (D181, 2026-04-27)
- DeepSeek 做 oracle 标注完全不可用，κ=0.0，导致 P2 必须找替代方案

## OpenAI 429 根因：insufficient_quota (2026-04-27)
- gpt4o_annotation.py 是单线程串行 24 RPM，远低于最低 tier 500 RPM → 不是 rate limit
- 最可能是账户余额不足（insufficient_quota），退避重试无效
- 全量 oracle 标注成本：GPT-4o ~$13.47, GPT-4o-mini ~$0.81（898 tasks, 5388 messages）
- GPT-4o-mini 作为 fallback 需先验证 κ（50 条 pilot）
- OPENAI_API_KEY 在 key store (key_id=openai_key)，需导入环境才能跑探针

## conda base 环境要求 (2026-04-27)
- westb-4x6000-a 服务器系统 Python 无 pyyaml，实验提交必须用 conda base 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`

## Seed 123 重跑验证通过 (2026-04-27)
- D186 事件：seed 123 首次 run 因 226 个 APIConnectionError 导致 baseline=50%（corrupted），已标记作废
- 重跑后 baseline=79.33%（正常范围），确认与旧脏数据分离
- 运行中有大量 BadRequestError 400（prompt+output 超 4096 token limit），脚本 gracefully 跳过，未影响 300 task 全部完成
- 教训：vLLM context length 限制可能导致部分 task 被跳过，但只要 n_tasks=target 就无影响

## P0 N=300 vs 原 N=200 一致性确认 (2026-04-27)
- N=300 3-seed: Δ=+2.44±1.71pp — 与原 10-seed N=200 (Δ=+2.1±2.4pp) 方向一致，均值略高，std 更紧
- 3 seeds 检验力不足：TOST ±5pp p=0.061 边际未过。论文主用 non-inferiority (p=0.0086)
- 关键：N=300 数据可作为 robustness check（更大样本量），但不替代 10-seed 作为主结果

## vLLM pre-flight check 必须校验 model name (2026-04-28)
- [失败模式] infrastructure：vLLM 端口存活但加载了错误模型，pre-flight check 仅验证 HTTP 200 未校验 model name → 全部 tasks 返回 404 SKIPPED
- 修复方案：pre-flight check 增加 `curl /v1/models` 解析返回的 model id，与期望模型名做字符串匹配，不匹配则 abort
- 影响实验：p2_oracle_online_llama_v3（3 seeds × 200 tasks 全废）

## 禁止对部分有效数据使用 --force 重跑 (2026-04-28)
- [调度失误] 修复 vLLM 参数后用 --force 重跑全部 5 seeds，覆盖了 seed 456 的有效数据。seed 456 在 vLLM 未就绪时重跑 → tasks 1-139 全部 404，数据作废
- 正确做法：让有效 seeds (456/789/1011) 先完成，再不带 --force 只补跑缺失的 seeds (42/123)
- 教训：--force 是危险操作，会覆盖已验证的有效数据。只有在确认所有旧数据都需要丢弃时才用 --force
- 竞态根因：脚本启动和 vLLM 就绪之间有时间差（~3min），per-seed pre-flight check 已修复此问题（commit 88770b7）