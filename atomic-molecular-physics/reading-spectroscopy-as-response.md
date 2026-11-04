# Optional reading for Unit 5 · What a spectrum measures: spectroscopy as linear response

**Where it fits.** This optional reading follows the provisional connected draft of [Unit 5](unit-5-light-matter-interaction.md): response functions mean more once transitions, populations and widths have been studied. It is not required for the course argument, which begins with [Unit 0](unit-0-learning-from-measurements.md). The syllabus does not list response theory as a separate topic, but it connects selection rules, spectral widths, Einstein coefficients, magnetic resonance and Raman spectroscopy.

**For readers from condensed matter.** This is the same linear-response theory used for optical conductivity or neutron scattering, applied to a single atom.

The aim here is to connect absorption, dispersion and transition strengths through one response function. Optional problems and answers follow the explanation.

---

## R.1 The data

> **How it is measured.**
> - **Absorption.** White light passes through a cell of sodium vapour into a spectrometer. The transmitted intensity is $`I = I_0\,e^{-N\sigma(\omega)L}`$, where N is the number of atoms per unit volume, L is the length of the cell and σ(ω) is the absorption cross-section (the Beer–Lambert law).
> - **Dispersion.** In Rozhdestvensky's "hook method" (1912), an interferometer has the vapour cell in one arm, and its output goes into a spectrograph. The fringes shift by the extra optical path, (n − 1)L. Near each absorption line they bend into hook shapes, and the separation of the hooks gives the product of the atom density and the strength of the line.
> - **Lifetimes.** Atoms are excited by a short pulse of light or electrons, and the emitted light is timed. Its intensity decays as $`e^{-t/\tau}`$.

**1. Absorption and dispersion go together.** Sodium vapour absorbs strongly at each D line, and near each line its refractive index changes sharply. The isolated line's contribution to n − 1 is positive below resonance and negative above it. Across the central absorption region, n decreases as frequency increases: **anomalous dispersion**.

**2. Each line has a measurable strength.** It is expressed as the oscillator strength f, defined in Section R.3:

| Transition | Wavelength (nm) | Oscillator strength f |
|---|---|---|
| Na 3s → 3p, D2 | 589.0 | 0.641 |
| Na 3s → 3p, D1 | 589.6 | 0.320 |
| H 1s → 2p, Lyman α | 121.6 | 0.416 |
| H 1s → 3p, Lyman β | 102.6 | 0.079 |

The hydrogen values are calculations in the non-relativistic Coulomb model, supported by measured lifetimes.

**3. The excited states decay.** Sodium's 3p level lives 16.2 ns; hydrogen's 2p level lives 1.6 ns.

## R.2 The puzzle

- Why are absorption and the refractive index linked, so that every line affects both?
- Why do the integrated D-line oscillator strengths have an approximately 2:1 ratio?
- Is there a connection between how strongly an atom absorbs a line and how quickly it emits it?

## R.3 Model 1: the Lorentz oscillator

Lorentz treated the electron as a particle on a spring, with natural frequency ω₀ and damping γ, driven by the light's electric field:

```math
m\left(\ddot{x} + \gamma\dot{x} + \omega_0^2 x\right) = -eE_0\,e^{-i\omega t}.
```

The induced dipole p = −ex is proportional to the field, $`p = \alpha(\omega)E`$, with the **polarizability**

```math
\alpha(\omega) = \frac{e^2}{m}\,\frac{1}{\omega_0^2 - \omega^2 - i\gamma\omega}.
```

Both measurements follow from α:

- A dilute gas with N atoms per unit volume has refractive index $`n(\omega) - 1 \approx N\,\mathrm{Re}\,\alpha(\omega)/(2\varepsilon_0)`$.
- The absorption cross-section is

```math
\sigma(\omega) = \frac{\omega}{\varepsilon_0 c}\,\mathrm{Im}\,\alpha(\omega).
```

Close to resonance,

```math
\alpha(\omega) \approx \frac{e^2}{2m\omega_0}\,\frac{1}{\omega_0 - \omega - i\gamma/2}.
```

Im α is a Lorentzian of full width γ. Re α is positive below the resonance and negative above it, which is exactly the shape of anomalous dispersion.

![Absorption and dispersion near a resonance](figures/lorentz-response.svg)

*Figure R.1. Absorption and dispersion of one damped oscillator near resonance. This is a model curve, not data.*

The area under the absorption line does not depend on γ:

```math
\int \sigma\,d\nu = \frac{e^2}{4\varepsilon_0 m c} = 2.65 \times 10^{-6}\ \text{m}^2\,\text{Hz}.
```

