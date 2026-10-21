# Paper Patch Status: Budget Curve + Head-Tail Data

**审计时间**: 2026-05-18  
**论文路径**: `/root/trace-verdict-study/docs/paper/` (服务器) / `docs/paper/` (本地)

---

## 一、Budget Curve（tail-256/512/1024/2048）

### 已写入 ✅

| 数据点 | 位置 | 状态 |
|--------|------|------|
| Qwen-7B: 78.9/93.6/96.5/97.3 | appendix.tex Table 6 (`tab:tail_cross_model`) | ✅ 完整 |
| DeepSeek-6.7B: 76.4/93.9/96.5/95.0↓ | appendix.tex Table 6 | ✅ 完整 |
| Qwen-1.5B: 72.6/95.6/96.6/97.9 | appendix.tex Table 6 | ✅ 完整 |
| Phase transition 256→512: +14.7~+23pp | experiments.tex L152 + appendix.tex L419-421 | ✅ |
| tail-512 convergence (93.6-95.6% band) | appendix.tex L422-423 | ✅ |
| tail-1024 convergence (96.5-96.6%) | appendix.tex L422-423 | ✅ |
| Non-monotonicity: DeepSeek only, -1.5pp at 1024→2048 | experiments.tex L147, appendix.tex L428-429 | ✅ 正确描述为 architecture-specific |
| Scale behavior inversion (signal-poor vs signal-rich) | appendix.tex L425-426 | ✅ |
| Budget curve figure (`budget_curve`) | appendix.tex Fig 5 (`fig:trace_length`) | ✅ (仅 Qwen-7B) |

### 缺失 ❌

| 数据点 | 状态 | 说明 |
|--------|------|------|
| **CodeLlama-13B tail-512 = 97.5%** | ❌ 未写入 | 数据已有，表格和正文均无 |
| **CodeLlama-13B tail-256** | ⏳ 实验运行中 | 等待结果 |
| **CodeLlama-13B tail-1024** | ⏳ 实验运行中 | 等待结果 |
| **CodeLlama-13B tail-2048** | ❓ 未确认 | 未见相关数据 |
| 4-model budget curve figure 更新 | ❌ | 当前 figure 仅含 Qwen-7B 单模型 |

### 正文描述需更新的地方

- `experiments.tex` L152: "all three models jump" → 需改为 4 模型（待 CL-13B 数据齐全）
- `appendix.tex` L382-383: "three models spanning two architecture families" → 需扩展为 four models, three families
- `appendix.tex` Table 6 caption: 需加入 CodeLlama-13B 行
- `appendix.tex` L419: "all three models" → "all four models"（待数据齐全）

---

## 二、Head-Tail Gap（跨模型对比）

### 已写入 ✅

| 数据点 | 位置 | 状态 |
|--------|------|------|
| Qwen-7B: head-2048=81.8%, tail-2048=97.3%, gap=+15.5pp | appendix.tex Table 7 (`tab:head_vs_tail`) | ✅ |
| DeepSeek-6.7B: head-2048=78.7%, tail-2048=95.0%, gap=+16.3pp | appendix.tex Table 7 | ✅ |
| Qwen-1.5B: head-2048=75.3%, tail-2048=97.9%, gap=+22.6pp | appendix.tex Table 7 | ✅ |
| 15.5-22.6pp gap range | experiments.tex L150 | ✅ |
| 小模型 gap 更大 (Qwen-1.5B +22.6pp vs Qwen-7B +15.5pp) | experiments.tex L150-151 + appendix.tex L431-432 | ✅ |

### 缺失 ❌

| 数据点 | 状态 | 说明 |
|--------|------|------|
| **CodeLlama-13B head-2048 vs tail-2048** | ❌ | 无 head-2048 实验数据 |

---

## 三、Non-Monotonicity Correction

### 已写入 ✅

正文和附录均已正确表述：仅 DeepSeek 在 tail-1024→2048 下降 1.5pp，非 universal pattern。

- experiments.tex L147: "only DeepSeek showing a mild architecture-specific reversal"
- appendix.tex L357: "only DeepSeek-6.7B shows a mild −1.5pp decrease"
- appendix.tex L428-429: 明确说 "while the other two models increase monotonically"

**状态**: ✅ 无需修改

---

## 四、总结

### 已完成的 patch
1. ✅ 3-model budget curve 表格和分析（Qwen-7B, DeepSeek, Qwen-1.5B）
2. ✅ Phase transition / convergence / scale inversion 叙事
3. ✅ 3-model head-tail gap 表格和分析
4. ✅ Non-monotonicity 正确描述
5. ✅ Budget curve figure (单模型版)

### 待完成的 patch（按优先级）
1. **P1**: CodeLlama-13B tail-512=97.5% 写入 Table 6（数据已有，立即可做）
2. **P2**: 等待 CL-13B tail-256 和 tail-1024 实验完成后补全表格
3. **P3**: 更新正文 "three models" → "four models"（待 P2 完成）
4. **P4**: 更新 budget curve figure 为 4-model 版本
5. **P5**: CodeLlama-13B head-tail gap 数据（需要 head-2048 实验）

### 需要更新的章节列表
| 文件 | 章节/位置 | 更新内容 |
|------|-----------|----------|
| `experiments.tex` | §4.5 Additional Analyses, L149-156 | 加入 CL-13B 数据，更新 "three models" |
| `appendix.tex` | §Trace Length Full, Table 6 | 加 CL-13B 行 |
| `appendix.tex` | §Trace Length Full, Table 7 | 加 CL-13B 行（待 head-2048 数据）|
| `appendix.tex` | L382-383, L419 | "three models" → "four models" |
| `appendix.tex` | budget_curve figure | 更新为多模型版本 |
