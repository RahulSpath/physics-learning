# Physics Learning

Study material for sharpening physics problem solving, with a focus on theoretical condensed matter.

## Atomic and Molecular Physics, Data First

**Read the notes:** [atomic-molecular-physics/](atomic-molecular-physics/README.md)

Lecture notes for Section VII of the CSIR-UGC NET Physical Sciences syllabus. Each topic starts from real textbook data and builds the theory needed to explain it. Lecture 0 (spectroscopy as linear response) and Units 1–3 (the hydrogen atom; spin, fine and hyperfine structure; many-electron atoms) are written; Units 4–6 are planned. A [worked example](atomic-molecular-physics/worked-example-raw-spectrum.md) goes from a real lamp spectrum to energy levels, with the data and a Python script to repeat it.

## Condensed Matter Scales

**Open the page:** https://rahulspath.github.io/physics-learning/

A pocket reference of the relations and typical numbers worth knowing by heart:

- Ten anchor numbers, and a conversion table between eV, K, THz, cm⁻¹ and tesla
- An energy ladder from μeV to 10 eV, showing what physics happens at each scale
- Specific-heat laws for electrons, phonons, magnons, Dirac and Weyl systems, superconductors and glasses
- Typical scales for metals, transport, semiconductors, phonons, magnetism, superconductivity, quantum Hall and mesoscopic physics, and correlated and moiré materials
- Time scales, critical exponents, and a checklist of derivations to work through

To quiz yourself, switch to **Hide values** or **Hide relations** at the top of the page, then tap a hidden entry to check it. When you miss one, derive it instead of rereading it.

## How to solve a problem

1. Draw it. Define coordinates, including signs and the origin, and count the degrees of freedom.
2. Write the governing law in full (Newton, Lagrangian or Hamiltonian), with every term.
3. Build each term from first principles instead of recalling a formula.
4. Check the equation before solving it: units, limits and symmetry.
5. Classify the equation (oscillator, separable, energy-integrable, linear with constant coefficients).
6. Solve it.
7. Check the answer: units, limits, and whether its size is reasonable.

## Daily routine

- **Mon, Wed, Fri:** one fundamentals problem, rotating through mechanics, E&M, quantum mechanics and statistical mechanics
- **Tue, Thu:** one condensed matter problem
- **Sat:** one closed-book derivation from the checklist on the page
- **Sun:** review the error log

## Files

- `index.html`: the Condensed Matter Scales page. It is a single self-contained file, so you can also download it and open it in any browser.
