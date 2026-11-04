# Measured hydrogen 2S–6P excitation spectra

These two CSV files are unchanged copies of experimental scans from Lothar Maisenbacher's [MPQ dataset](https://doi.org/10.5281/zenodo.15874385), version v1, released on 11 February 2026 under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). They support Maisenbacher et al., [*Sub-part-per-trillion test of the Standard Model with atomic hydrogen*](https://doi.org/10.1038/s41586-026-10124-3), *Nature* **650**, 845–851 (2026). The upstream data are condensed measured fluorescence counts, binned by detection delay.

Atoms prepared in the same 2S state are excited by a scanned laser near 410 nm. The detected photons predominantly come from subsequent ultraviolet Lyman-ε emission. Thus the signal is an excitation spectrum, rather than a direct measurement of emitted Hδ intensity.

`provenance.json` identifies the original scans, dates, archive checksum and individual SHA-256 checksums. G3 probes the 6P₁/₂ branch; G8 probes 6P₃/₂. Both selected scans have nominally zero beam offset, zero applied bias fields, 10 μW spectroscopy laser power and the same polarization. The top-detector velocity-group D13 data pass the source's main-analysis selection.

Use the measured `Ch0D13` counts. Each point accumulates 160 chopper cycles, corresponding to one second of acquisition. Expected photon-counting uncertainty is the square root of the counts; this does not include technical noise.

Restore frequency by adding each scan's disclosed `unblind_offset_hz` to `Freq_Blind`, then subtract the shared `reference_hz`. These are the source's unblinding constants. Convert frequency offset to vacuum-wavenumber offset by dividing hertz by 29,979,245,800 cm/s.

Keep the two independently acquired frequency windows distinct: the intervening gap was unmeasured. Retain repeated centre points as separate observations. No fitting, smoothing, synthetic peaks, background subtraction or normalization is required. Further systematic corrections and zero-velocity extrapolation are needed for precision spectroscopy. Relative peak heights here should not be interpreted as an oscillator-strength ratio.

The [plotting script](../../analysis/plot_hydrogen_fine_structure.py) generates [Figure 1.2](../../figures/hydrogen-2s-6p-measured.svg) and [the plotted coordinates](plotted-points.csv). From the repository root, run `python3 atomic-molecular-physics/analysis/plot_hydrogen_fine_structure.py` with NumPy and Matplotlib installed.
