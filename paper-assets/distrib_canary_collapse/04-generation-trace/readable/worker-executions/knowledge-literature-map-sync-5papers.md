# knowledge literature map sync 5papers

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_knowledge_literature-map-sync-5papers_20260515T044455.log`
- **Structured JSON:** [`fbbc4355c321c9527c9a.json`](../../sessions/fb/fbbc4355c321c9527c9a.json)

## Before a recorded user message

35 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "af7ac655-58f5-46ca-9801-6faf5ce7ac71",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778836800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "101fc117-a1a9-4fd4-b7fc-c8f4a8ca4f70",
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the memory.md and literature_map.yaml files to understand the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "30e7c581-fe81-49ad-adb4-21ff877d13e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012G6xrwWE41yASvk8XEFYbZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11479,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11479
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01T1qZgT6u47CX6wa1NTzGtr`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "44f55d42-6f96-4251-b664-e8881d76f71c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012G6xrwWE41yASvk8XEFYbZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11479,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11479
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T04:45:08.236Z_

<details><summary>↩ Tool result · `toolu_01T1qZgT6u47CX6wa1NTzGtr`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "9054dd4d-1259-4621-a2b7-075ed9dcca78",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me read both files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "92125e62-3aa5-469f-ae47-a9ffe8407da2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrwUaBkbsVz7WaZx5n3TY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 23320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 736
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XCDztsbk7NaFe79cdJ35bb`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "d4ff93f4-e9fa-46ed-8d9d-c5ba83fb3cdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrwUaBkbsVz7WaZx5n3TY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 23320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 736
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T04:45:12.071Z_

<details><summary>↩ Tool result · `toolu_01XCDztsbk7NaFe79cdJ35bb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/memory.md\", \"content\": \"# Memory\\n\\n## 2026-05-14 — MVP 代码设计决策\\n\\n- **训练方式**: 用 HF Trainer，每代独立训练 steps_per_gen 步（非 epoch-based），避免数据量波动导致训练量不一致\\n- **Generation 0 = baseline**: 不训练，只计算初始指标，作为后续 degradation 的参照\\n- **synthetic_ratio 控制混合**: 1.0 = 纯合成（MVP 压力测试），以 synthetic 为基准，ratio<1 时按比例补 real\\n- **Self-BLEU 采样**: 随机抽 500 pairs 而非全组合（O(n²) 太贵），固定 seed=0 保证可复现\\n- **Effective rank**: 用 mean-pooled last hidden states 的协方差矩阵，exp(entropy of normalized eigenvalues)\\n- **MAUVE**: 依赖 mauve-text 包，用 eval_dataset（真实）vs gen_dataset（合成）对比\\n- **ECE**: next-token calibration，10 bins，softmax max prob vs correctness\\n- **Cross-correlation 分析**: normalize 后翻转符号使 \\\"collapse direction\\\" 一致为正，peak lag 的符号决定 lead/lag\\n- **Metrics JSON 每代独立保存 + 汇总**: gen_N/metrics.json 做细粒度追溯，all_metrics.json 做分析输入\\n\\n## 2026-05-14 — AutoDL 服务器经验\\n\\n- **HF 下载不要用 network_turbo 代理**（会卡死），改用 `HF_ENDPOINT=https://hf-mirror.com` 直连国内镜像\\n- **pip install 可以用 network_turbo**\\n- **服务器默认没有 tmux**，需手动 apt 安装\\n- 环境：conda base, Python 3.12.3, PyTorch 2.10.0+cu128, 2× RTX PRO 6000 Blackwell 96GB\\n- **服务器名**: `westd-19828`（非 autodl-rtx6000），submit_training_job 必须用此名\\n\\n## 2026-05-14 — 参数修复 (D004)\\n\\n- 原始参数：n_prompts=1000, steps_per_gen=10000 → 40 epochs/gen，过拟合导致指标骤然击穿\\n- 修正参数：n_prompts=5000, steps_per_gen=5000 → 4 epochs/gen，合理 fine-tuning 量\\n- WikiText-103 test split 仅 ~1500 条 ≥64 words 段落，不够 5000 prompts，改为从 train split 取 prompt 前缀（prompts 仅做生成种子，不参与 loss）\\n- 新数据放 data/wikitext103_5k/ 避免影响正在跑的实验\\n\\n## 2026-05-14 — 文献调研核心发现\\n\\n- 最直接竞争者：chen2025scales (arXiv 2510.05133) 报告 \\\"calibration degradation precedes accuracy loss\\\"——ECE 在 iter 1 + 30% synthetic 时上升 75%，accuracy 未显著变化。但**未做 lead-lag 因果分析**，也没多指标 panel\\n- 8 个文献空白中最关键的 3 个：(1) 无人做 canary Granger causality / lead-lag 量化 (2) ECE 在 collapse 场景下几乎未被系统研究 (3) 多指标 panel 框架完全缺失\\n- Novelty 风险：如果 chen2025scales 团队扩展工作，会侵蚀 ECE-as-canary 的 novelty。需在方法论（Granger causality 框架）上尽快建立壁垒\\n- 共收录 31 篇论文（含补全的 6 篇）\\n- SIGMA (arXiv 2601.03385): Gram matrix 谱双轨监控，我们的 effective rank 是其简化版\\n- Truong & Truong: Class 1 凸反馈 entropy collapse 是一阶相变，canary 在此 regime 可能失效\\n- Fu et al. (ICLR 2025): 恒定 real data 比例保证 STL 收敛，α-sweep 理论基础\\n\\n## 2026-05-14 — 运维教训\\n\\n- **kill_job 只杀 tmux session，不杀子进程**。旧进程 (v1) 存活导致 v2 写同一输出目录死锁。后续 kill 后必须用 `ps aux | grep iterative_train` 确认子进程全部死亡，必要时 `kill -9 $(pgrep -f iterative_train)`\\n- **提交新实验前必须确认输出目录干净**，或使用不同的输出路径\\n- **analyze_mvp.py dry-run 验证通过**：cross-correlation 逻辑正确，token_entropy 和 effective_rank 在信噪比充足时检测准确\\n- **pgrep -a iterative_train 匹配不到训练进程**：因为进程名是 `python`，不是脚本名。用 `nvidia-smi` 或 `ps aux | grep python` 检查\\n- **nohup 启动的实验不写 EXIT_CODE 哨兵**，cron 检测到进程退出后无法判断成功/失败，误判为 failed（rep44 事故）。已在 iterative_train.py 添加 EXIT_CODE 哨兵机制\\n\\n## 2026-05-14 — MVP 4-Seed 正式分析（FINAL VERDICT）\\n\\n- **Overall: STRONG PASS** — 2 个 canary 家族 (token_entropy, ECE) 各自对 ≥1 个 diversity 指标有 SIGNIFICANT LEAD\\n- **最强结果 (4/4 seed 完全一致, std=0)**：\\n  - token_entropy → distinct_1: lag=-1, |r|=0.993–0.998, p=0.0006–0.0036\\n  - ece → distinct_2: lag=-1, |r|=0.995–0.997, p=0.0001–0.0023\\n- **Demoted**: MAUVE (floor effect), effective_rank (non-monotonic, 2+/2- across seeds)\\n- **Eliminated**: self_bleu (方向不一致), ece→perplexity (ECE 反而滞后 perplexity)\\n\\n## 2026-05-14 — ⚠️ Narrative 约束（4-seed 确认 + max_lag=7 验证 + 差分确认）\\n\\n- **Canary 仅能 lead diversity metrics (distinct_n)，不能 lead quality metric (perplexity)**\\n  - token_entropy→perplexity: lag=-5，4/4 seed 一致，但 p borderline（seed42 p=0.12）\\n  - **差分版 permutation Granger 最终确认**：canary→perplexity 全部 F→0, 完全不显著——旧结果 100% 由共享非平稳趋势驱动。这不是统计功效问题，是伪回归\\n  - ECE→perplexity: lag=+4.75（ECE 滞后 perplexity！完全反向）\\n  - 论文 claim 硬限：只能声称 \\\"canary predicts diversity collapse\\\"，不能声称 \\\"canary predicts perplexity\\\"\\n- **plan_006 dual-timescale 升级前景大幅降低**：差分后 F→0 说明关系是纯趋势驱动，更长序列不会改变。plan_006 仍值得跑（验证 diversity lead 在 T=20 下是否更稳健），但不应期望 perplexity channel 突破\\n\\n## 2026-05-14 — ⚠️ 方法论 Ablation 关键结论（plan_002 Phase 1）\\n\\n- **75% 伪回归率**：16/16 naive 显著 pair 中，12 个被 Toda-Yamamoto 推翻\\n- **token_entropy 是唯一 gold-standard canary**：对 distinct_1/2/3 均通过 Granger 因果检验（F=100-550, p<0.001, 4/4 seed）\\n- **ECE 因果预测力大幅缩水**：仅对 distinct_1 通过 TY（3/4 seed），distinct_2/3 的\\\"完美 cross-corr\\\"(lag=-1, std=0) 实为伪回归\\n- **所有 canary→perplexity 全部伪回归**——包括 token_entropy→perplexity (lag=-5)。非平稳驱动的假信号\\n- **self_bleu + effective_rank 完全失效**：100% 伪回归\\n- **Story 调整**：方法论贡献从 \\\"nice to have\\\" 变为 \\\"essential\\\"——naive 方法给出 100% 显著率实为 75% 伪信号\\n- 结果存：`results/mvp/analysis/method_ablation.json` + 服务器上 `method_ablation.py`\\n\\n## 2026-05-14 — ⚠️ Bootstrap TY Power Analysis（plan_009, CRITICAL）\\n\\n- **T=10 下 TY 效力严重不足**：d_max=0 power=0.205, d_max=1 power=0.09, d_max=adaptive power=0.05（≈随机）\\n- **T=20 仍不够**：d_max=1 power=0.172, 远低于 0.50 门槛\\n- **T=30 也不达标**：d_max=1 power=0.283; 唯有 d_max=0 达 0.606 但此时 Type I error 偏高 (0.081)\\n- **d_max 敏感性巨大**：所有 T 下 power range > 0.15\\n- **对论文影响**：(1) TY 不能作为核心证据，只能辅助; (2) 需要补充 permutation-based 或 bootstrap 推断作为替代; (3) limitation 必须透明报告; (4) 这反而强化 Claim 3——方法选择不仅改变结论，连检验本身的 power 也 regime-dependent\\n- **结果存**: `results/bootstrap_ty_results.json`\\n\\n## 2026-05-14 — ⚠️ Permutation Granger 差分版最终结论（D015 → Reviewer 修复）\\n\\n- **差分后 canary→diversity 全部保持显著**：token_entropy→distinct_1/2/3 和 ece→distinct_1/2/3 均 4/4 sig，F 值甚至上升（非伪回归，因果关系真实）\\n- **差分后 canary→perplexity 全部归零**：F→0, p→1。旧结果完全由共享非平稳趋势驱动。这是决定性证据\\n- **5-method ablation 最终排序**：naive 16/16 (100%) > differenced 14/16 (88%) > threshold 9/16 (56%) > permutation Granger 6/16 (38%) > TY 4/16 (25%)\\n- **ECE 地位回升**：差分版 permutation Granger 下 ece→distinct_1/2/3 全部 4/4 sig，比 TY (3/4) 更一致。ECE 作为 secondary canary 的证据比 TY-only 评估更强\\n- **Effect size 统一为 Cohen's f²**：所有分析脚本已统一（method_ablation.py, analyze_alpha_sweep.py, permutation_granger.py）\\n- **脚本**: `permutation_granger.py`（差分+shuffle），结果: `results/mvp/analysis/permutation_granger.json`（含 differenced 和 undifferenced 两组）\\n\\n## 2026-05-14 — mix_datasets bug 修复\\n\\n- **原逻辑**: 保全 synthetic，subsample real → 低 α 下 real 不足时比例静默偏移（α=0.25 变成实际 α=0.50）\\n- **修复后**: 双向 subsample（低 α: 保全 real + subsample syn; 高 α: 保全 syn + subsample real）+ shuffle(seed=seed) 避免位置偏差\\n- 14/14 测试通过，全 α 范围误差 <0.05\\n\\n## 2026-05-14 — plan_006 分析 checklist（20-gen extended run 完成时执行）\\n\\n- [ ] Full series cross-correlation: gen 0-20, max_lag=10, 所有 canary→downstream pair\\n- [ ] **Rolling-window 验证**: gen 5-20 子序列分析 token_entropy→perplexity，排除 gen 0→1 初始跳变\\n- [ ] 与 MVP 10-gen 结果对比：lag 值是否稳定，p-value 是否因样本量增大而达显著\\n- [ ] **主检验用 cross-corr + permutation Granger**（D015 决策），TY 仅 supplementary\\n- [ ] **注意**：差分版已证明 canary→perplexity 是纯趋势驱动。plan_006 的 perplexity channel 预期不会变显著，focus 转向验证 diversity lead 在更长序列下的稳健性\\n\\n## 2026-05-15 文献扫描\\n\\n**搜索范围**: arXiv 2026-05-01 至 2026-05-15，5 组关键词（model collapse synthetic data / distributional collapse iterative training / canary metric degradation / early warning LLM collapse / token entropy calibration ECE model collapse）\\n\\n**结论：未发现直接竞争者。** 过去两周无人发表 canary → collapse prediction 的 lead-lag / Granger causality 分析。我们的核心 novelty（多指标 canary panel + 因果分析框架）仍然安全。\\n\\n### 新论文（目标窗口内）\\n\\n1. **Du & Tanaka-Ishii (2605.00435)** — \\\"Escaping Mode Collapse in LLM Generation via Geometric Regulation\\\" [May 1, 2026]\\n   - 将 mode collapse 重新解释为表示空间中的 geometric collapse：生成时模型内部轨迹被限制在低维子空间。提出 RMR（Reinforced Mode Regulation），在 value cache 中抑制 dominant self-reinforcing directions\\n   - **关系: orthogonal** — 针对推理时 mode collapse，非迭代训练场景。但 \\\"geometric collapse = 低维子空间坍缩\\\" 与我们的 effective rank 指标在概念上有连接，可在 related work 中引用以说明 representation-space collapse 检测的跨场景通用性\\n\\n2. **Gauthier, Bach & Jordan (2605.04266)** — \\\"Explaining and Preventing Alignment Collapse in Iterative RLHF\\\" [May 5, 2026]\\n   - 迭代 RLHF 中 policy 生成 reward model 的训练数据形成反馈环路 → alignment collapse（policy 系统性利用 reward model 盲区）。用 Stackelberg game 建模，提出 FPO（foresighted policy optimization）\\n   - **关系: complementary** — 反馈环路结构与我们的 iterative synthetic training loop 类似（模型输出成为下一轮输入）。他们的 \\\"collapse = 反馈环路中的系统性退化\\\" 叙事支持我们的大框架。Stackelberg game 视角可能启发 canary 的博弈论解释\\n\\n3. **Shi et al. (2605.07271)** — \\\"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\\\" [May 2026]\\n   - 层剪枝导致的 performance collapse。定义 Silent Phase（模型预测被单一选项主导 = distributional collapse）和 Decisive Phase。剪枝 Silent Phase 立即触发 collapse\\n   - **关系: orthogonal** — 架构剪枝 collapse，非数据驱动。其 \\\"distributional collapse = 预测分布退化为单峰\\\" 的操作定义与我们 token entropy 下降检测的是同一现象的不同表现\\n\\n4. **Tübingen AI Center et al. (2605.06366)** — \\\"Layer Collapse in Diffusion Language Models\\\" [May 11, 2026]\\n   - LLaDA-8B 中发现层级 activation collapse：少数早期层的 activation 被单个 super-outlier 主导。剪掉此 outlier 导致模型输出退化为重复随机 token\\n   - **关系: orthogonal** — diffusion LM 的架构 collapse，与迭代合成数据训练无关\\n\\n### 窗口外但新发现的相关论文（已不在 literature_map 中）\\n\\n5. **Bergsma et al. (2509.25087, rev. Mar 2026)** — \\\"Scaling with Collapse: Efficient and Predictable Training of LLM Families\\\" [Cerebras]\\n   - \\\"Collapse\\\" 此处指 loss curve 归一化后坍缩到通用轨迹（非 model collapse）。deviation-from-collapse 作为训练病理的早期诊断信号\\n   - **关系: orthogonal** — 不同语境下的 \\\"collapse\\\"。但其 \\\"偏离通用轨迹 = 训练出问题\\\" 的监控思路与我们的 canary 理念相似\\n\\n### 对项目的影响评估\\n\\n- **Novelty 安全**：2 周内无人做 canary lead-lag 分析或多指标 panel，chen2025scales 仍是最接近竞争者且无更新\\n- **值得引用**：Du & Tanaka-Ishii 的 geometric collapse 概念可强化我们 effective rank 的理论动机（尽管其已被 demoted）\\n- **无需紧急调整路线图**\\n\", \"total_chars\": 8994, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "da0ce9ff-f0e2-4a58-acbc-751dfb8f0424",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/memory.md\\\", \\\"content\\\": \\\"# Memory\\\\n\\\\n## 2026-05-14 — MVP 代码设计决策\\\\n\\\\n- **训练方式**: 用 HF Trainer，每代独立训练 steps_per_gen 步（非 epoch-based），避免数据量波动导致训练量不一致\\\\n- **Generation 0 = baseline**: 不训练，只计算初始指标，作为后续 degradation 的参照\\\\n- **synthetic_ratio 控制混合**: 1.0 = 纯合成（MVP 压力测试），以 synthetic 为基准，ratio<1 时按比例补 real\\\\n- **Self-BLEU 采样**: 随机抽 500 pairs 而非全组合（O(n²) 太贵），固定 seed=0 保证可复现\\\\n- **Effective rank**: 用 mean-pooled last hidden states 的协方差矩阵，exp(entropy of normalized eigenvalues)\\\\n- **MAUVE**: 依赖 mauve-text 包，用 eval_dataset（真实）vs gen_dataset（合成）对比\\\\n- **ECE**: next-token calibration，10 bins，softmax max prob vs correctness\\\\n- **Cross-correlation 分析**: normalize 后翻转符号使 \\\\\\\"collapse direction\\\\\\\" 一致为正，peak lag 的符号决定 lead/lag\\\\n- **Metrics JSON 每代独立保存 + 汇总**: gen_N/metrics.json 做细粒度追溯，all_metrics.json 做分析输入\\\\n\\\\n## 2026-05-14 — AutoDL 服务器经验\\\\n\\\\n- **HF 下载不要用 network_turbo 代理**（会卡死），改用 `HF_ENDPOINT=https://hf-mirror.com` 直连国内镜像\\\\n- **pip install 可以用 network_turbo**\\\\n- **服务器默认没有 tmux**，需手动 apt 安装\\\\n- 环境：conda base, Python 3.12.3, PyTorch 2.10.0+cu128, 2× RTX PRO 6000 Blackwell 96GB\\\\n- **服务器名**: `westd-19828`（非 autodl-rtx6000），submit_training_job 必须用此名\\\\n\\\\n## 2026-05-14 — 参数修复 (D004)\\\\n\\\\n- 原始参数：n_prompts=1000, steps_per_gen=10000 → 40 epochs/gen，过拟合导致指标骤然击穿\\\\n- 修正参数：n_prompts=5000, steps_per_gen=5000 → 4 epochs/gen，合理 fine-tuning 量\\\\n- WikiText-103 test split 仅 ~1500 条 ≥64 words 段落，不够 5000 prompts，改为从 train split 取 prompt 前缀（prompts 仅做生成种子，不参与 loss）\\\\n- 新数据放 data/wikitext103_5k/ 避免影响正在跑的实验\\\\n\\\\n## 2026-05-14 — 文献调研核心发现\\\\n\\\\n- 最直接竞争者：chen2025scales (arXiv 2510.05133) 报告 \\\\\\\"calibration degradation precedes accuracy loss\\\\\\\"——ECE 在 iter 1 + 30% synthetic 时上升 75%，accuracy 未显著变化。但**未做 lead-lag 因果分析**，也没多指标 panel\\\\n- 8 个文献空白中最关键的 3 个：(1) 无人做 canary Granger causality / lead-lag 量化 (2) ECE 在 collapse 场景下几乎未被系统研究 (3) 多指标 panel 框架完全缺失\\\\n- Novelty 风险：如果 chen2025scales 团队扩展工作，会侵蚀 ECE-as-canary 的 novelty。需在方法论（Granger causality 框架）上尽快建立壁垒\\\\n- 共收录 31 篇论文（含补全的 6 篇）\\\\n- SIGMA (arXiv 2601.03385): Gram matrix 谱双轨监控，我们的 effective rank 是其简化版\\\\n- Truong & Truong: Class 1 凸反馈 entropy collapse 是一阶相变，canary 在此 regime 可能失效\\\\n- Fu et al. (ICLR 2025): 恒定 real data 比例保证 STL 收敛，α-sweep 理论基础\\\\n\\\\n## 2026-05-14 — 运维教训\\\\n\\\\n- **kill_job 只杀 tmux session，不杀子进程**。旧进程 (v1) 存活导致 v2 写同一输出目录死锁。后续 kill 后必须用 `ps aux | grep iterative_train` 确认子进程全部死亡，必要时 `kill -9 $(pgrep -f iterative_train)`\\\\n- **提交新实验前必须确认输出目录干净**，或使用不同的输出路径\\\\n- **analyze_mvp.py dry-run 验证通过**：cross-correlation 逻辑正确，token_entropy 和 effective_rank 在信噪比充足时检测准确\\\\n- **pgrep -a iterative_train 匹配不到训练进程**：因为进程名是 `python`，不是脚本名。用 `nvidia-smi` 或 `ps aux | grep python` 检查\\\\n- **nohup 启动的实验不写 EXIT_CODE 哨兵**，cron 检测到进程退出后无法判断成功/失败，误判为 failed（rep44 事故）。已在 iterative_train.py 添加 EXIT_CODE 哨兵机制\\\\n\\\\n## 2026-05-14 — MVP 4-Seed 正式分析（FINAL VERDICT）\\\\n\\\\n- **Overall: STRONG PASS** — 2 个 canary 家族 (token_entropy, ECE) 各自对 ≥1 个 diversity 指标有 SIGNIFICANT LEAD\\\\n- **最强结果 (4/4 seed 完全一致, std=0)**：\\\\n  - token_entropy → distinct_1: lag=-1, |r|=0.993–0.998, p=0.0006–0.0036\\\\n  - ece → distinct_2: lag=-1, |r|=0.995–0.997, p=0.0001–0.0023\\\\n- **Demoted**: MAUVE (floor effect), effective_rank (non-monotonic, 2+/2- across seeds)\\\\n- **Eliminated**: self_bleu (方向不一致), ece→perplexity (ECE 反而滞后 perplexity)\\\\n\\\\n## 2026-05-14 — ⚠️ Narrative 约束（4-seed 确认 + max_lag=7 验证 + 差分确认）\\\\n\\\\n- **Canary 仅能 lead diversity metrics (distinct_n)，不能 lead quality metric (perplexity)**\\\\n  - token_entropy→perplexity: lag=-5，4/4 seed 一致，但 p borderline（seed42 p=0.12）\\\\n  - **差分版 permutation Granger 最终确认**：canary→perplexity 全部 F→0, 完全不显著——旧结果 100% 由共享非平稳趋势驱动。这不是统计功效问题，是伪回归\\\\n  - ECE→perplexity: lag=+4.75（ECE 滞后 perplexity！完全反向）\\\\n  - 论文 claim 硬限：只能声称 \\\\\\\"canary predicts diversity collapse\\\\\\\"，不能声称 \\\\\\\"canary predicts perplexity\\\\\\\"\\\\n- **plan_006 dual-timescale 升级前景大幅降低**：差分后 F→0 说明关系是纯趋势驱动，更长序列不会改变。plan_006 仍值得跑（验证 diversity lead 在 T=20 下是否更稳健），但不应期望 perplexity channel 突破\\\\n\\\\n## 2026-05-14 — ⚠️ 方法论 Ablation 关键结论（plan_002 Phase 1）\\\\n\\\\n- **75% 伪回归率**：16/16 naive 显著 pair 中，12 个被 Toda-Yamamoto 推翻\\\\n- **token_entropy 是唯一 gold-standard canary**：对 distinct_1/2/3 均通过 Granger 因果检验（F=100-550, p<0.001, 4/4 seed）\\\\n- **ECE 因果预测力大幅缩水**：仅对 distinct_1 通过 TY（3/4 seed），distinct_2/3 的\\\\\\\"完美 cross-corr\\\\\\\"(lag=-1, std=0) 实为伪回归\\\\n- **所有 canary→perplexity 全部伪回归**——包括 token_entropy→perplexity (lag=-5)。非平稳驱动的假信号\\\\n- **self_bleu + effective_rank 完全失效**：100% 伪回归\\\\n- **Story 调整**：方法论贡献从 \\\\\\\"nice to have\\\\\\\" 变为 \\\\\\\"essential\\\\\\\"——naive 方法给出 100% 显著率实为 75% 伪信号\\\\n- 结果存：`results/mvp/analysis/method_ablation.json` + 服务器上 `method_ablation.py`\\\\n\\\\n## 2026-05-14 — ⚠️ Bootstrap TY Power Analysis（plan_009, CRITICAL）\\\\n\\\\n- **T=10 下 TY 效力严重不足**：d_max=0 power=0.205, d_max=1 power=0.09, d_max=adaptive power=0.05（≈随机）\\\\n- **T=20 仍不够**：d_max=1 power=0.172, 远低于 0.50 门槛\\\\n- **T=30 也不达标**：d_max=1 power=0.283; 唯有 d_max=0 达 0.606 但此时 Type I error 偏高 (0.081)\\\\n- **d_max 敏感性巨大**：所有 T 下 power range > 0.15\\\\n- **对论文影响**：(1) TY 不能作为核心证据，只能辅助; (2) 需要补充 permutation-based 或 bootstrap 推断作为替代; (3) limitation 必须透明报告; (4) 这反而强化 Claim 3——方法选择不仅改变结论，连检验本身的 power 也 regime-dependent\\\\n- **结果存**: `results/bootstrap_ty_results.json`\\\\n\\\\n## 2026-05-14 — ⚠️ Permutation Granger 差分版最终结论（D015 → Reviewer 修复）\\\\n\\\\n- **差分后 canary→diversity 全部保持显著**：token_entropy→distinct_1/2/3 和 ece→distinct_1/2/3 均 4/4 sig，F 值甚至上升（非伪回归，因果关系真实）\\\\n- **差分后 canary→perplexity 全部归零**：F→0, p→1。旧结果完全由共享非平稳趋势驱动。这是决定性证据\\\\n- **5-method ablation 最终排序**：naive 16/16 (100%) > differenced 14/16 (88%) > threshold 9/16 (56%) > permutation Granger 6/16 (38%) > TY 4/16 (25%)\\\\n- **ECE 地位回升**：差分版 permutation Granger 下 ece→distinct_1/2/3 全部 4/4 sig，比 TY (3/4) 更一致。ECE 作为 secondary canary 的证据比 TY-only 评估更强\\\\n- **Effect size 统一为 Cohen's f²**：所有分析脚本已统一（method_ablation.py, analyze_alpha_sweep.py, permutation_granger.py）\\\\n- **脚本**: `permutation_granger.py`（差分+shuffle），结果: `results/mvp/analysis/permutation_granger.json`（含 differenced 和 undifferenced 两组）\\\\n\\\\n## 2026-05-14 — mix_datasets bug 修复\\\\n\\\\n- **原逻辑**: 保全 synthetic，subsample real → 低 α 下 real 不足时比例静默偏移（α=0.25 变成实际 α=0.50）\\\\n- **修复后**: 双向 subsample（低 α: 保全 real + subsample syn; 高 α: 保全 syn + subsample real）+ shuffle(seed=seed) 避免位置偏差\\\\n- 14/14 测试通过，全 α 范围误差 <0.05\\\\n\\\\n## 2026-05-14 — plan_006 分析 checklist（20-gen extended run 完成时执行）\\\\n\\\\n- [ ] Full series cross-correlation: gen 0-20, max_lag=10, 所有 canary→downstream pair\\\\n- [ ] **Rolling-window 验证**: gen 5-20 子序列分析 token_entropy→perplexity，排除 gen 0→1 初始跳变\\\\n- [ ] 与 MVP 10-gen 结果对比：lag 值是否稳定，p-value 是否因样本量增大而达显著\\\\n- [ ] **主检验用 cross-corr + permutation Granger**（D015 决策），TY 仅 supplementary\\\\n- [ ] **注意**：差分版已证明 canary→perplexity 是纯趋势驱动。plan_006 的 perplexity channel 预期不会变显著，focus 转向验证 diversity lead 在更长序列下的稳健性\\\\n\\\\n## 2026-05-15 文献扫描\\\\n\\\\n**搜索范围**: arXiv 2026-05-01 至 2026-05-15，5 组关键词（model collapse synthetic data / distributional collapse iterative training / canary metric degradation / early warning LLM collapse / token entropy calibration ECE model collapse）\\\\n\\\\n**结论：未发现直接竞争者。** 过去两周无人发表 canary → collapse prediction 的 lead-lag / Granger causality 分析。我们的核心 novelty（多指标 canary panel + 因果分析框架）仍然安全。\\\\n\\\\n### 新论文（目标窗口内）\\\\n\\\\n1. **Du & Tanaka-Ishii (2605.00435)** — \\\\\\\"Escaping Mode Collapse in LLM Generation via Geometric Regulation\\\\\\\" [May 1, 2026]\\\\n   - 将 mode collapse 重新解释为表示空间中的 geometric collapse：生成时模型内部轨迹被限制在低维子空间。提出 RMR（Reinforced Mode Regulation），在 value cache 中抑制 dominant self-reinforcing directions\\\\n   - **关系: orthogonal** — 针对推理时 mode collapse，非迭代训练场景。但 \\\\\\\"geometric collapse = 低维子空间坍缩\\\\\\\" 与我们的 effective rank 指标在概念上有连接，可在 related work 中引用以说明 representation-space collapse 检测的跨场景通用性\\\\n\\\\n2. **Gauthier, Bach & Jordan (2605.04266)** — \\\\\\\"Explaining and Preventing Alignment Collapse in Iterative RLHF\\\\\\\" [May 5, 2026]\\\\n   - 迭代 RLHF 中 policy 生成 reward model 的训练数据形成反馈环路 → alignment collapse（policy 系统性利用 reward model 盲区）。用 Stackelberg game 建模，提出 FPO（foresighted policy optimization）\\\\n   - **关系: complementary** — 反馈环路结构与我们的 iterative synthetic training loop 类似（模型输出成为下一轮输入）。他们的 \\\\\\\"collapse = 反馈环路中的系统性退化\\\\\\\" 叙事支持我们的大框架。Stackelberg game 视角可能启发 canary 的博弈论解释\\\\n\\\\n3. **Shi et al. (2605.07271)** — \\\\\\\"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\\\\\\\" [May 2026]\\\\n   - 层剪枝导致的 performance collapse。定义 Silent Phase（模型预测被单一选项主导 = distributional collapse）和 Decisive Phase。剪枝 Silent Phase 立即触发 collapse\\\\n   - **关系: orthogonal** — 架构剪枝 collapse，非数据驱动。其 \\\\\\\"distributional collapse = 预测分布退化为单峰\\\\\\\" 的操作定义与我们 token entropy 下降检测的是同一现象的不同表现\\\\n\\\\n4. **Tübingen AI Center et al. (2605.06366)** — \\\\\\\"Layer Collapse in Diffusion Language Models\\\\\\\" [May 11, 2026]\\\\n   - LLaDA-8B 中发现层级 activation collapse：少数早期层的 activation 被单个 super-outlier 主导。剪掉此 outlier 导致模型输出退化为重复随机 token\\\\n   - **关系: orthogonal** — diffusion LM 的架构 collapse，与迭代合成数据训练无关\\\\n\\\\n### 窗口外但新发现的相关论文（已不在 literature_map 中）\\\\n\\\\n5. **Bergsma et al. (2509.25087, rev. Mar 2026)** — \\\\\\\"Scaling with Collapse: Efficient and Predictable Training of LLM Families\\\\\\\" [Cerebras]\\\\n   - \\\\\\\"Collapse\\\\\\\" 此处指 loss curve 归一化后坍缩到通用轨迹（非 model collapse）。deviation-from-collapse 作为训练病理的早期诊断信号\\\\n   - **关系: orthogonal** — 不同语境下的 \\\\\\\"collapse\\\\\\\"。但其 \\\\\\\"偏离通用轨迹 = 训练出问题\\\\\\\" 的监控思路与我们的 canary 理念相似\\\\n\\\\n### 对项目的影响评估\\\\n\\\\n- **Novelty 安全**：2 周内无人做 canary lead-lag 分析或多指标 panel，chen2025scales 仍是最接近竞争者且无更新\\\\n- **值得引用**：Du & Tanaka-Ishii 的 geometric collapse 概念可强化我们 effective rank 的理论动机（尽管其已被 demoted）\\\\n- **无需紧急调整路线图**\\\\n\\\", \\\"total_chars\\\": 8994, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/memory.md\", \"content\": \"# Memory\\n\\n## 2026-05-14 — MVP 代码设计决策\\n\\n- **训练方式**: 用 HF Trainer，每代独立训练 steps_per_gen 步（非 epoch-based），避免数据量波动导致训练量不一致\\n- **Generation 0 = baseline**: 不训练，只计算初始指标，作为后续 degradation 的参照\\n- **synthetic_ratio 控制混合**: 1.0 = 纯合成（MVP 压力测试），以 synthetic 为基准，ratio<1 时按比例补 real\\n- **Self-BLEU 采样**: 随机抽 500 pairs 而非全组合（O(n²) 太贵），固定 seed=0 保证可复现\\n- **Effective rank**: 用 mean-pooled last hidden states 的协方差矩阵，exp(entropy of normalized eigenvalues)\\n- **MAUVE**: 依赖 mauve-text 包，用 eval_dataset（真实）vs gen_dataset（合成）对比\\n- **ECE**: next-token calibration，10 bins，softmax max prob vs correctness\\n- **Cross-correlation 分析**: normalize 后翻转符号使 \\\"collapse direction\\\" 一致为正，peak lag 的符号决定 lead/lag\\n- **Metrics JSON 每代独立保存 + 汇总**: gen_N/metrics.json 做细粒度追溯，all_metrics.json 做分析输入\\n\\n## 2026-05-14 — AutoDL 服务器经验\\n\\n- **HF 下载不要用 network_turbo 代理**（会卡死），改用 `HF_ENDPOINT=https://hf-mirror.com` 直连国内镜像\\n- **pip install 可以用 network_turbo**\\n- **服务器默认没有 tmux**，需手动 apt 安装\\n- 环境：conda base, Python 3.12.3, PyTorch 2.10.0+cu128, 2× RTX PRO 6000 Blackwell 96GB\\n- **服务器名**: `westd-19828`（非 autodl-rtx6000），submit_training_job 必须用此名\\n\\n## 2026-05-14 — 参数修复 (D004)\\n\\n- 原始参数：n_prompts=1000, steps_per_gen=10000 → 40 epochs/gen，过拟合导致指标骤然击穿\\n- 修正参数：n_prompts=5000, steps_per_gen=5000 → 4 epochs/gen，合理 fine-tuning 量\\n- WikiText-103 test split 仅 ~1500 条 ≥64 words 段落，不够 5000 prompts，改为从 train split 取 prompt 前缀（prompts 仅做生成种子，不参与 loss）\\n- 新数据放 data/wikitext103_5k/ 避免影响正在跑的实验\\n\\n## 2026-05-14 — 文献调研核心发现\\n\\n- 最直接竞争者：chen2025scales (arXiv 2510.05133) 报告 \\\"calibration degradation precedes accuracy loss\\\"——ECE 在 iter 1 + 30% synthetic 时上升 75%，accuracy 未显著变化。但**未做 lead-lag 因果分析**，也没多指标 panel\\n- 8 个文献空白中最关键的 3 个：(1) 无人做 canary Granger causality / lead-lag 量化 (2) ECE 在 collapse 场景下几乎未被系统研究 (3) 多指标 panel 框架完全缺失\\n- Novelty 风险：如果 chen2025scales 团队扩展工作，会侵蚀 ECE-as-canary 的 novelty。需在方法论（Granger causality 框架）上尽快建立壁垒\\n- 共收录 31 篇论文（含补全的 6 篇）\\n- SIGMA (arXiv 2601.03385): Gram matrix 谱双轨监控，我们的 effective rank 是其简化版\\n- Truong & Truong: Class 1 凸反馈 entropy collapse 是一阶相变，canary 在此 regime 可能失效\\n- Fu et al. (ICLR 2025): 恒定 real data 比例保证 STL 收敛，α-sweep 理论基础\\n\\n## 2026-05-14 — 运维教训\\n\\n- **kill_job 只杀 tmux session，不杀子进程**。旧进程 (v1) 存活导致 v2 写同一输出目录死锁。后续 kill 后必须用 `ps aux | grep iterative_train` 确认子进程全部死亡，必要时 `kill -9 $(pgrep -f iterative_train)`\\n- **提交新实验前必须确认输出目录干净**，或使用不同的输出路径\\n- **analyze_mvp.py dry-run 验证通过**：cross-correlation 逻辑正确，token_entropy 和 effective_rank 在信噪比充足时检测准确\\n- **pgrep -a iterative_train 匹配不到训练进程**：因为进程名是 `python`，不是脚本名。用 `nvidia-smi` 或 `ps aux | grep python` 检查\\n- **nohup 启动的实验不写 EXIT_CODE 哨兵**，cron 检测到进程退出后无法判断成功/失败，误判为 failed（rep44 事故）。已在 iterative_train.py 添加 EXIT_CODE 哨兵机制\\n\\n## 2026-05-14 — MVP 4-Seed 正式分析（FINAL VERDICT）\\n\\n- **Overall: STRONG PASS** — 2 个 canary 家族 (token_entropy, ECE) 各自对 ≥1 个 diversity 指标有 SIGNIFICANT LEAD\\n- **最强结果 (4/4 seed 完全一致, std=0)**：\\n  - token_entropy → distinct_1: lag=-1, |r|=0.993–0.998, p=0.0006–0.0036\\n  - ece → distinct_2: lag=-1, |r|=0.995–0.997, p=0.0001–0.0023\\n- **Demoted**: MAUVE (floor effect), effective_rank (non-monotonic, 2+/2- across seeds)\\n- **Eliminated**: self_bleu (方向不一致), ece→perplexity (ECE 反而滞后 perplexity)\\n\\n## 2026-05-14 — ⚠️ Narrative 约束（4-seed 确认 + max_lag=7 验证 + 差分确认）\\n\\n- **Canary 仅能 lead diversity metrics (distinct_n)，不能 lead quality metric (perplexity)**\\n  - token_entropy→perplexity: lag=-5，4/4 seed 一致，但 p borderline（seed42 p=0.12）\\n  - **差分版 permutation Granger 最终确认**：canary→perplexity 全部 F→0, 完全不显著——旧结果 100% 由共享非平稳趋势驱动。这不是统计功效问题，是伪回归\\n  - ECE→perplexity: lag=+4.75（ECE 滞后 perplexity！完全反向）\\n  - 论文 claim 硬限：只能声称 \\\"canary predicts diversity collapse\\\"，不能声称 \\\"canary predicts perplexity\\\"\\n- **plan_006 dual-timescale 升级前景大幅降低**：差分后 F→0 说明关系是纯趋势驱动，更长序列不会改变。plan_006 仍值得跑（验证 diversity lead 在 T=20 下是否更稳健），但不应期望 perplexity channel 突破\\n\\n## 2026-05-14 — ⚠️ 方法论 Ablation 关键结论（plan_002 Phase 1）\\n\\n- **75% 伪回归率**：16/16 naive 显著 pair 中，12 个被 Toda-Yamamoto 推翻\\n- **token_entropy 是唯一 gold-standard canary**：对 distinct_1/2/3 均通过 Granger 因果检验（F=100-550, p<0.001, 4/4 seed）\\n- **ECE 因果预测力大幅缩水**：仅对 distinct_1 通过 TY（3/4 seed），distinct_2/3 的\\\"完美 cross-corr\\\"(lag=-1, std=0) 实为伪回归\\n- **所有 canary→perplexity 全部伪回归**——包括 token_entropy→perplexity (lag=-5)。非平稳驱动的假信号\\n- **self_bleu + effective_rank 完全失效**：100% 伪回归\\n- **Story 调整**：方法论贡献从 \\\"nice to have\\\" 变为 \\\"essential\\\"——naive 方法给出 100% 显著率实为 75% 伪信号\\n- 结果存：`results/mvp/analysis/method_ablation.json` + 服务器上 `method_ablation.py`\\n\\n## 2026-05-14 — ⚠️ Bootstrap TY Power Analysis（plan_009, CRITICAL）\\n\\n- **T=10 下 TY 效力严重不足**：d_max=0 power=0.205, d_max=1 power=0.09, d_max=adaptive power=0.05（≈随机）\\n- **T=20 仍不够**：d_max=1 power=0.172, 远低于 0.50 门槛\\n- **T=30 也不达标**：d_max=1 power=0.283; 唯有 d_max=0 达 0.606 但此时 Type I error 偏高 (0.081)\\n- **d_max 敏感性巨大**：所有 T 下 power range > 0.15\\n- **对论文影响**：(1) TY 不能作为核心证据，只能辅助; (2) 需要补充 permutation-based 或 bootstrap 推断作为替代; (3) limitation 必须透明报告; (4) 这反而强化 Claim 3——方法选择不仅改变结论，连检验本身的 power 也 regime-dependent\\n- **结果存**: `results/bootstrap_ty_results.json`\\n\\n## 2026-05-14 — ⚠️ Permutation Granger 差分版最终结论（D015 → Reviewer 修复）\\n\\n- **差分后 canary→diversity 全部保持显著**：token_entropy→distinct_1/2/3 和 ece→distinct_1/2/3 均 4/4 sig，F 值甚至上升（非伪回归，因果关系真实）\\n- **差分后 canary→perplexity 全部归零**：F→0, p→1。旧结果完全由共享非平稳趋势驱动。这是决定性证据\\n- **5-method ablation 最终排序**：naive 16/16 (100%) > differenced 14/16 (88%) > threshold 9/16 (56%) > permutation Granger 6/16 (38%) > TY 4/16 (25%)\\n- **ECE 地位回升**：差分版 permutation Granger 下 ece→distinct_1/2/3 全部 4/4 sig，比 TY (3/4) 更一致。ECE 作为 secondary canary 的证据比 TY-only 评估更强\\n- **Effect size 统一为 Cohen's f²**：所有分析脚本已统一（method_ablation.py, analyze_alpha_sweep.py, permutation_granger.py）\\n- **脚本**: `permutation_granger.py`（差分+shuffle），结果: `results/mvp/analysis/permutation_granger.json`（含 differenced 和 undifferenced 两组）\\n\\n## 2026-05-14 — mix_datasets bug 修复\\n\\n- **原逻辑**: 保全 synthetic，subsample real → 低 α 下 real 不足时比例静默偏移（α=0.25 变成实际 α=0.50）\\n- **修复后**: 双向 subsample（低 α: 保全 real + subsample syn; 高 α: 保全 syn + subsample real）+ shuffle(seed=seed) 避免位置偏差\\n- 14/14 测试通过，全 α 范围误差 <0.05\\n\\n## 2026-05-14 — plan_006 分析 checklist（20-gen extended run 完成时执行）\\n\\n- [ ] Full series cross-correlation: gen 0-20, max_lag=10, 所有 canary→downstream pair\\n- [ ] **Rolling-window 验证**: gen 5-20 子序列分析 token_entropy→perplexity，排除 gen 0→1 初始跳变\\n- [ ] 与 MVP 10-gen 结果对比：lag 值是否稳定，p-value 是否因样本量增大而达显著\\n- [ ] **主检验用 cross-corr + permutation Granger**（D015 决策），TY 仅 supplementary\\n- [ ] **注意**：差分版已证明 canary→perplexity 是纯趋势驱动。plan_006 的 perplexity channel 预期不会变显著，focus 转向验证 diversity lead 在更长序列下的稳健性\\n\\n## 2026-05-15 文献扫描\\n\\n**搜索范围**: arXiv 2026-05-01 至 2026-05-15，5 组关键词（model collapse synthetic data / distributional collapse iterative training / canary metric degradation / early warning LLM collapse / token entropy calibration ECE model collapse）\\n\\n**结论：未发现直接竞争者。** 过去两周无人发表 canary → collapse prediction 的 lead-lag / Granger causality 分析。我们的核心 novelty（多指标 canary panel + 因果分析框架）仍然安全。\\n\\n### 新论文（目标窗口内）\\n\\n1. **Du & Tanaka-Ishii (2605.00435)** — \\\"Escaping Mode Collapse in LLM Generation via Geometric Regulation\\\" [May 1, 2026]\\n   - 将 mode collapse 重新解释为表示空间中的 geometric collapse：生成时模型内部轨迹被限制在低维子空间。提出 RMR（Reinforced Mode Regulation），在 value cache 中抑制 dominant self-reinforcing directions\\n   - **关系: orthogonal** — 针对推理时 mode collapse，非迭代训练场景。但 \\\"geometric collapse = 低维子空间坍缩\\\" 与我们的 effective rank 指标在概念上有连接，可在 related work 中引用以说明 representation-space collapse 检测的跨场景通用性\\n\\n2. **Gauthier, Bach & Jordan (2605.04266)** — \\\"Explaining and Preventing Alignment Collapse in Iterative RLHF\\\" [May 5, 2026]\\n   - 迭代 RLHF 中 policy 生成 reward model 的训练数据形成反馈环路 → alignment collapse（policy 系统性利用 reward model 盲区）。用 Stackelberg game 建模，提出 FPO（foresighted policy optimization）\\n   - **关系: complementary** — 反馈环路结构与我们的 iterative synthetic training loop 类似（模型输出成为下一轮输入）。他们的 \\\"collapse = 反馈环路中的系统性退化\\\" 叙事支持我们的大框架。Stackelberg game 视角可能启发 canary 的博弈论解释\\n\\n3. **Shi et al. (2605.07271)** — \\\"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\\\" [May 2026]\\n   - 层剪枝导致的 performance collapse。定义 Silent Phase（模型预测被单一选项主导 = distributional collapse）和 Decisive Phase。剪枝 Silent Phase 立即触发 collapse\\n   - **关系: orthogonal** — 架构剪枝 collapse，非数据驱动。其 \\\"distributional collapse = 预测分布退化为单峰\\\" 的操作定义与我们 token entropy 下降检测的是同一现象的不同表现\\n\\n4. **Tübingen AI Center et al. (2605.06366)** — \\\"Layer Collapse in Diffusion Language Models\\\" [May 11, 2026]\\n   - LLaDA-8B 中发现层级 activation collapse：少数早期层的 activation 被单个 super-outlier 主导。剪掉此 outlier 导致模型输出退化为重复随机 token\\n   - **关系: orthogonal** — diffusion LM 的架构 collapse，与迭代合成数据训练无关\\n\\n### 窗口外但新发现的相关论文（已不在 literature_map 中）\\n\\n5. **Bergsma et al. (2509.25087, rev. Mar 2026)** — \\\"Scaling with Collapse: Efficient and Predictable Training of LLM Families\\\" [Cerebras]\\n   - \\\"Collapse\\\" 此处指 loss curve 归一化后坍缩到通用轨迹（非 model collapse）。deviation-from-collapse 作为训练病理的早期诊断信号\\n   - **关系: orthogonal** — 不同语境下的 \\\"collapse\\\"。但其 \\\"偏离通用轨迹 = 训练出问题\\\" 的监控思路与我们的 canary 理念相似\\n\\n### 对项目的影响评估\\n\\n- **Novelty 安全**：2 周内无人做 canary lead-lag 分析或多指标 panel，chen2025scales 仍是最接近竞争者且无更新\\n- **值得引用**：Du & Tanaka-Ishii 的 geometric collapse 概念可强化我们 effective rank 的理论动机（尽管其已被 demoted）\\n- **无需紧急调整路线图**\\n\", \"total_chars\": 8994, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01G2uKHPhZSRu5yc8Zr2K3QH`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "49c4abc3-77e8-4d0a-9ea1-e4785139fbd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrwUaBkbsVz7WaZx5n3TY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 23320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 736
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T04:45:12.657Z_

