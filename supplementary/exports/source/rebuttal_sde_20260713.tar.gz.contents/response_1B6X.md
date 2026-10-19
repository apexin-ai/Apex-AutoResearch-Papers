We thank Reviewer 1B6X for the positive assessment and thoughtful questions. We address both points below.

**Q1: NER U-shape recovery at full schema.**

We do not yet have direct experimental evidence for the mechanism behind the U-shape. We offer three hypotheses, each consistent with the observed data but not yet independently verified:

(1) *Coarse-category disambiguation (hypothesis).* Few-NERD's 66 types span 8 coarse categories. At intermediate counts (22–44 types), random batches may over-represent fine-grained types from 2–3 categories while lacking others, removing inter-category contrast. At full schema, all 8 coarse categories are present, potentially providing discriminative anchors. Our error taxonomy (Table 3) is consistent with this: missed-entity rates are substantially higher at intermediate counts (43–65%) than at full schema, suggesting the model suppresses predictions when the presented types lack categorical breadth.

(2) *Task recognition (hypothesis).* The full 66-type schema may activate task-recognition patterns from pretraining, as LLMs have likely seen complete NER tagsets during training. This is consistent with full-schema recall (0.41) exceeding intermediate counts (0.28) despite maximally many candidate types.

(3) *Reduced omission under complete schemas (hypothesis).* Under partial schemas, the model may conservatively suppress predictions when the input does not clearly match any available type. Under full schema, this suppression may be reduced.

We note that the U-shape is specific to NER (where recall is the bottleneck); RE shows monotonic decline because its errors are dominated by type substitution rather than omission. We clearly label these as hypotheses in the Discussion and identify controlled verification (e.g., manipulating coarse-category coverage at fixed type count) as future work.

**Q2: Influence of type definitions on findings.**

To directly answer how the definitions are obtained: type definitions are sourced from the respective dataset documentation and injected into the prompt as "- {type_name}: {definition}" lines (Appendix C.3). Specifically:
- **Few-NERD (NER):** 66 fine-grained entity type definitions derived from the Few-NERD type ontology (Ding et al., 2021). Each definition is a one-sentence natural-language description (e.g., "person-actor: A person who performs in movies, TV shows, theater, or other entertainment productions").
- **MAVEN (ED):** 168 event type definitions based on FrameNet frame descriptions (Wang et al., 2020).
- **FewRel / DocRED (RE):** Wikidata property labels are used as type names (e.g., "place of birth," "country of origin"). The RE prompts list candidate relation names without additional definitions beyond the label itself.

Regarding the influence on findings: our SCS ablation (Appendix G) shows that name-only SCS yields equivalent predictive accuracy to name+definition SCS (r = 0.172 vs. 0.168 for MiniLM on FewRel pairwise correlations), suggesting that type-name similarity is the dominant confusability signal for the embedding-based metric.

For extraction performance, prior work (including the reference you cite, Li et al., EMNLP 2024) shows that definitions improve absolute performance. We expect definitions would shift the count-degradation curve upward but would not eliminate the confusability effect, because: (a) the RE results (where definitions are absent) show the strongest BCS signal, while NER (where definitions are present) shows a null; (b) the BCS–accuracy correlation already holds under our current prompts, which vary in definition inclusion across tasks. We add a brief note in the revision: "Type definitions may modulate absolute extraction quality but do not eliminate the confusability effect: the strongest BCS signal emerges in RE (no definitions), while the NER null (with definitions) reflects dispersed error modes rather than definition-based disambiguation."
