# DNA and Protein Sequence Operations using Biopython

This project demonstrates essential bioinformatics operations on DNA and protein sequences using the [Biopython](https://biopython.org/) library. It includes functionalities such as:

- Generating the reverse complement of a DNA sequence
- Transcribing DNA to RNA
- Translating DNA to a protein sequence
- Calculating the molecular weight of a protein

## Features

✅ Reverse complement of a DNA sequence  
✅ Transcription of DNA to RNA  
✅ Translation of DNA to protein  
✅ Molecular weight calculation for a protein sequence  

---

## 🧬 Code Overview

### 1. Reverse Complement of DNA
Generates the reverse complement of a given DNA sequence using `Seq.reverse_complement()`.

### 2. Transcription to RNA
Converts DNA to RNA using `Seq.transcribe()`.

### 3. Translation to Protein
Translates a DNA sequence into a protein using `Seq.translate()`.

### 4. Protein Molecular Weight
Calculates the molecular weight of a given protein using `molecular_weight()` from `Bio.SeqUtils`.

---

## 🔧 Requirements

- Python 3.6+
- [Biopython](https://biopython.org/)

### Install Biopython

```bash
pip install biopython
```

---

## 🚀 How to Run

1. Clone or download this repository.
2. Make sure you have Python and Biopython installed.
3. Run the script:

```bash
python main.py
```

---

## 📂 Example Output

```text
Original DNA Sequence:      ATGCGTAC
Reverse Complement:         GTACGCAT
RNA Sequence:               AUGGCCAAUUG
Protein Sequence:           MAIVMGR*KGAR*
Molecular Weight of Protein: 5225.90 Da
```

---

## 📚 References

- [Biopython Documentation](https://biopython.org/wiki/Documentation)
- [Biopython Tutorial and Cookbook](https://biopython.org/DIST/docs/tutorial/Tutorial.html)

---

## 📄 License

This project is open-source and available under the MIT License.
