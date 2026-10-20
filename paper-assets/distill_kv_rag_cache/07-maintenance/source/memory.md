# CompressLink Memory

## 项目终止 (2026-05-14)

**决策 D004**: MVP Kill — 核心假设被否决。

### Kill 原因
- Kill Criterion #1 完全触发：D(RABA+CEGR) ≤ A(standard) 在 6x 和 8x 均成立
- 8x offline PCA: D F1=0.0, A F1=0.114 — 联合优化反而有害
- CEGR epsilon fix 后 C_8x F1=0.0（修复前 A=C=0.2）— compression error 信号与 QA 需求反相关
- 高压缩误差 token = PCA 异常 token ≠ QA 关键 token

### 关键教训
1. **Per-sample PCA + boundary restoration + greedy argmax 三重保护掩盖 config 差异** — 6x 压缩下所有 config 输出完全相同，浪费三次全量运行
2. **Offline PCA calibration 解决了差异掩盖问题** — shared basis 引入足够损失暴露 config 差异
3. **CEGR per-token compression error 是常量 bug** — quantization step Δ_j²/12 对所有 token 相同
4. **修复后 compression error 引导到错误 token** — 高误差 token 是 PCA 异常值，不是 QA 需要的信息 token
5. **RABA 在高压缩比时有害** — restoration-aware weighting 在 8x 导致 bit 分配偏移过大
6. **NQ 数据集 context 太短** — 96% 样本 < 512 tokens，chunk boundary 不存在，切到 HotpotQA 解决
7. **AutoDL network_turbo 代理拖慢 ModelScope 国内 CDN** — 不要对 ModelScope 用代理

### 保留的 Artifacts
- 代码: /root/autodl-tmp/compresslink/ (autodl-rtx6000)
- Offline PCA basis: calibration/hotpotqa_50/calibration.pt
- HotpotQA 500 samples: data/hotpotqa_500.jsonl
- 压缩敏感性分析、PCA cosine diagnostic 等脚本在 scripts/ 下
