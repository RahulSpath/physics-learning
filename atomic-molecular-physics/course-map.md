# Atomic and Molecular Physics · Course map

**Version 1: a connected MSc-level course covering CSIR–UGC NET Physical Sciences, Part B, Section VII.** This map follows the unit sequence in the course plan of 3 November 2026.

| Unit | Central question and essential content | Connection to the next unit |
|---|---|---|
| **0. How do we learn about the microscopic world?** | How do measurements reveal microscopic properties? Instrument signals, spectra, energy differences and probe-dependent inference. | We observe discrete lines. Why do discrete bound-state energies exist? |
| **1. The hydrogen atom** | What explains discrete levels and spectral series? Balmer/Rydberg patterns, Franck–Hertz electron-impact evidence, the Coulomb Hamiltonian, quantum numbers and reduced mass. | Hydrogenic levels explain the gross spectrum. What produces additional splittings? |
| **2. Spin and atomic fine structure** | Why do levels and lines split? Stern–Gerlach, spin, spin–orbit coupling, relativistic corrections, hyperfine structure and isotope shifts. | A single electron is understood approximately. What changes when several electrons interact? |
| **3. Many-electron atoms** | How do interacting electrons change atomic spectra? Helium, exchange, Pauli principle, singlets/triplets, alkalis, quantum defects and LS/jj coupling. | How can external fields test state assignments and manipulate the states? |
| **4. Atoms in external fields** | How do fields shift, split and connect states? Zeeman, Paschen–Back and Stark effects; ESR, NMR and chemical shifts. | Transition frequencies alone do not explain spectral intensities and widths. |
| **5. Light–matter interaction** | What determines strengths, widths and laser oscillation? Matrix elements, selection rules, Einstein coefficients, lifetimes, broadening, pumping, inversion, rate equations, resonator modes and coherence. | What new structure appears when nuclei move relative to one another? |
| **6. Molecules and nuclear motion** | How do molecules bind, rotate and vibrate? Potential-energy curves, Born–Oppenheimer approximation, rotational/vibrational levels and rovibrational structure. | Which molecular levels can different probes reveal? |
| **7. Molecular spectroscopy** | How do probes reveal molecular motion and electronic structure? Infrared, Raman and electronic spectra, selection rules, Franck–Condon factors and vibrational progressions. | Can we disentangle a complicated experimental spectrum? |
| **8. Putting the ideas together** | What can a complex spectrum establish? Individual Hg, Cd and Ar spectra, mixtures, line identification, resolution, calibration and limits of inference. | Concluding synthesis: return to measurement, models and microscopic inference. |

The course develops one investigation: measurements reveal discrete transitions; hydrogen explains their first pattern; additional interactions explain splittings; external fields probe the states; transition theory explains strengths, widths and gain; nuclear motion introduces molecular spectra; and the final unit brings these ideas back to experimental inference.

A recurring distinction is that **what we measure is not everything that exists in the system**. An absent peak may reflect a selection rule, an unpopulated state, broadening or limited sensitivity.

**Conventions.** Quoted visible wavelengths are in air unless explicitly marked vacuum. Energy and spectroscopic wavenumber conversions use $`\lambda_{\mathrm{vac}}=n_{\mathrm{air}}\lambda_{\mathrm{air}}`$; use wavelength-dependent refractive indices when precision requires them. Constants are CODATA 2018 values. Distinguish measured records, tabulated measurements and model illustrations.

The first two days establish this map and Unit 0. Then develop each unit in sequence: Day 1 builds its physical argument; Day 2 tests the explanation with a useful example, questions and references. Version 1 needs essential reasoning and equations throughout the syllabus. Available data should strengthen that argument; missing datasets must not prevent its completion.

## Unit 0 · How do we learn about the microscopic world?

**Central question.** We cannot directly see the internal quantum states of an atom or molecule. How do we learn about them through measurements?

**Motivating observation.** A hydrogen discharge produces discrete optical lines, while a magnetic-resonance experiment produces a signal as frequency or field is scanned. What does each instrument record, and what microscopic interpretation requires a model?

**Essential concepts.** Follow the plan’s six short sections:

