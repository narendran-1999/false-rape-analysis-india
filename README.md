
# False Rape Analysis India

Data Analysis project on **False Rape Cases in India**, with aim to estimate percentage of false cases and its trend from 2016 to 2022

## Data Source

**NCRB (National Crime Records Bureau) "Crime in India" reports 2016 - 2022**  
**Volume 1 - Chapter 3A (Crimes Against Women - All India)**.  

**Tables:**  
- Police Disposal
- Court Disposal

Link to reports: [NCRB Crime in India Year-wise Reports](https://ncrb.gov.in/crime-in-india-year-wise.html?year=2022).  

## Methodology of Analysis

### Which categories are considered fake?  

**Final Report False** - Filed after confirming bogus report  
  
**Mistake of Fact or of Law or Civil Dispute** - Filed after confirming exaggeration or misinterpretation of incident by complainant, or a false allegation filed over civil dispute.  
  
Both final reports are filed by police with approval from court.  

  
### Faulty convictions and Miscategorization  

- Faulty conviction data wasn't available in official sources
- Faulty convictions are rare incidents, similar to incidences of miscategorization on part of police
- Both rare incidences nullify the effect of each other on the estimate

Thus the numbers in *Mistake of Fact or of Law or Civil Dispute* and *Convicted* are left as they are.

### FAQs  
  
1. **If false case get resolved quick, wouldn't they accumulate more than convicted ones?**
   The genuinity of the case has no effect on how quick it reaches resolution, or on whether it results in _acquiittal due to lack of evidence_ or _a solid conclusion (fake or true)_.
   
2. 

  
## Files

- **Fake_Rape_DataVis.ipynb**: Jupyter notebook containing visualizations and exploratory data analysis of related data.
- **datavis-rape.py**: Python script used for data visualization and analysis.
- **rape.csv**: Dataset in CSV format containing extracted data on false rape cases.
- **requirements.txt**: Lists the Python dependencies needed to run the analysis.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/narendran-1999/false-rape-analysis-india.git
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- **Jupyter Notebook**: Open `Fake_Rape_DataVis.ipynb` in a Jupyter environment to explore the data and visualize trends.
- **Python Script**: Run `datavis-rape.py` to perform analysis and generate visualizations in a script-based environment.

```bash
python datavis-rape.py
```

## License

This project is licensed under the MIT License.
