# Research conversation: [HANDOFF] 你是 Director，这是 Loop #11。 ## 上一轮交接 (task_context) ### 1. 🔴 硬约束 / 红线 - EMNLP 2026 ARR 正文严格 8 页限制，当前恰好 8 页——任何正文内 — Part 7 of 7

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

[← Part 6](part-006.md) · [Transcript overview](../research-conversation-handoff-director-loop-11-task-context-1-emnlp-2026-arr-8-8.md) · [Structured JSON](../../../sessions/bb/bba85b95582788f6859e.json)

## Round 141

### Runtime record

_source line 1876 · 2026-05-25T19:48:11.402Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T19:48:11.402Z",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "content": "&lt;task-notification>\n&lt;task-id>a16b2408c4cfcd2a6&lt;/task-id>\n&lt;tool-use-id>toolu_01Y8sq2Cw76Rnx2iUs5eZQ6i&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-director-8494441a/485a49b0-2f8a-4e9c-b75d-f286f7540b25/tasks/a16b2408c4cfcd2a6.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Extract appendix numbers\" completed&lt;/summary>\n&lt;result>Now I have read all 25 appendix files. Let me compile the complete numerical extraction.\n\n---\n\n## appendix_prompts.tex\n- \"96\" — number of Wikidata relation types in DocRED system prompt (line ~36)\n- \"6\" — entity types listed for DocRED (line ~35)\n\n---\n\n## appendix_related_work.tex\n- \"100×\" — speedup of XGrammar over prior CFG-constrained decoding (line ~9)\n- \"13\" — number of IE datasets UIE trains on (line ~55)\n- \"29K\" — number of entity types from Wikidata encoded in KnowCoder (line ~57)\n- \"50%\" — reduction in compilation errors by type-constrained codegen (line ~28)\n- \"98.8%\" — ODKE+ precision across 195 predicates (line ~72)\n- \"195\" — number of predicates in ODKE+ (line ~72)\n- \"10×\" — violation reduction by OntoLogX iterative re-prompting (line ~74)\n- \"29%\" — F1 improvement by constrained inference on CaRB (line ~75)\n- \"94%\" — F1 accuracy@10 achieved by RELATE on ChemProt (line ~77)\n- \"15.37%\" — fraction of generated triples with domain/range violations under unconstrained decoding (line ~83)\n- \"DR↓94% on SciERC\" — DR reduction claim (line ~85)\n- \"↓45–90% on DocRED\" — DR reduction range on DocRED (line ~85)\n- \"+0.13pp\" — F1 gain on SciERC (p=0.58) (line ~98)\n- \"p=0.58\" — p-value for SciERC F1 (line ~98)\n- \"p&lt;0.001\" — p-value for DocRED Qwen R-F1 (line ~98)\n- \"p=0.013\" — p-value for DocRED Llama R-F1 (line ~98)\n- \"7B–70B\" — model scale range evaluated (line ~108)\n- \"p≤0.013\" — significance threshold for DocRED R-F1 gains (line ~109)\n- \"15.37%→0.93%\" — DR reduction on SciERC (line ~98)\n- \"45–90%\" — DR reduction range on DocRED (line ~109)\n\n---\n\n## appendix_discussion.tex\n- \"100%\" — fraction of Qwen3-8B CF violations from registry override (line ~17)\n- \"5,882\" — Llama-3.1-8B grammar-first fallbacks on SciERC (line ~17)\n- \"10.7\" — fallbacks per document on SciERC for Llama (line ~17)\n- \"57,825\" — Llama-3.1-8B grammar-first fallbacks on DocRED (line ~17)\n- \"63.8\" — fallbacks per document on DocRED for Llama (line ~17)\n- \"2.57%\" — Qwen CF on DocRED (line ~18)\n- \"12.02%\" — Llama CF on DocRED (line ~18)\n- \"36.6%\" — token-level fallback rate on SciERC Llama (line ~28)\n- \"2.87\" — average BPE tokens for OtherScientificTerm type name (line ~28)\n- \"0.04–5.7%\" — first-token fallback rate range zero-shot (line ~28)\n- \"≤0.11%\" — fallback rate under fine-tuning (line ~28)\n- \"4.5%\" — registry-consistent fallback rate (line ~31)\n- \"36.6%\" — grammar-first fallback rate (f_gf), SciERC Llama (line ~34)\n- \"6,237 of 17,024\" — mask calls resulting in fallback on SciERC Llama (line ~34)\n- \"63.4%\" — effective semantic constraint coverage on SciERC Llama (line ~34)\n- \"46 of 54,859\" — fallback events on DocRED Qwen (line ~35)\n- \"0.08%\" — f_gf on DocRED Qwen (line ~35)\n- \"99.9%\" — effective coverage on DocRED Qwen (line ~35)\n- \"2.87\" — mask calls per type field for OtherScientificTerm (line ~36)\n- \"100%\" — effective coverage Qwen3-8B on SciERC (line ~39)\n- \"0.93% vs. Llama's 0.08%\" — residual DR comparison (line ~39, note: Qwen vs Llama reversed from main text)\n- \"24%\" — DR reduction by semantic layer without grammar layer (line ~79)\n- \"2.71%\" — CF rises to this under semantic-only ablation (line ~82)\n- \"0.08%\" — CF without semantic-only ablation (line ~82)\n- \"2.63pp\" — additional violations from structural ambiguity (line ~82)\n- \"9.90%\" — CF on SciERC zero-shot (line ~92)\n- \"12.02%\" — CF on Llama DocRED (line ~92)\n- \"0.93%\" — S1 DR on SciERC (table line ~103)\n- \"9.90%\" — S1 CF on SciERC (table line ~103)\n- \"10.83%\" — DR+CF total under S1 (table line ~103)\n- \"14.78%\" — DR under CF fallback (table line ~104)\n- \"0.04%\" — CF under CF fallback (table line ~104)\n- \"14.82%\" — DR+CF total under CF fallback (table line ~104)\n- \"36.64%\" — f_gf under CF fallback (table line ~104)\n- \"+13.85pp\" — DR increase from CF fallback (line ~106)\n- \"-9.86pp\" — CF decrease from CF fallback (line ~106)\n- \"+3.99pp\" — total violation increase from CF fallback (line ~106)\n- \"15.9×\" — DR increase multiplier (0.93%→14.78%) (line ~113)\n- \"36.64%\" — token-level fallback rate at type-bearing positions (line ~117)\n- \"0.46%\" — first-token position fallback rate (line ~117)\n- \"3 models × 2 datasets\" — scope of DR/CF inverse association (line ~121)\n- \"63.3%\" — fraction of CF violations involving Generic type on SciERC (line ~124)\n- \"9.90%→1.18%\" — CF reduction with LoRA fine-tuning (line ~127)\n- \"88%\" — relative CF reduction from LoRA (line ~127)\n- \"1.18%\" — residual CF after LoRA (line ~128)\n- \"551\" — SciERC document count (multiple occurrences)\n\n**Causal tracing table (lines 59–64):**\n- Qwen3-8B FT S1: Fallback 0/2256 (0%), DR=0\n- Qwen3-8B ZS S1: Fallback 16/3458 (0.46%), DR=16, From FB=100%\n- Llama-3.1-8B FT S1: Fallback 1/2162 (0.05%), DR=1, From FB=100%\n- Llama-3.1-8B ZS S1: Fallback 1/2630 (0.04%), DR=1, From FB=100%\n- \"18\" — total residual DR violations across four configurations (line ~70)\n- \"≤0.05%\" — fallback rate after fine-tuning (line ~71)\n\n**CF-DR trade-off table:**\n- \"0.93\" DR, \"9.90\" CF, \"10.83\" DR+CF — S1 baseline (line ~103)\n- \"14.78\" DR, \"0.04\" CF, \"14.82\" DR+CF, \"36.64\" f_gf — CF fallback (line ~104)\n\n**Bootstrap CIs table (lines 181–191):**\n- Qwen3-8B/SciERC: ΔR-F1 = −0.10pp, 95% CI [−0.30, 0.00], p=.726, d=−0.05\n- Qwen3-8B/DocRED: ΔR-F1 = −0.31pp, 95% CI [−0.69, +0.01], p=.056, d=−0.37\n- Llama-3.1-8B/SciERC: ΔR-F1 = +0.02pp, 95% CI [0.00, +0.07], p=.736, d=+0.01\n- Llama-3.1-8B/DocRED: ΔR-F1 = +0.06pp, 95% CI [−0.11, +0.25], p=.535, d=+0.07\n- Qwen3-8B/SciERC DR: Δ=−1.95, CI [−2.87, −1.11], p&lt;.001, d=−6.15\n- Qwen3-8B/DocRED DR: Δ=−0.75, CI [−1.07, −0.48], p&lt;.001, d=−7.00\n- Llama-3.1-8B/SciERC DR: Δ=−1.02, CI [−1.98, −0.29], p&lt;.001, d=−3.17\n- Llama-3.1-8B/DocRED DR: Δ=−0.29, CI [−0.53, −0.10], p&lt;.001, d=−3.02\n- \"k=4\" — comparisons for Bonferroni correction (line ~167)\n- \"α_adj=0.0125\" — adjusted alpha (line ~167)\n- \"|d|≤0.37\" — max effect size for R-F1 (line ~167)\n- \"p_B=1.00\" — Qwen3-8B/SciERC corrected p (line ~168)\n- \"p_B=0.224\" — Qwen3-8B/DocRED corrected p (line ~168)\n- \"p_B=1.00\" — Llama-3.1-8B/SciERC corrected p (line ~168)\n- \"p_B=1.00\" — Llama-3.1-8B/DocRED corrected p (line ~168)\n- \"|d|≥3.0\" — minimum DR effect size (line ~169)\n- \"all p_Bonf&lt;0.005\" — DR reduction significance (line ~169)\n- \"10,000\" — bootstrap iterations (line ~166)\n- \"seed=42\" — bootstrap seed (line ~166)\n\n**Practical significance:**\n- \"~8%\" — zero-shot relation F1 on both datasets (line ~205)\n- \"49–53%\" — supervised SOTA on SciERC (line ~206)\n- \"1–2%\" — residual DR after LoRA (line ~208)\n\n**Post-hoc filtering comparison:**\n- \"8.63 vs. 8.36\" — SciERC post-hoc vs. OntoCoDec F1 (line ~218)\n- \"9.61 vs. 8.23\" — DocRED post-hoc vs. OntoCoDec F1 (line ~218)\n- \"48.1%\" — DocRED triples discarded by post-hoc filtering (line ~221)\n- \"127\" — true positives lost in DocRED post-hoc (line ~221)\n- \"11.2%\" — fraction of correct predictions lost (line ~221)\n- \"9.46%→8.40%\" — recall drop from post-hoc filtering (line ~221)\n- \"2.47%\" — residual ET for post-hoc (line ~223)\n- \"0%\" — OntoCoDec ET (line ~223)\n\n**CF violation distribution table (lines 249–260):**\n- Generic ↔ OtherScientificTerm: 85 (34.7%)\n- Generic ↔ Material: 35 (14.3%)\n- Generic ↔ Metric: 30 (12.2%)\n- Method ↔ Task: 20 (8.2%)\n- Material ↔ Method: 17 (6.9%)\n- OtherScientificTerm ↔ Task: 12 (4.9%)\n- 10 further pairs (each ≤3.3%): 46 (18.8%)\n- Total: 245 (100.0%)\n- \"248 CF violations\" / \"245 unique entity-document pairs\" (line ~235)\n- \"63.3%\" — Generic-involving violations (line ~236)\n- \"155/245\" — count/total for Generic (line ~236)\n- \"53/162, 32.7%\" — Generic↔OtherScientificTerm on Llama SciERC (line ~239)\n- \"76.6%\" — MISC-driven Qwen DocRED CF violations (line ~239)\n- \"≤1%\" — CF rates under unconstrained decoding (line ~240)\n\n**Cascade error breakdown table (lines 289–296):**\n- Hallucinated entity: 144 (58.1%)\n- Correct type lock: 45 (18.1%)\n- True cascade error: 18 (7.3%)\n- Other/ambiguous: 41 (16.5%)\n- Total: 248 (100.0%)\n- \"2.5×\" — correct type locks more frequent than true cascade errors (line ~276)\n- \"22 CF violations, 20 documents\" — fine-tuned CF (line ~278)\n- \"0/22\" — cascade errors under fine-tuning (line ~279)\n\n**Per-relation DR elimination table (lines 324–331):**\n- Evaluate-for: κ=0.361, LoRA DR=13.13%, n=99; S1 DR=0%, n=98\n- Part-of: κ=0.417, LoRA DR=5.77%, n=52; S1 DR=0%, n=52\n- Compare: κ=0.528, LoRA DR=5.00%, n=40; S1 DR=0%, n=40\n- Conjunction: κ=0.306, LoRA DR=1.31%, n=153; S1 DR=0%, n=153\n- Feature-of: κ=0.278, LoRA DR=1.35%, n=74; S1 DR=0%, n=74\n- Used-for: κ=0.028, LoRA DR=0.16%, n=634; S1 DR=0%, n=635\n- Hyponym-of: κ=0.417, DR=0%\n\n**Fine-tuned four-way ablation table (lines 357–381):**\nSciERC Qwen3-8B:\n- Unconstrained: DR=1.95, RV=0, ET=0, CF=0, PF=0, E-F1=67.05, R-F1=43.86\n- Grammar: DR=1.90, RV=0, ET=0, CF=0, PF=0, E-F1=67.05, R-F1=43.86\n- Semantic: DR=0.60, RV=0, ET=0, CF=0.18, PF=0, E-F1=67.05, R-F1=43.69\n- S1: DR=0, RV=0, ET=0, CF=1.18, PF=0, E-F1=67.05, R-F1=43.77\n\nSciERC Llama-3.1-8B:\n- Unconstrained: DR=1.11, RV=0, ET=0, CF=0, PF=0, E-F1=67.76, R-F1=45.45\n- Grammar: DR=1.11, RV=0, ET=0, CF=0, PF=0, E-F1=67.76, R-F1=45.45\n- Semantic: DR=0.65, RV=0, ET=0, CF=0.10, PF=0, E-F1=67.76, R-F1=45.47\n- S1: DR=0.09, RV=0, ET=0, CF=0.46, PF=0, E-F1=67.76, R-F1=45.47\n\nDocRED Qwen3-8B:\n- Unconstrained: DR=0.76, RV=0.27, ET=0, CF=0.12, PF=7.11, E-F1=82.15, R-F1=40.86\n- Grammar: DR=0.61, RV=0, ET=0, CF=0.11, PF=7.01, E-F1=82.19, R-F1=40.85\n- Semantic: DR=0.19, RV=0.23, ET=0, CF=0.27, PF=7.52, E-F1=82.15, R-F1=40.85\n- S1: DR=0.01, RV=0, ET=0, CF=0.41, PF=8.52, E-F1=81.43, R-F1=40.56\n\nDocRED Llama-3.1-8B:\n- Unconstrained: DR=0.49, RV=0.15, ET=0, CF=0.08, PF=2.30, E-F1=83.93, R-F1=43.72\n- Grammar: DR=0.51, RV=0, ET=0, CF=0.12, PF=2.30, E-F1=84.04, R-F1=43.72\n- Semantic: DR=0.48, RV=0.15, ET=0, CF=0.16, PF=2.40, E-F1=84.02, R-F1=43.85\n- S1: DR=0.21, RV=0, ET=0, CF=0.21, PF=2.51, E-F1=83.94, R-F1=43.78\n\n- \"41–69%\" — semantic layer DR reduction on SciERC FT (line ~392)\n- \"2–75%\" — semantic layer DR reduction on DocRED FT (line ~392)\n- \"80 violations in 16,074 triples\" — Llama DocRED DR denominator (line ~392)\n- \"DR≤0.21%\" — near-complete elimination in all 4 FT settings (line ~393)\n- \"-0.30pp\" — max R-F1 decrease S1 vs. unconstrained (line ~394)\n\n**DocRED Zero-Shot Ablation table (lines 420–439):**\n- Unconstrained: DR=18.46, ΔDR=---, RV=29.66, ET=2.48, CF=0.10, Total=18.56, Rel.=7.74, Ent.=58.15\n- Grammar: DR=26.17, ΔDR=↑42%, RV=0.03, ET=0, CF=0.07, Total=26.24, Rel.=8.31, Ent.=59.38\n- Semantic: DR=13.84, ΔDR=↓25%, RV=29.87, ET=4.22, CF=1.05, Total=14.89, Rel.=7.70, Ent.=57.81\n- S1: DR=10.21, ΔDR=↓45%, RV=0.03, ET=0, CF=2.57, Total=12.78, Rel.=8.23, Ent.=59.37\n- \"+0.49pp\" — R-F1 bootstrap significance (p&lt;0.001) (line ~446)\n\n**Residual DR error analysis (lines 461–465):**\n- Entity type errors: 39%\n- Schema coverage gaps: 33%\n- Incorrect relation selection: 17%\n- Direction reversal: 11%\n- \"3 of 36\" — non-Llama DocRED residual violations (line ~468)\n- \"33 of 36\" — Llama DocRED residual violations (line ~469)\n- \"92%\" — Llama DocRED share of residual (line ~469)\n- \"14/33, 42%\" — entity type errors in Llama DocRED (line ~469)\n- \"36\" — total fine-tuned residual DR violations (line ~457)\n\n**Post-hoc extended table (lines 490–510):**\nZS:\n- Qwen/SciERC: Reject=16.8%, R-F1_ph=8.63, R-F1_cd=8.36, ph wins\n- Llama/SciERC: Reject=13.9%, R-F1_ph=2.71, R-F1_cd=2.54, ph wins\n- Mistral/SciERC: Reject=20.3%, R-F1_ph=3.94, R-F1_cd=3.67, ph wins\n- Qwen/DocRED: Reject=48.1%, R-F1_ph=9.61, R-F1_cd=8.23, ph wins\n- Llama/DocRED: Reject=42.2%, R-F1_ph=7.44, R-F1_cd=6.27, ph wins\n- Mistral/DocRED: Reject=73.7%, R-F1_ph=3.85, R-F1_cd=5.52, cd wins\nFT:\n- Qwen/SciERC: Reject=1.95%, R-F1_ph=43.94, R-F1_cd=43.77, ph wins\n- Llama/SciERC: Reject=1.11%, R-F1_ph=45.23, R-F1_cd=45.47, cd wins\n- Qwen/DocRED: Reject=1.03%, R-F1_ph=41.11, R-F1_cd=40.79, ph wins (note: likely 40.56 in main FT table — potential inconsistency)\n- Llama/DocRED: Reject=0.64%, R-F1_ph=43.92, R-F1_cd=43.78, cd wins\n- \"~70%\" — crossover rejection rate (line ~513)\n- \"+1.67pp\" — cd advantage at &gt;70% rejection (line ~513)\n- \"Δ≤0.55pp\" — FT convergence (line ~515)\n\n**Runtime:**\n- \"4.163 s/doc\" — SciERC unconstrained inference (line ~522)\n- \"4.710 s/doc\" — SciERC S1 constrained decoding (line ~522)\n- \"+13.1%\" — overhead (line ~522)\n- \"0.044 s\" — XGrammar compilation (line ~524)\n- \"0.33 s\" — full constraint pipeline compilation on SciERC (line ~524)\n- \"2.612 s/doc\" — fine-tuned unconstrained inference (line ~529)\n- \"2.873 s/doc\" — fine-tuned S1 constrained (line ~529)\n- \"+10.0%\" — fine-tuned overhead (line ~529)\n- \"n=551\" — document count for fine-tuned latency (line ~529)\n- \"37%\" — absolute generation time drop under FT vs. ZS (line ~530)\n\n**Fuzzy matching:**\n- \"80%\" — token overlap threshold (line ~538)\n- \"≤2\" — edit distance threshold (line ~538)\n- \"98\" — additional TPs from fuzzy matching on Mistral DocRED (line ~540)\n- \"+0.84pp\" — R-F1 from fuzzy matching (line ~540)\n- \"3.50% vs. 4.34%\" — strict vs. fuzzy R-F1 for Mistral (line ~540)\n\n**Prompt comparison table (lines 562–568):**\nSciERC Unconstrained: DR=15.4, RV=1.4, ET=0.4, CF=0.1\nSciERC Schema-informed: DR=5.8, RV=0.3, ET=0.0\nDocRED Unconstrained: DR=18.5, RV=29.7, ET=2.5, CF=0.1\nDocRED Schema-informed: DR=12.8, RV=18.4, ET=0.2, CF=0.2\n\n**WikiEvents:**\n- \"56\" — event types (line ~576)\n- \"80\" — argument roles (line ~576)\n- \"27\" — entity types (line ~576)\n- \"245\" — (event_type, role)→allowed_entity_types constraints (line ~576)\n- \"mean κ̄=0.82\" — WikiEvents role-level tightness (line ~582)\n- \"median 0.89\" — WikiEvents median κ (line ~582)\n- \"84%\" — fraction of roles with κ≥0.80 (line ~582)\n- \"4 or fewer\" — valid entity types for roles with κ≥0.80 (line ~582)\n- \"50%\" — AC rate for roles with κ≥0.90 (line ~583)\n- \"21%\" — AC rate for 0.80≤κ&lt;0.90 (line ~583)\n- \"30%\" — AC rate for loose (κ&lt;0.80) roles (line ~583)\n- \"0%\" — AC for Transportation.Vehicle→VEH (line ~584)\n- \"κ=0.963\" — tightness for Transportation.Vehicle→VEH (line ~584)\n- \"126 args, 34% AC, κ=0.59\" — Attack.Target role (line ~585)\n\n**Lucky violations table (lines 606–611):**\n- Qwen3-8B/SciERC: DR 1.95→0, Lucky=4 (0.41%), ΔRecall=−0.10, Churn=0.22%\n- Llama-8B/SciERC: DR 1.11→0.09, Lucky=5 (0.51%), ΔRecall=±0.00, Churn=0%\n- Qwen3-8B/DocRED: DR 1.03→0.01, Lucky=1 (0.01%), ΔRecall=−0.84, Churn=2.05%\n- Llama-8B/DocRED: DR 0.64→0.21, Lucky=1 (0.01%), ΔRecall=−0.10, Churn=0.86%\n- Average lucky: 0.24%, average ΔRecall=−0.26, average churn=0.78%\n\n**Trie-only baseline table (lines 642–655):**\n- Qwen3-8B LoRA: ET=0, RV=0, DR=95.5%, CF=0.09, R-F1=41.16, PF=9.1%\n- Qwen3-8B ZS: ET=0, RV=0, DR=29.3%, CF=0, R-F1=8.64, PF=0%\n- Llama-8B LoRA: ET=0, RV=0, DR=15.2%, CF=0, R-F1=19.95, PF=50.8%\n- Llama-8B ZS: ET=0, RV=0, DR=84.4%, CF=0.36, R-F1=2.90, PF=0%\nDR gaps vs S1:\n- Qwen3-8B LoRA: S1=0%, Trie=95.5%, Gap=95.5pp\n- Qwen3-8B ZS: S1=0.93%, Trie=29.3%, Gap=28.4pp\n- Llama-8B LoRA: S1=0.09%, Trie=15.2%, Gap=15.1pp\n- Llama-8B ZS: S1=0.08%, Trie=84.4%, Gap=84.3pp\n- \"83%\" — fraction of triples with entity type fields omitted under trie-only (line ~628)\n- \"0–51%\" — parse failure range for trie-only (line ~628)\n- \"15–96%\" — DR range for trie-only (line ~628)\n- \"50.8%\" — Llama LoRA parse failure (line ~629)\n- \"45.47→19.95\" — R-F1 collapse (line ~629)\n\n**vLLM verification table (lines 714–717):**\n- Grammar-Only (XGrammar): DR=14.84, RV=0, ET=0, CF=9.90, R-F1=8.23\n- vLLM guided_json: DR=15.26, RV=0, ET=0, R-F1=8.75\n- Δ: DR=+0.42, R-F1=+0.52\n- \"~15%\" — DR left unaddressed by CFG-based approaches (line ~724)\n\n**Dual-factor analysis:**\n- \"y=0.366x−0.138\" — linear fit (line ~140)\n- \"R²=0.886\" — fit quality (line ~140)\n- \"n=4\" — data points (line ~140)\n- \"F(1,2)=15.54\" — F-statistic (line ~140)\n- \"p≈0.058\" — p-value (line ~140)\n- \"7.58%\" — Mistral-7B unconstrained ET on DocRED (line ~142)\n- \"33.21%\" — Mistral residual DR on DocRED (line ~142)\n- \"&gt;5%\" — ET threshold for principled exclusion (line ~143)\n- \"0.842\" — DocRED κ̄ (line ~144)\n- \"0.333\" — SciERC κ̄ (line ~144)\n\n**Dataset-dependent F1:**\n- \"+0.49pp\" — DocRED R-F1 gain (p&lt;0.001) (line ~153)\n- \"+0.13pp\" — SciERC R-F1 gain (p=0.58) (line ~153)\n- \"29.66%\" — DocRED baseline RV (line ~154)\n- \"5,189\" — OOV predictions as false positives (line ~154)\n- \"1.39%\" — SciERC baseline RV (line ~155)\n- \"24\" — SciERC OOV predictions (line ~155)\n- \"16.03%\" — Llama DocRED baseline RV (line ~156)\n- \"+0.29pp\" — Llama DocRED R-F1 gain (line ~156)\n\n---\n\n## appendix_70b_ablation.tex\n\n**SciERC 70B table (lines 21–27):**\n- Unconstrained: DR=1.50, RV=0, ET=0, CF=0, R-F1=44.73, E-F1=64.86\n- Grammar: DR=1.50, RV=0, ET=0, CF=0, R-F1=44.63, E-F1=64.82\n- Semantic: DR=0.60, RV=0, ET=0, CF=9, R-F1=44.73, E-F1=64.86\n- S1: DR=0, RV=0, ET=0, CF=15, R-F1=44.53, E-F1=64.76\n- S2: DR=0, RV=0, ET=0, CF=18, R-F1=36.28, E-F1=62.35\n- Beam4 S1: DR=0, RV=0, ET=0, CF=1, R-F1=44.81, E-F1=64.89\n- \"+3.58pp\" — DR increase from grammar-only on DocRED ZS (line ~34)\n- \"60%\" — semantic layer DR reduction at 70B (line ~35)\n- \"−8.45pp\" — S2 R-F1 degradation vs. S1 on SciERC (line ~36)\n- \"k=4\" — optimal beam width (line ~37)\n\n**DocRED LoRA 70B table (lines 58–64):**\n- Unconstrained: DR=0.22, RV=0.57, ET=0, CF=2, R-F1=43.80, E-F1=80.34\n- Grammar: DR=0.38, RV=0, ET=0, CF=0.06%, R-F1=43.96, E-F1=80.13\n- Semantic: DR=0, RV=0.51, ET=0, CF=0.21%, R-F1=43.61, E-F1=80.06\n- S1: DR=0, RV=0, ET=0, CF=0.18%, R-F1=43.95, E-F1=79.38\n- S2: DR=0, RV=0, ET=0, CF=0.34%, R-F1=36.45, E-F1=84.96\n- Beam4 S1: DR=0, RV=0, ET=0, CF=0, R-F1=48.14, E-F1=85.57\n- PF: greedy S1=12.5% (25/200), S2=0% (0/200), beam4=0.5% (1/200) (line ~69)\n- \"+0.16pp\" — grammar DR increase (line ~73)\n- \"−7.50pp\" — S2 R-F1 degradation on DocRED (line ~75)\n- \"+4.19pp\" — R-F1 gain from beam search (43.95→48.14) (line ~77)\n- \"12.5%\" — greedy S1 parse failures (25/200) (line ~77)\n- \"0.5%\" — beam parse failures (1/200) (line ~77)\n- \"+0.28pp\" — pure beam quality gain on SciERC (line ~78)\n\n**DocRED ZS 70B table (lines 97–101):**\n- Unconstrained: DR=13.45, RV=7.88, ET=0, CF=0, R-F1=13.25, E-F1=70.14\n- Grammar: DR=17.03, RV=0, ET=0, CF=0, R-F1=13.23, E-F1=70.12\n- Semantic: DR=1.66, RV=8.24, ET=0.12, CF=132, R-F1=13.05, E-F1=70.10\n- S1: DR=0, RV=0, ET=0, CF=173, R-F1=13.25, E-F1=70.05\n- \"+3.58pp\" — grammar DR increase on DocRED ZS 70B (line ~108)\n- \"87.7%\" — semantic-only DR reduction (line ~109)\n- \"200-document subset\" — evaluation size (line ~103)\n\n---\n\n## appendix_llama_per_relation.tex\n\n**Per-relation table (lines 21–31):**\n- dissolved/demolished (P576): 73 triples, 24 violations, 32.9% DR\n- followed by (P156): 117 triples, 24 violations, 20.5% DR\n- unemployment rate (P1198): 15 triples, 3 violations, 20.0% DR\n- end time (P582): 130 triples, 21 violations, 16.2% DR\n- instance of (P31): 290 triples, 37 violations, 12.8% DR\n- product/material produced (P1056): 98 triples, 11 violations, 11.2% DR\n- location of formation (P740): 81 triples, 8 violations, 9.9% DR\n- head of state (P35): 41 triples, 3 violations, 7.3% DR\n- applies to jurisdiction (P1001): 637 triples, 45 violations, 7.1% DR\n- conflict (P607): 453 triples, 30 violations, 6.6% DR\n- \"16.03%\" — Llama baseline RV (line ~8)\n- \"29.66%\" — Qwen baseline RV (line ~8)\n- \"2.55%\" — Llama residual DR under S1 (line ~9)\n- \"418/16,368 triples\" — DR violations/total (line ~9)\n- \"10.21%\" — Qwen residual DR under S1 (line ~36)\n- \"83%\" — P1198 fallback rate (Qwen) (line ~36)\n- \"78%\" — P171 fallback rate (Qwen) (line ~36)\n- \"20.0%\" — Llama P1198 DR rate (line ~36)\n- \"2.55% vs. 10.21%\" — Llama vs. Qwen residual DR (line ~38)\n\n---\n\n## appendix_sampling_table.tex\n\n**Sampling table (lines 12–17):**\nSciERC (551):\n- Greedy: ET=0, RV=0, DR=0.93, CF=9.90, E-F1=30.98, R-F1=8.36\n- Sampling (T=0.7, p=0.9): ET=0, RV=0, DR=0.75, CF=9.90, E-F1=31.28, R-F1=7.42\nDocRED (114†):\n- Greedy: ET=0, RV=0.03, DR=10.21, CF=2.57, E-F1=59.37, R-F1=8.23\n- Sampling: ET=0, RV=0, DR=10.31, CF=12.63, E-F1=57.05, R-F1=7.92\n- \"T=0.7\" — sampling temperature (line ~7)\n- \"p=0.9\" — nucleus sampling parameter (line ~7)\n- \"114\" — DocRED sampling subset size (line ~15)\n- \"~300h\" — estimated time for full DocRED sampling (line ~19)\n\n---\n\n## appendix_beam_search.tex\n\n**Beam search table (lines 31–54):**\n- Qwen3-8B/SciERC: Greedy DR=0.93, CF=9.90, E-F1=30.98, R-F1=8.36; Beam DR=0, CF=0.53, E-F1=32.00, R-F1=8.56\n- Qwen3-8B/DocRED(50): Greedy DR=8.69, CF=2.08, E-F1=59.08, R-F1=8.33; Beam DR=0, CF=0.55, E-F1=58.64, R-F1=9.37\n- Llama/SciERC: Greedy DR=0.08, CF=6.56, E-F1=23.49, R-F1=2.54; Beam DR=0, CF=0.93, E-F1=25.04, R-F1=3.33\n- Llama/DocRED(50): Greedy DR=1.58, CF=6.85, E-F1=55.35, R-F1=6.12; Beam DR=0, CF=0.94, E-F1=55.62, R-F1=9.47\n- Mistral/SciERC: Greedy DR=13.40, CF=1.27, E-F1=27.46, R-F1=3.67; Beam DR=13.79, CF=0.57, E-F1=26.66, R-F1=4.37\n- Mistral/DocRED(50): Greedy DR=28.37, CF=0.34, E-F1=51.60, R-F1=4.19; Beam DR=21.37, CF=0.19, E-F1=51.78, R-F1=5.70\n- \"64 lines of code\" — GrammarMatcher adaptation (line ~11)\n- \"61 lines of code\" — TypeConstraintProcessor adaptation (line ~13)\n- \"~125 lines total\" — beam search adaptation (line ~14)\n- \"k=4\" — beam width (line ~17)\n- \"74%\" — CF reduction Qwen DocRED (8 → 50-doc subset) (line ~61)\n- \"86%\" — CF reduction Llama DocRED (line ~61)\n- \"+3.4pp\" — Llama DocRED R-F1 gain (line ~62)\n- \"55%\" — Mistral SciERC CF relative reduction (line ~66)\n- \"+0.7pp\" — Mistral SciERC R-F1 improvement (line ~66)\n- \"25%\" — Mistral DocRED DR relative reduction (line ~67)\n\n**Beam ablation table (lines 82–86):**\n- k=1: DR=0.93, CF=9.90, E-F1=30.98, R-F1=8.36\n- k=2: DR=0.35, CF=4.12, E-F1=31.54, R-F1=8.75\n- k=4: DR=0, CF=0.53, E-F1=32.00, R-F1=8.56\n- k=8: DR=0, CF=0.08, E-F1=32.18, R-F1=8.39\n- \"2 residual violations\" — at k=8 (line ~91)\n\n**Beam width-latency Pareto (LoRA) table (lines 116–131):**\n- k=1 unc: E-F1=66.88, R-F1=42.95, DR=2.11, CF=0, Lat=2.494s, Rel=1.00×\n- k=1 con: E-F1=66.88, R-F1=42.95, DR=0, CF=0.50, Lat=2.932s, Rel=1.18×\n- k=2 unc: E-F1=67.79, R-F1=44.75, DR=1.54, CF=0, Lat=2.954s, Rel=1.18×\n- k=2 con (Pareto optimal): E-F1=67.71, R-F1=44.60, DR=0, CF=0.11, Lat=3.463s, Rel=1.39×\n- k=4 unc: E-F1=67.49, R-F1=43.72, DR=1.89, CF=0, Lat=3.485s, Rel=1.40×\n- k=4 con: E-F1=67.22, R-F1=43.60, DR=0, CF=0, Lat=4.069s, Rel=1.63×\n- k=8 unc: E-F1=66.40, R-F1=43.17, DR=1.77, CF=0, Lat=4.194s, Rel=1.68×\n- k=8 con: E-F1=66.36, R-F1=43.65, DR=0, CF=0, Lat=5.058s, Rel=2.03×\n\n**LoRA + beam composability:**\n- \"1.18%→0%\" — CF elimination with beam k=4 on SciERC LoRA (line ~137)\n- R-F1=43.60, E-F1=66.88 — Qwen LoRA beam-4 SciERC (line ~137)\n- \"0% across all four metrics\" — zero-violation result (line ~138)\n- \"R-F1=46.18\" — Llama LoRA beam-4 SciERC (line ~138)\n\n**Full DocRED 998-doc zero-shot beam (lines 155–157):**\n- Qwen3-8B: ET=0, RV=0, DR=0, CF=4.94, E-F1=58.19, R-F1=8.72\n- Llama-3.1-8B: ET=0, RV=0, DR=0, CF=1.00, E-F1=57.81, R-F1=8.83\n- \"8.54%→1.00%, 88% reduction\" — Llama CF improvement (line ~143)\n- \"+2.6pp\" — Llama R-F1 gain (line ~143)\n\n**DocRED LoRA beam table (lines 175–183):**\n- Qwen3-8B Greedy: DR=0.01, CF=0.41, E-F1=81.43, R-F1=40.56, PF=8.52\n- Qwen3-8B Beam-4: DR=0, CF=0.01, E-F1=84.00, R-F1=44.46, PF=2.9\n- Llama-3.1-8B Greedy: DR=0.21, CF=0.21, E-F1=83.94, R-F1=43.78, PF=2.51\n- Llama-3.1-8B Beam-4: DR=0, CF=0, E-F1=85.23, R-F1=47.17, PF=1.3\n- \"1.3% to 2.9%\" — LoRA beam-4 parse failure range (line ~162)\n\n**Beam latency table (lines 199–204):**\n- Greedy unconstrained: 2.612 s/doc, 1.00×\n- Greedy constrained (S1): 2.873 s/doc, 1.10×\n- Beam-4 unconstrained: 3.446 s/doc, 1.32×\n- Beam-4 constrained (S1): 4.013 s/doc, 1.54×\n- \"32%\" — beam search latency overhead (line ~210)\n- \"10%→17%\" — constraint overhead increase greedy→beam (line ~210)\n- \"&lt;1 MB\" — per-beam entity registry memory at k=8 (line ~211)\n- \"100% skip rate\" — type-consensus constraint on 551 SciERC/50 DocRED (line ~216)\n- \"0/551\" — SciERC candidates changed by TCR with beam (line ~220)\n\n---\n\n## appendix_reproducibility.tex\n\n**LoRA hyperparameters:**\n- \"r=16\" — rank (line ~5)\n- \"α=32\" — alpha (line ~5)\n- \"dropout 0.05\" — dropout rate (line ~5)\n- \"lr 2×10⁻⁴\" — learning rate (line ~6)\n- \"warmup ratio 0.1\" — warmup (line ~6)\n- \"effective batch size 16\" — batch size (line ~6)\n- \"3 epochs\" — training epochs (line ~6)\n- \"SciERC: 1,762 examples (260 dev), 333 steps\" (line ~7)\n- \"DocRED: 3,053 examples (998 dev), 573 steps\" (line ~7)\n- \"2,048\" — max sequence length SciERC (line ~8)\n- \"4,096\" — max sequence length DocRED (line ~8)\n- \"seed 42\" — random seed (line ~9)\n- \"98 GB VRAM\" — GPU memory (line ~12)\n- \"~11 minutes\" — SciERC fine-tuning time (line ~13)\n- \"~1.5 hours\" — DocRED fine-tuning time (line ~13)\n- \"PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13\" — software versions (line ~14)\n- \"+13.1%\" — ZS S1 overhead on SciERC (line ~18)\n- \"+10.0%\" — FT S1 overhead on SciERC (line ~18)\n- \"seeds 42, 123, 456\" — seeds tested (line ~25)\n\n**Seed variance table (lines 42–45):**\n- Qwen3-8B Unc: E-F1=66.94±0.08, R-F1=43.25±0.43, DR=2.06±0.08\n- Qwen3-8B Con: E-F1=66.94±0.08, R-F1=43.22±0.39, DR=0.00±0.00\n- Llama-3.1-8B Unc: E-F1=67.99±0.16, R-F1=45.38±0.05, DR=1.04±0.05\n- Llama-3.1-8B Con: E-F1=67.99±0.16, R-F1=45.40±0.05, DR=0.03±0.04\n- \"σ(E-F1)≤0.16pp\" (line ~28)\n- \"σ(R-F1)≤0.43pp\" (line ~28)\n- \"σ(DR%)≤0.08pp\" (line ~28)\n- \"−2.06pp (Qwen), −1.01pp (Llama)\" — DR reduction vs. variance (line ~29)\n- \"&gt;12×\" — signal-to-noise ratio (line ~29)\n- \"5,000\" — bootstrap resamples for 200-doc justification (line ~58)\n- \"±3.3 points\" — 95% CI for 200-doc R-F1 (line ~59)\n- \"±0.45pp\" — 200-doc DR margin of error (line ~59)\n- \"15.0%\" — unconstrained DR for ZS power analysis (line ~60)\n- \"Cohen's h=0.80\" — effect size for ZS power (line ~60)\n- \"100% power\" — ZS 200-doc power (line ~60)\n- \"&lt;0.5%\" — FT violation rate for fine-tuned power (line ~60)\n- \"94.9%\" — fraction of 200-doc subsamples correctly identifying DR direction (line ~60)\n\n---\n\n## appendix_power_analysis.tex\n\n**Power analysis table (lines 15–20):**\n- SciERC: n=551, 95% CI=±1.8pp, MDE=1.2pp\n- DocRED: n=998, 95% CI=±0.8pp, MDE=0.5pp\n- DocRED (70B): n=200, 95% CI=±3.3pp, MDE=2.1pp\n- WikiEvents: n=20, 95% CI=±3.0pp, MDE=2.0pp\n- \"≥1,000 bootstrap resamples\" (line ~7)\n- \"80% power, α=0.05\" — test parameters (line ~7)\n- \"ρ=0.9\" — assumed correlation (line ~7)\n- \"8.8–38.3%\" — WikiEvents RoV before constraints (line ~30)\n- \"0%\" — WikiEvents RoV after constraints (line ~30)\n- \"[0%,0%]\" — constrained bootstrap CI (line ~30)\n- \"[2.4%,15.4%]\" and \"[25.4%,46.7%]\" — unconstrained CIs (line ~30)\n- \"power≈1.0\" — power for violation elimination (line ~30)\n- \"n=20\" — WikiEvents test size (line ~29)\n- \"n=551, n=998\" — SciERC/DocRED CI evaluation sizes (line ~31)\n- \"≤1.8pp\" — CI bound (line ~31)\n\n---\n\n## appendix_doc_length.tex\n\n**SciERC doc length table (lines 16–23):**\n- Short (196 docs): Uncon. ET=1, RV=5, DR=57, CF=0, Total=63, E-F1=32.4, R-F1=8.9; Const. ET=0, RV=0, DR=5, CF=5, Total=10, E-F1=32.4, R-F1=8.9\n- Medium (180 docs): Uncon. ET=6, RV=9, DR=104, CF=0, Total=119, E-F1=27.8, R-F1=6.7; Const. ET=0, RV=0, DR=7, CF=15, Total=22, E-F1=27.8, R-F1=6.7\n- Long (175 docs): Uncon. ET=3, RV=10, DR=104, CF=1, Total=118, E-F1=29.9, R-F1=7.0; Const. ET=0, RV=0, DR=4, CF=20, Total=24, E-F1=30.0, R-F1=7.3\n- \"≤19 words\" — short bin boundary (line ~9)\n- \"≤27 words\" — medium bin boundary (line ~9)\n- \"&gt;27 words\" — long bin boundary (line ~9)\n\n**DocRED doc length table (lines 37–45):**\n- Short (336 docs): Uncon. ET=177, RV=1238, DR=1021, CF=9, Total=2445, E-F1=61.1, R-F1=9.3; Const. ET=0, RV=0, DR=495, CF=138, Total=633, E-F1=62.6, R-F1=9.6\n- Medium (332 docs): Uncon. ET=147, RV=1742, DR=1047, CF=5, Total=2941, E-F1=59.3, R-F1=7.9; Const. ET=0, RV=5, DR=544, CF=180, Total=729, E-F1=60.7, R-F1=8.5\n- Long (330 docs): Uncon. ET=176, RV=2209, DR=1162, CF=3, Total=3550, E-F1=53.9, R-F1=5.6; Const. ET=0, RV=0, DR=731, CF=200, Total=931, E-F1=54.8, R-F1=5.8\n- \"≤160 words\" — short bin DocRED (line ~31)\n- \"≤208 words\" — medium bin DocRED (line ~31)\n- \"&gt;208 words\" — long bin DocRED (line ~31)\n\n**Violation reduction table (lines 62–64):**\n- SciERC Short: 63→10, 84.1% reduction\n- SciERC Medium: 119→22, 81.5% reduction\n- SciERC Long: 118→24, 79.7% reduction\n- DocRED Short: 2445→633, 74.1% reduction\n- DocRED Medium: 2941→729, 75.2% reduction\n- DocRED Long: 3550→931, 73.8% reduction\n- \"80–84%\" — SciERC reduction range (line ~69)\n- \"74–75%\" — DocRED reduction range (line ~69)\n- \"+0.9–1.5 E-F1\" — DocRED E-F1 improvement (line ~72)\n- \"+0.2–0.6 R-F1\" — DocRED R-F1 improvement (line ~72)\n\n---\n\n## appendix_prompt_sensitivity.tex\n\n**Prompt sensitivity table (lines 17–41):**\nQwen3-8B:\n- Default Unconstrained: ET=0.40, RV=1.39, DR=15.37, E-F1=31.01, R-F1=8.23\n- Default Constrained: ET=0, RV=0, DR=0.93, ΔDR=94.0%, E-F1=30.98, R-F1=8.36\n- Minimal Unconstrained: ET=0.58, RV=1.16, DR=16.91, E-F1=31.98, R-F1=7.91\n- Minimal Constrained: ET=0, RV=0, DR=0.92, ΔDR=94.6%, E-F1=31.99, R-F1=7.85\n- Detailed Unconstrained: ET=0.22, RV=0.45, DR=11.07, E-F1=33.55, R-F1=10.48\n- Detailed Constrained: ET=0, RV=0, DR=0.64, ΔDR=94.2%, E-F1=33.56, R-F1=10.48\n\nLlama-3.1-70B (AWQ INT4):\n- Default Unconstrained: ET=0, RV=0.61, DR=6.41, E-F1=35.22, R-F1=11.23\n- Default Constrained: ET=0, RV=0, DR=0, ΔDR=100%, E-F1=35.19, R-F1=11.24\n- Minimal Unconstrained: ET=0.27, RV=5.88, DR=0.22, E-F1=37.51, R-F1=13.42\n- Minimal Constrained: ET=0, RV=0, DR=0, ΔDR=100%, E-F1=37.22, R-F1=11.35\n- Detailed Unconstrained: ET=0, RV=0.26, DR=4.57, E-F1=40.42, R-F1=11.12\n- Detailed Constrained: ET=0, RV=0, DR=0, ΔDR=100%, E-F1=40.35, R-F1=11.16\n\n- \"94.0%–94.6%\" — 8B ΔDR range across prompts (line ~45)\n- \"0.3pp\" — standard deviation across prompts (line ~45)\n- \"0.13pp max\" — R-F1 shift (line ~45)\n- \"11.1%–16.9%\" — 8B baseline DR range (line ~49)\n- \"0.22%–6.41%\" — 70B baseline DR range (line ~49)\n- \"0.62%–3.50%\" — CF introduced at 70B (line ~47)\n- \"0.62% and 0.75%\" — LoRA 70B CF under Minimal/Detailed prompts (line ~53)\n\n---\n\n## appendix_case_studies.tex\n\n**Error analysis (lines 148–177):**\n- \"514 FN, 668 FP, 21 CF\" — LoRA S1 SciERC errors (line ~148)\n- \"460 TP\" — true positives (line ~148)\n- \"R-F1=43.77\" — LoRA S1 SciERC R-F1 (line ~148)\n- \"1 of 514 (0.2%)\" — constraint-blocked false negatives (line ~177)\n- \"56%\" — Used-for fraction of all SciERC relations (line ~163)\n- \"DR≤0.21%\" — constraint enforcement leaves type-invalid outputs at this rate (line ~177)\n\n---\n\n## appendix_downstream_analysis.tex\n\n**Lucky violations detail table (lines 13–18):**\n- SciERC/Qwen-LoRA: TP=461, Lucky=4, %TP=0.87%, R drop=0.41pp\n- SciERC/Llama-LoRA: TP=467, Lucky=5, %TP=1.07%, R drop=0.51pp\n- DocRED/Qwen-LoRA: TP=5746, Lucky=1, %TP=0.02%, R drop=0.01pp\n- DocRED/Llama-LoRA: TP=6226, Lucky=1, %TP=0.02%, R drop=0.01pp\n- \"1.07%\" — max lucky violation fraction (5/467) (line ~24)\n- \"0.02%\" — min lucky violation fraction (DocRED) (line ~24)\n- \"0.51pp\" — max recall drop (line ~25)\n- \"164\" — schema-violating predictions eliminated on Qwen DocRED (line ~26)\n- \"1\" — correct predictions removed (line ~26)\n- \"163\" — false positive predictions removed (line ~26)\n\n---\n\n## appendix_scalability.tex\n\n**Scalability table (lines 12–15):**\n- Small (SciERC): 6 types, 7 relations, compile=0.33s, overhead=1.02×\n- Medium (DocRED): 6 types, 96 relations, compile=0.32s, overhead=1.03×\n- Large (synth.): 100 types, 500 relations, compile=0.35s, overhead=1.03×\n- XLarge (synth.): 200 types, 1,000 relations, compile=0.42s, overhead=1.03×\n- \"0.32s to 0.42s\" — compilation range (7→1,000 relations) (line ~22)\n- \"~0.044s\" — XGrammar automaton compilation (line ~22)\n- \"0.4ms to 17ms\" — semantic constraint compilation range (line ~22)\n- \"2–3%\" — constant inference overhead (line ~23)\n- \"~200\" — entity type limit before prefix collisions (line ~24)\n- \"10 documents\" — measurement sample per scale (caption line ~17)\n\n---\n\n## appendix_full_ft.tex\n\n**Full FT table (lines 12–17):**\n- Full FT unconstrained: E-F1=64.78, R-F1=37.89, DR=2.74%, CF=0%\n- Full FT + S1: E-F1=64.78, R-F1=37.89, DR=0%, CF=1.31%\n- LoRA unconstrained: E-F1=67.05, R-F1=43.86, DR=1.95%, CF=0%\n- LoRA + S1: E-F1=67.05, R-F1=43.77, DR=0%, CF=1.18%\n- \"30 triples\" — full FT DR violations (line ~24)\n- \"Part-of: 14.6%, Hyponym-of: 9.6%, Evaluate-for: 8.4%\" — violation distribution by relation (line ~24)\n- \"lr=2×10⁻⁴\" — learning rate (line ~4)\n- \"3 epochs, seed 42\" — training config (line ~4)\n- \"0%→1.31%\" — CF increase (line ~24)\n\n---\n\n## appendix_tcr.tex\n\n**TCR SciERC table (lines 26–33):**\nZero-shot:\n- Qwen: CF pre=9.75%, post=0%, DR pre=0.93%, post=1.21%, ΔE-F1=−1.29pp, Fund.=2.04%\n- Llama: CF pre=6.40%, post=0%, DR pre=0.08%, post=0.30%, ΔE-F1=−1.78pp, Fund.=1.85%\n- Mistral: CF pre=0.67%, post=0%, DR pre=13.36%, post=12.87%, ΔE-F1=+0.05pp, Fund.=0%\nLoRA:\n- Qwen: CF pre=1.19%, post=0%, DR pre=0%, post=0%, ΔE-F1=−0.75pp, Fund.=0%\n- Llama: CF pre=0.46%, post=0%, DR pre=0.09%, post=0.09%, ΔE-F1=−0.18pp, Fund.=0%\n- \"κ̄=0.333\" — SciERC (line ~35)\n- \"≤0.28pp\" — max DR increase from TCR on SciERC (line ~39)\n- \"0–2%\" — fundamental conflict rate SciERC (line ~39)\n\n**TCR DocRED table (lines 56–65):**\nZero-shot:\n- Qwen: CF pre=13.11%, post=0%, DR pre=10.21%, post=11.74%, ΔE-F1=−3.44pp, Fund.=13.52%\n- Llama: CF pre=23.71%, post=0%, DR pre=2.55%, post=11.93%, ΔE-F1=−5.21pp, Fund.=22.78%\n- 70B: CF pre=11.61%, post=0%, DR pre=0%, post=4.20%, ΔE-F1=−5.98pp, Fund.=18.26%\nLoRA:\n- Qwen: CF pre=0.42%, post=0%, DR pre=0.01%, post=0.14%, ΔE-F1=−0.16pp, Fund.=12.16%\n- Llama: CF pre=0.36%, post=0%, DR pre=0.21%, post=0.20%, ΔE-F1=−0.17pp, Fund.=11.59%\n- \"κ̄=0.842\" — DocRED (line ~67)\n- \"+9.38pp\" — max DR regression from Llama TCR (line ~67)\n- \"−5.98pp\" — max E-F1 drop from 70B TCR (line ~67)\n- \"12–23%\" — fundamental conflict rates DocRED (line ~67)\n- \"2.55%→11.93%\" — Llama DR regression (line ~78)\n- \"0%→4.20%\" — 70B DR regression (line ~78)\n- \"0.36–0.42%\" — LoRA baseline CF on DocRED (line ~79)\n- \"1.39×\" — beam search latency (line ~83)\n\n---\n\n## appendix_kappa_case_study.tex\n\n**Kappa case study table (lines 14–28):**\nHigh DR:\n- basin country (DocRED): κ=0.97, DR=74.6%, n=63\n- product produced (DocRED): κ=0.94, DR=67.2%, n=61\n- participant of (DocRED): κ=0.81, DR=58.6%, n=326\n- Compare (SciERC): κ=0.53, DR=42.4%, n=66\n- Feature-of (SciERC): κ=0.28, DR=33.5%, n=486\nHigh κ, zero violations:\n- lyrics by (DocRED): κ=0.94, DR=0.0%, n=9\n- place of birth (DocRED): κ=0.92, DR=0.0%, n=157\n- place of death (DocRED): κ=0.89, DR=0.0%, n=60\n- subsidiary (DocRED): κ=0.86, DR=0.0%, n=5\n- father (DocRED): κ=0.81, DR=0.0%, n=69\n- \"&gt;50%\" — DR for confusable-type relations (line ~36)\n\n---\n\n## appendix_high_kappa_analysis.tex\n\n**Schema ambiguity table (lines 26–47):**\nSciERC:\n- Hyponym-of: α=0.83, |P_r|=21, Gold=298, Gold%=9.3%\n- Part-of: α=0.83, |P_r|=21, Gold=179, Gold%=5.6%\n- Compare: α=0.82, |P_r|=17, Gold=166, Gold%=5.2%\n- Conjunction: α=0.77, |P_r|=25, Gold=400, Gold%=12.4%\n- Feature-of: α=0.76, |P_r|=26, Gold=173, Gold%=5.4%\n- Evaluate-for: α=0.71, |P_r|=23, Gold=313, Gold%=9.7%\n- Used-for: α=0.67, |P_r|=35, Gold=1,690, Gold%=52.5%\nDocRED (high α, 12 of 96 relations):\n- sister city (P190): α=0.42, |P_r|=1, Gold=4, Gold%=0.01%\n- basin country (P205): α=0.42, |P_r|=1, Gold=85, Gold%=0.22%\n- mouth of watercourse (P403): α=0.42, |P_r|=1, Gold=95, Gold%=0.25%\n- separated from (P807): α=0.41, |P_r|=2, Gold=2, Gold%=0.01%\n- replaces (P1365): α=0.39, |P_r|=4, Gold=18, Gold%=0.05%\n- capital of (P1376): α=0.37, |P_r|=3, Gold=76, Gold%=0.20%\n- place of birth (P19): α=0.37, |P_r|=3, Gold=511, Gold%=1.34%\n- operator (P137): α=0.36, |P_r|=7, Gold=95, Gold%=0.25%\n- military branch (P241): α=0.36, |P_r|=5, Gold=108, Gold%=0.28%\n- production company (P272): α=0.36, |P_r|=5, Gold=82, Gold%=0.21%\n- place of death (P20): α=0.36, |P_r|=4, Gold=203, Gold%=0.53%\n- location (P276): α=0.36, |P_r|=5, Gold=172, Gold%=0.45%\n- \"3.8%\" — fraction of gold triples in high-α DocRED relations (line ~19)\n- \"36\" — type pair slots (6²) (line ~75)\n- \"7 relations\" — SciERC total (line ~75)\n- \"α≥0.36\" — threshold (line ~18)\n- \"12 relations\" — DocRED high-α count (line ~34)\n- \"(Method, Method)\" — valid for all 7 SciERC relations; α=1.0 (line ~76)\n\n**DR by ambiguity table (lines 62–70):**\nLlama-3.1-8B:\n- High-α (12 rels): Unconstrained DR=43.8%, n=861; S1 DR=3.2%, n=1,043\n- Low-α (84 rels): Unconstrained DR=29.9%, n=12,809; S1 DR=2.5%, n=15,325\nQwen3-8B:\n- High-α (12 rels): Unconstrained DR=31.9%, n=718; S1 DR=20.0%, n=1,119\n- Low-α (84 rels): Unconstrained DR=21.2%, n=10,898; S1 DR=9.5%, n=16,217\n- \"2×\" — gap Qwen retains high vs. low α under S1 (line ~81)\n- \"2.55%→2.51% for Llama\" — exclusion analysis result (line ~82)\n- \"10.21%→9.53% for Qwen\" — exclusion analysis result (line ~82)\n- \"15.4%→0.9% (Qwen), 13.3%→0.08% (Llama)\" — SciERC DR reduction (line ~83)\n\n---\n\n## appendix_order_invariance.tex\n- \"551\" — SciERC documents (line ~6)\n- No other numerical data; purely qualitative result (byte-identical outputs)\n\n---\n\n## appendix_pumping_lemma.tex\n- \"6 entity types, 20+ entities\" → \"exceeds 10¹⁵ states\" — DFA state count (line ~64)\n- \"O(|T|^|E|)\" — DFA state complexity (line ~64)\n\n---\n\n## appendix_wikievents_pilot.tex\n\n**WikiEvents table (lines 32–44):**\nQwen3-8B:\n- Unconstrained: EV=24.0%, RoV=74.9%, AC=0.3%, CF=0, Trig.=11.8, Ent.=0\n- Grammar: EV=0%, RoV=76.1%, AC=8.2%, CF=---\n- S1: EV=0%, RoV=0%, AC=2.1%, CF=21.1%, Trig.=13.4, Ent.=14.1\nLlama-3.1-8B:\n- Unconstrained: EV=10.5%, RoV=88.8%, AC=0.1%, CF=0, Trig.=5.7, Ent.=0\n- Grammar: EV=0%, RoV=77.0%, AC=8.8%, CF=---\n- S1: EV=0%, RoV=0%, AC=3.8%, CF=17.2%, Trig.=7.5, Ent.=17.6\nMistral-7B:\n- Unconstrained: EV=37.3%, RoV=63.9%, AC=0%, CF=0, Trig.=2.4, Ent.=0\n- Grammar: EV=0%, RoV=64.0%, AC=13.8%, CF=---\n- S1: EV=0%, RoV=0%, AC=1.3%, CF=14.9%, Trig.=3.9, Ent.=11.7\n- \"n=246 documents\" — WikiEvents ZS evaluation (caption line ~47)\n- \"EV+RoV&gt;85%\" — combined vocabulary violations (line ~55)\n- \"entity F1=0\" — unconstrained baseline (line ~55)\n- \"8–14%\" — grammar-only AC rate range (line ~57)\n- \"64–77%\" — grammar-only residual RoV range (line ~57)\n- \"1.3–3.8%\" — residual AC range under S1 (line ~58)\n- \"15–21%\" — CF range under S1 (line ~58)\n- \"0%→12–18%\" — entity F1 gain (line ~59)\n- \"+1.5–1.8pp\" — trigger F1 gain (line ~59)\n- \"n=20\" — WikiEvents FT test split (line ~62)\n- \"194/20/20\" — train/dev/test split (line ~62)\n- \"Qwen 38.31%→0%\" — LoRA RoV elimination (line ~63)\n- \"Llama 8.8%→0%\" — LoRA RoV elimination (line ~63)\n- \"≤0.8%\" — LoRA AC rate (line ~63)\n- \"±1.1pp\" — argument F1 range (line ~63)\n- \"−5.4/−0.6pp\" — trigger F1 shifts (line ~63)\n- \"0.77–1.18%\" — CF under FT (line ~64)\n- \"Arg-F1 std/mean&gt;0.5\" — high per-document variance (line ~64)\n- \"MDE≈±5.0pp\" — WikiEvents FT MDE note (caption line ~50)\n\n---\n\n## appendix_zs_crossmodel.tex\n\n**Cross-model table (lines 23–42):**\nSciERC:\n- Qwen (U): DR=15.37, RV=1.39, ET=0.40, CF=0.08, R-F1=8.23\n- Qwen (S1): DR=0.93, RV=0, ET=0, CF=9.90, R-F1=8.36\n- Llama (U): DR=13.34, RV=0.55, ET=0, CF=0.24, R-F1=2.68\n- Llama (S1): DR=0.08, RV=0, ET=0, CF=6.56, R-F1=2.54\n- Mistral (U): DR=56.94, RV=0, ET=1.50, CF=56.87†, R-F1=3.66\n- Mistral (S1): DR=13.40, RV=0, ET=0, CF=1.27, R-F1=3.67\nDocRED:\n- Qwen (U): DR=18.46, RV=29.66, ET=2.48, CF=0.10, R-F1=7.74\n- Qwen (S1): DR=10.21, RV=0.03, ET=0, CF=2.57, R-F1=8.23\n- Llama (U): DR=26.07, RV=16.03, ET=0.13, CF=0.17, R-F1=5.98\n- Llama (S1): DR=2.55, RV=0, ET=0, CF=12.02, R-F1=6.27\n- Mistral (U): DR=57.42, RV=42.35, ET=7.58, CF=24.78, R-F1=4.34\n- Mistral (S1): DR=33.20, RV=0, ET=0, CF=0.19, R-F1=5.52\n- \"Llama DocRED 9.1%\" — parse failure rate (line ~45)\n- \"≤1.1%\" — other parse failure rates (line ~45)\n- \"76–99% on SciERC\" — DR reduction range (line ~53)\n- \"42–90% on DocRED\" — DR reduction range (line ~53)\n- \"5/6 settings\" — R-F1 improvements (line ~53)\n- \"12.02%\" — max CF introduced (line ~54)\n- \"56.87%→1.27%\" — Mistral CF reduction (line ~54)\n- \"15–74%\" — post-hoc rejection rates (line ~55)\n- \"14×\" — DocRED scale relative to SciERC (line ~59)\n\n---\n\n## appendix_quantization.tex\n\n**Quantization table (lines 20–29):**\nSciERC (551 docs):\n- Qwen3-8B FP16: DR=0, R-F1=43.77, E-F1=67.05\n- Qwen3-8B INT4: DR=0, R-F1=41.71, E-F1=67.05, Δ R-F1=−2.06\n- Llama-3.1-8B FP16: DR=0.09, R-F1=45.47, E-F1=67.76\n- Llama-3.1-8B INT4: DR=0, R-F1=43.98, E-F1=67.54, ΔDR=−0.09, ΔR-F1=−1.49, ΔE-F1=−0.22\nDocRED (200 docs):\n- Qwen3-8B FP16†: DR=0, R-F1=40.79†, E-F1=81.87†, PF=8.5%†\n- Qwen3-8B INT4: DR=0, R-F1=40.07, E-F1=74.84, ΔR-F1=−0.72, ΔE-F1=−7.03‡, PF=18.5%\n- Llama-3.1-8B FP16: DR=0, R-F1=47.35, E-F1=85.43, PF=2.0%\n- Llama-3.1-8B INT4: DR=0, R-F1=48.04, E-F1=84.18, ΔR-F1=+0.69, ΔE-F1=−1.25, PF=2.5%\n- \"−2.06 to +0.69pp\" — R-F1 change range (line ~39)\n- \"18.5% vs. 8.5%\" — Qwen INT4 vs FP16 parse failures (line ~40)\n- \"−7.03pp\" — Qwen DocRED E-F1 gap (line ~40)\n- \"†Qwen DocRED FP16 evaluated on 998 docs\" (note line ~33)\n\n---\n\n## appendix_gollie_comparison.tex\nNo numerical data (qualitative comparison only)\n\n---\n\n## appendix_ai_assistants.tex\nNo numerical data\n\n---\n\n**Summary of key numbers by category for cross-reference audit:**\n\nKey numbers appearing in multiple places (cross-reference candidates):\n- \"551\" — SciERC document count (reproducibility, sampling, beam, causal tracing, fallback coverage, CF tables, error analysis, doc length, prompt sensitivity, order invariance, seed variance, scalability, quantization)\n- \"998\" — DocRED document count (reproducibility, power analysis, DocRED ablation, beam, TCR)\n- \"15.37%\" — SciERC baseline DR (related work, discussion, prompt sensitivity, cross-model table)\n- \"0.93%\" — SciERC Qwen S1 DR (sampling, beam, causal tracing, CF-DR tradeoff, bootstrap table)\n- \"10.21%\" — DocRED Qwen S1 DR (sampling, Llama per-relation, TCR, DocRED ablation, cross-model)\n- \"94%\" — SciERC DR reduction (related work, discussion, prompt sensitivity)\n- \"29.66%\" — DocRED baseline RV (discussion, DocRED ablation, cross-model)\n- \"18.46%\" — DocRED baseline DR (discussion, DocRED ablation, cross-model)\n- \"8.36\" — SciERC Qwen ZS R-F1 (sampling, beam ablation, beam pareto k=1, vLLM table, prompt sensitivity)\n- \"8.23\" — DocRED Qwen ZS R-F1 (sampling, DocRED ablation, cross-model, vLLM)\n- \"43.77\" — SciERC Qwen LoRA+S1 R-F1 (FT ablation, full FT, quantization, error analysis, beam composability)\n- \"67.05\" — SciERC Qwen LoRA E-F1 (FT ablation, full FT, quantization, beam composability)\n- \"κ̄=0.333\" (SciERC) and \"κ̄=0.842\" (DocRED) — appear in dual-factor, TCR, Llama per-relation\n- \"+0.49pp p&lt;0.001\" — DocRED R-F1 gain (discussion, DocRED ablation, cross-model)\n- \"2.87 BPE tokens\" — OtherScientificTerm tokenization (discussion, twice)\n- \"seed=42\" — reproducibility, bootstrap, full FT, beam pareto\n- \"10,000 bootstrap iterations\" — discussion (bootstrap CI), reproducibility\n\n**Potential inconsistency flagged:**\n- In `appendix_discussion.tex` line ~39, text says \"Qwen achieves CF=2.57% on DocRED vs. Llama's 12.02%\", and also \"Qwen3-8B shows f_gf=0.08% ... yielding 99.9% coverage\" and \"residual DR (0.93% vs. Llama's 0.08%)\" — note this implies Qwen DR=0.93% and Llama DR=0.08% on SciERC, which is consistent with the main tables.\n- In `appendix_discussion.tex` line ~39: \"consistent with its lower residual DR (0.93% vs. Llama's 0.08%)\" — but this is Qwen's DR vs Llama's DR on SciERC (both ZS S1), consistent with causal tracing table.\n- `appendix_posthoc_extended` table: Qwen DocRED FT shows R-F1_cd=40.79, but `appendix_ft_ablation` table shows Qwen DocRED S1 R-F1=40.56 — **potential inconsistency** between these two tables for Qwen DocRED FT constrained R-F1 (40.79 vs 40.56).\n- `appendix_beam_search.tex`: DocRED LoRA Qwen Greedy shows R-F1=40.56, PF=8.52 — matches FT ablation table.\n- `appendix_quantization.tex`: Qwen DocRED FP16 R-F1=40.79† with note \"evaluated on 998 docs\" — explains discrepancy (subset vs. full set).&lt;/result>\n&lt;usage>&lt;total_tokens>100700&lt;/total_tokens>&lt;tool_uses>25&lt;/tool_uses>&lt;duration_ms>376042&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---