The model explains the **shape** of anomalous dispersion. Different lines require different strength factors f, historically called the "number of dispersion electrons". The classical model cannot calculate them; f need not be less than one for a multi-electron atom.

## R.4 Model 2: the quantum response function

For an atom with $`N_e`$ electrons, define $`Z_e=\sum_{i=1}^{N_e}z_i`$ and $`d_z=-eZ_e`$. Apply $`H'=eZ_eE(t)`$ to the ground state $`|0\rangle`$ and calculate the induced dipole to first order in E. This is **linear response**. For the chosen polarization axis, a spectral representation with phenomenological damping is

```math
\alpha(\omega) = \frac{e^2}{m}\sum_n \frac{f_{n0}}{\omega_{n0}^2 - \omega^2 - i\gamma_n\omega},
\qquad
f_{n0} = \frac{2m\,\omega_{n0}}{\hbar}\,\bigl|\langle n|Z_e|0\rangle\bigr|^2,
\qquad
\omega_{n0} = \frac{E_n - E_0}{\hbar}.
```

Here m is the electron mass, and n labels complete atomic excited states, including the continuum. For an isotropic gas, sum over degenerate final states and average over the initial magnetic-state populations and orientations. Each resonance has three distinct ingredients:

- **Position.** Each resonance sits at a transition frequency, a difference of two energy levels.
- **Weight.** Its strength is the oscillator strength $`f_{n0}`$, set by a matrix element.
- **Width.** Its angular-frequency FWHM is $`\gamma_n=2/T_{2,n}`$, determined by coherence decay. It equals the upper-state population decay rate only for a stable lower state with no additional dephasing.

**For readers from condensed matter:** this is the Kubo formula for one atom,

```math
\alpha(\omega) = \frac{i}{\hbar}\int_0^\infty dt\,e^{i\omega t}\,\bigl\langle 0\bigl|\,[d_z(t), d_z(0)]\,\bigr|0\bigr\rangle, \qquad d_z = -eZ_e,
```

evaluated by inserting a complete set of states, with the coherence widths added phenomenologically. For population decay rates $`\Gamma_n,\Gamma_0`$ and pure-dephasing rate $`\gamma_{\phi,n0}`$, $`\gamma_n=\Gamma_n+\Gamma_0+2\gamma_{\phi,n0}`$, as developed in Unit 5.

**A historical note.** Kramers' 1924 dispersion formula helped motivate Heisenberg's matrix mechanics in 1925. Transition amplitudes, represented here by matrix elements such as $`\langle n|Z_e|0\rangle`$, became central quantities.

### Three exact properties

**1. The f-sum rule (Thomas–Reiche–Kuhn).** For a non-relativistic atom with a fixed nucleus and a coordinate-dependent potential, $`[Z_e,[H,Z_e]]=N_e\hbar^2/m`$. A complete sum over bound and continuum states gives

```math
\sum_n f_{n0} = N_e,
```

the number of electrons. So far above every resonance, $`\alpha(\omega) \to -N_e e^2/(m\omega^2)`$: the electrons respond as if they were free. This is the same f-sum rule you know from condensed matter, and it is why X-rays see a refractive index slightly less than 1 (Problem R.2).

**2. The Kramers–Kronig relations.** The response is causal: the dipole cannot respond before the field arrives. This links the real and imaginary parts:

```math
\mathrm{Re}\,\alpha(\omega) = \frac{2}{\pi}\,\mathcal{P}\!\int_0^\infty \frac{\omega'\,\mathrm{Im}\,\alpha(\omega')}{\omega'^2 - \omega^2}\,d\omega'.
```

Absorption lines and anomalous dispersion are two views of the same resonances.

**3. The golden rule gives the same answer.** For a weak field $`E_0\cos\omega t`$, Fermi's golden rule gives the transition rate

```math
W = \frac{2\pi}{\hbar}\,\Bigl|\bigl\langle n\bigl|\tfrac12 eZ_eE_0\bigr|0\bigr\rangle\Bigr|^2\,\delta(E_n - E_0 - \hbar\omega).
```

Multiplied by ħω, this is exactly the power absorbed in linear response, $`P = \tfrac{\omega}{2}\,\mathrm{Im}\,\alpha(\omega)\,E_0^2`$, with each narrow Lorentzian replaced by a delta function (Problem R.4). So linear response is the framework, and the golden rule is the calculating tool. The later units, and the NET exam, mostly use the golden rule.

## R.5 Numbers from the data