1. **What does an experiment actually give us?** Compare an emission spectrum, a resonance signal and, optionally, an inelastic-scattering spectrum.
2. **An atomic emission spectrum.** Begin with a real single-element spectrum, preferably hydrogen; explain its axes before interpreting its peaks.
3. **What information does a spectral line contain?** Ask about position, strength, width and response to external conditions.
4. **From observations to a mathematical model.** Introduce states, energies and probe-dependent access to transitions.
5. **The same reasoning across physics.** Preview molecular spectroscopy, magnetic resonance, photoemission and inelastic scattering. Diffraction primarily reveals spatial structure and correlations; these experiments need not measure the same quantity.
6. **Questions that will guide the course.** Discreteness, splittings, missing transitions, molecular structure, intensities and widths.

**Indispensable equations.**

```math
H|n\rangle=E_n|n\rangle,\qquad
E_u-E_l=h\nu=\frac{hc}{\lambda_{\mathrm{vac}}}
=hc\tilde{\nu},\qquad
\tilde{\nu}=\frac{1}{\lambda_{\mathrm{vac}}}.
```

A transition’s visibility also depends on the probe’s coupling to the system; no perturbation-theory or susceptibility derivation is needed here.

**Syllabus coverage.** Conceptual preparation for all units. Energy differences, transition strengths, widths and magnetic resonance appear here as previews; their explanations follow below.

**Connection to Unit 1.** Discrete lines suggest discrete energy differences. Why does an atom possess discrete bound states?

## Unit 1 · The hydrogen atom

**Central question.** What physical model explains hydrogen’s spectral series and their convergence towards ionization?

**Motivating observation.** The Balmer lines crowd towards a series limit. Other series and the nearby lines of ionized helium test whether the pattern extends beyond the original observations. Franck–Hertz current minima in mercury provide independent evidence of discrete levels through electron-impact excitation.

**Essential concepts.** Balmer and Rydberg patterns; the Ritz combination principle; Franck–Hertz and electron-impact excitation; the Coulomb Hamiltonian; normalizable bound states; quantum numbers $`n,l,m`$; wavefunctions and degeneracy; reduced mass. Use Bohr’s model briefly to connect the observed pattern to energy scales, then explain quantization through the Schrödinger problem.

**Indispensable equations.**

```math
H_C=\frac{p^2}{2\mu}-\frac{Ze^2}{4\pi\varepsilon_0r},
\qquad
\mu=\frac{m_eM}{m_e+M},
\qquad
\psi_{nlm}=R_{nl}(r)Y_{lm}(\theta,\phi).
```

```math
E_n=-hcR_M\frac{Z^2}{n^2},
\qquad
R_M=R_\infty\frac{\mu}{m_e},
\qquad
\tilde{\nu}=Z^2R_M
\left(\frac{1}{n_l^2}-\frac{1}{n_u^2}\right).
```

Here $`n=1,2,\ldots`$, $`l=0,\ldots,n-1`$ and $`m=-l,\ldots,l`$.

**Syllabus coverage.** Quantum states of an electron in an atom. Introduce isotope shifts through reduced mass before Unit 2. Introduce electric-dipole matrix elements and the basic rules $`\Delta l=\pm1`$, $`\Delta m=0,\pm1`$ to explain why 2p and 2s decay differently; rates and the general framework belong to Unit 5.

**Connection to Unit 2.** The Coulomb model predicts the gross spectrum, but precise measurements resolve additional structure. Which degrees of freedom and interactions have been omitted?

## Unit 2 · Spin and atomic fine structure

**Central question.** Why do apparently single atomic levels and spectral lines split?

**Motivating observation.** A silver beam splits into two in a Stern–Gerlach magnet; sodium has a D doublet; hydrogen shows fine and hyperfine intervals and isotope-dependent line positions.

**Essential concepts.** Electron spin and magnetic moment; addition of orbital and spin angular momenta; spin–orbit coupling; relativistic kinetic-energy and Darwin corrections; nuclear spin and hyperfine coupling; mass and nuclear-volume isotope shifts. Distinguish these mechanisms by their energy scales. The Lamb shift marks a limitation of the theory, without requiring a QED derivation.

**Indispensable equations.**

```math
\boldsymbol{\mu}_s=-g_s\mu_B\frac{\mathbf S}{\hbar},
\qquad s=\frac12,
\qquad \mathbf J=\mathbf L+\mathbf S.
```

