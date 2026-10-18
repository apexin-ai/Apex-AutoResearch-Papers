# paper v2 narrative rewrite

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_v2-narrative-rewrite_20260516T053203_result.json`
- **Structured JSON:** [`59a4c1c7d1bab62d9a4e.json`](../../sessions/59/59a4c1c7d1bab62d9a4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，无 error，输出 18 页 PDF。

验证总结：

| 检查项 | 状态 |
|--------|------|
| "7.9" 残留 | 仅 Appendix G 中故意保留的 n=5 对比，正文已全部更新 |
| "does not reach significance" | 已删除，全文无残留 |
| "ruling out prompt-specific confounding" | 存在于 results.tex §4.3 和 main.tex Appendix G |
| Appendix G 包含 n=5 + n=25 | 确认，n=25 为主结果，n=5 标注为 underpowered |
| pdflatex 编译 | 无 error |

共修改 5 处：
1. **results.tex:135-136** — §4.3 Prompt sensitivity 段落完全重写
2. **results.tex:69** — §4.1 括号内 "attenuated to 7.9pp" → "persisting at Δ=−25.5pp, r=−0.919"
3. **main.tex:219-220** — Appendix G RE 段落，新增 n=25 主结果 + 保留 n=5 作为 cautionary note
4. **main.tex:225-226** — Appendix G Interpretation 段落，更新为反映 n=25 definitive result
5. **discussion.tex:5** — Discussion 中 "7.9pp" → "25.5pp" 并补充统计量

---
