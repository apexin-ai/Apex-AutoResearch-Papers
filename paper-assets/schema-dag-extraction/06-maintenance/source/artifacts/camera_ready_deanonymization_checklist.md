# De-anonymization Checklist (Camera-Ready)

## LaTeX Configuration

- [ ] `main.tex` L3: `\usepackage[review]{acl}` → `\usepackage[final]{acl}`
  - Effect: disables anonymization, removes line numbers, removes page numbers

## Author Block

- [ ] `main.tex` L19: `\author{Anonymous}` → real author block with names, affiliations, emails
  - Template format:
    ```latex
    \author{
      Author One\textsuperscript{1} \and
      Author Two\textsuperscript{2} \\
      \textsuperscript{1}Affiliation One \\
      \textsuperscript{2}Affiliation Two \\
      \texttt{\{author1, author2\}@example.com}
    }
    ```

## Anonymous Repository URL

- [ ] `introduction.tex` L4 (footnote 2): `\url{https://anonymous.4open.science/r/schema-dag-extraction}` → real GitHub URL
  - Current text: "Code and data will be released upon acceptance. Anonymous review materials: \url{...}"
  - Camera-ready: "Code and data are available at \url{https://github.com/REAL_REPO_URL}"

## Checklist / Reproducibility

- [ ] `checklist.tex` L75: "Code and scripts will be released upon acceptance." → "Code and scripts are available at \url{...}."

## Acknowledgements

- [ ] Add `\section*{Acknowledgements}` before `\bibliography` in main.tex (see acknowledgements_draft.tex)

## Supplementary Material

- [ ] `supplementary.tex` L18: Verify "All supplementary material is included in the appendix" is still accurate
- [ ] If separate supplementary zip is required, prepare it per ARR camera-ready instructions

## Final Verification

- [ ] Compile with `[final]` option and verify: no line numbers, no page numbers, author names visible
- [ ] Verify no remaining "Anonymous" strings: `grep -ri "anonymous" *.tex`
- [ ] Verify no remaining anonymous URLs: `grep -ri "anonymous.4open" *.tex`
- [ ] Verify no "upon acceptance" / "will be released" language remains