<details><summary>↩ Tool result · `toolu_01G2uKHPhZSRu5yc8Zr2K3QH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # CORE MODEL COLLAPSE\\n  # ============================================================\\n  - id: \\\"shumailov2024curse\\\"\\n    title: \\\"The Curse of Recursion: Training on Generated Data Makes Models Forget\\\"\\n    authors: \\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\\\"\\n    venue: \\\"Nature\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2305.17493\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\\\"\\n      - \\\"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\\\"\\n      - \\\"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\\\"\\n      - \\\"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\\\"\\n    relevance_to_us: \\\"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\\\"\\n    metrics_studied: [\\\"perplexity\\\", \\\"distributional tail mass\\\"]\\n\\n  - id: \\\"alemohammad2024mad\\\"\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2307.01850\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"提出 Model Autophagy Disorder (MAD) 概念\\\"\\n      - \\\"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\\\"\\n      - \\\"在图像生成领域验证 self-consuming loop 的退化效应\\\"\\n    relevance_to_us: \\\"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\\\"\\n    metrics_studied: [\\\"FID\\\", \\\"precision\\\", \\\"recall\\\", \\\"diversity\\\"]\\n\\n  - id: \\\"dohmatob2024tale\\\"\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Elvis Dohmatob, Yunzhen Feng, et al.\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2402.07043\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\\\"\\n      - \\\"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\\\"\\n      - \\\"混入少量干净数据可缓解 collapse 并引发 grokking 现象\\\"\\n      - \\\"在 transformer 算术任务和 Llama2 文本生成上验证\\\"\\n    relevance_to_us: \\\"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\\\"\\n    metrics_studied: [\\\"test loss\\\", \\\"scaling exponents\\\"]\\n\\n  - id: \\\"dohmatob2025strong\\\"\\n    title: \\\"Strong Model Collapse\\\"\\n    authors: \\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\"\\n    venue: \\\"ICLR 2025 (Spotlight)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.04840\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"即使合成数据占比极小（1/1000），仍可导致 model collapse\\\"\\n      - \\\"更大的训练集并不能避免 collapse\\\"\\n      - \\\"更大的模型（random projection 近似下）反而可能放大 collapse\\\"\\n      - \\\"存在 interpolation threshold 的 double-descent 现象\\\"\\n    relevance_to_us: \\\"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\\\"\\n    metrics_studied: [\\\"test loss\\\", \\\"population risk\\\"]\\n\\n  - id: \\\"guo2024linguistic\\\"\\n    title: \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\"\\n    authors: \\\"Yanzhu Guo, Guokan Shang, et al.\\\"\\n    venue: \\\"NAACL 2024 Findings\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2311.09807\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"evaluation\\\"\\n    key_findings:\\n      - \\\"递归微调中，linguistic diversity 在连续迭代中持续下降\\\"\\n      - \\\"创造性任务中 diversity 下降最显著\\\"\\n      - \\\"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\\\"\\n    relevance_to_us: \\\"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\\\"\\n    metrics_studied: [\\\"distinct-n\\\", \\\"type-token ratio\\\", \\\"syntactic diversity\\\", \\\"semantic diversity\\\"]\\n\\n  - id: \\\"briesch2024selfconsuming\\\"\\n    title: \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\"\\n    authors: \\\"Martin Briesch, Dominik Sobania, Franz Rothlauf\\\"\\n    venue: \\\"arXiv (2311.16822)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2311.16822\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"首次系统研究 LLM 的 self-consuming training loop\\\"\\n      - \\\"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\\\"\\n      - \\\"expanding data cycle（累积）在 50 代内保持 diversity\\\"\\n    relevance_to_us: \\\"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\\\"\\n    metrics_studied: [\\\"diversity\\\", \\\"quality\\\"]\\n\\n  - id: \\\"truong2025entropy\\\"\\n    title: \\\"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\\\"\\n    authors: \\\"Truong Xuan Khanh, Truong Quynh Hoa\\\"\\n    venue: \\\"arXiv (2512.12381)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2512.12381\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\\\"\\n      - \\\"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\\\"\\n      - \\\"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\\\"\\n    relevance_to_us: \\\"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\\\"\\n    gaps: \\\"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\\\"\\n    metrics_studied: [\\\"entropy\\\", \\\"autocorrelation\\\", \\\"variance\\\"]\\n\\n  - id: \\\"wang2026contaminated\\\"\\n    title: \\\"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\\\"\\n    authors: \\\"Kevin Wang, Hongqian Niu, Didong Li\\\"\\n    venue: \\\"arXiv (2602.16065)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.16065\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\\\"\\n      - \\\"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\\\"\\n      - \\\"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\\\"\\n    relevance_to_us: \\\"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\\\"\\n    gaps: \\\"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\\\"\\n    metrics_studied: [\\\"convergence rate\\\", \\\"population risk\\\"]\\n\\n  # ============================================================\\n  # CANARY / EARLY WARNING METRICS\\n  # ============================================================\\n  - id: \\\"chen2025scales\\\"\\n    title: \\\"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"arXiv (2510.05133)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.05133\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\\\"\\n      - \\\"20% synthetic data 以下性能稳定，30% 以上退化加速\\\"\\n      - \\\"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\\\"\\n      - \\\"推理任务比检索任务更易退化\\\"\\n      - \\\"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\\\"\\n    relevance_to_us: \\\"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"accuracy\\\", \\\"perplexity\\\"]\\n\\n  - id: \\\"gambetta2024surplexity\\\"\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\"\\n    authors: \\\"Daniele Gambetta et al.\\\"\\n    venue: \\\"arXiv (2410.12341)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.12341\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\\\"\\n      - \\\"用 semantic networks 分析文本重复性和语义多样性\\\"\\n      - \\\"用 next-token probability 定量衡量 diversity loss\\\"\\n      - \\\"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\\\"\\n      - \\\"不需要区分 human vs AI-generated data\\\"\\n    relevance_to_us: \\\"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\\\"\\n    metrics_studied: [\\\"surplexity\\\", \\\"semantic network metrics\\\", \\\"next-token probability\\\"]\\n\\n  - id: \\\"qiu2025spectral\\\"\\n    title: \\\"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\\\"\\n    authors: \\\"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\\\"\\n    venue: \\\"arXiv (2510.04202)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.04202\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\\\"\\n      - \\\"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\\\"\\n      - \\\"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\\\"\\n      - \\\"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\\\"\\n    relevance_to_us: \\\"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\\\"\\n    metrics_studied: [\\\"spectral alignment\\\", \\\"weight norm\\\", \\\"gradient norm\\\"]\\n\\n  - id: \\\"he2025closer\\\"\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: \\\"Shiliang He et al.\\\"\\n    venue: \\\"NeurIPS 2025 (Spotlight)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2509.16499\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"识别 diffusion model collapse 中的 generalization → memorization 转变\\\"\\n      - \\\"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\\\"\\n      - \\\"提出基于 entropy 的数据选择策略，有效缓解 collapse\\\"\\n    relevance_to_us: \\\"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\\\"\\n    metrics_studied: [\\\"entropy\\\", \\\"FID\\\", \\\"diversity\\\"]\\n\\n  - id: \\\"ba2024fill\\\"\\n    title: \\\"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\\\"\\n    authors: \\\"Yang Ba, Michelle V Mancenido, Rong Pan\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.10864\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\\\"\\n      - \\\"推导了基于 PAC 框架的 ECE bound\\\"\\n      - \\\"合成数据可改善 calibration 但需精心设计生成策略\\\"\\n    relevance_to_us: \\\"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"accuracy\\\"]\\n\\n  - id: \\\"sigma2026spectral\\\"\\n    title: \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\"\\n    authors: \\\"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\\\"\\n    venue: \\\"arXiv (2601.03385)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2601.03385\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\\\"\\n      - \\\"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\\\"\\n      - \\\"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\\\"\\n    relevance_to_us: \\\"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\\\"\\n    gaps: \\\"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\\\"\\n    metrics_studied: [\\\"Gram matrix eigenspectrum\\\", \\\"spectral norm bounds\\\"]\\n\\n  - id: \\\"kalinowski2026topology\\\"\\n    title: \\\"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\\\"\\n    authors: \\\"Alexander Kalinowski\\\"\\n    venue: \\\"arXiv (2604.26984)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2604.26984\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\\\"\\n      - \\\"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\\\"\\n      - \\\"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\\\"\\n    relevance_to_us: \\\"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\\\"\\n    gaps: \\\"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\\\"\\n    metrics_studied: [\\\"Collapse Index\\\", \\\"persistent homology features\\\"]\\n\\n  # ============================================================\\n  # DIVERSITY METRICS (BACKGROUND)\\n  # ============================================================\\n  - id: \\\"zhu2018texygen\\\"\\n    title: \\\"Texygen: A Benchmarking Platform for Text Generation Models\\\"\\n    authors: \\\"Yaoming Zhu et al.\\\"\\n    venue: \\\"SIGIR 2018\\\"\\n    year: 2018\\n    url: \\\"https://arxiv.org/abs/1802.01886\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\\\"\\n      - \\\"成为文本生成多样性评估的标准基准之一\\\"\\n    relevance_to_us: \\\"Self-BLEU 是我们 diversity canary 的经典候选\\\"\\n    metrics_studied: [\\\"Self-BLEU\\\", \\\"BLEU\\\"]\\n\\n  - id: \\\"li2016diversity\\\"\\n    title: \\\"A Diversity-Promoting Objective Function for Neural Conversation Models\\\"\\n    authors: \\\"Jiwei Li et al.\\\"\\n    venue: \\\"NAACL 2016\\\"\\n    year: 2016\\n    url: \\\"https://arxiv.org/abs/1510.03055\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\\\"\\n      - \\\"计算 unique n-gram 数占总 n-gram 数的比例\\\"\\n    relevance_to_us: \\\"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\\\"\\n    metrics_studied: [\\\"distinct-1\\\", \\\"distinct-2\\\"]\\n\\n  # ============================================================\\n  # REPRESENTATION / SPECTRAL COLLAPSE\\n  # ============================================================\\n  - id: \\\"jing2022understanding\\\"\\n    title: \\\"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\\\"\\n    authors: \\\"Li Jing et al.\\\"\\n    venue: \\\"ICLR 2022\\\"\\n    year: 2022\\n    url: \\\"https://openreview.net/forum?id=YevsQ05DEN7\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"定义 dimensional collapse：embedding 向量只跨越低维子空间\\\"\\n      - \\\"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\\\"\\n      - \\\"strong augmentation 和 implicit regularization 驱动低秩解\\\"\\n    relevance_to_us: \\\"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\\\"\\n    metrics_studied: [\\\"effective rank\\\", \\\"singular value spectrum\\\"]\\n\\n  - id: \\\"noci2024mind\\\"\\n    title: \\\"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\\\"\\n    authors: \\\"Lorenzo Noci et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.07799\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"用 Random Matrix Theory 分析 attention 层的 rank collapse\\\"\\n      - \\\"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\\\"\\n      - \\\"rank collapse in depth: 所有 token 沿层收敛到单一表示\\\"\\n    relevance_to_us: \\\"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\\\"\\n    metrics_studied: [\\\"spectral gap\\\", \\\"singular values\\\", \\\"effective rank\\\"]\\n\\n  # ============================================================\\n  # DATA MIXING & ACCUMULATION\\n  # ============================================================\\n  - id: \\\"kazdan2025collapse\\\"\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.16713\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"系统对比 replace vs accumulate 场景\\\"\\n      - \\\"replace → collapse；accumulate → 可避免 collapse\\\"\\n      - \\\"发现 real data 和 synthetic data 之间存在非平凡的交互效应\\\"\\n      - \\\"synthetic data 的价值取决于 real data 的绝对数量\\\"\\n    relevance_to_us: \\\"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\\\"\\n    metrics_studied: [\\\"test loss\\\"]\\n\\n  - id: \\\"dey2024breaking\\\"\\n    title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n    authors: \\\"Apratim Dey, David Donoho, et al.\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2404.01413\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"替换数据 → 发散 population risk；累积数据 → 避免发散\\\"\\n      - \\\"证明累积策略在多种模型（GMM, HMM, LLM）上有效\\\"\\n    relevance_to_us: \\\"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\\\"\\n    metrics_studied: [\\\"population risk\\\"]\\n\\n  - id: \\\"epstein2024howbad\\\"\\n    title: \\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\"\\n    authors: \\\"Mohamed El Amine Epstein et al.\\\"\\n    venue: \\\"arXiv (2404.05090)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2404.05090\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"纯合成数据训练不可避免 collapse\\\"\\n      - \\\"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\\\"\\n      - \\\"递归训练使原始分布尾部消失\\\"\\n    relevance_to_us: \\\"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\\\"\\n    metrics_studied: [\\\"perplexity\\\"]\\n\\n  - id: \\\"fu2025selfconsuming\\\"\\n    title: \\\"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\\\"\\n    authors: \\\"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\\\"\\n    venue: \\\"ICLR 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2502.18865\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\\\"\\n      - \\\"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\\\"\\n      - \\\"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\\\"\\n    relevance_to_us: \\\"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\\\"\\n    gaps: \\\"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\\\"\\n    metrics_studied: [\\\"generalization bound\\\", \\\"population risk\\\"]\\n\\n  - id: \\\"bakshi2026improvement\\\"\\n    title: \\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\"\\n    authors: \\\"Soham Bakshi, Sunrit Chakraborty\\\"\\n    venue: \\\"arXiv (2602.10531)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.10531\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\\\"\\n      - \\\"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\\\"\\n      - \\\"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\\\"\\n      - \\\"在 next-token prediction 语言模型上分析完整迭代演化动态\\\"\\n    relevance_to_us: \\\"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\\\"\\n    gaps: \\\"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\\\"\\n    metrics_studied: [\\\"population risk\\\", \\\"total variation distance\\\"]\\n\\n  # ============================================================\\n  # MITIGATION & VERIFICATION\\n  # ============================================================\\n  - id: \\\"feng2025escaping\\\"\\n    title: \\\"Escaping Model Collapse via Synthetic Data Verification\\\"\\n    authors: \\\"Yunzhen Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.16657\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"通过外部 verifier（human 或 better model）注入信息可避免 collapse\\\"\\n      - \\\"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\\\"\\n      - \\\"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\\\"\\n    relevance_to_us: \\\"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\\\"\\n    metrics_studied: [\\\"test loss\\\"]\\n\\n  - id: \\\"barzilai2025consistency\\\"\\n    title: \\\"When Models Don't Collapse: On the Consistency of Iterative MLE\\\"\\n    authors: \\\"Daniel Barzilai, Ohad Shamir\\\"\\n    venue: \\\"ICML 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2505.19046\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\\\"\\n      - \\\"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\\\"\\n    relevance_to_us: \\\"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"dces2026counter\\\"\\n    title: \\\"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"MDPI Electronics (2026)\\\"\\n    year: 2026\\n    url: \\\"https://www.mdpi.com/2079-9292/15/4/869\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 DCES（dynamic center-edge sampling）数据选择框架\\\"\\n      - \\\"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\\\"\\n    relevance_to_us: \\\"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"entropy\\\"]\\n\\n  # ============================================================\\n  # POSITION / SURVEY / EPISTEMICS\\n  # ============================================================\\n  - id: \\\"schaeffer2025position\\\"\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: \\\"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\\\"\\n    venue: \\\"arXiv (2503.03150)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2503.03150\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\\\"\\n      - \\\"许多 collapse 预测依赖于与现实不符的假设\\\"\\n      - \\\"多种 collapse 场景是可以轻易避免的\\\"\\n    relevance_to_us: \\\"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"wang2025epistemic\\\"\\n    title: \\\"Epistemic Diversity and Knowledge Collapse in Large Language Models\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv (2510.04226)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.04226\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\\\"\\n      - \\\"所有模型的 epistemic diversity 低于基本 web 搜索\\\"\\n      - \\\"模型越大 epistemic diversity 反而越低；RAG 有正面效果\\\"\\n    relevance_to_us: \\\"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\\\"\\n    metrics_studied: [\\\"epistemic diversity\\\"]\\n\\n  # ============================================================\\n  # METHODOLOGY (GRANGER / LEAD-LAG)\\n  # ============================================================\\n  - id: \\\"shojaie2022granger\\\"\\n    title: \\\"Granger Causality: A Review and Recent Advances\\\"\\n    authors: \\\"Ali Shojaie, Emily B. Fox\\\"\\n    venue: \\\"Annual Review of Statistics and Its Application\\\"\\n    year: 2022\\n    url: \\\"https://arxiv.org/abs/2105.02675\\\"\\n    category: \\\"methodology\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"Granger causality 综述：从经典线性到非线性/neural 方法\\\"\\n      - \\\"Panel data 场景的 Granger causality 扩展\\\"\\n      - \\\"VAR 和 neural Granger causality 的对比\\\"\\n    relevance_to_us: \\\"为我们的 panel Granger causality 分析提供方法论基础\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"marcinkevics2022neural\\\"\\n    title: \\\"Granger Causality Using Neural Networks\\\"\\n    authors: \\\"Raphael Marcinkevics, Julia Vogt\\\"\\n    venue: \\\"arXiv (2208.03703)\\\"\\n    year: 2022\\n    url: \\\"https://arxiv.org/abs/2208.03703\\\"\\n    category: \\\"methodology\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"用 neural network 估计 Granger causality，突破线性假设\\\"\\n      - \\\"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\\\"\\n    relevance_to_us: \\\"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\\\"\\n    metrics_studied: []\\n\\ngaps:\\n  - \\\"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\\\"\\n  - \\\"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\\\"\\n  - \\\"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\\\"\\n  - \\\"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\\\"\\n  - \\\"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\\\"\\n  - \\\"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\\\"\\n  - \\\"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\\\"\\n  - \\\"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\\\"\\n\\nnovelty_assessment: |\\n  我们项目的核心 novelty 在于：\\n\\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\\n     但没有人做过系统的 lead-lag 量化分析。\\n\\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\\n     现有工作都是单一指标或最多两三个指标的孤立分析。\\n\\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\\n     但没人研究 canary 在不同 alpha 下的行为。\\n\\n  4. **与已有工作的差异**：\\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\\n       我们将类似思路迁移到 iterative collapse 场景\\n\\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\\n\", \"total_chars\": 24089, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "e811014a-e8fe-4570-b3d9-07c48fc1de54",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml\\\", \\\"content\\\": \\\"papers:\\\\n  # ============================================================\\\\n  # CORE MODEL COLLAPSE\\\\n  # ============================================================\\\\n  - id: \\\\\\\"shumailov2024curse\\\\\\\"\\\\n    title: \\\\\\\"The Curse of Recursion: Training on Generated Data Makes Models Forget\\\\\\\"\\\\n    authors: \\\\\\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\\\\\\\"\\\\n    venue: \\\\\\\"Nature\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2305.17493\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\\\\\\\"\\\\n      - \\\\\\\"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\\\\\\\"\\\\n      - \\\\\\\"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\\\\\\\"\\\\n      - \\\\\\\"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"perplexity\\\\\\\", \\\\\\\"distributional tail mass\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"alemohammad2024mad\\\\\\\"\\\\n    title: \\\\\\\"Self-Consuming Generative Models Go MAD\\\\\\\"\\\\n    authors: \\\\\\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2307.01850\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"提出 Model Autophagy Disorder (MAD) 概念\\\\\\\"\\\\n      - \\\\\\\"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\\\\\\\"\\\\n      - \\\\\\\"在图像生成领域验证 self-consuming loop 的退化效应\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"FID\\\\\\\", \\\\\\\"precision\\\\\\\", \\\\\\\"recall\\\\\\\", \\\\\\\"diversity\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"dohmatob2024tale\\\\\\\"\\\\n    title: \\\\\\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\\\\\"\\\\n    authors: \\\\\\\"Elvis Dohmatob, Yunzhen Feng, et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2402.07043\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\\\\\\\"\\\\n      - \\\\\\\"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\\\\\\\"\\\\n      - \\\\\\\"混入少量干净数据可缓解 collapse 并引发 grokking 现象\\\\\\\"\\\\n      - \\\\\\\"在 transformer 算术任务和 Llama2 文本生成上验证\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"test loss\\\\\\\", \\\\\\\"scaling exponents\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"dohmatob2025strong\\\\\\\"\\\\n    title: \\\\\\\"Strong Model Collapse\\\\\\\"\\\\n    authors: \\\\\\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2025 (Spotlight)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.04840\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"即使合成数据占比极小（1/1000），仍可导致 model collapse\\\\\\\"\\\\n      - \\\\\\\"更大的训练集并不能避免 collapse\\\\\\\"\\\\n      - \\\\\\\"更大的模型（random projection 近似下）反而可能放大 collapse\\\\\\\"\\\\n      - \\\\\\\"存在 interpolation threshold 的 double-descent 现象\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"test loss\\\\\\\", \\\\\\\"population risk\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"guo2024linguistic\\\\\\\"\\\\n    title: \\\\\\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\\\\\"\\\\n    authors: \\\\\\\"Yanzhu Guo, Guokan Shang, et al.\\\\\\\"\\\\n    venue: \\\\\\\"NAACL 2024 Findings\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2311.09807\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"evaluation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"递归微调中，linguistic diversity 在连续迭代中持续下降\\\\\\\"\\\\n      - \\\\\\\"创造性任务中 diversity 下降最显著\\\\\\\"\\\\n      - \\\\\\\"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"distinct-n\\\\\\\", \\\\\\\"type-token ratio\\\\\\\", \\\\\\\"syntactic diversity\\\\\\\", \\\\\\\"semantic diversity\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"briesch2024selfconsuming\\\\\\\"\\\\n    title: \\\\\\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\\\\\"\\\\n    authors: \\\\\\\"Martin Briesch, Dominik Sobania, Franz Rothlauf\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2311.16822)\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2311.16822\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"direct-competitor\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"首次系统研究 LLM 的 self-consuming training loop\\\\\\\"\\\\n      - \\\\\\\"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\\\\\\\"\\\\n      - \\\\\\\"expanding data cycle（累积）在 50 代内保持 diversity\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"diversity\\\\\\\", \\\\\\\"quality\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"truong2025entropy\\\\\\\"\\\\n    title: \\\\\\\"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\\\\\\\"\\\\n    authors: \\\\\\\"Truong Xuan Khanh, Truong Quynh Hoa\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2512.12381)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.12381\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"theoretical-foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\\\\\\\"\\\\n      - \\\\\\\"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\\\\\\\"\\\\n      - \\\\\\\"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\\\\\\\"\\\\n    gaps: \\\\\\\"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"entropy\\\\\\\", \\\\\\\"autocorrelation\\\\\\\", \\\\\\\"variance\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"wang2026contaminated\\\\\\\"\\\\n    title: \\\\\\\"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\\\\\\\"\\\\n    authors: \\\\\\\"Kevin Wang, Hongqian Niu, Didong Li\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2602.16065)\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.16065\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"theoretical-foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\\\\\\\"\\\\n      - \\\\\\\"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\\\\\\\"\\\\n      - \\\\\\\"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\\\\\\\"\\\\n    gaps: \\\\\\\"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"convergence rate\\\\\\\", \\\\\\\"population risk\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # CANARY / EARLY WARNING METRICS\\\\n  # ============================================================\\\\n  - id: \\\\\\\"chen2025scales\\\\\\\"\\\\n    title: \\\\\\\"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\\\\\\\"\\\\n    authors: \\\\\\\"Anonymous\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2510.05133)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.05133\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"direct-competitor\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\\\\\\\"\\\\n      - \\\\\\\"20% synthetic data 以下性能稳定，30% 以上退化加速\\\\\\\"\\\\n      - \\\\\\\"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\\\\\\\"\\\\n      - \\\\\\\"推理任务比检索任务更易退化\\\\\\\"\\\\n      - \\\\\\\"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"ECE\\\\\\\", \\\\\\\"accuracy\\\\\\\", \\\\\\\"perplexity\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"gambetta2024surplexity\\\\\\\"\\\\n    title: \\\\\\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\\\\\"\\\\n    authors: \\\\\\\"Daniele Gambetta et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2410.12341)\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.12341\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"direct-competitor\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\\\\\\\"\\\\n      - \\\\\\\"用 semantic networks 分析文本重复性和语义多样性\\\\\\\"\\\\n      - \\\\\\\"用 next-token probability 定量衡量 diversity loss\\\\\\\"\\\\n      - \\\\\\\"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\\\\\\\"\\\\n      - \\\\\\\"不需要区分 human vs AI-generated data\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"surplexity\\\\\\\", \\\\\\\"semantic network metrics\\\\\\\", \\\\\\\"next-token probability\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"qiu2025spectral\\\\\\\"\\\\n    title: \\\\\\\"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\\\\\\\"\\\\n    authors: \\\\\\\"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2510.04202)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.04202\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"method-component\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\\\\\\\"\\\\n      - \\\\\\\"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\\\\\\\"\\\\n      - \\\\\\\"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\\\\\\\"\\\\n      - \\\\\\\"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"spectral alignment\\\\\\\", \\\\\\\"weight norm\\\\\\\", \\\\\\\"gradient norm\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"he2025closer\\\\\\\"\\\\n    title: \\\\\\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\\\\\"\\\\n    authors: \\\\\\\"Shiliang He et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025 (Spotlight)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2509.16499\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"direct-competitor\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"识别 diffusion model collapse 中的 generalization → memorization 转变\\\\\\\"\\\\n      - \\\\\\\"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\\\\\\\"\\\\n      - \\\\\\\"提出基于 entropy 的数据选择策略，有效缓解 collapse\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"entropy\\\\\\\", \\\\\\\"FID\\\\\\\", \\\\\\\"diversity\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"ba2024fill\\\\\\\"\\\\n    title: \\\\\\\"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\\\\\\\"\\\\n    authors: \\\\\\\"Yang Ba, Michelle V Mancenido, Rong Pan\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.10864\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\\\\\\\"\\\\n      - \\\\\\\"推导了基于 PAC 框架的 ECE bound\\\\\\\"\\\\n      - \\\\\\\"合成数据可改善 calibration 但需精心设计生成策略\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"ECE\\\\\\\", \\\\\\\"accuracy\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"sigma2026spectral\\\\\\\"\\\\n    title: \\\\\\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\\\\\"\\\\n    authors: \\\\\\\"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2601.03385)\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.03385\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"direct-competitor\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\\\\\\\"\\\\n      - \\\\\\\"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\\\\\\\"\\\\n      - \\\\\\\"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\\\\\\\"\\\\n    gaps: \\\\\\\"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"Gram matrix eigenspectrum\\\\\\\", \\\\\\\"spectral norm bounds\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"kalinowski2026topology\\\\\\\"\\\\n    title: \\\\\\\"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\\\\\\\"\\\\n    authors: \\\\\\\"Alexander Kalinowski\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2604.26984)\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.26984\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\\\\\\\"\\\\n      - \\\\\\\"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\\\\\\\"\\\\n      - \\\\\\\"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\\\\\\\"\\\\n    gaps: \\\\\\\"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"Collapse Index\\\\\\\", \\\\\\\"persistent homology features\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # DIVERSITY METRICS (BACKGROUND)\\\\n  # ============================================================\\\\n  - id: \\\\\\\"zhu2018texygen\\\\\\\"\\\\n    title: \\\\\\\"Texygen: A Benchmarking Platform for Text Generation Models\\\\\\\"\\\\n    authors: \\\\\\\"Yaoming Zhu et al.\\\\\\\"\\\\n    venue: \\\\\\\"SIGIR 2018\\\\\\\"\\\\n    year: 2018\\\\n    url: \\\\\\\"https://arxiv.org/abs/1802.01886\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\\\\\\\"\\\\n      - \\\\\\\"成为文本生成多样性评估的标准基准之一\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"Self-BLEU 是我们 diversity canary 的经典候选\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"Self-BLEU\\\\\\\", \\\\\\\"BLEU\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"li2016diversity\\\\\\\"\\\\n    title: \\\\\\\"A Diversity-Promoting Objective Function for Neural Conversation Models\\\\\\\"\\\\n    authors: \\\\\\\"Jiwei Li et al.\\\\\\\"\\\\n    venue: \\\\\\\"NAACL 2016\\\\\\\"\\\\n    year: 2016\\\\n    url: \\\\\\\"https://arxiv.org/abs/1510.03055\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\\\\\\\"\\\\n      - \\\\\\\"计算 unique n-gram 数占总 n-gram 数的比例\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"distinct-1\\\\\\\", \\\\\\\"distinct-2\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # REPRESENTATION / SPECTRAL COLLAPSE\\\\n  # ============================================================\\\\n  - id: \\\\\\\"jing2022understanding\\\\\\\"\\\\n    title: \\\\\\\"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\\\\\\\"\\\\n    authors: \\\\\\\"Li Jing et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2022\\\\\\\"\\\\n    year: 2022\\\\n    url: \\\\\\\"https://openreview.net/forum?id=YevsQ05DEN7\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"method-component\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"定义 dimensional collapse：embedding 向量只跨越低维子空间\\\\\\\"\\\\n      - \\\\\\\"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\\\\\\\"\\\\n      - \\\\\\\"strong augmentation 和 implicit regularization 驱动低秩解\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"effective rank\\\\\\\", \\\\\\\"singular value spectrum\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"noci2024mind\\\\\\\"\\\\n    title: \\\\\\\"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\\\\\\\"\\\\n    authors: \\\\\\\"Lorenzo Noci et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.07799\\\\\\\"\\\\n    category: \\\\\\\"canary-metrics\\\\\\\"\\\\n    role: \\\\\\\"method-component\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"用 Random Matrix Theory 分析 attention 层的 rank collapse\\\\\\\"\\\\n      - \\\\\\\"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\\\\\\\"\\\\n      - \\\\\\\"rank collapse in depth: 所有 token 沿层收敛到单一表示\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"spectral gap\\\\\\\", \\\\\\\"singular values\\\\\\\", \\\\\\\"effective rank\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # DATA MIXING & ACCUMULATION\\\\n  # ============================================================\\\\n  - id: \\\\\\\"kazdan2025collapse\\\\\\\"\\\\n    title: \\\\\\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\\\\\"\\\\n    authors: \\\\\\\"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2025\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.16713\\\\\\\"\\\\n    category: \\\\\\\"data-mixing\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"系统对比 replace vs accumulate 场景\\\\\\\"\\\\n      - \\\\\\\"replace → collapse；accumulate → 可避免 collapse\\\\\\\"\\\\n      - \\\\\\\"发现 real data 和 synthetic data 之间存在非平凡的交互效应\\\\\\\"\\\\n      - \\\\\\\"synthetic data 的价值取决于 real data 的绝对数量\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"test loss\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"dey2024breaking\\\\\\\"\\\\n    title: \\\\\\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\\\\\"\\\\n    authors: \\\\\\\"Apratim Dey, David Donoho, et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2404.01413\\\\\\\"\\\\n    category: \\\\\\\"data-mixing\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"替换数据 → 发散 population risk；累积数据 → 避免发散\\\\\\\"\\\\n      - \\\\\\\"证明累积策略在多种模型（GMM, HMM, LLM）上有效\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"population risk\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"epstein2024howbad\\\\\\\"\\\\n    title: \\\\\\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\\\\\"\\\\n    authors: \\\\\\\"Mohamed El Amine Epstein et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2404.05090)\\\\\\\"\\\\n    year: 2024\\\\n    url: \\\\\\\"https://arxiv.org/abs/2404.05090\\\\\\\"\\\\n    category: \\\\\\\"data-mixing\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"纯合成数据训练不可避免 collapse\\\\\\\"\\\\n      - \\\\\\\"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\\\\\\\"\\\\n      - \\\\\\\"递归训练使原始分布尾部消失\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"perplexity\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"fu2025selfconsuming\\\\\\\"\\\\n    title: \\\\\\\"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\\\\\\\"\\\\n    authors: \\\\\\\"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2025\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2502.18865\\\\\\\"\\\\n    category: \\\\\\\"data-mixing\\\\\\\"\\\\n    role: \\\\\\\"theoretical-foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\\\\\\\"\\\\n      - \\\\\\\"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\\\\\\\"\\\\n      - \\\\\\\"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\\\\\\\"\\\\n    gaps: \\\\\\\"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"generalization bound\\\\\\\", \\\\\\\"population risk\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"bakshi2026improvement\\\\\\\"\\\\n    title: \\\\\\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\\\\\"\\\\n    authors: \\\\\\\"Soham Bakshi, Sunrit Chakraborty\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2602.10531)\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.10531\\\\\\\"\\\\n    category: \\\\\\\"data-mixing\\\\\\\"\\\\n    role: \\\\\\\"theoretical-foundation\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\\\\\\\"\\\\n      - \\\\\\\"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\\\\\\\"\\\\n      - \\\\\\\"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\\\\\\\"\\\\n      - \\\\\\\"在 next-token prediction 语言模型上分析完整迭代演化动态\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\\\\\\\"\\\\n    gaps: \\\\\\\"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"population risk\\\\\\\", \\\\\\\"total variation distance\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # MITIGATION & VERIFICATION\\\\n  # ============================================================\\\\n  - id: \\\\\\\"feng2025escaping\\\\\\\"\\\\n    title: \\\\\\\"Escaping Model Collapse via Synthetic Data Verification\\\\\\\"\\\\n    authors: \\\\\\\"Yunzhen Feng et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.16657\\\\\\\"\\\\n    category: \\\\\\\"data-mixing\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"通过外部 verifier（human 或 better model）注入信息可避免 collapse\\\\\\\"\\\\n      - \\\\\\\"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\\\\\\\"\\\\n      - \\\\\\\"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"test loss\\\\\\\"]\\\\n\\\\n  - id: \\\\\\\"barzilai2025consistency\\\\\\\"\\\\n    title: \\\\\\\"When Models Don't Collapse: On the Consistency of Iterative MLE\\\\\\\"\\\\n    authors: \\\\\\\"Daniel Barzilai, Ohad Shamir\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2025\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2505.19046\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\\\\\\\"\\\\n      - \\\\\\\"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\\\\\\\"\\\\n    metrics_studied: []\\\\n\\\\n  - id: \\\\\\\"dces2026counter\\\\\\\"\\\\n    title: \\\\\\\"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\\\\\\\"\\\\n    authors: \\\\\\\"Anonymous\\\\\\\"\\\\n    venue: \\\\\\\"MDPI Electronics (2026)\\\\\\\"\\\\n    year: 2026\\\\n    url: \\\\\\\"https://www.mdpi.com/2079-9292/15/4/869\\\\\\\"\\\\n    category: \\\\\\\"data-mixing\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"提出 DCES（dynamic center-edge sampling）数据选择框架\\\\\\\"\\\\n      - \\\\\\\"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"ECE\\\\\\\", \\\\\\\"entropy\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # POSITION / SURVEY / EPISTEMICS\\\\n  # ============================================================\\\\n  - id: \\\\\\\"schaeffer2025position\\\\\\\"\\\\n    title: \\\\\\\"Position: Model Collapse Does Not Mean What You Think\\\\\\\"\\\\n    authors: \\\\\\\"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2503.03150)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2503.03150\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\\\\\\\"\\\\n      - \\\\\\\"许多 collapse 预测依赖于与现实不符的假设\\\\\\\"\\\\n      - \\\\\\\"多种 collapse 场景是可以轻易避免的\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\\\\\\\"\\\\n    metrics_studied: []\\\\n\\\\n  - id: \\\\\\\"wang2025epistemic\\\\\\\"\\\\n    title: \\\\\\\"Epistemic Diversity and Knowledge Collapse in Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Wang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2510.04226)\\\\\\\"\\\\n    year: 2025\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.04226\\\\\\\"\\\\n    category: \\\\\\\"core-collapse\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\\\\\\\"\\\\n      - \\\\\\\"所有模型的 epistemic diversity 低于基本 web 搜索\\\\\\\"\\\\n      - \\\\\\\"模型越大 epistemic diversity 反而越低；RAG 有正面效果\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\\\\\\\"\\\\n    metrics_studied: [\\\\\\\"epistemic diversity\\\\\\\"]\\\\n\\\\n  # ============================================================\\\\n  # METHODOLOGY (GRANGER / LEAD-LAG)\\\\n  # ============================================================\\\\n  - id: \\\\\\\"shojaie2022granger\\\\\\\"\\\\n    title: \\\\\\\"Granger Causality: A Review and Recent Advances\\\\\\\"\\\\n    authors: \\\\\\\"Ali Shojaie, Emily B. Fox\\\\\\\"\\\\n    venue: \\\\\\\"Annual Review of Statistics and Its Application\\\\\\\"\\\\n    year: 2022\\\\n    url: \\\\\\\"https://arxiv.org/abs/2105.02675\\\\\\\"\\\\n    category: \\\\\\\"methodology\\\\\\\"\\\\n    role: \\\\\\\"method-component\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"Granger causality 综述：从经典线性到非线性/neural 方法\\\\\\\"\\\\n      - \\\\\\\"Panel data 场景的 Granger causality 扩展\\\\\\\"\\\\n      - \\\\\\\"VAR 和 neural Granger causality 的对比\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"为我们的 panel Granger causality 分析提供方法论基础\\\\\\\"\\\\n    metrics_studied: []\\\\n\\\\n  - id: \\\\\\\"marcinkevics2022neural\\\\\\\"\\\\n    title: \\\\\\\"Granger Causality Using Neural Networks\\\\\\\"\\\\n    authors: \\\\\\\"Raphael Marcinkevics, Julia Vogt\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (2208.03703)\\\\\\\"\\\\n    year: 2022\\\\n    url: \\\\\\\"https://arxiv.org/abs/2208.03703\\\\\\\"\\\\n    category: \\\\\\\"methodology\\\\\\\"\\\\n    role: \\\\\\\"method-component\\\\\\\"\\\\n    key_findings:\\\\n      - \\\\\\\"用 neural network 估计 Granger causality，突破线性假设\\\\\\\"\\\\n      - \\\\\\\"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\\\\\\\"\\\\n    relevance_to_us: \\\\\\\"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\\\\\\\"\\\\n    metrics_studied: []\\\\n\\\\ngaps:\\\\n  - \\\\\\\"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\\\\\\\"\\\\n  - \\\\\\\"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\\\\\\\"\\\\n  - \\\\\\\"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\\\\\\\"\\\\n  - \\\\\\\"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\\\\\\\"\\\\n  - \\\\\\\"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\\\\\\\"\\\\n  - \\\\\\\"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\\\\\\\"\\\\n  - \\\\\\\"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\\\\\\\"\\\\n  - \\\\\\\"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\\\\\\\"\\\\n\\\\nnovelty_assessment: |\\\\n  我们项目的核心 novelty 在于：\\\\n\\\\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\\\\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\\\\n     但没有人做过系统的 lead-lag 量化分析。\\\\n\\\\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\\\\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\\\\n     现有工作都是单一指标或最多两三个指标的孤立分析。\\\\n\\\\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\\\\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\\\\n     但没人研究 canary 在不同 alpha 下的行为。\\\\n\\\\n  4. **与已有工作的差异**：\\\\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\\\\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\\\\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\\\\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\\\\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\\\\n       我们将类似思路迁移到 iterative collapse 场景\\\\n\\\\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\\\\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\\\\n\\\", \\\"total_chars\\\": 24089, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # CORE MODEL COLLAPSE\\n  # ============================================================\\n  - id: \\\"shumailov2024curse\\\"\\n    title: \\\"The Curse of Recursion: Training on Generated Data Makes Models Forget\\\"\\n    authors: \\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\\\"\\n    venue: \\\"Nature\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2305.17493\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\\\"\\n      - \\\"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\\\"\\n      - \\\"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\\\"\\n      - \\\"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\\\"\\n    relevance_to_us: \\\"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\\\"\\n    metrics_studied: [\\\"perplexity\\\", \\\"distributional tail mass\\\"]\\n\\n  - id: \\\"alemohammad2024mad\\\"\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2307.01850\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"提出 Model Autophagy Disorder (MAD) 概念\\\"\\n      - \\\"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\\\"\\n      - \\\"在图像生成领域验证 self-consuming loop 的退化效应\\\"\\n    relevance_to_us: \\\"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\\\"\\n    metrics_studied: [\\\"FID\\\", \\\"precision\\\", \\\"recall\\\", \\\"diversity\\\"]\\n\\n  - id: \\\"dohmatob2024tale\\\"\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Elvis Dohmatob, Yunzhen Feng, et al.\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2402.07043\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\\\"\\n      - \\\"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\\\"\\n      - \\\"混入少量干净数据可缓解 collapse 并引发 grokking 现象\\\"\\n      - \\\"在 transformer 算术任务和 Llama2 文本生成上验证\\\"\\n    relevance_to_us: \\\"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\\\"\\n    metrics_studied: [\\\"test loss\\\", \\\"scaling exponents\\\"]\\n\\n  - id: \\\"dohmatob2025strong\\\"\\n    title: \\\"Strong Model Collapse\\\"\\n    authors: \\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\"\\n    venue: \\\"ICLR 2025 (Spotlight)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.04840\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"即使合成数据占比极小（1/1000），仍可导致 model collapse\\\"\\n      - \\\"更大的训练集并不能避免 collapse\\\"\\n      - \\\"更大的模型（random projection 近似下）反而可能放大 collapse\\\"\\n      - \\\"存在 interpolation threshold 的 double-descent 现象\\\"\\n    relevance_to_us: \\\"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\\\"\\n    metrics_studied: [\\\"test loss\\\", \\\"population risk\\\"]\\n\\n  - id: \\\"guo2024linguistic\\\"\\n    title: \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\"\\n    authors: \\\"Yanzhu Guo, Guokan Shang, et al.\\\"\\n    venue: \\\"NAACL 2024 Findings\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2311.09807\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"evaluation\\\"\\n    key_findings:\\n      - \\\"递归微调中，linguistic diversity 在连续迭代中持续下降\\\"\\n      - \\\"创造性任务中 diversity 下降最显著\\\"\\n      - \\\"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\\\"\\n    relevance_to_us: \\\"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\\\"\\n    metrics_studied: [\\\"distinct-n\\\", \\\"type-token ratio\\\", \\\"syntactic diversity\\\", \\\"semantic diversity\\\"]\\n\\n  - id: \\\"briesch2024selfconsuming\\\"\\n    title: \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\"\\n    authors: \\\"Martin Briesch, Dominik Sobania, Franz Rothlauf\\\"\\n    venue: \\\"arXiv (2311.16822)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2311.16822\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"首次系统研究 LLM 的 self-consuming training loop\\\"\\n      - \\\"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\\\"\\n      - \\\"expanding data cycle（累积）在 50 代内保持 diversity\\\"\\n    relevance_to_us: \\\"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\\\"\\n    metrics_studied: [\\\"diversity\\\", \\\"quality\\\"]\\n\\n  - id: \\\"truong2025entropy\\\"\\n    title: \\\"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\\\"\\n    authors: \\\"Truong Xuan Khanh, Truong Quynh Hoa\\\"\\n    venue: \\\"arXiv (2512.12381)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2512.12381\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\\\"\\n      - \\\"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\\\"\\n      - \\\"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\\\"\\n    relevance_to_us: \\\"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\\\"\\n    gaps: \\\"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\\\"\\n    metrics_studied: [\\\"entropy\\\", \\\"autocorrelation\\\", \\\"variance\\\"]\\n\\n  - id: \\\"wang2026contaminated\\\"\\n    title: \\\"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\\\"\\n    authors: \\\"Kevin Wang, Hongqian Niu, Didong Li\\\"\\n    venue: \\\"arXiv (2602.16065)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.16065\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\\\"\\n      - \\\"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\\\"\\n      - \\\"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\\\"\\n    relevance_to_us: \\\"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\\\"\\n    gaps: \\\"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\\\"\\n    metrics_studied: [\\\"convergence rate\\\", \\\"population risk\\\"]\\n\\n  # ============================================================\\n  # CANARY / EARLY WARNING METRICS\\n  # ============================================================\\n  - id: \\\"chen2025scales\\\"\\n    title: \\\"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"arXiv (2510.05133)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.05133\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\\\"\\n      - \\\"20% synthetic data 以下性能稳定，30% 以上退化加速\\\"\\n      - \\\"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\\\"\\n      - \\\"推理任务比检索任务更易退化\\\"\\n      - \\\"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\\\"\\n    relevance_to_us: \\\"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"accuracy\\\", \\\"perplexity\\\"]\\n\\n  - id: \\\"gambetta2024surplexity\\\"\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\"\\n    authors: \\\"Daniele Gambetta et al.\\\"\\n    venue: \\\"arXiv (2410.12341)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.12341\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\\\"\\n      - \\\"用 semantic networks 分析文本重复性和语义多样性\\\"\\n      - \\\"用 next-token probability 定量衡量 diversity loss\\\"\\n      - \\\"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\\\"\\n      - \\\"不需要区分 human vs AI-generated data\\\"\\n    relevance_to_us: \\\"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\\\"\\n    metrics_studied: [\\\"surplexity\\\", \\\"semantic network metrics\\\", \\\"next-token probability\\\"]\\n\\n  - id: \\\"qiu2025spectral\\\"\\n    title: \\\"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\\\"\\n    authors: \\\"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\\\"\\n    venue: \\\"arXiv (2510.04202)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.04202\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\\\"\\n      - \\\"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\\\"\\n      - \\\"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\\\"\\n      - \\\"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\\\"\\n    relevance_to_us: \\\"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\\\"\\n    metrics_studied: [\\\"spectral alignment\\\", \\\"weight norm\\\", \\\"gradient norm\\\"]\\n\\n  - id: \\\"he2025closer\\\"\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: \\\"Shiliang He et al.\\\"\\n    venue: \\\"NeurIPS 2025 (Spotlight)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2509.16499\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"识别 diffusion model collapse 中的 generalization → memorization 转变\\\"\\n      - \\\"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\\\"\\n      - \\\"提出基于 entropy 的数据选择策略，有效缓解 collapse\\\"\\n    relevance_to_us: \\\"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\\\"\\n    metrics_studied: [\\\"entropy\\\", \\\"FID\\\", \\\"diversity\\\"]\\n\\n  - id: \\\"ba2024fill\\\"\\n    title: \\\"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\\\"\\n    authors: \\\"Yang Ba, Michelle V Mancenido, Rong Pan\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.10864\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\\\"\\n      - \\\"推导了基于 PAC 框架的 ECE bound\\\"\\n      - \\\"合成数据可改善 calibration 但需精心设计生成策略\\\"\\n    relevance_to_us: \\\"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"accuracy\\\"]\\n\\n  - id: \\\"sigma2026spectral\\\"\\n    title: \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\"\\n    authors: \\\"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\\\"\\n    venue: \\\"arXiv (2601.03385)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2601.03385\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\\\"\\n      - \\\"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\\\"\\n      - \\\"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\\\"\\n    relevance_to_us: \\\"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\\\"\\n    gaps: \\\"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\\\"\\n    metrics_studied: [\\\"Gram matrix eigenspectrum\\\", \\\"spectral norm bounds\\\"]\\n\\n  - id: \\\"kalinowski2026topology\\\"\\n    title: \\\"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\\\"\\n    authors: \\\"Alexander Kalinowski\\\"\\n    venue: \\\"arXiv (2604.26984)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2604.26984\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\\\"\\n      - \\\"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\\\"\\n      - \\\"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\\\"\\n    relevance_to_us: \\\"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\\\"\\n    gaps: \\\"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\\\"\\n    metrics_studied: [\\\"Collapse Index\\\", \\\"persistent homology features\\\"]\\n\\n  # ============================================================\\n  # DIVERSITY METRICS (BACKGROUND)\\n  # ============================================================\\n  - id: \\\"zhu2018texygen\\\"\\n    title: \\\"Texygen: A Benchmarking Platform for Text Generation Models\\\"\\n    authors: \\\"Yaoming Zhu et al.\\\"\\n    venue: \\\"SIGIR 2018\\\"\\n    year: 2018\\n    url: \\\"https://arxiv.org/abs/1802.01886\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\\\"\\n      - \\\"成为文本生成多样性评估的标准基准之一\\\"\\n    relevance_to_us: \\\"Self-BLEU 是我们 diversity canary 的经典候选\\\"\\n    metrics_studied: [\\\"Self-BLEU\\\", \\\"BLEU\\\"]\\n\\n  - id: \\\"li2016diversity\\\"\\n    title: \\\"A Diversity-Promoting Objective Function for Neural Conversation Models\\\"\\n    authors: \\\"Jiwei Li et al.\\\"\\n    venue: \\\"NAACL 2016\\\"\\n    year: 2016\\n    url: \\\"https://arxiv.org/abs/1510.03055\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\\\"\\n      - \\\"计算 unique n-gram 数占总 n-gram 数的比例\\\"\\n    relevance_to_us: \\\"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\\\"\\n    metrics_studied: [\\\"distinct-1\\\", \\\"distinct-2\\\"]\\n\\n  # ============================================================\\n  # REPRESENTATION / SPECTRAL COLLAPSE\\n  # ============================================================\\n  - id: \\\"jing2022understanding\\\"\\n    title: \\\"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\\\"\\n    authors: \\\"Li Jing et al.\\\"\\n    venue: \\\"ICLR 2022\\\"\\n    year: 2022\\n    url: \\\"https://openreview.net/forum?id=YevsQ05DEN7\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"定义 dimensional collapse：embedding 向量只跨越低维子空间\\\"\\n      - \\\"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\\\"\\n      - \\\"strong augmentation 和 implicit regularization 驱动低秩解\\\"\\n    relevance_to_us: \\\"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\\\"\\n    metrics_studied: [\\\"effective rank\\\", \\\"singular value spectrum\\\"]\\n\\n  - id: \\\"noci2024mind\\\"\\n    title: \\\"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\\\"\\n    authors: \\\"Lorenzo Noci et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.07799\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"用 Random Matrix Theory 分析 attention 层的 rank collapse\\\"\\n      - \\\"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\\\"\\n      - \\\"rank collapse in depth: 所有 token 沿层收敛到单一表示\\\"\\n    relevance_to_us: \\\"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\\\"\\n    metrics_studied: [\\\"spectral gap\\\", \\\"singular values\\\", \\\"effective rank\\\"]\\n\\n  # ============================================================\\n  # DATA MIXING & ACCUMULATION\\n  # ============================================================\\n  - id: \\\"kazdan2025collapse\\\"\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.16713\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"系统对比 replace vs accumulate 场景\\\"\\n      - \\\"replace → collapse；accumulate → 可避免 collapse\\\"\\n      - \\\"发现 real data 和 synthetic data 之间存在非平凡的交互效应\\\"\\n      - \\\"synthetic data 的价值取决于 real data 的绝对数量\\\"\\n    relevance_to_us: \\\"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\\\"\\n    metrics_studied: [\\\"test loss\\\"]\\n\\n  - id: \\\"dey2024breaking\\\"\\n    title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n    authors: \\\"Apratim Dey, David Donoho, et al.\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2404.01413\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"替换数据 → 发散 population risk；累积数据 → 避免发散\\\"\\n      - \\\"证明累积策略在多种模型（GMM, HMM, LLM）上有效\\\"\\n    relevance_to_us: \\\"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\\\"\\n    metrics_studied: [\\\"population risk\\\"]\\n\\n  - id: \\\"epstein2024howbad\\\"\\n    title: \\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\"\\n    authors: \\\"Mohamed El Amine Epstein et al.\\\"\\n    venue: \\\"arXiv (2404.05090)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2404.05090\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"纯合成数据训练不可避免 collapse\\\"\\n      - \\\"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\\\"\\n      - \\\"递归训练使原始分布尾部消失\\\"\\n    relevance_to_us: \\\"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\\\"\\n    metrics_studied: [\\\"perplexity\\\"]\\n\\n  - id: \\\"fu2025selfconsuming\\\"\\n    title: \\\"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\\\"\\n    authors: \\\"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\\\"\\n    venue: \\\"ICLR 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2502.18865\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\\\"\\n      - \\\"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\\\"\\n      - \\\"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\\\"\\n    relevance_to_us: \\\"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\\\"\\n    gaps: \\\"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\\\"\\n    metrics_studied: [\\\"generalization bound\\\", \\\"population risk\\\"]\\n\\n  - id: \\\"bakshi2026improvement\\\"\\n    title: \\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\"\\n    authors: \\\"Soham Bakshi, Sunrit Chakraborty\\\"\\n    venue: \\\"arXiv (2602.10531)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.10531\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\\\"\\n      - \\\"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\\\"\\n      - \\\"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\\\"\\n      - \\\"在 next-token prediction 语言模型上分析完整迭代演化动态\\\"\\n    relevance_to_us: \\\"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\\\"\\n    gaps: \\\"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\\\"\\n    metrics_studied: [\\\"population risk\\\", \\\"total variation distance\\\"]\\n\\n  # ============================================================\\n  # MITIGATION & VERIFICATION\\n  # ============================================================\\n  - id: \\\"feng2025escaping\\\"\\n    title: \\\"Escaping Model Collapse via Synthetic Data Verification\\\"\\n    authors: \\\"Yunzhen Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.16657\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"通过外部 verifier（human 或 better model）注入信息可避免 collapse\\\"\\n      - \\\"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\\\"\\n      - \\\"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\\\"\\n    relevance_to_us: \\\"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\\\"\\n    metrics_studied: [\\\"test loss\\\"]\\n\\n  - id: \\\"barzilai2025consistency\\\"\\n    title: \\\"When Models Don't Collapse: On the Consistency of Iterative MLE\\\"\\n    authors: \\\"Daniel Barzilai, Ohad Shamir\\\"\\n    venue: \\\"ICML 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2505.19046\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\\\"\\n      - \\\"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\\\"\\n    relevance_to_us: \\\"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"dces2026counter\\\"\\n    title: \\\"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"MDPI Electronics (2026)\\\"\\n    year: 2026\\n    url: \\\"https://www.mdpi.com/2079-9292/15/4/869\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 DCES（dynamic center-edge sampling）数据选择框架\\\"\\n      - \\\"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\\\"\\n    relevance_to_us: \\\"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"entropy\\\"]\\n\\n  # ============================================================\\n  # POSITION / SURVEY / EPISTEMICS\\n  # ============================================================\\n  - id: \\\"schaeffer2025position\\\"\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: \\\"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\\\"\\n    venue: \\\"arXiv (2503.03150)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2503.03150\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\\\"\\n      - \\\"许多 collapse 预测依赖于与现实不符的假设\\\"\\n      - \\\"多种 collapse 场景是可以轻易避免的\\\"\\n    relevance_to_us: \\\"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"wang2025epistemic\\\"\\n    title: \\\"Epistemic Diversity and Knowledge Collapse in Large Language Models\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv (2510.04226)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.04226\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\\\"\\n      - \\\"所有模型的 epistemic diversity 低于基本 web 搜索\\\"\\n      - \\\"模型越大 epistemic diversity 反而越低；RAG 有正面效果\\\"\\n    relevance_to_us: \\\"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\\\"\\n    metrics_studied: [\\\"epistemic diversity\\\"]\\n\\n  # ============================================================\\n  # METHODOLOGY (GRANGER / LEAD-LAG)\\n  # ============================================================\\n  - id: \\\"shojaie2022granger\\\"\\n    title: \\\"Granger Causality: A Review and Recent Advances\\\"\\n    authors: \\\"Ali Shojaie, Emily B. Fox\\\"\\n    venue: \\\"Annual Review of Statistics and Its Application\\\"\\n    year: 2022\\n    url: \\\"https://arxiv.org/abs/2105.02675\\\"\\n    category: \\\"methodology\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"Granger causality 综述：从经典线性到非线性/neural 方法\\\"\\n      - \\\"Panel data 场景的 Granger causality 扩展\\\"\\n      - \\\"VAR 和 neural Granger causality 的对比\\\"\\n    relevance_to_us: \\\"为我们的 panel Granger causality 分析提供方法论基础\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"marcinkevics2022neural\\\"\\n    title: \\\"Granger Causality Using Neural Networks\\\"\\n    authors: \\\"Raphael Marcinkevics, Julia Vogt\\\"\\n    venue: \\\"arXiv (2208.03703)\\\"\\n    year: 2022\\n    url: \\\"https://arxiv.org/abs/2208.03703\\\"\\n    category: \\\"methodology\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"用 neural network 估计 Granger causality，突破线性假设\\\"\\n      - \\\"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\\\"\\n    relevance_to_us: \\\"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\\\"\\n    metrics_studied: []\\n\\ngaps:\\n  - \\\"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\\\"\\n  - \\\"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\\\"\\n  - \\\"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\\\"\\n  - \\\"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\\\"\\n  - \\\"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\\\"\\n  - \\\"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\\\"\\n  - \\\"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\\\"\\n  - \\\"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\\\"\\n\\nnovelty_assessment: |\\n  我们项目的核心 novelty 在于：\\n\\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\\n     但没有人做过系统的 lead-lag 量化分析。\\n\\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\\n     现有工作都是单一指标或最多两三个指标的孤立分析。\\n\\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\\n     但没人研究 canary 在不同 alpha 下的行为。\\n\\n  4. **与已有工作的差异**：\\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\\n       我们将类似思路迁移到 iterative collapse 场景\\n\\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\\n\", \"total_chars\": 24089, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now I have both files. Let me extract the information for the 5 papers from memory.md and prepare the literature_map.yaml update.

From memory.md (under "2026-05-15 文献扫描"):

1. **Du & Tanaka-Ishii (2605.00435)** — "Escaping Mode Collapse in LLM Generation via Geometric Regulation" [May 1, 2026]
   - Geometric collapse in representation space, RMR method
   - Relation: orthogonal — inference-time mode collapse, not iterative training
   - Connection to effective rank concept
   
2. **Gauthier, Bach & Jordan (2605.04266)** — "Explaining and Preventing Alignment Collapse in Iterative RLHF" [May 5, 2026]
   - Iterative RLHF alignment collapse, Stackelberg game, FPO
   - Relation: complementary — feedback loop structure mirrors our iterative synthetic training approach
   - Role MUST be "complementary"

3. **Shi et al. (2605.07271)** — "Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions" [May 2026]
   - Layer pruning effects on performance, decision representation shifts across training phases
   - Relation: orthogonal — architecture-specific collapse mechanism

4. **Tübingen AI Center et al. (2605.06366)** — "Layer Collapse in Diffusion Language Models" [May 11, 2026]
   - Layer activation collapse in diffusion-based LMs, super-outlier phenomena
   - Relation: orthogonal — different architectural paradigm

5. **Bergsma et al. (2509.25087, rev. Mar 2026)** — "Scaling with Collapse: Efficient and Predictable Training of LLM Families" [Cerebras]
   - Loss curve normalization patterns and deviation-from-collapse as a training diagnostic
   - Relation: orthogonal — addresses scaling dynamics rather than model failure

Now I'm working through how to categorize these papers and assign their roles relative to my framework.

Looking at the available categories—core-collapse, canary-metrics, data-mixing, methodology—and roles like foundation, direct-competitor, complementary, evaluation, background, theoretical-foundation, and method-component, I need to map each paper. Du & Tanaka-Ishii fits as background under core-collapse since it's conceptually adjacent through effective rank. Gauthier et al. belongs in core-collapse as complementary given the iterative alignment dynamics. Shi et al. also maps to core-collapse but as background since the pruning collapse is orthogonal. For Tübingen, I'm considering whether the diffusion-specific layer collapse warrants its own treatment or fits as background in core-collapse.

Now I'm deciding where Bergsma et al. belongs—their deviation-from-collapse metric could serve as a canary-metrics entry since it functions as a monitoring signal, though the "collapse" terminology differs from the core-collapse papers. I'll construct the YAML entries carefully to maintain proper formatting and logical grouping. I'm organizing where each paper belongs in the YAML structure. The first four papers fit naturally in the core model collapse section, while Bergsma et al. belongs in the canary metrics section since it's about monitoring signals during training rather than collapse itself. Now I'll construct the complete file content with all five papers inserted at their appropriate positions. I need to construct the YAML file strategically by reading the current structure and inserting the new papers in their appropriate sections—core collapse papers go into the core-collapse category, while the Bergsma et al. paper on scaling laws fits better as a canary metric since it's about using deviation as a diagnostic signal. I'm working through the citation IDs for the new papers I need to add, following the author-year-keyword pattern. I've identified five entries to insert at specific points in the bibliography, and now I need to construct the full YAML content and save it back to the file.

Adding YAML entries... 我看到这篇论文讨论迭代 RLHF 中的对齐崩溃问题——policy 通过反馈环路系统性地利用 reward model 的盲区，他们用 Stackelberg 博弈建模并提出了前瞻性策略优化方法。这与我们项目中迭代合成数据的反馈环路有直接关联，可以作为补充参考来理解迭代过程中的崩溃机制。

接下来还有关于层剪枝导致性能崩溃的研究...

这篇论文定义了两个关键阶段：Silent Phase 是模型预测被单一选项主导的分布崩溃，Decisive Phase 则是之后的阶段。有趣的是，在 Silent Phase 进行剪枝会立即触发崩溃。这与我们用 token entropy 下降来检测的现象本质上是一样的——都是预测分布退化为单峰的表现，只是从不同角度观察。还有一篇关于扩散语言模型中层崩溃的论文也在相关范围内。

它发现 LLaDA-8B 中少数早期层的激活被超级异常值主导，移除这个异常值会导致模型输出退化为重复的随机 token。虽然这是架构层面的崩溃而非数据驱动的，但激活崩溃的表征与谱崩溃有重叠。现在我看到一篇新的论文在讨论 LLM 族群的可扩展训练。

这篇论文用"崩溃"指的是损失曲线在归一化后坍缩到通用轨迹，并用偏离这个轨迹作为训练病理的早期诊断信号。这与我们的 canary 理念相似——都是从时序异常检测的角度来监控模型训练状态。

现在我需要把这个新条目和其他四篇核心论文插入到 YAML 文件的正确位置。我会在 wang2026contaminated 条目之后、canary 指标部分之前添加这些论文，然后在 kalinowski2026topology 之后、多样性指标部分之前添加 bergsma 条目。

Constructing the full YAML file... I need to find the exact locations in the YAML file where I should insert the new entries. I'm looking for the end of the wang2026contaminated entry and the kalinowski2026topology entry, then I'll use the file editing tool to insert the new content at those specific points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "783b3ed4-ae39-4209-b56d-e46135e035a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016guF5bS3kjHt6qX3ct79km",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18106,
      "cache_read_input_tokens": 24056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18106
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 13_

读取到两个文件。现在定位插入点并添加 5 篇新论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "d0bb5b14-e3b9-42b6-9980-352ca4e6514c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016guF5bS3kjHt6qX3ct79km",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18106,
      "cache_read_input_tokens": 24056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18106
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01QaNraJx6A3bQd7DXUs9y6K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "5050c034-0cda-4f2a-840e-220a7a22abcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016guF5bS3kjHt6qX3ct79km",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18106,
      "cache_read_input_tokens": 24056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18106
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T04:46:49.044Z_

<details><summary>↩ Tool result · `toolu_01QaNraJx6A3bQd7DXUs9y6K`</summary>

```text
1	papers:
2	  # ============================================================
3	  # CORE MODEL COLLAPSE
4	  # ============================================================
5	  - id: "shumailov2024curse"
6	    title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
7	    authors: "Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson"
8	    venue: "Nature"
9	    year: 2024
10	    url: "https://arxiv.org/abs/2305.17493"
11	    category: "core-collapse"
12	    role: "foundation"
13	    key_findings:
14	      - "定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失"
15	      - "区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）"
16	      - "三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合"
17	      - "在 VAE、GMM、LLM 上均验证了 collapse 的普遍性"
18	    relevance_to_us: "奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段"
19	    metrics_studied: ["perplexity", "distributional tail mass"]
20	
21	  - id: "alemohammad2024mad"
22	    title: "Self-Consuming Generative Models Go MAD"
23	    authors: "Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk"
24	    venue: "ICLR 2024"
25	    year: 2024
26	    url: "https://arxiv.org/abs/2307.01850"
27	    category: "core-collapse"
28	    role: "foundation"
29	    key_findings:
30	      - "提出 Model Autophagy Disorder (MAD) 概念"
31	      - "autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降"
32	      - "在图像生成领域验证 self-consuming loop 的退化效应"
33	    relevance_to_us: "MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上"
34	    metrics_studied: ["FID", "precision", "recall", "diversity"]
35	
36	  - id: "dohmatob2024tale"
37	    title: "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
38	    authors: "Elvis Dohmatob, Yunzhen Feng, et al."
39	    venue: "ICML 2024"
40	    year: 2024
41	    url: "https://arxiv.org/abs/2402.07043"
42	    category: "core-collapse"
43	    role: "foundation"
44	    key_findings:
45	      - "通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化"
46	      - "发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式"
47	      - "混入少量干净数据可缓解 collapse 并引发 grokking 现象"
48	      - "在 transformer 算术任务和 Llama2 文本生成上验证"
49	    relevance_to_us: "scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为"
50	    metrics_studied: ["test loss", "scaling exponents"]
51	
52	  - id: "dohmatob2025strong"
53	    title: "Strong Model Collapse"
54	    authors: "Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe"
55	    venue: "ICLR 2025 (Spotlight)"
56	    year: 2025
57	    url: "https://arxiv.org/abs/2410.04840"
58	    category: "core-collapse"
59	    role: "foundation"
60	    key_findings:
61	      - "即使合成数据占比极小（1/1000），仍可导致 model collapse"
62	      - "更大的训练集并不能避免 collapse"
63	      - "更大的模型（random projection 近似下）反而可能放大 collapse"
64	      - "存在 interpolation threshold 的 double-descent 现象"
65	    relevance_to_us: "强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感"
66	    metrics_studied: ["test loss", "population risk"]
67	
68	  - id: "guo2024linguistic"
69	    title: "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text"
70	    authors: "Yanzhu Guo, Guokan Shang, et al."
71	    venue: "NAACL 2024 Findings"
72	    year: 2024
73	    url: "https://arxiv.org/abs/2311.09807"
74	    category: "core-collapse"
75	    role: "evaluation"
76	    key_findings:
77	      - "递归微调中，linguistic diversity 在连续迭代中持续下降"
78	      - "创造性任务中 diversity 下降最显著"
79	      - "开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系"
80	    relevance_to_us: "其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度"
81	    metrics_studied: ["distinct-n", "type-token ratio", "syntactic diversity", "semantic diversity"]
82	
83	  - id: "briesch2024selfconsuming"
84	    title: "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop"
85	    authors: "Martin Briesch, Dominik Sobania, Franz Rothlauf"
86	    venue: "arXiv (2311.16822)"
87	    year: 2024
88	    url: "https://arxiv.org/abs/2311.16822"
89	    category: "core-collapse"
90	    role: "direct-competitor"
91	    key_findings:
92	      - "首次系统研究 LLM 的 self-consuming training loop"
93	      - "full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降"
94	      - "expanding data cycle（累积）在 50 代内保持 diversity"
95	    relevance_to_us: "其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置"
96	    metrics_studied: ["diversity", "quality"]
97	
98	  - id: "truong2025entropy"
99	    title: "Entropy Collapse: A Universal Failure Mode of Intelligent Systems"
100	    authors: "Truong Xuan Khanh, Truong Quynh Hoa"
101	    venue: "arXiv (2512.12381)"
102	    year: 2025
103	    url: "https://arxiv.org/abs/2512.12381"
104	    category: "core-collapse"
105	    role: "theoretical-foundation"
106	    key_findings:
107	      - "证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats"
108	      - "两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2"
109	      - "因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警"
110	    relevance_to_us: "定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效"
111	    gaps: "理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力"
112	    metrics_studied: ["entropy", "autocorrelation", "variance"]
113	
114	  - id: "wang2026contaminated"
115	    title: "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training"
116	    authors: "Kevin Wang, Hongqian Niu, Didong Li"
117	    venue: "arXiv (2602.16065)"
118	    year: 2026
119	    url: "https://arxiv.org/abs/2602.16065"
120	    category: "core-collapse"
121	    role: "theoretical-foundation"
122	    key_findings:
123	      - "首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛"
124	      - "收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈"
125	      - "突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布"
126	    relevance_to_us: "为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率"
127	    gaps: "universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为"
128	    metrics_studied: ["convergence rate", "population risk"]
129	
130	  # ============================================================
131	  # CANARY / EARLY WARNING METRICS
132	  # ============================================================
133	  - id: "chen2025scales"
134	    title: "Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios"
135	    authors: "Anonymous"
136	    venue: "arXiv (2510.05133)"
137	    year: 2025
138	    url: "https://arxiv.org/abs/2510.05133"
139	    category: "canary-metrics"
140	    role: "direct-competitor"
141	    key_findings:
142	      - "**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal"
143	      - "20% synthetic data 以下性能稳定，30% 以上退化加速"
144	      - "大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒"
145	      - "推理任务比检索任务更易退化"
146	      - "iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）"
147	    relevance_to_us: "**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架"
148	    metrics_studied: ["ECE", "accuracy", "perplexity"]
149	
150	  - id: "gambetta2024surplexity"
151	    title: "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI"
152	    authors: "Daniele Gambetta et al."
153	    venue: "arXiv (2410.12341)"
154	    year: 2024
155	    url: "https://arxiv.org/abs/2410.12341"
156	    category: "canary-metrics"
157	    role: "direct-competitor"
158	    key_findings:
159	      - "提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据"
160	      - "用 semantic networks 分析文本重复性和语义多样性"
161	      - "用 next-token probability 定量衡量 diversity loss"
162	      - "高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜"
163	      - "不需要区分 human vs AI-generated data"
164	    relevance_to_us: "surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角"
165	    metrics_studied: ["surplexity", "semantic network metrics", "next-token probability"]
166	
167	  - id: "qiu2025spectral"
168	    title: "Spectral Alignment as Predictor of Loss Explosion in Neural Network Training"
169	    authors: "Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao"
170	    venue: "arXiv (2510.04202)"
171	    year: 2025
172	    url: "https://arxiv.org/abs/2510.04202"
173	    category: "canary-metrics"
174	    role: "method-component"
175	    key_findings:
176	      - "Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐"
177	      - "SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器"
178	      - "比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败"
179	      - "健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定"
180	    relevance_to_us: "SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel"
181	    metrics_studied: ["spectral alignment", "weight norm", "gradient norm"]
182	
183	  - id: "he2025closer"
184	    title: "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"
185	    authors: "Shiliang He et al."
186	    venue: "NeurIPS 2025 (Spotlight)"
187	    year: 2025
188	    url: "https://arxiv.org/abs/2509.16499"
189	    category: "canary-metrics"
190	    role: "direct-competitor"
191	    key_findings:
192	      - "识别 diffusion model collapse 中的 generalization → memorization 转变"
193	      - "**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**"
194	      - "提出基于 entropy 的数据选择策略，有效缓解 collapse"
195	    relevance_to_us: "data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效"
196	    metrics_studied: ["entropy", "FID", "diversity"]
197	
198	  - id: "ba2024fill"
199	    title: "Fill In The Gaps: Model Calibration and Generalization with Synthetic Data"
200	    authors: "Yang Ba, Michelle V Mancenido, Rong Pan"
201	    venue: "EMNLP 2024"
202	    year: 2024
203	    url: "https://arxiv.org/abs/2410.10864"
204	    category: "canary-metrics"
205	    role: "background"
206	    key_findings:
207	      - "用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins"
208	      - "推导了基于 PAC 框架的 ECE bound"
209	      - "合成数据可改善 calibration 但需精心设计生成策略"
210	    relevance_to_us: "ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据"
211	    metrics_studied: ["ECE", "accuracy"]
212	
213	  - id: "sigma2026spectral"
214	    title: "SIGMA: Scalable Spectral Insights for LLM Model Collapse"
215	    authors: "Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue"
216	    venue: "arXiv (2601.03385)"
217	    year: 2026
218	    url: "https://arxiv.org/abs/2601.03385"
219	    category: "canary-metrics"
220	    role: "direct-competitor"
221	    key_findings:
222	      - "基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样"
223	      - "Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影"
224	      - "随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控"
225	    relevance_to_us: "最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成"
226	    gaps: "未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略"
227	    metrics_studied: ["Gram matrix eigenspectrum", "spectral norm bounds"]
228	
229	  - id: "kalinowski2026topology"
230	    title: "Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index"
231	    authors: "Alexander Kalinowski"
232	    venue: "arXiv (2604.26984)"
233	    year: 2026
234	    url: "https://arxiv.org/abs/2604.26984"
235	    category: "canary-metrics"
236	    role: "background"
237	    key_findings:
238	      - "提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建"
239	      - "Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning"
240	      - "拓扑方法捕捉表示空间的各向异性和多尺度结构丧失"
241	    relevance_to_us: "topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由"
242	    gaps: "计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比"
243	    metrics_studied: ["Collapse Index", "persistent homology features"]
244	
245	  # ============================================================
246	  # DIVERSITY METRICS (BACKGROUND)
247	  # ============================================================
248	  - id: "zhu2018texygen"
249	    title: "Texygen: A Benchmarking Platform for Text Generation Models"
250	    authors: "Yaoming Zhu et al."
251	    venue: "SIGIR 2018"
252	    year: 2018
253	    url: "https://arxiv.org/abs/1802.01886"
254	    category: "canary-metrics"
255	    role: "background"
256	    key_findings:
257	      - "提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低"
258	      - "成为文本生成多样性评估的标准基准之一"
259	    relevance_to_us: "Self-BLEU 是我们 diversity canary 的经典候选"
260	    metrics_studied: ["Self-BLEU", "BLEU"]
261	
262	  - id: "li2016diversity"
263	    title: "A Diversity-Promoting Objective Function for Neural Conversation Models"
264	    authors: "Jiwei Li et al."
265	    venue: "NAACL 2016"
266	    year: 2016
267	    url: "https://arxiv.org/abs/1510.03055"
268	    category: "canary-metrics"
269	    role: "background"
270	    key_findings:
271	      - "提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性"
272	      - "计算 unique n-gram 数占总 n-gram 数的比例"
273	    relevance_to_us: "distinct-n 是最廉价的 diversity canary 之一，计算开销极低"
274	    metrics_studied: ["distinct-1", "distinct-2"]
275	
276	  # ============================================================
277	  # REPRESENTATION / SPECTRAL COLLAPSE
278	  # ============================================================
279	  - id: "jing2022understanding"
280	    title: "Understanding Dimensional Collapse in Contrastive Self-supervised Learning"
281	    authors: "Li Jing et al."
282	    venue: "ICLR 2022"
283	    year: 2022
284	    url: "https://openreview.net/forum?id=YevsQ05DEN7"
285	    category: "canary-metrics"
286	    role: "method-component"
287	    key_findings:
288	      - "定义 dimensional collapse：embedding 向量只跨越低维子空间"
289	      - "effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量"
290	      - "strong augmentation 和 implicit regularization 驱动低秩解"
291	    relevance_to_us: "effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控"
292	    metrics_studied: ["effective rank", "singular value spectrum"]
293	
294	  - id: "noci2024mind"
295	    title: "Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers"
296	    authors: "Lorenzo Noci et al."
297	    venue: "NeurIPS 2024"
298	    year: 2024
299	    url: "https://arxiv.org/abs/2410.07799"
300	    category: "canary-metrics"
301	    role: "method-component"
302	    key_findings:
303	      - "用 Random Matrix Theory 分析 attention 层的 rank collapse"
304	      - "发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因"
305	      - "rank collapse in depth: 所有 token 沿层收敛到单一表示"
306	    relevance_to_us: "spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作"
307	    metrics_studied: ["spectral gap", "singular values", "effective rank"]
308	
309	  # ============================================================
310	  # DATA MIXING & ACCUMULATION
311	  # ============================================================
312	  - id: "kazdan2025collapse"
313	    title: "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"
314	    authors: "Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo"
315	    venue: "ICML 2025"
316	    year: 2025
317	    url: "https://arxiv.org/abs/2410.16713"
318	    category: "data-mixing"
319	    role: "foundation"
320	    key_findings:
321	      - "系统对比 replace vs accumulate 场景"
322	      - "replace → collapse；accumulate → 可避免 collapse"
323	      - "发现 real data 和 synthetic data 之间存在非平凡的交互效应"
324	      - "synthetic data 的价值取决于 real data 的绝对数量"
325	    relevance_to_us: "直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考"
326	    metrics_studied: ["test loss"]
327	
328	  - id: "dey2024breaking"
329	    title: "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"
330	    authors: "Apratim Dey, David Donoho, et al."
331	    venue: "ICML 2024"
332	    year: 2024
333	    url: "https://arxiv.org/abs/2404.01413"
334	    category: "data-mixing"
335	    role: "foundation"
336	    key_findings:
337	      - "替换数据 → 发散 population risk；累积数据 → 避免发散"
338	      - "证明累积策略在多种模型（GMM, HMM, LLM）上有效"
339	    relevance_to_us: "为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子"
340	    metrics_studied: ["population risk"]
341	
342	  - id: "epstein2024howbad"
343	    title: "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse"
344	    authors: "Mohamed El Amine Epstein et al."
345	    venue: "arXiv (2404.05090)"
346	    year: 2024
347	    url: "https://arxiv.org/abs/2404.05090"
348	    category: "data-mixing"
349	    role: "background"
350	    key_findings:
351	      - "纯合成数据训练不可避免 collapse"
352	      - "给出 synthetic data 比例上界的估计——低于此比例可避免 collapse"
353	      - "递归训练使原始分布尾部消失"
354	    relevance_to_us: "其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值"
355	    metrics_studied: ["perplexity"]
356	
357	  - id: "fu2025selfconsuming"
358	    title: "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops"
359	    authors: "Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao"
360	    venue: "ICLR 2025"
361	    year: 2025
362	    url: "https://arxiv.org/abs/2502.18865"
363	    category: "data-mixing"
364	    role: "theoretical-foundation"
365	    key_findings:
366	      - "引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析"
367	      - "恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight"
368	      - "模型架构和 real/synthetic 数据比例共同决定 STL 的成败"
369	    relevance_to_us: "为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证"
370	    gaps: "理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构"
371	    metrics_studied: ["generalization bound", "population risk"]
372	
373	  - id: "bakshi2026improvement"
374	    title: "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources"
375	    authors: "Soham Bakshi, Sunrit Chakraborty"
376	    venue: "arXiv (2602.10531)"
377	    year: 2026
378	    url: "https://arxiv.org/abs/2602.10531"
379	    category: "data-mixing"
380	    role: "theoretical-foundation"
381	    key_findings:
382	      - "αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency"
383	      - "当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）"
384	      - "αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime"
385	      - "在 next-token prediction 语言模型上分析完整迭代演化动态"
386	    relevance_to_us: "αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式"
387	    gaps: "理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime"
388	    metrics_studied: ["population risk", "total variation distance"]
389	
390	  # ============================================================
391	  # MITIGATION & VERIFICATION
392	  # ============================================================
393	  - id: "feng2025escaping"
394	    title: "Escaping Model Collapse via Synthetic Data Verification"
395	    authors: "Yunzhen Feng et al."
396	    venue: "NeurIPS 2025"
397	    year: 2025
398	    url: "https://arxiv.org/abs/2510.16657"
399	    category: "data-mixing"
400	    role: "background"
401	    key_findings:
402	      - "通过外部 verifier（human 或 better model）注入信息可避免 collapse"
403	      - "verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center"
404	      - "除非 verifier 完全可靠，早期收益会 plateau 甚至逆转"
405	    relevance_to_us: "verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention"
406	    metrics_studied: ["test loss"]
407	
408	  - id: "barzilai2025consistency"
409	    title: "When Models Don't Collapse: On the Consistency of Iterative MLE"
410	    authors: "Daniel Barzilai, Ohad Shamir"
411	    venue: "ICML 2025"
412	    year: 2025
413	    url: "https://arxiv.org/abs/2505.19046"
414	    category: "core-collapse"
415	    role: "background"
416	    key_findings:
417	      - "在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse"
418	      - "但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例"
419	    relevance_to_us: "理论上的 collapse 可发生任意快的结论强化了 early warning 的价值"
420	    metrics_studied: []
421	
422	  - id: "dces2026counter"
423	    title: "Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling"
424	    authors: "Anonymous"
425	    venue: "MDPI Electronics (2026)"
426	    year: 2026
427	    url: "https://www.mdpi.com/2079-9292/15/4/869"
428	    category: "data-mixing"
429	    role: "background"
430	    key_findings:
431	      - "提出 DCES（dynamic center-edge sampling）数据选择框架"
432	      - "DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择"
433	    relevance_to_us: "其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考"
434	    metrics_studied: ["ECE", "entropy"]
435	
436	  # ============================================================
437	  # POSITION / SURVEY / EPISTEMICS
438	  # ============================================================
439	  - id: "schaeffer2025position"
440	    title: "Position: Model Collapse Does Not Mean What You Think"
441	    authors: "Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo"
442	    venue: "arXiv (2503.03150)"
443	    year: 2025
444	    url: "https://arxiv.org/abs/2503.03150"
445	    category: "core-collapse"
446	    role: "background"
447	    key_findings:
448	      - "文献中实际包含 8 种不同且有时矛盾的 model collapse 定义"
449	      - "许多 collapse 预测依赖于与现实不符的假设"
450	      - "多种 collapse 场景是可以轻易避免的"
451	    relevance_to_us: "提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标"
452	    metrics_studied: []
453	
454	  - id: "wang2025epistemic"
455	    title: "Epistemic Diversity and Knowledge Collapse in Large Language Models"
456	    authors: "Wang et al."
457	    venue: "arXiv (2510.04226)"
458	    year: 2025
459	    url: "https://arxiv.org/abs/2510.04226"
460	    category: "core-collapse"
461	    role: "background"
462	    key_findings:
463	      - "27 个 LLM 在 155 个主题上的 epistemic diversity 评估"
464	      - "所有模型的 epistemic diversity 低于基本 web 搜索"
465	      - "模型越大 epistemic diversity 反而越低；RAG 有正面效果"
466	    relevance_to_us: "knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic"
467	    metrics_studied: ["epistemic diversity"]
468	
469	  # ============================================================
470	  # METHODOLOGY (GRANGER / LEAD-LAG)
471	  # ============================================================
472	  - id: "shojaie2022granger"
473	    title: "Granger Causality: A Review and Recent Advances"
474	    authors: "Ali Shojaie, Emily B. Fox"
475	    venue: "Annual Review of Statistics and Its Application"
476	    year: 2022
477	    url: "https://arxiv.org/abs/2105.02675"
478	    category: "methodology"
479	    role: "method-component"
480	    key_findings:
481	      - "Granger causality 综述：从经典线性到非线性/neural 方法"
482	      - "Panel data 场景的 Granger causality 扩展"
483	      - "VAR 和 neural Granger causality 的对比"
484	    relevance_to_us: "为我们的 panel Granger causality 分析提供方法论基础"
485	    metrics_studied: []
486	
487	  - id: "marcinkevics2022neural"
488	    title: "Granger Causality Using Neural Networks"
489	    authors: "Raphael Marcinkevics, Julia Vogt"
490	    venue: "arXiv (2208.03703)"
491	    year: 2022
492	    url: "https://arxiv.org/abs/2208.03703"
493	    category: "methodology"
494	    role: "method-component"
495	    key_findings:
496	      - "用 neural network 估计 Granger causality，突破线性假设"
497	      - "两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据"
498	    relevance_to_us: "我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择"
499	    metrics_studied: []
500	
501	gaps:
502	  - "无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse"
503	  - "ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析"
504	  - "embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过"
505	  - "多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系"
506	  - "alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化"
507	  - "predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益"
508	  - "surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证"
509	  - "跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠"
510	
511	novelty_assessment: |
512	  我们项目的核心 novelty 在于：
513	
514	  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。
515	     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，
516	     但没有人做过系统的 lead-lag 量化分析。
517	
518	  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、
519	     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。
520	     现有工作都是单一指标或最多两三个指标的孤立分析。
521	
522	  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary
523	     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，
524	     但没人研究 canary 在不同 alpha 下的行为。
525	
526	  4. **与已有工作的差异**：
527	     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化
528	     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；
529	       我们将其纳入更广的 panel 并研究其 lead-lag 特性
530	     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标
531	     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；
532	       我们将类似思路迁移到 iterative collapse 场景
533	
534	  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，
535	     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。
536	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "49f9fdad-0462-417d-abe1-8a06f5276de1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
      "content": "papers:\n  # ============================================================\n  # CORE MODEL COLLAPSE\n  # ============================================================\n  - id: \"shumailov2024curse\"\n    title: \"The Curse of Recursion: Training on Generated Data Makes Models Forget\"\n    authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\"\n    venue: \"Nature\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2305.17493\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\"\n      - \"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\"\n      - \"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\"\n      - \"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\"\n    relevance_to_us: \"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\"\n    metrics_studied: [\"perplexity\", \"distributional tail mass\"]\n\n  - id: \"alemohammad2024mad\"\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2307.01850\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"提出 Model Autophagy Disorder (MAD) 概念\"\n      - \"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\"\n      - \"在图像生成领域验证 self-consuming loop 的退化效应\"\n    relevance_to_us: \"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\"\n    metrics_studied: [\"FID\", \"precision\", \"recall\", \"diversity\"]\n\n  - id: \"dohmatob2024tale\"\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.07043\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\"\n      - \"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\"\n      - \"混入少量干净数据可缓解 collapse 并引发 grokking 现象\"\n      - \"在 transformer 算术任务和 Llama2 文本生成上验证\"\n    relevance_to_us: \"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\"\n    metrics_studied: [\"test loss\", \"scaling exponents\"]\n\n  - id: \"dohmatob2025strong\"\n    title: \"Strong Model Collapse\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n    venue: \"ICLR 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.04840\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"即使合成数据占比极小（1/1000），仍可导致 model collapse\"\n      - \"更大的训练集并不能避免 collapse\"\n      - \"更大的模型（random projection 近似下）反而可能放大 collapse\"\n      - \"存在 interpolation threshold 的 double-descent 现象\"\n    relevance_to_us: \"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\"\n    metrics_studied: [\"test loss\", \"population risk\"]\n\n  - id: \"guo2024linguistic\"\n    title: \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\"\n    authors: \"Yanzhu Guo, Guokan Shang, et al.\"\n    venue: \"NAACL 2024 Findings\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.09807\"\n    category: \"core-collapse\"\n    role: \"evaluation\"\n    key_findings:\n      - \"递归微调中，linguistic diversity 在连续迭代中持续下降\"\n      - \"创造性任务中 diversity 下降最显著\"\n      - \"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\"\n    relevance_to_us: \"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\"\n    metrics_studied: [\"distinct-n\", \"type-token ratio\", \"syntactic diversity\", \"semantic diversity\"]\n\n  - id: \"briesch2024selfconsuming\"\n    title: \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\"\n    authors: \"Martin Briesch, Dominik Sobania, Franz Rothlauf\"\n    venue: \"arXiv (2311.16822)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.16822\"\n    category: \"core-collapse\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"首次系统研究 LLM 的 self-consuming training loop\"\n      - \"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\"\n      - \"expanding data cycle（累积）在 50 代内保持 diversity\"\n    relevance_to_us: \"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\"\n    metrics_studied: [\"diversity\", \"quality\"]\n\n  - id: \"truong2025entropy\"\n    title: \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\"\n    authors: \"Truong Xuan Khanh, Truong Quynh Hoa\"\n    venue: \"arXiv (2512.12381)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.12381\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\"\n      - \"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\"\n      - \"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\"\n    relevance_to_us: \"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\"\n    gaps: \"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\"\n    metrics_studied: [\"entropy\", \"autocorrelation\", \"variance\"]\n\n  - id: \"wang2026contaminated\"\n    title: \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\"\n    authors: \"Kevin Wang, Hongqian Niu, Didong Li\"\n    venue: \"arXiv (2602.16065)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16065\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\"\n      - \"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\"\n      - \"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\"\n    relevance_to_us: \"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\"\n    gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"\n    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================\n  - id: \"chen2025scales\"\n    title: \"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\"\n    authors: \"Anonymous\"\n    venue: \"arXiv (2510.05133)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.05133\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\"\n      - \"20% synthetic data 以下性能稳定，30% 以上退化加速\"\n      - \"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\"\n      - \"推理任务比检索任务更易退化\"\n      - \"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\"\n    relevance_to_us: \"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\"\n    metrics_studied: [\"ECE\", \"accuracy\", \"perplexity\"]\n\n  - id: \"gambetta2024surplexity\"\n    title: \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\"\n    authors: \"Daniele Gambetta et al.\"\n    venue: \"arXiv (2410.12341)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.12341\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\"\n      - \"用 semantic networks 分析文本重复性和语义多样性\"\n      - \"用 next-token probability 定量衡量 diversity loss\"\n      - \"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\"\n      - \"不需要区分 human vs AI-generated data\"\n    relevance_to_us: \"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\"\n    metrics_studied: [\"surplexity\", \"semantic network metrics\", \"next-token probability\"]\n\n  - id: \"qiu2025spectral\"\n    title: \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\"\n    authors: \"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\"\n    venue: \"arXiv (2510.04202)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04202\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\"\n      - \"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\"\n      - \"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\"\n      - \"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\"\n    relevance_to_us: \"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\"\n    metrics_studied: [\"spectral alignment\", \"weight norm\", \"gradient norm\"]\n\n  - id: \"he2025closer\"\n    title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n    authors: \"Shiliang He et al.\"\n    venue: \"NeurIPS 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2509.16499\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"识别 diffusion model collapse 中的 generalization → memorization 转变\"\n      - \"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\"\n      - \"提出基于 entropy 的数据选择策略，有效缓解 collapse\"\n    relevance_to_us: \"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\"\n    metrics_studied: [\"entropy\", \"FID\", \"diversity\"]\n\n  - id: \"ba2024fill\"\n    title: \"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\"\n    authors: \"Yang Ba, Michelle V Mancenido, Rong Pan\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.10864\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\"\n      - \"推导了基于 PAC 框架的 ECE bound\"\n      - \"合成数据可改善 calibration 但需精心设计生成策略\"\n    relevance_to_us: \"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\"\n    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  - id: \"sigma2026spectral\"\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: \"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\"\n    venue: \"arXiv (2601.03385)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.03385\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\"\n      - \"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\"\n      - \"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\"\n    relevance_to_us: \"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\"\n    gaps: \"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\"\n    metrics_studied: [\"Gram matrix eigenspectrum\", \"spectral norm bounds\"]\n\n  - id: \"kalinowski2026topology\"\n    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"\n    authors: \"Alexander Kalinowski\"\n    venue: \"arXiv (2604.26984)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.26984\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\"\n      - \"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\"\n      - \"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\"\n    relevance_to_us: \"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\"\n    gaps: \"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\"\n    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================\n  - id: \"zhu2018texygen\"\n    title: \"Texygen: A Benchmarking Platform for Text Generation Models\"\n    authors: \"Yaoming Zhu et al.\"\n    venue: \"SIGIR 2018\"\n    year: 2018\n    url: \"https://arxiv.org/abs/1802.01886\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\"\n      - \"成为文本生成多样性评估的标准基准之一\"\n    relevance_to_us: \"Self-BLEU 是我们 diversity canary 的经典候选\"\n    metrics_studied: [\"Self-BLEU\", \"BLEU\"]\n\n  - id: \"li2016diversity\"\n    title: \"A Diversity-Promoting Objective Function for Neural Conversation Models\"\n    authors: \"Jiwei Li et al.\"\n    venue: \"NAACL 2016\"\n    year: 2016\n    url: \"https://arxiv.org/abs/1510.03055\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\"\n      - \"计算 unique n-gram 数占总 n-gram 数的比例\"\n    relevance_to_us: \"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\"\n    metrics_studied: [\"distinct-1\", \"distinct-2\"]\n\n  # ============================================================\n  # REPRESENTATION / SPECTRAL COLLAPSE\n  # ============================================================\n  - id: \"jing2022understanding\"\n    title: \"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\"\n    authors: \"Li Jing et al.\"\n    venue: \"ICLR 2022\"\n    year: 2022\n    url: \"https://openreview.net/forum?id=YevsQ05DEN7\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"定义 dimensional collapse：embedding 向量只跨越低维子空间\"\n      - \"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\"\n      - \"strong augmentation 和 implicit regularization 驱动低秩解\"\n    relevance_to_us: \"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\"\n    metrics_studied: [\"effective rank\", \"singular value spectrum\"]\n\n  - id: \"noci2024mind\"\n    title: \"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\"\n    authors: \"Lorenzo Noci et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.07799\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 Random Matrix Theory 分析 attention 层的 rank collapse\"\n      - \"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\"\n      - \"rank collapse in depth: 所有 token 沿层收敛到单一表示\"\n    relevance_to_us: \"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\"\n    metrics_studied: [\"spectral gap\", \"singular values\", \"effective rank\"]\n\n  # ============================================================\n  # DATA MIXING & ACCUMULATION\n  # ============================================================\n  - id: \"kazdan2025collapse\"\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: \"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.16713\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"系统对比 replace vs accumulate 场景\"\n      - \"replace → collapse；accumulate → 可避免 collapse\"\n      - \"发现 real data 和 synthetic data 之间存在非平凡的交互效应\"\n      - \"synthetic data 的价值取决于 real data 的绝对数量\"\n    relevance_to_us: \"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"dey2024breaking\"\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: \"Apratim Dey, David Donoho, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.01413\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"替换数据 → 发散 population risk；累积数据 → 避免发散\"\n      - \"证明累积策略在多种模型（GMM, HMM, LLM）上有效\"\n    relevance_to_us: \"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\"\n    metrics_studied: [\"population risk\"]\n\n  - id: \"epstein2024howbad\"\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Mohamed El Amine Epstein et al.\"\n    venue: \"arXiv (2404.05090)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.05090\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"纯合成数据训练不可避免 collapse\"\n      - \"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\"\n      - \"递归训练使原始分布尾部消失\"\n    relevance_to_us: \"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\"\n    metrics_studied: [\"perplexity\"]\n\n  - id: \"fu2025selfconsuming\"\n    title: \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\"\n    authors: \"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.18865\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\"\n      - \"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\"\n      - \"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\"\n    relevance_to_us: \"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\"\n    gaps: \"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\"\n    metrics_studied: [\"generalization bound\", \"population risk\"]\n\n  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi, Sunrit Chakraborty\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\"\n      - \"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\"\n      - \"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\"\n      - \"在 next-token prediction 语言模型上分析完整迭代演化动态\"\n    relevance_to_us: \"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\"\n    gaps: \"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\"\n    metrics_studied: [\"population risk\", \"total variation distance\"]\n\n  # ============================================================\n  # MITIGATION & VERIFICATION\n  # ============================================================\n  - id: \"feng2025escaping\"\n    title: \"Escaping Model Collapse via Synthetic Data Verification\"\n    authors: \"Yunzhen Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.16657\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"通过外部 verifier（human 或 better model）注入信息可避免 collapse\"\n      - \"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\"\n      - \"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\"\n    relevance_to_us: \"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"barzilai2025consistency\"\n    title: \"When Models Don't Collapse: On the Consistency of Iterative MLE\"\n    authors: \"Daniel Barzilai, Ohad Shamir\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2505.19046\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\"\n      - \"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\"\n    relevance_to_us: \"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\"\n    metrics_studied: []\n\n  - id: \"dces2026counter\"\n    title: \"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\"\n    authors: \"Anonymous\"\n    venue: \"MDPI Electronics (2026)\"\n    year: 2026\n    url: \"https://www.mdpi.com/2079-9292/15/4/869\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"提出 DCES（dynamic center-edge sampling）数据选择框架\"\n      - \"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\"\n    relevance_to_us: \"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\"\n    metrics_studied: [\"ECE\", \"entropy\"]\n\n  # ============================================================\n  # POSITION / SURVEY / EPISTEMICS\n  # ============================================================\n  - id: \"schaeffer2025position\"\n    title: \"Position: Model Collapse Does Not Mean What You Think\"\n    authors: \"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\"\n    venue: \"arXiv (2503.03150)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.03150\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\"\n      - \"许多 collapse 预测依赖于与现实不符的假设\"\n      - \"多种 collapse 场景是可以轻易避免的\"\n    relevance_to_us: \"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\"\n    metrics_studied: []\n\n  - id: \"wang2025epistemic\"\n    title: \"Epistemic Diversity and Knowledge Collapse in Large Language Models\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv (2510.04226)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04226\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\"\n      - \"所有模型的 epistemic diversity 低于基本 web 搜索\"\n      - \"模型越大 epistemic diversity 反而越低；RAG 有正面效果\"\n    relevance_to_us: \"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\"\n    metrics_studied: [\"epistemic diversity\"]\n\n  # ============================================================\n  # METHODOLOGY (GRANGER / LEAD-LAG)\n  # ============================================================\n  - id: \"shojaie2022granger\"\n    title: \"Granger Causality: A Review and Recent Advances\"\n    authors: \"Ali Shojaie, Emily B. Fox\"\n    venue: \"Annual Review of Statistics and Its Application\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2105.02675\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"Granger causality 综述：从经典线性到非线性/neural 方法\"\n      - \"Panel data 场景的 Granger causality 扩展\"\n      - \"VAR 和 neural Granger causality 的对比\"\n    relevance_to_us: \"为我们的 panel Granger causality 分析提供方法论基础\"\n    metrics_studied: []\n\n  - id: \"marcinkevics2022neural\"\n    title: \"Granger Causality Using Neural Networks\"\n    authors: \"Raphael Marcinkevics, Julia Vogt\"\n    venue: \"arXiv (2208.03703)\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2208.03703\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 neural network 估计 Granger causality，突破线性假设\"\n      - \"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\"\n    relevance_to_us: \"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\"\n    metrics_studied: []\n\ngaps:\n  - \"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\"\n  - \"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\"\n  - \"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\"\n  - \"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\"\n  - \"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\"\n  - \"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\"\n  - \"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\"\n  - \"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\"\n\nnovelty_assessment: |\n  我们项目的核心 novelty 在于：\n\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\n     但没有人做过系统的 lead-lag 量化分析。\n\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\n     现有工作都是单一指标或最多两三个指标的孤立分析。\n\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\n     但没人研究 canary 在不同 alpha 下的行为。\n\n  4. **与已有工作的差异**：\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\n       我们将类似思路迁移到 iterative collapse 场景\n\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\n",
      "numLines": 536,
      "startLine": 1,
      "totalLines": 536
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full file read via the Read tool. I'll make two insertions:

