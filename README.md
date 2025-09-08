# Hybrid Solar–Hydro Powered Greywater Treatment (OpenModelica Simulation)

This project demonstrates a simple simulation of a **Hybrid Solar–Hydro Greywater Treatment System** using OpenModelica.  
The model combines greywater flow from a building, a micro-hydro turbine, and solar PV to power UV disinfection and pumping.

---

## 🚀 Project Features
- Greywater tank with 150 liters per floor
- Micro-hydro generator producing power from greywater discharge
- Solar PV providing additional renewable energy
- UV disinfection and pumping system as electrical load
- Net power balance analysis (Solar + Hydro – Load)

---

## 📂 Repository Structure
```
Hybrid-Greywater-OpenModelica/
│── GreywaterHybrid.mo        # Main OpenModelica model
│── README.md                 # Documentation
│── docs/                     # Additional explanations
│── plots/                    # Output figures from simulations
└── python/                   # Python scripts for post-processing
```

---

## ⚙️ How to Run the Model
1. Open **OpenModelica (OMEdit)**.
2. Load the file `GreywaterHybrid.mo`.
3. Simulate the model to calculate **HydroPower** and **NetPower**.
4. Results can be visualized or exported for analysis.

---

## 🐍 Python Post-Processing
A Python script is provided (`python/analyze_results.py`) to analyze and visualize data, e.g., Net Power vs Flow Rate.

Run with:
```bash
python analyze_results.py
```

---

## 📝 Citation
If you use this project, please cite:

> Zeraatpisheh, Parsa. *Hybrid Solar–Hydro Powered Greywater Treatment Simulation in OpenModelica*. (Educational Project, 2025).

---

## 👤 Author
**Parsa Zeraatpisheh**  
- Email: parsazeraatpisheh2001@gmail.com  
- GitHub: [github.com/parsazrp](https://github.com/parsazrp)