```math
H_{\mathrm{fs}}=
-\frac{p^4}{8m_e^3c^2}
+\frac{1}{2m_e^2c^2r}\frac{dV}{dr}\,\mathbf L\cdot\mathbf S
+\frac{\hbar^2}{8m_e^2c^2}\nabla^2V.
```

For a point nucleus of infinite mass, through the leading fine-structure correction,

```math
E_{nj}\simeq E_n^{(0)}
\left[1+\frac{(Z\alpha)^2}{n^2}
\left(\frac{n}{j+\tfrac12}-\frac34\right)\right].
```

For magnetic-dipole hyperfine structure,

```math
H_{\mathrm{hf}}=A_{\mathrm{hf}}\frac{\mathbf I\cdot\mathbf J}{\hbar^2},
\qquad
E_F=\frac{A_{\mathrm{hf}}}{2}
\left[F(F+1)-I(I+1)-J(J+1)\right].
```

Here $`\mathbf F=\mathbf I+\mathbf J`$ and $`A_{\mathrm{hf}}`$ has energy units. Additional hyperfine interactions are needed where nuclear quadrupole moments contribute.

**Syllabus coverage.** Electron spin; relativistic corrections to hydrogen energy levels; hyperfine structure and isotopic shift. Alkali doublets are a basic application here; their electronic structure follows in Unit 3. Intensity ratios remain conditional previews of Unit 5.

**Connection to Unit 3.** A single electron is now understood approximately. What changes when electrons repel one another and must obey the Pauli principle?

## Unit 3 · Many-electron atoms

**Central question.** How do electron interactions produce helium’s two spectral systems, alkali series and different angular-momentum coupling schemes?

**Motivating observation.** Helium has singlet and triplet families; alkali levels depend strongly on orbital angular momentum; multiplet patterns change between light and heavy atoms.

**Essential concepts.** Antisymmetry and the Pauli principle; direct and exchange energies; screening and electron correlation; helium singlets, triplets and metastability; central-field approximations; alkali core penetration and quantum defects; term symbols, Hund’s rules and the Landé interval rule. Compare residual electrostatic interactions with spin–orbit coupling to distinguish LS, jj and intermediate coupling.

**Indispensable equations.**

```math
H=\sum_i\left(\frac{p_i^2}{2m_e}
-\frac{Ze^2}{4\pi\varepsilon_0r_i}\right)
+\sum_{i<j}\frac{e^2}{4\pi\varepsilon_0r_{ij}}.
```

For distinct orthogonal orbitals in a first-order helium model, and for alkali binding energies measured from ionization,

```math
E_{\mathrm{singlet/triplet}}=E^{(0)}+J_C\pm K,
\qquad
E_{nl}\simeq-\frac{hcR_M}{(n-\delta_l)^2}.
```

```math
\begin{aligned}
\text{LS:}\quad&
\mathbf L=\sum_i\mathbf l_i,\quad
\mathbf S=\sum_i\mathbf s_i,\quad
\mathbf J=\mathbf L+\mathbf S,\\
\text{jj:}\quad&
\mathbf j_i=\mathbf l_i+\mathbf s_i,\quad
\mathbf J=\sum_i\mathbf j_i,\\
&E_J-E_{J-1}=A_{\mathrm{LS}}J
\quad\text{within an isolated LS term.}
\end{aligned}
```

**Syllabus coverage.** Spectra of helium and alkali atoms; LS and JJ coupling. Explain the approximate LS rule $`\Delta S=0`$ through helium, and how state mixing weakens it. Unit 5 supplies the fuller transition framework. Revisit the additional, correlated mass shift in many-electron atoms.

**Connection to Unit 4.** Level patterns suggest angular-momentum assignments. How can applied fields test those assignments and manipulate the states?

## Unit 4 · Atoms in external fields

**Central question.** How do electric and magnetic fields shift, split and connect atomic states?

**Motivating observation.** Atomic lines split in a magnetic field, hydrogen exhibits a linear Stark effect in its degenerate Coulomb manifolds, and radio-frequency or microwave absorption occurs at field-dependent resonances.

**Essential concepts.** Normal and anomalous Zeeman effects; Landé factors and polarized components; Paschen–Back decoupling when magnetic energies exceed spin–orbit intervals; degenerate and non-degenerate Stark perturbations; magnetic-dipole transitions; ESR and NMR; nuclear shielding and chemical shift. Use $`F`$ rather than $`J`$ where resolved hyperfine coupling controls the weak-field states.

