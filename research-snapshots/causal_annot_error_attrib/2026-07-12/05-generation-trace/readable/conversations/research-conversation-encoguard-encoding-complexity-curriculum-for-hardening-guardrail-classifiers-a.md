# Research conversation: EncoGuard: Encoding-Complexity Curriculum for Hardening Guardrail Classifiers Against Character-Level Evasion **状态**: PE

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/26f38bba-2519-4824-b5c2-e0bb6981faaf.jsonl`
- **Structured JSON:** [`370d02b774932b41392f.json`](../../sessions/37/370d02b774932b41392f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T12:14:39.519Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:14:39.519Z",
  "sessionId": "26f38bba-2519-4824-b5c2-e0bb6981faaf",
  "content": "# EncoGuard: Encoding-Complexity Curriculum for Hardening Guardrail Classifiers Against Character-Level Evasion\n\n**状态**: PENDING_REVIEW\n**级别**: top-tier\n**创建时间**: 2026-05-16T09:42:11.878561+00:00\n**来源**: s4\n\n## 描述\nWe address the critical vulnerability of open-source safety guardrails to encoding-based evasion attacks, where character injection techniques achieve up to 100% bypass rates and simple mutations evade 15 state-of-the-art guardrails 44.5% of the time (Bassani & Sanchez, EMNLP 2025). The combinatorial explosion of encoding compositions — 20 transformations yielding thousands of unique attack strings at 83–91% ASR on HarmBench (Huang, NeurIPS 2024 Workshop) — makes exhaustive rule-based canonicalization fundamentally untenable. While curriculum-based adversarial co-training for safety has been established by ACE-Safety (arXiv 2511.19218) — achieving 8.8% ASR via model-evolution-based curriculum tiers (AC-TGPO) for semantic jailbreaks — its curriculum principle (attacker-defender strength asymmetry) is unsuited for encoding attacks, where difficulty is determined by encoding structural properties (nesting depth, CPT-ratio preservation, cross-script mixing) rather than model-evolution differentials. Flat character augmentation exists (AprielGuard trains with character noise and leetspeak) but lacks systematic encoding coverage and curriculum structure. We propose EncoGuard, whose primary contribution is demonstrating that an encoding-complexity-based curriculum — structurally distinct from ACE-Safety's model-evolution curriculum and AprielGuard's flat augmentation — is the critical design factor for encoding robustness. Using a 2-stage curriculum progressively escalating from single-encoding attacks (Stage 1: character substitution + full encoding transformations) to composite multi-encoding attacks with CPT-adversarial augmentation (Stage 2: nested encodings, partial encoding, mixed-script interleaving, staged delivery), we implement a co-evolutionary loop where a GRPO-trained attacker (Qwen3.5-2B) learns encoding evasions against a guardrail classifier (Qwen3.5-4B), using TRL v1.0's GRPOTrainer with a custom outer orchestration script for alternating attacker/defender training phases. A deterministic rule-based decoding pipeline serves as oracle fallback, validating GPT-4o's harmful/benign judgments on complex nested encodings to prevent reward signal corruption. A secondary contribution demonstrates generalization to untrained character-level encoding types: we hold out Braille Unicode substitution (mapping characters to U+2800–U+28FF Braille Patterns) and Morse code substitution from all training, testing whether encoding-complexity curriculum teaches encoding-invariant features. These held-out types test complementary aspects of generalization: Braille Unicode is known in red-teaming tooling (e.g., NVIDIA garak) but has received no systematic academic evaluation — no paper measures its attack effectiveness or proposes specific defenses. Morse code is well-established as an attack vector — CipherChat (Yuan et al., ICLR 2024) demonstrated 55.3% unsafety rate on GPT-4, and Plentiful Jailbreaks (Huang, NeurIPS 2024 Workshop) includes it among 20 composable transformations — but has never been included in guardrail training data. Both are valid held-out types: Braille tests generalization to an academically uncharacterized encoding, while Morse tests generalization to a known-but-untrained-against attack. No existing guardrail training includes Braille or Morse augmentation, and no encoding-specific defense paper evaluates against them. Beyond encoding attacks, our results are designed to test a broader hypothesis: that complexity-structured curriculum is a general principle for adversarial robustness whenever attack difficulty has a natural ordering independent of model capability — potentially applicable to multi-turn staged delivery (STACK-style), tool-call obfuscation sequences, and cross-modal attack chains, as independently suggested by DMAST's concurrent multi-stage GRPO co-training for cross-modal attacks (arXiv 2603.04364). This positions EncoGuard not merely as an encoding-specific defense but as a demonstration of a transferable curriculum methodology with encoding as the showcase domain. We evaluate on HarmBench, JailbreakBench, WildGuardTest, and EncoAttack (12,000 test cases + 1,000 generalization cases), with primary baselines: Ilin et al. (no encoding curriculum), AprielGuard-style flat augmentation (no curriculum structure), and random-order adversarial training (ablation control), plus reference comparisons to Broken-Token CPT-Filtering and TRYLOCK canonicalization from published numbers. We target ≥50% encoding ASR reduction vs. Ilin et al., with curriculum ordering outperforming flat augmentation by ≥10% and random-order training by ≥15% on composite attacks, and ≥25% reduction on held-out character-level encoding types demonstrating generalization to untrained encodings, while maintaining <3% FPR. To mitigate timeline risk, we specify a minimal viable paper (MVP) scope achievable in 7 days: 2 trained baselines (dropping flat augmentation), 6,000 EncoAttack test cases, and Braille-only generalization — retaining the core curriculum-vs-random finding with full scope completable at camera-ready. Timeline: 9 days with pre-built encoding generators and EncoAttack suite (deterministic scripts prepared before research clock), reduced trained baseline set (3 primary), and paper writing overlapping final evaluation. All code, training pipeline, encoding generators, EncoAttack suite, and model weights will be released.\n\n## 核心问题\nOpen-source safety guardrails are catastrophically vulnerable to encoding-based evasion attacks — character injection techniques achieve up to 100% bypass (emoji smuggling), Unicode tag attacks reach 90.15% ASR, number-mapping 81.18%, and bidirectional text 78.69% against six production guardrails including Azure Prompt Shield and Meta Prompt Guard (Hackett et al., LLMSEC 2025). Simple input mutations bypass 15 state-of-the-art guardrail models 44.5% of the time with a single adversarial token (Bassani & Sanchez, EMNLP 2025 Findings). The combinatorial explosion of encoding compositions — 20 individual transformations yielding thousands of unique attack strings via best-of-n sampling, achieving 83–91% ASR on HarmBench across frontier models (Huang, NeurIPS 2024 Workshop) — makes exhaustive rule-based canonicalization fundamentally untenable. While curriculum-based adversarial co-training for safety has been established — ACE-Safety (arXiv 2511.19218) achieves 8.8% ASR via model-evolution-based curriculum tiers with AC-TGPO — its curriculum is structured around attacker-defender asymmetry (stronger current attacker vs. weaker historical defender), uses MCTS-discovered semantic jailbreak strategies, and does not address encoding/character-level attacks at all. Flat character-level augmentation exists (AprielGuard trains with character noise, leetspeak, and typographical errors) but lacks systematic encoding coverage and curriculum structure. Rule-based canonicalization (TRYLOCK Layer 0) handles known encodings via regex and Unicode normalization but cannot generalize to novel encodings or adversarial combinations — a fundamental limitation given the combinatorial attack surface. Static CPT-Filtering (Broken-Token) detects common encodings via Characters-Per-Token ratios but fails on non-Latin scripts and obfuscation preserving normal CPT ratios. The gap — an encoding-complexity-based curriculum that systematically hardens guardrail classifiers across the full spectrum of character-level encoding manipulations, including novel and composite attacks — remains unaddressed. Can curriculum ordering based on encoding complexity (rather than model evolution or random augmentation) close the encoding evasion gap by ≥50% and enable generalization to unseen character-level encoding types?\n\n## 机遇 / Why Now\nACE-Safety (arXiv 2511.19218, Nov 2025) established that curriculum-based adversarial co-training via GRPO produces robust safety alignment — its AC-TGPO with Normal→Asymmetric→Hard tiers achieves 8.8% ASR versus 19.0% for the nearest competitor, converging by iteration 4. However, ACE-Safety's curriculum is fundamentally model-evolution-based (difficulty arises from attacking weaker historical defenders), uses GS-MCTS to discover semantic jailbreak strategies, and targets base LLM alignment — it neither addresses encoding/character-level attacks nor hardens external guardrail classifiers. Ilin et al. (arXiv 2507.08284, Jul 2025) demonstrated RL-guided adversarial training with a GAN-inspired loop using a 7B attacker (dolphin-2.1-mistral-7B) to train a lightweight 300M classifier (Lite-Oute-1-300M-Instruct) — but generates semantic jailbreaks without encoding-specific strategies. AprielGuard (arXiv 2512.20293, Dec 2025) trains with character-level noise, leetspeak substitutions, and typographical errors as flat data augmentation — the closest existing 'encoding augmentation for guardrail training' — but without systematic encoding coverage, curriculum structure, or evaluation on encoding-specific benchmarks. TRYLOCK (arXiv 2601.03300, Thornton, Jan 2026) introduced Layer 0 Input Canonicalization achieving 87.5% reduction in Unicode/homoglyph failures (from 8 to 1 out of 24 total system failures), but its rule-based approach fundamentally cannot generalize to novel encodings not in its rule set or adversarial combinations designed to evade detection — a critical limitation given that 20 composable transformations already generate a combinatorially intractable attack surface (Huang, NeurIPS 2024 Workshop). Broken-Token (arXiv 2510.26847, Oct 2025) achieves near-perfect CPT-Filtering accuracy on five tested encoding schemes including via sliding window detection, but fails on non-Latin scripts and is untested against obfuscation preserving normal CPT ratios. The specific opportunity is twofold: (1) demonstrating that an encoding-complexity-based curriculum — structurally distinct from ACE-Safety's model-evolution curriculum and AprielGuard's flat augmentation — is the critical design factor for encoding robustness, and that this curriculum enables generalization to character-level encoding types absent from training that neither rule-based canonicalization nor model-evolution-based curricula can achieve; and (2) establishing complexity-structured curriculum as a general principle for adversarial robustness whenever attack difficulty has a natural ordering independent of model capability — with encoding attacks as the showcase application and implications for multi-turn staged delivery (STACK-style), tool-call obfuscation sequences, and cross-modal attack chains, as independently suggested by DMAST's concurrent multi-stage GRPO co-training for cross-modal web agent attacks (arXiv 2603.04364, Mar 2026).\n\n## 方法思路\nWe propose EncoGuard, which demonstrates that encoding-complexity-based curriculum design — structurally distinct from ACE-Safety's model-evolution curriculum (Normal→Asymmetric→Hard tiers based on attacker-defender strength asymmetry) and AprielGuard's flat character augmentation — is the critical design factor for hardening guardrail classifiers against encoding evasion. While ACE-Safety established that curriculum adversarial co-training via GRPO produces robust safety alignment for semantic jailbreaks, encoding attacks require a fundamentally different curriculum principle: progressive escalation of encoding complexity rather than progressive escalation of model-evolution asymmetry, because encoding difficulty is determined by the structural properties of the transformation (nesting depth, CPT-ratio preservation, cross-script mixing) rather than by attacker-defender strength differentials.\n\n**Architecture**: A GRPO-trained adversarial attacker (Qwen3.5-2B) co-evolves against a guardrail classifier (Qwen3.5-4B, SFT-initialized) over 2 co-evolutionary rounds. The attacker receives reward proportional to the classifier's confidence that an encoding-obfuscated harmful prompt is safe, while a frozen oracle (GPT-4o) confirms the decoded content is genuinely harmful — preventing reward hacking via benign encoded content. **Oracle fallback**: A deterministic rule-based decoding pipeline (implementing all training-stage encoding transforms in reverse: base64 decode, hex decode, ROT-n reverse, URL decode, Unicode unescape, homoglyph normalization via TR39 mapping) serves as secondary verification — if the oracle's harmful/benign judgment disagrees with the deterministic decoder's output fed to a reference classifier, the sample is flagged for exclusion from reward computation, preventing reward signal corruption on complex nested encodings where GPT-4o may fail to decode correctly. Note: TRL v1.0's GRPOTrainer handles single-policy optimization, so the co-evolutionary loop requires a lightweight custom outer orchestration script alternating attacker GRPO and classifier SFT phases — standard engineering for adversarial co-training (as in Ilin et al. and DuoGuard) but a factor in timeline planning.\n\n**Primary contribution — Encoding-Complexity Curriculum**: Unlike ACE-Safety's model-evolution tiers (where difficulty emerges from training stronger attackers against weaker historical defenders), EncoGuard structures the attacker's encoding strategy space via a 2-stage curriculum of increasing encoding complexity — a curriculum principle grounded in the structural properties of encoding transformations themselves:\n- Stage 1 (Round 1 — Single-Encoding Attacks): Character-level substitution (leetspeak variants, homoglyph substitution via Cyrillic/Greek lookalikes, fullwidth characters, mathematical Unicode symbols) AND single-layer full encoding transformations (base64, hexadecimal, ROT-n ciphers, URL encoding, Unicode escape sequences). The attacker learns to generate obfuscations that preserve LLM readability while evading both character-level pattern matching and simple encoding detection.\n- Stage 2 (Round 2 — Composite Attacks with CPT-Adversarial Augmentation): Nested encodings (base64-of-hexadecimal, ROT13-of-base64), partial encoding (encoding only key harmful terms within natural text), mixed-script interleaving, zero-width character insertion between encoded segments, and STACK-style multi-turn staged delivery. This stage directly addresses the combinatorial composition threat demonstrated by Plentiful Jailbreaks (Huang, NeurIPS 2024 Workshop), where arbitrary sequencing of transformations generates an intractable attack surface that rule-based defenses cannot enumerate. Critically, the attacker receives bonus reward for encodings that maintain CPT ratios within 1 standard deviation of natural text (as measured by the target tokenizer), directly training against Broken-Token's CPT-Filtering detection mechanism — including its sliding window variant.\n\nThe Stage 2 attacker is initialized from the Stage 1 checkpoint, enabling progressive skill building — analogous to ACE-Safety's curriculum progression but with complexity tiers defined by encoding structure rather than model evolution. The classifier is retrained on the full accumulated adversarial dataset after each round, with curriculum-aware data balancing (equal representation of each complexity tier). Encoding attack generators are implemented as deterministic rule-based transforms (not learned via MCTS as in ACE-Safety), ensuring controlled complexity escalation and reproducibility.\n\n**Secondary contribution — Generalization to Untrained Character-Level Encodings**: We deliberately hold out two character-level encoding types from all training stages — Braille Unicode substitution (mapping ASCII characters to Unicode Braille Patterns U+2800–U+28FF, e.g., 'hello' → '⠓⠑⠇⠇⠕') and Morse code substitution (e.g., 'hello' → '.... . .-.. .-.. ---') — to test whether the encoding-complexity curriculum teaches encoding-invariant harmful content detection. These held-out types test different aspects of generalization: Braille Unicode is known in red-teaming tooling (e.g., NVIDIA garak's InjectBraille probe) but has received no systematic academic evaluation — no paper measures its attack effectiveness or proposes specific defenses, making it a test of generalization to an academically uncharacterized encoding. Morse code, by contrast, is well-established as an attack vector — CipherChat (Yuan et al., ICLR 2024) demonstrated 55.3% unsafety rate on GPT-4, and Plentiful Jailbreaks (Huang, NeurIPS 2024 Workshop) includes it among 20 composable transformations — but has never been included in guardrail training data, making it a test of generalization to a known-but-untrained-against attack. Both are genuine character-level encodings: Braille uses a deterministic 1-to-1 Unicode character mapping (structurally similar to trained encodings like fullwidth or mathematical Unicode), while Morse uses a character-to-symbol-sequence mapping (structurally similar to trained encodings like base64 or hexadecimal). No existing guardrail training includes Braille or Morse augmentation, and no encoding-specific defense paper evaluates against them — making them valid generalization tests for curriculum-trained encoding-invariant features. Our hypothesis: the progressive curriculum forces the classifier to develop features that recognize harmful semantic content regardless of surface-level character transformations, enabling generalization across character-level encoding families that neither rule-based defenses (TRYLOCK, which lacks Braille/Morse in its rule set), flat augmentation (AprielGuard), nor model-evolution curricula (ACE-Safety, which shows no encoding-specific generalization) can achieve. This tests generalization within the character-level encoding mechanism class — not across fundamentally different evasion mechanisms (e.g., semantic reformulation).\n\n**Stability mechanisms**: (a) Per-stage diversity enforcement via entropy regularization on the encoding-type distribution within each round (preventing collapse to a single encoding strategy, informed by TriPlay-RL's diversity penalties); (b) Defender checkpoint selection retaining the model with lowest FPR on a held-out benign set, with rollback if FPR exceeds 3%; (c) Semantic deduplication (embedding cosine similarity >0.9 threshold) to remove near-duplicate adversarial examples.\n\n**Evaluation**: Four benchmarks — HarmBench, JailbreakBench, WildGuardTest, and a novel EncoAttack suite (curated from encoding attack literature: 500 prompts × 8 encoding types × 3 nesting levels = 12,000 test cases, plus 500 × 2 held-out character-level encoding types = 1,000 generalization test cases). Primary baselines: (1) Ilin et al.'s approach (without encoding curriculum) trained to equivalent compute; (2) AprielGuard-style flat encoding augmentation — character noise + leetspeak + typographical errors applied without curriculum structure or systematic encoding coverage, directly testing whether curriculum ordering outperforms unstructured augmentation (H2); (3) Random-order adversarial training with the same encoding attack data but NO curriculum structure (ablation control). Reference comparisons (pre-computed from published numbers, not re-implemented): Broken-Token CPT-Filtering (both global and sliding window variants), TRYLOCK Layer 0 canonicalization + classifier pipeline. Secondary baselines: GuardReasoner, WildGuard, AprielGuard, Qwen3Guard. Key hypotheses: (H1) EncoGuard reduces encoding attack ASR by ≥50% relative to Ilin et al. baseline; (H2) Curriculum-ordered training outperforms both random-order training (≥15% on composite encoding attacks) AND AprielGuard-style flat augmentation (≥10% overall), demonstrating that curriculum ordering is the critical factor; (H3) EncoGuard catches ≥30% of attacks that evade CPT-Filtering (those with manipulated CPT ratios); (H4) EncoGuard achieves ≥25% ASR reduction on held-out character-level encoding types (Braille Unicode, Morse code) relative to Ilin et al. baseline, demonstrating generalization to untrained encodings — a capability that neither rule-based canonicalization (which lacks these encodings in its rule set) nor flat augmentation (which has no curriculum to build encoding-invariant features) can achieve. All code, training data, curriculum configurations, and model weights will be released.\n\n**Timeline contingency — Minimal Viable Paper (MVP)**: If engineering issues arise (co-evolutionary loop bugs, GPT-4o oracle degradation on nested encodings, GRPO training instability), a reduced-scope paper achievable in 7 days retains scientific validity: (a) drop AprielGuard-style flat augmentation baseline (retain Ilin et al. reimplementation + random-order ablation as the minimum set testing H1 and the curriculum-vs-random comparison from H2); (b) reduce EncoAttack to 6,000 test cases (4 encoding types × 3 nesting levels × 500 prompts); (c) report H4 generalization on Braille Unicode only (skip Morse if time-constrained), since Braille's 1-to-1 character mapping provides the cleaner structural analogy to trained encodings. This MVP still demonstrates the core claim (encoding-complexity curriculum > no curriculum) and generalization to one held-out type, with the full scope completable as a camera-ready extension.\n\n## Seed Topic\nTarget: EMNLP 2026, ARR submission deadline 2026-05-25 (11 days from today 2026-05-14). Track: LLM Security.\n\nDirection: LLM safety robustness — defense methods against jailbreaking, adversarial promp...\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T12:14:39.528Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:14:39.528Z",
  "sessionId": "26f38bba-2519-4824-b5c2-e0bb6981faaf"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T12:14:39.727Z_

# EncoGuard: Encoding-Complexity Curriculum for Hardening Guardrail Classifiers Against Character-Level Evasion

**状态**: PENDING_REVIEW
**级别**: top-tier
**创建时间**: 2026-05-16T09:42:11.878561+00:00
**来源**: s4

## 描述
We address the critical vulnerability of open-source safety guardrails to encoding-based evasion attacks, where character injection techniques achieve up to 100% bypass rates and simple mutations evade 15 state-of-the-art guardrails 44.5% of the time (Bassani & Sanchez, EMNLP 2025). The combinatorial explosion of encoding compositions — 20 transformations yielding thousands of unique attack strings at 83–91% ASR on HarmBench (Huang, NeurIPS 2024 Workshop) — makes exhaustive rule-based canonicalization fundamentally untenable. While curriculum-based adversarial co-training for safety has been established by ACE-Safety (arXiv 2511.19218) — achieving 8.8% ASR via model-evolution-based curriculum tiers (AC-TGPO) for semantic jailbreaks — its curriculum principle (attacker-defender strength asymmetry) is unsuited for encoding attacks, where difficulty is determined by encoding structural properties (nesting depth, CPT-ratio preservation, cross-script mixing) rather than model-evolution differentials. Flat character augmentation exists (AprielGuard trains with character noise and leetspeak) but lacks systematic encoding coverage and curriculum structure. We propose EncoGuard, whose primary contribution is demonstrating that an encoding-complexity-based curriculum — structurally distinct from ACE-Safety's model-evolution curriculum and AprielGuard's flat augmentation — is the critical design factor for encoding robustness. Using a 2-stage curriculum progressively escalating from single-encoding attacks (Stage 1: character substitution + full encoding transformations) to composite multi-encoding attacks with CPT-adversarial augmentation (Stage 2: nested encodings, partial encoding, mixed-script interleaving, staged delivery), we implement a co-evolutionary loop where a GRPO-trained attacker (Qwen3.5-2B) learns encoding evasions against a guardrail classifier (Qwen3.5-4B), using TRL v1.0's GRPOTrainer with a custom outer orchestration script for alternating attacker/defender training phases. A deterministic rule-based decoding pipeline serves as oracle fallback, validating GPT-4o's harmful/benign judgments on complex nested encodings to prevent reward signal corruption. A secondary contribution demonstrates generalization to untrained character-level encoding types: we hold out Braille Unicode substitution (mapping characters to U+2800–U+28FF Braille Patterns) and Morse code substitution from all training, testing whether encoding-complexity curriculum teaches encoding-invariant features. These held-out types test complementary aspects of generalization: Braille Unicode is known in red-teaming tooling (e.g., NVIDIA garak) but has received no systematic academic evaluation — no paper measures its attack effectiveness or proposes specific defenses. Morse code is well-established as an attack vector — CipherChat (Yuan et al., ICLR 2024) demonstrated 55.3% unsafety rate on GPT-4, and Plentiful Jailbreaks (Huang, NeurIPS 2024 Workshop) includes it among 20 composable transformations — but has never been included in guardrail training data. Both are valid held-out types: Braille tests generalization to an academically uncharacterized encoding, while Morse tests generalization to a known-but-untrained-against attack. No existing guardrail training includes Braille or Morse augmentation, and no encoding-specific defense paper evaluates against them. Beyond encoding attacks, our results are designed to test a broader hypothesis: that complexity-structured curriculum is a general principle for adversarial robustness whenever attack difficulty has a natural ordering independent of model capability — potentially applicable to multi-turn staged delivery (STACK-style), tool-call obfuscation sequences, and cross-modal attack chains, as independently suggested by DMAST's concurrent multi-stage GRPO co-training for cross-modal attacks (arXiv 2603.04364). This positions EncoGuard not merely as an encoding-specific defense but as a demonstration of a transferable curriculum methodology with encoding as the showcase domain. We evaluate on HarmBench, JailbreakBench, WildGuardTest, and EncoAttack (12,000 test cases + 1,000 generalization cases), with primary baselines: Ilin et al. (no encoding curriculum), AprielGuard-style flat augmentation (no curriculum structure), and random-order adversarial training (ablation control), plus reference comparisons to Broken-Token CPT-Filtering and TRYLOCK canonicalization from published numbers. We target ≥50% encoding ASR reduction vs. Ilin et al., with curriculum ordering outperforming flat augmentation by ≥10% and random-order training by ≥15% on composite attacks, and ≥25% reduction on held-out character-level encoding types demonstrating generalization to untrained encodings, while maintaining <3% FPR. To mitigate timeline risk, we specify a minimal viable paper (MVP) scope achievable in 7 days: 2 trained baselines (dropping flat augmentation), 6,000 EncoAttack test cases, and Braille-only generalization — retaining the core curriculum-vs-random finding with full scope completable at camera-ready. Timeline: 9 days with pre-built encoding generators and EncoAttack suite (deterministic scripts prepared before research clock), reduced trained baseline set (3 primary), and paper writing overlapping final evaluation. All code, training pipeline, encoding generators, EncoAttack suite, and model weights will be released.

## 核心问题
Open-source safety guardrails are catastrophically vulnerable to encoding-based evasion attacks — character injection techniques achieve up to 100% bypass (emoji smuggling), Unicode tag attacks reach 90.15% ASR, number-mapping 81.18%, and bidirectional text 78.69% against six production guardrails including Azure Prompt Shield and Meta Prompt Guard (Hackett et al., LLMSEC 2025). Simple input mutations bypass 15 state-of-the-art guardrail models 44.5% of the time with a single adversarial token (Bassani & Sanchez, EMNLP 2025 Findings). The combinatorial explosion of encoding compositions — 20 individual transformations yielding thousands of unique attack strings via best-of-n sampling, achieving 83–91% ASR on HarmBench across frontier models (Huang, NeurIPS 2024 Workshop) — makes exhaustive rule-based canonicalization fundamentally untenable. While curriculum-based adversarial co-training for safety has been established — ACE-Safety (arXiv 2511.19218) achieves 8.8% ASR via model-evolution-based curriculum tiers with AC-TGPO — its curriculum is structured around attacker-defender asymmetry (stronger current attacker vs. weaker historical defender), uses MCTS-discovered semantic jailbreak strategies, and does not address encoding/character-level attacks at all. Flat character-level augmentation exists (AprielGuard trains with character noise, leetspeak, and typographical errors) but lacks systematic encoding coverage and curriculum structure. Rule-based canonicalization (TRYLOCK Layer 0) handles known encodings via regex and Unicode normalization but cannot generalize to novel encodings or adversarial combinations — a fundamental limitation given the combinatorial attack surface. Static CPT-Filtering (Broken-Token) detects common encodings via Characters-Per-Token ratios but fails on non-Latin scripts and obfuscation preserving normal CPT ratios. The gap — an encoding-complexity-based curriculum that systematically hardens guardrail classifiers across the full spectrum of character-level encoding manipulations, including novel and composite attacks — remains unaddressed. Can curriculum ordering based on encoding complexity (rather than model evolution or random augmentation) close the encoding evasion gap by ≥50% and enable generalization to unseen character-level encoding types?

## 机遇 / Why Now
ACE-Safety (arXiv 2511.19218, Nov 2025) established that curriculum-based adversarial co-training via GRPO produces robust safety alignment — its AC-TGPO with Normal→Asymmetric→Hard tiers achieves 8.8% ASR versus 19.0% for the nearest competitor, converging by iteration 4. However, ACE-Safety's curriculum is fundamentally model-evolution-based (difficulty arises from attacking weaker historical defenders), uses GS-MCTS to discover semantic jailbreak strategies, and targets base LLM alignment — it neither addresses encoding/character-level attacks nor hardens external guardrail classifiers. Ilin et al. (arXiv 2507.08284, Jul 2025) demonstrated RL-guided adversarial training with a GAN-inspired loop using a 7B attacker (dolphin-2.1-mistral-7B) to train a lightweight 300M classifier (Lite-Oute-1-300M-Instruct) — but generates semantic jailbreaks without encoding-specific strategies. AprielGuard (arXiv 2512.20293, Dec 2025) trains with character-level noise, leetspeak substitutions, and typographical errors as flat data augmentation — the closest existing 'encoding augmentation for guardrail training' — but without systematic encoding coverage, curriculum structure, or evaluation on encoding-specific benchmarks. TRYLOCK (arXiv 2601.03300, Thornton, Jan 2026) introduced Layer 0 Input Canonicalization achieving 87.5% reduction in Unicode/homoglyph failures (from 8 to 1 out of 24 total system failures), but its rule-based approach fundamentally cannot generalize to novel encodings not in its rule set or adversarial combinations designed to evade detection — a critical limitation given that 20 composable transformations already generate a combinatorially intractable attack surface (Huang, NeurIPS 2024 Workshop). Broken-Token (arXiv 2510.26847, Oct 2025) achieves near-perfect CPT-Filtering accuracy on five tested encoding schemes including via sliding window detection, but fails on non-Latin scripts and is untested against obfuscation preserving normal CPT ratios. The specific opportunity is twofold: (1) demonstrating that an encoding-complexity-based curriculum — structurally distinct from ACE-Safety's model-evolution curriculum and AprielGuard's flat augmentation — is the critical design factor for encoding robustness, and that this curriculum enables generalization to character-level encoding types absent from training that neither rule-based canonicalization nor model-evolution-based curricula can achieve; and (2) establishing complexity-structured curriculum as a general principle for adversarial robustness whenever attack difficulty has a natural ordering independent of model capability — with encoding attacks as the showcase application and implications for multi-turn staged delivery (STACK-style), tool-call obfuscation sequences, and cross-modal attack chains, as independently suggested by DMAST's concurrent multi-stage GRPO co-training for cross-modal web agent attacks (arXiv 2603.04364, Mar 2026).

## 方法思路
We propose EncoGuard, which demonstrates that encoding-complexity-based curriculum design — structurally distinct from ACE-Safety's model-evolution curriculum (Normal→Asymmetric→Hard tiers based on attacker-defender strength asymmetry) and AprielGuard's flat character augmentation — is the critical design factor for hardening guardrail classifiers against encoding evasion. While ACE-Safety established that curriculum adversarial co-training via GRPO produces robust safety alignment for semantic jailbreaks, encoding attacks require a fundamentally different curriculum principle: progressive escalation of encoding complexity rather than progressive escalation of model-evolution asymmetry, because encoding difficulty is determined by the structural properties of the transformation (nesting depth, CPT-ratio preservation, cross-script mixing) rather than by attacker-defender strength differentials.

**Architecture**: A GRPO-trained adversarial attacker (Qwen3.5-2B) co-evolves against a guardrail classifier (Qwen3.5-4B, SFT-initialized) over 2 co-evolutionary rounds. The attacker receives reward proportional to the classifier's confidence that an encoding-obfuscated harmful prompt is safe, while a frozen oracle (GPT-4o) confirms the decoded content is genuinely harmful — preventing reward hacking via benign encoded content. **Oracle fallback**: A deterministic rule-based decoding pipeline (implementing all training-stage encoding transforms in reverse: base64 decode, hex decode, ROT-n reverse, URL decode, Unicode unescape, homoglyph normalization via TR39 mapping) serves as secondary verification — if the oracle's harmful/benign judgment disagrees with the deterministic decoder's output fed to a reference classifier, the sample is flagged for exclusion from reward computation, preventing reward signal corruption on complex nested encodings where GPT-4o may fail to decode correctly. Note: TRL v1.0's GRPOTrainer handles single-policy optimization, so the co-evolutionary loop requires a lightweight custom outer orchestration script alternating attacker GRPO and classifier SFT phases — standard engineering for adversarial co-training (as in Ilin et al. and DuoGuard) but a factor in timeline planning.

**Primary contribution — Encoding-Complexity Curriculum**: Unlike ACE-Safety's model-evolution tiers (where difficulty emerges from training stronger attackers against weaker historical defenders), EncoGuard structures the attacker's encoding strategy space via a 2-stage curriculum of increasing encoding complexity — a curriculum principle grounded in the structural properties of encoding transformations themselves:
- Stage 1 (Round 1 — Single-Encoding Attacks): Character-level substitution (leetspeak variants, homoglyph substitution via Cyrillic/Greek lookalikes, fullwidth characters, mathematical Unicode symbols) AND single-layer full encoding transformations (base64, hexadecimal, ROT-n ciphers, URL encoding, Unicode escape sequences). The attacker learns to generate obfuscations that preserve LLM readability while evading both character-level pattern matching and simple encoding detection.
- Stage 2 (Round 2 — Composite Attacks with CPT-Adversarial Augmentation): Nested encodings (base64-of-hexadecimal, ROT13-of-base64), partial encoding (encoding only key harmful terms within natural text), mixed-script interleaving, zero-width character insertion between encoded segments, and STACK-style multi-turn staged delivery. This stage directly addresses the combinatorial composition threat demonstrated by Plentiful Jailbreaks (Huang, NeurIPS 2024 Workshop), where arbitrary sequencing of transformations generates an intractable attack surface that rule-based defenses cannot enumerate. Critically, the attacker receives bonus reward for encodings that maintain CPT ratios within 1 standard deviation of natural text (as measured by the target tokenizer), directly training against Broken-Token's CPT-Filtering detection mechanism — including its sliding window variant.

The Stage 2 attacker is initialized from the Stage 1 checkpoint, enabling progressive skill building — analogous to ACE-Safety's curriculum progression but with complexity tiers defined by encoding structure rather than model evolution. The classifier is retrained on the full accumulated adversarial dataset after each round, with curriculum-aware data balancing (equal representation of each complexity tier). Encoding attack generators are implemented as deterministic rule-based transforms (not learned via MCTS as in ACE-Safety), ensuring controlled complexity escalation and reproducibility.

**Secondary contribution — Generalization to Untrained Character-Level Encodings**: We deliberately hold out two character-level encoding types from all training stages — Braille Unicode substitution (mapping ASCII characters to Unicode Braille Patterns U+2800–U+28FF, e.g., 'hello' → '⠓⠑⠇⠇⠕') and Morse code substitution (e.g., 'hello' → '.... . .-.. .-.. ---') — to test whether the encoding-complexity curriculum teaches encoding-invariant harmful content detection. These held-out types test different aspects of generalization: Braille Unicode is known in red-teaming tooling (e.g., NVIDIA garak's InjectBraille probe) but has received no systematic academic evaluation — no paper measures its attack effectiveness or proposes specific defenses, making it a test of generalization to an academically uncharacterized encoding. Morse code, by contrast, is well-established as an attack vector — CipherChat (Yuan et al., ICLR 2024) demonstrated 55.3% unsafety rate on GPT-4, and Plentiful Jailbreaks (Huang, NeurIPS 2024 Workshop) includes it among 20 composable transformations — but has never been included in guardrail training data, making it a test of generalization to a known-but-untrained-against attack. Both are genuine character-level encodings: Braille uses a deterministic 1-to-1 Unicode character mapping (structurally similar to trained encodings like fullwidth or mathematical Unicode), while Morse uses a character-to-symbol-sequence mapping (structurally similar to trained encodings like base64 or hexadecimal). No existing guardrail training includes Braille or Morse augmentation, and no encoding-specific defense paper evaluates against them — making them valid generalization tests for curriculum-trained encoding-invariant features. Our hypothesis: the progressive curriculum forces the classifier to develop features that recognize harmful semantic content regardless of surface-level character transformations, enabling generalization across character-level encoding families that neither rule-based defenses (TRYLOCK, which lacks Braille/Morse in its rule set), flat augmentation (AprielGuard), nor model-evolution curricula (ACE-Safety, which shows no encoding-specific generalization) can achieve. This tests generalization within the character-level encoding mechanism class — not across fundamentally different evasion mechanisms (e.g., semantic reformulation).

**Stability mechanisms**: (a) Per-stage diversity enforcement via entropy regularization on the encoding-type distribution within each round (preventing collapse to a single encoding strategy, informed by TriPlay-RL's diversity penalties); (b) Defender checkpoint selection retaining the model with lowest FPR on a held-out benign set, with rollback if FPR exceeds 3%; (c) Semantic deduplication (embedding cosine similarity >0.9 threshold) to remove near-duplicate adversarial examples.

**Evaluation**: Four benchmarks — HarmBench, JailbreakBench, WildGuardTest, and a novel EncoAttack suite (curated from encoding attack literature: 500 prompts × 8 encoding types × 3 nesting levels = 12,000 test cases, plus 500 × 2 held-out character-level encoding types = 1,000 generalization test cases). Primary baselines: (1) Ilin et al.'s approach (without encoding curriculum) trained to equivalent compute; (2) AprielGuard-style flat encoding augmentation — character noise + leetspeak + typographical errors applied without curriculum structure or systematic encoding coverage, directly testing whether curriculum ordering outperforms unstructured augmentation (H2); (3) Random-order adversarial training with the same encoding attack data but NO curriculum structure (ablation control). Reference comparisons (pre-computed from published numbers, not re-implemented): Broken-Token CPT-Filtering (both global and sliding window variants), TRYLOCK Layer 0 canonicalization + classifier pipeline. Secondary baselines: GuardReasoner, WildGuard, AprielGuard, Qwen3Guard. Key hypotheses: (H1) EncoGuard reduces encoding attack ASR by ≥50% relative to Ilin et al. baseline; (H2) Curriculum-ordered training outperforms both random-order training (≥15% on composite encoding attacks) AND AprielGuard-style flat augmentation (≥10% overall), demonstrating that curriculum ordering is the critical factor; (H3) EncoGuard catches ≥30% of attacks that evade CPT-Filtering (those with manipulated CPT ratios); (H4) EncoGuard achieves ≥25% ASR reduction on held-out character-level encoding types (Braille Unicode, Morse code) relative to Ilin et al. baseline, demonstrating generalization to untrained encodings — a capability that neither rule-based canonicalization (which lacks these encodings in its rule set) nor flat augmentation (which has no curriculum to build encoding-invariant features) can achieve. All code, training data, curriculum configurations, and model weights will be released.

**Timeline contingency — Minimal Viable Paper (MVP)**: If engineering issues arise (co-evolutionary loop bugs, GPT-4o oracle degradation on nested encodings, GRPO training instability), a reduced-scope paper achievable in 7 days retains scientific validity: (a) drop AprielGuard-style flat augmentation baseline (retain Ilin et al. reimplementation + random-order ablation as the minimum set testing H1 and the curriculum-vs-random comparison from H2); (b) reduce EncoAttack to 6,000 test cases (4 encoding types × 3 nesting levels × 500 prompts); (c) report H4 generalization on Braille Unicode only (skip Morse if time-constrained), since Braille's 1-to-1 character mapping provides the cleaner structural analogy to trained encodings. This MVP still demonstrates the core claim (encoding-complexity curriculum > no curriculum) and generalization to one held-out type, with the full scope completable as a camera-ready extension.

## Seed Topic
Target: EMNLP 2026, ARR submission deadline 2026-05-25 (11 days from today 2026-05-14). Track: LLM Security.

Direction: LLM safety robustness — defense methods against jailbreaking, adversarial promp...


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e2030f07-dcd1-435e-bb56-661bb24aec3a",
  "type": "user",
  "uuid": "d869bed0-ad62-4498-b285-903f930cf668",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "26f38bba-2519-4824-b5c2-e0bb6981faaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T12:14:39.721Z_

```json
{
  "parentUuid": "d869bed0-ad62-4498-b285-903f930cf668",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "fe04603c-7cea-4df0-8ef1-c4a547d8ae81",
  "timestamp": "2026-05-16T12:14:39.721Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "26f38bba-2519-4824-b5c2-e0bb6981faaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T12:14:39.721Z_

```json
{
  "parentUuid": "fe04603c-7cea-4df0-8ef1-c4a547d8ae81",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5c050cad-654f-4a1a-a41e-c7deb374ded9",
  "timestamp": "2026-05-16T12:14:39.721Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "26f38bba-2519-4824-b5c2-e0bb6981faaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# EncoGuard: Encoding-Complexity Curriculum for Hardening Guardrail Classifiers Against Character-Level Evasion  **状态**: PENDING_REVIEW **级别**: top-tier **创建时间**: 2026-05-16T09:42:11.878561+00:00 **来源…",
  "leafUuid": "5c050cad-654f-4a1a-a41e-c7deb374ded9",
  "sessionId": "26f38bba-2519-4824-b5c2-e0bb6981faaf"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Encoding-complexity curriculum for guardrail robustness",
  "sessionId": "26f38bba-2519-4824-b5c2-e0bb6981faaf"
}
```

---

### Assistant

_source line 8 · 2026-05-16T12:15:56.521Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal as the 发掘 agent (Discovery Agent). I need to evaluate the idea's novelty, significance, and related work differentiation, and identify whether there are opportunities to sharpen the idea's ceiling.

Let me first understand the core claim:

**Core Claim**: Encoding-complexity-based curriculum (progressively harder encoding attacks) is the critical design factor for hardening guardrail classifiers against encoding evasion, as opposed to model-evolution-based curriculum (ACE-Safety) or flat augmentation (AprielGuard).

**Key contributions**:
1. A 2-stage encoding-complexity curriculum for adversarial co-training


2. Generalization to held-out encoding types (Braille, Morse)
3. A broader hypothesis about complexity-structured curriculum as a general principle

Now I'm examining whether there's a simpler explanation for the results. The main alternative would be just adding encoding examples without any curriculum structure, which the paper addresses through ablations and comparisons to flat augmentation. But there's also the question of whether input canonicalization—preprocessing to normalize encodings before classification—might achieve similar robustness more directly, which some existing work like TRYLOCK already explores.

A learned normalizer trained as a seq2seq model could potentially generalize to novel encodings without needing curriculum learning at all. And there's the straightforward possibility that simply training a larger classifier on more diverse encoding data would eliminate the need for curriculum structure entirely.

On the premises themselves, I'm questioning whether the claimed structural properties—nesting depth, CPT-ratio preservation, cross-script mixing—actually determine encoding difficulty, or if this is just an assumption. The paper asserts this but doesn't empirically validate which dimensions actually matter for model learning.

The mechanistic claim that progressive curriculum forces encoding-invariant features is also suspect. Standard curriculum learning literature shows benefits are often marginal and task-dependent, so why would this approach outperform simply seeing all diverse examples at once? And the generalization claim about Braille being structurally similar to fullwidth characters is plausible, but the expected ≥25% ASR reduction needs better justification for why curriculum specifically enables this rather than flat augmentation.

Looking at the novelty angle, this work sits at the intersection of curriculum learning for adversarial robustness, encoding-specific attacks, and guardrail hardening. The core contribution is applying curriculum structure to encoding complexity, which is a reasonable but somewhat incremental combination—essentially curriculum learning in a new domain. The 2-stage curriculum design itself is fairly straightforward. The more interesting novelty claim is the generalization to held-out encodings, which could be the stronger angle here.

On significance, the problem is genuinely important and timely given the attack success rates cited, but whether this defense actually gets adopted in practice remains an open question.

I'm realizing the generalization story might actually be the primary contribution rather than the curriculum ordering itself. Showing that curriculum-trained classifiers generalize to entirely unseen encoding types is more surprising and novel than just demonstrating that curriculum ordering helps—that feels somewhat predictable. The generalization claim is where the real novelty lies.

There's also an underdeveloped claim about complexity-structured curriculum being a general principle for adversarial robustness whenever attack difficulty has a natural ordering independent of model capability. This is actually quite strong and could be positioned as a more fundamental contribution than the specific application to encodings.

The curriculum design itself feels ad-hoc though. Why exactly 2 stages? Why group these particular encoding types together? Without a principled framework for determining the ordering—like a formal encoding complexity metric—the contribution feels less generalizable and more hand-designed. That's where the rigor could be significantly strengthened.

There's also a simpler alternative I should address: what if a learned canonicalization model, like a seq2seq system trained to normalize encoded inputs back to plaintext before hitting the guardrail, could achieve similar results without needing curriculum learning at all? The proposal needs to explicitly consider and rule this out.

And the central claim about "encoding-invariant features" is still underspecified. There's no clear theoretical mechanism for why progressive exposure to increasingly complex encodings would produce these features in the first place, versus just flat augmentation. That's the conceptual gap that needs filling.

The curriculum ordering itself might also be misguided. Rather than ordering by structural complexity like nesting depth, the difficulty should probably be determined by how much each encoding disrupts the tokenizer's understanding of the text. A base64 string and a homoglyph substitution behave very differently at the token level, so the curriculum should reflect that tokenizer-level disruption, not abstract structural properties.

Now I'm thinking through what would make this paper strongest: reframing generalization as the primary claim rather than just robustness, formalizing the encoding complexity metric to make it less ad-hoc, directly addressing why learned canonicalization wouldn't be a simpler explanation, and sharpening the mechanistic argument for why curriculum learning beats flat augmentation. The core idea itself seems sound—the problem is real, the approach is reasonable, and the ablations test the right things. There's genuine potential here, though some key points need tightening.

I'm also checking whether recent related work might undermine the novelty. I've already accounted for ACE-Safety, Ilin et al., AprielGuard, TRYLOCK, and Broken-Token, but I should verify whether DuoGuard or LlamaGuard3 have explored encoding robustness in ways that would overlap with this work. I'm realizing the core novelty might come across as incremental—just applying curriculum learning to encoding attacks. To strengthen this, the paper should either highlight what's specifically different about how curriculum learning works for encodings, like how the staged approach builds compositional understanding, or lean heavily on the generalization results showing that curriculum-ordered training transfers to unseen encoding types while random ordering fails.

My main recommendation is to reframe the contribution as showing that encoding-complexity curriculum enables generalization to held-out encoding types, rather than just improving robustness to the encodings seen during training. That's the genuinely surprising finding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c050cad-654f-4a1a-a41e-c7deb374ded9",
  "isSidechain": false,
  "requestId": "req_011Cb6EH5kDixWtT4UCNEBjA",
  "type": "assistant",
  "uuid": "f3117b7b-e56f-4d89-b3d0-d6374c3a662c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "26f38bba-2519-4824-b5c2-e0bb6981faaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KPt9EuWBszKvg3HYbfNR9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19823,
      "cache_read_input_tokens": 0,
      "output_tokens": 4979,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19823,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4979,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 19823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19823
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-16T12:16:49.911Z_

【状态】: 有发掘空间

---

【发掘点 1】
- 维度: novelty 锐化
- 内容: 当前 proposal 的 primary contribution 定位为"encoding-complexity curriculum 优于 flat augmentation 和 model-evolution curriculum"。但这个 claim 的 surprise level 偏低——一个有经验的审稿人会说："当 attack difficulty 有 natural ordering 的时候，curriculum learning 优于 random ordering，这不是 curriculum learning 文献早就建立的结论吗？你只是把它搬到了 encoding domain。" 真正 surprising 的结果是 **generalization to held-out encoding types**：如果 curriculum-ordered training 能泛化到 Braille/Morse 而 random-order training 和 flat augmentation 不能，这才是 non-trivial 的发现。建议 **将 generalization 提升为 primary contribution，将 curriculum design 降为 enabling mechanism**。重新 framing 为"encoding-complexity curriculum teaches encoding-invariant harmful-content features that generalize to unseen encoding families"，核心 claim 变成一个关于表征学习的发现（classifier 学到了 encoding-agnostic features），而非一个关于训练策略的工程选择。这样的 claim 审稿人更难用 "I would have guessed this" 来 dismiss。
- 价值: 直接提升 Novelty 维度。将 paper 的核心贡献从"已知原则的 domain-specific application"提升为"关于 adversarial robustness 中 feature learning 的 insight"，天花板从 borderline 的 method paper 提升到有 conceptual contribution 的工作。

【发掘点 2】
- 维度: 前提假设质疑
- 内容: Proposal 断言"encoding difficulty is determined by structural properties (nesting depth, CPT-ratio preservation, cross-script mixing) rather than model-evolution differentials"，但这个前提本身未经验证，且可能是错误的。Classifier 对不同 encoding 的实际 difficulty 可能主要由 **tokenizer behavior** 决定——同样是单层 encoding，base64 和 homoglyph substitution 的 tokenization pattern 差异巨大，对 classifier 而言 difficulty gap 可能远超 nesting depth 的影响。当前 2-stage curriculum 的分组逻辑（Stage 1 = single encoding, Stage 2 = composite）是一个**未经验证的 heuristic**，审稿人会问："你怎么知道 nesting depth 是 difficulty 的 right axis？如果按 tokenizer disruption degree 排序效果更好呢？" 建议在 idea 层面引入一个 **formalized encoding complexity metric**（例如，综合 nesting depth、CPT deviation、tokenizer perplexity 的 composite score），并将 curriculum ordering 定义为沿这个 metric 的 progressive escalation。这不仅让 curriculum 有了 principled grounding，还直接强化了"general principle"的 claim——复杂度度量本身就是可迁移的方法论贡献。
- 价值: 同时命中 Novelty 和 Significance。将 curriculum design 从 ad-hoc 2-stage heuristic 提升为 principled framework，挡住"为什么是这个 ordering"的审稿质疑，同时为 generalization claim 提供更强的理论支撑（如果 metric 能预测 held-out encodings 的 difficulty，这本身就是一个 finding）。

【发掘点 3】
- 维度: trivial alternative 威胁
- 内容: Proposal 讨论了 rule-based canonicalization (TRYLOCK) 和 static CPT-Filtering (Broken-Token) 的局限性，但遗漏了一个更有力的 trivial alternative：**learned input canonicalization**。训练一个 seq2seq model（甚至一个轻量 encoder-decoder）将任意 encoded input 解码回 plaintext，然后喂给标准 guardrail classifier。这个 pipeline approach 不需要 curriculum learning，不需要 adversarial co-training，计算成本可能远低于 GRPO co-evolutionary loop。如果这个 simple baseline 效果接近，EncoGuard 的增量价值就很有限。Proposal 需要在 idea 层面明确论证为什么 **end-to-end encoding-robust classification** 优于 **canonicalization + standard classification** 的 pipeline——可能的论点包括：(a) canonicalization 是 error-propagating pipeline，decode 错误直接导致 classifier 失效；(b) 对 adversarially designed encodings，canonicalization 本身是一个 adversarial game，需要和攻击者 co-evolve；(c) partial encoding 场景下，正确 decode 需要 understanding 哪些部分是 encoded，这本身就需要 semantic understanding。不论论证方向如何，不正面回应这个 alternative 是一个 clear vulnerability。
- 价值: 命中 Novelty 和 Related Work 差异化。堵住审稿人最可能提出的"为什么不直接做 learned normalization"的质疑，同时通过回应这个 alternative 进一步锐化 EncoGuard 的 design rationale。

【发掘点 4】
- 维度: 核心 claim 强化
- 内容: Proposal 声称 curriculum 让 classifier 学到了"encoding-invariant features"，但从未解释 **why** curriculum ordering 比 flat exposure 更能产出 encoding-invariant representations。这是核心 claim 的逻辑链中一个缺失的环节。一个有力的论证可以基于 curriculum learning theory 中的 catastrophic confusion avoidance：**flat exposure 下，classifier 同时面对 simple 和 complex encodings，对 complex encodings 的 gradient signal 在早期训练中是噪声（因为 classifier 尚未建立基础的 encoding-aware features），这些 noisy gradients 干扰 simple encoding 的 feature learning；curriculum ordering 让 classifier 先在 simple encodings 上建立 robust token-level encoding-detection features，这些 features 作为 compositional building blocks 支撑 complex encoding 的 feature learning**。这个论证将"curriculum 有用"从一个经验观察提升为一个有 mechanistic motivation 的 claim，也自然解释了为什么 generalization 能发生：compositional building blocks 是 encoding-type-agnostic 的。
- 价值: 命中 Novelty 和 Significance。为核心 claim 提供 mechanistic grounding，将 paper 从"empirical observation that curriculum helps"提升到"mechanistically motivated principle + empirical validation"，这正是 EMNLP main 期待的贡献深度。

【发掘点 5】
- 维度: significance 提升
- 内容: Proposal 最后提到"complexity-structured curriculum is a general principle for adversarial robustness"并列举了 multi-turn staged delivery、tool-call obfuscation、cross-modal attack chains 作为 future directions，但这个 framing 目前是 hand-waving。问题在于：如果这只是 conclusion 里的一段展望，审稿人会直接忽略它。要真正提升 significance，需要将这个 general principle 在 paper 的 positioning 中前置——**将 encoding attacks 明确定位为"attack difficulty has natural complexity ordering"这一类攻击的 canonical instance**，在 introduction 中就建立这个 framing。然后，结论中不仅列举其他 domains，还要给出一个 **concrete formalization**：什么条件下 complexity-structured curriculum 适用？(a) attack space 有 composable primitives；(b) primitives 有 partial ordering on complexity；(c) defense model 的 feature learning 具有 compositional structure。这让 paper 的 contribution 从"encoding defense method"升级为"a general adversarial robustness principle demonstrated on encoding attacks"。这也回应了发掘点1的 re-framing——generalization 是 principle 的 evidence，curriculum 是 principle 的 instantiation。
- 价值: 直接提升 Significance 维度。一个 domain-specific defense method paper 和一个 establish a general principle 的 paper 在 impact 上有数量级差异。这个 re-positioning 不需要额外实验（encoding 就是 demonstration domain），但大幅提升审稿人对 paper 影响力的感知。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3117b7b-e56f-4d89-b3d0-d6374c3a662c",
  "isSidechain": false,
  "requestId": "req_011Cb6EH5kDixWtT4UCNEBjA",
  "type": "assistant",
  "uuid": "b710dc40-ea88-4571-9ba4-d4249d1e4e93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "26f38bba-2519-4824-b5c2-e0bb6981faaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KPt9EuWBszKvg3HYbfNR9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19823,
      "cache_read_input_tokens": 0,
      "output_tokens": 4979,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19823,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4979,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 19823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19823
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# EncoGuard: Encoding-Complexity Curriculum for Hardening Guardrail Classifiers Against Character-Level Evasion  **状态**: PENDING_REVIEW **级别**: top-tier **创建时间**: 2026-05-16T09:42:11.878561+00:00 **来源…",
  "leafUuid": "b710dc40-ea88-4571-9ba4-d4249d1e4e93",
  "sessionId": "26f38bba-2519-4824-b5c2-e0bb6981faaf"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Encoding-complexity curriculum for guardrail robustness",
  "sessionId": "26f38bba-2519-4824-b5c2-e0bb6981faaf"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# EncoGuard: Encoding-Complexity Curriculum for Hardening Guardrail Classifiers Against Character-Level Evasion  **状态**: PENDING_REVIEW **级别**: top-tier **创建时间**: 2026-05-16T09:42:11.878561+00:00 **来源…",
  "leafUuid": "b710dc40-ea88-4571-9ba4-d4249d1e4e93",
  "sessionId": "26f38bba-2519-4824-b5c2-e0bb6981faaf"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Encoding-complexity curriculum for guardrail robustness",
  "sessionId": "26f38bba-2519-4824-b5c2-e0bb6981faaf"
}
```

---