### Runtime record

_source line 1877_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[飞书用户 用户]: 📊 论文自检任务（重大）：全文数据真实性与可追溯性彻底审计  这是一次彻底的大检查，必须认真对待。AI 写论文最致命的两个问题：编数字（hallucinate）和抄数字（数字之间不一致或来源不明）。这次的目标是把每一个出现在论文里的数字都\"对账\"清楚。  ⚠️ 凡是查不到出处的数字，要么找到出处，要么删掉。不允许凭印象、凭\"差不多\"、凭老版本残留的数字留在论文里。  ---…",
  "leafUuid": "41ab9fbd-6d5c-4493-82ff-8f64699c8b22",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25"
}
```

---


### Runtime record

_source line 1878_

```json
{
  "type": "ai-title",
  "aiTitle": "Paper formatting and figure optimization for EMNLP",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25"
}
```

---


### Tool result

_source line 1879 · 2026-05-25T19:50:37.615Z_

<details><summary>↩ Tool result · `toolu_0198n4mwoh1YFCRf4QdjKDD5`</summary>

```text
I now have all the data needed for a complete audit. Let me compile the findings:

---

## Data Integrity Audit Report

### Figure 2 — gen_fig2_per_relation_dr.py

**Hardcoded values:**

| Relation | Unconstrained | Grammar-only | Semantic-only | Full S1 |
|---|---|---|---|---|
| Compare | 42.42 | 40.85 | 29.23 | 2.82 |
| Feature-of | 33.54 | 31.98 | 26.28 | 1.21 |
| Part-of | 25.00 | 23.38 | 11.27 | 0.00 |
| Evaluate-for | 24.06 | 23.13 | 23.13 | 5.76 |
| Hyponym-of | 14.52 | 14.40 | 7.09 | 0.00 |
| Used-for | 0.76 | 0.25 | 0.77 | 0.00 |
| Conjunction | 0.00 | 0.00 | 0.00 | 0.00 |

**Registry cross-reference:**

The `unconstrained` column maps to `mvp_phase0_violation_rate` / `phase2_scierc_unconstrained`. The registry has per_relation data only for the unconstrained condition:
- Compare: 28/66 = **42.42%** ✅ matches exactly
- Feature-of: 163/486 = **33.54%** ✅ matches exactly
- Part-of: 18/72 = **25.00%** ✅ matches exactly
- Evaluate-for: 32/133 = **24.06%** ✅ matches exactly
- Hyponym-of: 18/124 = **14.52%** ✅ matches exactly
- Used-for: 6/787 = **0.76%** ✅ matches exactly
- Conjunction: 0/32 = **0.00%** ✅ matches exactly

**For Grammar-only, Semantic-only, Full S1 columns:** The registry does NOT contain per-relation breakdown for these conditions. `phase2_scierc_grammar_only` metrics only record the aggregate `domain_range_violation_rate: 0.1484`. There are no `per_relation` sub-keys for grammar_only, semantic_only, or full_s1. **The per-relation values for these three columns (40.85, 31.98, etc.) cannot be verified against the registry — their source is unknown.**

**Verdict: Unconstrained column verified ✅. Grammar-only / Semantic-only / Full S1 per-relation columns have no registry provenance — UNVERIFIABLE ⚠️**

---

### Figure 3 — gen_fig3_scale_dependency.py

**Hardcoded values:** `dr_reduction = [24, 84]` for 8B / 70B models.

**Registry cross-reference:**
- **24% (8B):** Claimed to come from `phase2_scierc_semantic_only`: (15.37 − 11.65) / 15.37 = 3.72 / 15.37 = **24.2%** ✅ matches (rounds to 24%)
- **84% (70B):** Script labels this as "Llama-70B". The registry contains no 70B experiments anywhere. The cross-model experiments are all 8B class: Qwen3-8B, Llama-3.1-8B-Instruct, Mistral-7B. There is no `llama_70b_*` or any 70B model experiment in the registry.

**Verdict: 24% verified ✅. 84% / "70B" has NO registry entry — FABRICATED or from an external source not in the registry ❌**

---

### Figure 4 — gen_fig4_composition.py

**Hardcoded values:** `dr_reduction = [0, 3, 24, 94]`

**Registry cross-reference** (all from SciERC, Qwen3-8B, phase2 experiments):
- **0% (Unconstrained):** Correct by definition (baseline = 0 reduction) ✅
- **3% (Grammar-only):** Registry `phase2_scierc_grammar_only`: DR = 0.1484. Reduction = (0.1537 − 0.1484) / 0.1537 = 0.0053 / 0.1537 = **3.4%** ≈ rounds to 3% ✅
- **24% (Semantic-only):** Registry `phase2_scierc_semantic_only`: DR = 0.1165. Reduction = (0.1537 − 0.1165) / 0.1537 = **24.2%** ✅
- **94% (Full S1):** Registry `phase2_scierc_full_s1`: DR = 0.0093. Reduction = (0.1537 − 0.0093) / 0.1537 = **93.9%** ≈ rounds to 94% ✅

**Note:** The additive prediction label in the script says "3 + 24 = 27%" and then labels the gap as "3.5×" (94/27 ≈ 3.48). This is internally consistent.

**Verdict: All four values verified ✅**

---

### Figure 5 — gen_fig5_crossmodel_heatmap.py

**Hardcoded values (3×2 matrix, DR reduction %):**

| Model | SciERC | DocRED |
|---|---|---|
| Qwen3-8B | 94 | 45 |
| Llama-3.1-8B | 99 | 90 |
| Mistral-7B | 76 | 42 |

**Registry cross-reference:**

**Qwen SciERC (94%):** `phase2_scierc_full_s1` DR = 0.0093, baseline 0.1537 → (0.1537−0.0093)/0.1537 = **93.9%** ≅ 94% ✅

**Llama SciERC (99%):** `llama_scierc_full_s1` DR = 0.0008. Baseline from `llama_scierc_unconstrained` DR = 0.1334. Reduction = (0.1334−0.0008)/0.1334 = **99.4%** ≅ 99% ✅

**Mistral SciERC (76%):** `w6_mistral_scierc_unconstrained` DR = 56.94%, `w6_mistral_scierc_constrained` DR = 13.4%. Reduction = (56.94−13.4)/56.94 = **76.5%** ≅ 76% ✅

**Qwen DocRED (45%):** `phase2_docred_unconstrained` DR = 0.1846, `phase2_docred_full_s1` DR = 0.1021. Reduction = (0.1846−0.1021)/0.1846 = **44.7%** ≅ 45% ✅

**Llama DocRED (90%):** `llama_docred_unconstrained` DR = 26.07%, `llama_docred_full_s1` DR = 2.55%. Reduction = (26.07−2.55)/26.07 = **90.2%** ✅

**Mistral DocRED (42%):** `w6_mistral_docred_unconstrained` DR = 57.42%, `w6_mistral_docred_constrained` DR = 33.2%. Reduction = (57.42−33.2)/57.42 = **42.2%** ≅ 42% ✅

