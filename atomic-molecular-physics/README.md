# Atomic and Molecular Physics

A connected, observation-driven course in atomic and molecular physics at MSc level, in development. Its planned scope follows Section VII (Atomic & Molecular Physics) of the CSIR-UGC NET Physical Sciences syllabus.

We cannot directly see the internal quantum states of an atom or molecule. How do we learn about them through measurements? The course follows this question through a recurring cycle: **observation → provisional model → prediction → proposed experiment → measured result → assessment and next question**. Each experiment enters because we can explain what it would test. Agreement establishes the model's useful range; a discrepancy, a changed system or a different probe can motivate the next investigation. This is a reconstruction of scientific reasoning; historical context is distinguished from the teaching sequence.

**Start with [Unit 0](unit-0-learning-from-measurements.md).** The [course map](course-map.md) gives each unit's central question, motivating observation, essential equations and connection to the next.

The first connected writing pass now spans Units 0–8. Unit 0 is accepted as a first draft and Unit 1 as a provisional draft, with writing to revisit; Units 2–8 remain provisional. Missing measurements and independent tests are visible TODOs. This establishes the course's conceptual progression while leaving reader review, experimental enrichment and further validation to continue. The [progress audit](day-1-audit.md) records the work and remaining gaps.

## Units

| Unit | Central question | Syllabus topics | Notes |
|---|---|---|---|
| 0. How do we learn about the microscopic world? | How do measurements reveal microscopic properties? | Preparation for the whole section | [Unit 0](unit-0-learning-from-measurements.md) |
| 1. The hydrogen atom | What explains discrete levels and spectral series? | Quantum states of an electron in an atom | [Unit 1](unit-1-hydrogen.md), accepted provisional first draft |
| 2. Spin and atomic fine structure | Why do levels and lines split? | Electron spin; relativistic corrections for the energy levels of hydrogen; hyperfine structure and isotope shift | [Unit 2](unit-2-spin-fine-hyperfine.md), provisional first connected draft |
| 3. Many-electron atoms | How do interacting electrons change atomic spectra? | Spectra of helium and alkali atoms; LS and jj coupling | [Unit 3](unit-3-many-electron-atoms.md), provisional first connected draft |
| 4. Atoms in external fields | How do fields shift, split and connect states? | Zeeman, Paschen–Back and Stark effects; electron spin resonance; nuclear magnetic resonance and chemical shift | [Unit 4](unit-4-atoms-in-external-fields.md), provisional first connected draft |
| 5. Light–matter interaction | What determines strengths, widths and laser oscillation? | Width of spectral lines; spontaneous and stimulated emission; Einstein A and B coefficients; optical pumping, population inversion, rate equations; modes of resonators and coherence length | [Unit 5](unit-5-light-matter-interaction.md), provisional first connected draft. Optional reading: [spectroscopy as linear response](reading-spectroscopy-as-response.md) |
| 6. Molecules and nuclear motion | How do molecules bind, rotate and vibrate? | Born–Oppenheimer approximation; the levels behind the electronic, rotational and vibrational spectra of diatomic molecules | [Unit 6](unit-6-molecules-and-nuclear-motion.md), provisional first connected draft |
| 7. Molecular spectroscopy | How do probes reveal molecular motion and electronic structure? | Electronic, rotational, vibrational and Raman spectra of diatomic molecules; selection rules; Franck–Condon principle | [Unit 7](unit-7-molecular-spectroscopy.md), provisional first connected draft |
| 8. Putting the ideas together | What can a complex spectrum establish? | Synthesis of state assignments, coupling, intensities, widths and measurement inference | [Unit 8](unit-8-putting-the-ideas-together.md), provisional first connected draft |

## How the units are written

Version 1 aims to make the physics and its connections complete before the details are polished. A unit is complete for Version 1 when a reader can answer:

1. What physical phenomenon motivated this topic?
2. What new theoretical idea was necessary?
3. What can we calculate or predict with it?
4. What does it fail to explain, and what comes next?

Real measurements are used wherever good data exist, but a missing dataset does not hold up the physical argument.

