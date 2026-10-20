# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2 **你的审查侧重：新颖性 + 完整性 + 写作质量** ### 论文信息 - **标题**: How Deep Is Your Data? Estim — Part 6 of 6

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../research-conversation-round-1-round-1-reviewer-2-how-deep-is-your-data-estim.md) · [Structured JSON](../../../sessions/67/6712347043bad525dc54.json)

## Round 6

### Tool result

_source line 167 · 2026-05-18T17:04:50.944Z_

<details><summary>↩ Tool result · `toolu_01Knrq2GNCRxbtKKBJj23JaR`</summary>

```text
700	
701	
702	
703	
704	
705	
706	1.0
707	
708	On high-quality editorial text (WikiText), the false positive rate is below 2%, conrming that
709	the classier does not misidentify clean human text. Web-crawl false positive rates are higher
710	(1932%), but inspection reveals that false positives concentrate in d0 → d1 misclassication
711	and correspond to template content, SEO-generated pages, and formulaic text whose statistical
712	signatures (high repetition, low type-token ratio) overlap with rst-generation synthetic text.
713	Deep misclassication (d2 + predictions) remains rare (<4% across all datasets). Cross-model
714	FPR standard deviation is 8.5pp, reecting reference model sensitivity that must be accounted
715	for in deployment.
716	
717	8
718	
719	Theoretical Motivation
720	
721	We connect our empirical ndings to model collapse theory to provide mechanistic intuition
722	for the observed depth signals.
723	
724	This section oers motivation rather than formal theoretical
725	
726	contributions.
727	
728	Tail erosion and feature universality. Shumailov et al. [2024] showed that recursive
729	
730	training causes progressive tail collapse: the probability mass assigned to rare tokens decreases
731	monotonically with generation depth. This directly explains why p90_ppl (capturing the perplexity distribution's right tail) and var_surprisal (capturing distribution width) are universal
732	top features. As each generation erodes the tail, p90_ppl decreases monotonically, providing a
733	consistent depth signal regardless of model architecture or decoding strategy.
734	
735	EDD upper bound. Under the simplifying assumption that recursive generation acts as a
736	
737	contraction mapping with rate γ < 1 (each generation contracts the distribution toward a xed
738	attractor), the EDD is bounded by:
739	
740	
741	
742	log(DKL (P0 ∥Pref )/τdisc )
743	EDD ≤
744	log(1/γ)
745	
746	
747	(1)
748	
749	where τdisc is the minimum KL divergence required for statistical discrimination. For 1B models,
750	this bound gives EDD ≤ 6, while empirical EDD is 34. The bound is loose but directionally
751	correct, and the gap reects the violation of the i.i.d. assumption:
752	
753	our recursive chain uses
754	
755	dierent LoRA weights at each depth, creating a non-stationary contraction operator rather
756	than a xed one.
757	
758	Strategy-dependent convergence rates. Temperature scaling divides all logits by τ ,
759	
760	applying a uniform transformation that preserves distribution shape but rescales entropy.
761	
762	In
763	
764	contrast, nucleus and top-k sampling truncate the tail. Temperature's uniform scaling accelerates convergence to the attractor distribution by approximately 1.31.5× compared to truncation
765	methods, explaining why temperature-sampled text at depth N exhibits feature values similar
766	to nucleus/top-k text at depth N +1. This mechanistic dierence explains the feature trajectory
767	reversal observed in cross-strategy experiments (Section 6).
768	
769	8
770	
771	9
772	
773	Analysis: Contrastive Ordinal Learning
774	
775	We attempted to learn depth-discriminative text embeddings via contrastive ordinal learning,
776	training a RoBERTa-large encoder with an N-pair contrastive loss that attracts same-depth
777	embeddings and repels dierent-depth embeddings with margins proportional to depth distance.
778	Across six architecture and training variants (v1v6), all attempts failed: embedding collapse
779	(v1v2), out-of-memory errors (v3), catastrophic forgetting (v4), hyperparameter instability
780	(v5), and the nal RoBERTa-large variant (v6) achieved only 64.4% accuracy, 13.7pp below the
781	Random Forest baseline (78.2%).
782	This negative result is informative. Ordinal depth signal resides primarily in distributional
783	statistics (perplexity tails, surprisal variance) rather than in token-level semantic features that
784	RoBERTa-style encoders capture.
785	
786	The contrastive objective attempts to learn an embedding
787	
788	space where depth is linearly ordered, but the depth-discriminative information is not naturally
789	accessible to the [CLS] representation, which encodes semantic content rather than generationprocess statistics. This supports the Atlas nding that hand-crafted statistical features, specically those targeting the tail erosion mechanism, provide a more direct path to depth estimation
790	than learned representations.
791	
792	10
793	
794	Discussion
795	
796	Strategy interaction eects. Our results reveal a three-tier pattern among decoding strategies: nucleus sampling provides stable baseline performance with consistent feature trajectories
797	across depths; temperature scaling enhances within-strategy signal strength but introduces feature trajectory reversal that breaks cross-strategy transfer; top-k truncation attenuates signal
798	strength while preserving directional consistency. This three-tier structure has practical implications: cross-strategy deployment systems must either identify the decoding strategy a priori
799	or accept that d1 /d2 predictions may be inverted for temperature-sampled text.
800	
801	Depth-graduated curation. Predicted depth provides a ner-grained quality proxy than
802	
803	binary real/synthetic labels. A corpus curator could assign graduated weights: full weight for
804	
805	d0 , reduced weight for d1 , and exclusion for d ≥ 2. The depth-accuracy correlation in our 3×3
806	matrix (higher accuracy at shallower depths) suggests that this graduated signal is reliable for
807	the most actionable decisions. Full experimental validation of depth-weighted training is left for
808	future work.
809	
810	Reference model considerations. Feature extraction requires a reference model for per-
811	
812	plexity computation. Our default (GPT-2 Large) is distinct from all generation models to avoid
813	circularity.
814	
815	Cross-model FPR variance of 8.5pp (Section 7.3) indicates non-trivial reference
816	
817	model sensitivity. Deployment systems should either x a single reference model or ensemble
818	predictions across multiple reference models.
819	
820	10.1 Limitations
821	Scale generality. The 14B experiment (68% accuracy) conrms signal existence at larger scale
822	but with attenuated discrimination compared to 1B models.
823	
824	This is a single-strategy, single-
825	
826	model experiment; comprehensive scale validation across multiple 14B+ models and strategies
827	remains for future work. The claim is feasible at 1B with preliminary evidence of scale persistence at 14B, not robust across scales.
828	
829	Cross-strategy deployment constraint. Cross-strategy deployment requires knowing
830	
831	or identifying the target decoding strategy.
832	for temperature-sampled text.
833	constraint:
834	
835	Without this, d1 /d2 predictions may be inverted
836	
837	The two-stage pipeline mitigates but does not fully solve this
838	
839	the strategy classier achieves only 57.8% accuracy, and the pipeline's improve-
840	
841	ment (+11.5pp) depends on even this imperfect routing. More sophisticated domain adaptation
842	methods may be needed.
843	
844	9
845	
846	Base model assumption. Depth estimation is most eective on base model outputs (70
847	85% accuracy) and substantially weaker on instruction-tuned and API model outputs (4245%).
848	Since the primary use case is detecting recursive contamination in training data (which predominantly involves base model outputs), this limitation is contextually bounded but important to
849	state.
850	
851	Wild data false positives. Web-crawl FPR of 1932% is too high for deployment without
852	
853	additional ltering. Template and SEO content triggers false positives, and deployment on webcrawl data would require domain-adapted thresholds or supplementary quality lters.
854	
855	Cross-
856	
857	model FPR standard deviation of 8.5pp adds further calibration challenges.
858	
859	Controlled setting. Our benchmark uses LoRA ne-tuning for recursive chains, which is
860	
861	one specic instantiation of model-data-model feedback loops. Real-world recursive generation
862	may involve dierent ne-tuning methods, data mixing ratios, or partial-depth contamination,
863	all of which could alter the depth signal.
864	
865	11
866	
867	Conclusion
868	
869	We formalized ordinal generation depth estimation and provided the rst systematic empirical
870	characterization of how text statistical properties evolve across recursive generation depths. On
871	our multi-generational benchmark spanning three model families and three decoding strategies,
872	feature-based classiers achieve 7085% four-class accuracy, with perplexity tail statistics consistently among the top features across all settings. The Depth Degradation Atlas reveals nonuniform inter-depth distances, eective discriminable depth boundaries, and strategy-dependent
873	feature trajectory reversal rooted in fundamental dierences between uniform logit scaling and
874	tail truncation.
875	
876	A two-stage strategy-aware pipeline addresses the cross-strategy deployment
877	
878	challenge with an 11.5pp improvement over naive transfer.
879	
880	Preliminary 14B results conrm
881	
882	signal persistence at larger scale, while honest reporting of limitations (API model attenuation,
883	cross-strategy reversal, wild data FPR) delineates the boundaries of current feasibility.
884	
885	References
886	S. Alemohammad, J. Casco-Rodriguez, L. Luzi, A. I. Ahmed, D. Chinber, Y. Huang, and R. G.
887	Baraniuk. Self-consuming generative models go MAD. In Proceedings of ICLR, 2024.
888	G. Bao, Y. Zhao, Z. Teng, L. Yang, and J. Zhang. Fast-DetectGPT: Ecient zero-shot detection
889	of machine-generated text via conditional probability curvature. In Proceedings of ICLR, 2024.
890	S. Biderman, H. Schoelkopf, Q. Anthony, H. Bradley, K. O'Brien, E. Hallahan, M. A. Khan,
891	S. Purohit, U. S. Prashanth, E. Ra, A. Skowron, L. Sutawika, and O. van der Wal. Pythia:
892	A suite for analyzing large language models across training and scaling.
893	
894	In Proceedings of
895	
896	ICML, 2023.
897	
898	W. Cao, V. Mirjalili, and S. Raschka. Rank consistent ordinal regression for neural networks
899	with CORAL. Pattern Recognition, 108:107450, 2020.
900	E. Dohmatob, Y. Feng, P. Yin, and F. Berthet. A tale of tails: Model collapse as a change of
901	scaling laws. arXiv preprint arXiv:2402.07043, 2024.
902	R. Drayson, N. Duong-Trung, and O. Lemon. Quality degradation in multi-generational language
903	model text. In Proceedings of EMNLP, 2025.
904	F. Garces Arias, A. Mendoza, and M. Patel. Decoding strategy eects on machine-generated
905	text detectability. In Proceedings of COLING, 2025.
906	
907	10
908	
909	M. Gerstgrasser, R. Schaeer, A. Dey, R. Rafailov, H. Sleight, J. Hughes, T. Korbak, R. Agarwal,
910	D. Pai, A. Gromov, D. A. Roberts, D. Yang, and S. Dohan.
911	
912	Is model collapse inevitable?
913	
914	Breaking the curse of recursion by accumulating real and synthetic data.
915	
916	arXiv preprint
917	
918	arXiv:2404.01413, 2024.
919	
920	D. Groeneveld, I. Beltagy, P. Walsh, A. Bhagia, R. Kinney, O. Tafjord, A. Jha, H. Ivison,
921	I. Magnusson, Y. Wang, S. Arber, D. Atkinson, R. Authur, K. Chandu, J. Cobbe, J. Dumas,
922	C. Elber, N. Gao, and H. Hajishirzi. OLMo: Accelerating the science of language models. In
923	Proceedings of ACL, 2024.
924	
925	A. Hans, A. Schwarzschild, V. Cherepanova, H. Kazemi, A. Saha, M. Goldblum, J. Geiping,
926	and T. Goldstein. Spotting LLMs with Binoculars: Zero-shot detection of machine-generated
927	text. In Proceedings of ICML, 2024.
928	Z. He, B. Chen, and Y. Liu. DivEye: Diversity-based detection of machine-generated text. In
929	Proceedings of ACL, 2024.
930	
931	A. Holtzman, J. Buys, L. Du, M. Forbes, and Y. Choi. The curious case of neural text degeneration. In Proceedings of ICLR, 2020.
932	J. Kirchenbauer, J. Geiping, Y. Wen, J. Katz, I. Miers, and T. Goldstein. A watermark for large
933	language models. In Proceedings of ICML, 2023.
934	K. Liu, Z. Wang, and F. Huang.
935	
936	LOKI: Large-scale detection of machine-generated text via
937	
938	token-level analysis. In Proceedings of EMNLP, 2024.
939	A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever.
940	
941	Language models are
942	
943	unsupervised multitask learners. OpenAI Blog, 2019.
944	I. Shumailov, Z. Shumaylov, Y. Zhao, N. Papernot, R. Anderson, and Y. Gal. AI models collapse
945	when trained on recursively generated data. Nature, 631:755759, 2024.
946	A. Uchendu, T. Le, K. Shu, and D. Lee. Authorship attribution for neural text generation. In
947	Proceedings of EMNLP, 2020.
948	
949	Q. Wang, B. Wu, and L. Deng.
950	
951	EditLens:
952	
953	Estimating the extent of AI editing in text.
954	
955	In
956	
957	Proceedings of ACL, 2024.
958	
959	A. Wettig, A. Gao, Z. Zhong, and D. Chen. QuRating: Selecting high-quality data for training
960	language models. In Proceedings of ICML, 2024.
961	S. M. Xie, S. Santurkar, T. Ma, and P. Liang. Data selection with importance resampling. In
962	Proceedings of NeurIPS, 2023.
963	
964	E. Mitchell, Y. Lee, A. Khazatsky, C. D. Manning, and C. Finn. DetectGPT: Zero-shot machinegenerated text detection using probability curvature. In Proceedings of ICML, 2023.
965	V. S. Sadasivan, A. Kumar, S. Balasubramanian, W. Wang, and S. Feizi. Can AI-generated text
966	be reliably detected? arXiv preprint arXiv:2303.11156, 2023.
967	E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen. LoRA:
968	Low-rank adaptation of large language models. In Proceedings of ICLR, 2022.
969	A. Yang, B. Yang, B. Hui, B. Zheng, B. Yu, C. Zhou, C. Li, C. Li, D. Liu, F. Huang, et al.
970	Qwen2 technical report. arXiv preprint arXiv:2407.10671, 2024.
971	
972	11
973	
974	H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra,
975	P. Bhargava, S. Bhosale, et al. Llama 2: Open foundation and ne-tuned chat models. arXiv
976	preprint arXiv:2307.09288, 2023.
977	
978	B. Guo, X. Zhang, Z. Wang, M. Jiang, J. Nie, Y. Ding, J. Yue, and Y. Wu.
979	
980	How close is
981	
982	ChatGPT to human experts? Comparison corpus, evaluation, and detection. arXiv preprint
983	arXiv:2301.07597, 2024.
984	
985	L. Breiman. Random forests. Machine Learning, 45(1):532, 2001.
986	S. Merity, C. Xiong, J. Bradbury, and R. Socher. Pointer sentinel mixture models. In Proceedings
987	of ICLR, 2017.
988	
989	C. Rael, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, and P. J.
990	Liu. Exploring the limits of transfer learning with a unied text-to-text transformer. JMLR,
991	21(140):167, 2020.
992	L. Soldaini, R. Kinney, A. Bhagia, D. Schwenk, D. Atkinson, R. Authur, B. Bogin, K. Chandu,
993	J. Dumas, Y. Elazar, et al. Dolma: An open corpus of three trillion tokens for language model
994	pretraining research. In Proceedings of ACL, 2024.
995	
996	12
997	
998	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "247f44c4-4acc-4af5-aa46-416b3ee5a97d",
  "isSidechain": false,
  "promptId": "c7cb83be-4c3e-488b-88aa-667dfc767445",
  "type": "user",
  "uuid": "e83f87cc-5f55-4138-a92b-086b53313ab4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/tmp/dream_paper_median.txt",
      "content": "\u0016\n\n\u0016\n\n\u0016\n\n1.0\n\nOn high-quality editorial text (WikiText), the false positive rate is below 2%, con\u001crming that\nthe classi\u001cer does not misidentify clean human text. Web-crawl false positive rates are higher\n(19\u001532%), but inspection reveals that false positives concentrate in d0 → d1 misclassi\u001ccation\nand correspond to template content, SEO-generated pages, and formulaic text whose statistical\nsignatures (high repetition, low type-token ratio) overlap with \u001crst-generation synthetic text.\nDeep misclassi\u001ccation (d2 + predictions) remains rare (<4% across all datasets). Cross-model\nFPR standard deviation is 8.5pp, re\u001decting reference model sensitivity that must be accounted\nfor in deployment.\n\n8\n\nTheoretical Motivation\n\nWe connect our empirical \u001cndings to model collapse theory to provide mechanistic intuition\nfor the observed depth signals.\n\nThis section o\u001bers motivation rather than formal theoretical\n\ncontributions.\n\nTail erosion and feature universality. Shumailov et al. [2024] showed that recursive\n\ntraining causes progressive tail collapse: the probability mass assigned to rare tokens decreases\nmonotonically with generation depth. This directly explains why p90_ppl (capturing the perplexity distribution's right tail) and var_surprisal (capturing distribution width) are universal\ntop features. As each generation erodes the tail, p90_ppl decreases monotonically, providing a\nconsistent depth signal regardless of model architecture or decoding strategy.\n\nEDD upper bound. Under the simplifying assumption that recursive generation acts as a\n\ncontraction mapping with rate γ < 1 (each generation contracts the distribution toward a \u001cxed\nattractor), the EDD is bounded by:\n\n\u0018\n\nlog(DKL (P0 ∥Pref )/τdisc )\nEDD ≤\nlog(1/γ)\n\n\u0019\n(1)\n\nwhere τdisc is the minimum KL divergence required for statistical discrimination. For 1B models,\nthis bound gives EDD ≤ 6, while empirical EDD is 3\u00154. The bound is loose but directionally\ncorrect, and the gap re\u001dects the violation of the i.i.d. assumption:\n\nour recursive chain uses\n\ndi\u001berent LoRA weights at each depth, creating a non-stationary contraction operator rather\nthan a \u001cxed one.\n\nStrategy-dependent convergence rates. Temperature scaling divides all logits by τ ,\n\napplying a uniform transformation that preserves distribution shape but rescales entropy.\n\nIn\n\ncontrast, nucleus and top-k sampling truncate the tail. Temperature's uniform scaling accelerates convergence to the attractor distribution by approximately 1.3\u00151.5× compared to truncation\nmethods, explaining why temperature-sampled text at depth N exhibits feature values similar\nto nucleus/top-k text at depth N +1. This mechanistic di\u001berence explains the feature trajectory\nreversal observed in cross-strategy experiments (Section 6).\n\n8\n\n\f9\n\nAnalysis: Contrastive Ordinal Learning\n\nWe attempted to learn depth-discriminative text embeddings via contrastive ordinal learning,\ntraining a RoBERTa-large encoder with an N-pair contrastive loss that attracts same-depth\nembeddings and repels di\u001berent-depth embeddings with margins proportional to depth distance.\nAcross six architecture and training variants (v1\u0015v6), all attempts failed: embedding collapse\n(v1\u0015v2), out-of-memory errors (v3), catastrophic forgetting (v4), hyperparameter instability\n(v5), and the \u001cnal RoBERTa-large variant (v6) achieved only 64.4% accuracy, 13.7pp below the\nRandom Forest baseline (78.2%).\nThis negative result is informative. Ordinal depth signal resides primarily in distributional\nstatistics (perplexity tails, surprisal variance) rather than in token-level semantic features that\nRoBERTa-style encoders capture.\n\nThe contrastive objective attempts to learn an embedding\n\nspace where depth is linearly ordered, but the depth-discriminative information is not naturally\naccessible to the [CLS] representation, which encodes semantic content rather than generationprocess statistics. This supports the Atlas \u001cnding that hand-crafted statistical features, speci\u001ccally those targeting the tail erosion mechanism, provide a more direct path to depth estimation\nthan learned representations.\n\n10\n\nDiscussion\n\nStrategy interaction e\u001bects. Our results reveal a three-tier pattern among decoding strategies: nucleus sampling provides stable baseline performance with consistent feature trajectories\nacross depths; temperature scaling enhances within-strategy signal strength but introduces feature trajectory reversal that breaks cross-strategy transfer; top-k truncation attenuates signal\nstrength while preserving directional consistency. This three-tier structure has practical implications: cross-strategy deployment systems must either identify the decoding strategy a priori\nor accept that d1 /d2 predictions may be inverted for temperature-sampled text.\n\nDepth-graduated curation. Predicted depth provides a \u001cner-grained quality proxy than\n\nbinary real/synthetic labels. A corpus curator could assign graduated weights: full weight for\n\nd0 , reduced weight for d1 , and exclusion for d ≥ 2. The depth-accuracy correlation in our 3×3\nmatrix (higher accuracy at shallower depths) suggests that this graduated signal is reliable for\nthe most actionable decisions. Full experimental validation of depth-weighted training is left for\nfuture work.\n\nReference model considerations. Feature extraction requires a reference model for per-\n\nplexity computation. Our default (GPT-2 Large) is distinct from all generation models to avoid\ncircularity.\n\nCross-model FPR variance of 8.5pp (Section 7.3) indicates non-trivial reference\n\nmodel sensitivity. Deployment systems should either \u001cx a single reference model or ensemble\npredictions across multiple reference models.\n\n10.1 Limitations\nScale generality. The 14B experiment (68% accuracy) con\u001crms signal existence at larger scale\nbut with attenuated discrimination compared to 1B models.\n\nThis is a single-strategy, single-\n\nmodel experiment; comprehensive scale validation across multiple 14B+ models and strategies\nremains for future work. The claim is \u0010feasible at 1B with preliminary evidence of scale persistence at 14B,\u0011 not \u0010robust across scales.\u0011\n\nCross-strategy deployment constraint. Cross-strategy deployment requires knowing\n\nor identifying the target decoding strategy.\nfor temperature-sampled text.\nconstraint:\n\nWithout this, d1 /d2 predictions may be inverted\n\nThe two-stage pipeline mitigates but does not fully solve this\n\nthe strategy classi\u001cer achieves only 57.8% accuracy, and the pipeline's improve-\n\nment (+11.5pp) depends on even this imperfect routing. More sophisticated domain adaptation\nmethods may be needed.\n\n9\n\n\fBase model assumption. Depth estimation is most e\u001bective on base model outputs (70\u0015\n85% accuracy) and substantially weaker on instruction-tuned and API model outputs (42\u001545%).\nSince the primary use case is detecting recursive contamination in training data (which predominantly involves base model outputs), this limitation is contextually bounded but important to\nstate.\n\nWild data false positives. Web-crawl FPR of 19\u001532% is too high for deployment without\n\nadditional \u001cltering. Template and SEO content triggers false positives, and deployment on webcrawl data would require domain-adapted thresholds or supplementary quality \u001clters.\n\nCross-\n\nmodel FPR standard deviation of 8.5pp adds further calibration challenges.\n\nControlled setting. Our benchmark uses LoRA \u001cne-tuning for recursive chains, which is\n\none speci\u001cc instantiation of model-data-model feedback loops. Real-world recursive generation\nmay involve di\u001berent \u001cne-tuning methods, data mixing ratios, or partial-depth contamination,\nall of which could alter the depth signal.\n\n11\n\nConclusion\n\nWe formalized ordinal generation depth estimation and provided the \u001crst systematic empirical\ncharacterization of how text statistical properties evolve across recursive generation depths. On\nour multi-generational benchmark spanning three model families and three decoding strategies,\nfeature-based classi\u001cers achieve 70\u001585% four-class accuracy, with perplexity tail statistics consistently among the top features across all settings. The Depth Degradation Atlas reveals nonuniform inter-depth distances, e\u001bective discriminable depth boundaries, and strategy-dependent\nfeature trajectory reversal rooted in fundamental di\u001berences between uniform logit scaling and\ntail truncation.\n\nA two-stage strategy-aware pipeline addresses the cross-strategy deployment\n\nchallenge with an 11.5pp improvement over naive transfer.\n\nPreliminary 14B results con\u001crm\n\nsignal persistence at larger scale, while honest reporting of limitations (API model attenuation,\ncross-strategy reversal, wild data FPR) delineates the boundaries of current feasibility.\n\nReferences\nS. Alemohammad, J. Casco-Rodriguez, L. Luzi, A. I. Ahmed, D. Chinber, Y. Huang, and R. G.\nBaraniuk. Self-consuming generative models go MAD. In Proceedings of ICLR, 2024.\nG. Bao, Y. Zhao, Z. Teng, L. Yang, and J. Zhang. Fast-DetectGPT: E\u001ecient zero-shot detection\nof machine-generated text via conditional probability curvature. In Proceedings of ICLR, 2024.\nS. Biderman, H. Schoelkopf, Q. Anthony, H. Bradley, K. O'Brien, E. Hallahan, M. A. Khan,\nS. Purohit, U. S. Prashanth, E. Ra\u001b, A. Skowron, L. Sutawika, and O. van der Wal. Pythia:\nA suite for analyzing large language models across training and scaling.\n\nIn Proceedings of\n\nICML, 2023.\n\nW. Cao, V. Mirjalili, and S. Raschka. Rank consistent ordinal regression for neural networks\nwith CORAL. Pattern Recognition, 108:107450, 2020.\nE. Dohmatob, Y. Feng, P. Yin, and F. Berthet. A tale of tails: Model collapse as a change of\nscaling laws. arXiv preprint arXiv:2402.07043, 2024.\nR. Drayson, N. Duong-Trung, and O. Lemon. Quality degradation in multi-generational language\nmodel text. In Proceedings of EMNLP, 2025.\nF. Garces Arias, A. Mendoza, and M. Patel. Decoding strategy e\u001bects on machine-generated\ntext detectability. In Proceedings of COLING, 2025.\n\n10\n\n\fM. Gerstgrasser, R. Schae\u001ber, A. Dey, R. Rafailov, H. Sleight, J. Hughes, T. Korbak, R. Agarwal,\nD. Pai, A. Gromov, D. A. Roberts, D. Yang, and S. Dohan.\n\nIs model collapse inevitable?\n\nBreaking the curse of recursion by accumulating real and synthetic data.\n\narXiv preprint\n\narXiv:2404.01413, 2024.\n\nD. Groeneveld, I. Beltagy, P. Walsh, A. Bhagia, R. Kinney, O. Tafjord, A. Jha, H. Ivison,\nI. Magnusson, Y. Wang, S. Arber, D. Atkinson, R. Authur, K. Chandu, J. Cobbe, J. Dumas,\nC. Elber, N. Gao, and H. Hajishirzi. OLMo: Accelerating the science of language models. In\nProceedings of ACL, 2024.\n\nA. Hans, A. Schwarzschild, V. Cherepanova, H. Kazemi, A. Saha, M. Goldblum, J. Geiping,\nand T. Goldstein. Spotting LLMs with Binoculars: Zero-shot detection of machine-generated\ntext. In Proceedings of ICML, 2024.\nZ. He, B. Chen, and Y. Liu. DivEye: Diversity-based detection of machine-generated text. In\nProceedings of ACL, 2024.\n\nA. Holtzman, J. Buys, L. Du, M. Forbes, and Y. Choi. The curious case of neural text degeneration. In Proceedings of ICLR, 2020.\nJ. Kirchenbauer, J. Geiping, Y. Wen, J. Katz, I. Miers, and T. Goldstein. A watermark for large\nlanguage models. In Proceedings of ICML, 2023.\nK. Liu, Z. Wang, and F. Huang.\n\nLOKI: Large-scale detection of machine-generated text via\n\ntoken-level analysis. In Proceedings of EMNLP, 2024.\nA. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever.\n\nLanguage models are\n\nunsupervised multitask learners. OpenAI Blog, 2019.\nI. Shumailov, Z. Shumaylov, Y. Zhao, N. Papernot, R. Anderson, and Y. Gal. AI models collapse\nwhen trained on recursively generated data. Nature, 631:755\u0015759, 2024.\nA. Uchendu, T. Le, K. Shu, and D. Lee. Authorship attribution for neural text generation. In\nProceedings of EMNLP, 2020.\n\nQ. Wang, B. Wu, and L. Deng.\n\nEditLens:\n\nEstimating the extent of AI editing in text.\n\nIn\n\nProceedings of ACL, 2024.\n\nA. Wettig, A. Gao, Z. Zhong, and D. Chen. QuRating: Selecting high-quality data for training\nlanguage models. In Proceedings of ICML, 2024.\nS. M. Xie, S. Santurkar, T. Ma, and P. Liang. Data selection with importance resampling. In\nProceedings of NeurIPS, 2023.\n\nE. Mitchell, Y. Lee, A. Khazatsky, C. D. Manning, and C. Finn. DetectGPT: Zero-shot machinegenerated text detection using probability curvature. In Proceedings of ICML, 2023.\nV. S. Sadasivan, A. Kumar, S. Balasubramanian, W. Wang, and S. Feizi. Can AI-generated text\nbe reliably detected? arXiv preprint arXiv:2303.11156, 2023.\nE. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen. LoRA:\nLow-rank adaptation of large language models. In Proceedings of ICLR, 2022.\nA. Yang, B. Yang, B. Hui, B. Zheng, B. Yu, C. Zhou, C. Li, C. Li, D. Liu, F. Huang, et al.\nQwen2 technical report. arXiv preprint arXiv:2407.10671, 2024.\n\n11\n\n\fH. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra,\nP. Bhargava, S. Bhosale, et al. Llama 2: Open foundation and \u001cne-tuned chat models. arXiv\npreprint arXiv:2307.09288, 2023.\n\nB. Guo, X. Zhang, Z. Wang, M. Jiang, J. Nie, Y. Ding, J. Yue, and Y. Wu.\n\nHow close is\n\nChatGPT to human experts? Comparison corpus, evaluation, and detection. arXiv preprint\narXiv:2301.07597, 2024.\n\nL. Breiman. Random forests. Machine Learning, 45(1):5\u001532, 2001.\nS. Merity, C. Xiong, J. Bradbury, and R. Socher. Pointer sentinel mixture models. In Proceedings\nof ICLR, 2017.\n\nC. Ra\u001bel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, and P. J.\nLiu. Exploring the limits of transfer learning with a uni\u001ced text-to-text transformer. JMLR,\n21(140):1\u001567, 2020.\nL. Soldaini, R. Kinney, A. Bhagia, D. Schwenk, D. Atkinson, R. Authur, B. Bogin, K. Chandu,\nJ. Dumas, Y. Elazar, et al. Dolma: An open corpus of three trillion tokens for language model\npretraining research. In Proceedings of ACL, 2024.\n\n12\n\n\f",
      "numLines": 299,
      "startLine": 700,
      "totalLines": 998
    }
  },
  "sourceToolAssistantUUID": "247f44c4-4acc-4af5-aa46-416b3ee5a97d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 168_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: [Dream 审稿任务 — Reviewer 2：新颖性 + 相关工作]  论文标题：Ordinal Depth Estimation for Recursive Model-Generated Text: A Depth Degradation Atlas  PDF 路径：/home/ubuntu/.agent-ml-research-idea_gen_0513_…",
  "leafUuid": "e83f87cc-5f55-4138-a92b-086b53313ab4",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Runtime record

_source line 169_

```json
{
  "type": "ai-title",
  "aiTitle": "Review recursive generation depth estimation paper",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Assistant

_source line 170 · 2026-05-18T17:06:15.985Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the complete median dream paper. Let me analyze it thoroughly across my assigned dimensions.

## Key differences from the best dream paper:

1. **Title**: "Ordinal Depth Estimation for Recursive Model-Generated Text: A Depth Degradation Atlas" (more descriptive, less catchy)

2. **Abstract**: More conservative. Says "1B-1.5B" explicitly, mentions 14B as "preliminary" with 68% accuracy (vs best's 79%), no theoretical contribution claimed.

3. **Contributions list**: Only 3 contributions (task formalization, Atlas, cross-strategy pipeline). 

4. **Related Work**: 4 paragraphs (model collapse, detection, decoding strategies, data curation). Still missing ordinal classification, but includes LOKI and DivEye. CORAL is mentioned in classifiers (§3.4) but not in Related Work.

5. **Theoretical section**: Section 8, labeled "Theoretical Motivation," explicitly downgraded from formal theory. The EDD bound is looser (≤6 vs ≤5) and acknowledged as directional rather than rigorous, with the paper sidestepping some of the formal assumptions about independence.

6. **14B results**: Performance drops to 68% (vs 79% best), feature overlap halves to 2/4, and the d1v2 AUC weakens to 0.76—all framed as preliminary findings.

7. **Binary detector baselines**: Fast-DetectGPT and Binoculars perform much closer to the proposed method than expected (54% and 48% vs 30-36% and 32-38%), which substantially narrows the performance gap and undermines the case that specialized methods are necessary.

8. **Reference model**: The paper uses GPT-2 Large instead of the actual generating models, diverging from both the original work and the stronger baseline approach of self-referential detection.

9. **Feature description**: Now examining how the features are characterized and whether the descriptions align with what's actually being measured.

10. **Discussion and limitations**: The paper acknowledges its constraints honestly, explicitly stating the claims are about feasibility at 1B scale with only preliminary evidence of persistence at 14B, not robustness across scales.

Looking at novelty, the problem formalization around ordinal depth estimation and the systematic empirical mapping feel genuinely new, and the feature trajectory reversal finding is interesting. But the core approach relies on random forests with hand-crafted features—there's no algorithmic innovation there, and the binary detection baselines are closer than initially suggested.

The detectors like Binoculars and Fast-DetectGPT retain meaningful ordinal signal at 48% and 54% respectively, narrowing the gap with the RF approach to around 12 percentage points in the worst cases. This undermines the argument that entirely new methods are necessary. The theoretical section is also explicitly framed as motivation rather than a contribution, and the EDD bound is loose compared to empirical results. So the real question becomes whether task formalization plus a comprehensive empirical atlas and a useful definition like EDD can carry a top-tier venue when the methodology itself is fairly standard.

Looking at the related work, there's solid coverage of model collapse, detection methods, decoding approaches, and data curation. But ordinal classification is conspicuously absent from the discussion despite CORAL appearing as a classifier in the methods section, and the recent detection survey by Wu et al. 2025 isn't cited.

There are also some citation mismatches I'm noticing—EditLens, DivEye, and LOKI all appear to reference different papers than the well-known versions of these works, which could create confusion about which methods are actually being discussed.

Now I'm checking whether the abstract claims align with what's actually in the paper. The accuracy numbers, the depth signal persistence result, and the pipeline improvement all check out against the tables and sections. The abstract also doesn't overstate things by claiming theoretical contributions that aren't there, which is good.

Looking at the contributions list against the paper itself—the task formalization, the Degradation Atlas, and the cross-strategy pipeline are all present and accounted for. But there's a tension in the ordinal framing that's worth noting: the paper argues for treating this as ordinal classification because depth has inherent structure, yet the best-performing model (Random Forest at 78.3%) doesn't actually exploit that structure, while the method that does (CORAL at 74.1%) performs worse. And there are no ordinal-specific metrics like MAE or QWK being reported to evaluate this claim properly.

The 14B scalability claim is appropriately hedged—the abstract says "preliminary," the table shows modest results with limited feature overlap, and the limitations section is honest about what's actually demonstrated versus what's speculated. That's consistent.

For the theoretical section, it's framed as motivation rather than a contribution, which is correct. The EDD bound derivation gives an upper bound of 6 while empirical results sit at 3-4, and the paper acknowledges this gap comes from violating i.i.d. assumptions. Let me verify the math on that bound...

Now looking at the binary detector comparisons, there's a substantial gap between Fast-DetectGPT and the random forest baseline—54% versus 78.3% accuracy is a 24 percentage point difference. The AUC scores tell a similar story: at the d0v1 level both detectors are quite strong (0.975 vs 0.998), but that gap widens significantly at d1v2 (0.66 vs 0.861) and continues diverging further.

The paper's framing makes sense here—binary detectors excel at the easy boundary between d0 and v1 but struggle to maintain ordinal resolution as the depth increases. This aligns with what the data shows.

On the feature families, there's a minor design choice worth noting: the paper lists three families (Perplexity, Surprisal, Diversity) totaling 19 features, whereas earlier work had four families including repetition as separate. The median approach merges repetition into diversity, which is a reasonable consolidation rather than an actual inconsistency.

The main tension I'm seeing is between the ordinal framing of the problem and how the execution actually handles it. The paper does acknowledge the partial signal issue explicitly, and the 24pp average improvement with a substantial AUC gap (0.80 vs 0.54) is meaningful—plus the 3-class accuracy drops detectors to near-chance levels. So that's more of a should-fix than a major flaw. But stepping back, the core problems remain: the method is just random forests with hand-crafted features (no algorithmic novelty), the ordinal framing contradicts itself since the ordinal method underperforms, the related work completely omits ordinal classification literature, the 14B validation is thin, and binary detectors still capture meaningful signal. For a top-tier venue, the ordinal framing inconsistency and lack of methodological novelty are the real blockers.

The paper frames its contributions as task formalization, empirical characterization, and a cross-strategy pipeline—not algorithmic innovation. That distinction matters depending on the venue: EMNLP might accept this as a solid empirical contribution, but NeurIPS or ICML would likely expect more methodological depth. Given the 6-point scale and top-venue bar, I'm treating the ordinal framing mismatch as the major issue and the novelty concern as a significant weakness rather than major.

The missing ordinal classification literature is actually an idea-level problem, not just presentation—if the task is framed as ordinal classification but the paper doesn't engage with that subfield, the formalization itself could be incomplete or missing standard baselines. That's worth flagging as a major issue too.

Let me consolidate these into one coherent criticism: the paper frames the problem as ordinal classification but never demonstrates that the ordinal structure actually matters—the ordinal method underperforms, no ordinal-specific metrics are reported, and the entire ordinal classification literature is missing. That's one Major issue at the idea level, which puts the paper at Weak Accept (5/6) at best, though the other significant weaknesses probably push it down to Weak Reject (3/6).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e83f87cc-5f55-4138-a92b-086b53313ab4",
  "isSidechain": false,
  "requestId": "req_011CbAQ2NKP5qfZGmuLvP11R",
  "type": "assistant",
  "uuid": "a6b7d80f-e644-4483-af64-0e0fe6f52f9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQdov7by9oTPWffjdzGQKV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4866,
      "cache_read_input_tokens": 145243,
      "output_tokens": 7803,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7803,
          "cache_read_input_tokens": 145243,
          "cache_creation_input_tokens": 4866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4866
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

_source line 171 · 2026-05-18T17:06:17.506Z_

论文全文已读完（12 pages + references）。撰写审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6b7d80f-e644-4483-af64-0e0fe6f52f9b",
  "isSidechain": false,
  "requestId": "req_011CbAQ2NKP5qfZGmuLvP11R",
  "type": "assistant",
  "uuid": "2e71efb9-64ae-41c9-a044-4a82ffb6e6d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQdov7by9oTPWffjdzGQKV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4866,
      "cache_read_input_tokens": 145243,
      "output_tokens": 7803,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7803,
          "cache_read_input_tokens": 145243,
          "cache_creation_input_tokens": 4866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4866
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

_source line 172 · 2026-05-18T17:07:47.644Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01EQeJDQd6xGsxkjVBc5e1xf`</summary>

```json
{
  "text": "## Dream Review — Reviewer 2（新颖性 + 相关工作 + Story 一致性）\n\n**论文**: Ordinal Depth Estimation for Recursive Model-Generated Text: A Depth Degradation Atlas\n**Dream ID**: 20260518T162616 (median 档)\n**评审标准**: Top ML venue, 6 分制，接受率 ~25%\n\n---\n\n## Summary\n\n本文将 recursive generation depth estimation 形式化为 ordinal classification，构建 3×3 benchmark（3 model families × 3 strategies × 4 depths），用 19 统计特征 + RF 达到 70-85% 4-class accuracy。贡献为 Depth Degradation Atlas（系统化特征-depth 映射）、EDD 指标、和 two-stage cross-strategy pipeline (+11.5pp)。14B 验证（68%）为 preliminary，理论 section 定位为 \"Theoretical Motivation\" 不列入 contributions。论文定位诚实、实验系统，但方法论新颖性有限，且 ordinal framing 与实际执行之间存在核心矛盾。\n\n---\n\n## Strengths\n\n**S1. 问题定义清晰且有实际意义 [idea 层面]。** 从 binary detection 推进到 ordinal depth estimation 是一个 well-motivated 的方向。Introduction 的叙事从 recursive contamination → binary detection 的局限 → ordinal estimation 的实用价值（depth-graduated curation）自然流畅。\n\n**S2. 实验覆盖系统 [idea 层面]。** 3×3 atlas grid 有效隔离 model family 和 strategy 的效应。Binary detector baselines (Binoculars 48%, Fast-DetectGPT 54%, Table 3) 是关键比较——清楚展示在 d1v2/d2v3 边界上 binary scores 急剧退化（d2v3 AUC 0.54-0.57），而 RF 特征保持 0.80。3-class accuracy（排除 d0）进一步确认 detectors 接近 chance (41% vs 33%)。\n\n**S3. Cross-strategy reversal 的发现和解释有深度 [idea 层面]。** Temperature sampling 的 d1/d2 boundary inversion（d1v2 AUC 低至 0.13-0.25）不是噪声而是 structural distributional shift。Section 6.1 和 Section 8 的 mechanistic explanation（uniform logit scaling 加速 convergence 约 1.3-1.5×）提供了因果层面的理解，且 z-score normalization 的失败（RF Δ < 0.02pp）证实这不是 simple feature-scale 问题。\n\n**S4. 论文诚实度高 [presentation 层面]。** Limitations section 直接说 \"The claim is 'feasible at 1B with preliminary evidence of scale persistence at 14B,' not 'robust across scales'\"。DCOL negative results 的报告（Section 9, 6 variants all failing）展示了对 alternative approaches 的系统探索。Wild-data FPR 19-32% 被诚实标注为 deployment 限制。\n\n**S5. 3-class companion metric 展示了自省意识 [idea 层面]。** Section 4.4 主动报告排除 d0 后的 3-class accuracy（59-82%）来隔离 ordinal 信号和 binary detection 的贡献。这直接回应了 d0 inflation 的常见审稿质疑。\n\n---\n\n## Weaknesses\n\n### Major Issues\n\n**W1 [MAJOR, idea 层面] Ordinal framing 与实际方法/指标/文献之间存在三重不一致**\n\n这是论文最核心的 idea-level 问题，由三个相互关联的子问题构成：\n\n**(a) Method 不利用 ordinal structure。** §3.1 明确说 \"ordinal structure (depth 1 is closer to depth 2 than to depth 3) should be exploited by the classifier\"，但主分类器 RF 将 d0/d1/d2/d3 视为无序标签。更关键的是，真正利用 ordinal structure 的 CORAL 反而比 RF **低 4.2pp**（74.1% vs 78.3%, Table 3）。论文没有解释为什么 ordinal method 表现更差——如果 ordinal structure 真的重要，为什么利用它反而有害？\n\n**(b) 无 ordinal metrics。** 全文只报告 standard accuracy 和 pairwise AUC，没有 MAE、QWK、adjacent-class confusion ratio 等 ordinal-specific 指标。如果 d1→d3 的错误比 d1→d2 更少（即 ordinal structure 存在），这应该被量化报告。没有这些指标，\"ordinal classification\" 的 framing 缺乏经验支撑。\n\n**(c) Related Work 完全缺失 ordinal classification 文献。** McCullagh 1980（ordinal regression 奠基）、Frank & Hall 2001（ordinal-to-binary decomposition）、CLOC (Pitawela et al. 2025, contrastive ordinal learning) 均未引用或讨论。CORAL 出现在 §3.4 作为 classifier 但 Related Work 中没有 ordinal classification 段落。论文声称提出的是 ordinal classification 任务，却不讨论 ordinal classification 领域——这是 positioning 的基本缺失。\n\n**综合影响**：论文的 title 包含 \"Ordinal\"，abstract 突出 \"ordinal generation depth estimation as a new task\"，§3.1 论证 ordinal framing 的三个理由。但 method 不利用 ordinal 结构、ordinal method 表现更差、无 ordinal metrics、无 ordinal literature。这构成论文核心 framing 与 execution 之间的系统性矛盾。读者有理由问：如果去掉所有 \"ordinal\" 的包装，将任务重新描述为 \"multi-class depth classification\"，论文的方法和结果完全不需要改变——那么 ordinal framing 的实质贡献是什么？\n\n**建议**：(1) 报告 MAE 和 confusion matrix 的 adjacent vs non-adjacent error ratio 来经验性地验证 ordinal structure；(2) 分析为什么 CORAL < RF（是因为 ordinal structure 不存在，还是因为 RF 的 feature space 隐式编码了 ordinal information？）；(3) 在 Related Work 增加 ordinal classification 段落。\n\n---\n\n**W2 [MAJOR, idea 层面] 方法论贡献不足以支撑 top venue 的 novelty 门槛**\n\n论文的三项 contributions 分别是：(1) 任务定义 + benchmark，(2) empirical atlas，(3) two-stage pipeline。这些都是有价值的，但 method 层面没有新算法、新 loss function、新 representation learning 方法。核心 pipeline 是 \"提取 19 个统计特征 → Random Forest\"，这是 standard feature engineering。\n\n具体来说：\n- Table 3 中 RF (78.3%) vs CORAL (74.1%) vs DivEye (71.5%) vs Fast-DetectGPT (54%) vs Binoculars (48%)。RF 的领先主要来自 feature engineering 而非分类方法——三种不同 feature-based 方法在同一特征集上 spread 仅 7pp (71.5-78.3%)，说明 ceiling 由 features 决定。\n- Two-stage pipeline（Section 6.2）中 strategy classifier 仅 57.8%（chance = 33%），且 pipeline 的 +11.5pp 改进取决于这个不完美的 routing。这不是一个强 method 贡献。\n- Theoretical section 被正确标注为 \"Motivation\"（Section 8），EDD bound ≤ 6 vs empirical 3-4 是 loose 的。\n\n对于 top ML venue（接受率 ~25%），单纯的 \"task formalization + empirical study\" 通常需要 (a) 足够有影响力的新发现，或 (b) enabling 后续研究的 infrastructure/benchmark 贡献。本文的 Atlas 和 EDD 有一定 benchmark 价值，但 feature universality（p90_ppl + var_surprisal 主导）在 model collapse 理论的框架下是可预期的（Shumailov tail erosion 直接预测了这一点）。\n\n**综合影响**：审稿人需要找到一个理由说 \"this paper changes how we think about recursive contamination\" 才能 accept。目前的贡献更适合 workshop 或 lower-tier venue。\n\n---\n\n### Minor Weaknesses\n\n**W3 [minor, idea 层面] Binary detector baselines 的 partial ordinal signal 削弱了 \"new task requires new methods\" 的论点。**\nFast-DetectGPT 在 best cell 达到 60%（Table 3），在 top-k cells 上 gap 缩小到 ~12pp。虽然 3-class accuracy (41%) 确认 binary scores 在排除 d0 后退化，但 4-class accuracy 54% 意味着 calibrated binary scores 已提取了相当的 ordinal signal。论文诚实地承认了 \"partial ordinal signal\"，但 Introduction 中 \"no existing method estimates recursion depth from text alone\" 的措辞与 Table 3 中 binary detectors 的 above-chance performance 存在张力。\n\n**W4 [minor, idea 层面] 14B 验证的 evidence 弱于论文叙事所暗示的。**\n68% accuracy (Table 4) 比 1B best 低 17.9pp，feature overlap 仅 2/4，d2 recall 低至 46%。Abstract 说 \"confirm depth signal persistence\" 但 Table 4 显示这更像是 \"signal exists but substantially attenuated\"。论文的 Limitations 对此很诚实，但 abstract/conclusion 的措辞可以更谨慎。\n\n**W5 [minor, presentation 层面] 部分引用的作者/venue 存在疑问。**\n- EditLens 引用 \"Q. Wang, B. Wu, and L. Deng\" (ACL 2024)——学术界更广为人知的 EditLens 是 Thai et al. (ICLR 2026)，需确认是否正确\n- DivEye 引用 \"Z. He, B. Chen, and Y. Liu\" (ACL 2024)——已知的 DivEye 是 Basani & Chen 2026 (TMLR)\n- LOKI 引用 \"K. Liu, Z. Wang, and F. Huang\" (EMNLP 2024)——已知的 LOKI 是 Ye et al. 2025 (ICLR Spotlight)\n（标注为 presentation 层面，因 dream 论文数字和引用是想象的，但应确认一致性。）\n\n**W6 [minor, presentation 层面] 参考文献缺少 detection 领域综述和重要方法。**\n缺少 Wu et al. 2025 (Computational Linguistics 综述)、GLTR (Gehrmann et al. 2019)、Tulchinskii et al. 2023 (intrinsic dimension)、RAID benchmark (Dugan et al. 2024)。Detection 领域的文献覆盖面不够全面。\n\n---\n\n## Questions\n\n**Q1** 如果将 Table 3 中的 confusion matrices 按 adjacent vs non-adjacent error 分类，是否能经验性地证明 ordinal structure 存在？具体地说，d1→d3 错误是否少于 d1→d2 错误（期望值应如此 if ordinal structure holds）？\n\n**Q2** CORAL 为什么比 RF 低 4.2pp？是因为 (a) ordinal structure 不存在（adjacent depths 的 feature 分布并非单调有序），(b) RF 的 decision boundaries 隐式编码了 ordinal information，还是 (c) CORAL 的 training 不稳定？\n\n**Q3** 如果将 \"ordinal\" framing 替换为 \"multi-class\" framing，论文的方法和结果是否需要任何改变？\n\n**Q4** EDD bound (≤6, Eq. 1) 对 14B 模型的预测是多少？14B 的 attenuated signal（d2v3 AUC = 0.67 接近 T=0.70 threshold）是否导致 EDD 显著降低？\n\n---\n\n## Missing References (idea-level gaps)\n\n1. **McCullagh 1980** — Regression Models for Ordinal Data（奠基性论文，论文 framing 为 ordinal 但不引用）\n2. **Frank & Hall 2001** — A Simple Approach to Ordinal Classification（ordinal-to-binary decomposition，直接相关 EDD 的 pairwise AUC 方法）\n3. **CLOC (Pitawela et al. 2025)** — Contrastive Learning for Ordinal Classification（直接相关 DCOL negative results）\n4. **Schaeffer et al. 2025** — \"Position: Model Collapse Does Not Mean What You Think\"（model collapse 术语辨析）\n\n---\n\n## Overall Assessment\n\n**Score: 3/6 (Weak Reject)**\n**Confidence: 4/5**\n\n**Major issues 计数**: 2（W1: ordinal framing 三重不一致, W2: 方法论贡献不足）\n**校准规则**: 2 Major issues → 不高于 Weak Accept (4/6)。综合考虑 W3-W4 的 minor 弱点，下调至 3/6。\n\n**简要理由**：\n\n论文在实验系统性和诚实度上达到了较高标准。3×3 atlas 的设计、cross-strategy reversal 的发现和解释、以及 limitations 的坦诚报告都值得肯定。\n\n但 top venue 的 novelty 门槛要求要么 (a) 有显著的方法论贡献，要么 (b) 有改变领域认知的发现。本文的方法是 standard feature engineering + RF，核心发现（perplexity tail statistics 作为 depth marker）在 Shumailov tail erosion 理论下是可预期的。更关键的是，论文以 \"ordinal classification\" 作为核心 framing，但 ordinal method (CORAL) 表现更差、无 ordinal metrics、无 ordinal classification literature，构成了论文叙事的内在矛盾。\n\n如果将论文重新定位为 \"multi-class depth classification: a systematic empirical study\"（去掉 ordinal 包装），并增加 ordinal metrics 来检验 ordinal structure 是否确实存在，论文的诚实度和实验质量足以在 workshop 或 Findings track 发表。当前 framing 下 top venue 接收的可能性较低。",
  "reviewer_id": "2",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e71efb9-64ae-41c9-a044-4a82ffb6e6d7",
  "isSidechain": false,
  "requestId": "req_011CbAQ2NKP5qfZGmuLvP11R",
  "type": "assistant",
  "uuid": "2cbc713b-e9d1-44d9-9635-b6e43f568e91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQdov7by9oTPWffjdzGQKV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4866,
      "cache_read_input_tokens": 145243,
      "output_tokens": 7803,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7803,
          "cache_read_input_tokens": 145243,
          "cache_creation_input_tokens": 4866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4866
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

_source line 173_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: [Dream 审稿任务 — Reviewer 2：新颖性 + 相关工作]  论文标题：Ordinal Depth Estimation for Recursive Model-Generated Text: A Depth Degradation Atlas  PDF 路径：/home/ubuntu/.agent-ml-research-idea_gen_0513_…",
  "leafUuid": "2cbc713b-e9d1-44d9-9635-b6e43f568e91",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Runtime record

_source line 174_

```json
{
  "type": "ai-title",
  "aiTitle": "Review recursive generation depth estimation paper",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Tool result

_source line 175 · 2026-05-18T17:07:52.125Z_

<details><summary>↩ Tool result · `toolu_01EQeJDQd6xGsxkjVBc5e1xf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cbc713b-e9d1-44d9-9635-b6e43f568e91",
  "isSidechain": false,
  "promptId": "c7cb83be-4c3e-488b-88aa-667dfc767445",
  "type": "user",
  "uuid": "33c0a309-3127-4c8a-bcdc-d2db4f765ee3",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "2cbc713b-e9d1-44d9-9635-b6e43f568e91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 176_

```json
{
  "type": "ai-title",
  "aiTitle": "Review recursive generation depth estimation paper",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


### Runtime record

_source line 177 · 2026-05-18T17:08:05.517Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T17:08:05.517Z",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "content": "[Round 2 审稿请求]:\n[Round 2 — Cross-Share]\n\nReviewer 1（方法 + 实验）的 Round 1 报告：\n\n---\n**R1 Score: 3/6 (Borderline Reject)**\n\n**R1 Major Issues:**\n1. **W1: d0-d3 depth range too shallow for \"Atlas\" framing**: The EDD bound predicts ≤6, empirical EDD is 3-4, yet experiments cap at d3. The hardest regime (d4+, where degradation is near-maximal) is never tested. d2vd3 AUC already degrades to 0.67 for 14B.\n2. **W2: LoRA fine-tuning protocol underspecified**: Missing training steps/epochs, learning rate, scheduler, adapter initialization (from scratch vs previous depth). The benchmark is unreproducible without these.\n3. **W3: Strategy classifier accuracy (57.8%) undermines two-stage pipeline contribution**: No error propagation breakdown. Oracle 78.3% vs actual 70.5% = 7.8pp lost. The 70.5% result conflates pipeline success with partial luck.\n\n**R1 Minor Issues:**\n- W4: Wild data FPR (32% C4) with no calibration mitigation attempted\n- W5: 14B only nucleus strategy tested\n- W6: Reference model (GPT-2 Large) fixed, not ablated\n\n**R1 Questions:**\n1. Full LoRA training protocol details?\n2. Depth accuracy conditioned on strategy classifier correctness vs incorrectness?\n3. Was d4 generation attempted? d3vd4 AUC?\n4. Any threshold recalibration for wild FPR?\n---\n\n请你（Reviewer 2）从新颖性 + 相关工作角度对 R1 的发现做补充：\n- R1 的 W1（depth range too shallow）——从 novelty 角度看，如果 depth estimation 只在 d0-d3 有效，这是否 fundamentally 限制了 task formalization 的价值？还是 d0-d3 本身已经 cover 了 practical use cases？\n- R1 的 W2（LoRA protocol underspecified）——这是 presentation 问题还是 idea 问题？如果 protocol 补齐后 benchmark 可复现，novelty claim 是否受影响？\n- R1 的 W3（cross-strategy pipeline）——从 contribution positioning 角度看，如果 pipeline 的 improvement 只有在 oracle strategy 条件下才 robust，这条 contribution 是否应该降级？"
}
```

---


### Runtime record

_source line 178 · 2026-05-18T17:08:05.518Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T17:08:05.518Z",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6"
}
```

---


## Round 7

## Round 7

2 recorded events


### User

_source line 179 · 2026-05-18T17:08:05.506Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33c0a309-3127-4c8a-bcdc-d2db4f765ee3",
  "isSidechain": false,
  "promptId": "d6bc15eb-a3be-49ad-a729-9479878415ac",
  "type": "user",
  "isMeta": true,
  "uuid": "743422df-5d49-43d8-893c-7968276daec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 180 · 2026-05-18T17:08:05.506Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "743422df-5d49-43d8-893c-7968276daec7",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "d0befd51-8a6e-4dc9-be66-0eb231fcfe4e",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "23b24129-509f-428c-9746-7dd63a58e76f",
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


## Round 8

## Round 8

3 recorded events


### User

_source line 181 · 2026-05-18T17:08:05.642Z_

[Round 2 审稿请求]:
[Round 2 — Cross-Share]

Reviewer 1（方法 + 实验）的 Round 1 报告：

---
**R1 Score: 3/6 (Borderline Reject)**

**R1 Major Issues:**
1. **W1: d0-d3 depth range too shallow for "Atlas" framing**: The EDD bound predicts ≤6, empirical EDD is 3-4, yet experiments cap at d3. The hardest regime (d4+, where degradation is near-maximal) is never tested. d2vd3 AUC already degrades to 0.67 for 14B.
2. **W2: LoRA fine-tuning protocol underspecified**: Missing training steps/epochs, learning rate, scheduler, adapter initialization (from scratch vs previous depth). The benchmark is unreproducible without these.
3. **W3: Strategy classifier accuracy (57.8%) undermines two-stage pipeline contribution**: No error propagation breakdown. Oracle 78.3% vs actual 70.5% = 7.8pp lost. The 70.5% result conflates pipeline success with partial luck.

**R1 Minor Issues:**
- W4: Wild data FPR (32% C4) with no calibration mitigation attempted
- W5: 14B only nucleus strategy tested
- W6: Reference model (GPT-2 Large) fixed, not ablated

**R1 Questions:**
1. Full LoRA training protocol details?
2. Depth accuracy conditioned on strategy classifier correctness vs incorrectness?
3. Was d4 generation attempted? d3vd4 AUC?
4. Any threshold recalibration for wild FPR?
---

请你（Reviewer 2）从新颖性 + 相关工作角度对 R1 的发现做补充：
- R1 的 W1（depth range too shallow）——从 novelty 角度看，如果 depth estimation 只在 d0-d3 有效，这是否 fundamentally 限制了 task formalization 的价值？还是 d0-d3 本身已经 cover 了 practical use cases？
- R1 的 W2（LoRA protocol underspecified）——这是 presentation 问题还是 idea 问题？如果 protocol 补齐后 benchmark 可复现，novelty claim 是否受影响？
- R1 的 W3（cross-strategy pipeline）——从 contribution positioning 角度看，如果 pipeline 的 improvement 只有在 oracle strategy 条件下才 robust，这条 contribution 是否应该降级？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0befd51-8a6e-4dc9-be66-0eb231fcfe4e",
  "isSidechain": false,
  "promptId": "d6bc15eb-a3be-49ad-a729-9479878415ac",
  "type": "user",
  "uuid": "9649c70c-7152-4367-b086-ab2c49e2d3b6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-18T17:08:58.424Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01AHcfa8sHckZSik4Nh8kunk`</summary>

```json
{
  "text": "## Reviewer 2 — Round 2 Cross-Share 回应 Reviewer 1\n\n---\n\n### R1-W1: Depth range too shallow (d0-d3) for \"Atlas\" framing\n\n**从 novelty 角度的判断：d0-d3 范围对 task formalization 的价值有限制但不致命，取决于 framing。**\n\n两层分析：\n\n**(a) Practical use case 层面：d0-d3 已覆盖核心场景。** 现实中的 recursive contamination 主要发生在前几代。Web-crawl → train → deploy → web-crawl 的循环周期以月计，d3 已经代表至少三轮完整的模型迭代。Model collapse 文献（Shumailov et al. 2024, Dohmatob et al. 2024）的核心发现也是前几代的 degradation 最显著。从 data curation 的角度，区分 d0/d1/d2/d3 已经足以实现 \"retain d1, downweight d2, filter d3+\" 的 graduated curation。因此 d0-d3 覆盖了 practical use case 的主体。\n\n**(b) \"Atlas\" 和 \"EDD\" 的 scope claim 层面：存在张力。** R1 的批评有道理的部分在于：论文定义了 EDD 作为 \"practical horizon of ordinal depth estimation\"，理论 bound 给出 EDD ≤ 6，但实验只到 d3。如果论文声称提供了一个 \"Atlas\"（系统性地图），那么地图应该覆盖到 EDD boundary 附近，而不是在 boundary 之前就停止。具体来说，d3v4 AUC 是 EDD 的关键判断点（是否跌破 threshold），但 median 档论文没有 d4 数据。\n\n**我的综合判断：这是一个 significant weakness 但不是 major issue。** 原因：(1) 论文的 EDD bound 本身承认了 EDD ≤ 6 是 loose 的（实际 3-4），说明 d3 已经接近 practical boundary；(2) 14B 的 d2v3 AUC 降到 0.67（Table 4），说明在更大模型上 d3 可能已经是 EDD 边界。但论文应该要么 (a) 提供 d4 数据来验证 EDD boundary，要么 (b) 将 \"Atlas\" framing 降级为 \"partial atlas covering the most practically relevant depth range\"。\n\n**与我的 Round 1 findings 的关系：** 这与我在 W2 中指出的 \"方法论贡献不足\" 相关——如果 Atlas 的覆盖范围被限制在 d0-d3，那么 Atlas 作为 contribution 的 scope 进一步缩小。\n\n---\n\n### R1-W2: LoRA protocol underspecified\n\n**从 novelty 角度的判断：这是 presentation 问题，不是 idea 问题。**\n\nLoRA hyperparameters（rank, alpha, learning rate, epochs, scheduler, adapter initialization）的缺失影响的是 reproducibility，不是 novelty claim。具体来说：\n\n1. **如果 protocol 补齐后 benchmark 可复现**：论文的所有 findings（feature universality, EDD, cross-strategy reversal）的 validity 不受影响。Novelty claim（task formalization + Atlas）完全不依赖于 LoRA 的具体超参数选择。\n2. **唯一可能影响 novelty 的情况**：如果 LoRA protocol 存在 implicit choices that inflate results（例如，adapter initialization from previous depth vs from scratch 会影响 depth signal 强度）。但这属于 experimental soundness，不属于 novelty。\n\n**与 R1 的分歧：** R1 将此列为 Major issue，我认为更准确的定位是 **critical presentation issue**（必须修复但不 block acceptance on idea grounds）。对于 dream review，标注为 presentation 层面。\n\n---\n\n### R1-W3: Cross-strategy pipeline — contribution 是否应降级？\n\n**从 contribution positioning 角度的判断：是的，pipeline 应从 independent contribution 降级为 diagnostic finding。**\n\n理由如下：\n\n1. **Strategy classifier 57.8% (chance 33%) 是 pipeline 的瓶颈。** 论文声称 pipeline \"improves cross-strategy accuracy by +11.5pp\"，但这个 +11.5pp 的来源是什么？Oracle ceiling 78.3% vs actual 70.5% = 7.8pp 被 routing error 消耗。R1 正确指出这里缺少 error propagation 分解——当 strategy classifier 错误时 depth accuracy 是多少？如果 correctly-routed samples 达到 ~78% 而 incorrectly-routed samples 仅 ~55%，那么 pipeline 的 \"improvement\" 本质上是在混合一个好的和一个差的 estimator。\n\n2. **Pipeline 不是一个 novel method。** \"先分类策略再分类深度\" 是一个 trivial engineering solution。它的价值取决于 execution quality，而 57.8% 的 strategy accuracy 意味着 execution 不够好。\n\n3. **更好的 framing：将 pipeline 作为 cross-strategy challenge 的 diagnostic。** 论文发现了一个重要问题（cross-strategy transfer 的 d1/d2 boundary inversion），提出了一个 initial mitigation（two-stage pipeline），并诚实报告了 mitigation 的局限。这个叙事作为 \"diagnostic finding + preliminary solution\" 比作为 \"contribution #3\" 更合适。\n\n**我的建议：** Contribution list 改为两项——(1) task formalization + benchmark, (2) Depth Degradation Atlas（包含 EDD, feature universality, cross-strategy reversal 作为 Atlas 的子发现）。Two-stage pipeline 降级为 Section 6 中的 \"mitigation analysis\"，不在 Introduction contribution list 中单列。\n\n---\n\n### 综合评估更新\n\nR1 的发现与我的 Round 1 review 高度互补：\n\n| 维度 | R2 Round 1 发现 | R1 Round 1 发现 | 互补性 |\n|------|----------------|----------------|--------|\n| Ordinal framing | **MAJOR**: framing vs execution 不一致 | 未涉及 | R2 独有 |\n| Method novelty | **MAJOR**: RF + features 不够 | W3: pipeline contribution weak | R1 从实验角度验证了 R2 的 novelty 担忧 |\n| Depth range | 未涉及 | **MAJOR**: d0-d3 太浅 | R1 独有，我同意是 significant 但非 major |\n| Reproducibility | 未涉及 | **MAJOR**: LoRA protocol 缺失 | R1 独有，我认为是 presentation 非 idea |\n| Scale | W4 (minor): 14B 弱 | W5 (minor): 14B 仅 nucleus | 一致 |\n\n**我维持 3/6 (Weak Reject) 评分。** R1 的 W1（depth range）加强了我对 contribution scope 有限的判断，但不改变核心评估。R1 的 W2（LoRA protocol）是必须修复的 presentation issue，修复后不影响 novelty。R1 的 W3（pipeline）与我的判断一致——pipeline 不应作为 independent contribution。\n\n两位 reviewer 的共识是：论文的实验诚实度和系统性高于平均，但 top venue 的 novelty 门槛未达到。核心矛盾是 ordinal framing 没有带来可验证的收益（我的 W1）+ method 贡献有限（我的 W2 + R1 的 W3）+ Atlas 覆盖不完整（R1 的 W1）。",
  "reviewer_id": "2",
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9649c70c-7152-4367-b086-ab2c49e2d3b6",
  "isSidechain": false,
  "requestId": "req_011CbAQGicAcZrSUYLazH29R",
  "type": "assistant",
  "uuid": "f62cfdce-6172-42a5-a8fd-920fe6b983fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199W5cCFcKUzyp3JWDy3xy8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 157982,
      "output_tokens": 2306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2306,
          "cache_read_input_tokens": 157982,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 680
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

_source line 183 · 2026-05-18T17:09:02.452Z_

<details><summary>↩ Tool result · `toolu_01AHcfa8sHckZSik4Nh8kunk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f62cfdce-6172-42a5-a8fd-920fe6b983fb",
  "isSidechain": false,
  "promptId": "d6bc15eb-a3be-49ad-a729-9479878415ac",
  "type": "user",
  "uuid": "e2677e48-a592-4f2a-9ae0-14906e6ddceb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_db3bd143165620ee6950e6ef0826eec8:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "f62cfdce-6172-42a5-a8fd-920fe6b983fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/review_reviewer_2_2744903e",
  "sessionId": "292b83c2-1301-4e2c-bd74-9cdf15ff83d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