**Verdict: All 6 heatmap cells verified ✅**

---

### Figure 6 — gen_fig6_violation_composition.py

**Hardcoded values:**
- `dr = [15.37, 14.84, 11.65, 0.93]`
- `cf = [0.08, 0.08, 2.71, 9.90]`

**Registry cross-reference** (all SciERC Qwen3-8B, phase2):

**DR values:**
- Unconstrained (15.37): `phase2_scierc_unconstrained` DR = 0.1537 = **15.37%** ✅
- Grammar-only (14.84): `phase2_scierc_grammar_only` DR = 0.1484 = **14.84%** ✅
- Semantic-only (11.65): `phase2_scierc_semantic_only` DR = 0.1165 = **11.65%** ✅
- Full S1 (0.93): `phase2_scierc_full_s1` DR = 0.0093 = **0.93%** ✅

**CF values:**
- Unconstrained (0.08): `phase2_scierc_unconstrained` CF = 0.0008 = **0.08%** ✅
- Grammar-only (0.08): `phase2_scierc_grammar_only` CF = 0.0008 = **0.08%** ✅
- Semantic-only (2.71): `phase2_scierc_semantic_only` CF = 0.0271 = **2.71%** ✅
- Full S1 (9.90): `phase2_scierc_full_s1` CF = 0.099 = **9.90%** ✅

**Verdict: All 8 values verified ✅**

---

### Beam Pareto Figure — plot_pareto_dual_v2.py

**Hardcoded SciERC Qwen data verified against `d066_beam_sweep` registry metrics:**

| k | unc rf1 | con rf1 | unc dr | con dr | unc cf | con cf |
|---|---|---|---|---|---|---|
| 1 | 42.95 | 42.95 | 2.11 | 0 | 0 | 0.50 |
| 2 | 44.75 | 44.60 | 1.54 | 0 | 0 | 0.11 |
| 4 | 43.72 | 43.60 | 1.89 | 0 | 0 | 0 |
| 8 | 43.17 | 43.65 | 1.77 | 0 | 0 | 0 |

Registry `d066_beam_sweep` metrics section `scierc_qwen3_8b`: k2_unc R_F1=44.75 ✅, k2_con R_F1=44.60 ✅, k4_unc R_F1=43.72 ✅, k8_con R_F1=43.65 ✅ — all match exactly.

**Hardcoded SciERC Llama data:**
- k1 con: rf1=45.47, dr=0.09, cf=0.46 — **registry has no k1 Llama SciERC beam sweep data**; `d066_sweep_llama_scierc_beam1_unc` was INVALIDATED (used dev set). Source unclear.
- k2 con: rf1=46.12, dr=0, cf=0.17 — matches `d066_sweep_llama_scierc_beam2_s1_551`: R-F1=46.12 ✅, DR=0 ✅, CF=0.17 ✅
- k4 con: rf1=46.18, dr=0, cf=0 — matches `d066_sweep_llama_scierc_beam4_s1_551`: R-F1=46.18 ✅
- k8 con: rf1=44.95, dr=0, cf=0 — matches `d066_sweep_llama_scierc_beam8_s1_551`: R-F1=44.95 ✅

**Hardcoded DocRED Llama data:**
- k1 unc: rf1=47.28 — `d066_sweep_llama_docred_beam1_unc` has no F1 metrics recorded (only total/success/fail counts). **Unverifiable** ⚠️
- k1 con: rf1=47.35 — `d066_sweep_llama_docred_beam1_s1`: R-F1=47.35 ✅, DR=0 ✅, CF=0.19 ✅
- k2 unc: rf1=51.31, dr=0.11, cf=0.05, rv=0.07 — `d066_sweep_16980_gpu1` has no F1 metrics. **Unverifiable** ⚠️
- k2 con: rf1=51.17 — `d066_sweep_llama_beam2_s1`: R-F1=51.17 ✅, DR=0 ✅, CF=0 ✅
- k4 unc: rf1=52.65, dr=0.04 — `d066_sweep_llama_docred_beam4_unc`: R-F1=52.65 ✅, DR=0.04 ✅
- k4 con: rf1=51.89 — `d066_sweep_llama_docred_beam4_s1`: R-F1=51.89 ✅
- k8 unc: rf1=51.97, dr=0, cf=0.05, rv=0.07 — `d066_sweep_llama_beam8_unc`: R-F1=51.97 ✅, DR=0 ✅, CF=0.05 ✅, RV=0.07 ✅
- k8 con: rf1=51.74 — `d066_sweep_llama_beam8_s1`: R-F1=51.74 ✅

**Verdict: SciERC Qwen fully verified ✅. SciERC Llama k1 unverifiable (invalidated experiment) ⚠️. DocRED k1 unc and k2 unc rf1/violation values unverifiable (registry entries lack F1 metrics) ⚠️. All other DocRED points verified ✅.**

---

### kappa_dr_data.json

The file contains per-relation kappa and DR% for SciERC and DocRED under the constrained (full_s1) condition based on a 36-annotator sample. **This file does not correspond to any registry experiment** — it appears to be an annotation study / ontology analysis (noting `n_valid`, `total_possible: 36` consistently, suggesting 36 annotators or sample pairs). No registry entry for a kappa study exists. The DR% values in this file (e.g., SciERC Compare=35.0%, Feature-of=8.29%) differ substantially from the full-test-set constrained DR values in the registry (full_s1 Compare≈2.82%, Feature-of≈1.21%), suggesting this represents a *different analysis* (possibly constraint strictness analysis, not model output). **Provenance is unverifiable against the experiment registry** ⚠️.

---

## Summary of Issues

| Figure | Status | Issues |
|---|---|---|
| Fig2 unconstrained column | ✅ Verified | Exact match to registry per_relation |
| Fig2 grammar/semantic/full_s1 columns | ❌ Unverifiable | No per-relation breakdown in registry for these conditions |
| Fig3 8B (24%) | ✅ Verified | Derived from phase2_scierc_semantic_only |
| Fig3 70B (84%) | ❌ No registry entry | Zero 70B experiments exist anywhere in registry |
| Fig4 all values | ✅ Verified | All 4 DR reduction values match exactly |
| Fig5 all 6 cells | ✅ Verified | All match computed from respective registry experiments |
| Fig6 all 8 values | ✅ Verified | Exact match to phase2 SciERC metrics |
| Pareto (SciERC Qwen) | ✅ Verified | Exact match to d066_beam_sweep |
| Pareto (SciERC Llama k1) | ⚠️ Unverifiable | Source experiment invalidated |
| Pareto (DocRED k1 unc, k2 unc) | ⚠️ Unverifiable | Registry entries missing F1 metrics |
| kappa_dr_data.json | ⚠️ Unverifiable | No corresponding registry experiment |

**Critical blocker:** Fig3's 84%/70B data point has no registry backing. There are no 70B model experiments in the registry at all. This value is either from an external source not tracked in the registry, or fabricated.

**Medium priority:** Fig2's grammar/semantic/full_s1 per-relation bars need sourcing — the registry stores only aggregate DR rates for these conditions, not per-relation breakdowns.

agentId: a3cb85d65eaec24bb (use SendMessage with to: 'a3cb85d65eaec24bb' to continue this agent)
&lt;usage>total_tokens: 137507
tool_uses: 37
duration_ms: 182965&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0a14f26-7c3a-49e8-9278-d9aab224d3f9",
  "isSidechain": false,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "type": "user",
  "uuid": "1e2cf802-b072-4d19-aeea-81a3ce33793d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "This is a data integrity audit. I need you to verify that hardcoded data in figure generation scripts matches experiment registry entries.\n\nRegistry: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/registry.yaml\n\nFigure scripts are at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/figures/\n\nRead each of these scripts and extract the hardcoded data values, then cross-reference against the registry:\n\n1. **gen_fig2_per_relation_dr.py** — Per-relation DR rates for SciERC. Verify against registry entries for per-relation violation data: exp_ids like mvp_phase0_violation_rate, phase2_scierc_unconstrained, etc. Look for per_relation_violations or similar metrics.\n\n2. **gen_fig3_scale_dependency.py** — Should have dr_reduction = [24, 84] for 8B/70B. The 24% comes from phase2_scierc_semantic_only: (15.37-11.65)/15.37. The 84% needs 70B semantic-only experiment.\n\n3. **gen_fig4_composition.py** — dr_reduction = [0, 3, 24, 94]. These are from Table 1's ΔDR column.\n\n4. **gen_fig5_crossmodel_heatmap.py** — 3×2 matrix of DR reduction. Need to find cross-model experiments for Qwen/Llama/Mistral × SciERC/DocRED.\n\n5. **gen_fig6_violation_composition.py** — dr = [15.37, 14.84, 11.65, 0.93], cf = [0.08, 0.08, 2.71, 9.90]. These should match Table 1.\n\n6. **plot_pareto_dual_v2.py** (or similar beam Pareto script) — Beam sweep data points.\n\nAlso check if there's a kappa_dr_data.json file with per-relation data and verify it against registry.\n\nFor each figure, report: (a) what hardcoded values exist, (b) where in registry they should come from, (c) whether they match.",
    "agentId": "a3cb85d65eaec24bb",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the data needed for a complete audit. Let me compile the findings:\n\n---\n\n## Data Integrity Audit Report\n\n### Figure 2 — gen_fig2_per_relation_dr.py\n\n**Hardcoded values:**\n\n| Relation | Unconstrained | Grammar-only | Semantic-only | Full S1 |\n|---|---|---|---|---|\n| Compare | 42.42 | 40.85 | 29.23 | 2.82 |\n| Feature-of | 33.54 | 31.98 | 26.28 | 1.21 |\n| Part-of | 25.00 | 23.38 | 11.27 | 0.00 |\n| Evaluate-for | 24.06 | 23.13 | 23.13 | 5.76 |\n| Hyponym-of | 14.52 | 14.40 | 7.09 | 0.00 |\n| Used-for | 0.76 | 0.25 | 0.77 | 0.00 |\n| Conjunction | 0.00 | 0.00 | 0.00 | 0.00 |\n\n**Registry cross-reference:**\n\nThe `unconstrained` column maps to `mvp_phase0_violation_rate` / `phase2_scierc_unconstrained`. The registry has per_relation data only for the unconstrained condition:\n- Compare: 28/66 = **42.42%** ✅ matches exactly\n- Feature-of: 163/486 = **33.54%** ✅ matches exactly\n- Part-of: 18/72 = **25.00%** ✅ matches exactly\n- Evaluate-for: 32/133 = **24.06%** ✅ matches exactly\n- Hyponym-of: 18/124 = **14.52%** ✅ matches exactly\n- Used-for: 6/787 = **0.76%** ✅ matches exactly\n- Conjunction: 0/32 = **0.00%** ✅ matches exactly\n\n**For Grammar-only, Semantic-only, Full S1 columns:** The registry does NOT contain per-relation breakdown for these conditions. `phase2_scierc_grammar_only` metrics only record the aggregate `domain_range_violation_rate: 0.1484`. There are no `per_relation` sub-keys for grammar_only, semantic_only, or full_s1. **The per-relation values for these three columns (40.85, 31.98, etc.) cannot be verified against the registry — their source is unknown.**\n\n**Verdict: Unconstrained column verified ✅. Grammar-only / Semantic-only / Full S1 per-relation columns have no registry provenance — UNVERIFIABLE ⚠️**\n\n---\n\n### Figure 3 — gen_fig3_scale_dependency.py\n\n**Hardcoded values:** `dr_reduction = [24, 84]` for 8B / 70B models.\n\n**Registry cross-reference:**\n- **24% (8B):** Claimed to come from `phase2_scierc_semantic_only`: (15.37 − 11.65) / 15.37 = 3.72 / 15.37 = **24.2%** ✅ matches (rounds to 24%)\n- **84% (70B):** Script labels this as \"Llama-70B\". The registry contains no 70B experiments anywhere. The cross-model experiments are all 8B class: Qwen3-8B, Llama-3.1-8B-Instruct, Mistral-7B. There is no `llama_70b_*` or any 70B model experiment in the registry.\n\n**Verdict: 24% verified ✅. 84% / \"70B\" has NO registry entry — FABRICATED or from an external source not in the registry ❌**\n\n---\n\n### Figure 4 — gen_fig4_composition.py\n\n**Hardcoded values:** `dr_reduction = [0, 3, 24, 94]`\n\n**Registry cross-reference** (all from SciERC, Qwen3-8B, phase2 experiments):\n- **0% (Unconstrained):** Correct by definition (baseline = 0 reduction) ✅\n- **3% (Grammar-only):** Registry `phase2_scierc_grammar_only`: DR = 0.1484. Reduction = (0.1537 − 0.1484) / 0.1537 = 0.0053 / 0.1537 = **3.4%** ≈ rounds to 3% ✅\n- **24% (Semantic-only):** Registry `phase2_scierc_semantic_only`: DR = 0.1165. Reduction = (0.1537 − 0.1165) / 0.1537 = **24.2%** ✅\n- **94% (Full S1):** Registry `phase2_scierc_full_s1`: DR = 0.0093. Reduction = (0.1537 − 0.0093) / 0.1537 = **93.9%** ≈ rounds to 94% ✅\n\n**Note:** The additive prediction label in the script says \"3 + 24 = 27%\" and then labels the gap as \"3.5×\" (94/27 ≈ 3.48). This is internally consistent.\n\n**Verdict: All four values verified ✅**\n\n---\n\n### Figure 5 — gen_fig5_crossmodel_heatmap.py\n\n**Hardcoded values (3×2 matrix, DR reduction %):**\n\n| Model | SciERC | DocRED |\n|---|---|---|\n| Qwen3-8B | 94 | 45 |\n| Llama-3.1-8B | 99 | 90 |\n| Mistral-7B | 76 | 42 |\n\n**Registry cross-reference:**\n\n**Qwen SciERC (94%):** `phase2_scierc_full_s1` DR = 0.0093, baseline 0.1537 → (0.1537−0.0093)/0.1537 = **93.9%** ≅ 94% ✅\n\n**Llama SciERC (99%):** `llama_scierc_full_s1` DR = 0.0008. Baseline from `llama_scierc_unconstrained` DR = 0.1334. Reduction = (0.1334−0.0008)/0.1334 = **99.4%** ≅ 99% ✅\n\n**Mistral SciERC (76%):** `w6_mistral_scierc_unconstrained` DR = 56.94%, `w6_mistral_scierc_constrained` DR = 13.4%. Reduction = (56.94−13.4)/56.94 = **76.5%** ≅ 76% ✅\n\n**Qwen DocRED (45%):** `phase2_docred_unconstrained` DR = 0.1846, `phase2_docred_full_s1` DR = 0.1021. Reduction = (0.1846−0.1021)/0.1846 = **44.7%** ≅ 45% ✅\n\n**Llama DocRED (90%):** `llama_docred_unconstrained` DR = 26.07%, `llama_docred_full_s1` DR = 2.55%. Reduction = (26.07−2.55)/26.07 = **90.2%** ✅\n\n**Mistral DocRED (42%):** `w6_mistral_docred_unconstrained` DR = 57.42%, `w6_mistral_docred_constrained` DR = 33.2%. Reduction = (57.42−33.2)/57.42 = **42.2%** ≅ 42% ✅\n\n**Verdict: All 6 heatmap cells verified ✅**\n\n---\n\n### Figure 6 — gen_fig6_violation_composition.py\n\n**Hardcoded values:**\n- `dr = [15.37, 14.84, 11.65, 0.93]`\n- `cf = [0.08, 0.08, 2.71, 9.90]`\n\n**Registry cross-reference** (all SciERC Qwen3-8B, phase2):\n\n**DR values:**\n- Unconstrained (15.37): `phase2_scierc_unconstrained` DR = 0.1537 = **15.37%** ✅\n- Grammar-only (14.84): `phase2_scierc_grammar_only` DR = 0.1484 = **14.84%** ✅\n- Semantic-only (11.65): `phase2_scierc_semantic_only` DR = 0.1165 = **11.65%** ✅\n- Full S1 (0.93): `phase2_scierc_full_s1` DR = 0.0093 = **0.93%** ✅\n\n**CF values:**\n- Unconstrained (0.08): `phase2_scierc_unconstrained` CF = 0.0008 = **0.08%** ✅\n- Grammar-only (0.08): `phase2_scierc_grammar_only` CF = 0.0008 = **0.08%** ✅\n- Semantic-only (2.71): `phase2_scierc_semantic_only` CF = 0.0271 = **2.71%** ✅\n- Full S1 (9.90): `phase2_scierc_full_s1` CF = 0.099 = **9.90%** ✅\n\n**Verdict: All 8 values verified ✅**\n\n---\n\n### Beam Pareto Figure — plot_pareto_dual_v2.py\n\n**Hardcoded SciERC Qwen data verified against `d066_beam_sweep` registry metrics:**\n\n| k | unc rf1 | con rf1 | unc dr | con dr | unc cf | con cf |\n|---|---|---|---|---|---|---|\n| 1 | 42.95 | 42.95 | 2.11 | 0 | 0 | 0.50 |\n| 2 | 44.75 | 44.60 | 1.54 | 0 | 0 | 0.11 |\n| 4 | 43.72 | 43.60 | 1.89 | 0 | 0 | 0 |\n| 8 | 43.17 | 43.65 | 1.77 | 0 | 0 | 0 |\n\nRegistry `d066_beam_sweep` metrics section `scierc_qwen3_8b`: k2_unc R_F1=44.75 ✅, k2_con R_F1=44.60 ✅, k4_unc R_F1=43.72 ✅, k8_con R_F1=43.65 ✅ — all match exactly.\n\n**Hardcoded SciERC Llama data:**\n- k1 con: rf1=45.47, dr=0.09, cf=0.46 — **registry has no k1 Llama SciERC beam sweep data**; `d066_sweep_llama_scierc_beam1_unc` was INVALIDATED (used dev set). Source unclear.\n- k2 con: rf1=46.12, dr=0, cf=0.17 — matches `d066_sweep_llama_scierc_beam2_s1_551`: R-F1=46.12 ✅, DR=0 ✅, CF=0.17 ✅\n- k4 con: rf1=46.18, dr=0, cf=0 — matches `d066_sweep_llama_scierc_beam4_s1_551`: R-F1=46.18 ✅\n- k8 con: rf1=44.95, dr=0, cf=0 — matches `d066_sweep_llama_scierc_beam8_s1_551`: R-F1=44.95 ✅\n\n**Hardcoded DocRED Llama data:**\n- k1 unc: rf1=47.28 — `d066_sweep_llama_docred_beam1_unc` has no F1 metrics recorded (only total/success/fail counts). **Unverifiable** ⚠️\n- k1 con: rf1=47.35 — `d066_sweep_llama_docred_beam1_s1`: R-F1=47.35 ✅, DR=0 ✅, CF=0.19 ✅\n- k2 unc: rf1=51.31, dr=0.11, cf=0.05, rv=0.07 — `d066_sweep_16980_gpu1` has no F1 metrics. **Unverifiable** ⚠️\n- k2 con: rf1=51.17 — `d066_sweep_llama_beam2_s1`: R-F1=51.17 ✅, DR=0 ✅, CF=0 ✅\n- k4 unc: rf1=52.65, dr=0.04 — `d066_sweep_llama_docred_beam4_unc`: R-F1=52.65 ✅, DR=0.04 ✅\n- k4 con: rf1=51.89 — `d066_sweep_llama_docred_beam4_s1`: R-F1=51.89 ✅\n- k8 unc: rf1=51.97, dr=0, cf=0.05, rv=0.07 — `d066_sweep_llama_beam8_unc`: R-F1=51.97 ✅, DR=0 ✅, CF=0.05 ✅, RV=0.07 ✅\n- k8 con: rf1=51.74 — `d066_sweep_llama_beam8_s1`: R-F1=51.74 ✅\n\n**Verdict: SciERC Qwen fully verified ✅. SciERC Llama k1 unverifiable (invalidated experiment) ⚠️. DocRED k1 unc and k2 unc rf1/violation values unverifiable (registry entries lack F1 metrics) ⚠️. All other DocRED points verified ✅.**\n\n---\n\n### kappa_dr_data.json\n\nThe file contains per-relation kappa and DR% for SciERC and DocRED under the constrained (full_s1) condition based on a 36-annotator sample. **This file does not correspond to any registry experiment** — it appears to be an annotation study / ontology analysis (noting `n_valid`, `total_possible: 36` consistently, suggesting 36 annotators or sample pairs). No registry entry for a kappa study exists. The DR% values in this file (e.g., SciERC Compare=35.0%, Feature-of=8.29%) differ substantially from the full-test-set constrained DR values in the registry (full_s1 Compare≈2.82%, Feature-of≈1.21%), suggesting this represents a *different analysis* (possibly constraint strictness analysis, not model output). **Provenance is unverifiable against the experiment registry** ⚠️.\n\n---\n\n## Summary of Issues\n\n| Figure | Status | Issues |\n|---|---|---|\n| Fig2 unconstrained column | ✅ Verified | Exact match to registry per_relation |\n| Fig2 grammar/semantic/full_s1 columns | ❌ Unverifiable | No per-relation breakdown in registry for these conditions |\n| Fig3 8B (24%) | ✅ Verified | Derived from phase2_scierc_semantic_only |\n| Fig3 70B (84%) | ❌ No registry entry | Zero 70B experiments exist anywhere in registry |\n| Fig4 all values | ✅ Verified | All 4 DR reduction values match exactly |\n| Fig5 all 6 cells | ✅ Verified | All match computed from respective registry experiments |\n| Fig6 all 8 values | ✅ Verified | Exact match to phase2 SciERC metrics |\n| Pareto (SciERC Qwen) | ✅ Verified | Exact match to d066_beam_sweep |\n| Pareto (SciERC Llama k1) | ⚠️ Unverifiable | Source experiment invalidated |\n| Pareto (DocRED k1 unc, k2 unc) | ⚠️ Unverifiable | Registry entries missing F1 metrics |\n| kappa_dr_data.json | ⚠️ Unverifiable | No corresponding registry experiment |\n\n**Critical blocker:** Fig3's 84%/70B data point has no registry backing. There are no 70B model experiments in the registry at all. This value is either from an external source not tracked in the registry, or fabricated.\n\n**Medium priority:** Fig2's grammar/semantic/full_s1 per-relation bars need sourcing — the registry stores only aggregate DR rates for these conditions, not per-relation breakdowns."
      }
    ],
    "totalDurationMs": 182965,
    "totalTokens": 137507,
    "totalToolUseCount": 37,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2062,
      "cache_read_input_tokens": 131106,
      "output_tokens": 4338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2062
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4338,
          "cache_read_input_tokens": 131106,
          "cache_creation_input_tokens": 2062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2062,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 21,
      "searchCount": 7,
      "bashCount": 9,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "a0a14f26-7c3a-49e8-9278-d9aab224d3f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---


### Tool result

_source line 1880 · 2026-05-25T19:53:41.915Z_

<details><summary>↩ Tool result · `toolu_01K7JemnEuCrSPttxTVqu7Cb`</summary>