New experiments should enter because an earlier observation leaves a specific question unresolved. Explain what to vary, what to record and what outcomes would test the proposed explanation before interpreting the result. Where a first-pass measurement or comparison is missing, place a visible **TODO** box at that point, specifying what is needed. Original research papers can be linked where they clarify motivation, experimental difficulties or historical development. They supplement the self-contained physics; an external manual or slide set does not supply a missing argument or detector record. Keep source attribution in the bibliography and data provenance.

Units 1–8 develop connected physical arguments rather than a compulsory lecture template. Measured hydrogen excitation, published CO line centres, a processed CO infrared record and an empirical calibration template supply examples. Their provenance distinguishes recorded signals, tabulated results, processing and model figures. The [optional response reading](reading-spectroscopy-as-response.md) belongs after Unit 5 and is not required to begin the course.

## Numerical companion to Unit 8

[Unit 8](unit-8-putting-the-ideas-together.md) proposes single-element controls before interpreting a mixed Hg–Cd–Ar record. Those controls remain TODOs. The available archive is a continuum-subtracted, separately normalized and stitched wavelength-calibration template, with its [source audit](data/lamp-archive/README.md) preserved. Its four maxima at 10000 are normalization maxima, not demonstrated detector saturation.

The [numerical companion](worked-example-raw-spectrum.md) and [analysis](analysis/raw_spectrum_to_levels.py) reproduce guarded candidate measurements and a conditional Ritz reconstruction. The [current diagnostics](data/lamp-analysis/README.md) do not claim formal centroid errors or independent validation against the same references used for calibration. The older full-list line table is retained as a legacy record rather than treated as a reproduced identification result.

## Experiments for each syllabus topic