**Indispensable equations.**

```math
H_Z=\frac{\mu_BB}{\hbar}(L_z+g_sS_z),
\qquad
\Delta E_Z=g_J\mu_BBm_J
\quad\text{in the electronic weak-field limit}.
```

For LS coupling, with $`g_s\simeq2`$ and $`J>0`$,

```math
g_J=1+\frac{J(J+1)+S(S+1)-L(L+1)}{2J(J+1)}.
```

In the Paschen–Back limit, use $`m_L,m_S`$ and $`\Delta E_Z\simeq\mu_BB(m_L+g_sm_S)`$.

```math
H_E=-\mathbf d\cdot\boldsymbol{\mathcal E},
\qquad
\Delta E_{\mathrm{quadratic}}=-\frac12\alpha_{\mathrm{stat}}\mathcal E^2.
```

```math
h\nu_{\mathrm{ESR}}=g\mu_BB,
\qquad
\nu_{\mathrm{NMR}}=\frac{|\gamma_N|}{2\pi}B_0(1-\sigma),
\qquad
\delta_{\mathrm{ppm}}=10^6
\frac{\nu_{\mathrm{sample}}-\nu_{\mathrm{reference}}}
{\nu_{\mathrm{reference}}}.
```

**Syllabus coverage.** Zeeman, Paschen–Back and Stark effects; electron spin resonance; nuclear magnetic resonance and chemical shift. Magnetic-resonance line widths introduce coherence decay; Unit 5 develops its relation to line shape.

**Connection to Unit 5.** Predicting transition frequencies does not predict a complete spectrum. What determines whether a transition is visible, how intense it is and how broad it becomes?

## Unit 5 · Light–matter interaction

**Central question.** What determines spectral strengths and widths, and how can emission become sustained laser oscillation?

**Motivating observation.** States with comparable excitation energies can have vastly different lifetimes. Sodium lines broaden between an atomic beam and a vapour cell. A pumped optical medium begins lasing only above threshold.

**Essential concepts.** Dipole coupling and transition matrix elements; the golden rule; polarization, parity and angular-momentum selection rules; spontaneous and stimulated emission; Einstein coefficients; populations and branching ratios. Develop natural, Doppler and collision broadening, homogeneous and inhomogeneous widths, and Voigt profiles.

Then follow absorption into optical pumping, population inversion and elementary three- and four-level laser cycles. Explain gain, loss and threshold with rate equations, followed by longitudinal and transverse resonator modes and temporal coherence. Detailed laser dynamics can be refined later.

**Indispensable equations.**

```math
H'(t)=-\mathbf d\cdot\mathbf E(t),
\qquad
A_{ul}=\frac{\omega_{ul}^3}{3\pi\varepsilon_0\hbar c^3}
|\langle l|\mathbf d|u\rangle|^2,
\qquad
\tau_{\mathrm{rad},u}^{-1}=\sum_l A_{ul}.
```

The electric-dipole operator requires a parity change and $`\Delta J=0,\pm1`$, excluding $`J=0\leftrightarrow0`$; LS coupling adds approximate $`\Delta S=0`$. Optically thin emitted power also depends on population: $`P_{ul}\propto N_uA_{ul}h\nu`$.

With Einstein B coefficients defined using spectral energy density per unit frequency,

```math
g_lB_{lu}=g_uB_{ul},
\qquad
\frac{A_{ul}}{B_{ul}}=\frac{8\pi h\nu^3}{c^3}.
```

For Lorentzian homogeneous and Gaussian Doppler profiles, the frequency FWHM values are

```math
\Delta\nu_{\mathrm{hom}}=\frac{1}{\pi T_2},
\qquad
\frac{1}{T_2}=\frac{\Gamma_u+\Gamma_l}{2}+\gamma_{\mathrm{deph}},
\qquad
\Delta\nu_D=\frac{\nu_0}{c}
\sqrt{\frac{8k_BT\ln2}{M}}.
```

Thus a radiative upper state above a stable lower state has natural width $`1/(2\pi\tau_u)`$. Population decay and pure dephasing are different processes.

For an ideal four-level laser with a rapidly emptied lower laser level,