1. After the wang2026contaminated entry (line 128, `metrics_studied: ["convergence rate", "population risk"]`), before the CANARY section comment (line 130), add 4 new core-collapse papers.

2. After the kalinowski2026topology entry (line 243, `metrics_studied: ["Collapse Index", "persistent homology features"]`), before the DIVERSITY METRICS section comment (line 245), add the bergsma entry.

Let me use the Edit tool for both insertions. I need to find unique strings for each insertion point.


I've identified the exact boundaries for both insertions—the unique text surrounding each location where I need to add the new entries. Since these edits don't overlap, I can make them both in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "77077934-c8a3-4e83-b5ec-b64cdab90e86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fss7sYHnFKTc1YauqWfJrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16068,
      "cache_read_input_tokens": 42162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16068
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 17_

在 core-collapse 和 canary-metrics 两个区段各插入新论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "2a85e309-1975-4168-97a1-7ee595e109aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fss7sYHnFKTc1YauqWfJrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16068,
      "cache_read_input_tokens": 42162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16068
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01TgFxxWv5dfVdgFFrFnCzyN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
  "old_string": "    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================",
  "new_string": "    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  - id: \"du2026geometric\"\n    title: \"Escaping Mode Collapse in LLM Generation via Geometric Regulation\"\n    authors: \"Du, Tanaka-Ishii\"\n    venue: \"arXiv (2605.00435)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.00435\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"将 mode collapse 重新解释为表示空间中的 geometric collapse：生成时模型内部轨迹被限制在低维子空间\"\n      - \"提出 RMR（Reinforced Mode Regulation），在 value cache 中抑制 dominant self-reinforcing directions\"\n    relevance_to_us: \"针对推理时 mode collapse，非迭代训练场景。但 'geometric collapse = 低维子空间坍缩' 与我们的 effective rank 指标在概念上有连接，可在 related work 中引用以说明 representation-space collapse 检测的跨场景通用性\"\n    metrics_studied: [\"effective rank proxy\", \"representation dimensionality\"]\n\n  - id: \"gauthier2026alignment\"\n    title: \"Explaining and Preventing Alignment Collapse in Iterative RLHF\"\n    authors: \"Gauthier, Bach, Jordan\"\n    venue: \"arXiv (2605.04266)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.04266\"\n    category: \"core-collapse\"\n    role: \"complementary\"\n    key_findings:\n      - \"迭代 RLHF 中 policy 生成 reward model 的训练数据形成反馈环路，导致 alignment collapse（policy 系统性利用 reward model 盲区）\"\n      - \"用 Stackelberg game 建模迭代 RLHF 的环路动力学，提出 FPO（foresighted policy optimization）\"\n    relevance_to_us: \"RLHF iterative feedback loop 与本项目 iterative synthetic data loop 结构类似——模型输出成为下一轮输入的反馈环路均导致系统性退化。其 'collapse = 反馈环路中的系统性退化' 叙事支持我们的大框架；Stackelberg game 视角可能启发 canary 的博弈论解释\"\n    metrics_studied: [\"alignment score\", \"reward model accuracy\"]\n\n  - id: \"shi2026pruning\"\n    title: \"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv (2605.07271)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.07271\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"层剪枝导致的 performance collapse，定义 Silent Phase（模型预测被单一选项主导 = distributional collapse）和 Decisive Phase\"\n      - \"剪枝 Silent Phase 立即触发 collapse\"\n    relevance_to_us: \"架构剪枝 collapse，非数据驱动。其 'distributional collapse = 预测分布退化为单峰' 的操作定义与我们 token entropy 下降检测的是同一现象的不同表现\"\n    metrics_studied: [\"prediction distribution entropy\", \"task accuracy\"]\n\n  - id: \"tubingen2026diffusion\"\n    title: \"Layer Collapse in Diffusion Language Models\"\n    authors: \"Tübingen AI Center et al.\"\n    venue: \"arXiv (2605.06366)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.06366\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"LLaDA-8B 中发现层级 activation collapse：少数早期层的 activation 被单个 super-outlier 主导\"\n      - \"剪掉此 outlier 导致模型输出退化为重复随机 token\"\n    relevance_to_us: \"Diffusion LM 的架构 collapse，与迭代合成数据训练无关。但 activation collapse 的表征与 spectral collapse 有交集\"\n    metrics_studied: [\"activation magnitude\", \"output repetition\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "d9c34260-51f4-406d-9b51-7ec7968dca66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fss7sYHnFKTc1YauqWfJrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16068,
      "cache_read_input_tokens": 42162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16068
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T04:47:27.022Z_

