# N≥17 Real-Data 扩展可行性报告

> 调研日期: 2026-05-23 | DDL: 2026-05-26 | 结论: **可行，预计 1.5-2 天完成**

---

## 1. 当前数据管线结构

```
Arena-Hard 500 prompts
  → target model responses (data/arena_hard/responses/*.jsonl)
  → 9 judges pairwise evaluation vs gpt-4-0314 (exp001/results/*/arena_hard_judgments.jsonl)
  → per-item exposure estimation (exp002/results/exposure_scores.csv, 317 items)
  → G-MFRM MCMC fitting (exp003/, NumPyro NUTS)
  → evaluation: Kendall τ vs Chatbot Arena ELO (exp003/evaluation.py, ARENA_ELO dict)
```

**当前规模**: N=8 targets, J=9 judges, I=316 filtered items, n_obs=4,250

**9 judges**: gpt-5.5, claude-opus-4.7, claude-sonnet-4.6, gemini-2.5-pro, deepseek-v4-pro, qwen3-235b (API) + llama-3.3-70b, qwen2.5-72b, mistral-large-2 (local vLLM)

**关键: 代码完全数据驱动**, N/I/J 从数据动态推断, 无硬编码。exp-018 已在 N=20 synthetic 上成功运行。

---

## 2. 候选模型列表

### 2A. 已有本地 responses 但未做 judge 评测的模型 (4 个)

| 模型 | Responses | Judge 评测 | Chatbot Arena ELO | 备注 |
|------|:---------:|:----------:|:-----------------:|------|
| claude-opus-4.7 | ✅ 500 | ❌ | ~1350 (est.) | **同时是 judge** |
| claude-sonnet-4.6 | ✅ 500 | ❌ | ~1310 (est.) | **同时是 judge** |
| gpt-5.5 | ✅ 500 | ❌ | ~1340 (est.) | **同时是 judge** |
| mistral-large-2 | ✅ 500 | ❌ | 1158 | **同时是 judge** |

> ⚠️ 全部 4 个都是 judges, 加入后 judge-target overlap 从 2/8 (25%) 升至 6/12 (50%). 虽然 exp-024 确认 self-evaluation robust, 但 50% overlap 可能引起 reviewer 质疑.

### 2B. Arena-Hard v0.1 HF 数据集可下载的模型 (推荐)

来源: `huggingface.co/datasets/lmarena-ai/arena-hard-auto`, 76 个模型有预生成 responses.

**推荐扩展 9 个模型 (达到 N=17):**

| # | 模型 | Arena ELO (est.) | 模型类型 | Arena-Hard response | 选择理由 |
|---|------|:----------------:|:--------:|:-------------------:|----------|
| 1 | claude-3-5-sonnet-20241022 | ~1299 | 商用 | ✅ HF | 高 ELO, 丰富上端 |
| 2 | gpt-4-turbo-2024-04-09 | ~1290 | 商用 | ✅ HF | GPT-4 variant |
| 3 | llama-3.1-70b-instruct | ~1265 | 开源 70B | ✅ HF | 中高, Llama 多样性 |
| 4 | gemma-2-27b-it | ~1248 | 开源 27B | ✅ HF | 中档, 已有 9b 版本 |
| 5 | claude-3-opus-20240229 | ~1265 | 商用 | ✅ HF | 旧 frontier |
| 6 | llama-3-70b-instruct | ~1224 | 开源 70B | ✅ HF | 中档, 旧 Llama |
| 7 | mixtral-8x22b-instruct-v0.1 | ~1215 | 开源 MoE | ✅ HF | MoE 架构多样性 |
| 8 | claude-3-haiku-20240307 | ~1195 | 商用小模型 | ✅ HF | 低端商用 |
| 9 | llama-3-8b-instruct | ~1165 | 开源 8B | ✅ HF | 低端, 扩大 ELO 范围 |

**扩展后 ELO 分布**: ~1105 (gpt-3.5) → ~1299 (claude-3.5-sonnet), 跨度 194 点, 17 个数据点.

### 2C. 备选方案: N=20+ (如需进一步扩展)

额外可选 (均有 HF responses + Arena ELO):