```text
Here is the complete data integrity audit report against all six claim categories:

---

## Data Integrity Audit Report

### 1. Beam Sweep Experiments

**Registry sources:** `d066_beam_sweep` (SciERC, Qwen3-8B LoRA FT, 551 docs), `w10_beam_ablation_k2`, `w10_beam_ablation_k8`, `w9_llama_scierc_beam_551`

**k=2 Pareto-optimal claim (R-F1 44.60, CF 0.11%, 1.18× greedy S1 latency):**
- Registry `d066_beam_sweep.scierc_qwen3_8b.k2_con`: R_F1=44.6, CF_pct=0.11, avg_time=3.463s
- `k1_con` (greedy S1): avg_time=2.932s
- Latency ratio: 3.463/2.932 = **1.18× — EXACT MATCH**

**k=4 achieves CF=0% at 1.39× claim:**
- Registry `k4_con`: CF_pct=0, avg_time=4.069s
- Ratio: 4.069/2.932 = **1.39× — EXACT MATCH**

Note: The paper's appendix text (`appendix_beam_search.tex` line 97) also correctly states "1.39× vs. greedy unconstrained; 1.18× vs. greedy S1" — both ratios appear in consistent contexts.

**ZS experiments (note: these use different exp_ids, not d066):**
- `beam_search_scierc_full_551` (Qwen ZS, k=4): R_F1=8.56, DR=0%, CF=0.53%
- `w9_llama_scierc_beam_551` (Llama ZS, k=4): R_F1=3.33, DR=0%, CF=0.93%
- `w10_beam_ablation_k2` (Qwen ZS, k=2): R_F1=8.75, DR=0.35%, CF=4.12%
- `w10_beam_ablation_k8` (Qwen ZS, k=8): R_F1=8.39, DR=0%, CF=0.08%

The **Pareto-optimal claims are about the FT regime** (d066_beam_sweep), not ZS. Registry data fully supports them.

---

### 2. 70B Experiments

**Registry sources:** `r16_70b_scierc_zs_s1`, `r16_70b_docred_zs_s1`, `eval_70b_lora_scierc_s1_constrained`, `eval_70b_lora_docred_200_s1_constrained`, `eval_70b_zs_scierc_semantic_only`

**SciERC ZS DR 6.41% → 0%:**
- `r16_70b_scierc_zs_s1`: `baseline_unc_DR_pct: 6.41`, `DR_pct: 0` — **EXACT MATCH**

**DocRED ZS DR 14.98% → 0%:**
- `r16_70b_docred_zs_s1`: `baseline_unc_DR_pct: 14.98`, `DR_pct: 0` — **EXACT MATCH**

**Semantic-only 84% DR reduction:**
- `eval_70b_zs_scierc_semantic_only`: DR_pct=1.01 (baseline=6.41%)
- Reduction: (6.41−1.01)/6.41 = **84.2% — matches paper's "84%"**
- For context, 8B semantic-only was (15.37−11.65)/15.37 = 24.2%, matching "24%" claim.

**LoRA confirms DR→0% on both datasets:**
- `eval_70b_lora_scierc_s1_constrained`: `DR_pct: 0`, `relation_f1: 0.4453` — **VERIFIED**
- `eval_70b_lora_docred_200_s1_constrained`: `DR_pct: 0`, `R_F1: 43.95` — **VERIFIED**

---

### 3. Runtime Benchmark

**Registry sources:** `p8_latency_overhead`, `p8c_ft_scierc_latency`, `d062_ontology_scalability`; file: `runtime_benchmark.json`

**S1 overhead +13.1% on SciERC (ZS):**
- `p8_latency_overhead`: unconstrained_mean_s=4.163, constrained_mean_s=4.71, `overhead_pct: 13.1`
- Calculated: (4.71−4.163)/4.163 = 13.1% — **EXACT MATCH**

**Under LoRA +10.0% overhead:**
- `p8c_ft_scierc_latency`: unconstrained_mean_s=2.612, constrained_mean_s=2.873, `overhead_mean_pct: 10`
- Calculated: (2.873−2.612)/2.612 = 10.0% — **EXACT MATCH**

**37% lower absolute latency under LoRA:**
- (4.163−2.612)/4.163 = 37.3% — **matches paper's "37%"**

**Constraint compilation <0.5s:**
- `d062_ontology_scalability`: compile_small=0.334s, compile_xlarge=0.42s — **all <0.5s, VERIFIED**

**2–3% overhead up to 200 entity types and 1000 relations:**
- `d062_ontology_scalability`: overhead_small=1.02, overhead_medium=1.03, overhead_large=1.03, overhead_xlarge=1.03 — **2–3%, EXACT MATCH**

**Note:** `runtime_benchmark.json` uses a different codebase/experimental setup (median_sec_per_doc for SciERC full_s1 shows _negative_ overhead vs unconstrained due to different sampling). The paper latency numbers come from `p8_latency_overhead` and `p8c_ft_scierc_latency` registry entries, not from `runtime_benchmark.json`.

---

### 4. Schema-Informed Prompting

**Registry source:** `mvp_phase0_scierc_schema`

**Reduces DR by 62% on SciERC:**
- `vs_minimal_dr_reduction: -0.624` (i.e., −62.4% relative reduction vs minimal prompt)
- Schema-informed DR=5.78% vs minimal/unconstrained DR=15.37%
- Calculated: (15.37−5.78)/15.37 = 62.4% — **EXACT MATCH to paper's "62%"**

**"Evaluate-for" relation violations increase by 5.8 pp:**
- `per_relation.Evaluate-for.delta_pp: 5.8` — **EXACT MATCH**

---

### 5. Post-Hoc Filtering

**Registry source:** `w8_ft_posthoc_baseline`, `posthoc_filtering_baseline`

**Achieves DR=0% but 15–74% rejection rates:**
- ZS regime rejection rates: Llama SciERC 13.89%, Qwen SciERC 16.76%, Mistral SciERC 20.27%, Llama DocRED 42.18%, Qwen DocRED 48.12%, Mistral DocRED 73.73%
- Range: **13.9%–73.7%**
- Paper claims "15–74%": the exact observed range is 13.9–73.7%; the "15–74%" is a rounded approximation. The FT regime is 0.6–1.95%.
- **MINOR DISCREPANCY**: The minimum of 13.9% is rounded up to "15%" in the paper. Not a fabrication but slightly imprecise at the lower bound.

---

### 6. Cross-Model Table (Table 3, Appendix)

**Registry sources:** `w6_mistral_scierc_unconstrained`, `w6_mistral_scierc_constrained`, `w6_mistral_docred_unconstrained`, `w6_mistral_docred_constrained`; paper table from `appendix_zs_crossmodel.tex`

**DR drops 76–99% on SciERC:**
- Qwen SciERC: 15.37→0.93 = **93.9%**
- Llama SciERC: 13.34→0.08 = **99.4%**
- Mistral SciERC: 56.94→13.4 = **76.5%**
- Range: **76–99% — EXACT MATCH**

**DR drops 42–90% on DocRED:**
- Qwen DocRED: 18.46→10.21 = **44.7%**
- Llama DocRED: 26.07→2.55 = **90.2%**
- Mistral DocRED: 57.42→33.2 = **42.2%**
- Range: **42–90% — EXACT MATCH**

**R-F1 improving in 5/6 settings:**
- SciERC Qwen: +0.13pp ✓, Llama: −0.14pp ✗, Mistral: +0.01pp ✓
- DocRED Qwen: +0.49pp ✓, Llama: +0.29pp ✓, Mistral: +1.18pp ✓
- **5/6 improved — EXACT MATCH**

---

### 7. Bootstrap CI (bootstrap_ci_results.json)

**Registry source:** `appendix_discussion.tex` Table 6 (exp_id: `r12_table2_bootstrap_ci`); the actual JSON is on the server at `/root/autodl-tmp/schema_outputs/r12_table2_bootstrap_ci.json`

The paper's Table 6 data (from the LaTeX source):
- Qwen3-8B/SciERC: Δ=−0.10, CI=[−0.30, 0.00]
- Qwen3-8B/DocRED: Δ=−0.31, CI=[**−0.69, +0.01**]
- Llama-3.1-8B/SciERC: Δ=+0.02, CI=[0.00, +0.07]
- Llama-3.1-8B/DocRED: Δ=+0.06, CI=[−0.11, **+0.25**]

**"No ΔR-F1 significant (Bonferroni-corrected)":** After Bonferroni correction at k=4, α_adj=0.0125, the smallest p-value is Qwen DocRED at p=0.056 (uncorrected), which × 4 = 0.224 — not significant. **VERIFIED**

**"95% CIs ⊆ [−0.69, +0.25] pp":** All four CIs fit exactly within [−0.69, +0.25]: lower bounds are −0.30, −0.69, 0.00, −0.11; upper bounds are 0.00, +0.01, +0.07, +0.25. **EXACT MATCH**

Note: An earlier report (`r5_ft_bootstrap_results.md`) showed different numbers (Qwen DocRED CI [−0.76, −0.05]); the paper uses the later `r12_table2_bootstrap_ci` results, which are the authoritative ones in the LaTeX.

**"Removed triples are 97.6–100% false positives":** Supported by `r12_dr_f1_impact_summary.txt`: "SciERC DR violations resolved 100% by type correction (0 removal), DocRED removed triples 97.6–100% FP." **VERIFIED** (data is on remote server, confirmed by pointer file and paper text which matches).

---

### Summary of Findings

All major paper claims are verified as consistent with registry data, with one minor precision issue:

| Claim | Status | Notes |
|-------|--------|-------|
| Beam k=2: R-F1 44.60, CF 0.11%, 1.18× greedy S1 | ✅ EXACT | d066_beam_sweep |
| Beam k=4: CF=0%, 1.39× | ✅ EXACT | d066_beam_sweep |
| 70B SciERC ZS 6.41%→0% | ✅ EXACT | r16_70b_scierc_zs_s1 |
| 70B DocRED ZS 14.98%→0% | ✅ EXACT | r16_70b_docred_zs_s1 |
| Semantic-only 84% DR reduction | ✅ EXACT (84.2%) | eval_70b_zs_scierc_semantic_only |
| LoRA DR→0% on both | ✅ EXACT | eval_70b_lora_scierc/docred_s1 |
| S1 overhead +13.1% SciERC | ✅ EXACT | p8_latency_overhead |
| LoRA +10.0% overhead | ✅ EXACT | p8c_ft_scierc_latency |
| 37% lower absolute latency | ✅ EXACT (37.3%) | calculated from above |
| Compilation <0.5s | ✅ VERIFIED | d062_ontology_scalability |
| 2–3% overhead to 200 types/1000 relations | ✅ EXACT | d062_ontology_scalability |
| Schema-informed prompt −62% DR | ✅ EXACT (−62.4%) | mvp_phase0_scierc_schema |
| Evaluate-for +5.8pp | ✅ EXACT | mvp_phase0_scierc_schema |
| Post-hoc 15–74% rejection | ⚠️ SLIGHT ROUNDING | Actual minimum is 13.9% (Llama SciERC), rounded to 15% |
| Cross-model DR 76–99% SciERC | ✅ EXACT | w6 mistral/qwen/llama experiments |
| Cross-model DR 42–90% DocRED | ✅ EXACT | w6 mistral/qwen/llama experiments |
| R-F1 improving 5/6 settings | ✅ EXACT | cross-model table data |
| No ΔR-F1 significant (Bonferroni) | ✅ VERIFIED | r12_table2_bootstrap_ci |
| CIs ⊆ [−0.69, +0.25] pp | ✅ EXACT | appendix Table 6 |
| Removed triples 97.6–100% FP | ✅ VERIFIED | r12_dr_f1_impact_summary.txt |

The only item warranting attention: the "15–74%" rejection rate lower bound is 13.9% in the data (Llama SciERC ZS, `w8_ft_posthoc_baseline.zs_regime.llama_scierc.reject_pct: 13.89`). Rounding 13.9% to "15%" is slightly aggressive — technically it should be "~14–74%". Everything else is clean.

agentId: a7fb85ca917a924dc (use SendMessage with to: 'a7fb85ca917a924dc' to continue this agent)
&lt;usage>total_tokens: 130336
tool_uses: 82
duration_ms: 378749&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e813390-996e-43d5-87fb-ebf51cabd867",
  "isSidechain": false,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "type": "user",
  "uuid": "7efeea1c-53f3-4b85-8136-02eb7cfe52b4",
  "toolUseResult": {
    "status": "completed",
    "prompt": "This is a data integrity audit for an academic paper. I need you to find specific experiment entries in the registry and verify them against paper claims.\n\nRegistry file: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/registry.yaml (7630 lines)\n\nFind and extract the EXACT metrics from these registry entries:\n\n1. **Beam sweep experiments** — search for exp_ids containing \"beam\" (e.g., d066_beam_sweep or similar). Need: k=1,2,4,8 results for Qwen and Llama on SciERC, including R-F1, CF%, latency multipliers.\n   Paper claims: k=2 Pareto-optimal: R-F1 44.60, CF 0.11%, 1.18× greedy S1 latency; k=4 achieves CF=0% at 1.39×\n\n2. **70B experiments** — search for exp_ids containing \"70b\" (e.g., r16_70b_scierc_zs_s1, r16_70b_docred_zs_s1, 70b_lora_scierc, 70b_lora_docred_200). Need: DR before/after, semantic-only DR reduction.\n   Paper claims: SciERC 6.41%→0%, DocRED 14.98%→0%; semantic-only 84% DR reduction; LoRA confirms DR→0% on both\n\n3. **Runtime benchmark** — search for exp_ids containing \"runtime\" or \"latency\" or \"overhead\". Also check this file: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/data/runtime_benchmark.json\n   Paper claims: S1 overhead +13.1% on SciERC; under LoRA +10.0% with 37% lower absolute latency; constraint compilation <0.5s; 2-3% overhead up to 200 entity types and 1000 relations\n\n4. **Schema-informed prompting** — search for exp_ids containing \"prompt\" or \"schema_informed\". \n   Paper claims: reduces DR by 62% on SciERC; \"Evaluate-for\" relation violations increase by 5.8 pp\n\n5. **Post-hoc filtering** — search for \"posthoc\" or \"post_hoc\" or \"filtering\"\n   Paper claims: achieves DR=0% but 15-74% rejection rates\n\n6. **Cross-model table** (Table 3 in appendix) — search for \"mistral\" experiments. \n   Paper claims: DR drops 76-99% on SciERC and 42-90% on DocRED; R-F1 improving in 5/6 settings\n\nFor each, grep the registry for the exp_id, read the full entry including all metrics, and report whether the paper's numbers match. Report exact registry values.\n\nAlso read: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/data/bootstrap_ci_results.json\nPaper claims: no ΔR-F1 significant (Bonferroni-corrected); 95% CIs ⊆ [-0.69, +0.25] pp; removed triples are 97.6-100% false positives",
    "agentId": "a7fb85ca917a924dc",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete data integrity audit report against all six claim categories:\n\n---\n\n## Data Integrity Audit Report\n\n### 1. Beam Sweep Experiments\n\n**Registry sources:** `d066_beam_sweep` (SciERC, Qwen3-8B LoRA FT, 551 docs), `w10_beam_ablation_k2`, `w10_beam_ablation_k8`, `w9_llama_scierc_beam_551`\n\n**k=2 Pareto-optimal claim (R-F1 44.60, CF 0.11%, 1.18× greedy S1 latency):**\n- Registry `d066_beam_sweep.scierc_qwen3_8b.k2_con`: R_F1=44.6, CF_pct=0.11, avg_time=3.463s\n- `k1_con` (greedy S1): avg_time=2.932s\n- Latency ratio: 3.463/2.932 = **1.18× — EXACT MATCH**\n\n**k=4 achieves CF=0% at 1.39× claim:**\n- Registry `k4_con`: CF_pct=0, avg_time=4.069s\n- Ratio: 4.069/2.932 = **1.39× — EXACT MATCH**\n\nNote: The paper's appendix text (`appendix_beam_search.tex` line 97) also correctly states \"1.39× vs. greedy unconstrained; 1.18× vs. greedy S1\" — both ratios appear in consistent contexts.\n\n**ZS experiments (note: these use different exp_ids, not d066):**\n- `beam_search_scierc_full_551` (Qwen ZS, k=4): R_F1=8.56, DR=0%, CF=0.53%\n- `w9_llama_scierc_beam_551` (Llama ZS, k=4): R_F1=3.33, DR=0%, CF=0.93%\n- `w10_beam_ablation_k2` (Qwen ZS, k=2): R_F1=8.75, DR=0.35%, CF=4.12%\n- `w10_beam_ablation_k8` (Qwen ZS, k=8): R_F1=8.39, DR=0%, CF=0.08%\n\nThe **Pareto-optimal claims are about the FT regime** (d066_beam_sweep), not ZS. Registry data fully supports them.\n\n---\n\n### 2. 70B Experiments\n\n**Registry sources:** `r16_70b_scierc_zs_s1`, `r16_70b_docred_zs_s1`, `eval_70b_lora_scierc_s1_constrained`, `eval_70b_lora_docred_200_s1_constrained`, `eval_70b_zs_scierc_semantic_only`\n\n**SciERC ZS DR 6.41% → 0%:**\n- `r16_70b_scierc_zs_s1`: `baseline_unc_DR_pct: 6.41`, `DR_pct: 0` — **EXACT MATCH**\n\n**DocRED ZS DR 14.98% → 0%:**\n- `r16_70b_docred_zs_s1`: `baseline_unc_DR_pct: 14.98`, `DR_pct: 0` — **EXACT MATCH**\n\n**Semantic-only 84% DR reduction:**\n- `eval_70b_zs_scierc_semantic_only`: DR_pct=1.01 (baseline=6.41%)\n- Reduction: (6.41−1.01)/6.41 = **84.2% — matches paper's \"84%\"**\n- For context, 8B semantic-only was (15.37−11.65)/15.37 = 24.2%, matching \"24%\" claim.\n\n**LoRA confirms DR→0% on both datasets:**\n- `eval_70b_lora_scierc_s1_constrained`: `DR_pct: 0`, `relation_f1: 0.4453` — **VERIFIED**\n- `eval_70b_lora_docred_200_s1_constrained`: `DR_pct: 0`, `R_F1: 43.95` — **VERIFIED**\n\n---\n\n### 3. Runtime Benchmark\n\n**Registry sources:** `p8_latency_overhead`, `p8c_ft_scierc_latency`, `d062_ontology_scalability`; file: `runtime_benchmark.json`\n\n**S1 overhead +13.1% on SciERC (ZS):**\n- `p8_latency_overhead`: unconstrained_mean_s=4.163, constrained_mean_s=4.71, `overhead_pct: 13.1`\n- Calculated: (4.71−4.163)/4.163 = 13.1% — **EXACT MATCH**\n\n**Under LoRA +10.0% overhead:**\n- `p8c_ft_scierc_latency`: unconstrained_mean_s=2.612, constrained_mean_s=2.873, `overhead_mean_pct: 10`\n- Calculated: (2.873−2.612)/2.612 = 10.0% — **EXACT MATCH**\n\n**37% lower absolute latency under LoRA:**\n- (4.163−2.612)/4.163 = 37.3% — **matches paper's \"37%\"**\n\n**Constraint compilation <0.5s:**\n- `d062_ontology_scalability`: compile_small=0.334s, compile_xlarge=0.42s — **all <0.5s, VERIFIED**\n\n**2–3% overhead up to 200 entity types and 1000 relations:**\n- `d062_ontology_scalability`: overhead_small=1.02, overhead_medium=1.03, overhead_large=1.03, overhead_xlarge=1.03 — **2–3%, EXACT MATCH**\n\n**Note:** `runtime_benchmark.json` uses a different codebase/experimental setup (median_sec_per_doc for SciERC full_s1 shows _negative_ overhead vs unconstrained due to different sampling). The paper latency numbers come from `p8_latency_overhead` and `p8c_ft_scierc_latency` registry entries, not from `runtime_benchmark.json`.\n\n---\n\n### 4. Schema-Informed Prompting\n\n**Registry source:** `mvp_phase0_scierc_schema`\n\n**Reduces DR by 62% on SciERC:**\n- `vs_minimal_dr_reduction: -0.624` (i.e., −62.4% relative reduction vs minimal prompt)\n- Schema-informed DR=5.78% vs minimal/unconstrained DR=15.37%\n- Calculated: (15.37−5.78)/15.37 = 62.4% — **EXACT MATCH to paper's \"62%\"**\n\n**\"Evaluate-for\" relation violations increase by 5.8 pp:**\n- `per_relation.Evaluate-for.delta_pp: 5.8` — **EXACT MATCH**\n\n---\n\n### 5. Post-Hoc Filtering\n\n**Registry source:** `w8_ft_posthoc_baseline`, `posthoc_filtering_baseline`\n\n**Achieves DR=0% but 15–74% rejection rates:**\n- ZS regime rejection rates: Llama SciERC 13.89%, Qwen SciERC 16.76%, Mistral SciERC 20.27%, Llama DocRED 42.18%, Qwen DocRED 48.12%, Mistral DocRED 73.73%\n- Range: **13.9%–73.7%**\n- Paper claims \"15–74%\": the exact observed range is 13.9–73.7%; the \"15–74%\" is a rounded approximation. The FT regime is 0.6–1.95%.\n- **MINOR DISCREPANCY**: The minimum of 13.9% is rounded up to \"15%\" in the paper. Not a fabrication but slightly imprecise at the lower bound.\n\n---\n\n### 6. Cross-Model Table (Table 3, Appendix)\n\n**Registry sources:** `w6_mistral_scierc_unconstrained`, `w6_mistral_scierc_constrained`, `w6_mistral_docred_unconstrained`, `w6_mistral_docred_constrained`; paper table from `appendix_zs_crossmodel.tex`\n\n**DR drops 76–99% on SciERC:**\n- Qwen SciERC: 15.37→0.93 = **93.9%**\n- Llama SciERC: 13.34→0.08 = **99.4%**\n- Mistral SciERC: 56.94→13.4 = **76.5%**\n- Range: **76–99% — EXACT MATCH**\n\n**DR drops 42–90% on DocRED:**\n- Qwen DocRED: 18.46→10.21 = **44.7%**\n- Llama DocRED: 26.07→2.55 = **90.2%**\n- Mistral DocRED: 57.42→33.2 = **42.2%**\n- Range: **42–90% — EXACT MATCH**\n\n**R-F1 improving in 5/6 settings:**\n- SciERC Qwen: +0.13pp ✓, Llama: −0.14pp ✗, Mistral: +0.01pp ✓\n- DocRED Qwen: +0.49pp ✓, Llama: +0.29pp ✓, Mistral: +1.18pp ✓\n- **5/6 improved — EXACT MATCH**\n\n---\n\n### 7. Bootstrap CI (bootstrap_ci_results.json)\n\n**Registry source:** `appendix_discussion.tex` Table 6 (exp_id: `r12_table2_bootstrap_ci`); the actual JSON is on the server at `/root/autodl-tmp/schema_outputs/r12_table2_bootstrap_ci.json`\n\nThe paper's Table 6 data (from the LaTeX source):\n- Qwen3-8B/SciERC: Δ=−0.10, CI=[−0.30, 0.00]\n- Qwen3-8B/DocRED: Δ=−0.31, CI=[**−0.69, +0.01**]\n- Llama-3.1-8B/SciERC: Δ=+0.02, CI=[0.00, +0.07]\n- Llama-3.1-8B/DocRED: Δ=+0.06, CI=[−0.11, **+0.25**]\n\n**\"No ΔR-F1 significant (Bonferroni-corrected)\":** After Bonferroni correction at k=4, α_adj=0.0125, the smallest p-value is Qwen DocRED at p=0.056 (uncorrected), which × 4 = 0.224 — not significant. **VERIFIED**\n\n**\"95% CIs ⊆ [−0.69, +0.25] pp\":** All four CIs fit exactly within [−0.69, +0.25]: lower bounds are −0.30, −0.69, 0.00, −0.11; upper bounds are 0.00, +0.01, +0.07, +0.25. **EXACT MATCH**\n\nNote: An earlier report (`r5_ft_bootstrap_results.md`) showed different numbers (Qwen DocRED CI [−0.76, −0.05]); the paper uses the later `r12_table2_bootstrap_ci` results, which are the authoritative ones in the LaTeX.\n\n**\"Removed triples are 97.6–100% false positives\":** Supported by `r12_dr_f1_impact_summary.txt`: \"SciERC DR violations resolved 100% by type correction (0 removal), DocRED removed triples 97.6–100% FP.\" **VERIFIED** (data is on remote server, confirmed by pointer file and paper text which matches).\n\n---\n\n### Summary of Findings\n\nAll major paper claims are verified as consistent with registry data, with one minor precision issue:\n\n| Claim | Status | Notes |\n|-------|--------|-------|\n| Beam k=2: R-F1 44.60, CF 0.11%, 1.18× greedy S1 | ✅ EXACT | d066_beam_sweep |\n| Beam k=4: CF=0%, 1.39× | ✅ EXACT | d066_beam_sweep |\n| 70B SciERC ZS 6.41%→0% | ✅ EXACT | r16_70b_scierc_zs_s1 |\n| 70B DocRED ZS 14.98%→0% | ✅ EXACT | r16_70b_docred_zs_s1 |\n| Semantic-only 84% DR reduction | ✅ EXACT (84.2%) | eval_70b_zs_scierc_semantic_only |\n| LoRA DR→0% on both | ✅ EXACT | eval_70b_lora_scierc/docred_s1 |\n| S1 overhead +13.1% SciERC | ✅ EXACT | p8_latency_overhead |\n| LoRA +10.0% overhead | ✅ EXACT | p8c_ft_scierc_latency |\n| 37% lower absolute latency | ✅ EXACT (37.3%) | calculated from above |\n| Compilation <0.5s | ✅ VERIFIED | d062_ontology_scalability |\n| 2–3% overhead to 200 types/1000 relations | ✅ EXACT | d062_ontology_scalability |\n| Schema-informed prompt −62% DR | ✅ EXACT (−62.4%) | mvp_phase0_scierc_schema |\n| Evaluate-for +5.8pp | ✅ EXACT | mvp_phase0_scierc_schema |\n| Post-hoc 15–74% rejection | ⚠️ SLIGHT ROUNDING | Actual minimum is 13.9% (Llama SciERC), rounded to 15% |\n| Cross-model DR 76–99% SciERC | ✅ EXACT | w6 mistral/qwen/llama experiments |\n| Cross-model DR 42–90% DocRED | ✅ EXACT | w6 mistral/qwen/llama experiments |\n| R-F1 improving 5/6 settings | ✅ EXACT | cross-model table data |\n| No ΔR-F1 significant (Bonferroni) | ✅ VERIFIED | r12_table2_bootstrap_ci |\n| CIs ⊆ [−0.69, +0.25] pp | ✅ EXACT | appendix Table 6 |\n| Removed triples 97.6–100% FP | ✅ VERIFIED | r12_dr_f1_impact_summary.txt |\n\nThe only item warranting attention: the \"15–74%\" rejection rate lower bound is 13.9% in the data (Llama SciERC ZS, `w8_ft_posthoc_baseline.zs_regime.llama_scierc.reject_pct: 13.89`). Rounding 13.9% to \"15%\" is slightly aggressive — technically it should be \"~14–74%\". Everything else is clean."
      }
    ],
    "totalDurationMs": 378749,
    "totalTokens": 130336,
    "totalToolUseCount": 82,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 959,
      "cache_read_input_tokens": 125441,
      "output_tokens": 3935,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 959
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3935,
          "cache_read_input_tokens": 125441,
          "cache_creation_input_tokens": 959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 959,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 22,
      "searchCount": 1,
      "bashCount": 59,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "8e813390-996e-43d5-87fb-ebf51cabd867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---


### Runtime record

_source line 1881_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[飞书用户 用户]: 📊 论文自检任务（重大）：全文数据真实性与可追溯性彻底审计  这是一次彻底的大检查，必须认真对待。AI 写论文最致命的两个问题：编数字（hallucinate）和抄数字（数字之间不一致或来源不明）。这次的目标是把每一个出现在论文里的数字都\"对账\"清楚。  ⚠️ 凡是查不到出处的数字，要么找到出处，要么删掉。不允许凭印象、凭\"差不多\"、凭老版本残留的数字留在论文里。  ---…",
  "leafUuid": "7efeea1c-53f3-4b85-8136-02eb7cfe52b4",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25"
}
```

---


### Runtime record

_source line 1882_

```json
{
  "type": "ai-title",
  "aiTitle": "Paper formatting and figure optimization for EMNLP",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25"
}
```

---


### Tool result

_source line 1883 · 2026-05-25T19:53:45.103Z_

<details><summary>↩ Tool result · `toolu_01GbX6E1kbjk4vHDez2cf3er`</summary>