<details><summary>↩ Tool result · `toolu_01TgFxxWv5dfVdgFFrFnCzyN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "68290fa4-1cea-45cd-96a7-202dc17ee3c6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
    "oldString": "    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================",
    "newString": "    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  - id: \"du2026geometric\"\n    title: \"Escaping Mode Collapse in LLM Generation via Geometric Regulation\"\n    authors: \"Du, Tanaka-Ishii\"\n    venue: \"arXiv (2605.00435)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.00435\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"将 mode collapse 重新解释为表示空间中的 geometric collapse：生成时模型内部轨迹被限制在低维子空间\"\n      - \"提出 RMR（Reinforced Mode Regulation），在 value cache 中抑制 dominant self-reinforcing directions\"\n    relevance_to_us: \"针对推理时 mode collapse，非迭代训练场景。但 'geometric collapse = 低维子空间坍缩' 与我们的 effective rank 指标在概念上有连接，可在 related work 中引用以说明 representation-space collapse 检测的跨场景通用性\"\n    metrics_studied: [\"effective rank proxy\", \"representation dimensionality\"]\n\n  - id: \"gauthier2026alignment\"\n    title: \"Explaining and Preventing Alignment Collapse in Iterative RLHF\"\n    authors: \"Gauthier, Bach, Jordan\"\n    venue: \"arXiv (2605.04266)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.04266\"\n    category: \"core-collapse\"\n    role: \"complementary\"\n    key_findings:\n      - \"迭代 RLHF 中 policy 生成 reward model 的训练数据形成反馈环路，导致 alignment collapse（policy 系统性利用 reward model 盲区）\"\n      - \"用 Stackelberg game 建模迭代 RLHF 的环路动力学，提出 FPO（foresighted policy optimization）\"\n    relevance_to_us: \"RLHF iterative feedback loop 与本项目 iterative synthetic data loop 结构类似——模型输出成为下一轮输入的反馈环路均导致系统性退化。其 'collapse = 反馈环路中的系统性退化' 叙事支持我们的大框架；Stackelberg game 视角可能启发 canary 的博弈论解释\"\n    metrics_studied: [\"alignment score\", \"reward model accuracy\"]\n\n  - id: \"shi2026pruning\"\n    title: \"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv (2605.07271)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.07271\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"层剪枝导致的 performance collapse，定义 Silent Phase（模型预测被单一选项主导 = distributional collapse）和 Decisive Phase\"\n      - \"剪枝 Silent Phase 立即触发 collapse\"\n    relevance_to_us: \"架构剪枝 collapse，非数据驱动。其 'distributional collapse = 预测分布退化为单峰' 的操作定义与我们 token entropy 下降检测的是同一现象的不同表现\"\n    metrics_studied: [\"prediction distribution entropy\", \"task accuracy\"]\n\n  - id: \"tubingen2026diffusion\"\n    title: \"Layer Collapse in Diffusion Language Models\"\n    authors: \"Tübingen AI Center et al.\"\n    venue: \"arXiv (2605.06366)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.06366\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"LLaDA-8B 中发现层级 activation collapse：少数早期层的 activation 被单个 super-outlier 主导\"\n      - \"剪掉此 outlier 导致模型输出退化为重复随机 token\"\n    relevance_to_us: \"Diffusion LM 的架构 collapse，与迭代合成数据训练无关。但 activation collapse 的表征与 spectral collapse 有交集\"\n    metrics_studied: [\"activation magnitude\", \"output repetition\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================",
    "originalFile": "papers:\n  # ============================================================\n  # CORE MODEL COLLAPSE\n  # ============================================================\n  - id: \"shumailov2024curse\"\n    title: \"The Curse of Recursion: Training on Generated Data Makes Models Forget\"\n    authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\"\n    venue: \"Nature\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2305.17493\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\"\n      - \"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\"\n      - \"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\"\n      - \"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\"\n    relevance_to_us: \"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\"\n    metrics_studied: [\"perplexity\", \"distributional tail mass\"]\n\n  - id: \"alemohammad2024mad\"\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2307.01850\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"提出 Model Autophagy Disorder (MAD) 概念\"\n      - \"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\"\n      - \"在图像生成领域验证 self-consuming loop 的退化效应\"\n    relevance_to_us: \"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\"\n    metrics_studied: [\"FID\", \"precision\", \"recall\", \"diversity\"]\n\n  - id: \"dohmatob2024tale\"\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.07043\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\"\n      - \"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\"\n      - \"混入少量干净数据可缓解 collapse 并引发 grokking 现象\"\n      - \"在 transformer 算术任务和 Llama2 文本生成上验证\"\n    relevance_to_us: \"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\"\n    metrics_studied: [\"test loss\", \"scaling exponents\"]\n\n  - id: \"dohmatob2025strong\"\n    title: \"Strong Model Collapse\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n    venue: \"ICLR 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.04840\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"即使合成数据占比极小（1/1000），仍可导致 model collapse\"\n      - \"更大的训练集并不能避免 collapse\"\n      - \"更大的模型（random projection 近似下）反而可能放大 collapse\"\n      - \"存在 interpolation threshold 的 double-descent 现象\"\n    relevance_to_us: \"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\"\n    metrics_studied: [\"test loss\", \"population risk\"]\n\n  - id: \"guo2024linguistic\"\n    title: \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\"\n    authors: \"Yanzhu Guo, Guokan Shang, et al.\"\n    venue: \"NAACL 2024 Findings\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.09807\"\n    category: \"core-collapse\"\n    role: \"evaluation\"\n    key_findings:\n      - \"递归微调中，linguistic diversity 在连续迭代中持续下降\"\n      - \"创造性任务中 diversity 下降最显著\"\n      - \"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\"\n    relevance_to_us: \"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\"\n    metrics_studied: [\"distinct-n\", \"type-token ratio\", \"syntactic diversity\", \"semantic diversity\"]\n\n  - id: \"briesch2024selfconsuming\"\n    title: \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\"\n    authors: \"Martin Briesch, Dominik Sobania, Franz Rothlauf\"\n    venue: \"arXiv (2311.16822)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.16822\"\n    category: \"core-collapse\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"首次系统研究 LLM 的 self-consuming training loop\"\n      - \"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\"\n      - \"expanding data cycle（累积）在 50 代内保持 diversity\"\n    relevance_to_us: \"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\"\n    metrics_studied: [\"diversity\", \"quality\"]\n\n  - id: \"truong2025entropy\"\n    title: \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\"\n    authors: \"Truong Xuan Khanh, Truong Quynh Hoa\"\n    venue: \"arXiv (2512.12381)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.12381\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\"\n      - \"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\"\n      - \"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\"\n    relevance_to_us: \"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\"\n    gaps: \"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\"\n    metrics_studied: [\"entropy\", \"autocorrelation\", \"variance\"]\n\n  - id: \"wang2026contaminated\"\n    title: \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\"\n    authors: \"Kevin Wang, Hongqian Niu, Didong Li\"\n    venue: \"arXiv (2602.16065)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16065\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\"\n      - \"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\"\n      - \"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\"\n    relevance_to_us: \"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\"\n    gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"\n    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================\n  - id: \"chen2025scales\"\n    title: \"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\"\n    authors: \"Anonymous\"\n    venue: \"arXiv (2510.05133)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.05133\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\"\n      - \"20% synthetic data 以下性能稳定，30% 以上退化加速\"\n      - \"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\"\n      - \"推理任务比检索任务更易退化\"\n      - \"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\"\n    relevance_to_us: \"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\"\n    metrics_studied: [\"ECE\", \"accuracy\", \"perplexity\"]\n\n  - id: \"gambetta2024surplexity\"\n    title: \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\"\n    authors: \"Daniele Gambetta et al.\"\n    venue: \"arXiv (2410.12341)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.12341\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\"\n      - \"用 semantic networks 分析文本重复性和语义多样性\"\n      - \"用 next-token probability 定量衡量 diversity loss\"\n      - \"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\"\n      - \"不需要区分 human vs AI-generated data\"\n    relevance_to_us: \"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\"\n    metrics_studied: [\"surplexity\", \"semantic network metrics\", \"next-token probability\"]\n\n  - id: \"qiu2025spectral\"\n    title: \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\"\n    authors: \"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\"\n    venue: \"arXiv (2510.04202)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04202\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\"\n      - \"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\"\n      - \"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\"\n      - \"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\"\n    relevance_to_us: \"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\"\n    metrics_studied: [\"spectral alignment\", \"weight norm\", \"gradient norm\"]\n\n  - id: \"he2025closer\"\n    title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n    authors: \"Shiliang He et al.\"\n    venue: \"NeurIPS 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2509.16499\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"识别 diffusion model collapse 中的 generalization → memorization 转变\"\n      - \"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\"\n      - \"提出基于 entropy 的数据选择策略，有效缓解 collapse\"\n    relevance_to_us: \"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\"\n    metrics_studied: [\"entropy\", \"FID\", \"diversity\"]\n\n  - id: \"ba2024fill\"\n    title: \"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\"\n    authors: \"Yang Ba, Michelle V Mancenido, Rong Pan\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.10864\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\"\n      - \"推导了基于 PAC 框架的 ECE bound\"\n      - \"合成数据可改善 calibration 但需精心设计生成策略\"\n    relevance_to_us: \"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\"\n    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  - id: \"sigma2026spectral\"\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: \"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\"\n    venue: \"arXiv (2601.03385)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.03385\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\"\n      - \"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\"\n      - \"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\"\n    relevance_to_us: \"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\"\n    gaps: \"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\"\n    metrics_studied: [\"Gram matrix eigenspectrum\", \"spectral norm bounds\"]\n\n  - id: \"kalinowski2026topology\"\n    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"\n    authors: \"Alexander Kalinowski\"\n    venue: \"arXiv (2604.26984)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.26984\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\"\n      - \"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\"\n      - \"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\"\n    relevance_to_us: \"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\"\n    gaps: \"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\"\n    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================\n  - id: \"zhu2018texygen\"\n    title: \"Texygen: A Benchmarking Platform for Text Generation Models\"\n    authors: \"Yaoming Zhu et al.\"\n    venue: \"SIGIR 2018\"\n    year: 2018\n    url: \"https://arxiv.org/abs/1802.01886\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\"\n      - \"成为文本生成多样性评估的标准基准之一\"\n    relevance_to_us: \"Self-BLEU 是我们 diversity canary 的经典候选\"\n    metrics_studied: [\"Self-BLEU\", \"BLEU\"]\n\n  - id: \"li2016diversity\"\n    title: \"A Diversity-Promoting Objective Function for Neural Conversation Models\"\n    authors: \"Jiwei Li et al.\"\n    venue: \"NAACL 2016\"\n    year: 2016\n    url: \"https://arxiv.org/abs/1510.03055\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\"\n      - \"计算 unique n-gram 数占总 n-gram 数的比例\"\n    relevance_to_us: \"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\"\n    metrics_studied: [\"distinct-1\", \"distinct-2\"]\n\n  # ============================================================\n  # REPRESENTATION / SPECTRAL COLLAPSE\n  # ============================================================\n  - id: \"jing2022understanding\"\n    title: \"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\"\n    authors: \"Li Jing et al.\"\n    venue: \"ICLR 2022\"\n    year: 2022\n    url: \"https://openreview.net/forum?id=YevsQ05DEN7\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"定义 dimensional collapse：embedding 向量只跨越低维子空间\"\n      - \"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\"\n      - \"strong augmentation 和 implicit regularization 驱动低秩解\"\n    relevance_to_us: \"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\"\n    metrics_studied: [\"effective rank\", \"singular value spectrum\"]\n\n  - id: \"noci2024mind\"\n    title: \"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\"\n    authors: \"Lorenzo Noci et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.07799\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 Random Matrix Theory 分析 attention 层的 rank collapse\"\n      - \"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\"\n      - \"rank collapse in depth: 所有 token 沿层收敛到单一表示\"\n    relevance_to_us: \"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\"\n    metrics_studied: [\"spectral gap\", \"singular values\", \"effective rank\"]\n\n  # ============================================================\n  # DATA MIXING & ACCUMULATION\n  # ============================================================\n  - id: \"kazdan2025collapse\"\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: \"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.16713\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"系统对比 replace vs accumulate 场景\"\n      - \"replace → collapse；accumulate → 可避免 collapse\"\n      - \"发现 real data 和 synthetic data 之间存在非平凡的交互效应\"\n      - \"synthetic data 的价值取决于 real data 的绝对数量\"\n    relevance_to_us: \"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"dey2024breaking\"\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: \"Apratim Dey, David Donoho, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.01413\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"替换数据 → 发散 population risk；累积数据 → 避免发散\"\n      - \"证明累积策略在多种模型（GMM, HMM, LLM）上有效\"\n    relevance_to_us: \"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\"\n    metrics_studied: [\"population risk\"]\n\n  - id: \"epstein2024howbad\"\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Mohamed El Amine Epstein et al.\"\n    venue: \"arXiv (2404.05090)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.05090\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"纯合成数据训练不可避免 collapse\"\n      - \"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\"\n      - \"递归训练使原始分布尾部消失\"\n    relevance_to_us: \"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\"\n    metrics_studied: [\"perplexity\"]\n\n  - id: \"fu2025selfconsuming\"\n    title: \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\"\n    authors: \"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.18865\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\"\n      - \"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\"\n      - \"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\"\n    relevance_to_us: \"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\"\n    gaps: \"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\"\n    metrics_studied: [\"generalization bound\", \"population risk\"]\n\n  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi, Sunrit Chakraborty\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\"\n      - \"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\"\n      - \"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\"\n      - \"在 next-token prediction 语言模型上分析完整迭代演化动态\"\n    relevance_to_us: \"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\"\n    gaps: \"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\"\n    metrics_studied: [\"population risk\", \"total variation distance\"]\n\n  # ============================================================\n  # MITIGATION & VERIFICATION\n  # ============================================================\n  - id: \"feng2025escaping\"\n    title: \"Escaping Model Collapse via Synthetic Data Verification\"\n    authors: \"Yunzhen Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.16657\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"通过外部 verifier（human 或 better model）注入信息可避免 collapse\"\n      - \"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\"\n      - \"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\"\n    relevance_to_us: \"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"barzilai2025consistency\"\n    title: \"When Models Don't Collapse: On the Consistency of Iterative MLE\"\n    authors: \"Daniel Barzilai, Ohad Shamir\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2505.19046\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\"\n      - \"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\"\n    relevance_to_us: \"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\"\n    metrics_studied: []\n\n  - id: \"dces2026counter\"\n    title: \"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\"\n    authors: \"Anonymous\"\n    venue: \"MDPI Electronics (2026)\"\n    year: 2026\n    url: \"https://www.mdpi.com/2079-9292/15/4/869\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"提出 DCES（dynamic center-edge sampling）数据选择框架\"\n      - \"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\"\n    relevance_to_us: \"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\"\n    metrics_studied: [\"ECE\", \"entropy\"]\n\n  # ============================================================\n  # POSITION / SURVEY / EPISTEMICS\n  # ============================================================\n  - id: \"schaeffer2025position\"\n    title: \"Position: Model Collapse Does Not Mean What You Think\"\n    authors: \"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\"\n    venue: \"arXiv (2503.03150)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.03150\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\"\n      - \"许多 collapse 预测依赖于与现实不符的假设\"\n      - \"多种 collapse 场景是可以轻易避免的\"\n    relevance_to_us: \"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\"\n    metrics_studied: []\n\n  - id: \"wang2025epistemic\"\n    title: \"Epistemic Diversity and Knowledge Collapse in Large Language Models\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv (2510.04226)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04226\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\"\n      - \"所有模型的 epistemic diversity 低于基本 web 搜索\"\n      - \"模型越大 epistemic diversity 反而越低；RAG 有正面效果\"\n    relevance_to_us: \"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\"\n    metrics_studied: [\"epistemic diversity\"]\n\n  # ============================================================\n  # METHODOLOGY (GRANGER / LEAD-LAG)\n  # ============================================================\n  - id: \"shojaie2022granger\"\n    title: \"Granger Causality: A Review and Recent Advances\"\n    authors: \"Ali Shojaie, Emily B. Fox\"\n    venue: \"Annual Review of Statistics and Its Application\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2105.02675\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"Granger causality 综述：从经典线性到非线性/neural 方法\"\n      - \"Panel data 场景的 Granger causality 扩展\"\n      - \"VAR 和 neural Granger causality 的对比\"\n    relevance_to_us: \"为我们的 panel Granger causality 分析提供方法论基础\"\n    metrics_studied: []\n\n  - id: \"marcinkevics2022neural\"\n    title: \"Granger Causality Using Neural Networks\"\n    authors: \"Raphael Marcinkevics, Julia Vogt\"\n    venue: \"arXiv (2208.03703)\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2208.03703\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 neural network 估计 Granger causality，突破线性假设\"\n      - \"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\"\n    relevance_to_us: \"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\"\n    metrics_studied: []\n\ngaps:\n  - \"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\"\n  - \"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\"\n  - \"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\"\n  - \"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\"\n  - \"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\"\n  - \"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\"\n  - \"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\"\n  - \"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\"\n\nnovelty_assessment: |\n  我们项目的核心 novelty 在于：\n\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\n     但没有人做过系统的 lead-lag 量化分析。\n\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\n     现有工作都是单一指标或最多两三个指标的孤立分析。\n\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\n     但没人研究 canary 在不同 alpha 下的行为。\n\n  4. **与已有工作的差异**：\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\n       我们将类似思路迁移到 iterative collapse 场景\n\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\n",
    "structuredPatch": [
      {
        "oldStart": 127,
        "oldLines": 6,
        "newStart": 127,
        "newLines": 62,
        "lines": [
          "     gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"",
          "     metrics_studied: [\"convergence rate\", \"population risk\"]",
          " ",
          "+  - id: \"du2026geometric\"",
          "+    title: \"Escaping Mode Collapse in LLM Generation via Geometric Regulation\"",
          "+    authors: \"Du, Tanaka-Ishii\"",
          "+    venue: \"arXiv (2605.00435)\"",
          "+    year: 2026",
          "+    url: \"https://arxiv.org/abs/2605.00435\"",
          "+    category: \"core-collapse\"",
          "+    role: \"background\"",
          "+    key_findings:",
          "+      - \"将 mode collapse 重新解释为表示空间中的 geometric collapse：生成时模型内部轨迹被限制在低维子空间\"",
          "+      - \"提出 RMR（Reinforced Mode Regulation），在 value cache 中抑制 dominant self-reinforcing directions\"",
          "+    relevance_to_us: \"针对推理时 mode collapse，非迭代训练场景。但 'geometric collapse = 低维子空间坍缩' 与我们的 effective rank 指标在概念上有连接，可在 related work 中引用以说明 representation-space collapse 检测的跨场景通用性\"",
          "+    metrics_studied: [\"effective rank proxy\", \"representation dimensionality\"]",
          "+",
          "+  - id: \"gauthier2026alignment\"",
          "+    title: \"Explaining and Preventing Alignment Collapse in Iterative RLHF\"",
          "+    authors: \"Gauthier, Bach, Jordan\"",
          "+    venue: \"arXiv (2605.04266)\"",
          "+    year: 2026",
          "+    url: \"https://arxiv.org/abs/2605.04266\"",
          "+    category: \"core-collapse\"",
          "+    role: \"complementary\"",
          "+    key_findings:",
          "+      - \"迭代 RLHF 中 policy 生成 reward model 的训练数据形成反馈环路，导致 alignment collapse（policy 系统性利用 reward model 盲区）\"",
          "+      - \"用 Stackelberg game 建模迭代 RLHF 的环路动力学，提出 FPO（foresighted policy optimization）\"",
          "+    relevance_to_us: \"RLHF iterative feedback loop 与本项目 iterative synthetic data loop 结构类似——模型输出成为下一轮输入的反馈环路均导致系统性退化。其 'collapse = 反馈环路中的系统性退化' 叙事支持我们的大框架；Stackelberg game 视角可能启发 canary 的博弈论解释\"",
          "+    metrics_studied: [\"alignment score\", \"reward model accuracy\"]",
          "+",
          "+  - id: \"shi2026pruning\"",
          "+    title: \"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\"",
          "+    authors: \"Shi et al.\"",
          "+    venue: \"arXiv (2605.07271)\"",
          "+    year: 2026",
          "+    url: \"https://arxiv.org/abs/2605.07271\"",
          "+    category: \"core-collapse\"",
          "+    role: \"background\"",
          "+    key_findings:",
          "+      - \"层剪枝导致的 performance collapse，定义 Silent Phase（模型预测被单一选项主导 = distributional collapse）和 Decisive Phase\"",
          "+      - \"剪枝 Silent Phase 立即触发 collapse\"",
          "+    relevance_to_us: \"架构剪枝 collapse，非数据驱动。其 'distributional collapse = 预测分布退化为单峰' 的操作定义与我们 token entropy 下降检测的是同一现象的不同表现\"",
          "+    metrics_studied: [\"prediction distribution entropy\", \"task accuracy\"]",
          "+",
          "+  - id: \"tubingen2026diffusion\"",
          "+    title: \"Layer Collapse in Diffusion Language Models\"",
          "+    authors: \"Tübingen AI Center et al.\"",
          "+    venue: \"arXiv (2605.06366)\"",
          "+    year: 2026",
          "+    url: \"https://arxiv.org/abs/2605.06366\"",
          "+    category: \"core-collapse\"",
          "+    role: \"background\"",
          "+    key_findings:",
          "+      - \"LLaDA-8B 中发现层级 activation collapse：少数早期层的 activation 被单个 super-outlier 主导\"",
          "+      - \"剪掉此 outlier 导致模型输出退化为重复随机 token\"",
          "+    relevance_to_us: \"Diffusion LM 的架构 collapse，与迭代合成数据训练无关。但 activation collapse 的表征与 spectral collapse 有交集\"",
          "+    metrics_studied: [\"activation magnitude\", \"output repetition\"]",
          "+",
          "   # ============================================================",
          "   # CANARY / EARLY WARNING METRICS",
          "   # ============================================================"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01QeVtU5g3BuhNVmMWJNtASS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
  "old_string": "    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================",
  "new_string": "    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  - id: \"bergsma2026scaling\"\n    title: \"Scaling with Collapse: Efficient and Predictable Training of LLM Families\"\n    authors: \"Bergsma et al.\"\n    venue: \"arXiv (2509.25087, rev. Mar 2026)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2509.25087\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"'Collapse' 此处指 loss curve 归一化后坍缩到通用轨迹（非 model collapse）\"\n      - \"deviation-from-collapse 作为训练病理的早期诊断信号\"\n    relevance_to_us: \"不同语境下的 'collapse'。但其 '偏离通用轨迹 = 训练出问题' 的监控思路与我们的 canary 理念相似——均从时序异常检测角度切入\"\n    metrics_studied: [\"loss curve deviation\", \"scaling law exponents\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "aedfce89-3711-4da9-8b82-5b7fa7c18ee8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fss7sYHnFKTc1YauqWfJrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16068,
      "cache_read_input_tokens": 42162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16068
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T04:47:33.477Z_

<details><summary>↩ Tool result · `toolu_01QeVtU5g3BuhNVmMWJNtASS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "477c692b-1378-4709-a5d4-fbf7d79ed67c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
    "oldString": "    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================",
    "newString": "    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  - id: \"bergsma2026scaling\"\n    title: \"Scaling with Collapse: Efficient and Predictable Training of LLM Families\"\n    authors: \"Bergsma et al.\"\n    venue: \"arXiv (2509.25087, rev. Mar 2026)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2509.25087\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"'Collapse' 此处指 loss curve 归一化后坍缩到通用轨迹（非 model collapse）\"\n      - \"deviation-from-collapse 作为训练病理的早期诊断信号\"\n    relevance_to_us: \"不同语境下的 'collapse'。但其 '偏离通用轨迹 = 训练出问题' 的监控思路与我们的 canary 理念相似——均从时序异常检测角度切入\"\n    metrics_studied: [\"loss curve deviation\", \"scaling law exponents\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================",
    "originalFile": "papers:\n  # ============================================================\n  # CORE MODEL COLLAPSE\n  # ============================================================\n  - id: \"shumailov2024curse\"\n    title: \"The Curse of Recursion: Training on Generated Data Makes Models Forget\"\n    authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\"\n    venue: \"Nature\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2305.17493\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\"\n      - \"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\"\n      - \"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\"\n      - \"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\"\n    relevance_to_us: \"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\"\n    metrics_studied: [\"perplexity\", \"distributional tail mass\"]\n\n  - id: \"alemohammad2024mad\"\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2307.01850\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"提出 Model Autophagy Disorder (MAD) 概念\"\n      - \"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\"\n      - \"在图像生成领域验证 self-consuming loop 的退化效应\"\n    relevance_to_us: \"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\"\n    metrics_studied: [\"FID\", \"precision\", \"recall\", \"diversity\"]\n\n  - id: \"dohmatob2024tale\"\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.07043\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\"\n      - \"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\"\n      - \"混入少量干净数据可缓解 collapse 并引发 grokking 现象\"\n      - \"在 transformer 算术任务和 Llama2 文本生成上验证\"\n    relevance_to_us: \"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\"\n    metrics_studied: [\"test loss\", \"scaling exponents\"]\n\n  - id: \"dohmatob2025strong\"\n    title: \"Strong Model Collapse\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n    venue: \"ICLR 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.04840\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"即使合成数据占比极小（1/1000），仍可导致 model collapse\"\n      - \"更大的训练集并不能避免 collapse\"\n      - \"更大的模型（random projection 近似下）反而可能放大 collapse\"\n      - \"存在 interpolation threshold 的 double-descent 现象\"\n    relevance_to_us: \"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\"\n    metrics_studied: [\"test loss\", \"population risk\"]\n\n  - id: \"guo2024linguistic\"\n    title: \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\"\n    authors: \"Yanzhu Guo, Guokan Shang, et al.\"\n    venue: \"NAACL 2024 Findings\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.09807\"\n    category: \"core-collapse\"\n    role: \"evaluation\"\n    key_findings:\n      - \"递归微调中，linguistic diversity 在连续迭代中持续下降\"\n      - \"创造性任务中 diversity 下降最显著\"\n      - \"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\"\n    relevance_to_us: \"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\"\n    metrics_studied: [\"distinct-n\", \"type-token ratio\", \"syntactic diversity\", \"semantic diversity\"]\n\n  - id: \"briesch2024selfconsuming\"\n    title: \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\"\n    authors: \"Martin Briesch, Dominik Sobania, Franz Rothlauf\"\n    venue: \"arXiv (2311.16822)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.16822\"\n    category: \"core-collapse\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"首次系统研究 LLM 的 self-consuming training loop\"\n      - \"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\"\n      - \"expanding data cycle（累积）在 50 代内保持 diversity\"\n    relevance_to_us: \"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\"\n    metrics_studied: [\"diversity\", \"quality\"]\n\n  - id: \"truong2025entropy\"\n    title: \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\"\n    authors: \"Truong Xuan Khanh, Truong Quynh Hoa\"\n    venue: \"arXiv (2512.12381)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.12381\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\"\n      - \"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\"\n      - \"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\"\n    relevance_to_us: \"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\"\n    gaps: \"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\"\n    metrics_studied: [\"entropy\", \"autocorrelation\", \"variance\"]\n\n  - id: \"wang2026contaminated\"\n    title: \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\"\n    authors: \"Kevin Wang, Hongqian Niu, Didong Li\"\n    venue: \"arXiv (2602.16065)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16065\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\"\n      - \"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\"\n      - \"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\"\n    relevance_to_us: \"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\"\n    gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"\n    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  - id: \"du2026geometric\"\n    title: \"Escaping Mode Collapse in LLM Generation via Geometric Regulation\"\n    authors: \"Du, Tanaka-Ishii\"\n    venue: \"arXiv (2605.00435)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.00435\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"将 mode collapse 重新解释为表示空间中的 geometric collapse：生成时模型内部轨迹被限制在低维子空间\"\n      - \"提出 RMR（Reinforced Mode Regulation），在 value cache 中抑制 dominant self-reinforcing directions\"\n    relevance_to_us: \"针对推理时 mode collapse，非迭代训练场景。但 'geometric collapse = 低维子空间坍缩' 与我们的 effective rank 指标在概念上有连接，可在 related work 中引用以说明 representation-space collapse 检测的跨场景通用性\"\n    metrics_studied: [\"effective rank proxy\", \"representation dimensionality\"]\n\n  - id: \"gauthier2026alignment\"\n    title: \"Explaining and Preventing Alignment Collapse in Iterative RLHF\"\n    authors: \"Gauthier, Bach, Jordan\"\n    venue: \"arXiv (2605.04266)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.04266\"\n    category: \"core-collapse\"\n    role: \"complementary\"\n    key_findings:\n      - \"迭代 RLHF 中 policy 生成 reward model 的训练数据形成反馈环路，导致 alignment collapse（policy 系统性利用 reward model 盲区）\"\n      - \"用 Stackelberg game 建模迭代 RLHF 的环路动力学，提出 FPO（foresighted policy optimization）\"\n    relevance_to_us: \"RLHF iterative feedback loop 与本项目 iterative synthetic data loop 结构类似——模型输出成为下一轮输入的反馈环路均导致系统性退化。其 'collapse = 反馈环路中的系统性退化' 叙事支持我们的大框架；Stackelberg game 视角可能启发 canary 的博弈论解释\"\n    metrics_studied: [\"alignment score\", \"reward model accuracy\"]\n\n  - id: \"shi2026pruning\"\n    title: \"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv (2605.07271)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.07271\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"层剪枝导致的 performance collapse，定义 Silent Phase（模型预测被单一选项主导 = distributional collapse）和 Decisive Phase\"\n      - \"剪枝 Silent Phase 立即触发 collapse\"\n    relevance_to_us: \"架构剪枝 collapse，非数据驱动。其 'distributional collapse = 预测分布退化为单峰' 的操作定义与我们 token entropy 下降检测的是同一现象的不同表现\"\n    metrics_studied: [\"prediction distribution entropy\", \"task accuracy\"]\n\n  - id: \"tubingen2026diffusion\"\n    title: \"Layer Collapse in Diffusion Language Models\"\n    authors: \"Tübingen AI Center et al.\"\n    venue: \"arXiv (2605.06366)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.06366\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"LLaDA-8B 中发现层级 activation collapse：少数早期层的 activation 被单个 super-outlier 主导\"\n      - \"剪掉此 outlier 导致模型输出退化为重复随机 token\"\n    relevance_to_us: \"Diffusion LM 的架构 collapse，与迭代合成数据训练无关。但 activation collapse 的表征与 spectral collapse 有交集\"\n    metrics_studied: [\"activation magnitude\", \"output repetition\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================\n  - id: \"chen2025scales\"\n    title: \"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\"\n    authors: \"Anonymous\"\n    venue: \"arXiv (2510.05133)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.05133\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\"\n      - \"20% synthetic data 以下性能稳定，30% 以上退化加速\"\n      - \"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\"\n      - \"推理任务比检索任务更易退化\"\n      - \"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\"\n    relevance_to_us: \"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\"\n    metrics_studied: [\"ECE\", \"accuracy\", \"perplexity\"]\n\n  - id: \"gambetta2024surplexity\"\n    title: \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\"\n    authors: \"Daniele Gambetta et al.\"\n    venue: \"arXiv (2410.12341)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.12341\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\"\n      - \"用 semantic networks 分析文本重复性和语义多样性\"\n      - \"用 next-token probability 定量衡量 diversity loss\"\n      - \"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\"\n      - \"不需要区分 human vs AI-generated data\"\n    relevance_to_us: \"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\"\n    metrics_studied: [\"surplexity\", \"semantic network metrics\", \"next-token probability\"]\n\n  - id: \"qiu2025spectral\"\n    title: \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\"\n    authors: \"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\"\n    venue: \"arXiv (2510.04202)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04202\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\"\n      - \"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\"\n      - \"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\"\n      - \"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\"\n    relevance_to_us: \"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\"\n    metrics_studied: [\"spectral alignment\", \"weight norm\", \"gradient norm\"]\n\n  - id: \"he2025closer\"\n    title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n    authors: \"Shiliang He et al.\"\n    venue: \"NeurIPS 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2509.16499\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"识别 diffusion model collapse 中的 generalization → memorization 转变\"\n      - \"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\"\n      - \"提出基于 entropy 的数据选择策略，有效缓解 collapse\"\n    relevance_to_us: \"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\"\n    metrics_studied: [\"entropy\", \"FID\", \"diversity\"]\n\n  - id: \"ba2024fill\"\n    title: \"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\"\n    authors: \"Yang Ba, Michelle V Mancenido, Rong Pan\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.10864\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\"\n      - \"推导了基于 PAC 框架的 ECE bound\"\n      - \"合成数据可改善 calibration 但需精心设计生成策略\"\n    relevance_to_us: \"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\"\n    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  - id: \"sigma2026spectral\"\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: \"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\"\n    venue: \"arXiv (2601.03385)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.03385\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\"\n      - \"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\"\n      - \"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\"\n    relevance_to_us: \"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\"\n    gaps: \"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\"\n    metrics_studied: [\"Gram matrix eigenspectrum\", \"spectral norm bounds\"]\n\n  - id: \"kalinowski2026topology\"\n    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"\n    authors: \"Alexander Kalinowski\"\n    venue: \"arXiv (2604.26984)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.26984\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\"\n      - \"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\"\n      - \"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\"\n    relevance_to_us: \"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\"\n    gaps: \"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\"\n    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================\n  - id: \"zhu2018texygen\"\n    title: \"Texygen: A Benchmarking Platform for Text Generation Models\"\n    authors: \"Yaoming Zhu et al.\"\n    venue: \"SIGIR 2018\"\n    year: 2018\n    url: \"https://arxiv.org/abs/1802.01886\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\"\n      - \"成为文本生成多样性评估的标准基准之一\"\n    relevance_to_us: \"Self-BLEU 是我们 diversity canary 的经典候选\"\n    metrics_studied: [\"Self-BLEU\", \"BLEU\"]\n\n  - id: \"li2016diversity\"\n    title: \"A Diversity-Promoting Objective Function for Neural Conversation Models\"\n    authors: \"Jiwei Li et al.\"\n    venue: \"NAACL 2016\"\n    year: 2016\n    url: \"https://arxiv.org/abs/1510.03055\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\"\n      - \"计算 unique n-gram 数占总 n-gram 数的比例\"\n    relevance_to_us: \"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\"\n    metrics_studied: [\"distinct-1\", \"distinct-2\"]\n\n  # ============================================================\n  # REPRESENTATION / SPECTRAL COLLAPSE\n  # ============================================================\n  - id: \"jing2022understanding\"\n    title: \"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\"\n    authors: \"Li Jing et al.\"\n    venue: \"ICLR 2022\"\n    year: 2022\n    url: \"https://openreview.net/forum?id=YevsQ05DEN7\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"定义 dimensional collapse：embedding 向量只跨越低维子空间\"\n      - \"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\"\n      - \"strong augmentation 和 implicit regularization 驱动低秩解\"\n    relevance_to_us: \"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\"\n    metrics_studied: [\"effective rank\", \"singular value spectrum\"]\n\n  - id: \"noci2024mind\"\n    title: \"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\"\n    authors: \"Lorenzo Noci et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.07799\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 Random Matrix Theory 分析 attention 层的 rank collapse\"\n      - \"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\"\n      - \"rank collapse in depth: 所有 token 沿层收敛到单一表示\"\n    relevance_to_us: \"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\"\n    metrics_studied: [\"spectral gap\", \"singular values\", \"effective rank\"]\n\n  # ============================================================\n  # DATA MIXING & ACCUMULATION\n  # ============================================================\n  - id: \"kazdan2025collapse\"\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: \"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.16713\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"系统对比 replace vs accumulate 场景\"\n      - \"replace → collapse；accumulate → 可避免 collapse\"\n      - \"发现 real data 和 synthetic data 之间存在非平凡的交互效应\"\n      - \"synthetic data 的价值取决于 real data 的绝对数量\"\n    relevance_to_us: \"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"dey2024breaking\"\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: \"Apratim Dey, David Donoho, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.01413\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"替换数据 → 发散 population risk；累积数据 → 避免发散\"\n      - \"证明累积策略在多种模型（GMM, HMM, LLM）上有效\"\n    relevance_to_us: \"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\"\n    metrics_studied: [\"population risk\"]\n\n  - id: \"epstein2024howbad\"\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Mohamed El Amine Epstein et al.\"\n    venue: \"arXiv (2404.05090)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.05090\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"纯合成数据训练不可避免 collapse\"\n      - \"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\"\n      - \"递归训练使原始分布尾部消失\"\n    relevance_to_us: \"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\"\n    metrics_studied: [\"perplexity\"]\n\n  - id: \"fu2025selfconsuming\"\n    title: \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\"\n    authors: \"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.18865\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\"\n      - \"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\"\n      - \"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\"\n    relevance_to_us: \"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\"\n    gaps: \"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\"\n    metrics_studied: [\"generalization bound\", \"population risk\"]\n\n  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi, Sunrit Chakraborty\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\"\n      - \"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\"\n      - \"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\"\n      - \"在 next-token prediction 语言模型上分析完整迭代演化动态\"\n    relevance_to_us: \"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\"\n    gaps: \"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\"\n    metrics_studied: [\"population risk\", \"total variation distance\"]\n\n  # ============================================================\n  # MITIGATION & VERIFICATION\n  # ============================================================\n  - id: \"feng2025escaping\"\n    title: \"Escaping Model Collapse via Synthetic Data Verification\"\n    authors: \"Yunzhen Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.16657\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"通过外部 verifier（human 或 better model）注入信息可避免 collapse\"\n      - \"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\"\n      - \"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\"\n    relevance_to_us: \"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"barzilai2025consistency\"\n    title: \"When Models Don't Collapse: On the Consistency of Iterative MLE\"\n    authors: \"Daniel Barzilai, Ohad Shamir\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2505.19046\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\"\n      - \"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\"\n    relevance_to_us: \"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\"\n    metrics_studied: []\n\n  - id: \"dces2026counter\"\n    title: \"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\"\n    authors: \"Anonymous\"\n    venue: \"MDPI Electronics (2026)\"\n    year: 2026\n    url: \"https://www.mdpi.com/2079-9292/15/4/869\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"提出 DCES（dynamic center-edge sampling）数据选择框架\"\n      - \"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\"\n    relevance_to_us: \"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\"\n    metrics_studied: [\"ECE\", \"entropy\"]\n\n  # ============================================================\n  # POSITION / SURVEY / EPISTEMICS\n  # ============================================================\n  - id: \"schaeffer2025position\"\n    title: \"Position: Model Collapse Does Not Mean What You Think\"\n    authors: \"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\"\n    venue: \"arXiv (2503.03150)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.03150\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\"\n      - \"许多 collapse 预测依赖于与现实不符的假设\"\n      - \"多种 collapse 场景是可以轻易避免的\"\n    relevance_to_us: \"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\"\n    metrics_studied: []\n\n  - id: \"wang2025epistemic\"\n    title: \"Epistemic Diversity and Knowledge Collapse in Large Language Models\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv (2510.04226)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04226\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\"\n      - \"所有模型的 epistemic diversity 低于基本 web 搜索\"\n      - \"模型越大 epistemic diversity 反而越低；RAG 有正面效果\"\n    relevance_to_us: \"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\"\n    metrics_studied: [\"epistemic diversity\"]\n\n  # ============================================================\n  # METHODOLOGY (GRANGER / LEAD-LAG)\n  # ============================================================\n  - id: \"shojaie2022granger\"\n    title: \"Granger Causality: A Review and Recent Advances\"\n    authors: \"Ali Shojaie, Emily B. Fox\"\n    venue: \"Annual Review of Statistics and Its Application\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2105.02675\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"Granger causality 综述：从经典线性到非线性/neural 方法\"\n      - \"Panel data 场景的 Granger causality 扩展\"\n      - \"VAR 和 neural Granger causality 的对比\"\n    relevance_to_us: \"为我们的 panel Granger causality 分析提供方法论基础\"\n    metrics_studied: []\n\n  - id: \"marcinkevics2022neural\"\n    title: \"Granger Causality Using Neural Networks\"\n    authors: \"Raphael Marcinkevics, Julia Vogt\"\n    venue: \"arXiv (2208.03703)\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2208.03703\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 neural network 估计 Granger causality，突破线性假设\"\n      - \"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\"\n    relevance_to_us: \"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\"\n    metrics_studied: []\n\ngaps:\n  - \"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\"\n  - \"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\"\n  - \"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\"\n  - \"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\"\n  - \"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\"\n  - \"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\"\n  - \"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\"\n  - \"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\"\n\nnovelty_assessment: |\n  我们项目的核心 novelty 在于：\n\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\n     但没有人做过系统的 lead-lag 量化分析。\n\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\n     现有工作都是单一指标或最多两三个指标的孤立分析。\n\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\n     但没人研究 canary 在不同 alpha 下的行为。\n\n  4. **与已有工作的差异**：\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\n       我们将类似思路迁移到 iterative collapse 场景\n\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\n",
    "structuredPatch": [
      {
        "oldStart": 298,
        "oldLines": 6,
        "newStart": 298,
        "newLines": 20,
        "lines": [
          "     gaps: \"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\"",
          "     metrics_studied: [\"Collapse Index\", \"persistent homology features\"]",
          " ",
          "+  - id: \"bergsma2026scaling\"",
          "+    title: \"Scaling with Collapse: Efficient and Predictable Training of LLM Families\"",
          "+    authors: \"Bergsma et al.\"",
          "+    venue: \"arXiv (2509.25087, rev. Mar 2026)\"",
          "+    year: 2026",
          "+    url: \"https://arxiv.org/abs/2509.25087\"",
          "+    category: \"canary-metrics\"",
          "+    role: \"background\"",
          "+    key_findings:",
          "+      - \"'Collapse' 此处指 loss curve 归一化后坍缩到通用轨迹（非 model collapse）\"",
          "+      - \"deviation-from-collapse 作为训练病理的早期诊断信号\"",
          "+    relevance_to_us: \"不同语境下的 'collapse'。但其 '偏离通用轨迹 = 训练出问题' 的监控思路与我们的 canary 理念相似——均从时序异常检测角度切入\"",
          "+    metrics_studied: [\"loss curve deviation\", \"scaling law exponents\"]",
          "+",
          "   # ============================================================",
          "   # DIVERSITY METRICS (BACKGROUND)",
          "   # ============================================================"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Both edits succeeded. Now I need to save this file via the MCP tool (save_project_file) since the file is managed by the project system. Wait - actually, I edited the file directly using the Edit tool on the filesystem path. But the file is managed by the MCP project system. Let me check - does save_project_file need to be used, or is direct editing fine?

Looking at the save_project_file description: "Write a project file (unified entry point, strict whitelist). Writable: memory.md, writing_plan.yaml, paper_framing.md. Other files have dedicated tools..."


Since literature_map.yaml isn't on the whitelist, direct file editing is the right approach. Let me read the file back to verify the changes took and that the YAML syntax is valid.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "59387a2f-498d-44ea-b8ec-a037223292d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dwsd796ztTVPKQmuU4aph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2346,
      "cache_read_input_tokens": 58230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2346
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 23_

两处插入完成。验证文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "d09d268d-c004-428e-9600-116d9ea84af8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dwsd796ztTVPKQmuU4aph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2346,
      "cache_read_input_tokens": 58230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2346
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01UD5ra51hxGgjmkHoznm4Sj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
  "offset": 126,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "451205f4-0a64-4199-b281-c50aaeba5371",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dwsd796ztTVPKQmuU4aph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2346,
      "cache_read_input_tokens": 58230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2346
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T04:47:43.345Z_

<details><summary>↩ Tool result · `toolu_01UD5ra51hxGgjmkHoznm4Sj`</summary>

```text
126	    relevance_to_us: "为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率"
127	    gaps: "universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为"
128	    metrics_studied: ["convergence rate", "population risk"]
129	
130	  - id: "du2026geometric"
131	    title: "Escaping Mode Collapse in LLM Generation via Geometric Regulation"
132	    authors: "Du, Tanaka-Ishii"
133	    venue: "arXiv (2605.00435)"
134	    year: 2026
135	    url: "https://arxiv.org/abs/2605.00435"
136	    category: "core-collapse"
137	    role: "background"
138	    key_findings:
139	      - "将 mode collapse 重新解释为表示空间中的 geometric collapse：生成时模型内部轨迹被限制在低维子空间"
140	      - "提出 RMR（Reinforced Mode Regulation），在 value cache 中抑制 dominant self-reinforcing directions"
141	    relevance_to_us: "针对推理时 mode collapse，非迭代训练场景。但 'geometric collapse = 低维子空间坍缩' 与我们的 effective rank 指标在概念上有连接，可在 related work 中引用以说明 representation-space collapse 检测的跨场景通用性"
142	    metrics_studied: ["effective rank proxy", "representation dimensionality"]
143	
144	  - id: "gauthier2026alignment"
145	    title: "Explaining and Preventing Alignment Collapse in Iterative RLHF"
146	    authors: "Gauthier, Bach, Jordan"
147	    venue: "arXiv (2605.04266)"
148	    year: 2026
149	    url: "https://arxiv.org/abs/2605.04266"
150	    category: "core-collapse"
151	    role: "complementary"
152	    key_findings:
153	      - "迭代 RLHF 中 policy 生成 reward model 的训练数据形成反馈环路，导致 alignment collapse（policy 系统性利用 reward model 盲区）"
154	      - "用 Stackelberg game 建模迭代 RLHF 的环路动力学，提出 FPO（foresighted policy optimization）"
155	    relevance_to_us: "RLHF iterative feedback loop 与本项目 iterative synthetic data loop 结构类似——模型输出成为下一轮输入的反馈环路均导致系统性退化。其 'collapse = 反馈环路中的系统性退化' 叙事支持我们的大框架；Stackelberg game 视角可能启发 canary 的博弈论解释"
156	    metrics_studied: ["alignment score", "reward model accuracy"]
157	
158	  - id: "shi2026pruning"
159	    title: "Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions"
160	    authors: "Shi et al."
161	    venue: "arXiv (2605.07271)"
162	    year: 2026
163	    url: "https://arxiv.org/abs/2605.07271"
164	    category: "core-collapse"
165	    role: "background"
166	    key_findings:
167	      - "层剪枝导致的 performance collapse，定义 Silent Phase（模型预测被单一选项主导 = distributional collapse）和 Decisive Phase"
168	      - "剪枝 Silent Phase 立即触发 collapse"
169	    relevance_to_us: "架构剪枝 collapse，非数据驱动。其 'distributional collapse = 预测分布退化为单峰' 的操作定义与我们 token entropy 下降检测的是同一现象的不同表现"
170	    metrics_studied: ["prediction distribution entropy", "task accuracy"]
171	
172	  - id: "tubingen2026diffusion"
173	    title: "Layer Collapse in Diffusion Language Models"
174	    authors: "Tübingen AI Center et al."
175	    venue: "arXiv (2605.06366)"
176	    year: 2026
177	    url: "https://arxiv.org/abs/2605.06366"
178	    category: "core-collapse"
179	    role: "background"
180	    key_findings:
181	      - "LLaDA-8B 中发现层级 activation collapse：少数早期层的 activation 被单个 super-outlier 主导"
182	      - "剪掉此 outlier 导致模型输出退化为重复随机 token"
183	    relevance_to_us: "Diffusion LM 的架构 collapse，与迭代合成数据训练无关。但 activation collapse 的表征与 spectral collapse 有交集"
184	    metrics_studied: ["activation magnitude", "output repetition"]
185	
186	  # ============================================================
187	  # CANARY / EARLY WARNING METRICS
188	  # ============================================================
189	  - id: "chen2025scales"
190	    title: "Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios"
191	    authors: "Anonymous"
192	    venue: "arXiv (2510.05133)"
193	    year: 2025
194	    url: "https://arxiv.org/abs/2510.05133"
195	    category: "canary-metrics"
196	    role: "direct-competitor"
197	    key_findings:
198	      - "**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal"
199	      - "20% synthetic data 以下性能稳定，30% 以上退化加速"
200	      - "大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒"
201	      - "推理任务比检索任务更易退化"
202	      - "iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）"
203	    relevance_to_us: "**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架"
204	    metrics_studied: ["ECE", "accuracy", "perplexity"]
205	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "69fb861a-4f23-4e41-8350-3593d6bb3c16",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
      "content": "    relevance_to_us: \"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\"\n    gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"\n    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  - id: \"du2026geometric\"\n    title: \"Escaping Mode Collapse in LLM Generation via Geometric Regulation\"\n    authors: \"Du, Tanaka-Ishii\"\n    venue: \"arXiv (2605.00435)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.00435\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"将 mode collapse 重新解释为表示空间中的 geometric collapse：生成时模型内部轨迹被限制在低维子空间\"\n      - \"提出 RMR（Reinforced Mode Regulation），在 value cache 中抑制 dominant self-reinforcing directions\"\n    relevance_to_us: \"针对推理时 mode collapse，非迭代训练场景。但 'geometric collapse = 低维子空间坍缩' 与我们的 effective rank 指标在概念上有连接，可在 related work 中引用以说明 representation-space collapse 检测的跨场景通用性\"\n    metrics_studied: [\"effective rank proxy\", \"representation dimensionality\"]\n\n  - id: \"gauthier2026alignment\"\n    title: \"Explaining and Preventing Alignment Collapse in Iterative RLHF\"\n    authors: \"Gauthier, Bach, Jordan\"\n    venue: \"arXiv (2605.04266)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.04266\"\n    category: \"core-collapse\"\n    role: \"complementary\"\n    key_findings:\n      - \"迭代 RLHF 中 policy 生成 reward model 的训练数据形成反馈环路，导致 alignment collapse（policy 系统性利用 reward model 盲区）\"\n      - \"用 Stackelberg game 建模迭代 RLHF 的环路动力学，提出 FPO（foresighted policy optimization）\"\n    relevance_to_us: \"RLHF iterative feedback loop 与本项目 iterative synthetic data loop 结构类似——模型输出成为下一轮输入的反馈环路均导致系统性退化。其 'collapse = 反馈环路中的系统性退化' 叙事支持我们的大框架；Stackelberg game 视角可能启发 canary 的博弈论解释\"\n    metrics_studied: [\"alignment score\", \"reward model accuracy\"]\n\n  - id: \"shi2026pruning\"\n    title: \"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv (2605.07271)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.07271\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"层剪枝导致的 performance collapse，定义 Silent Phase（模型预测被单一选项主导 = distributional collapse）和 Decisive Phase\"\n      - \"剪枝 Silent Phase 立即触发 collapse\"\n    relevance_to_us: \"架构剪枝 collapse，非数据驱动。其 'distributional collapse = 预测分布退化为单峰' 的操作定义与我们 token entropy 下降检测的是同一现象的不同表现\"\n    metrics_studied: [\"prediction distribution entropy\", \"task accuracy\"]\n\n  - id: \"tubingen2026diffusion\"\n    title: \"Layer Collapse in Diffusion Language Models\"\n    authors: \"Tübingen AI Center et al.\"\n    venue: \"arXiv (2605.06366)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.06366\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"LLaDA-8B 中发现层级 activation collapse：少数早期层的 activation 被单个 super-outlier 主导\"\n      - \"剪掉此 outlier 导致模型输出退化为重复随机 token\"\n    relevance_to_us: \"Diffusion LM 的架构 collapse，与迭代合成数据训练无关。但 activation collapse 的表征与 spectral collapse 有交集\"\n    metrics_studied: [\"activation magnitude\", \"output repetition\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================\n  - id: \"chen2025scales\"\n    title: \"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\"\n    authors: \"Anonymous\"\n    venue: \"arXiv (2510.05133)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.05133\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\"\n      - \"20% synthetic data 以下性能稳定，30% 以上退化加速\"\n      - \"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\"\n      - \"推理任务比检索任务更易退化\"\n      - \"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\"\n    relevance_to_us: \"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\"\n    metrics_studied: [\"ECE\", \"accuracy\", \"perplexity\"]\n",
      "numLines": 80,
      "startLine": 126,
      "totalLines": 606
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01X49SENXmnnzCGDhWBwmGvi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
  "offset": 280,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "fcb06249-fef8-40e9-be6f-fb0752e9cb9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dwsd796ztTVPKQmuU4aph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2346,
      "cache_read_input_tokens": 58230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2346
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T04:47:43.966Z_

<details><summary>↩ Tool result · `toolu_01X49SENXmnnzCGDhWBwmGvi`</summary>

```text
280	      - "随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控"
281	    relevance_to_us: "最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成"
282	    gaps: "未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略"
283	    metrics_studied: ["Gram matrix eigenspectrum", "spectral norm bounds"]
284	
285	  - id: "kalinowski2026topology"
286	    title: "Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index"
287	    authors: "Alexander Kalinowski"
288	    venue: "arXiv (2604.26984)"
289	    year: 2026
290	    url: "https://arxiv.org/abs/2604.26984"
291	    category: "canary-metrics"
292	    role: "background"
293	    key_findings:
294	      - "提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建"
295	      - "Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning"
296	      - "拓扑方法捕捉表示空间的各向异性和多尺度结构丧失"
297	    relevance_to_us: "topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由"
298	    gaps: "计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比"
299	    metrics_studied: ["Collapse Index", "persistent homology features"]
300	
301	  - id: "bergsma2026scaling"
302	    title: "Scaling with Collapse: Efficient and Predictable Training of LLM Families"
303	    authors: "Bergsma et al."
304	    venue: "arXiv (2509.25087, rev. Mar 2026)"
305	    year: 2026
306	    url: "https://arxiv.org/abs/2509.25087"
307	    category: "canary-metrics"
308	    role: "background"
309	    key_findings:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "c3b00690-048b-429f-ada1-54ab9e0b60c7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
      "content": "      - \"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\"\n    relevance_to_us: \"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\"\n    gaps: \"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\"\n    metrics_studied: [\"Gram matrix eigenspectrum\", \"spectral norm bounds\"]\n\n  - id: \"kalinowski2026topology\"\n    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"\n    authors: \"Alexander Kalinowski\"\n    venue: \"arXiv (2604.26984)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.26984\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\"\n      - \"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\"\n      - \"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\"\n    relevance_to_us: \"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\"\n    gaps: \"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\"\n    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  - id: \"bergsma2026scaling\"\n    title: \"Scaling with Collapse: Efficient and Predictable Training of LLM Families\"\n    authors: \"Bergsma et al.\"\n    venue: \"arXiv (2509.25087, rev. Mar 2026)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2509.25087\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:",
      "numLines": 30,
      "startLine": 280,
      "totalLines": 606
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Both insertions look correct. Let me also verify the YAML syntax by running a quick check.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "1e394523-219d-4176-9cef-d3eb318435d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qij9v6DBfs2vX4A4UyKES",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3249,
      "cache_read_input_tokens": 60576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3249
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 29_

插入正确。验证 YAML 语法。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "3e1cea65-4a8c-4e35-93e6-f395be1288d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qij9v6DBfs2vX4A4UyKES",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3249,
      "cache_read_input_tokens": 60576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3249
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01EDFLT7719KSSchg5X1EQxo`</summary>

```json
{
  "command": "python3 -c \"import yaml; yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml')); print('YAML valid')\"",
  "description": "Validate YAML syntax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "54cfe3ba-5070-4478-9a9a-821e4445b00e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qij9v6DBfs2vX4A4UyKES",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3249,
      "cache_read_input_tokens": 60576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3249
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T04:47:51.050Z_

<details><summary>↩ Tool result · `toolu_01EDFLT7719KSSchg5X1EQxo`</summary>

```text
YAML valid
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "dce5f763-6b0a-4c19-a50d-3ab3a331b7ea",
  "tool_use_result": {
    "stdout": "YAML valid",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01LHkQtNkwqvo3WfLsJChhkj`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\ndata = yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml'))\nnew_ids = ['du2026geometric', 'gauthier2026alignment', 'shi2026pruning', 'tubingen2026diffusion', 'bergsma2026scaling']\nfor nid in new_ids:\n    found = [p for p in data['papers'] if p['id'] == nid]\n    if found:\n        p = found[0]\n        print(f\\\"✓ {nid}: role={p['role']}, category={p['category']}\\\")\n    else:\n        print(f\\\"✗ {nid}: NOT FOUND\\\")\n# Check Gauthier relevance\ng = [p for p in data['papers'] if p['id'] == 'gauthier2026alignment'][0]\nassert 'RLHF iterative feedback loop' in g['relevance_to_us'], 'Missing RLHF mention'\nassert 'iterative synthetic data loop' in g['relevance_to_us'], 'Missing synthetic loop mention'\nprint(f\\\"✓ Gauthier relevance_to_us contains required phrases\\\")\nprint(f\\\"Total papers: {len(data['papers'])}\\\")\n\"",
  "description": "Verify all 5 new papers and Gauthier constraints"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "055ae648-d696-418d-8162-f405be7cf27c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qij9v6DBfs2vX4A4UyKES",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3249,
      "cache_read_input_tokens": 60576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3249
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T04:47:56.515Z_

<details><summary>↩ Tool result · `toolu_01LHkQtNkwqvo3WfLsJChhkj`</summary>

```text
✓ du2026geometric: role=background, category=core-collapse
✓ gauthier2026alignment: role=complementary, category=core-collapse
✓ shi2026pruning: role=background, category=core-collapse
✓ tubingen2026diffusion: role=background, category=core-collapse
✓ bergsma2026scaling: role=background, category=canary-metrics
✓ Gauthier relevance_to_us contains required phrases
Total papers: 36
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "fc3502d3-77e5-4f7f-a35e-840160f52843",
  "tool_use_result": {
    "stdout": "✓ du2026geometric: role=background, category=core-collapse\n✓ gauthier2026alignment: role=complementary, category=core-collapse\n✓ shi2026pruning: role=background, category=core-collapse\n✓ tubingen2026diffusion: role=background, category=core-collapse\n✓ bergsma2026scaling: role=background, category=canary-metrics\n✓ Gauthier relevance_to_us contains required phrases\nTotal papers: 36",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 34_

5 篇全部添加完成，从 31 篇增加到 36 篇。

- `du2026geometric` — core-collapse / background
- `gauthier2026alignment` — core-collapse / **complementary**，relevance_to_us 包含 RLHF iterative feedback loop 与 iterative synthetic data loop 的结构类似性说明
- `shi2026pruning` — core-collapse / background
- `tubingen2026diffusion` — core-collapse / background
- `bergsma2026scaling` — canary-metrics / background

YAML 语法验证通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "uuid": "6567d56b-cfe5-45b4-8816-6bd6f5a40726",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qxNee2a3HHbrJ7XW23jJN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 767,
      "cache_read_input_tokens": 63825,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 767
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 35_

5 篇全部添加完成，从 31 篇增加到 36 篇。

- `du2026geometric` — core-collapse / background
- `gauthier2026alignment` — core-collapse / **complementary**，relevance_to_us 包含 RLHF iterative feedback loop 与 iterative synthetic data loop 的结构类似性说明
- `shi2026pruning` — core-collapse / background
- `tubingen2026diffusion` — core-collapse / background
- `bergsma2026scaling` — canary-metrics / background

YAML 语法验证通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 185946,
  "duration_api_ms": 186905,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "4bcb29ca-ba81-47d6-a99a-aa9e46aab2d7",
  "total_cost_usd": 0.6790747500000001,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 52751,
    "cache_read_input_tokens": 284010,
    "output_tokens": 8235,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 52751,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 158,
        "cache_read_input_tokens": 63825,
        "cache_creation_input_tokens": 767,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 767
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1341,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001446,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 8235,
      "cacheReadInputTokens": 284010,
      "cacheCreationInputTokens": 52751,
      "webSearchRequests": 0,
      "costUSD": 0.67762875,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "37730b85-e241-476c-aaea-db67f5fe909a"
}
```

</details>

---