```math
\dot N=R_p-\frac{N}{\tau}-v_g\sigma_eNn_\gamma,
\qquad
\dot n_\gamma=(v_g\sigma_eN-\kappa)n_\gamma+\beta\frac{N}{\tau}.
```

Here $`N`$ and $`n_\gamma`$ are upper-state and photon densities, $`R_p`$ is the pump rate density, $`\kappa`$ is the photon loss rate and $`\beta`$ is the spontaneous-emission fraction entering the mode. Threshold occurs at $`v_g\sigma_eN=\kappa`$. More generally, inversion requires $`N_u/g_u>N_l/g_l`$.

For an empty cavity of length $`L`$,

```math
\nu_q=\frac{qc}{2L},
\qquad
\Delta\nu_{\mathrm{FSR}}=\frac{c}{2L},
\qquad
L_c=c\tau_c.
```

For a single Lorentzian spectral line, defining $`\tau_c`$ by the field correlation’s $`1/e`$ decay gives $`\tau_c=1/(\pi\Delta\nu)`$. Coherence length therefore requires a stated spectral shape and convention.

**Syllabus coverage.** Width of spectral lines; selection rules; lasers; spontaneous and stimulated emission; Einstein A and B coefficients; optical pumping; population inversion; rate equations; resonator modes and coherence length. This is the fuller treatment of transition ideas introduced in Units 0–4.

**Connection to Unit 6.** Atomic electronic transitions now have positions, strengths and widths. What new structure appears when nuclei move relative to one another?

## Unit 6 · Molecules and nuclear motion

**Central question.** How can electronic binding and nuclear motion be separated sufficiently to calculate molecular levels?

**Motivating observation.** Diatomic molecules show closely spaced rotational levels, larger vibrational intervals and isotope-dependent frequencies, rather than only atomic-like electronic lines.

**Essential concepts.** Molecular bonding and potential-energy curves; the Born–Oppenheimer approximation; nuclear reduced mass; equilibrium separation and dissociation; rigid rotation and harmonic vibration; anharmonicity, centrifugal distortion and vibration–rotation coupling. Explain the hierarchy of electronic, vibrational and rotational scales and where separation can fail.

**Indispensable equations.**

```math
\Psi(\mathbf r,R)\simeq\phi_a(\mathbf r;R)\chi_{avJ}(R),
\qquad
[T_N+U_a(R)]\chi_{avJ}=E\chi_{avJ},
\qquad
\mu_N=\frac{M_1M_2}{M_1+M_2}.
```

The potential $`U_a(R)`$ includes electronic energy and nuclear repulsion; neglecting couplings generated by nuclear derivatives is the central approximation.

```math
E_{\mathrm{rot}}=\frac{\hbar^2J(J+1)}{2\mu_NR_e^2}
=hcB_eJ(J+1),
\qquad
\omega_v=\sqrt{\frac{k}{\mu_N}},
```

```math
E_v\simeq\hbar\omega_v\left(v+\frac12\right)
-\hbar\omega_vx_e\left(v+\frac12\right)^2.
```

Here $`B_e`$ is in wavenumber units and $`k`$ is the potential curvature at equilibrium.

**Syllabus coverage.** Born–Oppenheimer approximation; the level structure underlying electronic, rotational and vibrational spectra of diatomic molecules. Spectral spacings appear at a basic level here; probe-dependent selection rules and observed bands belong to Unit 7.

**Connection to Unit 7.** A molecule possesses these levels, but which ones can infrared light, Raman scattering or electronic absorption reveal?

## Unit 7 · Molecular spectroscopy

**Central question.** How do different probes reveal molecular rotation, vibration and electronic structure?

**Motivating observation.** CO has a microwave rotational spectrum; HCl infrared absorption has rotational branches; homonuclear molecules can show Raman spectra despite lacking ordinary electric-dipole rotational and vibrational absorption. Electronic bands contain vibrational progressions.

**Essential concepts.** Pure rotational and rovibrational spectra; infrared activity; Raman scattering through polarizability; Stokes and anti-Stokes shifts; electronic transitions and molecular symmetry; Franck–Condon factors and vibrational progressions.

Pure rotational electric-dipole transitions require a permanent molecular dipole and have $`\Delta J=\pm1`$. Harmonic vibrational absorption requires $`(d\mu/dR)_e\ne0`$ and has $`\Delta v=\pm1`$; anharmonicity permits weak overtones. For simple $`\Sigma\leftrightarrow\Sigma`$ rovibrational bands, $`\Delta J=\pm1`$ gives P and R branches without a Q branch.

