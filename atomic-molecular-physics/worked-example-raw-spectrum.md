# Numerical companion · From a processed spectrum to a conditional level scheme

[Unit 8](unit-8-putting-the-ideas-together.md) gives the physical investigation, proposed controls and limits of inference. This companion makes its arithmetic reproducible. The historical filename says “raw”; the supplied spectrum is a processed PypeIt wavelength-calibration template.

## What the source audit changes

The [CSV](data/hg-cd-ar-lamp-spectrum.csv) exactly reproduces the preserved upstream FITS columns after rounding. Its wavelength axis uses known reference lines. Four input exposures were continuum-subtracted, aligned, normalized separately and stitched. A value of 10000 is a normalization maximum, not established detector saturation. The old CSV header and older `measured-lines.csv` clipping flags are incorrect; both files remain unchanged as archive records. The [source audit](data/lamp-archive/README.md) documents this correction.

No raw detector variance, independent calibration uncertainty or intensity-response curve is supplied. The calculation therefore estimates centres for an illustration; it does not determine formal centroid errors or intrinsic branching strengths.

## Reproduce the candidate measurements

From the repository root, using Python and NumPy:

```sh
python3 atomic-molecular-physics/analysis/raw_spectrum_to_levels.py --no-plot --output-dir atomic-molecular-physics/data/lamp-analysis
```

This writes the current [candidate table](data/lamp-analysis/candidate-lines.csv) and [summary](data/lamp-analysis/analysis-summary.json). It finds 38 local-max candidates at the declared threshold; 31 pass the limited profile guards and seven fail. Thresholding is relative to the processed signal, not a statistical significance test. Other thresholds change the inventory.

The fit uses positive core samples in an eleven-sample window. Values at 10000 are included. It rejects insufficient samples, nonnegative curvature, misplaced vertices and widths inconsistent with the window. Remaining background, blending and profile mismatch can still bias an accepted estimate. Only seven reference transitions are compared; this script does not reproduce the older full-list identification table.

| Candidate | Estimated centre (Å, vacuum) | Reference input (Å, vacuum) |
|---|---:|---:|
| Cd ground-state anchor | 3261.9638 | 3261.9951 |
| Cd branch to ³P₀ | 4679.4463 | 4679.4587 |
| Cd branch to ³P₁ | 4801.2394 | 4801.2540 |
| Cd branch to ³P₂ | 5087.2581 | 5087.2393 |
| Hg branch to ³P₀ | 4047.7095 | 4047.7080 |
| Hg branch to ³P₁ | 4359.5965 | 4359.5600 |
| Hg branch to ³P₂ | 5462.2916 | 5462.2680 |

Digits are retained to reproduce the arithmetic, not to claim those uncertainties. The named lower states and shared upper states come from reference assignments. Agreement with references already used in the wavelength scale is not independent validation.

## Carry out the Ritz sums

Convert each estimated vacuum wavelength using

```math
\tilde\nu\ [\mathrm{cm}^{-1}]=\frac{10^8}{\lambda\ [\text{Å}]}.
```

If the three visible Cd branches share 5s6s ³S₁, their differences give

```math
\begin{aligned}
(E_{P_1}-E_{P_0})/(hc)&\simeq542.095\ \mathrm{cm}^{-1},\\
(E_{P_2}-E_{P_1})/(hc)&\simeq1171.001\ \mathrm{cm}^{-1}.
\end{aligned}
```

The proposed 326.2 nm transition anchors ³P₁ to the ground state. Add the branch to ³P₁ to obtain the common upper energy, then subtract the other branches:

| Cd level | Reconstructed energy / $`hc`$ (cm⁻¹) |
|---|---:|
| 5s5p ³P₀ | 30114.3 |
| 5s5p ³P₁ | 30656.4 |
| 5s5p ³P₂ | 31827.4 |
| 5s6s ³S₁ | 51484.3 |

These are conditional values without a formal uncertainty budget. Four transitions connect five levels: after fixing the ground energy, the graph has no independent cycle. Add a new upper state with two branches to existing levels; one branch fixes the new energy and the other tests a prediction.

The analogous Hg intervals are about 1767.428 and 4630.568 cm⁻¹. The 253.7 nm ground-state connection lies outside the recorded range, so this example supplies relative intervals only. Ratios of consecutive intervals are approximately 2.16 for Cd and 2.62 for Hg, compared with 2 in the simple LS interval model. Deviations motivate further coupling and measurement tests rather than uniquely identifying their cause.

## What the signal cannot establish here

The three Cd peak heights are not calibrated integrated photon counts. Even a pure-LS angular-strength ratio 1:3:5 would require frequency, population, collection and detector factors before comparison with a measurement. Separate normalization prevents a common physical intensity comparison across archive snippets. This calculation does not attribute a discrepancy uniquely to detector sensitivity or state mixing.

The fitted FWHM near 480 nm is about 1.70 Å, giving an apparent resolving power near 2800 only if an isolated instrumental profile dominates. Widths alone do not establish that condition or the atomic lifetime.

## Questions for the next measurement

- Which candidate survives an independently recorded single-element control?
- Which additional branch closes a Ritz cycle without being used to set the fitted energies?
- How could a field-dependent component pattern distinguish alternative angular-momentum labels?
- What calibration and retained exposure information would turn a branch-area ratio into a test of transition probabilities?

The archived input, legacy line table and older labelled figures are retained for traceability. Use the corrected Unit 8 figures and current diagnostics for the investigation.