| 模型 | Arena ELO | 备注 |
|------|:---------:|------|
| llama-3.1-405b-instruct-fp8 | ~1310 | 超大模型, 高 ELO |
| o1-preview-2024-09-12 | ~1340 | 推理模型, 行为模式不同 |
| gemini-1.5-pro-api-0514 | ~1290 | Gemini 系列 |
| mistral-large-2407 | ~1269 | 注意与 judge mistral-large-2 版本相近 |
| qwen2-72b-instruct | ~1260 | Qwen 旧版, 与 qwen2.5-72b 重叠 |
| command-r-plus | ~1233 | Cohere 系列 |
| mixtral-8x7b-instruct-v0.1 | ~1170 | 小 MoE |
| llama-2-70b-chat | ~1140 | 极低端 |

---

## 3. 工作量分解

### Phase 1: 数据准备 (2-3h)

| 步骤 | 时间 | 说明 |
|------|------|------|
| 下载 Arena-Hard v0.1 HF 数据集 | 30min | `git lfs clone`, ~3.3GB |
| 格式转换: HF → 项目格式 | 30min | uid+messages → id+response, 脚本 ~30 行 |
| 验证 item_id 匹配 | 15min | 确认 500 prompts uid 一致 |
| 筛选 9 个目标模型 responses | 15min | 复制到 data/arena_hard/responses/ |
| 查询并更新 ARENA_ELO 字典 | 30min | 从 Chatbot Arena 获取精确 ELO, 更新 evaluation.py |

### Phase 2: Judge 评测 (3-4h wall time)

**每新模型**: 500 items × 2 positions × 9 judges = 9,000 calls
**总计**: 9 models × 9,000 = 81,000 calls

| Judge | RPM | 9 models 时间 | 并行化 |
|-------|-----|:------------:|:------:|
| claude-opus-4.7 | 50 | 3h | 瓶颈 |
| claude-sonnet-4.6 | 50 | 3h | 与 opus 并行 |
| gpt-5.5 | 200 | 45min | ✅ |
| gemini-2.5-pro | 150 | 1h | ✅ |
| deepseek-v4-pro | 300 | 30min | ✅ |
| qwen3-235b | 100 | 1.5h | ✅ |
| llama-3.3-70b (local) | ~100 | 1.5h | 需启动 vLLM |
| qwen2.5-72b (local) | ~100 | 1.5h | 需启动 vLLM |
| mistral-large-2 (local) | ~100 | 1.5h | 顺序执行 |

**Wall time**: ~3-4h (瓶颈: claude 系列 50 RPM)
**Local vLLM**: rtx6000-4x 4 卡可同时跑 2 × 70B 模型, 第 3 个顺序

### Phase 3: Pipeline 运行 (14-18h)

| 步骤 | 时间 | GPU |
|------|------|-----|
| exp-002 re-run (exposure scores) | 30min | CPU only |
| exp-003 G-MFRM fitting (N=17) | 10-14h | 1× GPU |
| exp-004 baselines re-run | 1-2h | CPU |
| Bootstrap Δτ | 2-3h | 1× GPU |

MCMC 参数量: 2×17+9+I+1 ≈ 360 (vs 当前 350), 增量小.
观测量: ~4250 × (17/8) ≈ 9,031 (线性增长).

### Phase 4: Paper 更新 (2-4h)

| 步骤 | 时间 |
|------|------|
| 更新 Table 1 (model list) | 30min |
| 更新 Table 2/3 (results) | 30min |
| 更新 Figure 3 (θ vs ELO scatter) | 30min |
| 更新 bootstrap CI / Δτ narrative | 1h |
| 更新 abstract/intro claims | 30min |

### 总时间线

| 天 | 活动 | 累计 |
|----|------|------|
| Day 1 (5/24) | Phase 1 + Phase 2 (并行 API calls) | 数据就绪 |
| Day 1-2 (5/24-25) | Phase 3 (MCMC overnight) | 结果就绪 |
| Day 2 (5/25) | Phase 4 (paper update) | **完成** |

**Buffer**: 0.5-1 天 for 问题排查

---

## 4. 成本估算

### Judge 评测 API 成本

每次 call: ~1,426 input tokens + ~420 output tokens

