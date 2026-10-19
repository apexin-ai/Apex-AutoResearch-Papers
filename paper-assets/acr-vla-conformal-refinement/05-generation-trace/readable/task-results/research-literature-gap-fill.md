# research literature gap fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-gap-fill_20260515T134355_result.json`
- **Structured JSON:** [`733623c08d93d1f8da27.json`](../../sessions/73/733623c08d93d1f8da27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

YAML 有效，从 56 篇增至 69 篇（+13 篇新条目）。

完成。5 个文献缺口的覆盖情况：

| 缺口 | 新增论文 | 关键发现 |
|------|---------|---------|
| **Gap 1**: 监督式残差矫正 | CR-DAgger, RaC, Reactive Diffusion Policy, DAgger | CRM 的 supervised L2 correction 有 CR-DAgger/RaC 等先例 |
| **Gap 2**: 不确定性特征无效的先例 | Ovadia et al. 2019 | **直接先例在文献中缺失**，使我们的 negative result 成为真正新发现；Ovadia 提供 UQ-under-shift 退化的间接支撑 |
| **Gap 3**: Object vs Spatial 鲁棒性分类 | LIBERO-PRO, GenDP, S²-Diffusion | Spatial 需要 re-planning（不可通过 residual 矫正），Object 靠语义特征（observation features 可达） |
| **Gap 4**: 动作预测中的累积误差 | DAgger (Ross 2011), DART, Somalwar 2025 | O(T²) 理论解释 magnitude 阈值的 phase transition |
| **Gap 5**: CP 作为特征提取器 | Feature CP (ICLR 2023), Conformal Decision Theory, Selection by Prediction | **无先例将 CP scores 作为 NN 输入特征**，ACR-VLA 是 novel use case |

产出文件：
- `artifacts/literature_gap_report.md` — 完整报告含每篇论文的摘要、关系、BibTeX key
- `literature_map.yaml` — 追加 13 条新条目（69 篇总计）

---