Raman activity depends on polarizability: rotational Raman shifts have $`\Delta J=\pm2`$, while vibrational Raman bands may include $`\Delta J=0,\pm2`$. A purely rotational $`\Delta J=0`$ contribution is unshifted Rayleigh scattering.

**Indispensable equations.**

```math
\tilde{\nu}_{J\to J+1}\simeq2B_e(J+1),
\qquad
\nu_{\mathrm{Stokes/anti\text{-}Stokes}}
=\nu_L\mp\frac{\Delta E}{h}.
```

```math
\boldsymbol{\mu}_{\mathrm{ind}}
=\boldsymbol{\alpha}(R)\mathbf E,
\qquad
\boldsymbol{\alpha}(R)\simeq
\boldsymbol{\alpha}_e+
\left(\frac{\partial\boldsymbol{\alpha}}{\partial R}\right)_e(R-R_e).
```

In the Condon approximation, the electronic transition dipole varies slowly over the nuclear wavefunctions, giving the Franck–Condon factor

```math
q_{v'v}=
\left|\int\chi_{a'v'}^*(R)\chi_{av}(R)\,dR\right|^2.
```

**Syllabus coverage.** Electronic, rotational, vibrational and Raman spectra of diatomic molecules; molecular selection rules; Franck–Condon principle. Apply Unit 5’s transition framework to the levels established in Unit 6.

**Connection to Unit 8.** We can interpret individual transition mechanisms. Can we combine that knowledge to disentangle an experimental spectrum with several species, blends and instrumental limitations?

## Unit 8 · Putting the ideas together

**Central question.** What microscopic conclusions can a complicated spectrum support, and what remains ambiguous?

**Motivating observation.** Individual Hg, Cd and Ar spectra have recognizable patterns; their mixed lamp spectrum combines lines with different strengths, unresolved blends and clipped peaks.

**Essential concepts.** Study the single-element spectra first, then the mixture. Distinguish detector counts, wavelength calibration and intensity response; identify candidate lines; test shared-level assignments with Ritz combinations; compare coupling predictions; account for resolution, line blending, uncertainty and missing transitions. Preserve unresolved identifications where the evidence is insufficient.

**Indispensable equations.**

```math
\mathcal R=\frac{\lambda}{\delta\lambda},
\qquad
\tilde{\nu}_{ul}=\frac{E_u-E_l}{hc},
\qquad
\tilde{\nu}_{ua}-\tilde{\nu}_{ub}=\frac{E_b-E_a}{hc}.
```

A useful measurement model is

```math
S_{\mathrm{det}}(\lambda)=
[\eta(\lambda)S_{\mathrm{source}}(\lambda)]*G_{\mathrm{inst}}(\lambda)
+b(\lambda),
```

where $`\eta`$ represents spectral sensitivity, $`G_{\mathrm{inst}}`$ the instrumental profile and $`b`$ the background. Reference assignments and calibration standards are evidence entering the inference, not conclusions obtained from peak positions alone.

**Syllabus coverage.** Synthesis of quantum states, coupling, selection rules, intensities and widths, with external-field and molecular examples available for comparison. This unit adds no large theoretical topic.

**Closing connection.** Return to Unit 0: explain what was recorded, which model connected the signal to microscopic structure, what was inferred and which further measurement could resolve the remaining uncertainty.

## Working reconciliation — remove once restructuring is complete

This is the proposed restructuring following inspection of commit `a0164bc`. Numerical analyses have not been rerun; existing claims of calculation or agreement are not independent verification.

### Current files and lectures

