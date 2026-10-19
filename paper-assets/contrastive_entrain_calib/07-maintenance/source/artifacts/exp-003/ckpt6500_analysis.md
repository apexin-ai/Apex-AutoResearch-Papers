## exp-003-eval-ckpt6500 分析结果

### 指标
- SYCONScore: **0.1529**
- ToF: 0.0829
- NoF: 0.9834
- completed_pairs: 362/362（完整）

### 与 trajectory 对比

| Checkpoint | SYCONScore | ToF    | NoF    | 备注 |
|-----------|-----------|--------|--------|------|
| ckpt-1000 | 0.057     | —      | —      | 早期 |
| ckpt-2000 | 0.085     | —      | —      | |
| ckpt-3000 | 0.095     | —      | —      | |
| ckpt-4000 | 0.120     | —      | —      | |
| ckpt-4500 | 0.1337    | —      | —      | 前 peak，≈ vanilla |
| ckpt-5000 | 0.1144    | 0.0608 | 0.9669 | regression 开始 |
| ckpt-5500 | 0.1144    | 0.0608 | 0.9724 | 平坦 |
| ckpt-6000 | 0.0846    | 0.0442 | 0.9724 | 深度 regression |
| **ckpt-6500** | **0.1529** | **0.0829** | **0.9834** | **新 peak，超越 vanilla** |
| vanilla   | 0.134     | —      | —      | baseline |

### 建议 conclusion

**Success — ckpt-6500 以 SYCONScore 0.1529 超越 vanilla baseline (0.134)，相对提升 +14.1%。**

这是 exp-003 全 trajectory 的新 peak，也是首次实质性突破 vanilla ceiling。

### 对 narrative 的影响

1. **"vanilla ceiling" narrative 被打破**：ckpt-4500 的 0.1337 曾被解读为 R3-only 只能逼近但无法超越 vanilla baseline。ckpt-6500 的 0.1529 证明 R3-only GRPO 训练在足够步数后可以突破这个天花板。

2. **spike-regression narrative 需要修正**：ckpt-5000→6000 的持续下滑（0.114→0.114→0.085）确实存在，但 ckpt-6500 的 +80% 反弹（0.085→0.153）说明这不是单调 regression，而是 **非单调的训练动态**。曲线呈现 "rise → dip → recovery" 的 W-shape。

3. **需要注意的问题**：
   - ckpt-6000→6500 仅 500 步就从 0.085 跳到 0.153，波动幅度大，训练稳定性存疑
   - 建议补充 ckpt-7000/7500 eval 确认趋势是持续上升还是再次回落
   - 高 NoF (0.9834) 说明模型在 invalid pairs 上的拒绝能力很强，ToF 的提升（0.044→0.083）是 SYCONScore 跳升的主要驱动