- **Sodium.** The two D lines carry f = 0.641 + 0.320 = 0.961. An approximate valence-electron comparison places this on a scale of one, with about 96% in the D lines. This is not sodium's full atomic sum: neutral sodium has 11 electrons, and the complete TRK sum is 11, including core excitations. The D-line ratio is approximately 2:1, also an approximate emission ratio for an optically thin source with equally populated upper magnetic sublevels and nearly equal decay rates, under the conditions discussed in Unit 5.
- **Hydrogen.** Lyman α carries 0.416 and Lyman β 0.079. All the lines together carry 0.565, and the ionization continuum the remaining 0.435. The total is exactly 1.

![Hydrogen oscillator strengths and an approximate sodium valence-sector comparison](figures/oscillator-strengths.svg)

*Figure R.2. Reference oscillator strengths, not a measured spectrum. Hydrogen's complete sum is one. The sodium bar is an approximate valence-sector comparison; core excitations contributing to its full atomic sum of 11 are not shown.*

## R.6 Test a prediction: absorption predicts emission

Absorption and dispersion measure f. Einstein's relation between absorption and emission turns f into a rate of spontaneous emission. Unit 5 derives it from thermal equilibrium; it is a form of the fluctuation–dissipation theorem.

```math
A_{ul} = \frac{2\pi e^2\nu^2}{\varepsilon_0 m_e c^3}\,\frac{g_l}{g_u}\,f_{lu}.
```

Here l and u label the lower and upper electronic levels, g = 2J + 1 counts their magnetic states, and f is the corresponding level-averaged absorption oscillator strength. Hyperfine structure is omitted. In general $`\tau_u^{-1}=\sum_l A_{ul}`$; the table uses nearly single-branch decays.

| Line | f | Predicted lifetime τ = 1/A | Measured lifetime |
|---|---|---|---|
| Na D2 (from 3p ²P<sub>3/2</sub>) | 0.641 | 16.2 ns | 16.2 ns |
| H Lyman α (from 2p) | 0.416 | 1.60 ns | 1.6 ns |

For these nearly single-branch decays to a stable lower state, with no additional dephasing, $`\gamma\simeq A`$. The natural frequency FWHM $`A/(2\pi)`$ is therefore 9.8 MHz for the sodium D lines and 100 MHz for Lyman α. Unit 5 distinguishes these lifetime-limited widths from Doppler and collision broadening.

## R.7 The course in response language

| Response-function idea | Where it appears |
|---|---|
| Positions of the resonances, $`\omega_{n0}`$ | Every energy level: hydrogen (Unit 1), fine and hyperfine structure (Unit 2), Zeeman and Stark shifts (Unit 4), molecular levels (Unit 6) |
| Weights of the resonances, $`f_{n0}`$ | Selection rules (Units 1, 3 and 5), line intensities (Unit 5), Franck–Condon factors (Unit 7) |
| Widths of the resonances, $`\gamma_n`$ | Natural line width, then Doppler and collision broadening (Unit 5) |
| The f-sum rule | Checks on line strengths; free-electron response at high frequency |
| Kramers–Kronig relations | Anomalous dispersion near absorption lines |
| Fluctuation–dissipation theorem | Einstein A and B coefficients (Unit 5) |
| Magnetic susceptibility χ″(ω) | ESR and NMR (Unit 4); exponential coherence decay gives angular-frequency HWHM $`1/T_2`$, or frequency FWHM $`1/(\pi T_2)`$ (Unit 5) |
| Correlation function of the polarizability, like S(q, ω) | Raman spectra (Unit 7) |
| Electron energy loss | The Franck–Hertz experiment, an early form of electron energy-loss spectroscopy; electron impact also excites levels that light cannot reach from the ground state (Unit 1) |
| Im χ < 0, meaning gain | Lasers and population inversion (Unit 5) |

## R.8 What linear response does not cover

- **Stern–Gerlach** (Unit 2) measures magnetic-moment projections through deflection. It is not a spectrum.
- **Spontaneous emission** needs the quantized light field. Linear response reaches it only indirectly, through Einstein's relation or the fluctuation–dissipation theorem.
- **Lasers above threshold, saturation and two-photon spectroscopy** are nonlinear: the response depends on the strength of the field.
- **Linear response tells you how to read a spectrum,** but the positions and weights of the resonances still come from the atom's Hamiltonian. Calculating them is the job of the rest of the course.

---

## Problems

**R.1** For the Lorentz oscillator, show that the area under the absorption line, $`\int\sigma(\omega)\,d\omega = \pi e^2/(2\varepsilon_0 mc)`$, does not depend on γ. Use the near-resonance form of α.