| Current material | Destination and action |
|---|---|
| [Course README](README.md) | **Done:** navigation follows Units 0–8 and links this map; references and conventions are kept. The seven-step pattern is described as that of the lectures written so far, and a missing dataset no longer holds up a unit. |
| [Former Lecture 0](reading-spectroscopy-as-response.md) | The course entrance is now the written [Unit 0](unit-0-learning-from-measurements.md). **Done:** retitled as optional response-theory reading attached to Unit 5 (Lorentz oscillator, polarizability, oscillator strengths, Kubo formula, sum rule and Kramers–Kronig relations), with sections renumbered R.1–R.8 and unit references updated to this map. Revise it further when Unit 5 is developed. |
| [Unit 1](unit-1-hydrogen.md), Lectures 1–3 | Keep in Unit 1: spectral series; Franck–Hertz and reduced mass; quantum states. Keep selection rules and lifetime contrasts as explicitly basic previews of Unit 5. |
| [Unit 2](unit-2-spin-fine-hyperfine.md), Lectures 4–6 | Keep in Unit 2: spin; fine structure; hyperfine structure and isotope shifts. Keep sodium as an illustrative single-valence-electron example before its fuller explanation in Unit 3. |
| [Unit 3](unit-3-many-electron-atoms.md), Lectures 7–9 | Keep alkali spectra, helium and coupling in Unit 3; arrange helium, alkalis and coupling into a continuous argument. Keep rare-earth moments as an optional application after Unit 4 introduces the Landé factor. |
| Former Unit 3, Lecture 10 | **Done:** moved with its problems, answers, sources and `line-shapes.svg` to [Unit 5](unit-5-light-matter-interaction.md). Earlier units need only enough resolution context to explain why splittings may be hidden. |
| README’s planned Lectures 11–13 | Develop in Unit 4: Zeeman/Paschen–Back, Stark, ESR/NMR and chemical shift. These are currently plans, not written units. |
| README’s planned Lectures 14–15 | Divide between Unit 6’s molecular potentials and nuclear levels and Unit 7’s rotational/infrared transitions and bands. |
| README’s planned Lectures 16–17 | Develop Raman and electronic/Franck–Condon spectroscopy in Unit 7. |
| README’s planned Lectures 18–20 | Develop Einstein coefficients, pumping, inversion, rate equations, resonators and coherence in Unit 5. |
| [Worked lamp example](worked-example-raw-spectrum.md) | Rework as Unit 8’s principal example, preceded by individual Hg, Cd and Ar spectra. Preserve its useful Ritz reconstruction and explicit calibration limitation. |
| [Top-level README](../README.md) | **Done:** the Atomic and Molecular Physics introduction, entry link and progress description match the new course. |

Old lecture numbers above identify existing material. Use unit and section numbers in the revised course; update lecture-number references, figure captions and links together. Replace repetitive compulsory “In response language” endings with physically useful connections to the next question.

Retain the present asset directories:

- **Units 1–3:** keep the hydrogen, sodium, helium and coupling figures with their corresponding discussions. Label diagrams and plots from tabulated values accurately.
- **Unit 5:** associate `lorentz-response.svg`, `oscillator-strengths.svg` and `line-shapes.svg` with transitions, response and broadening.
- **Unit 8:** retain the two lamp-spectrum figures and `cadmium-levels-from-lines.svg`, together with both CSV files, the optional analysis script and `PypeIt-LICENSE.txt`. The notes must explain the inference without requiring Python.

### Coverage still to develop

The written units provide substantial atomic-structure material through Unit 3, and Unit 5 already holds the lecture on line widths. External fields and magnetic resonance are largely only planned. Einstein coefficients and selection rules appear in existing notes, but the connected treatment of optical processes and lasers remains to be written. Molecular structure and spectroscopy are currently README outlines.

The repository contains a mixed measured lamp spectrum, but no separate measured hydrogen, Hg, Cd or Ar spectra. `balmer-spectrum.svg` is a line-position illustration, not a measured intensity trace. Source a properly attributed single-element record for Unit 0 and individual-element examples for Unit 8; do not manufacture experimental traces or present selected lines from the mixture as separately measured spectra.

### Scientific concerns to address during restructuring

- **Scope of atomic models.** In Unit 2, describe Hα’s apparent “doublet” as prominent groups within a spectrum containing several allowed components, and state the approximations used.
- **Strengths and populations.** In Unit 8’s lamp example, distinguish integrated photon counts, emitted power and peak heights before applying frequency factors or attributing discrepancies to detector sensitivity.
- **Limits of the archived analysis.** In Unit 8, review blends, background treatment, clipping and uncertainties before retaining precision claims. Agreement on a scale calibrated from reference lines cannot independently validate those same reference wavelengths.
- **Coherence and beating.** In Unit 5, separate the sodium doublet’s periodic two-frequency beating from the coherence envelope set by each component’s width.
