# research literature scan emnlp

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_scan_emnlp_20260515T093405_result.json`
- **Structured JSON:** [`bfd409d4d011892f02a0.json`](../../sessions/bf/bfd409d4d011892f02a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

literature_map.yaml 已更新。下面输出文献扫描报告。

---

## 文献扫描报告（2026-05-15）

### 一、新增条目（6 篇）

| ID | 标题 | Venue | 方向 | 与我们的关系 |
|---|---|---|---|---|
| `wang_2026_survive_contamination` | Can Generative AI Survive Data Contamination? | arXiv 2026 | **τ 的理论动机** | α = m₁/(m₁+m₂) 是已知设计参数，收敛率 = min(baseline, α)。与 Claim 3 (proportion-free) 有张力——需在论文中讨论 τ 作为 α 的 proxy |
| `chen_2025_aioli` | Aioli: Unified Optimization for LM Data Mixing | ICLR 2025 | 自适应加权 (non-grid-search) | 最直接的在线自适应对比：domain-level loss-driven vs 我们的 instance-level α_eff-based |
| `yang_2026_data_mixing_agent` | Data Mixing Agent | ACL 2026 | 数据加权 / 自适应 | RL-based domain reweighting，另一条非 grid-search 路线 |
| `cheng_2025_contamination_survey` | A Survey on Data Contamination for LLMs | arXiv 2025 | 合成数据污染 | 全面综述，支撑 problem statement |
| `wei_2024_data_watermarks` | Proving Membership via Data Watermarks | arXiv 2024 | 数据溯源/检测 | 主动 provenance (事前水印) vs 我们的被动方案 (事后检测) |
| — | (Wang et al. 同时归类 theoretical-foundation) | | | |

### 二、修正条目（2 处）

1. **`feng_2024_beyond_collapse`** → 改为 `feng_2025_beyond_collapse`
   - venue: ~~arXiv preprint~~ → **ICLR 2025**
   - year: ~~2024~~ → **2025**

2. **`xie_2023_doremi`** 标题错误
   - ~~"DoReMi: Optimizing Data Mixtures by Predicting Language Modeling Performance"~~
   - → **"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining"**
   - （原标题是 Ye et al. Data Mixing Laws 的副标题，误用到了 DoReMi 上）

### 三、现有条目验证（7 篇抽查）

| 条目 | 标注 venue/year | 验证结果 |
|---|---|---|
| drayson_2025 | EMNLP 2025 | **正确** |
| shumailov_2024 | Nature 2024 | **正确** |
| dohmatob_2025 | ICLR 2025 (Spotlight) | **正确** |
| vehtari_2024 | JMLR 2024 | **正确** (Vol 25, Article 72) |
| kimura_2024 | TMLR 2024 | **正确** |
| sow_2025 | ICLR 2025 | **正确** |
| ye_2025 | ICLR 2025 | **正确** |

### 四、各方向搜索总结

**Data provenance / data weighting (2024-2026)**：新增 AIOLI (online mixing law optimization) 和 Data Mixing Agent (RL-based)。两者都是 domain-level，不处理 instance-level 污染。

**Importance sampling + ESS in ML training**：已有 Vehtari (PSIS) 和 Kimura (IW survey) 覆盖充分。Wang 2026 补充了 α (ESS-like) 的收敛理论。未发现直接将 ESS 约束用于 training weight selection 的其他工作——我们的方法在此方向是新颖的。

**Synthetic data detection / contamination**：新增 Cheng 2025 综述和 Wei 2024 水印方案。综述可用于 Related Work 的 problem motivation 段；水印方案与我们的被动检测形成互补对比。

**Adaptive weighting (non-grid-search)**：AIOLI 是最强对比——在线估计 mixing law 参数并动态调整。关键区分：AIOLI 是 domain-level + loss-driven，我们是 instance-level + provenance-driven + 有 ESS 理论约束。

### 五、写论文时需注意

- Wang et al. 的 α 是已知参数，与我们的 proportion-free claim 有张力，建议在 Related Work 或 Discussion 中明确说明：τ 是 α 的 principled proxy（通过检测器 batch 统计量估计），而非假设已知比例
- Feng et al. (ICLR 2025) 从 "arXiv preprint" 升级为 ICLR 2025，在 Related Work 中应标注正确 venue
- AIOLI 作为 adaptive mixing 的 SOTA baseline，建议在实验中至少做定性对比讨论

---