| Judge | Input $/1M | Output $/1M | Per-model (1000 calls) | 9 models 总计 |
|-------|:---------:|:----------:|:---------------------:|:------------:|
| gpt-5.5 | $15 | $60 | $46.59 | $419 |
| claude-opus-4.7 | $15 | $75 | $52.89 | $476 |
| claude-sonnet-4.6 | $3 | $15 | $10.58 | $95 |
| gemini-2.5-pro | $2.50 | $15 | $9.87 | $89 |
| deepseek-v4-pro | $2 | $8 | $6.21 | $56 |
| qwen3-235b | $2 | $6 | $5.37 | $48 |
| **API subtotal** | | | **$131.51** | **$1,184** |
| llama/qwen/mistral (local) | — | — | $0 | $0 |
| **Total** | | | **$131.51** | **$1,184** |

### 成本优化选项

| 方案 | 成本 | 牺牲 |
|------|:----:|------|
| 全量 (推荐) | $1,184 | 无 |
| 去掉 gpt-5.5 judge | $765 | 少 1 judge (J=8), 影响 d_j profile |
| 去掉 gpt-5.5 + opus judges | $289 | 少 2 judges (J=7), 丢失最贵但最有信息量的 judges |
| 仅 5 models (N=13) | $658 | N=13 < 17 target, Δτ 可能仍不显著 |

### 其他成本
- **Response 生成**: $0 (用 HF 预生成数据)
- **GPU 计算**: $0 (用项目服务器)
- **总预算**: ~$1,200

---

## 5. 风险点和建议

### 高风险

| 风险 | 影响 | 缓解 |
|------|------|------|
| **Chatbot Arena ELO 不精确** | τ 计算依赖 ground truth 排名, ELO 误差直接影响评估 | 用官方 API/数据集获取精确 ELO; 仅选 ELO CI 不重叠的模型 |
| **Arena-Hard v0.1 responses 格式不匹配** | 需转换 `messages[].content.answer` → `response` 字段 | 转换脚本 trivial (~30 行); 验证 item_id 匹配 |
| **Δτ 仍不显著** | 即使 N=17, real-data model-data mismatch 可能导致 Δτ 依然不显著 | exp-015/018 已证明这是 DGP limitation 而非 power issue; N=17 下 τ 分辨率提高 (1/C(17,2)=0.0074 vs 1/C(8,2)=0.036) |

### 中风险

| 风险 | 影响 | 缓解 |
|------|------|------|
| **MCMC 收敛问题 (N=17)** | 参数增加可能加剧 posterior geometry 困难 | exp-018 N=20 synthetic 已收敛; 增加 warmup 到 6000 作为保险 |
| **exp-002 exposure 变化** | 新 judgment 数据可能改变 per-item e_i | exp-002 以 item 属性为主, 不依赖 target model set; 重跑验证即可 |
| **API rate limit / 超时** | claude-opus 50 RPM 是瓶颈 | collect.py 支持 resume; 失败后重跑补充 |

### 低风险

| 风险 | 影响 | 缓解 |
|------|------|------|
| **旧模型 responses 质量** | llama-3-8b 等弱模型 win rate 极低, 可能导致数据极度偏斜 | data_loader 已有 tie filtering; MFRM 设计处理 imbalanced data |
| **Judge-target overlap** | 推荐方案仅保持 2/17 overlap (12%), 低于当前 2/8 (25%) | 已验证 self-eval robust; 推荐方案避开 judge 模型 |
| **Paper 页面溢出** | 表格扩大到 17 模型 | 用 Appendix 放完整表格, 正文用 summary |

### 建议

1. **立即执行**: N=17 方案技术可行, 成本 ~$1,200, 2 天可完成, 在 DDL 内
2. **优先用 HF 预生成 responses**: 避免 judge-target overlap, 节省 response 生成时间
3. **ELO 验证优先**: 在开始 judge 评测前, 先确认所有 17 个模型都有可靠的 Chatbot Arena ELO
4. **备选降级方案**: 若预算紧张, 可只加 5 个模型到 N=13 ($658), 但 N=17 审稿效果更好
5. **qwen3-8b ELO 确认**: 当前 8 models 中 qwen3-8b 较新, 需确认其 Arena ELO 是否稳定