| Syllabus topic | Textbook experiment and data | Theory it leads to |
|---|---|---|
| Quantum states of an electron in an atom | Hydrogen Balmer lines at 656.3, 486.1, 434.0 and 410.2 nm. Franck–Hertz: in mercury vapour the current drops every 4.9 V | Rydberg formula, Bohr model, Schrödinger hydrogen atom: $`E_n = -13.6\ \text{eV}/n^2`$; quantum numbers n, l, m |
| Electron spin | Stern–Gerlach: a silver beam splits in two. The sodium D line is a doublet at 589.0 and 589.6 nm | Spin ½, spin magnetic moment, spin–orbit coupling |
| Alkali spectra | Sodium's sharp, principal and diffuse series, converging to the ionization energy of 5.14 eV | Quantum defect, $`E = -13.6\ \text{eV}/(n - \delta_l)^2`$, with $`\delta_s = 1.35`$, $`\delta_p = 0.86`$, $`\delta_d \approx 0`$; core penetration |
| Helium spectrum | Two separate line systems (singlet and triplet). The 1s2s levels at 19.82 eV (triplet) and 20.62 eV (singlet). Ground state at −79.0 eV | Pauli principle and exchange energy. Perturbation theory gives −74.8 eV; the variational method gives −77.5 eV |
| Relativistic corrections for hydrogen | Resolved 2s → 6p excitation resonances about 405 MHz apart | Relativistic kinetic energy, spin–orbit and Darwin terms; leading fine-structure prediction about 406 MHz |
| Hyperfine structure and isotope shift | Hydrogen's 21 cm line at 1420.4 MHz. Deuterium Hα at 656.10 nm against 656.28 nm for hydrogen | Coupling to the nuclear magnetic moment ($`F = I + J`$); reduced-mass correction |
| Width of spectral lines | Sodium D line: natural width about 10 MHz (lifetime 16 ns); Doppler width about 1.3 GHz at room temperature | Lifetime (Lorentzian), Doppler (Gaussian) and pressure broadening |
| LS and jj coupling | Calcium 4s4p ³P levels 52 and 106 cm⁻¹ apart (ratio 2). The np² level pattern changes from LS in carbon to jj in lead | Term symbols, Hund's rules, Landé interval rule, the jj limit |
| Zeeman and Paschen–Back effects | Cadmium 643.8 nm splits into three lines, 0.019 nm apart at 1 T. Sodium D1 splits into 4 lines and D2 into 6. Lithium's 2p doublet (0.34 cm⁻¹) reaches the strong-field regime at a few tesla | Normal Zeeman effect and e/m, Landé g-factor, anomalous Zeeman effect, decoupling of L and S |
| Stark effect | Hydrogen Balmer lines split in proportion to the electric field; alkali lines shift as its square | Degenerate perturbation theory ($`\pm 3ea_0F`$ for n = 2); polarizability |
| Electron spin resonance | DPPH absorbs at g = 2.0036 (9.5 GHz at 0.34 T). Mn²⁺ gives six lines | $`h\nu = g\mu_B B`$; hyperfine splitting into 2I + 1 lines |
| NMR and chemical shift | The 1951 proton spectrum of ethanol: three peaks with areas 3 : 2 : 1 | Larmor precession (42.58 MHz/T), shielding, chemical shift in ppm |
| Born–Oppenheimer approximation | CO isotope comparisons; harmonic constants distinguished from fundamental intervals | Approximately shared electronic potential; rotational and harmonic vibrational scales vary as $`\mu_{\mathrm{red}}^{-1}`$ and $`\mu_{\mathrm{red}}^{-1/2}`$ |
| Rotational spectra | Published CO line centres near 115.271, 230.538 and 345.796 GHz | Rigid-rotor prediction and its residuals; effective bond length near 1.13 Å; centrifugal distortion |
| Vibrational spectra | HCl infrared band at 2886 cm⁻¹: P and R branches, no Q branch, doublets from ³⁵Cl and ³⁷Cl, overtone at 5668 cm⁻¹ | Harmonic oscillator, then the Morse potential; anharmonicity; vibration–rotation coupling |
| Raman spectra | Nonpolar molecules can show shifted scattering despite absent ordinary dipole absorption; Stokes/anti-Stokes and polarization comparisons | Polarizability; rotational ΔJ = ±2; rovibrational ΔJ = 0, ±2. Measured strengths also depend on populations, spin statistics and detection |
| Electronic spectra and Franck–Condon principle | Electronic bands contain vibrational progressions; calibrated band records remain a TODO | Electronic transition moments and Franck–Condon overlaps; corrected band strengths test nuclear-state assignments and potential displacement |
| Einstein A and B coefficients | Sodium 3p lifetime of 16 ns, so A = 6.2 × 10⁷ s⁻¹ | Spontaneous and stimulated emission; $`A/B \propto \nu^3`$ |
| Optical pumping, population inversion, rate equations | He–Ne laser: helium's 2¹S level (20.62 eV) matches a neon level (20.66 eV). A laser diode's light output jumps at a threshold current. Rubidium optical pumping | Three- and four-level systems, rate equations and threshold, optical pumping |
| Resonator modes and coherence length | A 30 cm He–Ne cavity has modes 500 MHz apart. Michelson interferometer with a sodium lamp: successive visibility minima are 0.29 mm apart in mirror travel, from beating between D1 and D2 | Longitudinal and transverse modes; doublet beat spacing λ²/(2Δλ) in mirror travel; coherence length ≈ λ²/δλ, set by each line's own width δλ |

## Where the data comes from

- **Atoms:** Haken & Wolf, *The Physics of Atoms and Quanta*; White, *Introduction to Atomic Spectra*; Foot, *Atomic Physics*; Eisberg & Resnick, *Quantum Physics of Atoms, Molecules, Solids, Nuclei, and Particles*.
- **Molecules:** Banwell & McCash, *Fundamentals of Molecular Spectroscopy*; Herzberg, *Spectra of Diatomic Molecules*.
- **Lasers:** Svelto, *Principles of Lasers*; Thyagarajan & Ghatak, *Lasers: Fundamentals and Applications*.
- **Checking numbers:** the NIST Atomic Spectra Database and the NIST Chemistry WebBook.

## Conventions

- Visible wavelengths are given in air, as in most textbooks, unless marked "vacuum". To convert, multiply the air wavelength by $`n_\text{air} \approx 1.00028`$.
- Constants are CODATA 2018 values.
- Every derived number in the notes was checked with a short calculation.