**R.2** Use the f-sum rule to show that $`\alpha(\omega) \to -N_e e^2/(m\omega^2)`$ at high frequency. Show that the refractive index for X-rays is $`n = 1 - \omega_p^2/(2\omega^2)`$, where $`\omega_p^2 = n_e e^2/(\varepsilon_0 m)`$ and $`n_e`$ is the electron density. What happens to X-rays that strike a polished surface at a grazing angle?

**R.3** Using f = 0.416 for Lyman α, find the spontaneous emission rate and lifetime of the hydrogen 2p level.

**R.4** For a single electron, so that $`Z_e=z`$, show that the golden-rule rate multiplied by ħω equals $`\tfrac{\omega}{2}\,\mathrm{Im}\,\alpha\,E_0^2`$ when γ → 0. Use $`\lim_{\gamma\to0}\frac{\gamma/2\pi}{(\omega_0-\omega)^2 + \gamma^2/4} = \delta(\omega - \omega_0)`$.

**R.5** Find the peak absorption cross-section of the sodium D2 line for an atom at rest, using its natural width of 9.8 MHz. Compare it with the geometric size of an atom, about 10⁻²⁰ m².

**R.6** In atomic units the static polarizability is $`\alpha(0) = \sum_n f_{n0}/\omega_{n0}^2`$, with ω in hartrees. Estimate the polarizability of hydrogen from Lyman α alone. The exact value is 4.5. Where does the rest come from?

## Answers

**R.1** Near resonance, $`\mathrm{Im}\,\alpha \approx \frac{e^2}{2m\omega_0}\,\frac{\gamma/2}{(\omega_0-\omega)^2 + \gamma^2/4}`$, whose integral over ω is $`\frac{e^2}{2m\omega_0}\,\pi`$. Multiplying by $`\omega_0/(\varepsilon_0 c)`$ gives $`\pi e^2/(2\varepsilon_0 mc)`$. In frequency units, $`\int\sigma\,d\nu = e^2/(4\varepsilon_0 mc) = 2.65 \times 10^{-6}`$ m² Hz.

**R.2** For ω much larger than every $`\omega_{n0}`$, $`\alpha \approx -\frac{e^2}{m\omega^2}\sum_n f_{n0} = -\frac{N_e e^2}{m\omega^2}`$. Then $`n - 1 = N\,\mathrm{Re}\,\alpha/(2\varepsilon_0) = -\omega_p^2/(2\omega^2)`$. Since n < 1, X-rays at a grazing angle are totally reflected from the outside. This is how X-ray mirrors and telescopes work.

**R.3** $`A = \frac{2\pi e^2\nu^2}{\varepsilon_0 m_e c^3}\cdot\frac{2}{6}\cdot 0.416 = 6.26 \times 10^8\ \text{s}^{-1}`$, so τ = 1.60 ns.

**R.4** As γ → 0, $`\mathrm{Im}\,\alpha \to \frac{\pi e^2 f}{2m\omega_0}\,\delta(\omega - \omega_0) = \frac{\pi e^2|z_{n0}|^2}{\hbar}\,\delta(\omega - \omega_0)`$, so $`P = \frac{\pi e^2|z_{n0}|^2E_0^2\,\omega}{2\hbar}\,\delta(\omega - \omega_0)`$. The golden rule gives $`W = \frac{2\pi}{\hbar}\cdot\frac{e^2|z_{n0}|^2E_0^2}{4}\cdot\frac{1}{\hbar}\,\delta(\omega - \omega_0)`$, and $`\hbar\omega W`$ is the same expression.

**R.5** $`\sigma_0 = \frac{g_u}{g_l}\,\frac{\lambda^2}{2\pi} = 2 \times \frac{(589\ \text{nm})^2}{2\pi} = 1.1 \times 10^{-13}\ \text{m}^2`$. To resonant light, the atom looks about ten million times larger than it is.

**R.6** Lyman α alone gives $`0.416/(3/8)^2 = 2.96`$. All the Lyman lines together give 3.66, and the ionization continuum supplies the remaining 0.84.

---

## Sources of the data

- Oscillator strengths and lifetimes: NIST Atomic Spectra Database; hydrogen values from the exact formula in Bethe & Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms*.
- Anomalous dispersion and the hook method: Thorne, Litzén and Johansson, *Spectrophysics*.
- Linear response and the Kramers–Heisenberg formula: Bransden & Joachain, *Physics of Atoms and Molecules*.
- Constants: CODATA 2018. Every derived number in these notes was checked with a short calculation.