```text
Now I have comprehensive data. Let me compile the audit report:

---

## Data Integrity Audit Results

### 1. WikiEvents Section (section5_wikievents_draft.tex)

The section contains exactly 3 numbers:
- "246 documents" — Registry: all 4 WikiEvents experiments have `data_count: 246`. **MATCH**
- "3 models" — Registry confirms Qwen, Llama, Mistral. **MATCH**
- "$n{=}20$" (fine-tuning composability) — Described as "preliminary"; no fine-tuning WikiEvents experiment exists in registry. This is a claimed limitation/caveat, not a number derived from a completed experiment. **UNVERIFIABLE — no registry backing**. The section should either be removed or backed by an actual experiment.

No other numbers in the section body. The rest of the WikiEvents details are in the Appendix files (which were not specified for audit here).

---

### 2. Appendix Beam Search (appendix_beam_search.tex)

**Table tab:beam-search (Zero-shot greedy vs beam, 50-doc DocRED subset)**

Paper vs Registry (`d066_beam_sweep` metrics + earlier ZS experiments):

| Row | Metric | Paper | Registry | Status |
|-----|--------|-------|----------|--------|
| Qwen/SciERC Greedy | DR, CF, E-F1, R-F1 | 0.93, 9.90, 30.98, 8.36 | phase2_scierc_full_s1: DR=0.93, CF=9.90%, E-F1=30.98, R-F1=8.36 | **MATCH** |
| Qwen/SciERC Beam-4 | DR, CF, E-F1, R-F1 | 0, 0.53, 32.00, 8.56 | Not found in registry as standalone ZS beam Qwen SciERC 50-doc | **UNVERIFIED** |
| Llama/SciERC Greedy | DR, CF, E-F1, R-F1 | 0.08, 6.56, 23.49, 2.54 | llama_scierc_full_s1: DR=0.08%, CF=6.56%, E-F1=23.49, R-F1=2.54 | **MATCH** |
| Mistral/SciERC Greedy | DR, CF, E-F1, R-F1 | 13.40, 1.27, 27.46, 3.67 | w6_mistral_scierc_constrained: DR=13.4%, CF=1.27%, R-F1=3.67 | **MATCH** (E-F1 27.46 from notes, consistent) |

**Table tab:beam-ablation (Qwen3-8B SciERC, beam width ablation)**

All 8 numbers (k=1,2,4,8 for DR and CF, E-F1, R-F1) match `d066_beam_sweep.metrics.scierc_qwen3_8b` exactly:
- k=1: DR=0.93, CF=9.90 (→paper: 0.93, 9.90) **MATCH**
- k=2: DR=0.35, CF=4.12 (paper: 0.35, 4.12) **MATCH**
- k=4: DR=0, CF=0.53 (paper: 0, 0.53) **MATCH**
- k=8: DR=0, CF=0.08 (paper: 0, 0.08) **MATCH**
- E-F1: 30.98/31.54/32.00/32.18 — **MATCH**
- R-F1: 8.36/8.75/8.56/8.39 — **MATCH**

**Table tab:beam-sweep (LoRA beam sweep, Qwen3-8B SciERC)**

All values match `d066_beam_sweep.metrics.scierc_qwen3_8b`:
- k=1 unc: E-F1=66.88, R-F1=42.95, DR=2.11%, lat=2.494s **MATCH**
- k=1 con: E-F1=66.88, R-F1=42.95, DR=0, CF=0.50, lat=2.932s **MATCH**
- k=2 unc: E-F1=67.79, R-F1=44.75, DR=1.54, lat=2.954s **MATCH**
- k=2 con: E-F1=67.71, R-F1=44.60, DR=0, CF=0.11, lat=3.463s **MATCH**
- k=4 unc: E-F1=67.49, R-F1=43.72, DR=1.89, lat=3.485s **MATCH**
- k=4 con: E-F1=67.22, R-F1=43.60, DR=0, CF=0, lat=4.069s **MATCH**
- k=8 unc: E-F1=66.40, R-F1=43.17, DR=1.77, lat=4.194s **MATCH**
- k=8 con: E-F1=66.36, R-F1=43.65, DR=0, CF=0, lat=5.058s **MATCH**

**Latency table (tab:beam-latency):** Paper shows Greedy unc=2.612, Greedy con=2.873, Beam-4 unc=3.446, Beam-4 con=4.013. Registry `d066_beam_sweep` has k=1 unc lat=2.494 and k=1 con lat=2.932. **MISMATCH** — latency table uses different numbers from beam sweep. These may come from a separate latency experiment; the paper cites SciERC 551 docs Qwen3-8B LoRA RTX PRO 6000 Blackwell, but d066 values for k=1 are 2.494/2.932 vs paper 2.612/2.873. This is a **discrepancy** that needs verification.

**Table tab:beam-docred-998-zs** (998-doc ZS beam):
- Qwen: DR=0, CF=4.94, E-F1=58.19, R-F1=8.72 — Registry `r14_qwen_docred_beam4_998`: DR=0, CF=4.94%, E-F1=58.19, R-F1=8.72 **MATCH**
- Llama: DR=0, CF=1.00, E-F1=57.81, R-F1=8.83 — Registry `r14_llama_docred_beam4_998`: DR=0, CF=1%, E-F1=57.81, R-F1=8.83 **MATCH**

Text claim: "Llama: CF 8.54%→1.00%, 88% reduction; R-F1 +2.6pp" — Registry baseline notes show `baseline_ZS_greedy_CF_pct: 8.54` and `baseline_ZS_greedy_R_F1: 6.27`, and beam R-F1=8.83, so +2.56pp ≈ "+2.6pp". **MATCH**

**Composability paragraph:** "CF=1.18%→0%, E-F1=66.88, R-F1=43.60" after adding beam-4 to greedy FT LoRA. Paper also claims "Llama beam-4 k=4 achieves R-F1=46.18" — Registry `q1_llama_lora_scierc_beam4` gives R-F1=46.11 (not 46.18). **DISCREPANCY: paper says 46.18, registry says 46.11**.

**Table tab:beam-docred-lora** (LoRA greedy vs beam, DocRED 998 docs):
- Qwen Greedy: DR=0.01, CF=0.41, E-F1=81.43, R-F1=40.56, PF=8.52 — Registry `d065_qwen_greedy_4096_r2`: DR=0, CF=0.22, PF=8.52, E-F1=81.87, R-F1=40.79. **MISMATCH**: Paper shows DR=0.01, CF=0.41, E-F1=81.43, R-F1=40.56; registry shows DR=0, CF=0.22, E-F1=81.87, R-F1=40.79. These are divergent. There may be a separate greedy LoRA DocRED 998 experiment not found.
- Qwen Beam-4: DR=0, CF=0.01, E-F1=84.00, R-F1=44.46, PF=2.9 — Cannot find this experiment in registry under d066 (d066 swept only 200-doc subset). **UNVERIFIED**
- Llama Greedy: DR=0.21, CF=0.21, E-F1=83.94, R-F1=43.78, PF=2.51 — **UNVERIFIED** (no direct match found)
- Llama Beam-4: DR=0, CF=0, E-F1=85.23, R-F1=47.17, PF=1.3 — `d066_sweep_llama_beam2_s1` was 200 docs. `d066_sweep_llama_beam8_s1` shows E-F1=85.76, R-F1=51.74 on 200 docs. For 998 docs beam-4, not directly found. **UNVERIFIED**

---

### 3. Appendix 70B Ablation (appendix_70b_ablation.tex)

**Table tab:70b-ft-ablation (SciERC, 551 docs)**

| Mode | DR | R-F1 | E-F1 | CF | Paper | Registry | Status |
|------|-----|------|------|-----|-------|----------|--------|
| Unconstrained | 1.50 | 44.73 | 64.86 | 0 | Paper | `eval_70b_lora_scierc_unconstrained`: DR=1.5, R-F1=44.73, E-F1=64.86, CF=0 | **MATCH** |
| Grammar | 1.50 | 44.63 | 64.82 | 0 | Paper | `eval_70b_lora_scierc_grammar_only`: DR=0.015→1.5%, R-F1=44.63, E-F1=64.82, CF=0 | **MATCH** |
| Semantic | 0.60 | 44.73 | 64.86 | 9 (count) | Paper | `eval_70b_lora_scierc_semantic_only`: DR=0.6%, R-F1=44.73, E-F1=64.86, CF_count=9 | **MATCH** |
| S1 | 0 | 44.53 | 64.76 | 15 | Paper | `eval_70b_lora_scierc_s1_constrained`: DR=0, R-F1=44.53, E-F1=64.76, CF_count=15 | **MATCH** |
| S2 | 0 | 36.28 | 62.35 | 18 | Paper | `eval_70b_lora_scierc_full_s2`: DR=0, R-F1=36.28, E-F1=62.35, CF_count=18 | **MATCH** |
| Beam4 S1 | 0 | 44.81 | 64.89 | 1 | Paper | `eval_70b_lora_scierc_beam4_s1`: DR=0, R-F1=44.81, E-F1=64.89, CF_count=1 | **MATCH** |

Text: "S2 causes -8.45pp R-F1" → 44.53-36.28=8.25pp. **DISCREPANCY: paper says -8.45pp, actual is -8.25pp**.

**Table tab:70b-docred-ablation (DocRED, 998 docs)**

| Mode | DR | R-F1 | E-F1 | Status |
|------|-----|------|------|--------|
| Unconstrained | 0.22 | 43.80 | 80.34 | `eval_70b_lora_docred_200_unconstrained`: DR=0.22, R-F1=43.80, E-F1=80.34 | **MATCH** |
| Grammar | 0.38 | 43.96 | 80.13 | `eval_70b_lora_docred_200_grammar_only`: DR=0.38, R-F1=43.96, E-F1=80.13 | **MATCH** |
| Semantic | 0 | 43.61 | 80.06 | `eval_70b_lora_docred_200_semantic_only`: DR=0, R-F1=43.61, E-F1=80.06 | **MATCH** |
| S1 | 0 | 43.95 | 79.38 | `eval_70b_lora_docred_200_s1_constrained`: DR=0, R-F1=43.95, E-F1=79.38 | **MATCH** |
| S2 | 0 | 36.45 | 84.96 | `eval_70b_lora_docred_200_full_s2`: DR=0, R-F1=36.45, E-F1=84.96 | **MATCH** |
| Beam4 S1 | 0 | 48.14 | 85.57 | `eval_70b_lora_docred_200_beam4_s1`: DR=0, R-F1=48.14, E-F1=85.57 | **MATCH** |

Note: Paper caption says "998 docs" but all DocRED 70B experiments in registry used 200-doc subsets. The caption says 998 but the underlying experiments are 200 docs. **CAPTION ERROR: tab:70b-docred-ablation caption claims 998 docs; actual experiments were 200-doc subsets.**

Text: "S2 causes -7.50pp vs S1" → 43.95-36.45=7.50pp. **MATCH**. Text: "beam +4.19pp R-F1 (43.95→48.14)" — 48.14-43.95=4.19. **MATCH**.

Text: "greedy S1 fails to parse 12.5% of documents (25/200)" — Registry PF=12.5% (25/200). **MATCH**.

**Table tab:70b-docred-zs-ablation (ZS, 200-doc subset)**

| Mode | DR | RV | ET | CF | R-F1 | E-F1 | Registry | Status |
|------|-----|----|----|-----|------|------|----------|--------|
| Unconstrained | 13.45 | 7.88 | 0 | 0 | 13.25 | 70.14 | `eval_70b_zs_docred_200_unconstrained`: DR=13.45, RV=7.88, CF=0, R-F1=13.25, E-F1=70.14 | **MATCH** |
| Grammar | 17.03 | 0 | 0 | 0 | 13.23 | 70.12 | `eval_70b_zs_docred_200_grammar_only`: DR=17.03, RV=0, CF=0, R-F1=13.23, E-F1=70.12 | **MATCH** |
| Semantic | 1.66 | 8.24 | 0.12 | 132 | 13.05 | 70.10 | `eval_70b_zs_docred_200_semantic_only`: DR=1.66, RV=8.24, ET=0.12, CF_count=132, R-F1=13.05, E-F1=70.10 | **MATCH** |
| S1 | 0 | 0 | 0 | 173 | 13.25 | 70.05 | `eval_70b_zs_docred_200_full_s1`: DR=0, CF%=5.34 (not count 173). **DISCREPANCY: paper says CF=173 (count), registry shows CF%=5.34%** — 5.34% of 2637 relations = ~141, not 173. Needs reconciliation. |

Text: "grammar-only DR increases +3.58pp (13.45→17.03)" — 17.03-13.45=3.58. **MATCH**.

---

### 4. Appendix Quantization (appendix_quantization.tex)

**Table tab:quantization**

| Cell | Paper | Registry | Status |
|------|-------|----------|--------|
| Qwen SciERC FP16 DR | 0 | `w5_qwen_lora_scierc_constrained_eval` (full S1): DR=0 | **MATCH** |
| Qwen SciERC FP16 R-F1 | 43.77 | Qwen FT S1 greedy SciERC (from composability text) | **MATCH** |
| Qwen SciERC FP16 E-F1 | 67.05 | **MATCH** |
| Qwen SciERC INT4 DR | 0 | `sf2_qwen_int4_scierc_s1`: DR=0 | **MATCH** |
| Qwen SciERC INT4 R-F1 | 41.71 | `sf2_qwen_int4_scierc_s1`: R-F1=41.71 | **MATCH** |
| Qwen SciERC INT4 E-F1 | 67.05 | `sf2_qwen_int4_scierc_s1`: E-F1=67.05 | **MATCH** |
| Llama SciERC FP16 DR | 0.09 | Llama FP16 SciERC LoRA S1 DR noted in quantization text | **MATCH** |
| Llama SciERC FP16 R-F1 | 45.47 | Llama LoRA SciERC S1 FP16 (from various experiment notes) | **MATCH** |
| Llama SciERC INT4 DR | 0 | `sf2_llama_int4_scierc_s1`: DR=0 | **MATCH** |
| Llama SciERC INT4 R-F1 | 43.98 | `sf2_llama_int4_scierc_s1`: R-F1=43.98 | **MATCH** |
| Llama SciERC INT4 E-F1 | 67.54 | `sf2_llama_int4_scierc_s1`: E-F1=67.54 | **MATCH** |
| Qwen DocRED FP16 R-F1 | 40.79 (998 docs, dagger) | `d065_qwen_greedy_4096_r2`: R-F1=40.79 | **MATCH** |
| Qwen DocRED FP16 E-F1 | 81.87 (dagger) | `d065_qwen_greedy_4096_r2`: E-F1=81.87 | **MATCH** |
| Qwen DocRED FP16 PF | 8.5% (dagger) | `d065_qwen_greedy_4096_r2`: PF=8.52% | **MATCH** |
| Qwen DocRED INT4 R-F1 | 40.07 | `sf2_qwen_int4_docred_s1`: R-F1=40.07 | **MATCH** |
| Qwen DocRED INT4 E-F1 | 74.84 | `sf2_qwen_int4_docred_s1`: E-F1=74.84 | **MATCH** |
| Qwen DocRED INT4 PF | 18.5 | `sf2_qwen_int4_docred_s1`: PF=18.5% | **MATCH** |
| Llama DocRED FP16 R-F1 | 47.35 | Not directly found in registry with this exact value | **UNVERIFIED** |
| Llama DocRED FP16 E-F1 | 85.43 | Not directly found | **UNVERIFIED** |
| Llama DocRED INT4 R-F1 | 48.04 | `sf2_llama_int4_docred_s1`: R-F1=48.04 | **MATCH** |
| Llama DocRED INT4 E-F1 | 84.18 | `sf2_llama_int4_docred_s1`: E-F1=84.18 | **MATCH** |
| Llama DocRED INT4 PF | 2.5 | `sf2_llama_int4_docred_s1`: PF=2.5% | **MATCH** |

All verified numbers match. Two Llama DocRED FP16 cells are unverified (no clear registry entry found for FP16 Llama DocRED LoRA S1 200-doc eval).

---

### 5. Appendix Full Fine-Tuning (appendix_full_ft.tex)

**Table tab:full-ft**

| Row | E-F1 | R-F1 | DR% | CF% | Registry | Status |
|-----|------|------|-----|-----|----------|--------|
| Full FT unconstrained | 64.78 | 37.89 | 2.74 | 0 | `d062_full_ft_scierc.metrics.unconstrained`: E-F1=64.78, R-F1=37.89, DR=2.74, CF=0 | **MATCH** |
| Full FT + S1 | 64.78 | 37.89 | 0 | 1.31 | `d062_full_ft_scierc.metrics.constrained`: E-F1=64.78, R-F1=37.89, DR=0, CF=1.31 | **MATCH** |
| LoRA unconstrained | 67.05 | 43.86 | 1.95 | 0 | Various Qwen LoRA experiments | **MATCH** |
| LoRA + S1 | 67.05 | 43.77 | 0 | 1.18 | Consistent with d066 k=1 con S1 | **MATCH** |

Text: "30 violations, Part-of 14.6%, Hyponym-of 9.6%, Evaluate-for 8.4%" — these per-type breakdowns are not in the registry. **UNVERIFIED** (qualitative analysis not registered).

---

### 6. Appendix Cross-Model Zero-Shot (appendix_zs_crossmodel.tex)

**Table tab:cross-model**

| Row | DR | RV | ET | CF | R-F1 | Registry | Status |
|-----|-----|----|----|-----|------|----------|--------|
| Qwen SciERC U | 15.37 | 1.39 | 0.40 | 0.08 | 8.23 | `phase2_scierc_unconstrained`: DR=15.37, RV=1.39, ET=0.40, CF=0.08, R-F1=8.23 | **MATCH** |
| Qwen SciERC S1 | 0.93 | 0 | 0 | 9.90 | 8.36 | `phase2_scierc_full_s1`: DR=0.93, CF=9.90, R-F1=8.36 | **MATCH** |
| Llama SciERC U | 13.34 | 0.55 | 0 | 0.24 | 2.68 | `llama_scierc_unconstrained`: DR=13.34, RV=0.55, ET=0, CF=0.24 (6 violations = ~0.47%, not 0.24%) — **MINOR DISCREPANCY**: registry shows 6 CF violations from 1274 relations = 0.47%, paper shows 0.24. The earlier notes say "cross_field_consistency_violations: 6" — 6/1315 = 0.46%, not 0.24%. But some run's metrics may differ. |
| Llama SciERC S1 | 0.08 | 0 | 0 | 6.56 | 2.54 | `llama_scierc_full_s1`: DR=0.08, CF=6.56, R-F1=2.54 | **MATCH** |
| Mistral SciERC U | 56.94 | 0 | 1.50 | 56.87 | 3.66 | `w6_mistral_scierc_unconstrained`: DR=56.94, ET=1.5, RV=0, CF=56.87, R-F1=3.66 | **MATCH** |
| Mistral SciERC S1 | 13.40 | 0 | 0 | 1.27 | 3.67 | `w6_mistral_scierc_constrained`: DR=13.4, CF=1.27, R-F1=3.67 | **MATCH** |
| Qwen DocRED U | 18.46 | 29.66 | 2.48 | 0.10 | 7.74 | `phase2_docred_unconstrained`: DR=18.46, RV=29.66, ET=2.48, CF=0.10, R-F1=7.74 | **MATCH** |
| Qwen DocRED S1 | 10.21 | 0.03 | 0 | 2.57 | 8.23 | `phase2_docred_full_s1`: DR=10.21, RV=0.03, CF=2.57, R-F1=8.23 | **MATCH** |
| Llama DocRED U | 26.07 | 16.03 | 0.13 | 0.17 | 5.98 | `llama_docred_unconstrained`: DR=26.07, RV=16.03, ET=0.13, CF=0.17, R-F1=5.98 | **MATCH** |
| Llama DocRED S1 | 2.55 | 0 | 0 | 12.02 | 6.27 | `llama_docred_full_s1`: DR=2.55, CF=12.02, R-F1=6.27 | **MATCH** |
| Mistral DocRED U | 57.42 | 42.35 | 7.58 | 24.78 | 4.34 | `w6_mistral_docred_unconstrained`: DR=57.42, RV=42.35, ET=7.58, CF=24.78, R-F1=4.34 | **MATCH** |
| Mistral DocRED S1 | 33.20 | 0 | 0 | 0.19 | 5.52 | `w6_mistral_docred_constrained`: DR=33.2, CF=0.19, R-F1=5.52 | **MATCH** |

Parse failures footnote: "Llama DocRED 9.1%" — Registry `llama_docred_unconstrained`: 68 failures / 998 docs = 6.8%. **DISCREPANCY: paper says 9.1%, registry says 6.8%**. (The S1 run had 91/998=9.1%). The footnote likely should say "Llama DocRED S1 9.1%; unconstrained 6.8%" but paper applies it ambiguously. If it refers to S1, it matches registry.

---

### 7. Appendix Downstream Analysis (appendix_downstream_analysis.tex)

Claims to verify:

**Table tab:lucky-violations-detail:**
- SciERC Qwen: TP=461, Lucky=4, 0.87%, R drop=0.41pp — **NOT IN REGISTRY** (no experiment ID found for lucky violation audit)
- SciERC Llama: TP=467, Lucky=5, 1.07%, R drop=0.51pp — **NOT IN REGISTRY**
- DocRED Qwen: TP=5746, Lucky=1, 0.02%, R drop=0.01pp — **NOT IN REGISTRY**
- DocRED Llama: TP=6226, Lucky=1, 0.02%, R drop=0.01pp — **NOT IN REGISTRY**

No registry experiment IDs are referenced in the tex file for these specific downstream analysis figures. These appear to be post-hoc analysis numbers computed from existing outputs but not registered as formal experiments. **ALL NUMBERS UNVERIFIED AGAINST REGISTRY.**

Text claims: "97.6-100% false positives", "0.24% gold triples affected", "0.2% false negatives blocked", "36 residual DR violations with 39%/33%/28% decomposition", "irreducible floor ~3 violations" — **NONE of these specific numbers appear in the registry**. These are analytical claims not backed by formal experiment entries.

---

### 8. Appendix GoLLIE Comparison (appendix_gollie_comparison.tex)

The appendix contains **no numerical table** — it is a purely qualitative discussion of the paradigm difference between GoLLIE and OntoCoDec, explicitly stating that "direct numerical comparison is methodologically constrained" and is left to future work. There are no numbers to cross-reference. **N/A — no numbers to verify.**

---

## Summary of Issues (Priority Order)

**Critical mismatches requiring correction:**

1. **tab:beam-docred-lora (Qwen Greedy DocRED 998)**: Paper shows DR=0.01%, CF=0.41%, E-F1=81.43, R-F1=40.56; registry `d065_qwen_greedy_4096_r2` shows DR=0%, CF=0.22%, E-F1=81.87, R-F1=40.79. These diverge significantly — paper may be using a different (earlier) experiment run not found in registry, or numbers were misreported.

2. **Llama FT beam SciERC R-F1**: Paper claims 46.18; registry `q1_llama_lora_scierc_beam4` = 46.11. Small but exact value differs.

3. **tab:70b-docred-ablation caption**: Claims "998 docs" but all underlying experiments were 200-doc subsets.

4. **70B SciERC S2 R-F1 degradation**: Paper says "−8.45pp"; actual is 44.53−36.28 = −8.25pp.

5. **tab:beam-latency latency values**: Paper greedy unc=2.612, registry d066 k=1=2.494. May come from a separate latency experiment (`p8_latency_overhead`) not checked — needs verification.

6. **tab:70b-docred-zs-ablation S1 CF**: Paper says CF=173 (count); registry `eval_70b_zs_docred_200_full_s1` reports CF%=5.34% (which on ~2637 relations ≈ 141, not 173).

7. **Cross-model table parse failure footnote**: "Llama DocRED 9.1%" — this matches the S1 run (91/998), not the unconstrained run (68/998=6.8%). Context is ambiguous.

**Unverified numbers (no registry backing found):**
- All numbers in `appendix_downstream_analysis.tex` (lucky violations table and all percentage claims)
- Llama DocRED FP16 baseline in quantization table (R-F1=47.35, E-F1=85.43)
- WikiEvents $n{=}20$ fine-tuning composability claim
- Qwen/Llama beam ZS SciERC and DocRED 50-doc subset numbers (tab:beam-search rows for beam configurations)
- Tab:beam-docred-lora Qwen Beam-4 and all Llama rows

agentId: ab411afdd72479434 (use SendMessage with to: 'ab411afdd72479434' to continue this agent)
&lt;usage>total_tokens: 135054
tool_uses: 72
duration_ms: 359439&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41ab9fbd-6d5c-4493-82ff-8f64699c8b22",
  "isSidechain": false,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "type": "user",
  "uuid": "767a0ee1-fc30-451c-94e0-f020ec4528c0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Data integrity audit for an academic paper. Verify WikiEvents and key appendix numbers.\n\nRegistry: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/registry.yaml\nPaper dir: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/\n\nTasks:\n\n1. **WikiEvents section**: Read section5_wikievents_draft.tex. Extract ALL numbers. Then find WikiEvents experiments in registry (search for \"wikievents\" in exp_ids). Verify each number matches.\n\n2. **Appendix beam search**: Read appendix_beam_search.tex. Extract all beam sweep table data. Cross-reference with registry beam experiments (search for \"beam\" or \"d066\").\n\n3. **Appendix 70B ablation**: Read appendix_70b_ablation.tex. Extract all numbers. Cross-reference with 70B registry entries.\n\n4. **Appendix quantization**: Read appendix_quantization.tex. Extract all numbers. Cross-reference with quantization registry entries.\n\n5. **Appendix full fine-tuning**: Read appendix_full_ft.tex. Extract all numbers. Cross-reference with full-ft registry entries (search \"full_ft\" or \"full_finetune\").\n\n6. **Appendix cross-model zero-shot**: Read appendix_zs_crossmodel.tex. This should contain Table 3 (cross-model). Extract all numbers. Cross-reference with Qwen/Llama/Mistral unconstrained and constrained experiments on both SciERC and DocRED.\n\n7. **Appendix downstream analysis**: Read appendix_downstream_analysis.tex. Extract key claims: \"97.6-100% false positives\", \"0.24% gold triples affected\", \"0.2% false negatives blocked\", \"36 residual DR violations decompose into entity type errors (39%), schema gaps (33%), relation/direction errors (28%)\", \"irreducible floor ~3 violations\".\n\n8. **Appendix GoLLIE comparison**: Read appendix_gollie_comparison.tex. Extract numbers, verify against registry (search \"gollie\").\n\nFor each, report exact matches/mismatches.",
    "agentId": "ab411afdd72479434",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data. Let me compile the audit report:\n\n---\n\n## Data Integrity Audit Results\n\n### 1. WikiEvents Section (section5_wikievents_draft.tex)\n\nThe section contains exactly 3 numbers:\n- \"246 documents\" — Registry: all 4 WikiEvents experiments have `data_count: 246`. **MATCH**\n- \"3 models\" — Registry confirms Qwen, Llama, Mistral. **MATCH**\n- \"$n{=}20$\" (fine-tuning composability) — Described as \"preliminary\"; no fine-tuning WikiEvents experiment exists in registry. This is a claimed limitation/caveat, not a number derived from a completed experiment. **UNVERIFIABLE — no registry backing**. The section should either be removed or backed by an actual experiment.\n\nNo other numbers in the section body. The rest of the WikiEvents details are in the Appendix files (which were not specified for audit here).\n\n---\n\n### 2. Appendix Beam Search (appendix_beam_search.tex)\n\n**Table tab:beam-search (Zero-shot greedy vs beam, 50-doc DocRED subset)**\n\nPaper vs Registry (`d066_beam_sweep` metrics + earlier ZS experiments):\n\n| Row | Metric | Paper | Registry | Status |\n|-----|--------|-------|----------|--------|\n| Qwen/SciERC Greedy | DR, CF, E-F1, R-F1 | 0.93, 9.90, 30.98, 8.36 | phase2_scierc_full_s1: DR=0.93, CF=9.90%, E-F1=30.98, R-F1=8.36 | **MATCH** |\n| Qwen/SciERC Beam-4 | DR, CF, E-F1, R-F1 | 0, 0.53, 32.00, 8.56 | Not found in registry as standalone ZS beam Qwen SciERC 50-doc | **UNVERIFIED** |\n| Llama/SciERC Greedy | DR, CF, E-F1, R-F1 | 0.08, 6.56, 23.49, 2.54 | llama_scierc_full_s1: DR=0.08%, CF=6.56%, E-F1=23.49, R-F1=2.54 | **MATCH** |\n| Mistral/SciERC Greedy | DR, CF, E-F1, R-F1 | 13.40, 1.27, 27.46, 3.67 | w6_mistral_scierc_constrained: DR=13.4%, CF=1.27%, R-F1=3.67 | **MATCH** (E-F1 27.46 from notes, consistent) |\n\n**Table tab:beam-ablation (Qwen3-8B SciERC, beam width ablation)**\n\nAll 8 numbers (k=1,2,4,8 for DR and CF, E-F1, R-F1) match `d066_beam_sweep.metrics.scierc_qwen3_8b` exactly:\n- k=1: DR=0.93, CF=9.90 (→paper: 0.93, 9.90) **MATCH**\n- k=2: DR=0.35, CF=4.12 (paper: 0.35, 4.12) **MATCH**\n- k=4: DR=0, CF=0.53 (paper: 0, 0.53) **MATCH**\n- k=8: DR=0, CF=0.08 (paper: 0, 0.08) **MATCH**\n- E-F1: 30.98/31.54/32.00/32.18 — **MATCH**\n- R-F1: 8.36/8.75/8.56/8.39 — **MATCH**\n\n**Table tab:beam-sweep (LoRA beam sweep, Qwen3-8B SciERC)**\n\nAll values match `d066_beam_sweep.metrics.scierc_qwen3_8b`:\n- k=1 unc: E-F1=66.88, R-F1=42.95, DR=2.11%, lat=2.494s **MATCH**\n- k=1 con: E-F1=66.88, R-F1=42.95, DR=0, CF=0.50, lat=2.932s **MATCH**\n- k=2 unc: E-F1=67.79, R-F1=44.75, DR=1.54, lat=2.954s **MATCH**\n- k=2 con: E-F1=67.71, R-F1=44.60, DR=0, CF=0.11, lat=3.463s **MATCH**\n- k=4 unc: E-F1=67.49, R-F1=43.72, DR=1.89, lat=3.485s **MATCH**\n- k=4 con: E-F1=67.22, R-F1=43.60, DR=0, CF=0, lat=4.069s **MATCH**\n- k=8 unc: E-F1=66.40, R-F1=43.17, DR=1.77, lat=4.194s **MATCH**\n- k=8 con: E-F1=66.36, R-F1=43.65, DR=0, CF=0, lat=5.058s **MATCH**\n\n**Latency table (tab:beam-latency):** Paper shows Greedy unc=2.612, Greedy con=2.873, Beam-4 unc=3.446, Beam-4 con=4.013. Registry `d066_beam_sweep` has k=1 unc lat=2.494 and k=1 con lat=2.932. **MISMATCH** — latency table uses different numbers from beam sweep. These may come from a separate latency experiment; the paper cites SciERC 551 docs Qwen3-8B LoRA RTX PRO 6000 Blackwell, but d066 values for k=1 are 2.494/2.932 vs paper 2.612/2.873. This is a **discrepancy** that needs verification.\n\n**Table tab:beam-docred-998-zs** (998-doc ZS beam):\n- Qwen: DR=0, CF=4.94, E-F1=58.19, R-F1=8.72 — Registry `r14_qwen_docred_beam4_998`: DR=0, CF=4.94%, E-F1=58.19, R-F1=8.72 **MATCH**\n- Llama: DR=0, CF=1.00, E-F1=57.81, R-F1=8.83 — Registry `r14_llama_docred_beam4_998`: DR=0, CF=1%, E-F1=57.81, R-F1=8.83 **MATCH**\n\nText claim: \"Llama: CF 8.54%→1.00%, 88% reduction; R-F1 +2.6pp\" — Registry baseline notes show `baseline_ZS_greedy_CF_pct: 8.54` and `baseline_ZS_greedy_R_F1: 6.27`, and beam R-F1=8.83, so +2.56pp ≈ \"+2.6pp\". **MATCH**\n\n**Composability paragraph:** \"CF=1.18%→0%, E-F1=66.88, R-F1=43.60\" after adding beam-4 to greedy FT LoRA. Paper also claims \"Llama beam-4 k=4 achieves R-F1=46.18\" — Registry `q1_llama_lora_scierc_beam4` gives R-F1=46.11 (not 46.18). **DISCREPANCY: paper says 46.18, registry says 46.11**.\n\n**Table tab:beam-docred-lora** (LoRA greedy vs beam, DocRED 998 docs):\n- Qwen Greedy: DR=0.01, CF=0.41, E-F1=81.43, R-F1=40.56, PF=8.52 — Registry `d065_qwen_greedy_4096_r2`: DR=0, CF=0.22, PF=8.52, E-F1=81.87, R-F1=40.79. **MISMATCH**: Paper shows DR=0.01, CF=0.41, E-F1=81.43, R-F1=40.56; registry shows DR=0, CF=0.22, E-F1=81.87, R-F1=40.79. These are divergent. There may be a separate greedy LoRA DocRED 998 experiment not found.\n- Qwen Beam-4: DR=0, CF=0.01, E-F1=84.00, R-F1=44.46, PF=2.9 — Cannot find this experiment in registry under d066 (d066 swept only 200-doc subset). **UNVERIFIED**\n- Llama Greedy: DR=0.21, CF=0.21, E-F1=83.94, R-F1=43.78, PF=2.51 — **UNVERIFIED** (no direct match found)\n- Llama Beam-4: DR=0, CF=0, E-F1=85.23, R-F1=47.17, PF=1.3 — `d066_sweep_llama_beam2_s1` was 200 docs. `d066_sweep_llama_beam8_s1` shows E-F1=85.76, R-F1=51.74 on 200 docs. For 998 docs beam-4, not directly found. **UNVERIFIED**\n\n---\n\n### 3. Appendix 70B Ablation (appendix_70b_ablation.tex)\n\n**Table tab:70b-ft-ablation (SciERC, 551 docs)**\n\n| Mode | DR | R-F1 | E-F1 | CF | Paper | Registry | Status |\n|------|-----|------|------|-----|-------|----------|--------|\n| Unconstrained | 1.50 | 44.73 | 64.86 | 0 | Paper | `eval_70b_lora_scierc_unconstrained`: DR=1.5, R-F1=44.73, E-F1=64.86, CF=0 | **MATCH** |\n| Grammar | 1.50 | 44.63 | 64.82 | 0 | Paper | `eval_70b_lora_scierc_grammar_only`: DR=0.015→1.5%, R-F1=44.63, E-F1=64.82, CF=0 | **MATCH** |\n| Semantic | 0.60 | 44.73 | 64.86 | 9 (count) | Paper | `eval_70b_lora_scierc_semantic_only`: DR=0.6%, R-F1=44.73, E-F1=64.86, CF_count=9 | **MATCH** |\n| S1 | 0 | 44.53 | 64.76 | 15 | Paper | `eval_70b_lora_scierc_s1_constrained`: DR=0, R-F1=44.53, E-F1=64.76, CF_count=15 | **MATCH** |\n| S2 | 0 | 36.28 | 62.35 | 18 | Paper | `eval_70b_lora_scierc_full_s2`: DR=0, R-F1=36.28, E-F1=62.35, CF_count=18 | **MATCH** |\n| Beam4 S1 | 0 | 44.81 | 64.89 | 1 | Paper | `eval_70b_lora_scierc_beam4_s1`: DR=0, R-F1=44.81, E-F1=64.89, CF_count=1 | **MATCH** |\n\nText: \"S2 causes -8.45pp R-F1\" → 44.53-36.28=8.25pp. **DISCREPANCY: paper says -8.45pp, actual is -8.25pp**.\n\n**Table tab:70b-docred-ablation (DocRED, 998 docs)**\n\n| Mode | DR | R-F1 | E-F1 | Status |\n|------|-----|------|------|--------|\n| Unconstrained | 0.22 | 43.80 | 80.34 | `eval_70b_lora_docred_200_unconstrained`: DR=0.22, R-F1=43.80, E-F1=80.34 | **MATCH** |\n| Grammar | 0.38 | 43.96 | 80.13 | `eval_70b_lora_docred_200_grammar_only`: DR=0.38, R-F1=43.96, E-F1=80.13 | **MATCH** |\n| Semantic | 0 | 43.61 | 80.06 | `eval_70b_lora_docred_200_semantic_only`: DR=0, R-F1=43.61, E-F1=80.06 | **MATCH** |\n| S1 | 0 | 43.95 | 79.38 | `eval_70b_lora_docred_200_s1_constrained`: DR=0, R-F1=43.95, E-F1=79.38 | **MATCH** |\n| S2 | 0 | 36.45 | 84.96 | `eval_70b_lora_docred_200_full_s2`: DR=0, R-F1=36.45, E-F1=84.96 | **MATCH** |\n| Beam4 S1 | 0 | 48.14 | 85.57 | `eval_70b_lora_docred_200_beam4_s1`: DR=0, R-F1=48.14, E-F1=85.57 | **MATCH** |\n\nNote: Paper caption says \"998 docs\" but all DocRED 70B experiments in registry used 200-doc subsets. The caption says 998 but the underlying experiments are 200 docs. **CAPTION ERROR: tab:70b-docred-ablation caption claims 998 docs; actual experiments were 200-doc subsets.**\n\nText: \"S2 causes -7.50pp vs S1\" → 43.95-36.45=7.50pp. **MATCH**. Text: \"beam +4.19pp R-F1 (43.95→48.14)\" — 48.14-43.95=4.19. **MATCH**.\n\nText: \"greedy S1 fails to parse 12.5% of documents (25/200)\" — Registry PF=12.5% (25/200). **MATCH**.\n\n**Table tab:70b-docred-zs-ablation (ZS, 200-doc subset)**\n\n| Mode | DR | RV | ET | CF | R-F1 | E-F1 | Registry | Status |\n|------|-----|----|----|-----|------|------|----------|--------|\n| Unconstrained | 13.45 | 7.88 | 0 | 0 | 13.25 | 70.14 | `eval_70b_zs_docred_200_unconstrained`: DR=13.45, RV=7.88, CF=0, R-F1=13.25, E-F1=70.14 | **MATCH** |\n| Grammar | 17.03 | 0 | 0 | 0 | 13.23 | 70.12 | `eval_70b_zs_docred_200_grammar_only`: DR=17.03, RV=0, CF=0, R-F1=13.23, E-F1=70.12 | **MATCH** |\n| Semantic | 1.66 | 8.24 | 0.12 | 132 | 13.05 | 70.10 | `eval_70b_zs_docred_200_semantic_only`: DR=1.66, RV=8.24, ET=0.12, CF_count=132, R-F1=13.05, E-F1=70.10 | **MATCH** |\n| S1 | 0 | 0 | 0 | 173 | 13.25 | 70.05 | `eval_70b_zs_docred_200_full_s1`: DR=0, CF%=5.34 (not count 173). **DISCREPANCY: paper says CF=173 (count), registry shows CF%=5.34%** — 5.34% of 2637 relations = ~141, not 173. Needs reconciliation. |\n\nText: \"grammar-only DR increases +3.58pp (13.45→17.03)\" — 17.03-13.45=3.58. **MATCH**.\n\n---\n\n### 4. Appendix Quantization (appendix_quantization.tex)\n\n**Table tab:quantization**\n\n| Cell | Paper | Registry | Status |\n|------|-------|----------|--------|\n| Qwen SciERC FP16 DR | 0 | `w5_qwen_lora_scierc_constrained_eval` (full S1): DR=0 | **MATCH** |\n| Qwen SciERC FP16 R-F1 | 43.77 | Qwen FT S1 greedy SciERC (from composability text) | **MATCH** |\n| Qwen SciERC FP16 E-F1 | 67.05 | **MATCH** |\n| Qwen SciERC INT4 DR | 0 | `sf2_qwen_int4_scierc_s1`: DR=0 | **MATCH** |\n| Qwen SciERC INT4 R-F1 | 41.71 | `sf2_qwen_int4_scierc_s1`: R-F1=41.71 | **MATCH** |\n| Qwen SciERC INT4 E-F1 | 67.05 | `sf2_qwen_int4_scierc_s1`: E-F1=67.05 | **MATCH** |\n| Llama SciERC FP16 DR | 0.09 | Llama FP16 SciERC LoRA S1 DR noted in quantization text | **MATCH** |\n| Llama SciERC FP16 R-F1 | 45.47 | Llama LoRA SciERC S1 FP16 (from various experiment notes) | **MATCH** |\n| Llama SciERC INT4 DR | 0 | `sf2_llama_int4_scierc_s1`: DR=0 | **MATCH** |\n| Llama SciERC INT4 R-F1 | 43.98 | `sf2_llama_int4_scierc_s1`: R-F1=43.98 | **MATCH** |\n| Llama SciERC INT4 E-F1 | 67.54 | `sf2_llama_int4_scierc_s1`: E-F1=67.54 | **MATCH** |\n| Qwen DocRED FP16 R-F1 | 40.79 (998 docs, dagger) | `d065_qwen_greedy_4096_r2`: R-F1=40.79 | **MATCH** |\n| Qwen DocRED FP16 E-F1 | 81.87 (dagger) | `d065_qwen_greedy_4096_r2`: E-F1=81.87 | **MATCH** |\n| Qwen DocRED FP16 PF | 8.5% (dagger) | `d065_qwen_greedy_4096_r2`: PF=8.52% | **MATCH** |\n| Qwen DocRED INT4 R-F1 | 40.07 | `sf2_qwen_int4_docred_s1`: R-F1=40.07 | **MATCH** |\n| Qwen DocRED INT4 E-F1 | 74.84 | `sf2_qwen_int4_docred_s1`: E-F1=74.84 | **MATCH** |\n| Qwen DocRED INT4 PF | 18.5 | `sf2_qwen_int4_docred_s1`: PF=18.5% | **MATCH** |\n| Llama DocRED FP16 R-F1 | 47.35 | Not directly found in registry with this exact value | **UNVERIFIED** |\n| Llama DocRED FP16 E-F1 | 85.43 | Not directly found | **UNVERIFIED** |\n| Llama DocRED INT4 R-F1 | 48.04 | `sf2_llama_int4_docred_s1`: R-F1=48.04 | **MATCH** |\n| Llama DocRED INT4 E-F1 | 84.18 | `sf2_llama_int4_docred_s1`: E-F1=84.18 | **MATCH** |\n| Llama DocRED INT4 PF | 2.5 | `sf2_llama_int4_docred_s1`: PF=2.5% | **MATCH** |\n\nAll verified numbers match. Two Llama DocRED FP16 cells are unverified (no clear registry entry found for FP16 Llama DocRED LoRA S1 200-doc eval).\n\n---\n\n### 5. Appendix Full Fine-Tuning (appendix_full_ft.tex)\n\n**Table tab:full-ft**\n\n| Row | E-F1 | R-F1 | DR% | CF% | Registry | Status |\n|-----|------|------|-----|-----|----------|--------|\n| Full FT unconstrained | 64.78 | 37.89 | 2.74 | 0 | `d062_full_ft_scierc.metrics.unconstrained`: E-F1=64.78, R-F1=37.89, DR=2.74, CF=0 | **MATCH** |\n| Full FT + S1 | 64.78 | 37.89 | 0 | 1.31 | `d062_full_ft_scierc.metrics.constrained`: E-F1=64.78, R-F1=37.89, DR=0, CF=1.31 | **MATCH** |\n| LoRA unconstrained | 67.05 | 43.86 | 1.95 | 0 | Various Qwen LoRA experiments | **MATCH** |\n| LoRA + S1 | 67.05 | 43.77 | 0 | 1.18 | Consistent with d066 k=1 con S1 | **MATCH** |\n\nText: \"30 violations, Part-of 14.6%, Hyponym-of 9.6%, Evaluate-for 8.4%\" — these per-type breakdowns are not in the registry. **UNVERIFIED** (qualitative analysis not registered).\n\n---\n\n### 6. Appendix Cross-Model Zero-Shot (appendix_zs_crossmodel.tex)\n\n**Table tab:cross-model**\n\n| Row | DR | RV | ET | CF | R-F1 | Registry | Status |\n|-----|-----|----|----|-----|------|----------|--------|\n| Qwen SciERC U | 15.37 | 1.39 | 0.40 | 0.08 | 8.23 | `phase2_scierc_unconstrained`: DR=15.37, RV=1.39, ET=0.40, CF=0.08, R-F1=8.23 | **MATCH** |\n| Qwen SciERC S1 | 0.93 | 0 | 0 | 9.90 | 8.36 | `phase2_scierc_full_s1`: DR=0.93, CF=9.90, R-F1=8.36 | **MATCH** |\n| Llama SciERC U | 13.34 | 0.55 | 0 | 0.24 | 2.68 | `llama_scierc_unconstrained`: DR=13.34, RV=0.55, ET=0, CF=0.24 (6 violations = ~0.47%, not 0.24%) — **MINOR DISCREPANCY**: registry shows 6 CF violations from 1274 relations = 0.47%, paper shows 0.24. The earlier notes say \"cross_field_consistency_violations: 6\" — 6/1315 = 0.46%, not 0.24%. But some run's metrics may differ. |\n| Llama SciERC S1 | 0.08 | 0 | 0 | 6.56 | 2.54 | `llama_scierc_full_s1`: DR=0.08, CF=6.56, R-F1=2.54 | **MATCH** |\n| Mistral SciERC U | 56.94 | 0 | 1.50 | 56.87 | 3.66 | `w6_mistral_scierc_unconstrained`: DR=56.94, ET=1.5, RV=0, CF=56.87, R-F1=3.66 | **MATCH** |\n| Mistral SciERC S1 | 13.40 | 0 | 0 | 1.27 | 3.67 | `w6_mistral_scierc_constrained`: DR=13.4, CF=1.27, R-F1=3.67 | **MATCH** |\n| Qwen DocRED U | 18.46 | 29.66 | 2.48 | 0.10 | 7.74 | `phase2_docred_unconstrained`: DR=18.46, RV=29.66, ET=2.48, CF=0.10, R-F1=7.74 | **MATCH** |\n| Qwen DocRED S1 | 10.21 | 0.03 | 0 | 2.57 | 8.23 | `phase2_docred_full_s1`: DR=10.21, RV=0.03, CF=2.57, R-F1=8.23 | **MATCH** |\n| Llama DocRED U | 26.07 | 16.03 | 0.13 | 0.17 | 5.98 | `llama_docred_unconstrained`: DR=26.07, RV=16.03, ET=0.13, CF=0.17, R-F1=5.98 | **MATCH** |\n| Llama DocRED S1 | 2.55 | 0 | 0 | 12.02 | 6.27 | `llama_docred_full_s1`: DR=2.55, CF=12.02, R-F1=6.27 | **MATCH** |\n| Mistral DocRED U | 57.42 | 42.35 | 7.58 | 24.78 | 4.34 | `w6_mistral_docred_unconstrained`: DR=57.42, RV=42.35, ET=7.58, CF=24.78, R-F1=4.34 | **MATCH** |\n| Mistral DocRED S1 | 33.20 | 0 | 0 | 0.19 | 5.52 | `w6_mistral_docred_constrained`: DR=33.2, CF=0.19, R-F1=5.52 | **MATCH** |\n\nParse failures footnote: \"Llama DocRED 9.1%\" — Registry `llama_docred_unconstrained`: 68 failures / 998 docs = 6.8%. **DISCREPANCY: paper says 9.1%, registry says 6.8%**. (The S1 run had 91/998=9.1%). The footnote likely should say \"Llama DocRED S1 9.1%; unconstrained 6.8%\" but paper applies it ambiguously. If it refers to S1, it matches registry.\n\n---\n\n### 7. Appendix Downstream Analysis (appendix_downstream_analysis.tex)\n\nClaims to verify:\n\n**Table tab:lucky-violations-detail:**\n- SciERC Qwen: TP=461, Lucky=4, 0.87%, R drop=0.41pp — **NOT IN REGISTRY** (no experiment ID found for lucky violation audit)\n- SciERC Llama: TP=467, Lucky=5, 1.07%, R drop=0.51pp — **NOT IN REGISTRY**\n- DocRED Qwen: TP=5746, Lucky=1, 0.02%, R drop=0.01pp — **NOT IN REGISTRY**\n- DocRED Llama: TP=6226, Lucky=1, 0.02%, R drop=0.01pp — **NOT IN REGISTRY**\n\nNo registry experiment IDs are referenced in the tex file for these specific downstream analysis figures. These appear to be post-hoc analysis numbers computed from existing outputs but not registered as formal experiments. **ALL NUMBERS UNVERIFIED AGAINST REGISTRY.**\n\nText claims: \"97.6-100% false positives\", \"0.24% gold triples affected\", \"0.2% false negatives blocked\", \"36 residual DR violations with 39%/33%/28% decomposition\", \"irreducible floor ~3 violations\" — **NONE of these specific numbers appear in the registry**. These are analytical claims not backed by formal experiment entries.\n\n---\n\n### 8. Appendix GoLLIE Comparison (appendix_gollie_comparison.tex)\n\nThe appendix contains **no numerical table** — it is a purely qualitative discussion of the paradigm difference between GoLLIE and OntoCoDec, explicitly stating that \"direct numerical comparison is methodologically constrained\" and is left to future work. There are no numbers to cross-reference. **N/A — no numbers to verify.**\n\n---\n\n## Summary of Issues (Priority Order)\n\n**Critical mismatches requiring correction:**\n\n1. **tab:beam-docred-lora (Qwen Greedy DocRED 998)**: Paper shows DR=0.01%, CF=0.41%, E-F1=81.43, R-F1=40.56; registry `d065_qwen_greedy_4096_r2` shows DR=0%, CF=0.22%, E-F1=81.87, R-F1=40.79. These diverge significantly — paper may be using a different (earlier) experiment run not found in registry, or numbers were misreported.\n\n2. **Llama FT beam SciERC R-F1**: Paper claims 46.18; registry `q1_llama_lora_scierc_beam4` = 46.11. Small but exact value differs.\n\n3. **tab:70b-docred-ablation caption**: Claims \"998 docs\" but all underlying experiments were 200-doc subsets.\n\n4. **70B SciERC S2 R-F1 degradation**: Paper says \"−8.45pp\"; actual is 44.53−36.28 = −8.25pp.\n\n5. **tab:beam-latency latency values**: Paper greedy unc=2.612, registry d066 k=1=2.494. May come from a separate latency experiment (`p8_latency_overhead`) not checked — needs verification.\n\n6. **tab:70b-docred-zs-ablation S1 CF**: Paper says CF=173 (count); registry `eval_70b_zs_docred_200_full_s1` reports CF%=5.34% (which on ~2637 relations ≈ 141, not 173).\n\n7. **Cross-model table parse failure footnote**: \"Llama DocRED 9.1%\" — this matches the S1 run (91/998), not the unconstrained run (68/998=6.8%). Context is ambiguous.\n\n**Unverified numbers (no registry backing found):**\n- All numbers in `appendix_downstream_analysis.tex` (lucky violations table and all percentage claims)\n- Llama DocRED FP16 baseline in quantization table (R-F1=47.35, E-F1=85.43)\n- WikiEvents $n{=}20$ fine-tuning composability claim\n- Qwen/Llama beam ZS SciERC and DocRED 50-doc subset numbers (tab:beam-search rows for beam configurations)\n- Tab:beam-docred-lora Qwen Beam-4 and all Llama rows"
      }
    ],
    "totalDurationMs": 359439,
    "totalTokens": 135054,
    "totalToolUseCount": 72,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1942,
      "cache_read_input_tokens": 124756,
      "output_tokens": 8355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1942
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8355,
          "cache_read_input_tokens": 124756,
          "cache_creation_input_tokens": 1942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1942,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 23,
      "searchCount": 5,
      "bashCount": 44,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "41ab9fbd-6d5c-4493-82ff-8f64699c8b22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---


### Runtime record

_source line 1884 · 2026-05-25T19:53:45.113Z_

```json
{
  "parentUuid": "767a0ee1-fc30-451c-94e0-f020ec4528c0",
  "isSidechain": false,
  "attachment": {
    "type": "queued_command",
    "prompt": "&lt;task-notification>\n&lt;task-id>a16b2408c4cfcd2a6&lt;/task-id>\n&lt;tool-use-id>toolu_01Y8sq2Cw76Rnx2iUs5eZQ6i&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-director-8494441a/485a49b0-2f8a-4e9c-b75d-f286f7540b25/tasks/a16b2408c4cfcd2a6.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Extract appendix numbers\" completed&lt;/summary>\n&lt;result>Now I have read all 25 appendix files. Let me compile the complete numerical extraction.\n\n---\n\n## appendix_prompts.tex\n- \"96\" — number of Wikidata relation types in DocRED system prompt (line ~36)\n- \"6\" — entity types listed for DocRED (line ~35)\n\n---\n\n## appendix_related_work.tex\n- \"100×\" — speedup of XGrammar over prior CFG-constrained decoding (line ~9)\n- \"13\" — number of IE datasets UIE trains on (line ~55)\n- \"29K\" — number of entity types from Wikidata encoded in KnowCoder (line ~57)\n- \"50%\" — reduction in compilation errors by type-constrained codegen (line ~28)\n- \"98.8%\" — ODKE+ precision across 195 predicates (line ~72)\n- \"195\" — number of predicates in ODKE+ (line ~72)\n- \"10×\" — violation reduction by OntoLogX iterative re-prompting (line ~74)\n- \"29%\" — F1 improvement by constrained inference on CaRB (line ~75)\n- \"94%\" — F1 accuracy@10 achieved by RELATE on ChemProt (line ~77)\n- \"15.37%\" — fraction of generated triples with domain/range violations under unconstrained decoding (line ~83)\n- \"DR↓94% on SciERC\" — DR reduction claim (line ~85)\n- \"↓45–90% on DocRED\" — DR reduction range on DocRED (line ~85)\n- \"+0.13pp\" — F1 gain on SciERC (p=0.58) (line ~98)\n- \"p=0.58\" — p-value for SciERC F1 (line ~98)\n- \"p&lt;0.001\" — p-value for DocRED Qwen R-F1 (line ~98)\n- \"p=0.013\" — p-value for DocRED Llama R-F1 (line ~98)\n- \"7B–70B\" — model scale range evaluated (line ~108)\n- \"p≤0.013\" — significance threshold for DocRED R-F1 gains (line ~109)\n- \"15.37%→0.93%\" — DR reduction on SciERC (line ~98)\n- \"45–90%\" — DR reduction range on DocRED (line ~109)\n\n---\n\n## appendix_discussion.tex\n- \"100%\" — fraction of Qwen3-8B CF violations from registry override (line ~17)\n- \"5,882\" — Llama-3.1-8B grammar-first fallbacks on SciERC (line ~17)\n- \"10.7\" — fallbacks per document on SciERC for Llama (line ~17)\n- \"57,825\" — Llama-3.1-8B grammar-first fallbacks on DocRED (line ~17)\n- \"63.8\" — fallbacks per document on DocRED for Llama (line ~17)\n- \"2.57%\" — Qwen CF on DocRED (line ~18)\n- \"12.02%\" — Llama CF on DocRED (line ~18)\n- \"36.6%\" — token-level fallback rate on SciERC Llama (line ~28)\n- \"2.87\" — average BPE tokens for OtherScientificTerm type name (line ~28)\n- \"0.04–5.7%\" — first-token fallback rate range zero-shot (line ~28)\n- \"≤0.11%\" — fallback rate under fine-tuning (line ~28)\n- \"4.5%\" — registry-consistent fallback rate (line ~31)\n- \"36.6%\" — grammar-first fallback rate (f_gf), SciERC Llama (line ~34)\n- \"6,237 of 17,024\" — mask calls resulting in fallback on SciERC Llama (line ~34)\n- \"63.4%\" — effective semantic constraint coverage on SciERC Llama (line ~34)\n- \"46 of 54,859\" — fallback events on DocRED Qwen (line ~35)\n- \"0.08%\" — f_gf on DocRED Qwen (line ~35)\n- \"99.9%\" — effective coverage on DocRED Qwen (line ~35)\n- \"2.87\" — mask calls per type field for OtherScientificTerm (line ~36)\n- \"100%\" — effective coverage Qwen3-8B on SciERC (line ~39)\n- \"0.93% vs. Llama's 0.08%\" — residual DR comparison (line ~39, note: Qwen vs Llama reversed from main text)\n- \"24%\" — DR reduction by semantic layer without grammar layer (line ~79)\n- \"2.71%\" — CF rises to this under semantic-only ablation (line ~82)\n- \"0.08%\" — CF without semantic-only ablation (line ~82)\n- \"2.63pp\" — additional violations from structural ambiguity (line ~82)\n- \"9.90%\" — CF on SciERC zero-shot (line ~92)\n- \"12.02%\" — CF on Llama DocRED (line ~92)\n- \"0.93%\" — S1 DR on SciERC (table line ~103)\n- \"9.90%\" — S1 CF on SciERC (table line ~103)\n- \"10.83%\" — DR+CF total under S1 (table line ~103)\n- \"14.78%\" — DR under CF fallback (table line ~104)\n- \"0.04%\" — CF under CF fallback (table line ~104)\n- \"14.82%\" — DR+CF total under CF fallback (table line ~104)\n- \"36.64%\" — f_gf under CF fallback (table line ~104)\n- \"+13.85pp\" — DR increase from CF fallback (line ~106)\n- \"-9.86pp\" — CF decrease from CF fallback (line ~106)\n- \"+3.99pp\" — total violation increase from CF fallback (line ~106)\n- \"15.9×\" — DR increase multiplier (0.93%→14.78%) (line ~113)\n- \"36.64%\" — token-level fallback rate at type-bearing positions (line ~117)\n- \"0.46%\" — first-token position fallback rate (line ~117)\n- \"3 models × 2 datasets\" — scope of DR/CF inverse association (line ~121)\n- \"63.3%\" — fraction of CF violations involving Generic type on SciERC (line ~124)\n- \"9.90%→1.18%\" — CF reduction with LoRA fine-tuning (line ~127)\n- \"88%\" — relative CF reduction from LoRA (line ~127)\n- \"1.18%\" — residual CF after LoRA (line ~128)\n- \"551\" — SciERC document count (multiple occurrences)\n\n**Causal tracing table (lines 59–64):**\n- Qwen3-8B FT S1: Fallback 0/2256 (0%), DR=0\n- Qwen3-8B ZS S1: Fallback 16/3458 (0.46%), DR=16, From FB=100%\n- Llama-3.1-8B FT S1: Fallback 1/2162 (0.05%), DR=1, From FB=100%\n- Llama-3.1-8B ZS S1: Fallback 1/2630 (0.04%), DR=1, From FB=100%\n- \"18\" — total residual DR violations across four configurations (line ~70)\n- \"≤0.05%\" — fallback rate after fine-tuning (line ~71)\n\n**CF-DR trade-off table:**\n- \"0.93\" DR, \"9.90\" CF, \"10.83\" DR+CF — S1 baseline (line ~103)\n- \"14.78\" DR, \"0.04\" CF, \"14.82\" DR+CF, \"36.64\" f_gf — CF fallback (line ~104)\n\n**Bootstrap CIs table (lines 181–191):**\n- Qwen3-8B/SciERC: ΔR-F1 = −0.10pp, 95% CI [−0.30, 0.00], p=.726, d=−0.05\n- Qwen3-8B/DocRED: ΔR-F1 = −0.31pp, 95% CI [−0.69, +0.01], p=.056, d=−0.37\n- Llama-3.1-8B/SciERC: ΔR-F1 = +0.02pp, 95% CI [0.00, +0.07], p=.736, d=+0.01\n- Llama-3.1-8B/DocRED: ΔR-F1 = +0.06pp, 95% CI [−0.11, +0.25], p=.535, d=+0.07\n- Qwen3-8B/SciERC DR: Δ=−1.95, CI [−2.87, −1.11], p&lt;.001, d=−6.15\n- Qwen3-8B/DocRED DR: Δ=−0.75, CI [−1.07, −0.48], p&lt;.001, d=−7.00\n- Llama-3.1-8B/SciERC DR: Δ=−1.02, CI [−1.98, −0.29], p&lt;.001, d=−3.17\n- Llama-3.1-8B/DocRED DR: Δ=−0.29, CI [−0.53, −0.10], p&lt;.001, d=−3.02\n- \"k=4\" — comparisons for Bonferroni correction (line ~167)\n- \"α_adj=0.0125\" — adjusted alpha (line ~167)\n- \"|d|≤0.37\" — max effect size for R-F1 (line ~167)\n- \"p_B=1.00\" — Qwen3-8B/SciERC corrected p (line ~168)\n- \"p_B=0.224\" — Qwen3-8B/DocRED corrected p (line ~168)\n- \"p_B=1.00\" — Llama-3.1-8B/SciERC corrected p (line ~168)\n- \"p_B=1.00\" — Llama-3.1-8B/DocRED corrected p (line ~168)\n- \"|d|≥3.0\" — minimum DR effect size (line ~169)\n- \"all p_Bonf&lt;0.005\" — DR reduction significance (line ~169)\n- \"10,000\" — bootstrap iterations (line ~166)\n- \"seed=42\" — bootstrap seed (line ~166)\n\n**Practical significance:**\n- \"~8%\" — zero-shot relation F1 on both datasets (line ~205)\n- \"49–53%\" — supervised SOTA on SciERC (line ~206)\n- \"1–2%\" — residual DR after LoRA (line ~208)\n\n**Post-hoc filtering comparison:**\n- \"8.63 vs. 8.36\" — SciERC post-hoc vs. OntoCoDec F1 (line ~218)\n- \"9.61 vs. 8.23\" — DocRED post-hoc vs. OntoCoDec F1 (line ~218)\n- \"48.1%\" — DocRED triples discarded by post-hoc filtering (line ~221)\n- \"127\" — true positives lost in DocRED post-hoc (line ~221)\n- \"11.2%\" — fraction of correct predictions lost (line ~221)\n- \"9.46%→8.40%\" — recall drop from post-hoc filtering (line ~221)\n- \"2.47%\" — residual ET for post-hoc (line ~223)\n- \"0%\" — OntoCoDec ET (line ~223)\n\n**CF violation distribution table (lines 249–260):**\n- Generic ↔ OtherScientificTerm: 85 (34.7%)\n- Generic ↔ Material: 35 (14.3%)\n- Generic ↔ Metric: 30 (12.2%)\n- Method ↔ Task: 20 (8.2%)\n- Material ↔ Method: 17 (6.9%)\n- OtherScientificTerm ↔ Task: 12 (4.9%)\n- 10 further pairs (each ≤3.3%): 46 (18.8%)\n- Total: 245 (100.0%)\n- \"248 CF violations\" / \"245 unique entity-document pairs\" (line ~235)\n- \"63.3%\" — Generic-involving violations (line ~236)\n- \"155/245\" — count/total for Generic (line ~236)\n- \"53/162, 32.7%\" — Generic↔OtherScientificTerm on Llama SciERC (line ~239)\n- \"76.6%\" — MISC-driven Qwen DocRED CF violations (line ~239)\n- \"≤1%\" — CF rates under unconstrained decoding (line ~240)\n\n**Cascade error breakdown table (lines 289–296):**\n- Hallucinated entity: 144 (58.1%)\n- Correct type lock: 45 (18.1%)\n- True cascade error: 18 (7.3%)\n- Other/ambiguous: 41 (16.5%)\n- Total: 248 (100.0%)\n- \"2.5×\" — correct type locks more frequent than true cascade errors (line ~276)\n- \"22 CF violations, 20 documents\" — fine-tuned CF (line ~278)\n- \"0/22\" — cascade errors under fine-tuning (line ~279)\n\n**Per-relation DR elimination table (lines 324–331):**\n- Evaluate-for: κ=0.361, LoRA DR=13.13%, n=99; S1 DR=0%, n=98\n- Part-of: κ=0.417, LoRA DR=5.77%, n=52; S1 DR=0%, n=52\n- Compare: κ=0.528, LoRA DR=5.00%, n=40; S1 DR=0%, n=40\n- Conjunction: κ=0.306, LoRA DR=1.31%, n=153; S1 DR=0%, n=153\n- Feature-of: κ=0.278, LoRA DR=1.35%, n=74; S1 DR=0%, n=74\n- Used-for: κ=0.028, LoRA DR=0.16%, n=634; S1 DR=0%, n=635\n- Hyponym-of: κ=0.417, DR=0%\n\n**Fine-tuned four-way ablation table (lines 357–381):**\nSciERC Qwen3-8B:\n- Unconstrained: DR=1.95, RV=0, ET=0, CF=0, PF=0, E-F1=67.05, R-F1=43.86\n- Grammar: DR=1.90, RV=0, ET=0, CF=0, PF=0, E-F1=67.05, R-F1=43.86\n- Semantic: DR=0.60, RV=0, ET=0, CF=0.18, PF=0, E-F1=67.05, R-F1=43.69\n- S1: DR=0, RV=0, ET=0, CF=1.18, PF=0, E-F1=67.05, R-F1=43.77\n\nSciERC Llama-3.1-8B:\n- Unconstrained: DR=1.11, RV=0, ET=0, CF=0, PF=0, E-F1=67.76, R-F1=45.45\n- Grammar: DR=1.11, RV=0, ET=0, CF=0, PF=0, E-F1=67.76, R-F1=45.45\n- Semantic: DR=0.65, RV=0, ET=0, CF=0.10, PF=0, E-F1=67.76, R-F1=45.47\n- S1: DR=0.09, RV=0, ET=0, CF=0.46, PF=0, E-F1=67.76, R-F1=45.47\n\nDocRED Qwen3-8B:\n- Unconstrained: DR=0.76, RV=0.27, ET=0, CF=0.12, PF=7.11, E-F1=82.15, R-F1=40.86\n- Grammar: DR=0.61, RV=0, ET=0, CF=0.11, PF=7.01, E-F1=82.19, R-F1=40.85\n- Semantic: DR=0.19, RV=0.23, ET=0, CF=0.27, PF=7.52, E-F1=82.15, R-F1=40.85\n- S1: DR=0.01, RV=0, ET=0, CF=0.41, PF=8.52, E-F1=81.43, R-F1=40.56\n\nDocRED Llama-3.1-8B:\n- Unconstrained: DR=0.49, RV=0.15, ET=0, CF=0.08, PF=2.30, E-F1=83.93, R-F1=43.72\n- Grammar: DR=0.51, RV=0, ET=0, CF=0.12, PF=2.30, E-F1=84.04, R-F1=43.72\n- Semantic: DR=0.48, RV=0.15, ET=0, CF=0.16, PF=2.40, E-F1=84.02, R-F1=43.85\n- S1: DR=0.21, RV=0, ET=0, CF=0.21, PF=2.51, E-F1=83.94, R-F1=43.78\n\n- \"41–69%\" — semantic layer DR reduction on SciERC FT (line ~392)\n- \"2–75%\" — semantic layer DR reduction on DocRED FT (line ~392)\n- \"80 violations in 16,074 triples\" — Llama DocRED DR denominator (line ~392)\n- \"DR≤0.21%\" — near-complete elimination in all 4 FT settings (line ~393)\n- \"-0.30pp\" — max R-F1 decrease S1 vs. unconstrained (line ~394)\n\n**DocRED Zero-Shot Ablation table (lines 420–439):**\n- Unconstrained: DR=18.46, ΔDR=---, RV=29.66, ET=2.48, CF=0.10, Total=18.56, Rel.=7.74, Ent.=58.15\n- Grammar: DR=26.17, ΔDR=↑42%, RV=0.03, ET=0, CF=0.07, Total=26.24, Rel.=8.31, Ent.=59.38\n- Semantic: DR=13.84, ΔDR=↓25%, RV=29.87, ET=4.22, CF=1.05, Total=14.89, Rel.=7.70, Ent.=57.81\n- S1: DR=10.21, ΔDR=↓45%, RV=0.03, ET=0, CF=2.57, Total=12.78, Rel.=8.23, Ent.=59.37\n- \"+0.49pp\" — R-F1 bootstrap significance (p&lt;0.001) (line ~446)\n\n**Residual DR error analysis (lines 461–465):**\n- Entity type errors: 39%\n- Schema coverage gaps: 33%\n- Incorrect relation selection: 17%\n- Direction reversal: 11%\n- \"3 of 36\" — non-Llama DocRED residual violations (line ~468)\n- \"33 of 36\" — Llama DocRED residual violations (line ~469)\n- \"92%\" — Llama DocRED share of residual (line ~469)\n- \"14/33, 42%\" — entity type errors in Llama DocRED (line ~469)\n- \"36\" — total fine-tuned residual DR violations (line ~457)\n\n**Post-hoc extended table (lines 490–510):**\nZS:\n- Qwen/SciERC: Reject=16.8%, R-F1_ph=8.63, R-F1_cd=8.36, ph wins\n- Llama/SciERC: Reject=13.9%, R-F1_ph=2.71, R-F1_cd=2.54, ph wins\n- Mistral/SciERC: Reject=20.3%, R-F1_ph=3.94, R-F1_cd=3.67, ph wins\n- Qwen/DocRED: Reject=48.1%, R-F1_ph=9.61, R-F1_cd=8.23, ph wins\n- Llama/DocRED: Reject=42.2%, R-F1_ph=7.44, R-F1_cd=6.27, ph wins\n- Mistral/DocRED: Reject=73.7%, R-F1_ph=3.85, R-F1_cd=5.52, cd wins\nFT:\n- Qwen/SciERC: Reject=1.95%, R-F1_ph=43.94, R-F1_cd=43.77, ph wins\n- Llama/SciERC: Reject=1.11%, R-F1_ph=45.23, R-F1_cd=45.47, cd wins\n- Qwen/DocRED: Reject=1.03%, R-F1_ph=41.11, R-F1_cd=40.79, ph wins (note: likely 40.56 in main FT table — potential inconsistency)\n- Llama/DocRED: Reject=0.64%, R-F1_ph=43.92, R-F1_cd=43.78, cd wins\n- \"~70%\" — crossover rejection rate (line ~513)\n- \"+1.67pp\" — cd advantage at &gt;70% rejection (line ~513)\n- \"Δ≤0.55pp\" — FT convergence (line ~515)\n\n**Runtime:**\n- \"4.163 s/doc\" — SciERC unconstrained inference (line ~522)\n- \"4.710 s/doc\" — SciERC S1 constrained decoding (line ~522)\n- \"+13.1%\" — overhead (line ~522)\n- \"0.044 s\" — XGrammar compilation (line ~524)\n- \"0.33 s\" — full constraint pipeline compilation on SciERC (line ~524)\n- \"2.612 s/doc\" — fine-tuned unconstrained inference (line ~529)\n- \"2.873 s/doc\" — fine-tuned S1 constrained (line ~529)\n- \"+10.0%\" — fine-tuned overhead (line ~529)\n- \"n=551\" — document count for fine-tuned latency (line ~529)\n- \"37%\" — absolute generation time drop under FT vs. ZS (line ~530)\n\n**Fuzzy matching:**\n- \"80%\" — token overlap threshold (line ~538)\n- \"≤2\" — edit distance threshold (line ~538)\n- \"98\" — additional TPs from fuzzy matching on Mistral DocRED (line ~540)\n- \"+0.84pp\" — R-F1 from fuzzy matching (line ~540)\n- \"3.50% vs. 4.34%\" — strict vs. fuzzy R-F1 for Mistral (line ~540)\n\n**Prompt comparison table (lines 562–568):**\nSciERC Unconstrained: DR=15.4, RV=1.4, ET=0.4, CF=0.1\nSciERC Schema-informed: DR=5.8, RV=0.3, ET=0.0\nDocRED Unconstrained: DR=18.5, RV=29.7, ET=2.5, CF=0.1\nDocRED Schema-informed: DR=12.8, RV=18.4, ET=0.2, CF=0.2\n\n**WikiEvents:**\n- \"56\" — event types (line ~576)\n- \"80\" — argument roles (line ~576)\n- \"27\" — entity types (line ~576)\n- \"245\" — (event_type, role)→allowed_entity_types constraints (line ~576)\n- \"mean κ̄=0.82\" — WikiEvents role-level tightness (line ~582)\n- \"median 0.89\" — WikiEvents median κ (line ~582)\n- \"84%\" — fraction of roles with κ≥0.80 (line ~582)\n- \"4 or fewer\" — valid entity types for roles with κ≥0.80 (line ~582)\n- \"50%\" — AC rate for roles with κ≥0.90 (line ~583)\n- \"21%\" — AC rate for 0.80≤κ&lt;0.90 (line ~583)\n- \"30%\" — AC rate for loose (κ&lt;0.80) roles (line ~583)\n- \"0%\" — AC for Transportation.Vehicle→VEH (line ~584)\n- \"κ=0.963\" — tightness for Transportation.Vehicle→VEH (line ~584)\n- \"126 args, 34% AC, κ=0.59\" — Attack.Target role (line ~585)\n\n**Lucky violations table (lines 606–611):**\n- Qwen3-8B/SciERC: DR 1.95→0, Lucky=4 (0.41%), ΔRecall=−0.10, Churn=0.22%\n- Llama-8B/SciERC: DR 1.11→0.09, Lucky=5 (0.51%), ΔRecall=±0.00, Churn=0%\n- Qwen3-8B/DocRED: DR 1.03→0.01, Lucky=1 (0.01%), ΔRecall=−0.84, Churn=2.05%\n- Llama-8B/DocRED: DR 0.64→0.21, Lucky=1 (0.01%), ΔRecall=−0.10, Churn=0.86%\n- Average lucky: 0.24%, average ΔRecall=−0.26, average churn=0.78%\n\n**Trie-only baseline table (lines 642–655):**\n- Qwen3-8B LoRA: ET=0, RV=0, DR=95.5%, CF=0.09, R-F1=41.16, PF=9.1%\n- Qwen3-8B ZS: ET=0, RV=0, DR=29.3%, CF=0, R-F1=8.64, PF=0%\n- Llama-8B LoRA: ET=0, RV=0, DR=15.2%, CF=0, R-F1=19.95, PF=50.8%\n- Llama-8B ZS: ET=0, RV=0, DR=84.4%, CF=0.36, R-F1=2.90, PF=0%\nDR gaps vs S1:\n- Qwen3-8B LoRA: S1=0%, Trie=95.5%, Gap=95.5pp\n- Qwen3-8B ZS: S1=0.93%, Trie=29.3%, Gap=28.4pp\n- Llama-8B LoRA: S1=0.09%, Trie=15.2%, Gap=15.1pp\n- Llama-8B ZS: S1=0.08%, Trie=84.4%, Gap=84.3pp\n- \"83%\" — fraction of triples with entity type fields omitted under trie-only (line ~628)\n- \"0–51%\" — parse failure range for trie-only (line ~628)\n- \"15–96%\" — DR range for trie-only (line ~628)\n- \"50.8%\" — Llama LoRA parse failure (line ~629)\n- \"45.47→19.95\" — R-F1 collapse (line ~629)\n\n**vLLM verification table (lines 714–717):**\n- Grammar-Only (XGrammar): DR=14.84, RV=0, ET=0, CF=9.90, R-F1=8.23\n- vLLM guided_json: DR=15.26, RV=0, ET=0, R-F1=8.75\n- Δ: DR=+0.42, R-F1=+0.52\n- \"~15%\" — DR left unaddressed by CFG-based approaches (line ~724)\n\n**Dual-factor analysis:**\n- \"y=0.366x−0.138\" — linear fit (line ~140)\n- \"R²=0.886\" — fit quality (line ~140)\n- \"n=4\" — data points (line ~140)\n- \"F(1,2)=15.54\" — F-statistic (line ~140)\n- \"p≈0.058\" — p-value (line ~140)\n- \"7.58%\" — Mistral-7B unconstrained ET on DocRED (line ~142)\n- \"33.21%\" — Mistral residual DR on DocRED (line ~142)\n- \"&gt;5%\" — ET threshold for principled exclusion (line ~143)\n- \"0.842\" — DocRED κ̄ (line ~144)\n- \"0.333\" — SciERC κ̄ (line ~144)\n\n**Dataset-dependent F1:**\n- \"+0.49pp\" — DocRED R-F1 gain (p&lt;0.001) (line ~153)\n- \"+0.13pp\" — SciERC R-F1 gain (p=0.58) (line ~153)\n- \"29.66%\" — DocRED baseline RV (line ~154)\n- \"5,189\" — OOV predictions as false positives (line ~154)\n- \"1.39%\" — SciERC baseline RV (line ~155)\n- \"24\" — SciERC OOV predictions (line ~155)\n- \"16.03%\" — Llama DocRED baseline RV (line ~156)\n- \"+0.29pp\" — Llama DocRED R-F1 gain (line ~156)\n\n---\n\n## appendix_70b_ablation.tex\n\n**SciERC 70B table (lines 21–27):**\n- Unconstrained: DR=1.50, RV=0, ET=0, CF=0, R-F1=44.73, E-F1=64.86\n- Grammar: DR=1.50, RV=0, ET=0, CF=0, R-F1=44.63, E-F1=64.82\n- Semantic: DR=0.60, RV=0, ET=0, CF=9, R-F1=44.73, E-F1=64.86\n- S1: DR=0, RV=0, ET=0, CF=15, R-F1=44.53, E-F1=64.76\n- S2: DR=0, RV=0, ET=0, CF=18, R-F1=36.28, E-F1=62.35\n- Beam4 S1: DR=0, RV=0, ET=0, CF=1, R-F1=44.81, E-F1=64.89\n- \"+3.58pp\" — DR increase from grammar-only on DocRED ZS (line ~34)\n- \"60%\" — semantic layer DR reduction at 70B (line ~35)\n- \"−8.45pp\" — S2 R-F1 degradation vs. S1 on SciERC (line ~36)\n- \"k=4\" — optimal beam width (line ~37)\n\n**DocRED LoRA 70B table (lines 58–64):**\n- Unconstrained: DR=0.22, RV=0.57, ET=0, CF=2, R-F1=43.80, E-F1=80.34\n- Grammar: DR=0.38, RV=0, ET=0, CF=0.06%, R-F1=43.96, E-F1=80.13\n- Semantic: DR=0, RV=0.51, ET=0, CF=0.21%, R-F1=43.61, E-F1=80.06\n- S1: DR=0, RV=0, ET=0, CF=0.18%, R-F1=43.95, E-F1=79.38\n- S2: DR=0, RV=0, ET=0, CF=0.34%, R-F1=36.45, E-F1=84.96\n- Beam4 S1: DR=0, RV=0, ET=0, CF=0, R-F1=48.14, E-F1=85.57\n- PF: greedy S1=12.5% (25/200), S2=0% (0/200), beam4=0.5% (1/200) (line ~69)\n- \"+0.16pp\" — grammar DR increase (line ~73)\n- \"−7.50pp\" — S2 R-F1 degradation on DocRED (line ~75)\n- \"+4.19pp\" — R-F1 gain from beam search (43.95→48.14) (line ~77)\n- \"12.5%\" — greedy S1 parse failures (25/200) (line ~77)\n- \"0.5%\" — beam parse failures (1/200) (line ~77)\n- \"+0.28pp\" — pure beam quality gain on SciERC (line ~78)\n\n**DocRED ZS 70B table (lines 97–101):**\n- Unconstrained: DR=13.45, RV=7.88, ET=0, CF=0, R-F1=13.25, E-F1=70.14\n- Grammar: DR=17.03, RV=0, ET=0, CF=0, R-F1=13.23, E-F1=70.12\n- Semantic: DR=1.66, RV=8.24, ET=0.12, CF=132, R-F1=13.05, E-F1=70.10\n- S1: DR=0, RV=0, ET=0, CF=173, R-F1=13.25, E-F1=70.05\n- \"+3.58pp\" — grammar DR increase on DocRED ZS 70B (line ~108)\n- \"87.7%\" — semantic-only DR reduction (line ~109)\n- \"200-document subset\" — evaluation size (line ~103)\n\n---\n\n## appendix_llama_per_relation.tex\n\n**Per-relation table (lines 21–31):**\n- dissolved/demolished (P576): 73 triples, 24 violations, 32.9% DR\n- followed by (P156): 117 triples, 24 violations, 20.5% DR\n- unemployment rate (P1198): 15 triples, 3 violations, 20.0% DR\n- end time (P582): 130 triples, 21 violations, 16.2% DR\n- instance of (P31): 290 triples, 37 violations, 12.8% DR\n- product/material produced (P1056): 98 triples, 11 violations, 11.2% DR\n- location of formation (P740): 81 triples, 8 violations, 9.9% DR\n- head of state (P35): 41 triples, 3 violations, 7.3% DR\n- applies to jurisdiction (P1001): 637 triples, 45 violations, 7.1% DR\n- conflict (P607): 453 triples, 30 violations, 6.6% DR\n- \"16.03%\" — Llama baseline RV (line ~8)\n- \"29.66%\" — Qwen baseline RV (line ~8)\n- \"2.55%\" — Llama residual DR under S1 (line ~9)\n- \"418/16,368 triples\" — DR violations/total (line ~9)\n- \"10.21%\" — Qwen residual DR under S1 (line ~36)\n- \"83%\" — P1198 fallback rate (Qwen) (line ~36)\n- \"78%\" — P171 fallback rate (Qwen) (line ~36)\n- \"20.0%\" — Llama P1198 DR rate (line ~36)\n- \"2.55% vs. 10.21%\" — Llama vs. Qwen residual DR (line ~38)\n\n---\n\n## appendix_sampling_table.tex\n\n**Sampling table (lines 12–17):**\nSciERC (551):\n- Greedy: ET=0, RV=0, DR=0.93, CF=9.90, E-F1=30.98, R-F1=8.36\n- Sampling (T=0.7, p=0.9): ET=0, RV=0, DR=0.75, CF=9.90, E-F1=31.28, R-F1=7.42\nDocRED (114†):\n- Greedy: ET=0, RV=0.03, DR=10.21, CF=2.57, E-F1=59.37, R-F1=8.23\n- Sampling: ET=0, RV=0, DR=10.31, CF=12.63, E-F1=57.05, R-F1=7.92\n- \"T=0.7\" — sampling temperature (line ~7)\n- \"p=0.9\" — nucleus sampling parameter (line ~7)\n- \"114\" — DocRED sampling subset size (line ~15)\n- \"~300h\" — estimated time for full DocRED sampling (line ~19)\n\n---\n\n## appendix_beam_search.tex\n\n**Beam search table (lines 31–54):**\n- Qwen3-8B/SciERC: Greedy DR=0.93, CF=9.90, E-F1=30.98, R-F1=8.36; Beam DR=0, CF=0.53, E-F1=32.00, R-F1=8.56\n- Qwen3-8B/DocRED(50): Greedy DR=8.69, CF=2.08, E-F1=59.08, R-F1=8.33; Beam DR=0, CF=0.55, E-F1=58.64, R-F1=9.37\n- Llama/SciERC: Greedy DR=0.08, CF=6.56, E-F1=23.49, R-F1=2.54; Beam DR=0, CF=0.93, E-F1=25.04, R-F1=3.33\n- Llama/DocRED(50): Greedy DR=1.58, CF=6.85, E-F1=55.35, R-F1=6.12; Beam DR=0, CF=0.94, E-F1=55.62, R-F1=9.47\n- Mistral/SciERC: Greedy DR=13.40, CF=1.27, E-F1=27.46, R-F1=3.67; Beam DR=13.79, CF=0.57, E-F1=26.66, R-F1=4.37\n- Mistral/DocRED(50): Greedy DR=28.37, CF=0.34, E-F1=51.60, R-F1=4.19; Beam DR=21.37, CF=0.19, E-F1=51.78, R-F1=5.70\n- \"64 lines of code\" — GrammarMatcher adaptation (line ~11)\n- \"61 lines of code\" — TypeConstraintProcessor adaptation (line ~13)\n- \"~125 lines total\" — beam search adaptation (line ~14)\n- \"k=4\" — beam width (line ~17)\n- \"74%\" — CF reduction Qwen DocRED (8 → 50-doc subset) (line ~61)\n- \"86%\" — CF reduction Llama DocRED (line ~61)\n- \"+3.4pp\" — Llama DocRED R-F1 gain (line ~62)\n- \"55%\" — Mistral SciERC CF relative reduction (line ~66)\n- \"+0.7pp\" — Mistral SciERC R-F1 improvement (line ~66)\n- \"25%\" — Mistral DocRED DR relative reduction (line ~67)\n\n**Beam ablation table (lines 82–86):**\n- k=1: DR=0.93, CF=9.90, E-F1=30.98, R-F1=8.36\n- k=2: DR=0.35, CF=4.12, E-F1=31.54, R-F1=8.75\n- k=4: DR=0, CF=0.53, E-F1=32.00, R-F1=8.56\n- k=8: DR=0, CF=0.08, E-F1=32.18, R-F1=8.39\n- \"2 residual violations\" — at k=8 (line ~91)\n\n**Beam width-latency Pareto (LoRA) table (lines 116–131):**\n- k=1 unc: E-F1=66.88, R-F1=42.95, DR=2.11, CF=0, Lat=2.494s, Rel=1.00×\n- k=1 con: E-F1=66.88, R-F1=42.95, DR=0, CF=0.50, Lat=2.932s, Rel=1.18×\n- k=2 unc: E-F1=67.79, R-F1=44.75, DR=1.54, CF=0, Lat=2.954s, Rel=1.18×\n- k=2 con (Pareto optimal): E-F1=67.71, R-F1=44.60, DR=0, CF=0.11, Lat=3.463s, Rel=1.39×\n- k=4 unc: E-F1=67.49, R-F1=43.72, DR=1.89, CF=0, Lat=3.485s, Rel=1.40×\n- k=4 con: E-F1=67.22, R-F1=43.60, DR=0, CF=0, Lat=4.069s, Rel=1.63×\n- k=8 unc: E-F1=66.40, R-F1=43.17, DR=1.77, CF=0, Lat=4.194s, Rel=1.68×\n- k=8 con: E-F1=66.36, R-F1=43.65, DR=0, CF=0, Lat=5.058s, Rel=2.03×\n\n**LoRA + beam composability:**\n- \"1.18%→0%\" — CF elimination with beam k=4 on SciERC LoRA (line ~137)\n- R-F1=43.60, E-F1=66.88 — Qwen LoRA beam-4 SciERC (line ~137)\n- \"0% across all four metrics\" — zero-violation result (line ~138)\n- \"R-F1=46.18\" — Llama LoRA beam-4 SciERC (line ~138)\n\n**Full DocRED 998-doc zero-shot beam (lines 155–157):**\n- Qwen3-8B: ET=0, RV=0, DR=0, CF=4.94, E-F1=58.19, R-F1=8.72\n- Llama-3.1-8B: ET=0, RV=0, DR=0, CF=1.00, E-F1=57.81, R-F1=8.83\n- \"8.54%→1.00%, 88% reduction\" — Llama CF improvement (line ~143)\n- \"+2.6pp\" — Llama R-F1 gain (line ~143)\n\n**DocRED LoRA beam table (lines 175–183):**\n- Qwen3-8B Greedy: DR=0.01, CF=0.41, E-F1=81.43, R-F1=40.56, PF=8.52\n- Qwen3-8B Beam-4: DR=0, CF=0.01, E-F1=84.00, R-F1=44.46, PF=2.9\n- Llama-3.1-8B Greedy: DR=0.21, CF=0.21, E-F1=83.94, R-F1=43.78, PF=2.51\n- Llama-3.1-8B Beam-4: DR=0, CF=0, E-F1=85.23, R-F1=47.17, PF=1.3\n- \"1.3% to 2.9%\" — LoRA beam-4 parse failure range (line ~162)\n\n**Beam latency table (lines 199–204):**\n- Greedy unconstrained: 2.612 s/doc, 1.00×\n- Greedy constrained (S1): 2.873 s/doc, 1.10×\n- Beam-4 unconstrained: 3.446 s/doc, 1.32×\n- Beam-4 constrained (S1): 4.013 s/doc, 1.54×\n- \"32%\" — beam search latency overhead (line ~210)\n- \"10%→17%\" — constraint overhead increase greedy→beam (line ~210)\n- \"&lt;1 MB\" — per-beam entity registry memory at k=8 (line ~211)\n- \"100% skip rate\" — type-consensus constraint on 551 SciERC/50 DocRED (line ~216)\n- \"0/551\" — SciERC candidates changed by TCR with beam (line ~220)\n\n---\n\n## appendix_reproducibility.tex\n\n**LoRA hyperparameters:**\n- \"r=16\" — rank (line ~5)\n- \"α=32\" — alpha (line ~5)\n- \"dropout 0.05\" — dropout rate (line ~5)\n- \"lr 2×10⁻⁴\" — learning rate (line ~6)\n- \"warmup ratio 0.1\" — warmup (line ~6)\n- \"effective batch size 16\" — batch size (line ~6)\n- \"3 epochs\" — training epochs (line ~6)\n- \"SciERC: 1,762 examples (260 dev), 333 steps\" (line ~7)\n- \"DocRED: 3,053 examples (998 dev), 573 steps\" (line ~7)\n- \"2,048\" — max sequence length SciERC (line ~8)\n- \"4,096\" — max sequence length DocRED (line ~8)\n- \"seed 42\" — random seed (line ~9)\n- \"98 GB VRAM\" — GPU memory (line ~12)\n- \"~11 minutes\" — SciERC fine-tuning time (line ~13)\n- \"~1.5 hours\" — DocRED fine-tuning time (line ~13)\n- \"PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13\" — software versions (line ~14)\n- \"+13.1%\" — ZS S1 overhead on SciERC (line ~18)\n- \"+10.0%\" — FT S1 overhead on SciERC (line ~18)\n- \"seeds 42, 123, 456\" — seeds tested (line ~25)\n\n**Seed variance table (lines 42–45):**\n- Qwen3-8B Unc: E-F1=66.94±0.08, R-F1=43.25±0.43, DR=2.06±0.08\n- Qwen3-8B Con: E-F1=66.94±0.08, R-F1=43.22±0.39, DR=0.00±0.00\n- Llama-3.1-8B Unc: E-F1=67.99±0.16, R-F1=45.38±0.05, DR=1.04±0.05\n- Llama-3.1-8B Con: E-F1=67.99±0.16, R-F1=45.40±0.05, DR=0.03±0.04\n- \"σ(E-F1)≤0.16pp\" (line ~28)\n- \"σ(R-F1)≤0.43pp\" (line ~28)\n- \"σ(DR%)≤0.08pp\" (line ~28)\n- \"−2.06pp (Qwen), −1.01pp (Llama)\" — DR reduction vs. variance (line ~29)\n- \"&gt;12×\" — signal-to-noise ratio (line ~29)\n- \"5,000\" — bootstrap resamples for 200-doc justification (line ~58)\n- \"±3.3 points\" — 95% CI for 200-doc R-F1 (line ~59)\n- \"±0.45pp\" — 200-doc DR margin of error (line ~59)\n- \"15.0%\" — unconstrained DR for ZS power analysis (line ~60)\n- \"Cohen's h=0.80\" — effect size for ZS power (line ~60)\n- \"100% power\" — ZS 200-doc power (line ~60)\n- \"&lt;0.5%\" — FT violation rate for fine-tuned power (line ~60)\n- \"94.9%\" — fraction of 200-doc subsamples correctly identifying DR direction (line ~60)\n\n---\n\n## appendix_power_analysis.tex\n\n**Power analysis table (lines 15–20):**\n- SciERC: n=551, 95% CI=±1.8pp, MDE=1.2pp\n- DocRED: n=998, 95% CI=±0.8pp, MDE=0.5pp\n- DocRED (70B): n=200, 95% CI=±3.3pp, MDE=2.1pp\n- WikiEvents: n=20, 95% CI=±3.0pp, MDE=2.0pp\n- \"≥1,000 bootstrap resamples\" (line ~7)\n- \"80% power, α=0.05\" — test parameters (line ~7)\n- \"ρ=0.9\" — assumed correlation (line ~7)\n- \"8.8–38.3%\" — WikiEvents RoV before constraints (line ~30)\n- \"0%\" — WikiEvents RoV after constraints (line ~30)\n- \"[0%,0%]\" — constrained bootstrap CI (line ~30)\n- \"[2.4%,15.4%]\" and \"[25.4%,46.7%]\" — unconstrained CIs (line ~30)\n- \"power≈1.0\" — power for violation elimination (line ~30)\n- \"n=20\" — WikiEvents test size (line ~29)\n- \"n=551, n=998\" — SciERC/DocRED CI evaluation sizes (line ~31)\n- \"≤1.8pp\" — CI bound (line ~31)\n\n---\n\n## appendix_doc_length.tex\n\n**SciERC doc length table (lines 16–23):**\n- Short (196 docs): Uncon. ET=1, RV=5, DR=57, CF=0, Total=63, E-F1=32.4, R-F1=8.9; Const. ET=0, RV=0, DR=5, CF=5, Total=10, E-F1=32.4, R-F1=8.9\n- Medium (180 docs): Uncon. ET=6, RV=9, DR=104, CF=0, Total=119, E-F1=27.8, R-F1=6.7; Const. ET=0, RV=0, DR=7, CF=15, Total=22, E-F1=27.8, R-F1=6.7\n- Long (175 docs): Uncon. ET=3, RV=10, DR=104, CF=1, Total=118, E-F1=29.9, R-F1=7.0; Const. ET=0, RV=0, DR=4, CF=20, Total=24, E-F1=30.0, R-F1=7.3\n- \"≤19 words\" — short bin boundary (line ~9)\n- \"≤27 words\" — medium bin boundary (line ~9)\n- \"&gt;27 words\" — long bin boundary (line ~9)\n\n**DocRED doc length table (lines 37–45):**\n- Short (336 docs): Uncon. ET=177, RV=1238, DR=1021, CF=9, Total=2445, E-F1=61.1, R-F1=9.3; Const. ET=0, RV=0, DR=495, CF=138, Total=633, E-F1=62.6, R-F1=9.6\n- Medium (332 docs): Uncon. ET=147, RV=1742, DR=1047, CF=5, Total=2941, E-F1=59.3, R-F1=7.9; Const. ET=0, RV=5, DR=544, CF=180, Total=729, E-F1=60.7, R-F1=8.5\n- Long (330 docs): Uncon. ET=176, RV=2209, DR=1162, CF=3, Total=3550, E-F1=53.9, R-F1=5.6; Const. ET=0, RV=0, DR=731, CF=200, Total=931, E-F1=54.8, R-F1=5.8\n- \"≤160 words\" — short bin DocRED (line ~31)\n- \"≤208 words\" — medium bin DocRED (line ~31)\n- \"&gt;208 words\" — long bin DocRED (line ~31)\n\n**Violation reduction table (lines 62–64):**\n- SciERC Short: 63→10, 84.1% reduction\n- SciERC Medium: 119→22, 81.5% reduction\n- SciERC Long: 118→24, 79.7% reduction\n- DocRED Short: 2445→633, 74.1% reduction\n- DocRED Medium: 2941→729, 75.2% reduction\n- DocRED Long: 3550→931, 73.8% reduction\n- \"80–84%\" — SciERC reduction range (line ~69)\n- \"74–75%\" — DocRED reduction range (line ~69)\n- \"+0.9–1.5 E-F1\" — DocRED E-F1 improvement (line ~72)\n- \"+0.2–0.6 R-F1\" — DocRED R-F1 improvement (line ~72)\n\n---\n\n## appendix_prompt_sensitivity.tex\n\n**Prompt sensitivity table (lines 17–41):**\nQwen3-8B:\n- Default Unconstrained: ET=0.40, RV=1.39, DR=15.37, E-F1=31.01, R-F1=8.23\n- Default Constrained: ET=0, RV=0, DR=0.93, ΔDR=94.0%, E-F1=30.98, R-F1=8.36\n- Minimal Unconstrained: ET=0.58, RV=1.16, DR=16.91, E-F1=31.98, R-F1=7.91\n- Minimal Constrained: ET=0, RV=0, DR=0.92, ΔDR=94.6%, E-F1=31.99, R-F1=7.85\n- Detailed Unconstrained: ET=0.22, RV=0.45, DR=11.07, E-F1=33.55, R-F1=10.48\n- Detailed Constrained: ET=0, RV=0, DR=0.64, ΔDR=94.2%, E-F1=33.56, R-F1=10.48\n\nLlama-3.1-70B (AWQ INT4):\n- Default Unconstrained: ET=0, RV=0.61, DR=6.41, E-F1=35.22, R-F1=11.23\n- Default Constrained: ET=0, RV=0, DR=0, ΔDR=100%, E-F1=35.19, R-F1=11.24\n- Minimal Unconstrained: ET=0.27, RV=5.88, DR=0.22, E-F1=37.51, R-F1=13.42\n- Minimal Constrained: ET=0, RV=0, DR=0, ΔDR=100%, E-F1=37.22, R-F1=11.35\n- Detailed Unconstrained: ET=0, RV=0.26, DR=4.57, E-F1=40.42, R-F1=11.12\n- Detailed Constrained: ET=0, RV=0, DR=0, ΔDR=100%, E-F1=40.35, R-F1=11.16\n\n- \"94.0%–94.6%\" — 8B ΔDR range across prompts (line ~45)\n- \"0.3pp\" — standard deviation across prompts (line ~45)\n- \"0.13pp max\" — R-F1 shift (line ~45)\n- \"11.1%–16.9%\" — 8B baseline DR range (line ~49)\n- \"0.22%–6.41%\" — 70B baseline DR range (line ~49)\n- \"0.62%–3.50%\" — CF introduced at 70B (line ~47)\n- \"0.62% and 0.75%\" — LoRA 70B CF under Minimal/Detailed prompts (line ~53)\n\n---\n\n## appendix_case_studies.tex\n\n**Error analysis (lines 148–177):**\n- \"514 FN, 668 FP, 21 CF\" — LoRA S1 SciERC errors (line ~148)\n- \"460 TP\" — true positives (line ~148)\n- \"R-F1=43.77\" — LoRA S1 SciERC R-F1 (line ~148)\n- \"1 of 514 (0.2%)\" — constraint-blocked false negatives (line ~177)\n- \"56%\" — Used-for fraction of all SciERC relations (line ~163)\n- \"DR≤0.21%\" — constraint enforcement leaves type-invalid outputs at this rate (line ~177)\n\n---\n\n## appendix_downstream_analysis.tex\n\n**Lucky violations detail table (lines 13–18):**\n- SciERC/Qwen-LoRA: TP=461, Lucky=4, %TP=0.87%, R drop=0.41pp\n- SciERC/Llama-LoRA: TP=467, Lucky=5, %TP=1.07%, R drop=0.51pp\n- DocRED/Qwen-LoRA: TP=5746, Lucky=1, %TP=0.02%, R drop=0.01pp\n- DocRED/Llama-LoRA: TP=6226, Lucky=1, %TP=0.02%, R drop=0.01pp\n- \"1.07%\" — max lucky violation fraction (5/467) (line ~24)\n- \"0.02%\" — min lucky violation fraction (DocRED) (line ~24)\n- \"0.51pp\" — max recall drop (line ~25)\n- \"164\" — schema-violating predictions eliminated on Qwen DocRED (line ~26)\n- \"1\" — correct predictions removed (line ~26)\n- \"163\" — false positive predictions removed (line ~26)\n\n---\n\n## appendix_scalability.tex\n\n**Scalability table (lines 12–15):**\n- Small (SciERC): 6 types, 7 relations, compile=0.33s, overhead=1.02×\n- Medium (DocRED): 6 types, 96 relations, compile=0.32s, overhead=1.03×\n- Large (synth.): 100 types, 500 relations, compile=0.35s, overhead=1.03×\n- XLarge (synth.): 200 types, 1,000 relations, compile=0.42s, overhead=1.03×\n- \"0.32s to 0.42s\" — compilation range (7→1,000 relations) (line ~22)\n- \"~0.044s\" — XGrammar automaton compilation (line ~22)\n- \"0.4ms to 17ms\" — semantic constraint compilation range (line ~22)\n- \"2–3%\" — constant inference overhead (line ~23)\n- \"~200\" — entity type limit before prefix collisions (line ~24)\n- \"10 documents\" — measurement sample per scale (caption line ~17)\n\n---\n\n## appendix_full_ft.tex\n\n**Full FT table (lines 12–17):**\n- Full FT unconstrained: E-F1=64.78, R-F1=37.89, DR=2.74%, CF=0%\n- Full FT + S1: E-F1=64.78, R-F1=37.89, DR=0%, CF=1.31%\n- LoRA unconstrained: E-F1=67.05, R-F1=43.86, DR=1.95%, CF=0%\n- LoRA + S1: E-F1=67.05, R-F1=43.77, DR=0%, CF=1.18%\n- \"30 triples\" — full FT DR violations (line ~24)\n- \"Part-of: 14.6%, Hyponym-of: 9.6%, Evaluate-for: 8.4%\" — violation distribution by relation (line ~24)\n- \"lr=2×10⁻⁴\" — learning rate (line ~4)\n- \"3 epochs, seed 42\" — training config (line ~4)\n- \"0%→1.31%\" — CF increase (line ~24)\n\n---\n\n## appendix_tcr.tex\n\n**TCR SciERC table (lines 26–33):**\nZero-shot:\n- Qwen: CF pre=9.75%, post=0%, DR pre=0.93%, post=1.21%, ΔE-F1=−1.29pp, Fund.=2.04%\n- Llama: CF pre=6.40%, post=0%, DR pre=0.08%, post=0.30%, ΔE-F1=−1.78pp, Fund.=1.85%\n- Mistral: CF pre=0.67%, post=0%, DR pre=13.36%, post=12.87%, ΔE-F1=+0.05pp, Fund.=0%\nLoRA:\n- Qwen: CF pre=1.19%, post=0%, DR pre=0%, post=0%, ΔE-F1=−0.75pp, Fund.=0%\n- Llama: CF pre=0.46%, post=0%, DR pre=0.09%, post=0.09%, ΔE-F1=−0.18pp, Fund.=0%\n- \"κ̄=0.333\" — SciERC (line ~35)\n- \"≤0.28pp\" — max DR increase from TCR on SciERC (line ~39)\n- \"0–2%\" — fundamental conflict rate SciERC (line ~39)\n\n**TCR DocRED table (lines 56–65):**\nZero-shot:\n- Qwen: CF pre=13.11%, post=0%, DR pre=10.21%, post=11.74%, ΔE-F1=−3.44pp, Fund.=13.52%\n- Llama: CF pre=23.71%, post=0%, DR pre=2.55%, post=11.93%, ΔE-F1=−5.21pp, Fund.=22.78%\n- 70B: CF pre=11.61%, post=0%, DR pre=0%, post=4.20%, ΔE-F1=−5.98pp, Fund.=18.26%\nLoRA:\n- Qwen: CF pre=0.42%, post=0%, DR pre=0.01%, post=0.14%, ΔE-F1=−0.16pp, Fund.=12.16%\n- Llama: CF pre=0.36%, post=0%, DR pre=0.21%, post=0.20%, ΔE-F1=−0.17pp, Fund.=11.59%\n- \"κ̄=0.842\" — DocRED (line ~67)\n- \"+9.38pp\" — max DR regression from Llama TCR (line ~67)\n- \"−5.98pp\" — max E-F1 drop from 70B TCR (line ~67)\n- \"12–23%\" — fundamental conflict rates DocRED (line ~67)\n- \"2.55%→11.93%\" — Llama DR regression (line ~78)\n- \"0%→4.20%\" — 70B DR regression (line ~78)\n- \"0.36–0.42%\" — LoRA baseline CF on DocRED (line ~79)\n- \"1.39×\" — beam search latency (line ~83)\n\n---\n\n## appendix_kappa_case_study.tex\n\n**Kappa case study table (lines 14–28):**\nHigh DR:\n- basin country (DocRED): κ=0.97, DR=74.6%, n=63\n- product produced (DocRED): κ=0.94, DR=67.2%, n=61\n- participant of (DocRED): κ=0.81, DR=58.6%, n=326\n- Compare (SciERC): κ=0.53, DR=42.4%, n=66\n- Feature-of (SciERC): κ=0.28, DR=33.5%, n=486\nHigh κ, zero violations:\n- lyrics by (DocRED): κ=0.94, DR=0.0%, n=9\n- place of birth (DocRED): κ=0.92, DR=0.0%, n=157\n- place of death (DocRED): κ=0.89, DR=0.0%, n=60\n- subsidiary (DocRED): κ=0.86, DR=0.0%, n=5\n- father (DocRED): κ=0.81, DR=0.0%, n=69\n- \"&gt;50%\" — DR for confusable-type relations (line ~36)\n\n---\n\n## appendix_high_kappa_analysis.tex\n\n**Schema ambiguity table (lines 26–47):**\nSciERC:\n- Hyponym-of: α=0.83, |P_r|=21, Gold=298, Gold%=9.3%\n- Part-of: α=0.83, |P_r|=21, Gold=179, Gold%=5.6%\n- Compare: α=0.82, |P_r|=17, Gold=166, Gold%=5.2%\n- Conjunction: α=0.77, |P_r|=25, Gold=400, Gold%=12.4%\n- Feature-of: α=0.76, |P_r|=26, Gold=173, Gold%=5.4%\n- Evaluate-for: α=0.71, |P_r|=23, Gold=313, Gold%=9.7%\n- Used-for: α=0.67, |P_r|=35, Gold=1,690, Gold%=52.5%\nDocRED (high α, 12 of 96 relations):\n- sister city (P190): α=0.42, |P_r|=1, Gold=4, Gold%=0.01%\n- basin country (P205): α=0.42, |P_r|=1, Gold=85, Gold%=0.22%\n- mouth of watercourse (P403): α=0.42, |P_r|=1, Gold=95, Gold%=0.25%\n- separated from (P807): α=0.41, |P_r|=2, Gold=2, Gold%=0.01%\n- replaces (P1365): α=0.39, |P_r|=4, Gold=18, Gold%=0.05%\n- capital of (P1376): α=0.37, |P_r|=3, Gold=76, Gold%=0.20%\n- place of birth (P19): α=0.37, |P_r|=3, Gold=511, Gold%=1.34%\n- operator (P137): α=0.36, |P_r|=7, Gold=95, Gold%=0.25%\n- military branch (P241): α=0.36, |P_r|=5, Gold=108, Gold%=0.28%\n- production company (P272): α=0.36, |P_r|=5, Gold=82, Gold%=0.21%\n- place of death (P20): α=0.36, |P_r|=4, Gold=203, Gold%=0.53%\n- location (P276): α=0.36, |P_r|=5, Gold=172, Gold%=0.45%\n- \"3.8%\" — fraction of gold triples in high-α DocRED relations (line ~19)\n- \"36\" — type pair slots (6²) (line ~75)\n- \"7 relations\" — SciERC total (line ~75)\n- \"α≥0.36\" — threshold (line ~18)\n- \"12 relations\" — DocRED high-α count (line ~34)\n- \"(Method, Method)\" — valid for all 7 SciERC relations; α=1.0 (line ~76)\n\n**DR by ambiguity table (lines 62–70):**\nLlama-3.1-8B:\n- High-α (12 rels): Unconstrained DR=43.8%, n=861; S1 DR=3.2%, n=1,043\n- Low-α (84 rels): Unconstrained DR=29.9%, n=12,809; S1 DR=2.5%, n=15,325\nQwen3-8B:\n- High-α (12 rels): Unconstrained DR=31.9%, n=718; S1 DR=20.0%, n=1,119\n- Low-α (84 rels): Unconstrained DR=21.2%, n=10,898; S1 DR=9.5%, n=16,217\n- \"2×\" — gap Qwen retains high vs. low α under S1 (line ~81)\n- \"2.55%→2.51% for Llama\" — exclusion analysis result (line ~82)\n- \"10.21%→9.53% for Qwen\" — exclusion analysis result (line ~82)\n- \"15.4%→0.9% (Qwen), 13.3%→0.08% (Llama)\" — SciERC DR reduction (line ~83)\n\n---\n\n## appendix_order_invariance.tex\n- \"551\" — SciERC documents (line ~6)\n- No other numerical data; purely qualitative result (byte-identical outputs)\n\n---\n\n## appendix_pumping_lemma.tex\n- \"6 entity types, 20+ entities\" → \"exceeds 10¹⁵ states\" — DFA state count (line ~64)\n- \"O(|T|^|E|)\" — DFA state complexity (line ~64)\n\n---\n\n## appendix_wikievents_pilot.tex\n\n**WikiEvents table (lines 32–44):**\nQwen3-8B:\n- Unconstrained: EV=24.0%, RoV=74.9%, AC=0.3%, CF=0, Trig.=11.8, Ent.=0\n- Grammar: EV=0%, RoV=76.1%, AC=8.2%, CF=---\n- S1: EV=0%, RoV=0%, AC=2.1%, CF=21.1%, Trig.=13.4, Ent.=14.1\nLlama-3.1-8B:\n- Unconstrained: EV=10.5%, RoV=88.8%, AC=0.1%, CF=0, Trig.=5.7, Ent.=0\n- Grammar: EV=0%, RoV=77.0%, AC=8.8%, CF=---\n- S1: EV=0%, RoV=0%, AC=3.8%, CF=17.2%, Trig.=7.5, Ent.=17.6\nMistral-7B:\n- Unconstrained: EV=37.3%, RoV=63.9%, AC=0%, CF=0, Trig.=2.4, Ent.=0\n- Grammar: EV=0%, RoV=64.0%, AC=13.8%, CF=---\n- S1: EV=0%, RoV=0%, AC=1.3%, CF=14.9%, Trig.=3.9, Ent.=11.7\n- \"n=246 documents\" — WikiEvents ZS evaluation (caption line ~47)\n- \"EV+RoV&gt;85%\" — combined vocabulary violations (line ~55)\n- \"entity F1=0\" — unconstrained baseline (line ~55)\n- \"8–14%\" — grammar-only AC rate range (line ~57)\n- \"64–77%\" — grammar-only residual RoV range (line ~57)\n- \"1.3–3.8%\" — residual AC range under S1 (line ~58)\n- \"15–21%\" — CF range under S1 (line ~58)\n- \"0%→12–18%\" — entity F1 gain (line ~59)\n- \"+1.5–1.8pp\" — trigger F1 gain (line ~59)\n- \"n=20\" — WikiEvents FT test split (line ~62)\n- \"194/20/20\" — train/dev/test split (line ~62)\n- \"Qwen 38.31%→0%\" — LoRA RoV elimination (line ~63)\n- \"Llama 8.8%→0%\" — LoRA RoV elimination (line ~63)\n- \"≤0.8%\" — LoRA AC rate (line ~63)\n- \"±1.1pp\" — argument F1 range (line ~63)\n- \"−5.4/−0.6pp\" — trigger F1 shifts (line ~63)\n- \"0.77–1.18%\" — CF under FT (line ~64)\n- \"Arg-F1 std/mean&gt;0.5\" — high per-document variance (line ~64)\n- \"MDE≈±5.0pp\" — WikiEvents FT MDE note (caption line ~50)\n\n---\n\n## appendix_zs_crossmodel.tex\n\n**Cross-model table (lines 23–42):**\nSciERC:\n- Qwen (U): DR=15.37, RV=1.39, ET=0.40, CF=0.08, R-F1=8.23\n- Qwen (S1): DR=0.93, RV=0, ET=0, CF=9.90, R-F1=8.36\n- Llama (U): DR=13.34, RV=0.55, ET=0, CF=0.24, R-F1=2.68\n- Llama (S1): DR=0.08, RV=0, ET=0, CF=6.56, R-F1=2.54\n- Mistral (U): DR=56.94, RV=0, ET=1.50, CF=56.87†, R-F1=3.66\n- Mistral (S1): DR=13.40, RV=0, ET=0, CF=1.27, R-F1=3.67\nDocRED:\n- Qwen (U): DR=18.46, RV=29.66, ET=2.48, CF=0.10, R-F1=7.74\n- Qwen (S1): DR=10.21, RV=0.03, ET=0, CF=2.57, R-F1=8.23\n- Llama (U): DR=26.07, RV=16.03, ET=0.13, CF=0.17, R-F1=5.98\n- Llama (S1): DR=2.55, RV=0, ET=0, CF=12.02, R-F1=6.27\n- Mistral (U): DR=57.42, RV=42.35, ET=7.58, CF=24.78, R-F1=4.34\n- Mistral (S1): DR=33.20, RV=0, ET=0, CF=0.19, R-F1=5.52\n- \"Llama DocRED 9.1%\" — parse failure rate (line ~45)\n- \"≤1.1%\" — other parse failure rates (line ~45)\n- \"76–99% on SciERC\" — DR reduction range (line ~53)\n- \"42–90% on DocRED\" — DR reduction range (line ~53)\n- \"5/6 settings\" — R-F1 improvements (line ~53)\n- \"12.02%\" — max CF introduced (line ~54)\n- \"56.87%→1.27%\" — Mistral CF reduction (line ~54)\n- \"15–74%\" — post-hoc rejection rates (line ~55)\n- \"14×\" — DocRED scale relative to SciERC (line ~59)\n\n---\n\n## appendix_quantization.tex\n\n**Quantization table (lines 20–29):**\nSciERC (551 docs):\n- Qwen3-8B FP16: DR=0, R-F1=43.77, E-F1=67.05\n- Qwen3-8B INT4: DR=0, R-F1=41.71, E-F1=67.05, Δ R-F1=−2.06\n- Llama-3.1-8B FP16: DR=0.09, R-F1=45.47, E-F1=67.76\n- Llama-3.1-8B INT4: DR=0, R-F1=43.98, E-F1=67.54, ΔDR=−0.09, ΔR-F1=−1.49, ΔE-F1=−0.22\nDocRED (200 docs):\n- Qwen3-8B FP16†: DR=0, R-F1=40.79†, E-F1=81.87†, PF=8.5%†\n- Qwen3-8B INT4: DR=0, R-F1=40.07, E-F1=74.84, ΔR-F1=−0.72, ΔE-F1=−7.03‡, PF=18.5%\n- Llama-3.1-8B FP16: DR=0, R-F1=47.35, E-F1=85.43, PF=2.0%\n- Llama-3.1-8B INT4: DR=0, R-F1=48.04, E-F1=84.18, ΔR-F1=+0.69, ΔE-F1=−1.25, PF=2.5%\n- \"−2.06 to +0.69pp\" — R-F1 change range (line ~39)\n- \"18.5% vs. 8.5%\" — Qwen INT4 vs FP16 parse failures (line ~40)\n- \"−7.03pp\" — Qwen DocRED E-F1 gap (line ~40)\n- \"†Qwen DocRED FP16 evaluated on 998 docs\" (note line ~33)\n\n---\n\n## appendix_gollie_comparison.tex\nNo numerical data (qualitative comparison only)\n\n---\n\n## appendix_ai_assistants.tex\nNo numerical data\n\n---\n\n**Summary of key numbers by category for cross-reference audit:**\n\nKey numbers appearing in multiple places (cross-reference candidates):\n- \"551\" — SciERC document count (reproducibility, sampling, beam, causal tracing, fallback coverage, CF tables, error analysis, doc length, prompt sensitivity, order invariance, seed variance, scalability, quantization)\n- \"998\" — DocRED document count (reproducibility, power analysis, DocRED ablation, beam, TCR)\n- \"15.37%\" — SciERC baseline DR (related work, discussion, prompt sensitivity, cross-model table)\n- \"0.93%\" — SciERC Qwen S1 DR (sampling, beam, causal tracing, CF-DR tradeoff, bootstrap table)\n- \"10.21%\" — DocRED Qwen S1 DR (sampling, Llama per-relation, TCR, DocRED ablation, cross-model)\n- \"94%\" — SciERC DR reduction (related work, discussion, prompt sensitivity)\n- \"29.66%\" — DocRED baseline RV (discussion, DocRED ablation, cross-model)\n- \"18.46%\" — DocRED baseline DR (discussion, DocRED ablation, cross-model)\n- \"8.36\" — SciERC Qwen ZS R-F1 (sampling, beam ablation, beam pareto k=1, vLLM table, prompt sensitivity)\n- \"8.23\" — DocRED Qwen ZS R-F1 (sampling, DocRED ablation, cross-model, vLLM)\n- \"43.77\" — SciERC Qwen LoRA+S1 R-F1 (FT ablation, full FT, quantization, error analysis, beam composability)\n- \"67.05\" — SciERC Qwen LoRA E-F1 (FT ablation, full FT, quantization, beam composability)\n- \"κ̄=0.333\" (SciERC) and \"κ̄=0.842\" (DocRED) — appear in dual-factor, TCR, Llama per-relation\n- \"+0.49pp p&lt;0.001\" — DocRED R-F1 gain (discussion, DocRED ablation, cross-model)\n- \"2.87 BPE tokens\" — OtherScientificTerm tokenization (discussion, twice)\n- \"seed=42\" — reproducibility, bootstrap, full FT, beam pareto\n- \"10,000 bootstrap iterations\" — discussion (bootstrap CI), reproducibility\n\n**Potential inconsistency flagged:**\n- In `appendix_discussion.tex` line ~39, text says \"Qwen achieves CF=2.57% on DocRED vs. Llama's 12.02%\", and also \"Qwen3-8B shows f_gf=0.08% ... yielding 99.9% coverage\" and \"residual DR (0.93% vs. Llama's 0.08%)\" — note this implies Qwen DR=0.93% and Llama DR=0.08% on SciERC, which is consistent with the main tables.\n- In `appendix_discussion.tex` line ~39: \"consistent with its lower residual DR (0.93% vs. Llama's 0.08%)\" — but this is Qwen's DR vs Llama's DR on SciERC (both ZS S1), consistent with causal tracing table.\n- `appendix_posthoc_extended` table: Qwen DocRED FT shows R-F1_cd=40.79, but `appendix_ft_ablation` table shows Qwen DocRED S1 R-F1=40.56 — **potential inconsistency** between these two tables for Qwen DocRED FT constrained R-F1 (40.79 vs 40.56).\n- `appendix_beam_search.tex`: DocRED LoRA Qwen Greedy shows R-F1=40.56, PF=8.52 — matches FT ablation table.\n- `appendix_quantization.tex`: Qwen DocRED FP16 R-F1=40.79† with note \"evaluated on 998 docs\" — explains discrepancy (subset vs. full set).&lt;/result>\n&lt;usage>&lt;total_tokens>100700&lt;/total_tokens>&lt;tool_uses>25&lt;/tool_uses>&lt;duration_ms>376042&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>",
    "commandMode": "task-notification"
  },
  "type": "attachment",
  "uuid": "202a28ae-acd8-4597-b389-3f1fa0fb7f4f",
  "timestamp": "2026-05-25T19:53:45.113Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

---


### Runtime record

_source line 1885 · 2026-05-25T19:53:45.113Z_

```json
{
  "type": "queue-operation",
  "operation": "remove",
  "timestamp": "2026-05-25T19:53:45.113Z",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25"
}
```

---


### Runtime record

_source line 1886 · 2026-05-25T19:53:45.113Z_

```json
{
  "parentUuid": "202a28ae-acd8-4597-b389-3f1fa0fb7f4f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9cdc2aa4-f4ad-4970-a68b-63ac91d983ed",
  "timestamp": "2026-05-25T19:53:45.113Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

---


### Runtime record

_source line 1887_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[飞书用户 用户]: 📊 论文自检任务（重大）：全文数据真实性与可追溯性彻底审计  这是一次彻底的大检查，必须认真对待。AI 写论文最致命的两个问题：编数字（hallucinate）和抄数字（数字之间不一致或来源不明）。这次的目标是把每一个出现在论文里的数字都\"对账\"清楚。  ⚠️ 凡是查不到出处的数字，要么找到出处，要么删掉。不允许凭印象、凭\"差不多\"、凭老版本残留的数字留在论文里。  ---…",
  "leafUuid": "9cdc2aa4-f4ad-4970-a68b-63ac91d983ed",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25"
}
```

---


### Runtime record

_source line 1888_

```json
{
  "type": "ai-title",
  "aiTitle": "Paper formatting and figure optimization for EMNLP",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25"
}
```

---


### Assistant

_source line 1889 · 2026-05-25T19:55:04.742Z_

<details><summary>Logged reasoning block</summary>

```text
All four agents have completed. Now I need to synthesize all findings into a comprehensive audit report. Let me compile everything.

Let me summarize what we've found across all agents:

## Verified (✅):

### Table 1 (SciERC ablation) - ALL 48 numbers verified
### Table 2 (Composability) - ALL 56 numbers verified

### Abstract claims:
- "3%" grammar-only DR reduction: (15.37-14.84)/15.37 = 3.4% ≈ 3% ✅
- "24%" semantic-only: (15.37-11.65)/15.37 = 24.2% ≈ 24% ✅


- "94%" composition: (15.37-0.93)/15.37 = 93.9% ≈ 94% ✅
- "≤0.21%": Table 2 max DR under S1 FT is Llama DocRED 0.21% ✅
- "±0.3 pp": Bootstrap CIs ⊆ [-0.69, +0.25] pp ✅
- "~1.5× latency": beam k=4 is 1.39× ⚠️ (1.39 vs ~1.5, slightly lower than claimed)
- "24% to 84%": 8B 24.2%, 70B 84.2% ✅

Now checking the intro claims: the 15-18% improvement range holds across SciERC and DocRED, the unconstrained error rates fall within 0.5-2%, the 62% reduction calculation checks out, and the 5.8 percentage point delta from Evaluate-for is confirmed. Post-hoc rejection reaches up to 73.7%, the R-F1 range spans 40-46%, and I'm verifying the false positive rates.

The remaining metrics all check out—false positives hit 97.6-100%, constrained F1 stays at or below 1.4%, beam search with k=2 and k=4 produce the expected results, the 70B model shows zero error rates on both datasets with semantic-only performance at 84%, and runtime overhead is around 10-13% with 37% lower absolute latency.

I'm verifying the figures and tables now—the cross-model heatmap, composition bars, per-relation breakdowns, quantization results, and bootstrap confidence intervals all match. But I found a discrepancy in the 70B SciERC degradation: the paper claims -8.45 percentage points, but the actual difference between 44.53 and 36.28 is -8.25.

The 70B DocRED ablation caption also has an error—it says 998 documents when the experiments used 200-doc subsets. The zero-shot CF count for DocRED is harder to pin down: the paper lists 173, but calculating from the registry percentage of 5.34% on roughly 2637 relations gives around 141, so there might be a different denominator at play. For the post-hoc rejection rate, the stated range of 15-74% undershoots the actual minimum of 13.9%, and the abstract's claim of ~1.5× latency is slightly inflated—beam search with k=4 is actually 1.39×.

There's also a discrepancy with the Llama fine-tuned beam search SciERC R-F1: the appendix shows 46.18 but the registry entry shows 46.11. I'm noticing that different experiments might be involved here—one sweep experiment has 46.18 while another registry entry has 46.11—so I need to figure out which one the paper actually cites. Looking at the beam latency table, it turns out the paper uses a separate latency experiment (p8c_ft_scierc_latency) rather than d066, so that's not actually a mismatch. For the DocRED LoRA beam discrepancy, the appendix shows different values than the registry entry d065_qwen_greedy_4096_r2, though the main text Table 2 appears to have matching numbers—I need to verify which source the appendix is actually citing.

Now I'm checking the "40.79 vs 40.56" inconsistency across the appendix tables to see if there's a real conflict or if they're measuring different things. a potential reader confusion issue but not a data integrity error. There are several unverifiable results scattered throughout the paper—per-relation breakdowns in Figure 2 that lack registry backing, downstream analysis numbers from post-hoc work, some beam search metrics missing F1 values, and a few baseline numbers I can't locate in the registry. Agent 2 flagged the 70B model as having no entry, but that turned out to be a false alarm.

Now I'm tallying up everything I've audited across the tables, figures, and text sections to compile the final verification report. I'm noticing a discrepancy in how the 1.5× latency claim is framed—the abstract doesn't specify whether it's comparing beam search to constrained or unconstrained greedy, but the body text clarifies it's versus the constrained S1 baseline at 1.39×. The appendix table shows 1.54× when compared to unconstrained greedy instead, so there's an ambiguity about which baseline the abstract is referencing. So these are measurements from different experimental runs measuring different baselines—the abstract compares against unconstrained greedy while the body compares against constrained greedy S1, which explains the discrepancy. Now I'll put together the final report in a structured format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cdc2aa4-f4ad-4970-a68b-63ac91d983ed",
  "isSidechain": false,
  "requestId": "req_011CbPsa1DDSwpRLBz2DBcTc",
  "type": "assistant",
  "uuid": "f23b41a1-dd65-4e06-b817-a7fc2ac447f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PeW7mcLYo2Qxj5udGeSUao",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 42247,
      "cache_read_input_tokens": 59944,
      "output_tokens": 3453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3453,
          "cache_read_input_tokens": 59944,
          "cache_creation_input_tokens": 42247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42247
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

_source line 1890 · 2026-05-25T19:55:04.751Z_

All four agents have completed. Let me compile the comprehensive audit report now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f23b41a1-dd65-4e06-b817-a7fc2ac447f4",
  "isSidechain": false,
  "requestId": "req_011CbPsa1DDSwpRLBz2DBcTc",
  "type": "assistant",
  "uuid": "e1264b29-7183-42e8-9181-2eba37242305",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PeW7mcLYo2Qxj5udGeSUao",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 42247,
      "cache_read_input_tokens": 59944,
      "output_tokens": 3453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3453,
          "cache_read_input_tokens": 59944,
          "cache_creation_input_tokens": 42247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42247
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


### Tool call

_source line 1891 · 2026-05-25T19:55:05.921Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QwKf9SksL2kAmfavt7ZkpS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1264b29-7183-42e8-9181-2eba37242305",
  "isSidechain": false,
  "requestId": "req_011CbPsa1DDSwpRLBz2DBcTc",
  "type": "assistant",
  "uuid": "4e93b4b0-4f43-419d-a8a9-21f111c8516d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PeW7mcLYo2Qxj5udGeSUao",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 42247,
      "cache_read_input_tokens": 59944,
      "output_tokens": 3453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 42247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3453,
          "cache_read_input_tokens": 59944,
          "cache_creation_input_tokens": 42247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 42247
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


### Tool result

_source line 1892 · 2026-05-25T19:55:05.936Z_

<details><summary>↩ Tool result · `toolu_01QwKf9SksL2kAmfavt7ZkpS`</summary>

```text
1	% Section 5 — Event Extraction on WikiEvents (summary; full results in Appendix)
2	
3	\subsection{Event Extraction Validation}
4	\label{sec:wikievents}
5	
6	\emph{Does OntoCoDec generalize beyond relation extraction?}
7	Zero-shot evaluation on WikiEvents (246 documents, 3 models; Appendices~\ref{app:wikievents-pilot},~\ref{app:wikievents},~\ref{app:wikievents-kappa}) confirms constraint applicability to event extraction, with EV and RoV violations eliminated across all models; fine-tuning composability is preliminary ($n{=}20$).
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e93b4b0-4f43-419d-a8a9-21f111c8516d",
  "isSidechain": false,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "type": "user",
  "uuid": "f1072e4f-829a-407c-892b-8e26fe45955c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex",
      "content": "% Section 5 — Event Extraction on WikiEvents (summary; full results in Appendix)\n\n\\subsection{Event Extraction Validation}\n\\label{sec:wikievents}\n\n\\emph{Does OntoCoDec generalize beyond relation extraction?}\nZero-shot evaluation on WikiEvents (246 documents, 3 models; Appendices~\\ref{app:wikievents-pilot},~\\ref{app:wikievents},~\\ref{app:wikievents-kappa}) confirms constraint applicability to event extraction, with EV and RoV violations eliminated across all models; fine-tuning composability is preliminary ($n{=}20$).\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "4e93b4b0-4f43-419d-a8a9-21f111c8516d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---


### Tool call

_source line 1893 · 2026-05-25T19:55:09.512Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VTg2PFtct9Kq6eibxcuBTE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1072e4f-829a-407c-892b-8e26fe45955c",
  "isSidechain": false,
  "requestId": "req_011CbPsfmTu1gSri2ZQtScaT",
  "type": "assistant",
  "uuid": "e053957f-42f3-4501-a5c1-3a9a980b76e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LF4gSGjrFAuAS9YUusF1W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3635,
      "cache_read_input_tokens": 102191,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3635,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 102191,
          "cache_creation_input_tokens": 3635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3635
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


### Tool result

_source line 1894 · 2026-05-25T19:55:09.517Z_

<details><summary>↩ Tool result · `toolu_01VTg2PFtct9Kq6eibxcuBTE`</summary>

```text
1	% Section 7 — Discussion and Conclusion
2	
3	% ──────────────────────────────────────────
4	%  Figure: Cross-Model Heatmap (placed here for right-column [t] on p8)
5	% ──────────────────────────────────────────
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=0.75\columnwidth]{figures/fig_crossmodel_heatmap.pdf}
9	\caption{DR reduction (\%) across 3 models $\times$ 2 datasets (zero-shot S1). Calibrated models (Qwen, Llama) achieve $\geq$90\% on SciERC; DocRED's higher $\bar{\kappa}$ reduces effectiveness. Full violation breakdown in Table~\ref{tab:cross-model} (Appendix~\ref{app:cross-model-zs}).}
10	\label{fig:crossmodel-heatmap}
11	\end{figure}
12	
13	Neither layer alone suffices: grammar-only achieves 3\% DR reduction, semantic-only 24\%, but their composition yields 94\%, an enabling dependency that weakens at scale (84\% at 70B).
14	This non-additive interaction arises because the grammar layer provides a structured prerequisite: by restricting relation tokens to $\mathcal{R}$ and entity type tokens to $\mathcal{E}$, it ensures the semantic layer receives well-formed inputs on which domain/range lookups can operate.
15	Without grammar-enforced vocabulary membership, the semantic layer cannot reliably identify which relation governs a given type position.
16	
17	OntoCoDec composes both layers, reducing DR to $\leq$\,0.21\% across model families and datasets ($\pm$0.3\,pp R-F1).
18	The residual DR$\to$CF conversion is a severity downgrade rather than an error introduction: DR violations produce ontology-invalid triples that corrupt downstream knowledge graphs and require re-extraction, while CF violations (cross-triple type inconsistency) preserve individually valid triples and are resolvable via beam search or post-hoc reranking.
19	Beam $k{=}4$ achieves near-zero violations at 8B, making generative IE reliably schema-compliant.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e053957f-42f3-4501-a5c1-3a9a980b76e9",
  "isSidechain": false,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "type": "user",
  "uuid": "568d19be-56e4-4611-a648-012f3c6d67a7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex",
      "content": "% Section 7 — Discussion and Conclusion\n\n% ──────────────────────────────────────────\n%  Figure: Cross-Model Heatmap (placed here for right-column [t] on p8)\n% ──────────────────────────────────────────\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_crossmodel_heatmap.pdf}\n\\caption{DR reduction (\\%) across 3 models $\\times$ 2 datasets (zero-shot S1). Calibrated models (Qwen, Llama) achieve $\\geq$90\\% on SciERC; DocRED's higher $\\bar{\\kappa}$ reduces effectiveness. Full violation breakdown in Table~\\ref{tab:cross-model} (Appendix~\\ref{app:cross-model-zs}).}\n\\label{fig:crossmodel-heatmap}\n\\end{figure}\n\nNeither layer alone suffices: grammar-only achieves 3\\% DR reduction, semantic-only 24\\%, but their composition yields 94\\%, an enabling dependency that weakens at scale (84\\% at 70B).\nThis non-additive interaction arises because the grammar layer provides a structured prerequisite: by restricting relation tokens to $\\mathcal{R}$ and entity type tokens to $\\mathcal{E}$, it ensures the semantic layer receives well-formed inputs on which domain/range lookups can operate.\nWithout grammar-enforced vocabulary membership, the semantic layer cannot reliably identify which relation governs a given type position.\n\nOntoCoDec composes both layers, reducing DR to $\\leq$\\,0.21\\% across model families and datasets ($\\pm$0.3\\,pp R-F1).\nThe residual DR$\\to$CF conversion is a severity downgrade rather than an error introduction: DR violations produce ontology-invalid triples that corrupt downstream knowledge graphs and require re-extraction, while CF violations (cross-triple type inconsistency) preserve individually valid triples and are resolvable via beam search or post-hoc reranking.\nBeam $k{=}4$ achieves near-zero violations at 8B, making generative IE reliably schema-compliant.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "e053957f-42f3-4501-a5c1-3a9a980b76e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---


### Assistant

_source line 1895 · 2026-05-25T19:55:12.528Z_

Now let me verify the internal consistency of two key claims that appear in multiple places, and check the "~1.5×" vs "1.39×" ambiguity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "568d19be-56e4-4611-a648-012f3c6d67a7",
  "isSidechain": false,
  "requestId": "req_011CbPsg2odHQY6VCeEXF7bq",
  "type": "assistant",
  "uuid": "9fb0136f-4e29-47f6-bfaf-d1d3ad3f6e45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3KdzcVnb6ofabCWW4cotB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 105826,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 338,
          "cache_read_input_tokens": 105826,
          "cache_creation_input_tokens": 683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 683
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


### Tool call

_source line 1896 · 2026-05-25T19:55:13.981Z_

<details open><summary>🔧 Tool call — Grep · `toolu_019rcJRKHVLCQUdMdg7akKJM`</summary>

```json
{
  "pattern": "1\\.5.*latency|1\\.39|1\\.54",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fb0136f-4e29-47f6-bfaf-d1d3ad3f6e45",
  "isSidechain": false,
  "requestId": "req_011CbPsg2odHQY6VCeEXF7bq",
  "type": "assistant",
  "uuid": "4a2c2016-96ba-48c8-93ca-3d9d17958816",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3KdzcVnb6ofabCWW4cotB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 105826,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 338,
          "cache_read_input_tokens": 105826,
          "cache_creation_input_tokens": 683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 683
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


### Tool result

_source line 1897 · 2026-05-25T19:55:14.000Z_

<details><summary>↩ Tool result · `toolu_019rcJRKHVLCQUdMdg7akKJM`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:35:%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:44:On SciERC, the baseline RV rate is only 1.39\% (24~OOV predictions), too few to produce a detectable F1 effect.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:153:profiles (SciERC RV\,=\,1.39\% vs.\ DocRED RV\,=\,29.66\%) confirms
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:21:Composed with LoRA, greedy decoding reduces DR to near-zero ($\leq$\,0.21\%) at R-F1 40--46\% ($\pm$0.3\,pp, $+$10\% latency), with 97.6--100\% of removed triples confirmed as false positives; beam ($k{=}4$) achieves near-zero violations at ${\sim}$1.5$\times$ latency.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:36:  & 1.39  & 0.40
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex:83:TCR is a zero-cost complement for low-tightness schemas where beam search latency (1.39$\times$) is undesirable.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex:38:%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex:47:On SciERC, the baseline RV rate is only 1.39\% (24~OOV predictions), too few to produce a detectable F1 effect.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex:7:Composed with LoRA fine-tuning across three model families and two relation extraction datasets (up to 96 relations), OntoCoDec reduces DR to $\leq$\,0.21\% with minimal F1 impact ($\pm$0.3\,pp), converting irrecoverable type errors into correctable cross-field inconsistencies; beam search ($k{=}4$) achieves near-zero violations at ${\sim}$1.5$\times$ latency.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex:24:  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:35:  & 1.39  & 0.40
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:101:violations (1.39\%\,$\to$\,0\%) and entity type violations
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:150:%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:155:SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:83:2          & 0.35 & 4.12 & 31.54 & \textbf{8.75} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:97:Among constrained configurations, $k{=}2$ is Pareto optimal (R-F1 44.60, CF 0.11\%, 1.39$\times$ vs.\ greedy unconstrained; 1.18$\times$ vs.\ greedy S1); $k{\geq}4$ yields diminishing F1 returns with increasing latency (1.63--2.03$\times$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:121: & \textsc{unc} & 67.79 & 44.75 & 1.54 & 0    & 2.954 & 1.18$\times$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:122: & \cellcolor{blue!8}\textsc{con} & \cellcolor{blue!8}67.71 & \cellcolor{blue!8}\textbf{44.60} & \cellcolor{blue!8}\textbf{0} & \cellcolor{blue!8}0.11 & \cellcolor{blue!8}3.463 & \cellcolor{blue!8}1.39$\times$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:203:Beam-4 constrained (S1)& 4.013 & 1.54$\times$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:212:The total 1.54$\times$ overhead is acceptable for offline batch IE; \texttt{early\_stopping} limits additional compute to partial-sequence exploration.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex:7:We evaluate OntoCoDec in two deployment configurations: greedy S1 (DR\,$\leq$\,0.21\%, $+$10\% latency) and beam S1 (near-zero violations, 1.39$\times$ latency); zero-shot evaluation (\S\ref{sec:scierc-results}; Appendix~\ref{app:cross-model-zs}) serves as a diagnostic probe for the fine-tuned setting (relation F1 (R-F1) 40--46\%).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex:17:  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:14:A beam-width sweep ($k \in \{1,2,4,8\}$) reveals $k{=}2$ as Pareto-optimal: R-F1 44.60, CF 0.11\%, at 1.18$\times$ greedy S1 latency; $k{=}4$ achieves CF${=}$0\% at 1.39$\times$ (Figure~\ref{fig:beam-pareto}; Appendix~\ref{app:beam-search}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:15:This yields three deployment tiers: greedy S1 ($+$10\%, DR${\leq}$0.21\%, CF${\leq}$1.4\%), beam $k{=}2$ (1.18$\times$, near-zero CF), and beam $k{=}4$ (1.39$\times$, near-zero violations at 8B).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a2c2016-96ba-48c8-93ca-3d9d17958816",
  "isSidechain": false,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "type": "user",
  "uuid": "d9d0dfbd-0e58-4bee-a2f1-fb81b6cc9e50",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:35:%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:44:On SciERC, the baseline RV rate is only 1.39\\% (24~OOV predictions), too few to produce a detectable F1 effect.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:153:profiles (SciERC RV\\,=\\,1.39\\% vs.\\ DocRED RV\\,=\\,29.66\\%) confirms\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:21:Composed with LoRA, greedy decoding reduces DR to near-zero ($\\leq$\\,0.21\\%) at R-F1 40--46\\% ($\\pm$0.3\\,pp, $+$10\\% latency), with 97.6--100\\% of removed triples confirmed as false positives; beam ($k{=}4$) achieves near-zero violations at ${\\sim}$1.5$\\times$ latency.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:36:  & 1.39  & 0.40\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex:83:TCR is a zero-cost complement for low-tightness schemas where beam search latency (1.39$\\times$) is undesirable.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex:38:%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex:47:On SciERC, the baseline RV rate is only 1.39\\% (24~OOV predictions), too few to produce a detectable F1 effect.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex:7:Composed with LoRA fine-tuning across three model families and two relation extraction datasets (up to 96 relations), OntoCoDec reduces DR to $\\leq$\\,0.21\\% with minimal F1 impact ($\\pm$0.3\\,pp), converting irrecoverable type errors into correctable cross-field inconsistencies; beam search ($k{=}4$) achieves near-zero violations at ${\\sim}$1.5$\\times$ latency.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex:24:  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:35:  & 1.39  & 0.40\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:101:violations (1.39\\%\\,$\\to$\\,0\\%) and entity type violations\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:150:%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:155:SciERC's baseline RV is only 1.39\\% (24 OOV predictions), too few to produce a detectable F1 effect.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:83:2          & 0.35 & 4.12 & 31.54 & \\textbf{8.75} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:97:Among constrained configurations, $k{=}2$ is Pareto optimal (R-F1 44.60, CF 0.11\\%, 1.39$\\times$ vs.\\ greedy unconstrained; 1.18$\\times$ vs.\\ greedy S1); $k{\\geq}4$ yields diminishing F1 returns with increasing latency (1.63--2.03$\\times$).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:121: & \\textsc{unc} & 67.79 & 44.75 & 1.54 & 0    & 2.954 & 1.18$\\times$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:122: & \\cellcolor{blue!8}\\textsc{con} & \\cellcolor{blue!8}67.71 & \\cellcolor{blue!8}\\textbf{44.60} & \\cellcolor{blue!8}\\textbf{0} & \\cellcolor{blue!8}0.11 & \\cellcolor{blue!8}3.463 & \\cellcolor{blue!8}1.39$\\times$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:203:Beam-4 constrained (S1)& 4.013 & 1.54$\\times$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:212:The total 1.54$\\times$ overhead is acceptable for offline batch IE; \\texttt{early\\_stopping} limits additional compute to partial-sequence exploration.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex:7:We evaluate OntoCoDec in two deployment configurations: greedy S1 (DR\\,$\\leq$\\,0.21\\%, $+$10\\% latency) and beam S1 (near-zero violations, 1.39$\\times$ latency); zero-shot evaluation (\\S\\ref{sec:scierc-results}; Appendix~\\ref{app:cross-model-zs}) serves as a diagnostic probe for the fine-tuned setting (relation F1 (R-F1) 40--46\\%).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex:17:  & Unconstrained & 0.40 & 1.39 & 15.37 & \\multirow{2}{*}{94.0\\%} & 31.01 & 8.23 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:14:A beam-width sweep ($k \\in \\{1,2,4,8\\}$) reveals $k{=}2$ as Pareto-optimal: R-F1 44.60, CF 0.11\\%, at 1.18$\\times$ greedy S1 latency; $k{=}4$ achieves CF${=}$0\\% at 1.39$\\times$ (Figure~\\ref{fig:beam-pareto}; Appendix~\\ref{app:beam-search}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:15:This yields three deployment tiers: greedy S1 ($+$10\\%, DR${\\leq}$0.21\\%, CF${\\leq}$1.4\\%), beam $k{=}2$ (1.18$\\times$, near-zero CF), and beam $k{=}4$ (1.39$\\times$, near-zero violations at 8B).",
    "numLines": 24
  },
  "sourceToolAssistantUUID": "4a2c2016-96ba-48c8-93ca-3d9d17958816",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---


### Tool result

_source line 1898 · 2026-05-25T19:55:14.885Z_

<details><summary>↩ Tool result · `toolu_01NSZ4diJpNQKZ1zvEdzeM3z`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:21:Composed with LoRA, greedy decoding reduces DR to near-zero ($\leq$\,0.21\%) at R-F1 40--46\% ($\pm$0.3\,pp, $+$10\% latency), with 97.6--100\% of removed triples confirmed as false positives; beam ($k{=}4$) achieves near-zero violations at ${\sim}$1.5$\times$ latency.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:28:    \item A two-layer constrained decoding framework that reduces domain/range violations to near-zero ($\leq$\,0.21\%) without retraining or significant quality loss, showing that these type constraints require stateful enforcement beyond context-free grammars (Proposition~1; \S\ref{sec:decidability}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex:22:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex:7:We evaluate OntoCoDec in two deployment configurations: greedy S1 (DR\,$\leq$\,0.21\%, $+$10\% latency) and beam S1 (near-zero violations, 1.39$\times$ latency); zero-shot evaluation (\S\ref{sec:scierc-results}; Appendix~\ref{app:cross-model-zs}) serves as a diagnostic probe for the fine-tuned setting (relation F1 (R-F1) 40--46\%).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:98:Fine-tuning alone reduces DR to 0.5--2\% but leaves residual violations on tight-constraint relations (Table~\ref{tab:composability}; full fine-tuning in Appendix~\ref{app:full-ft}); adding S1 yields DR\,$\leq$\,0.21\% with no significant $\Delta$R-F1 (Bonferroni-corrected; 95\% CIs $\subseteq [-0.69, {+}0.25]$\,pp; removed triples are 97.6--100\% false positives; Appendix~\ref{app:downstream-impact}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex:9:S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates RV (29.66\%\,$\to$\,0.03\%) and ET, with R-F1 $+$0.49\,pp ($p < 0.001$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex:12:Fine-tuning reduces residual DR to $\leq$\,0.21\% (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex:17:OntoCoDec composes both layers, reducing DR to $\leq$\,0.21\% across model families and datasets ($\pm$0.3\,pp R-F1).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:15:This yields three deployment tiers: greedy S1 ($+$10\%, DR${\leq}$0.21\%, CF${\leq}$1.4\%), beam $k{=}2$ (1.18$\times$, near-zero CF), and beam $k{=}4$ (1.39$\times$, near-zero violations at 8B).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:48:  & & S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\downarrow$57\% \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5956b3aa-0a31-47f4-8737-75a9a9be452c",
  "isSidechain": false,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "type": "user",
  "uuid": "6b1af83e-5e4c-45a6-8218-1f37adc3bc23",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:21:Composed with LoRA, greedy decoding reduces DR to near-zero ($\\leq$\\,0.21\\%) at R-F1 40--46\\% ($\\pm$0.3\\,pp, $+$10\\% latency), with 97.6--100\\% of removed triples confirmed as false positives; beam ($k{=}4$) achieves near-zero violations at ${\\sim}$1.5$\\times$ latency.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:28:    \\item A two-layer constrained decoding framework that reduces domain/range violations to near-zero ($\\leq$\\,0.21\\%) without retraining or significant quality loss, showing that these type constraints require stateful enforcement beyond context-free grammars (Proposition~1; \\S\\ref{sec:decidability}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex:22:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex:7:We evaluate OntoCoDec in two deployment configurations: greedy S1 (DR\\,$\\leq$\\,0.21\\%, $+$10\\% latency) and beam S1 (near-zero violations, 1.39$\\times$ latency); zero-shot evaluation (\\S\\ref{sec:scierc-results}; Appendix~\\ref{app:cross-model-zs}) serves as a diagnostic probe for the fine-tuned setting (relation F1 (R-F1) 40--46\\%).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:98:Fine-tuning alone reduces DR to 0.5--2\\% but leaves residual violations on tight-constraint relations (Table~\\ref{tab:composability}; full fine-tuning in Appendix~\\ref{app:full-ft}); adding S1 yields DR\\,$\\leq$\\,0.21\\% with no significant $\\Delta$R-F1 (Bonferroni-corrected; 95\\% CIs $\\subseteq [-0.69, {+}0.25]$\\,pp; removed triples are 97.6--100\\% false positives; Appendix~\\ref{app:downstream-impact}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex:9:S1 reduces DR from 18.46\\% to 10.21\\% ($\\downarrow$45\\%), eliminates RV (29.66\\%\\,$\\to$\\,0.03\\%) and ET, with R-F1 $+$0.49\\,pp ($p < 0.001$).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex:12:Fine-tuning reduces residual DR to $\\leq$\\,0.21\\% (Table~\\ref{tab:composability}; residual decomposition in Appendix~\\ref{app:residual-dr-analysis}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex:17:OntoCoDec composes both layers, reducing DR to $\\leq$\\,0.21\\% across model families and datasets ($\\pm$0.3\\,pp R-F1).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:15:This yields three deployment tiers: greedy S1 ($+$10\\%, DR${\\leq}$0.21\\%, CF${\\leq}$1.4\\%), beam $k{=}2$ (1.18$\\times$, near-zero CF), and beam $k{=}4$ (1.39$\\times$, near-zero violations at 8B).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:48:  & & S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\\downarrow$57\\% \\\\",
    "numLines": 10
  },
  "sourceToolAssistantUUID": "5956b3aa-0a31-47f4-8737-75a9a9be452c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---


### Tool call

_source line 1899 · 2026-05-25T19:55:14.868Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NSZ4diJpNQKZ1zvEdzeM3z`</summary>

```json
{
  "pattern": "0\\.21",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "section*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9d0dfbd-0e58-4bee-a2f1-fb81b6cc9e50",
  "isSidechain": false,
  "requestId": "req_011CbPsg2odHQY6VCeEXF7bq",
  "type": "assistant",
  "uuid": "5956b3aa-0a31-47f4-8737-75a9a9be452c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3KdzcVnb6ofabCWW4cotB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 105826,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 338,
          "cache_read_input_tokens": 105826,
          "cache_creation_input_tokens": 683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 683
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

_source line 1900_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[飞书用户 用户]: 📊 论文自检任务（重大）：全文数据真实性与可追溯性彻底审计  这是一次彻底的大检查，必须认真对待。AI 写论文最致命的两个问题：编数字（hallucinate）和抄数字（数字之间不一致或来源不明）。这次的目标是把每一个出现在论文里的数字都\"对账\"清楚。  ⚠️ 凡是查不到出处的数字，要么找到出处，要么删掉。不允许凭印象、凭\"差不多\"、凭老版本残留的数字留在论文里。  ---…",
  "leafUuid": "6b1af83e-5e4c-45a6-8218-1f37adc3bc23",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25"
}
```

---


### Runtime record

_source line 1901_

```json
{
  "type": "ai-title",
  "aiTitle": "Paper formatting and figure optimization for EMNLP",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25"
}
```

---


### Assistant

_source line 1902 · 2026-05-25T19:55:38.665Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the latency issue:

- Abstract & Intro: "~1.5× latency" for beam k=4
- Section 3 setup: "1.39× latency" for beam S1
- Section 5 runtime: "k=4 achieves CF=0% at 1.39×" — vs greedy S1
- Appendix beam search: "k=2 con: 1.39× vs. greedy unconstrained; 1.18× vs. greedy S1"
- Appendix beam search: "Beam-4 constrained: 4.013s, 1.54×" — vs greedy unconstrained


- Appendix sweep table shows k=4 constrained at 4.069s, which is 1.63× compared to k=1 unconstrained (2.494s)
- But the body text references k=4 achieving 0% constraint failure at 1.39×, which comes from comparing against k=1 constrained (2.932s)
- The abstract's "~1.5×" appears to reference beam-4 constrained versus greedy unconstrained from the latency table
- These are measuring against different baselines, so it's not a factual error but rather an inconsistency in which baseline is being referenced

Now I'm checking the constraint failure claim in the deployment section where it says greedy S1 has CF≤1.4%, but looking at Table 2, the actual max CF values under S1 fine-tuning are 1.18% for Qwen SciERC and 0% for Qwen DocRED, so the claim appears to be supported by the data. I've got what I need to put together a comprehensive report for the user now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b1af83e-5e4c-45a6-8218-1f37adc3bc23",
  "isSidechain": false,
  "requestId": "req_011CbPsgRk1vd9p8MSfhDq7s",
  "type": "assistant",
  "uuid": "27a773b2-0144-40cf-9d1a-511c1f249a8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjJ4Ftd68BGzFVbSRKgi65",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4203,
      "cache_read_input_tokens": 106509,
      "output_tokens": 1090,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1090,
          "cache_read_input_tokens": 106509,
          "cache_creation_input_tokens": 4203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4203
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

_source line 1903 · 2026-05-25T19:55:38.825Z_

Now I have everything needed for the complete audit report. Let me compile and send it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27a773b2-0144-40cf-9d1a-511c1f249a8e",
  "isSidechain": false,
  "requestId": "req_011CbPsgRk1vd9p8MSfhDq7s",
  "type": "assistant",
  "uuid": "46014263-d32e-4190-b3cc-88f12f26618d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjJ4Ftd68BGzFVbSRKgi65",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4203,
      "cache_read_input_tokens": 106509,
      "output_tokens": 1090,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1090,
          "cache_read_input_tokens": 106509,
          "cache_creation_input_tokens": 4203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4203
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


### Tool call

_source line 1904 · 2026-05-25T19:55:38.972Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012CyAJULrSkQiiHgWp3MWuN`</summary>

```json
{
  "query": "select:director_reply_to_user",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46014263-d32e-4190-b3cc-88f12f26618d",
  "isSidechain": false,
  "requestId": "req_011CbPsgRk1vd9p8MSfhDq7s",
  "type": "assistant",
  "uuid": "88e01446-4096-4c59-ab92-dcf6e2c365ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjJ4Ftd68BGzFVbSRKgi65",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4203,
      "cache_read_input_tokens": 106509,
      "output_tokens": 1090,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1090,
          "cache_read_input_tokens": 106509,
          "cache_creation_input_tokens": 4203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4203
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


### Tool result

_source line 1905 · 2026-05-25T19:55:38.976Z_

<details><summary>↩ Tool result · `toolu_012CyAJULrSkQiiHgWp3MWuN`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88e01446-4096-4c59-ab92-dcf6e2c365ab",
  "isSidechain": false,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "type": "user",
  "uuid": "5a23be8c-6ef2-4759-918f-b8c8669906b0",
  "toolUseResult": {
    "matches": [],
    "query": "select:director_reply_to_user",
    "total_deferred_tools": 99
  },
  "sourceToolAssistantUUID": "88e01446-4096-4c59-ab92-dcf6e2c365ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---


### Tool call

_source line 1906 · 2026-05-25T19:55:41.985Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RGEsPEgDDo5ujNJEjzpx9i`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_reply_to_user",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a23be8c-6ef2-4759-918f-b8c8669906b0",
  "isSidechain": false,
  "requestId": "req_011CbPsiCsRKktgBeWGZgbd8",
  "type": "assistant",
  "uuid": "9d482e1a-1936-44ed-ac73-3d9018337321",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQNUaYk9PiE7wQaJYp2hg1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1106,
      "cache_read_input_tokens": 110712,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1106,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 110712,
          "cache_creation_input_tokens": 1106,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1106
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


### Tool result

_source line 1907 · 2026-05-25T19:55:41.988Z_

<details><summary>↩ Tool result · `toolu_01RGEsPEgDDo5ujNJEjzpx9i`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_reply_to_user"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d482e1a-1936-44ed-ac73-3d9018337321",
  "isSidechain": false,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "type": "user",
  "uuid": "bbca8df3-6f3d-4ef3-b73c-7144d814af53",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__director_reply_to_user"
    ],
    "query": "select:mcp__agent-ml-research__director_reply_to_user",
    "total_deferred_tools": 99
  },
  "sourceToolAssistantUUID": "9d482e1a-1936-44ed-ac73-3d9018337321",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---


### Tool call

_source line 1908 · 2026-05-25T19:56:59.584Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_reply_to_user · `toolu_01Y2Ho2WRdD5niXTu2Ch4Mh7`</summary>

```json
{
  "text": "📊 **论文数据真实性与可追溯性审计报告**\n\n---\n\n## 一、审计范围与方法\n\n- **审计对象**：全文 8 页正文 + 25 个附录文件中的所有数值声明\n- **方法**：4 个并行 Agent 分别提取正文数值、附录数值、图表脚本硬编码数据、数据源文件；逐条与 registry.yaml（7630 行，164 个实验）交叉验证\n- **审计总量**：约 **600+ 个独立数值声明**（含表格单元格、正文百分比、统计量、置信区间等）\n\n---\n\n## 二、核心表格验证（100% 覆盖）\n\n### Table 1（SciERC 五向消融，6行×8列=48 个数值）\n✅ **全部精确匹配** registry 对应实验：\n- Unconstrained → `phase2_scierc_unconstrained`\n- Grammar → `phase2_scierc_grammar_only`\n- GCD-equiv → vLLM `guided_json`\n- Semantic → `phase2_scierc_semantic_only`\n- S1 → `phase2_scierc_full_s1`\n- S2 → `phase2_scierc_full_s2`\n\n### Table 2（Fine-tuning composability，8行×7列=56 个数值）\n✅ **全部精确匹配** registry 对应实验（w5_lora_* 系列 8 个实验）\n\n---\n\n## 三、正文关键声明验证\n\n| 声明位置 | 数值 | Registry 来源 | 状态 |\n|---------|------|-------------|------|\n| Abstract: grammar-only 3% | (15.37−14.84)/15.37=3.4%≈3% | phase2_scierc_grammar_only | ✅ |\n| Abstract: semantic-only 24% | (15.37−11.65)/15.37=24.2% | phase2_scierc_semantic_only | ✅ |\n| Abstract: composition 94% | (15.37−0.93)/15.37=93.9% | phase2_scierc_full_s1 | ✅ |\n| Abstract: ≤0.21% DR | Table 2 最大值 Llama DocRED=0.21 | w5_llama_docred_lora_constrained_eval | ✅ |\n| Abstract: ±0.3pp | Bootstrap CIs ⊆[−0.69,+0.25] | r12_table2_bootstrap_ci | ✅ |\n| Abstract: 24%→84% at 70B | 8B=24.2%, 70B=84.2% | eval_70b_zs_scierc_semantic_only | ✅ |\n| Intro: 15-18% ZS violation | SciERC 15.37%, DocRED 18.46% | phase2 unconstrained | ✅ |\n| Intro: 0.5-2% after LoRA | 范围 0.49-1.95% | Table 2 unconstrained 行 | ✅ |\n| Intro: 62% prompting reduction | (15.37−5.78)/15.37=62.4% | mvp_phase0_scierc_schema | ✅ |\n| Intro: Evaluate-for +5.8pp | per_relation.delta_pp=5.8 | mvp_phase0_scierc_schema | ✅ |\n| Intro: 97.6-100% FP | r12_dr_f1_impact_summary 确认 | 远程服务器 pointer file | ✅ |\n| Body: k=2 R-F1=44.60, CF=0.11%, 1.18× | 精确匹配 | d066_beam_sweep | ✅ |\n| Body: k=4 CF=0%, 1.39× | 精确匹配 | d066_beam_sweep | ✅ |\n| Body: 70B SciERC 6.41%→0% | 精确匹配 | r16_70b_scierc_zs_s1 | ✅ |\n| Body: 70B DocRED 14.98%→0% | 精确匹配 | r16_70b_docred_zs_s1 | ✅ |\n| Body: +13.1% runtime overhead | overhead_pct=13.1 | p8_latency_overhead | ✅ |\n| Body: LoRA +10.0% overhead | overhead_mean_pct=10 | p8c_ft_scierc_latency | ✅ |\n| Body: 37% lower absolute latency | (4.163−2.612)/4.163=37.3% | 计算匹配 | ✅ |\n| Body: compilation <0.5s | max=0.42s | d062_ontology_scalability | ✅ |\n| Body: 2-3% overhead to 1000 rels | overhead 1.02-1.03× | d062_ontology_scalability | ✅ |\n| Body: Bonferroni-corrected not sig | all p_B≥0.224 | appendix bootstrap table | ✅ |\n| Body: CIs ⊆[−0.69,+0.25] | 精确匹配所有 4 组 CI | appendix Table 6 | ✅ |\n\n### 图表脚本硬编码数据验证\n\n| 图表 | 状态 | 说明 |\n|------|------|------|\n| Fig 2 per-relation (unconstrained 列) | ✅ | 7 个 relation 精确匹配 registry per_relation 分母/分子 |\n| Fig 3 scale dependency [24, 84] | ✅ | 8B=24.2%, 70B=84.2% |\n| Fig 4 composition [0, 3, 24, 94] | ✅ | 全部精确匹配 Table 1 ΔDR |\n| Fig 5 heatmap (3×2=6 cells) | ✅ | 所有 6 个 DR reduction 值精确匹配 |\n| Fig 6 composition (DR+CF×4=8 values) | ✅ | 全部精确匹配 phase2 metrics |\n| Beam Pareto (Qwen SciERC) | ✅ | 全部精确匹配 d066_beam_sweep |\n\n### 附录表格验证（主要结果）\n\n| 附录表格 | 状态 |\n|---------|------|\n| Cross-model Table 3 (12行×5列) | ✅ 全部匹配 |\n| 70B SciERC LoRA ablation (6行) | ✅ 全部匹配 |\n| 70B DocRED LoRA ablation (6行) | ✅ 全部匹配 |\n| Quantization table (8行) | ✅ 大部分匹配 |\n| Full FT table (4行) | ✅ 全部匹配 |\n| FT four-way ablation (16行) | ✅ 与 Table 2 一致 |\n| Beam ablation ZS (4行) | ✅ 全部匹配 |\n| Beam sweep LoRA (8行) | ✅ 全部匹配 d066 |\n| DocRED 998-doc ZS beam | ✅ 匹配 r14 实验 |\n| TCR tables (SciERC + DocRED) | ✅ 匹配 |\n| WikiEvents table (9行×3 models) | ✅ 匹配 |\n| Scalability table (4行) | ✅ 匹配 d062 |\n| Seed variance table (4行) | ✅ 匹配 |\n\n---\n\n## 四、发现的问题（按严重度排序）\n\n### 🔴 需要修正（3 个）\n\n**Issue 1: 70B SciERC S2 R-F1 下降量计算错误**\n- 位置：`appendix_70b_ablation.tex` 正文\n- 论文写 \"−8.45pp\"，实际 44.53−36.28 = **−8.25pp**\n- 差值 0.2pp，明确的算术错误\n\n**Issue 2: 70B DocRED 消融表 caption 文档数错误**\n- 位置：`appendix_70b_ablation.tex` Table tab:70b-docred-ablation caption\n- Caption 写 \"998 docs\"，但所有底层 70B DocRED 实验实际使用 **200-doc subset**\n- Registry 实验名均为 `eval_70b_lora_docred_200_*`\n\n**Issue 3: Post-hoc filtering rejection rate下界偏差**\n- 位置：正文多处 + 附录\n- 论文写 \"15–74%\"，实际最小值为 Llama SciERC ZS = **13.9%**\n- 建议改为 \"14–74%\" 或 \"~14–74%\"\n\n### 🟡 需要确认/澄清（3 个）\n\n**Issue 4: Abstract \"~1.5× latency\" vs 正文 \"1.39×\" 基线不一致**\n- Abstract/Intro: beam k=4 at \"~1.5× latency\" → 来自 p8c 实验: 4.013/2.612=1.54× (vs unconstrained greedy)\n- Section 5 正文: \"k=4 achieves CF=0% at 1.39×\" → 来自 d066: 4.069/2.932=1.39× (vs S1 greedy)\n- 两个数值来自不同实验、不同 baseline，各自正确但读者容易误解为矛盾\n- 建议：Abstract 明确写 \"~1.5× unconstrained latency\" 或统一为 \"1.4×\"\n\n**Issue 5: 70B DocRED ZS S1 CF count 存疑**\n- `appendix_70b_ablation.tex` 写 CF=173（count）\n- Registry `eval_70b_zs_docred_200_full_s1` 显示 CF_pct=5.34%\n- 5.34% × 估算 triple 数 ≈ 141，与 173 有差距。可能是分母不同，需确认\n\n**Issue 6: Appendix post-hoc 表 Qwen DocRED FT 的 R-F1 = 40.79 vs Table 2 = 40.56**\n- 不是错误：40.79 来自 d065（4096 context, rank 2），40.56 来自 w5 标准 LoRA\n- 但两个表在同一论文中都标注为 \"Qwen DocRED FT constrained\"，读者可能困惑\n- Quantization 表用 † 标注了 \"998 docs\"，但 post-hoc 表没有类似标注\n\n### ⚪ 不可验证但非错误（registry 无对应条目）\n\n- Fig 2 的 Grammar/Semantic/S1 三列 per-relation 细分：registry 只存聚合值，不存 per-relation\n- Downstream analysis 的 lucky violations 数据（4/5/1/1）：后处理分析未注册为正式实验\n- kappa_dr_data.json：本体分析文件，非实验产物\n- Llama DocRED FP16 baseline in quantization table（R-F1=47.35）：未找到精确对应 registry 条目\n\n---\n\n## 五、内部一致性检查\n\n以下关键数值在正文+附录多处出现，全部一致：\n- ✅ \"≤0.21%\" 出现 6 次（abstract, intro, §3, §5 composability, §5 DocRED, conclusion）\n- ✅ \"94%\" DR reduction 出现 8+ 次\n- ✅ \"3%/24%/94%\" 三元组出现 5+ 次\n- ✅ \"551 documents / 998 documents\" 全文一致\n- ✅ \"κ̄=0.333 / 0.842\" 全文一致\n- ✅ Bootstrap CIs [−0.69, +0.25] 正文与附录一致\n- ✅ 所有 Table 1 数值与附录 FT ablation table 一致\n- ✅ Table 2 数值与 beam search appendix greedy baseline 一致\n\n---\n\n## 六、总结\n\n| 指标 | 数值 |\n|------|------|\n| **审计数值总量** | ~600+ |\n| **完全匹配 registry** | ~570+ (95%+) |\n| **需要修正** | 3 个（算术错误 1、caption 错误 1、rounding 偏差 1） |\n| **需要澄清** | 3 个（baseline 不一致 1、count 存疑 1、表间来源不同 1） |\n| **不可验证（非错误）** | ~20 个（后处理分析、per-relation 细分等） |\n| **数据捏造** | **0** |\n\n**结论：全文数据高度可靠。** 所有核心表格（Table 1、Table 2）和主要 claim 数值均与 registry 精确匹配。发现的 3 个需修正问题均为轻微笔误（算术、caption、rounding），不影响任何 claim 的有效性。建议在提交前修正 Issue 1-3，澄清 Issue 4 的 latency baseline。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbca8df3-6f3d-4ef3-b73c-7144d814af53",
  "isSidechain": false,
  "requestId": "req_011CbPsiRaPry6mTsu2Eys4y",
  "type": "assistant",
  "uuid": "a5c7f50a-32b9-4e15-9946-cad63ef3fef1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFgA35g3QxR4CDia76RLLi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 111818,
      "output_tokens": 3799,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3799,
          "cache_read_input_tokens": 111818,
          "cache_creation_input_tokens": 399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 399
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


### Tool result

_source line 1909 · 2026-05-25T19:57:00.728Z_

<details><summary>↩ Tool result · `toolu_01Y2Ho2WRdD5niXTu2Ch4Mh7`</summary>

```text
{"result":"{\"success\": true}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5c7f50a-32b9-4e15-9946-cad63ef3fef1",
  "isSidechain": false,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "type": "user",
  "uuid": "d23df23e-a8a9-4b55-9caa-a681a46593e7",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true}"
    }
  },
  "sourceToolAssistantUUID": "a5c7f50a-32b9-4e15-9946-cad63ef3fef1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---


### Runtime record

_source line 1910 · 2026-05-25T19:57:00.736Z_

```json
{
  "parentUuid": "d23df23e-a8a9-4b55-9caa-a681a46593e7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4d4b98fb-792a-4e1b-9929-3f62e9bb4aaf",
  "timestamp": "2026-05-25T19:57:00.736Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

---


### Runtime record

_source line 1911_

```json
{
  "type": "ai-title",
  "aiTitle": "Paper formatting and figure optimization for EMNLP",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25"
}
```

---


### Runtime record

_source line 1912 · 2026-05-25T19:57:12.012Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T19:57:12.012Z",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "content": "[WRITE HANDOFF] 请立即写你的 handoff。\n\n**格式硬约束**:\n- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹\n- 禁止在标签外写任何寒暄 / 说明 / 确认（\"好的\"/\"我开始写\"/\"写完了\"等）\n\n**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:\n\n### 1. 🔴 硬约束 / 红线\n  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。\n  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。\n  下一个\"你\"第一眼看到的就是这里，写错了会被 Director CRITICAL。\n\n### 2. 🖥️ 基础设施快照\n  - 服务器名 + 工作目录 + Python 路径 + conda env\n  - 模型路径 / 数据集路径 / wandb config / HF cache\n  - 活跃进程：PID + tmux session + cron 任务 ID\n  写一次就稳定，下一个\"你\"不用再 SSH 探查。\n\n### 3. 📊 当前状态\n  - 你刚做完什么 / 正在做什么\n  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要\n  - 等待中的 Worker 回调 / Cron / Director 决策\n\n### 4. 📋 待办（条件触发式）\n  格式 \"条件 X 满足 → 动作 Y\"。例如:\n  - \"Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交\"\n  - \"pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result\"\n\n### 5. 🎯 战略上下文\n  - 项目核心结论 / 决策链（D001..）\n  - 下一个\"你\"最容易判断错的事 / 容易踩的坑\n\n**写作原则**：\n- 第 1 节必须是项目特定的（不是通用 L1 红线）\n- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查\n- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff\n\n示例格式:\n&lt;handoff>\n### 1. 🔴 硬约束 / 红线\n- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）\n- submit_training_job 不支持 shell builtin（source/conda activate 全不行）\n\n### 2. 🖥️ 基础设施快照\n- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases\n- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）\n- 模型：/root/autodl-tmp/qwen35_4b_direct\n- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)\n\n### 3. 📊 当前状态\n我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。\nregistry: pilot_011 RUNNING；其他全 DONE。\n\n### 4. 📋 待办\n- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算\n- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪\n\n### 5. 🎯 战略上下文\nFalcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。\n易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。\n&lt;/handoff>"
}
```

---


### Runtime record

_source line 1913 · 2026-05-25T19:57:12.012Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T19:57:12.012Z",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25"
}
```

---


## Round 142

## Round 142

2 recorded events


### User

_source line 1914 · 2026-05-25T19:57:12.001Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d4b98fb-792a-4e1b-9929-3f62e9bb4aaf",
  "isSidechain": false,
  "promptId": "297b8a7b-d22b-4b02-8aec-0c4d97e4df5b",
  "type": "user",
  "isMeta": true,
  "uuid": "aaa87d7c-eb1d-4754-8c16-10aa172d6775",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---


### Assistant

_source line 1915 · 2026-05-25T19:57:12.002Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaa87d7c-eb1d-4754-8c16-10aa172d6775",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "45757752-c11d-4014-93e1-91484742dd5a",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "id": "4cd6cb5e-8e0f-4a44-bef6-4030dac2ce49",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 143

## Round 143

2 recorded events


### User

_source line 1916 · 2026-05-25T19:57:12.189Z_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45757752-c11d-4014-93e1-91484742dd5a",
  "isSidechain": false,
  "promptId": "297b8a7b-d22b-4b02-8aec-0c4d97e4df5b",
  "type": "user",
  "uuid": "153e5f13-2f17-4227-8fad-8dbf54c1c998",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---


### Runtime record

_source line 1917 · 2026-05-25T19:57:12.188Z_

```json
{
  "parentUuid": "153e5f13-2f17-4227-8fad-8dbf54c1c998",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c2f490a0-ea29-46a1-b05f-24212774621c",
  "timestamp": "2026-05-25T19:57:12.188Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

---
